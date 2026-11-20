#!/bin/sh
# Lesson 162 lab: back up, restore, upgrade and triage Jenkins.
# Usage: lab162.sh up | backup | restore JOB | old | down      Own machine only. Needs the Jenkins from lesson 155, tar and Java.
J=${JENKINS_HOME:-$HOME/.jenkins}; B=$HOME/jenkins-lab162
case "$1" in
up) mkdir -p $B/backups
  curl -s -o /dev/null -m3 localhost:8080 && echo "Jenkins is up on 8080" || echo "Jenkins is NOT up on 8080"
  [ -d "$J" ] && echo "Jenkins home: $J" || echo "Set JENKINS_HOME to your Jenkins home folder"
  command -v java >/dev/null && echo "Java found" || echo "Java is missing"; echo "Backups go to $B/backups";;
backup) mkdir -p $B/backups; F=$B/backups/jenkins-backup.tgz
  tar czf $F --exclude=workspace --exclude=caches -C "$J" . && ls -lh $F
  echo "Now copy it to another disk or server. A copy on the same disk is not a backup.";;
restore) [ -n "$2" ] || { echo "usage: lab restore JOBNAME"; exit 1; }
  tar xzf $B/backups/jenkins-backup.tgz -C "$J" ./jobs/$2 && ls "$J/jobs"
  echo "Now: Manage Jenkins > Reload Configuration from Disk";;
old) mkdir -p $B/old/home; cd $B/old
  [ -f old.war ] || curl -sL -o old.war https://repo.jenkins-ci.org/releases/org/jenkins-ci/main/jenkins-war/2.555.3/jenkins-war-2.555.3.war
  JENKINS_HOME=$B/old/home nohup java -Djenkins.install.runSetupWizard=false -jar old.war --httpPort=8081 > old.log 2>&1 &
  echo "Old Jenkins 2.555.3 starting on http://localhost:8081 (no security: throwaway only)"
  echo "Upgrade drill: stop it, tar czf the home, replace the war with your current jenkins.war, start it again.";;
down) pkill -f 'httpPort=8081'; rm -rf $B; echo "Throwaway Jenkins stopped and lab files removed. Your real Jenkins home is untouched.";;
*) echo "usage: lab162.sh up|backup|restore JOB|old|down";;
esac
