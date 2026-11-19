#!/bin/sh
# Lesson 155 lab: a brand new Jenkins on port 8080 that shows the real setup wizard. Usage: lab155.sh up | pass | down
# Needs Java 21 and internet. Everything lives in ~/jenkins-lab155; "down" removes it. Run it as a normal user, never root.
H=$HOME/jenkins-lab155
[ "$(id -u)" = 0 ] && { echo "Do not run Jenkins as root. Use a normal user."; exit 1; }
case "$1" in
up)
  mkdir -p $H/home
  [ -f $H/jenkins.war ] || curl -fL -o $H/jenkins.war https://get.jenkins.io/war-stable/latest/jenkins.war || exit 1
  JENKINS_HOME=$H/home nohup java -jar $H/jenkins.war --httpPort=8080 > $H/jenkins.log 2>&1 &
  echo "Starting Jenkins (about a minute)..."; until curl -s -o /dev/null localhost:8080/login; do sleep 3; done
  echo "Open http://localhost:8080  then run: lab155.sh pass";;
pass) cat $H/home/secrets/initialAdminPassword;;
down) pkill -f "$H/jenkins.war"; sleep 2; rm -rf $H; echo "lab removed";;
*) echo "usage: lab155.sh up|pass|down";;
esac
