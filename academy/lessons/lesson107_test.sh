# runs inside the systemd namespace:  nsenter -t <systemd pid> -m -p sh lesson107_test.sh
cp /home/claude/devops-ai/academy/lab/lab107.sh /usr/local/sbin/lab107.sh; chmod 755 /usr/local/sbin/lab107.sh
L="sh /usr/local/sbin/lab107.sh"; export LAB107_TOMCAT_BASE=file:///opt/dist
$L down >/dev/null; $L up 2>&1 | tail -n 1; cd /opt/lab107
echo "base: $($L check 2>&1 | tail -n 1)"
JH=$(dirname $(dirname $(readlink -f $(command -v java))))
printf 'export JAVA_HOME=%s\nexport CATALINA_PID=/opt/lab107/tomcat/temp/tomcat.pid\nexport CATALINA_OPTS="-Xmx256m -Dhttp.port=8081 -Dcloudcart.env=staging"\n' $JH > tomcat/bin/setenv.sh; chown tomcat: tomcat/bin/setenv.sh; chmod 755 tomcat/bin/setenv.sh
cat > /etc/systemd/system/tomcat107.service <<EOF
[Unit]
Description=Tomcat for lab 107
After=network.target
[Service]
Type=forking
User=tomcat
Group=tomcat
PIDFile=/opt/lab107/tomcat/temp/tomcat.pid
ExecStart=/opt/lab107/tomcat/bin/startup.sh
ExecStop=/opt/lab107/tomcat/bin/shutdown.sh
Restart=on-failure
RestartSec=3
[Install]
WantedBy=multi-user.target
EOF
echo "setup: $($L check 2>&1 | tail -n 1)"
systemctl daemon-reload; systemctl enable --now tomcat107 2>&1 | tail -n 1; sleep 15
systemctl is-active tomcat107; curl -s -o /dev/null -w '%{http_code}\n' localhost:8081
P=$(systemctl show -p MainPID --value tomcat107); echo main $P; ps -o user=,args= -p $P | cut -c1-90
echo "run: $($L check 2>&1 | tail -n 1)"
kill -9 $P; sleep 14; systemctl show -p MainPID,NRestarts tomcat107; curl -s -o /dev/null -w '%{http_code}\n' localhost:8081
$L check 2>&1 | tail -n 6
$L down; ls /opt/lab107 2>&1 | head -n 1; getent passwd tomcat; ls /etc/systemd/system/tomcat107.service 2>&1 | head -n 1; pgrep -f catalina | head -n 1
