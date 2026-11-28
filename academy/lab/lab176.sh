#!/bin/sh
# Lesson 176 lab: the Nexus Repository mastery scenario. Seven checks prove your artifact pipeline works. Own machine only.
# Usage: lab176.sh up | check | down      Run "check" inside your CloudCart project folder (check 7 looks for passwords in its files).
# Env (never stored in a file): NEXUS_ADMIN = admin:password   NEXUS_USER and NEXUS_PASSWORD = your deployer account
# Optional: NEXUS_URL (default http://localhost:8081), REPO_SNAP (default cloudcart-snapshots), REPO_REL (default cloudcart-releases), COMP (default com/cloudcart/cart-core/1.0.0/cart-core-1.0.0)
U=${NEXUS_URL:-http://localhost:8081}; REPO_SNAP=${REPO_SNAP:-cloudcart-snapshots}; REPO_REL=${REPO_REL:-cloudcart-releases}; COMP=${COMP:-com/cloudcart/cart-core/1.0.0/cart-core-1.0.0}
OUT=${NEXUS_OUT:-./results176.txt}; P=0; N=0; PING=com/cloudcart/lab176/1.0-SNAPSHOT/lab176-1.0-SNAPSHOT.txt
ad() { curl -s -m 10 -u "$NEXUS_ADMIN" "$@"; }
dp() { curl -s -m 10 -u "$NEXUS_USER:$NEXUS_PASSWORD" "$@"; }
need() { [ -n "$NEXUS_ADMIN" ] && [ -n "$NEXUS_USER" ] && [ -n "$NEXUS_PASSWORD" ] || { echo "Set NEXUS_ADMIN (admin:password), NEXUS_USER and NEXUS_PASSWORD (deployer) first"; exit 2; }; }
case "$1" in
up) need
 [ "$(curl -s -o /dev/null -m 5 -w '%{http_code}' $U/service/rest/v1/status)" = 200 ] && echo "Nexus is UP at $U" || echo "Nexus is NOT up at $U (start it, wait for the status page)"
 echo "Scenario: releases $REPO_REL, snapshots $REPO_SNAP, deployer $NEXUS_USER"; echo "Results go to $OUT";;
check) need; : > $OUT
 if [ -t 1 ]; then G='\033[1;92m'; R='\033[1;91m'; W='\033[1;97m'; Z='\033[0m'; else G=; R=; W=; Z=; fi
 t() { N=$((N+1)); if [ "$1" = ok ]; then P=$((P+1)); L="PASS  $N  $2"; C=$G; else L="FAIL  $N  $2  -> $3"; C=$R; fi; printf '%b%s%b\n' "$C" "$L" "$Z"; echo "$L" >> $OUT; }
 [ "$(curl -s -o /dev/null -m 5 -w '%{http_code}' $U/service/rest/v1/status)" = 200 ] && t ok "Nexus is UP" || t no "Nexus is UP" "start Nexus, wait for the status page"
 ad "$U/service/rest/v1/repositories/maven/hosted/$REPO_REL" | tr -d ' \n' | grep -q '"online":true.*"writePolicy":"ALLOW_ONCE"' && t ok "$REPO_REL is online and immutable" || t no "$REPO_REL is online and immutable" "Repositories, tick Online, write policy Disable redeploy"
 [ "$(printf 'lab176' | dp -o /dev/null -m 10 -w '%{http_code}' -X PUT --data-binary @- $U/repository/$REPO_SNAP/$PING)" = 201 ] && t ok "The deployer can publish a snapshot" || t no "The deployer can publish a snapshot" "401: fix the password. 403: fix the role, add on $REPO_SNAP"
 [ "$(dp -o /dev/null -w '%{http_code}' -X DELETE $U/repository/$REPO_REL/com/cloudcart/lab176/none.txt)" = 403 ] && t ok "The deployer cannot delete from $REPO_REL" || t no "The deployer cannot delete from $REPO_REL" "Roles: remove delete and the star on the releases repository"
 S1=$(dp $U/repository/$REPO_REL/$COMP.jar.sha1); S2=$(dp $U/repository/$REPO_REL/$COMP.jar | sha1sum | cut -d' ' -f1)
 [ -n "$S1" ] && [ "$S1" = "$S2" ] && t ok "The release jar matches its checksum" || t no "The release jar matches its checksum" "404 or 503: check the path, check the repository is online"
 ad "$U/service/rest/v1/tasks" | grep -q 'repository.maven.remove-snapshots' && ad "$U/service/rest/v1/tasks" | grep -q 'db.backup' && t ok "Snapshot cleanup and backup tasks exist" || t no "Snapshot cleanup and backup tasks exist" "System, Tasks: create both"
 if grep -rIqE '<password>[^$<][^<]*</password>' . 2>/dev/null; then t no "No password in the code" "move it to an environment variable, then change the password"; else t ok "No password in the code"; fi
 printf '%bRESULT: %s of %s checks pass%b\n' "$W" $P $N "$Z"; echo "RESULT: $P of $N checks pass" >> $OUT; [ $P = $N ];;
down) need
 [ -f "$OUT" ] && grep -q "RESULT: 7 of 7" "$OUT" && cp "$OUT" "${OUT%.txt}-evidence.txt" && echo "Evidence kept: ${OUT%.txt}-evidence.txt"
 C=$(ad "$U/service/rest/v1/search?repository=$REPO_SNAP&group=com.cloudcart&name=lab176" | sed -n 's/.*"id" *: *"\([^"]*\)".*/\1/p' | head -1)
 [ -n "$C" ] && ad -X DELETE "$U/service/rest/v1/components/$C" -o /dev/null -w "delete test component: %{http_code}\n"
 echo "Test component removed. Nexus, your repositories, your role and your tasks are untouched. Change any password you typed in plain text.";;
*) echo "usage: lab176.sh up|check|down";;
esac
