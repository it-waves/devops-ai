#!/bin/sh
# Lesson 170 lab: check tokens and permissions. Own machine only.
# Usage: lab170.sh check   (run it inside your CloudCart repository)
# Env (required, never stored in a file): ANALYSIS_TOKEN = your CI analysis token, SONAR_TOKEN = your own SonarQube USER token, JENKINS_AUTH = Jenkins user:token
# Optional: SONAR_URL (default http://localhost:9000), JENKINS_URL (default http://localhost:8080), JOB (default cloudcart-quality)
S=${SONAR_URL:-http://localhost:9000}; J=${JENKINS_URL:-http://localhost:8080}; JOB=${JOB:-cloudcart-quality}
OUT=${SONAR_OUT:-./results170.txt}; P=0; N=4
ok() { P=$((P+1)); if [ -t 1 ]; then printf '\033[1;92mPASS\033[0m  %s\n' "$1"; else echo "PASS  $1"; fi; echo "PASS  $1" >> $OUT; }
no() { if [ -t 1 ]; then printf '\033[1;91mFAIL\033[0m  %s\n' "$1"; else echo "FAIL  $1"; fi; echo "FAIL  $1" >> $OUT; }
code() { curl -s -m 10 -o /dev/null -w '%{http_code}' -u "$1:" "$S/api/webhooks/list"; }
case "$1" in
check) : > $OUT
 [ -n "$ANALYSIS_TOKEN" ] && [ -n "$SONAR_TOKEN" ] && [ -n "$JENKINS_AUTH" ] || { echo "Set ANALYSIS_TOKEN, SONAR_TOKEN and JENKINS_AUTH first"; exit 2; }
 [ "$(code "$SONAR_TOKEN")" = 200 ] && ok "Your user token can administer (list webhooks)" || no "Your user token can administer (check SONAR_TOKEN)"
 [ "$(code "$ANALYSIS_TOKEN")" != 200 ] && ok "The CI analysis token is refused for administration" || no "The CI analysis token is refused for administration (it is too powerful: make a Project Analysis Token)"
 git grep -qE 'sq[apu]_[A-Za-z0-9]{20,}' 2>/dev/null && no "No token in the code (TOKEN FOUND)" || ok "No token in the code"
 curl -s -m 10 -u "$JENKINS_AUTH" "$J/job/$JOB/lastBuild/api/json" | grep -q '"result":"SUCCESS"' && ok "The last Jenkins build is SUCCESS (the CI token works)" || no "The last Jenkins build is SUCCESS (update the Jenkins credential)"
 echo "RESULT: $P of $N checks pass"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P -eq $N ];;
*) echo "usage: lab170.sh check";;
esac
