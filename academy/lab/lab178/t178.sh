#!/bin/sh
cd /home/claude/jenkins-lab
# dry validation of the L178 flow
J=localhost:8080; JA="-u admin:devops-lab"
crumb(){ curl -s $JA -c /tmp/cj178 $J/crumbIssuer/api/json -o /tmp/crumb178.json; C=$(python3 -c "import json;d=json.load(open('/tmp/crumb178.json'));print(d['crumbRequestField']+':'+d['crumb'])"); }
build(){ crumb; if [ -n "$3" ]; then curl -s $JA -b /tmp/cj178 -H "$C" -X POST "$J/job/$1/buildWithParameters?$3" -o /dev/null -w "start %{http_code}\n"; else curl -s $JA -b /tmp/cj178 -H "$C" -X POST "$J/job/$1/build" -o /dev/null -w "start %{http_code}\n"; fi; }
wait(){ for i in $(seq 120); do R=$(curl -s $JA $J/job/$1/$2/api/json | sed -n 's/.*"result":\("[A-Z]*"\|null\).*/\1/p'); [ -n "$R" ] && [ "$R" != null ] && break; sleep 2; done; echo "$1 #$2 $R"; }
git(){ su jenkins -c "cd /home/claude/jenkins-lab/repo178 && git -c user.name=Dana -c user.email=dana@cloudcart.example $(printf '%q ' "$@")"; }
approve(){ for i in $(seq 60); do ID=$(curl -s $JA $J/job/cloudcart-promote/$1/wfapi/describe | python3 -c "import json,sys;d=json.load(sys.stdin);print([s['id'] for s in d['stages'] if s['status']=='PAUSED_PENDING_INPUT'][0])" 2>/dev/null); [ -n "$ID" ] && break; sleep 2; done; curl -s $JA $J/job/cloudcart-promote/$1/wfapi/nextPendingInputAction | head -c 300; echo; crumb; curl -s $JA -b /tmp/cj178 -H "$C" -X POST $J/job/cloudcart-promote/$1/input/Release/proceedEmpty -o /dev/null -w "proceed %{http_code}\n"; }
sed -i 's/subtotal >= FREE/subtotal > FREE/' /home/claude/jenkins-lab/repo178/src/main/java/academy/cloudcart/Pricing.java; git commit -qam "Tidy shipping rule"
build cloudcart-ci 2; wait cloudcart-ci 2; cat /tmp/chat178.log
git revert --no-edit HEAD; git log --oneline | head -3
build cloudcart-ci 3; wait cloudcart-ci 3
build cloudcart-promote 1 "VERSION=1.0.3&TARGET=stage"; wait cloudcart-promote 1
build cloudcart-promote 2 "VERSION=1.0.3&TARGET=prod"; approve 2; wait cloudcart-promote 2
curl -s localhost:9100/cloudcart/health; echo; cat /home/claude/jenkins-lab/nginx178/live.conf
sed -i 's#"/health", "/api/\*"#"/health", "/apis/*"#' /home/claude/jenkins-lab/repo178/src/main/java/academy/cloudcart/ApiServlet.java; git commit -qam "Rename API path"
build cloudcart-ci 4; wait cloudcart-ci 4
build cloudcart-promote 3 "VERSION=1.0.4&TARGET=prod"; approve 3; wait cloudcart-promote 3
curl -s localhost:9100/cloudcart/health; echo
build cloudcart-promote 4 "VERSION=1.0.1&TARGET=prod"; approve 4; wait cloudcart-promote 4
curl -s localhost:9100/cloudcart/health; echo; cat /tmp/chat178.log
