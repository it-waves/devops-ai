#!/bin/sh
# Lesson 165 lab: check that your own SonarQube is installed, running and safe. Own machine only.
# Usage: lab165.sh check | stop     Env: SONAR_URL (default http://localhost:9000), SONAR_PASSWORD (your admin password), SONAR_HOME (install folder, for "stop")
U=${SONAR_URL:-http://localhost:9000}; OUT=${SONAR_OUT:-./results165.txt}; P=0; N=4
ok() { P=$((P+1)); if [ -t 1 ]; then printf '\033[1;92mPASS\033[0m  %s\n' "$1"; else echo "PASS  $1"; fi; echo "PASS  $1" >> $OUT; }
no() { if [ -t 1 ]; then printf '\033[1;91mFAIL\033[0m  %s\n' "$1"; else echo "FAIL  $1"; fi; echo "FAIL  $1" >> $OUT; }
case "$1" in
check) : > $OUT
 V=$(java -version 2>&1 | grep -v 'Picked up' | head -1 | sed 's/.*version "\([0-9]*\).*/\1/')
 [ "${V:-0}" -ge 17 ] 2>/dev/null && ok "Java $V is 17 or newer" || no "Java 17 or newer is installed"
 S=$(curl -s $U/api/system/status); case "$S" in *'"status":"UP"'*) ok "server answers: $(echo $S | sed 's/.*"version":"\([^"]*\)".*/version \1/; s/,.*//') is UP";; *) no "server answers and is UP";; esac
 H=$(curl -s -u admin:"$SONAR_PASSWORD" $U/api/system/health); case "$H" in *GREEN*) ok "health is GREEN";; *) no "health is GREEN (is SONAR_PASSWORD set?)";; esac
 C=$(curl -s -o /dev/null -w '%{http_code}' -u admin:admin $U/api/system/health); [ "$C" != 200 ] && ok "default password admin/admin no longer works" || no "default password admin/admin no longer works"
 echo "RESULT: $P of $N checks pass"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P -eq $N ];;
stop) [ -n "$SONAR_HOME" ] || { echo "Set SONAR_HOME to your SonarQube folder"; exit 1; }; "$SONAR_HOME/bin/linux-x86-64/sonar.sh" stop;;
*) echo "usage: lab165.sh check|stop";;
esac
