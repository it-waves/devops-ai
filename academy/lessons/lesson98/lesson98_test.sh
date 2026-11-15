L=/home/claude/devops-ai/academy/lab/lab98.sh
export SUDO_USER=student LAB98_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip
sh $L down >/dev/null; sh $L up 2>&1 | tail -n 2
echo "-- start"; sh $L check | tail -n 6
cd /opt/lab98/cartcore
G="runuser -u student -- env HOME=/home/student ./gradlew --console=plain"
$G -q showConfig 2>&1 | grep -v Picked
sed -i '/repoPassword/d' gradle.properties; echo 'greeting=Welcome to CloudCart' >> gradle.properties
echo "-- mid1"; sh $L check | tail -n 6
$G -q showConfig -Pgreeting=Hello 2>&1 | grep -v Picked > ../override.txt
ORG_GRADLE_PROJECT_repoPassword=test123 $G -q showConfig 2>&1 | grep -v Picked > ../secret.txt
cat ../override.txt ../secret.txt
printf "where: in the environment, one command at a time\nwhy: a file ends up in git, and then everyone can read it\noverride: -P on the command line\n" > ../notes.txt; chown student ../*.txt
echo "-- solved"; sh $L check | tail -n 6
sh $L down; ls /opt/lab98 2>&1 | head -n 1
echo TESTDONE
