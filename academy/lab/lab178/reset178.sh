#!/bin/sh
# L178 start state: CI #1 built 1.0.1 (dev), 1.0.1 live in production (blue, behind nginx 9100), stage empty, jobs fresh, repo178 at start178
cd /home/claude/jenkins-lab
A=$(grep '^NEXUS_PASSWORD=' /home/claude/academy/lesson173/pw.env | cut -d= -f2); N=http://localhost:8081/service/rest/v1
D=$(grep '^NEXUS_DEPLOYER_PASSWORD=' /home/claude/academy/lesson176/pw.env | cut -d= -f2)
for id in $(curl -s -u admin:$A "$N/search?repository=cloudcart-releases&group=academy.cloudcart" | sed -n 's/.*"id" *: *"\([^"]*\)".*/\1/p'); do curl -s -o /dev/null -u admin:$A -X DELETE $N/components/$id; done
for n in dev stage prod prodg; do rm -rf tc177/$n/webapps/cloudcart tc177/$n/webapps/cloudcart.war; done
printf 'location / { proxy_pass http://127.0.0.1:9103; }  # blue\n' > nginx178/live.conf; nginx -c /home/claude/jenkins-lab/nginx178/nginx.conf -s reload 2>/dev/null || su jenkins -s /bin/sh -c "nginx -c /home/claude/jenkins-lab/nginx178/nginx.conf -s reload"
: > /tmp/chat178.log
chown -R jenkins home154/jobs 2>/dev/null
rm -rf home154/workspace/cloudcart-ci* home154/workspace/cloudcart-promote*
su jenkins -c 'cd /home/claude/jenkins-lab/repo178 && git checkout -q main && git reset -q --hard start178 && git clean -qfd'
sh mkjobs178.sh
# setup build 1
J=localhost:8080; JA="-u admin:devops-lab"; curl -s $JA -c /tmp/cj178 $J/crumbIssuer/api/json -o /tmp/crumb178.json; C=$(python3 -c "import json;d=json.load(open('/tmp/crumb178.json'));print(d['crumbRequestField']+':'+d['crumb'])")
curl -s $JA -b /tmp/cj178 -H "$C" -X POST $J/job/cloudcart-ci/build -o /dev/null
for i in $(seq 100); do R=$(curl -s $JA $J/job/cloudcart-ci/1/api/json | sed -n 's/.*"result":\("[A-Z]*"\|null\).*/\1/p'); [ -n "$R" ] && [ "$R" != null ] && break; sleep 3; done; echo "setup build 1: $R"
su jenkins -s /bin/sh -c "cd /home/claude/jenkins-lab/repo178 && NEXUS_USER=cart-deployer NEXUS_PASSWORD=$D scripts/deploy.sh 1.0.1 prod"
: > /tmp/chat178.log
echo reset178 done
