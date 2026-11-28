#!/bin/sh
# Lesson 179 lab: prove the CloudCart pipeline. Seven checks. Own machine only, lab servers only.
# Usage: lab179.sh up | check | stats | down      Run "check" inside your CloudCart project folder (check 7 scans its files).
# Env (never stored in a file): JENKINS_AUTH = user:token   NEXUS_USER and NEXUS_PASSWORD = your deployer account
# Optional: JENKINS_URL (http://localhost:8080)  NEXUS_URL (http://localhost:8081)  CI_JOB (cloudcart-ci)  PROMOTE_JOB (cloudcart-promote)
#           DEV_PORT 9101  STAGE_PORT 9102  LIVE_PORT 9100  BLUE_PORT 9103  GREEN_PORT 9104  REPO_REL (cloudcart-releases)
JU=${JENKINS_URL:-http://localhost:8080}; NU=${NEXUS_URL:-http://localhost:8081}; CI=${CI_JOB:-cloudcart-ci}; PJ=${PROMOTE_JOB:-cloudcart-promote}
DEV=${DEV_PORT:-9101}; STG=${STAGE_PORT:-9102}; LIVE=${LIVE_PORT:-9100}; BLUE=${BLUE_PORT:-9103}; GREEN=${GREEN_PORT:-9104}; REPO=${REPO_REL:-cloudcart-releases}
OUT=${LAB_OUT:-./results179.txt}; P=0; N=0; BASE=$NU/repository/$REPO/academy/cloudcart/cloudcart
jk() { curl -g -s -m 15 -u "$JENKINS_AUTH" "$@"; }
nx() { curl -g -s -m 15 -u "$NEXUS_USER:$NEXUS_PASSWORD" "$@"; }
ver() { curl -s -m 5 localhost:$1/cloudcart/health | sed -n 's/.*"version":"\([^"]*\)".*/\1/p'; }
need() { [ -n "$JENKINS_AUTH" ] && [ -n "$NEXUS_USER" ] && [ -n "$NEXUS_PASSWORD" ] || { echo "Set JENKINS_AUTH (user:token), NEXUS_USER and NEXUS_PASSWORD first"; exit 2; }; }
case "$1" in
up) need
 [ "$(jk -o /dev/null -w '%{http_code}' $JU/api/json)" = 200 ] && echo "Jenkins is UP at $JU" || echo "Jenkins is NOT up at $JU"
 [ "$(curl -s -o /dev/null -m 5 -w '%{http_code}' $NU/service/rest/v1/status)" = 200 ] && echo "Nexus is UP at $NU" || echo "Nexus is NOT up at $NU"
 echo "Environments: dev $DEV, stage $STG, live (router) $LIVE, blue $BLUE, green $GREEN"; echo "Results go to $OUT";;
stats) need
 jk "$JU/job/$CI/api/json?tree=builds[number,result,duration]{0,10}" | python3 -c '
import json,sys
b=[x for x in json.load(sys.stdin)["builds"] if x["result"]]
ok=[x for x in b if x["result"]=="SUCCESS"]
for x in reversed(b): print("build %-3s %-8s %3d s" % (x["number"], x["result"], round(x["duration"]/1000)))
print("SUCCESS RATE: %d of %d builds, %d%%" % (len(ok), len(b), round(100*len(ok)/len(b))))
print("AVERAGE DURATION: %d s" % round(sum(x["duration"] for x in ok)/len(ok)/1000))';;
check) need; : > $OUT
 if [ -t 1 ]; then G='\033[1;92m'; R='\033[1;91m'; W='\033[1;97m'; Z='\033[0m'; else G=; R=; W=; Z=; fi
 t() { N=$((N+1)); if [ "$1" = ok ]; then P=$((P+1)); LN="PASS  $N  $2"; CL=$G; else LN="FAIL  $N  $2  -> $3"; CL=$R; fi; printf '%b%s%b\n' "$CL" "$LN" "$Z"; echo "$LN" >> $OUT; }
 J=$(jk "$JU/api/json?tree=jobs[name]"); echo "$J" | grep -q "\"$CI\"" && echo "$J" | grep -q "\"$PJ\"" && t ok "Jenkins is up and has both jobs" || t no "Jenkins is up and has both jobs" "start Jenkins, create the CI and promote jobs"
 LB=$(jk "$JU/job/$CI/lastBuild/api/json"); echo "$LB" | grep -q '"result":"SUCCESS"' && jk "$JU/job/$CI/lastBuild/consoleText" | grep -q 'Smoke test' && t ok "The last CI build is green and ran the smoke test" || t no "The last CI build is green and ran the smoke test" "open the console, read the FIRST error"
 LS=$(jk "$JU/job/$CI/lastSuccessfulBuild/buildNumber"); V=1.0.$LS; S1=$(nx $BASE/$V/cloudcart-$V.war.sha1); S2=$(nx $BASE/$V/cloudcart-$V.war | sha1sum | cut -d' ' -f1)
 [ -n "$LS" ] && [ -n "$S1" ] && [ "$S1" = "$S2" ] && t ok "Release $V matches its checksum in Nexus" || t no "Release $V matches its checksum in Nexus" "401: Nexus password. 404: that version was never published"
 D=$(ver $DEV); S=$(ver $STG); L=$(ver $LIVE); [ -n "$D" ] && [ -n "$S" ] && [ -n "$L" ] && t ok "Dev, stage and production all answer (dev $D, stage $S, live $L)" || t no "Dev, stage and production all answer" "no answer: is that Tomcat running? port $DEV, $STG, $LIVE"
 [ -n "$L" ] && [ "$(nx -o /dev/null -w '%{http_code}' $BASE/$L/cloudcart-$L.war.sha1)" = 200 ] && t ok "Production runs a version that is in Nexus ($L)" || t no "Production runs a version that is in Nexus" "production runs a file nobody can trace"
 NV=$(nx "$NU/service/rest/v1/search?repository=$REPO&group=academy.cloudcart&name=cloudcart" | grep -o '"version" *: *"[^"]*"' | sort -u | wc -l); B=$(ver $BLUE); GR=$(ver $GREEN)
 [ "$NV" -ge 2 ] && [ -n "$B" ] && [ -n "$GR" ] && t ok "Rollback is ready: $NV releases in Nexus, blue $B, green $GR" || t no "Rollback is ready" "keep two sides up and at least two releases"
 if grep -rIqE '(PASSWORD|password)[[:space:]]*[=:][[:space:]]*["'"'"']?[A-Za-z0-9]' --exclude-dir=.git --exclude-dir=target --exclude='results*' . 2>/dev/null; then t no "No password in the code" "remove the file, and change the password"; else t ok "No password in the code"; fi
 printf '%bRESULT: %s of %s checks pass%b\n' "$W" $P $N "$Z"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P = $N ];;
down) need
 [ -f "$OUT" ] && grep -q "RESULT: 7 of 7" "$OUT" && cp "$OUT" "${OUT%.txt}-evidence.txt" && echo "Evidence kept: ${OUT%.txt}-evidence.txt"
 rm -f /tmp/cloudcart-*.war; echo "Temporary files removed. Jenkins, Nexus, jobs and servers stay."; echo "Change any password you typed in plain text.";;
*) echo "usage: lab179.sh up|check|stats|down";;
esac
