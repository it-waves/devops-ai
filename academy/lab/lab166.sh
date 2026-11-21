#!/bin/sh
# Lesson 166 lab: check that your Maven project was scanned by your own SonarQube. Own machine only.
# Usage: lab166.sh check     Env: SONAR_URL (default http://localhost:9000), SONAR_TOKEN (your analysis token), SONAR_KEY (project key, default cloudcart)
U=${SONAR_URL:-http://localhost:9000}; K=${SONAR_KEY:-cloudcart}; OUT=${SONAR_OUT:-./results166.txt}; P=0; N=4
ok() { P=$((P+1)); if [ -t 1 ]; then printf '\033[1;92mPASS\033[0m  %s\n' "$1"; else echo "PASS  $1"; fi; echo "PASS  $1" >> $OUT; }
no() { if [ -t 1 ]; then printf '\033[1;91mFAIL\033[0m  %s\n' "$1"; else echo "FAIL  $1"; fi; echo "FAIL  $1" >> $OUT; }
case "$1" in
check) : > $OUT
 V=$(curl -s -u "$SONAR_TOKEN:" $U/api/authentication/validate); case "$V" in *'"valid":true'*) ok "the token is valid";; *) no "the token is valid (is SONAR_TOKEN set?)";; esac
 C=$(curl -s -u "$SONAR_TOKEN:" "$U/api/components/show?component=$K"); case "$C" in *'"key":"'$K'"'*) ok "project $K exists on the server";; *) no "project $K exists on the server";; esac
 A=$(curl -s -u "$SONAR_TOKEN:" "$U/api/project_analyses/search?project=$K&ps=1"); case "$A" in *'"key"'*'"date"'*) ok "at least one analysis was uploaded";; *) no "at least one analysis was uploaded";; esac
 L=$(curl -s -u "$SONAR_TOKEN:" "$U/api/measures/component?component=$K&metricKeys=ncloc" | sed 's/.*"value":"\([0-9]*\)".*/\1/'); case "$L" in ''|*[!0-9]*) L=0;; esac
 [ "$L" -gt 0 ] && ok "SonarQube counted $L lines of code" || no "SonarQube counted lines of code"
 echo "RESULT: $P of $N checks pass"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P -eq $N ];;
*) echo "usage: lab166.sh check";;
esac
