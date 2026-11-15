cp /home/claude/devops-ai/academy/lab/lab104.sh /usr/local/sbin/lab104.sh; chmod 755 /usr/local/sbin/lab104.sh
L="env SUDO_USER=student sh /usr/local/sbin/lab104.sh"
$L down >/dev/null; LAB104_TOMCAT_URL=file:///opt/dist/apache-tomcat-10.1.34.tar.gz $L up 2>&1 | tail -1; cd /opt/lab104
echo "base: $($L check 2>&1 | tail -1)"
runuser -u student -- env -u JAVA_TOOL_OPTIONS /opt/lab104/tomcat/bin/startup.sh >/dev/null 2>&1; sleep 12; echo "started: $($L check 2>&1 | tail -1)"
cp demo/hello.war tomcat/webapps/; chown student tomcat/webapps/hello.war; sleep 25; echo "deployed: $($L check 2>&1 | tail -1)"
unzip -l demo/hello.war > war-list.txt; echo "warlist: $($L check 2>&1 | tail -1)"
printf 'jvm: runs Tomcat and the Java code\nconnector: listens on port 8080 for http\ncontext: the url path of one app\nwar: a zip file of one web app\n' > facts.txt; $L check 2>&1 | tail -6
cd /; $L down; ls /opt/lab104 2>&1 | head -1; pgrep -f catalina | head -1
