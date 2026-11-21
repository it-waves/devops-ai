#!/bin/sh
# Lesson 167 lab: read your SonarQube results and check that coverage and history are there. Own machine only.
# Usage: lab167.sh check     Env: SONAR_URL (default http://localhost:9000), SONAR_TOKEN (your user token), SONAR_KEY (project key, default cloudcart)
U=${SONAR_URL:-http://localhost:9000}; K=${SONAR_KEY:-cloudcart}; OUT=${SONAR_OUT:-./results167.txt}; P=0; N=4
ok() { P=$((P+1)); if [ -t 1 ]; then printf '\033[1;92mPASS\033[0m  %s\n' "$1"; else echo "PASS  $1"; fi; echo "PASS  $1" >> $OUT; }
no() { if [ -t 1 ]; then printf '\033[1;91mFAIL\033[0m  %s\n' "$1"; else echo "FAIL  $1"; fi; echo "FAIL  $1" >> $OUT; }
m() { curl -s -u "$SONAR_TOKEN:" "$U/api/measures/component?component=$K&metricKeys=$1" | sed -n 's/.*"value":"\([0-9.]*\)".*/\1/p'; }
case "$1" in
check) : > $OUT
 V=$(curl -s -u "$SONAR_TOKEN:" $U/api/authentication/validate); case "$V" in *'"valid":true'*) ok "the token is valid";; *) no "the token is valid (is SONAR_TOKEN set?)";; esac
 CV=$(m coverage); [ -n "$CV" ] && ok "coverage is reported: $CV percent" || no "coverage is reported (scan with the JaCoCo report)"
 B=$(m bugs); VU=$(m vulnerabilities); S=$(m code_smells); [ -n "$B" ] && [ -n "$VU" ] && [ -n "$S" ] && ok "issues read: $B bugs, $VU vulnerabilities, $S code smells" || no "issues can be read"
 NA=$(curl -s -u "$SONAR_TOKEN:" "$U/api/project_analyses/search?project=$K&ps=5" | grep -o '"date"' | wc -l); [ "$NA" -ge 2 ] && ok "$NA analyses: you can compare before and after" || no "two analyses exist (scan again after a fix)"
 echo "RESULT: $P of $N checks pass"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P -eq $N ];;
*) echo "usage: lab167.sh check";;
esac
