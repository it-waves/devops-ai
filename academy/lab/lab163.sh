#!/bin/sh
# Lesson 163 lab: the Jenkins mastery scenario. Seven checks prove your release pipeline works.
# Usage: lab163.sh up | check | backup | down      Own machine only. Needs the Jenkins from lesson 155, curl, tar and Java.
# Set JENKINS_URL (default http://localhost:8080), JENKINS_AUTH (user:password or user:token) and JENKINS_HOME.
U=${JENKINS_URL:-http://localhost:8080}; A=${JENKINS_AUTH:-admin:devops-lab}; J=${JENKINS_HOME:-$HOME/.jenkins}
B=$HOME/jenkins-lab163; JOB=cloudcart-mastery; CRED=release-bot; TMP=${TMPDIR:-/tmp}/lab163.$$
api() { curl -s -m 10 -u "$A" "$U/$1"; }
case "$1" in
up) mkdir -p $B/backups
  curl -s -o /dev/null -m3 "$U/login" && echo "Jenkins answers at $U" || echo "Jenkins is NOT answering at $U"
  [ -d "$J" ] && echo "Jenkins home: $J" || echo "Set JENKINS_HOME to your Jenkins home folder"
  echo "Scenario job: $JOB    Credential id: $CRED"; echo "Results go to $B/results.txt";;
check) mkdir -p $B/backups; P=0; N=0; OUT=$B/results.txt; : > $OUT
  if [ -t 1 ]; then G='\033[1;92m'; R='\033[1;91m'; W='\033[1;97m'; Z='\033[0m'; else G=; R=; W=; Z=; fi
  t() { N=$((N+1)); if [ "$1" = ok ]; then P=$((P+1)); L="PASS  $N  $2"; C=$G; else L="FAIL  $N  $2  -> $3"; C=$R; fi; printf '%b%s%b\n' "$C" "$L" "$Z"; echo "$L" >> $OUT; }
  api "api/json" | grep -q '"mode"' && t ok "Jenkins answers and the login works" || t no "Jenkins answers and the login works" "start Jenkins, check JENKINS_AUTH"
  api "job/$JOB/api/json" | grep -q '"name":"'$JOB'"' && t ok "Job $JOB exists" || t no "Job $JOB exists" "create a Pipeline job with this exact name"
  api "job/$JOB/lastBuild/api/json" | grep -q '"result":"SUCCESS"' && t ok "Last build is SUCCESS" || t no "Last build is SUCCESS" "open the console, read the first error"
  api "job/$JOB/lastBuild/api/json" | grep -q '"relativePath"' && t ok "An artifact is archived" || t no "An artifact is archived" "add archiveArtifacts to the pipeline"
  api "job/$JOB/lastBuild/consoleText" > $TMP
  grep -q "Approved by" $TMP && t ok "A person approved the release" || t no "A person approved the release" "add an input step and approve it"
  if grep -q '\*\*\*\*' $TMP && ! grep -q 'releasing as .* with [^*]' $TMP; then t ok "The secret is masked in the log"; else t no "The secret is masked in the log" "use withCredentials, never echo plain text"; fi
  rm -f $TMP
  tar tzf $B/backups/jenkins-backup.tgz 2>/dev/null | grep -q "jobs/$JOB/config.xml" && t ok "A backup holds the job" || t no "A backup holds the job" "run: lab163.sh backup"
  printf '%bRESULT: %s of %s checks pass%b\n' "$W" $P $N "$Z"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P = $N ];;
backup) mkdir -p $B/backups; F=$B/backups/jenkins-backup.tgz
  tar czf $F --exclude=workspace --exclude=caches -C "$J" . && ls -lh $F
  echo "Now copy it to another disk or server. A copy on the same disk is not a backup.";;
down) CJ=$TMP.cj; CR=$(curl -s -c $CJ -u "$A" "$U/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,%22:%22,//crumb)")
  curl -s -b $CJ -u "$A" -H "$CR" -X POST "$U/job/$JOB/doDelete" -o /dev/null -w "delete job: %{http_code}\n"
  curl -s -b $CJ -u "$A" -H "$CR" -X POST "$U/manage/credentials/store/system/domain/_/credential/$CRED/doDelete" -o /dev/null -w "delete credential: %{http_code}\n"
  rm -rf $B $CJ; echo "Scenario job, credential and lab files removed. Jenkins itself is untouched.";;
*) echo "usage: lab163.sh up|check|backup|down";;
esac
