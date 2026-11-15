cp /home/claude/devops-ai/academy/lab/lab106.sh /usr/local/sbin/lab106.sh; chmod 755 /usr/local/sbin/lab106.sh
L="env SUDO_USER=student sh /usr/local/sbin/lab106.sh"
S="runuser -u student -- env -u JAVA_TOOL_OPTIONS"
$L down >/dev/null; $L up 2>&1 | tail -1; cd /opt/lab106
echo "base: $($L check 2>&1 | tail -1)"
$S sh -c 'cd /opt/lab106/cart-1.0 && MAVEN_OPTS="'"$JAVA_TOOL_OPTIONS"'" /opt/maven/bin/mvn -B -q package 2>&1 | tail -n 3; cp target/cart.war ../releases/cart-1.0.war'
$S sh -c 'cd /opt/lab106/cart-2.0 && MAVEN_OPTS="'"$JAVA_TOOL_OPTIONS"'" /opt/maven/bin/mvn -B -q package 2>&1 | tail -n 3; cp target/cart.war ../releases/cart-2.0.war'
ls -la releases; echo "built: $($L check 2>&1 | tail -1)"
$S /opt/lab106/tomcat/bin/startup.sh 2>&1 | tail -1; cp releases/cart-1.0.war tomcat/webapps/cart.war; chown student tomcat/webapps/cart.war; sleep 22
curl -s localhost:8080/cart/; curl -s -o /dev/null -w '%{http_code}\n' localhost:8080/cart/health
cp releases/cart-2.0.war tomcat/webapps/cart.war; sleep 22; curl -s localhost:8080/cart/; curl -s -o /dev/null -w '%{http_code}\n' localhost:8080/cart/health
cp releases/cart-1.0.war tomcat/webapps/cart.war; sleep 22; curl -s localhost:8080/cart/; curl -s -o /dev/null -w '%{http_code}\n' localhost:8080/cart/health
printf 'v1: 200\nv2: 500\nrollback: 200\n' > history.txt; $L check 2>&1 | tail -6
cd /; $L down; ls /opt/lab106 2>&1 | head -1; pgrep -f catalina | head -1
