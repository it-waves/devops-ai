#!/bin/sh
# three Tomcat instances for L177: dev 9101, stage 9102, prod 9103 (CATALINA_BASE each)
H=/tmp/cct/apache-tomcat-10.1.34; B=/home/claude/jenkins-lab/tc177
for e in dev:9101:9201 stage:9102:9202 prod:9103:9203; do n=${e%%:*}; r=${e#*:}; p=${r%%:*}; s=${r#*:}
 su jenkins -s /bin/sh -c "CATALINA_BASE=$B/$n JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java)))) $H/bin/catalina.sh stop" >/dev/null 2>&1
 rm -rf $B/$n; mkdir -p $B/$n/conf $B/$n/logs $B/$n/temp $B/$n/webapps $B/$n/work
 cp $H/conf/web.xml $H/conf/catalina.properties $H/conf/logging.properties $B/$n/conf/
 cat > $B/$n/conf/server.xml <<X
<Server port="$s" shutdown="SHUTDOWN"><Service name="Catalina"><Connector port="$p" protocol="HTTP/1.1" connectionTimeout="20000"/><Engine name="Catalina" defaultHost="localhost"><Host name="localhost" appBase="webapps" unpackWARs="true" autoDeploy="true"/></Engine></Service></Server>
X
done
chown -R jenkins $B
for n in dev stage prod; do su jenkins -s /bin/sh -c "CATALINA_BASE=$B/$n CATALINA_PID=$B/$n/tc.pid JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java)))) CATALINA_OPTS='-Xmx128m' $H/bin/catalina.sh start" >/dev/null 2>&1; done
for p in 9101 9102 9103; do for i in $(seq 30); do curl -s -o /dev/null localhost:$p/ && break; sleep 1; done; echo "$p $(curl -s -o /dev/null -w '%{http_code}' localhost:$p/)"; done
