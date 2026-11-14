unset JAVA_TOOL_OPTIONS
export PATH=/opt/maven/bin:$PATH
L=/home/claude/devops-ai/academy/lab/lab88.sh
export SUDO_USER=student
cp /home/claude/academy/lesson85/settings.xml.src /home/student/.m2/settings.xml; sed -i 's#<mirrorOf>\*</mirrorOf>#<mirrorOf>external:*</mirrorOf>#' /home/student/.m2/settings.xml
sh $L down >/dev/null; sh $L up; cd /opt/lab88/shop
echo "-- start"; sh $L check | tail -7
R="runuser -u student -- env HOME=/home/student"
$R sh -c "mvn -B dependency:tree -Dverbose | grep omitted > conflict.txt"; cat conflict.txt
python3 - <<'PY'
p=open('pom.xml').read()
p=p.replace('  <repositories>','  <dependencyManagement>\n    <dependencies>\n      <dependency>\n        <groupId>com.cloudcart.lib</groupId>\n        <artifactId>util</artifactId>\n        <version>2.0</version>\n      </dependency>\n    </dependencies>\n  </dependencyManagement>\n\n  <repositories>')
open('pom.xml','w').write(p)
PY
chown -R student /opt/lab88
echo "-- mid"; sh $L check | tail -7
$R sh -c "mvn -B dependency:tree > tree.txt; echo 'Maven picks the nearest version, and the first declared at equal depth.' > why.txt"
echo "-- final"; sh $L check | tail -7
cd /; sh $L down; ls /opt/lab88 2>&1 | head -1
