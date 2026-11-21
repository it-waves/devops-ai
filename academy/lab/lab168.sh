#!/bin/sh
# Lesson 168 lab: check that your project uses a custom quality gate with a coverage rule, and that it passes. Own machine only.
# Usage: lab168.sh check     Env: SONAR_URL (default http://localhost:9000), SONAR_TOKEN (your user token), SONAR_KEY (project key, default cloudcart)
U=${SONAR_URL:-http://localhost:9000}; K=${SONAR_KEY:-cloudcart}; OUT=${SONAR_OUT:-./results168.txt}; P=0; N=4
ok() { P=$((P+1)); if [ -t 1 ]; then printf '\033[1;92mPASS\033[0m  %s\n' "$1"; else echo "PASS  $1"; fi; echo "PASS  $1" >> $OUT; }
no() { if [ -t 1 ]; then printf '\033[1;91mFAIL\033[0m  %s\n' "$1"; else echo "FAIL  $1"; fi; echo "FAIL  $1" >> $OUT; }
api() { curl -s -u "$SONAR_TOKEN:" "$U/api/$1"; }
case "$1" in
check) : > $OUT
 V=$(api authentication/validate); case "$V" in *'"valid":true'*) ok "the token is valid";; *) no "the token is valid (is SONAR_TOKEN set?)";; esac
 G=$(api "qualitygates/get_by_project?project=$K" | sed -n 's/.*"name":"\([^"]*\)".*/\1/p'); DF=$(api "qualitygates/get_by_project?project=$K" | grep -o '"default":true')
 if [ -n "$G" ] && [ -z "$DF" ]; then ok "the project uses its own gate: $G"; else no "the project uses its own gate (not the default)"; fi
 GE=$(echo "$G" | sed 's/ /%20/g'); C=$(api "qualitygates/show?name=$GE" | grep -o '"metric":"coverage","op":"LT","error":"[0-9.]*"' | sed 's/.*"error":"\([0-9.]*\)"/\1/')
 [ -n "$C" ] && ok "the gate has an overall coverage rule: at least $C percent" || no "the gate has an overall coverage rule (Add Condition: Coverage, Overall Code)"
 S=$(api "qualitygates/project_status?projectKey=$K" | grep -o '"status":"[A-Z]*"' | head -1 | sed 's/.*:"\(.*\)"/\1/'); [ "$S" = "OK" ] && ok "the quality gate is Passed" || no "the quality gate is Passed (now: ${S:-unknown})"
 echo "RESULT: $P of $N checks pass"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P -eq $N ];;
*) echo "usage: lab168.sh check";;
esac
