#!/bin/sh
# L168: SonarQube up; fresh CloudCart copy; baseline scan WITH JaCoCo coverage; no custom gate; token saved for the terminal.
S=/home/claude/jenkins-lab/sq165/sonarqube-26.11.0.134175
mountpoint -q /mnt/sqdata || { mkdir -p /mnt/sqdata; mount -t tmpfs -o size=1500m tmpfs /mnt/sqdata; mkdir -p /mnt/sqdata/data /mnt/sqdata/temp; chown -R jenkins /mnt/sqdata; }
curl -s localhost:9000/api/system/status | grep -q UP || { su jenkins -s /bin/sh -c "$S/bin/linux-x86-64/sonar.sh start" >/dev/null 2>&1; for i in $(seq 40); do curl -s localhost:9000/api/system/status | grep -q UP && break; sleep 5; done; }
. /home/claude/academy/lesson168/pw.env
curl -s -u admin:admin localhost:9000/api/authentication/validate | grep -q 'true' && curl -s -u admin:admin -X POST localhost:9000/api/users/change_password -d login=admin -d previousPassword=admin --data-urlencode password="$SONAR_PASSWORD" -o /dev/null
curl -s -u admin:$SONAR_PASSWORD -X POST localhost:9000/api/projects/delete -d project=cloudcart -o /dev/null
curl -s -u admin:$SONAR_PASSWORD -X POST localhost:9000/api/qualitygates/destroy --data-urlencode name="Cloud Cart gate" -o /dev/null
for t in cloudcart-scan t167 t168; do curl -s -u admin:$SONAR_PASSWORD -X POST localhost:9000/api/user_tokens/revoke -d name=$t -o /dev/null; done
rm -rf /home/claude/jenkins-lab/cloudcart168 /tmp/.sonar-token; mkdir /home/claude/jenkins-lab/cloudcart168
cd /home/claude/jenkins-lab/repo164 && tar cf - --exclude=target --exclude=.git . | (cd /home/claude/jenkins-lab/cloudcart168 && tar xf -)
env | grep -E "^(JAVA_TOOL_OPTIONS|HTTPS_PROXY|https_proxy|NO_PROXY|no_proxy|SSL_CERT_FILE)=" | sed "s/^/export /; s/=\(.*\)/='\1'/" > /tmp/jto.env
TK=$(curl -s -u admin:$SONAR_PASSWORD -X POST localhost:9000/api/user_tokens/generate -d name=cloudcart-scan | sed 's/.*"token":"\([^"]*\)".*/\1/')
echo "$TK" > /tmp/.sonar-token; chown jenkins /tmp/.sonar-token; chmod 600 /tmp/.sonar-token
chown -R jenkins /home/claude/jenkins-lab/cloudcart168
cd /home/claude/jenkins-lab/cloudcart168
runuser -u jenkins -- env -i HOME=/home/claude/jenkins-lab PATH=/usr/local/bin:/usr/bin:/bin:/opt/maven/bin SONAR_TOKEN=$TK bash -c ". /tmp/jto.env; mvn -B -q org.jacoco:jacoco-maven-plugin:0.8.12:prepare-agent verify org.jacoco:jacoco-maven-plugin:0.8.12:report org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey=cloudcart -Dsonar.host.url=http://localhost:9000" > /tmp/base168.log 2>&1
for i in $(seq 30); do curl -s -u admin:$SONAR_PASSWORD "localhost:9000/api/ce/component?component=cloudcart" | grep -q '"queue":\[\]' && curl -s -u admin:$SONAR_PASSWORD "localhost:9000/api/project_analyses/search?project=cloudcart" | grep -q '"date"' && break; sleep 2; done
rm -f /home/claude/jenkins-lab/cloudcart168/results168.txt
echo reset168 done
