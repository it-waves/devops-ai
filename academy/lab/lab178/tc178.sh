#!/bin/sh
# L178 extras: green production Tomcat (9104) and nginx router on 9100 (blue = tc177/prod 9103, green = tc177/prodg 9104), chat webhook on 9300
H=/tmp/cct/apache-tomcat-10.1.34; B=/home/claude/jenkins-lab/tc177; N=/home/claude/jenkins-lab/nginx178
JH=$(dirname $(dirname $(readlink -f $(which java))))
su jenkins -s /bin/sh -c "CATALINA_BASE=$B/prodg $H/bin/catalina.sh stop" >/dev/null 2>&1
rm -rf $B/prodg; mkdir -p $B/prodg/conf $B/prodg/logs $B/prodg/temp $B/prodg/webapps $B/prodg/work
cp $H/conf/web.xml $H/conf/catalina.properties $H/conf/logging.properties $B/prodg/conf/
cat > $B/prodg/conf/server.xml <<Y
<Server port="9204" shutdown="SHUTDOWN"><Service name="Catalina"><Connector port="9104" protocol="HTTP/1.1" connectionTimeout="20000"/><Engine name="Catalina" defaultHost="localhost"><Host name="localhost" appBase="webapps" unpackWARs="true" autoDeploy="true"/></Engine></Service></Server>
Y
chown -R jenkins $B
su jenkins -s /bin/sh -c "CATALINA_BASE=$B/prodg CATALINA_PID=$B/prodg/tc.pid JAVA_HOME=$JH CATALINA_OPTS='-Xmx128m' $H/bin/catalina.sh start" >/dev/null 2>&1
mkdir -p $N/tmp; printf 'location / { proxy_pass http://127.0.0.1:9103; }  # blue\n' > $N/live.conf; chown -R jenkins $N
pkill -u jenkins nginx; pkill -f webhook178.py; sleep 1
su jenkins -s /bin/sh -c "nginx -c $N/nginx.conf"
: > /tmp/chat178.log; chmod 666 /tmp/chat178.log
(setsid nohup su jenkins -s /bin/sh -c "python3 $N/../webhook178.py" >/dev/null 2>&1 &)
for p in 9104 9100; do for i in $(seq 30); do curl -s -o /dev/null localhost:$p/ && break; sleep 1; done; echo "$p $(curl -s -o /dev/null -w '%{http_code}' localhost:$p/)"; done
