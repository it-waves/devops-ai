L=/home/claude/devops-ai/academy/lab/lab96.sh
export SUDO_USER=student LAB96_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip
sh $L down >/dev/null; sh $L up 2>&1 | tail -n 3
echo "-- start"; sh $L check | tail -n 7
cd /opt/lab96/cartcore
sed -i 's/return total() - percent;/return total() * (1 - percent \/ 100.0);/' src/main/java/cloudcart/Cart.java
G="runuser -u student -- env HOME=/home/student ./gradlew --console=plain"
$G test 2>&1 | grep -v Picked | tail -n 4
echo "-- mid"; sh $L check | tail -n 7
$G dependencies --configuration runtimeClasspath 2>&1 | grep -v Picked > ../deps.txt
$G dependencyInsight --dependency commons-lang3 --configuration runtimeClasspath 2>&1 | grep -v Picked > ../insight.txt
head -n 12 ../insight.txt
V=$(grep -m1 -oE 'commons-lang3:[0-9][0-9A-Za-z.]*' ../insight.txt | cut -d: -f2); echo "V=$V"
printf "version: $V\nwhy: commons-text needs a newer version, a version conflict, and Gradle takes the highest\nreport: build/reports/tests/test/index.html\n" > ../notes.txt; chown student ../deps.txt ../insight.txt ../notes.txt
echo "-- solved"; sh $L check | tail -n 7
sh $L down; ls /opt/lab96 2>&1 | head -n 1; ls /home/student/.gradle/wrapper/dists 2>&1 | head -n 3
echo TESTDONE
