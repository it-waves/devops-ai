rm -rf /home/student/.m2
L=/home/claude/devops-ai/academy/lab/lab92.sh
export SUDO_USER=student ACCEPT_NEXUS_EULA=yes
pkill -u nexus java 2>/dev/null; sleep 3
sh $L down >/dev/null; sh $L up > /tmp/up92.out 2>&1; tail -3 /tmp/up92.out
echo "-- start"; sh $L check | tail -7
cd /opt/lab92
P=$(cat pass.txt)
b() { (cd $1; shift; runuser -u student -- env CORP_PASS=$P HOME=/home/student mvn -B -q "$@" 2>&1 | grep -v '^Picked up' | grep -E 'ERROR|FAIL|Tests run' | head -3); }
echo "== notfound"; b notfound clean package
echo "== offline"; b offline clean package
echo "== tests"; b tests clean package
echo "== login"; b login -s settings.xml clean package
sed -i 's#3.14.99#3.14.0#' notfound/pom.xml
rm offline/.mvn/maven.config
sed -i 's#/ 1000#/ 100#' tests/src/main/java/cloudcart/Cart.java
sed -i 's#corp-repo#corp#' login/settings.xml
printf '1 notfound: wrong version, 404 not found\n2 offline: -o in maven.config\n3 tests: wrong divisor 1000\n4 login: 401, server id differs from mirror id\n' > diag.txt; chown student diag.txt
echo "-- solved"; sh $L check | tail -7
sh $L down; ls /opt/lab92 2>&1 | head -1; id nexus92 2>&1 | head -1
echo TESTDONE
