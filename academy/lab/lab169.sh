#!/bin/sh
# Lesson 169 lab: check that Jenkins runs the SonarQube scan and waits for the quality gate. Own machine only.
# Usage: lab169.sh check
# Env: JENKINS_AUTH (your Jenkins user:token, required), JENKINS_URL (default http://localhost:8080), JOB (default cloudcart-quality),
#      SONAR_URL (default http://localhost:9000), SONAR_TOKEN (your own SonarQube USER token, needed to list webhooks). Never store them in a file.
J=${JENKINS_URL:-http://localhost:8080}; A=$JENKINS_AUTH; JOB=${JOB:-cloudcart-quality}; S=${SONAR_URL:-http://localhost:9000}
OUT=${SONAR_OUT:-./results169.txt}; P=0; N=4
ok() { P=$((P+1)); if [ -t 1 ]; then printf '\033[1;92mPASS\033[0m  %s\n' "$1"; else echo "PASS  $1"; fi; echo "PASS  $1" >> $OUT; }
no() { if [ -t 1 ]; then printf '\033[1;91mFAIL\033[0m  %s\n' "$1"; else echo "FAIL  $1"; fi; echo "FAIL  $1" >> $OUT; }
case "$1" in
check) : > $OUT
 [ -n "$A" ] || { echo "Set JENKINS_AUTH first (user:token)"; exit 2; }
 curl -s -m 10 -u "$A" "$J/api/json" | grep -q '"mode"' && ok "Jenkins answers and the login works" || no "Jenkins answers and the login works (check JENKINS_AUTH)"
 curl -s -m 10 -u "$SONAR_TOKEN:" "$S/api/webhooks/list" | grep -q '/sonarqube-webhook/' && ok "SonarQube has a webhook to Jenkins" || no "SonarQube has a webhook to Jenkins (Administration, Configuration, Webhooks)"
 L=$(curl -s -m 20 -u "$A" "$J/job/$JOB/lastBuild/consoleText")
 echo "$L" | grep -q "Quality gate is" && ok "The last build waited for the quality gate" || no "The last build waited for the quality gate (add waitForQualityGate)"
 curl -s -m 10 -u "$A" "$J/job/$JOB/lastBuild/api/json" | grep -q '"result":"SUCCESS"' && ok "The last build is SUCCESS (the gate passed)" || no "The last build is SUCCESS (the gate passed)"
 echo "RESULT: $P of $N checks pass"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P -eq $N ];;
*) echo "usage: lab169.sh check";;
esac
