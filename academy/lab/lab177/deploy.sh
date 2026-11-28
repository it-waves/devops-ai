#!/bin/sh
# usage: deploy.sh <version> <env>   (env: dev, stage or prod)
# Downloads the SAME war from Nexus, checks its checksum, copies it to that environment's Tomcat.
set -e
VERSION=$1; ENVN=$2
case $ENVN in dev) PORT=9101;; stage) PORT=9102;; prod) PORT=9103;; *) echo "unknown env $ENVN"; exit 2;; esac
BASE=http://localhost:8081/repository/cloudcart-releases/academy/cloudcart/cloudcart/$VERSION
WAR=cloudcart-$VERSION.war
curl -sf -u "$NEXUS_USER:$NEXUS_PASSWORD" -o /tmp/$WAR $BASE/$WAR
EXPECT=$(curl -sf -u "$NEXUS_USER:$NEXUS_PASSWORD" $BASE/$WAR.sha1)
ACTUAL=$(sha1sum /tmp/$WAR | cut -d' ' -f1)
[ "$EXPECT" = "$ACTUAL" ] || { echo "CHECKSUM MISMATCH for $WAR"; exit 1; }
echo "checksum ok $ACTUAL"
cp /tmp/$WAR /home/claude/jenkins-lab/tc177/$ENVN/webapps/cloudcart.war.tmp
mv /home/claude/jenkins-lab/tc177/$ENVN/webapps/cloudcart.war.tmp /home/claude/jenkins-lab/tc177/$ENVN/webapps/cloudcart.war
for i in $(seq 40); do
  GOT=$(curl -s localhost:$PORT/cloudcart/health | sed -n 's/.*"version":"\([^"]*\)".*/\1/p')
  [ "$GOT" = "$VERSION" ] && { echo "verified $ENVN runs $VERSION"; exit 0; }; sleep 1
done
echo "VERIFY FAILED: $ENVN reports '$GOT', expected $VERSION"; exit 1
