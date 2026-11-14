unset JAVA_TOOL_OPTIONS
export PATH=/opt/maven/bin:$PATH
mkdir -p /tmp/gs && cat > /tmp/gs/gs.xml <<'X'
<settings><mirrors><mirror><id>offline-pkg</id><mirrorOf>external:*</mirrorOf><url>file:///opt/m2mirror</url></mirror></mirrors></settings>
X
chmod -R a+rX /tmp/gs
export MAVEN_ARGS="-gs /tmp/gs/gs.xml"
L=/home/claude/devops-ai/academy/lab/lab91.sh
export SUDO_USER=student
sh $L down >/dev/null; sh $L up; cd /opt/lab91/shop
echo "-- start"; sh $L check | tail -7
P=$(cat /opt/lab91/pass.txt)
runuser -u student -- env HOME=/home/student CORP_PASS=$P "MAVEN_ARGS=$MAVEN_ARGS" sh -c "mvn -B -q -s settings.xml deploy 2>&1 | tail -2; sed -i 's/1.0.0-SNAPSHOT/1.0.0/' pom.xml; mvn -B -q -s settings.xml deploy 2>&1 | tail -2; mvn -B -s settings.xml deploy 2>&1 | grep -o 'status code.*' > conflict.txt; cat conflict.txt; sed -i 's#<version>1.0.0</version>#<version>1.0.1</version>#' pom.xml; mvn -B -q -s settings.xml deploy 2>&1 | tail -2; echo 'A release must never be overwritten so it stays reproducible.' > why.txt"
echo "-- final"; sh $L check | tail -7
cd /; sh $L down; ls /opt/lab91 2>&1 | head -1; pgrep -fa srv.py | head -2
