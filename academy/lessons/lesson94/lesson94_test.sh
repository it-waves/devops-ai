rm -rf /home/student/.m2
L=/home/claude/devops-ai/academy/lab/lab94.sh
export SUDO_USER=student ACCEPT_NEXUS_EULA=yes
pkill -u nexus java 2>/dev/null; pkill -u nexus93 java 2>/dev/null; pkill -u nexus92 java 2>/dev/null; sleep 3
sh $L down >/dev/null; sh $L up > /tmp/up94.out 2>&1; tail -n 3 /tmp/up94.out
echo "-- start"; sh $L check | tail -n 7
cd /opt/lab94/cart-core; P=$(cat ../pass.txt)
b() { runuser -u student -- env CORP_PASS=$P HOME=/home/student mvn -B -q "$@" 2>&1 | grep -v '^Picked up' | grep -E 'ERROR|FAIL|Tests run|BUILD' | head -n 3; }
echo "== build 1"; b clean package
sed -i 's#<version>3.4</version>#<version>3.14.0</version>#' pom.xml
echo "== build 2"; b clean package
sed -i 's#truncate(name, 4)#truncate(name, 5)#' src/main/java/cloudcart/Cart.java
sed -i 's#<maven.compiler.release>21</maven.compiler.release>#&\n    <project.build.outputTimestamp>2024-01-01T00:00:00Z</project.build.outputTimestamp>#' pom.xml
echo "== deploy"; b -s settings.xml clean deploy; echo deployed
printf 'result: cart-core 1.0.0-SNAPSHOT published to corp-snapshots on Nexus\ntrouble: old dependency version without truncate; wrong number in the code; no output timestamp so the sha256 changed\ncleanup: lab down\n' > ../report.txt; chown student ../report.txt
echo "-- solved"; sh $L check | tail -n 7
sh $L down; ls /opt/lab94 2>&1 | head -n 1; id nexus94 2>&1 | head -n 1
echo TESTDONE
