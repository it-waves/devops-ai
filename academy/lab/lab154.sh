#!/bin/sh
# Lesson 154 lab: a throw-away Jenkins on port 8080. Usage: lab154.sh up | down
# Needs Java 21 and internet. Everything lives in ~/jenkins-lab154; "down" removes it.
H=$HOME/jenkins-lab154; J=localhost:8080; A="-u admin:devops-lab"
JOBS=${JOBS_DIR:-$(dirname "$0")/../lab154-jobs}
case "$1" in
up)
  mkdir -p $H/home/init.groovy.d
  [ -f $H/jenkins.war ] || curl -fL -o $H/jenkins.war https://get.jenkins.io/war-stable/latest/jenkins.war || exit 1
  cat > $H/home/init.groovy.d/admin.groovy <<'G'
import jenkins.model.*
import hudson.security.*
def j = Jenkins.get()
def r = new HudsonPrivateSecurityRealm(false); r.createAccount('admin', 'devops-lab')
j.setSecurityRealm(r); def s = new FullControlOnceLoggedInAuthorizationStrategy(); s.setAllowAnonymousRead(false); j.setAuthorizationStrategy(s); j.save()
G
  JENKINS_HOME=$H/home nohup java -Djenkins.install.runSetupWizard=false -jar $H/jenkins.war --httpPort=8080 > $H/jenkins.log 2>&1 &
  echo "Starting Jenkins (about a minute)..."; until curl -s -o /dev/null $A $J/login; do sleep 3; done
  echo "Open http://localhost:8080  user admin  password devops-lab"
  echo "Install plugins: Manage Jenkins > Plugins > Available (Pipeline, Git), then run: lab154.sh jobs";;
jobs)
  C=$(curl -s $A -c $H/cj $J/crumbIssuer/api/json | python3 -c "import sys,json;d=json.load(sys.stdin);print(d['crumbRequestField']+':'+d['crumb'])")
  for j in slow-build hello-pipeline broken-pipeline; do curl -s $A -b $H/cj -H "$C" -H 'Content-Type: application/xml' -X POST "$J/createItem?name=$j" --data-binary @$JOBS/$j/config.xml -o /dev/null; done; echo "jobs created";;
down)
  pkill -f "$H/jenkins.war"; sleep 2; rm -rf $H; echo "lab removed";;
*) echo "usage: lab154.sh up|jobs|down";;
esac
