cp /home/claude/devops-ai/academy/lab/lab105.sh /usr/local/sbin/lab105.sh; chmod 755 /usr/local/sbin/lab105.sh
L="env SUDO_USER=student sh /usr/local/sbin/lab105.sh"
$L down >/dev/null; $L up 2>&1 | tail -2; cd /opt/lab105
echo "base: $($L check 2>&1 | tail -1)"
( cd dl && sha512sum -c apache-tomcat-10.1.34.tar.gz.sha512 > ../checksum.txt; cat ../checksum.txt ); echo "sum: $($L check 2>&1 | tail -1)"
useradd -r -s /usr/sbin/nologin -d /opt/lab105/tomcat tomcat; echo "user: $($L check 2>&1 | tail -1)"
mkdir tomcat; tar xzf dl/apache-tomcat-10.1.34.tar.gz -C tomcat --strip-components=1; chown -R tomcat: tomcat; echo "unpack: $($L check 2>&1 | tail -1)"
env -u JAVA_TOOL_OPTIONS runuser -u tomcat -- tomcat/bin/startup.sh 2>&1 | tail -1; sleep 8; echo "started: $($L check 2>&1 | tail -1)"
grep "Server startup" tomcat/logs/catalina.out > startup.txt; cat startup.txt; $L check 2>&1 | tail -6
cd /; $L down; ls /opt/lab105 2>&1 | head -1; pgrep -f catalina | head -1; getent passwd tomcat
