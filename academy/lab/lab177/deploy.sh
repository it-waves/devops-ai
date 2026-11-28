#!/bin/sh
set -e
VERSION=$1; ENVN=$2
case $ENVN in dev) PORT=9101;; stage) PORT=9102;; prod) PORT=9103;; esac
REPO=http://localhost:8081/repository/cloudcart-releases
BASE=$REPO/academy/cloudcart/cloudcart/$VERSION
WAR=cloudcart-$VERSION.war
TOMCAT=/home/claude/jenkins-lab/tc177/$ENVN/webapps
# 1  download the war from Nexus
curl -sf -u "$NEXUS_USER:$NEXUS_PASSWORD" -o /tmp/$WAR $BASE/$WAR
# 2  compare its checksum with the one Nexus recorded
EXPECT=$(curl -sf -u "$NEXUS_USER:$NEXUS_PASSWORD" $BASE/$WAR.sha1)
ACTUAL=$(sha1sum /tmp/$WAR | cut -d' ' -f1)
[ "$EXPECT" = "$ACTUAL" ] || { echo "CHECKSUM MISMATCH"; exit 1; }
echo "checksum ok $ACTUAL"
# 3  copy it to Tomcat
cp /tmp/$WAR $TOMCAT/cloudcart.war.tmp
mv $TOMCAT/cloudcart.war.tmp $TOMCAT/cloudcart.war
# 4  verify: ask the running application which version it is
for i in $(seq 40); do
  GOT=$(curl -s localhost:$PORT/cloudcart/health | sed -n 's/.*"version":"\([^"]*\)".*/\1/p')
  [ "$GOT" = "$VERSION" ] && { echo "verified $ENVN runs $VERSION"; exit 0; }
  sleep 1
done
echo "VERIFY FAILED: $ENVN reports '$GOT', expected $VERSION"; exit 1
