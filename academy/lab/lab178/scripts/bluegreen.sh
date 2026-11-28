#!/bin/sh
# blue-green release to production: usage bluegreen.sh VERSION
set -e
VERSION=$1; ROUTER=/home/claude/jenkins-lab/nginx178/live.conf
LIVE=$(sed -n 's/.*# \(blue\|green\)$/\1/p' $ROUTER); [ $LIVE = blue ] && IDLE=green || IDLE=blue
[ $IDLE = blue ] && IP=9103 || IP=9104
echo "live is $LIVE, deploying $VERSION to the idle side: $IDLE"
scripts/deploy.sh $VERSION $IDLE
echo "smoke test on $IDLE, before any user can reach it"
scripts/smoke.sh $IP $VERSION || { echo "SMOKE TEST FAILED on $IDLE. Traffic stays on $LIVE."; exit 1; }
switch() { printf 'location / { proxy_pass http://127.0.0.1:%s; }  # %s\n' $1 $2 > $ROUTER; nginx -c /home/claude/jenkins-lab/nginx178/nginx.conf -s reload; sleep 1; }
switch $IP $IDLE; echo "traffic switched to $IDLE"
scripts/smoke.sh 9100 $VERSION || { [ $LIVE = blue ] && OP=9103 || OP=9104; switch $OP $LIVE; echo "ROLLED BACK to $LIVE"; exit 1; }
echo "release complete: $IDLE is live with $VERSION, $LIVE is the instant rollback"
