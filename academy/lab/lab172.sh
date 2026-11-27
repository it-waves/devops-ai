#!/bin/sh
# Lesson 172 lab: the SonarQube mastery scenario. Seven checks prove your quality pipeline works. Own machine only.
# Usage: lab172.sh up | check | down      Run "check" and "down" inside your CloudCart repository (the check looks for tokens in its files).
# Env (never stored in a file): SONAR_TOKEN = your own SonarQube USER token (administrator), JENKINS_AUTH = Jenkins user:token
# Optional: SONAR_URL (default http://localhost:9000), JENKINS_URL (default http://localhost:8080), JOB and PROJECT (default cloudcart-mastery), GATE (default "Cloud Cart gate")
S=${SONAR_URL:-http://localhost:9000}; J=${JENKINS_URL:-http://localhost:8080}; JOB=${JOB:-cloudcart-mastery}; PRJ=${PROJECT:-$JOB}; GATE=${GATE:-Cloud Cart gate}
OUT=${SONAR_OUT:-./results172.txt}; P=0; N=0
sq() { curl -s -m 10 -u "$SONAR_TOKEN:" "$@"; }
jk() { curl -s -m 10 -u "$JENKINS_AUTH" "$@"; }
need() { [ -n "$SONAR_TOKEN" ] && [ -n "$JENKINS_AUTH" ] || { echo "Set SONAR_TOKEN (your user token) and JENKINS_AUTH (user:token) first"; exit 2; }; }
case "$1" in
up) need
 curl -s -m 5 "$S/api/system/status" | grep -q '"status":"UP"' && echo "SonarQube is UP at $S" || echo "SonarQube is NOT up at $S (run sonar.sh start and wait for UP)"
 curl -s -o /dev/null -m 5 "$J/login" && echo "Jenkins answers at $J" || echo "Jenkins is NOT answering at $J"
 echo "Scenario: job $JOB, project $PRJ, gate \"$GATE\" (coverage on overall code must not be below 62)"; echo "Results go to $OUT";;
check) need; : > $OUT
 if [ -t 1 ]; then G='\033[1;92m'; R='\033[1;91m'; W='\033[1;97m'; Z='\033[0m'; else G=; R=; W=; Z=; fi
 t() { N=$((N+1)); if [ "$1" = ok ]; then P=$((P+1)); L="PASS  $N  $2"; C=$G; else L="FAIL  $N  $2  -> $3"; C=$R; fi; printf '%b%s%b\n' "$C" "$L" "$Z"; echo "$L" >> $OUT; }
 curl -s -m 5 "$S/api/system/status" | grep -q '"status":"UP"' && t ok "SonarQube is UP" || t no "SonarQube is UP" "run sonar.sh start, wait for UP"
 sq -G "$S/api/qualitygates/show" --data-urlencode "name=$GATE" | grep -q '"metric":"coverage","op":"LT","error":"62"' && t ok "Gate \"$GATE\" requires coverage of 62" || t no "Gate \"$GATE\" requires coverage of 62" "copy Sonar way, add coverage 62"
 sq "$S/api/webhooks/list" | grep -q 'sonarqube-webhook' && t ok "A web hook calls Jenkins back" || t no "A web hook calls Jenkins back" "Administration, Web hooks, create one"
 CV=$(sq -G "$S/api/measures/component" -d component=$PRJ -d metricKeys=coverage | sed -n 's/.*"value":"\([0-9.]*\)".*/\1/p')
 [ -n "$CV" ] && [ "$(echo "$CV >= 62" | bc -l 2>/dev/null || awk -v c="$CV" 'BEGIN{print (c>=62)}')" = 1 ] && t ok "Coverage is $CV (62 or more)" || t no "Coverage is ${CV:-unknown} (62 or more)" "add tests, scan again"
 sq -G "$S/api/qualitygates/project_status" -d projectKey=$PRJ | grep -q '"status":"OK"' && t ok "The quality gate for $PRJ is OK" || t no "The quality gate for $PRJ is OK" "read the failing condition"
 jk "$J/job/$JOB/lastBuild/api/json" | grep -q '"result":"SUCCESS"' && t ok "The last Jenkins build is SUCCESS" || t no "The last Jenkins build is SUCCESS" "open the console, read the first error"
 if git grep -qE 'sq[apu]_[A-Za-z0-9]{20,}' 2>/dev/null; then t no "No token in the code" "run leakcheck, remove it, revoke it"; else t ok "No token in the code"; fi
 printf '%bRESULT: %s of %s checks pass%b\n' "$W" $P $N "$Z"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P = $N ];;
down) need
 [ -f "$OUT" ] && grep -q "RESULT: 7 of 7" "$OUT" && cp "$OUT" "${OUT%.txt}-evidence.txt" && echo "Evidence kept: ${OUT%.txt}-evidence.txt"
 sq -X POST "$S/api/projects/delete" -d project=$PRJ -o /dev/null -w "delete project: %{http_code}\n"
 WK=$(sq "$S/api/webhooks/list" | tr '{' '\n' | grep sonarqube-webhook | sed -n 's/.*"key":"\([^"]*\)".*/\1/p' | head -1)
 [ -n "$WK" ] && sq -X POST "$S/api/webhooks/delete" -d webhook=$WK -o /dev/null -w "delete web hook: %{http_code}\n"
 sq -X POST "$S/api/qualitygates/select" -d gateName="Sonar way" -d projectKey=$PRJ -o /dev/null 2>/dev/null
 sq -X POST "$S/api/qualitygates/set_as_default" -d name="Sonar way" -o /dev/null
 sq -X POST "$S/api/qualitygates/destroy" -d name="$GATE" -o /dev/null -w "delete gate: %{http_code}\n"
 CJ=${TMPDIR:-/tmp}/lab172.$$.cj; CR=$(curl -s -c $CJ -u "$JENKINS_AUTH" "$J/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,%22:%22,//crumb)")
 curl -s -b $CJ -u "$JENKINS_AUTH" -H "$CR" -X POST "$J/job/$JOB/doDelete" -o /dev/null -w "delete job: %{http_code}\n"; rm -f $CJ
 echo "Scenario project, web hook, gate and job removed. SonarQube and Jenkins themselves are untouched. Revoke any token you used, in My Account, Security.";;
*) echo "usage: lab172.sh up|check|down";;
esac
