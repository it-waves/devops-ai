#!/bin/sh
# Lesson 160 lab: a distributed Jenkins build with one agent, labels, executors, archive and stash.
# Usage: lab160.sh up | agent | files | down      Own machine only. Needs the Jenkins from lesson 155, Java and Maven.
H=$HOME/jenkins-lab160
case "$1" in
up) mkdir -p $H
  curl -s -o /dev/null -m3 localhost:8080 && echo "Jenkins is up" || echo "Jenkins is NOT up on port 8080"
  command -v java >/dev/null && echo "Java found" || echo "Java is missing"
  command -v mvn >/dev/null && echo "Maven found" || echo "Maven is missing";;
agent) # creates a separate user so the agent has its own home, then prints the connect command
  id agent >/dev/null 2>&1 || sudo useradd -m -s /bin/bash agent
  echo "In Jenkins: Manage Jenkins > Nodes > New Node > name build-agent-1 > Permanent Agent."
  echo "Set executors 2, remote directory /home/agent/jenkins, label maven, launch by connecting to the controller."
  echo "Then, on this machine, as the agent user, run the two commands the node page shows:"
  echo "  curl -sO http://localhost:8080/jnlpJars/agent.jar"
  echo "  java -jar agent.jar -url http://localhost:8080/ -secret <secret> -name build-agent-1 -webSocket -workDir /home/agent/jenkins";;
files) mkdir -p $H
  cat > $H/Jenkinsfile.test <<'X'
pipeline {
  agent { label 'maven' }
  stages { stage('Where am I') { steps { sh 'hostname; whoami; pwd'; sh 'sleep 25' } } }
}
X
  cat > $H/Jenkinsfile.app <<'X'
pipeline {
  agent none
  stages {
    stage('Build on the agent') {
      agent { label 'maven' }
      steps {
        git url: 'https://github.com/it-waves/cloudcart', branch: 'main'
        sh 'mvn -B -ntp -DskipTests clean package'
        archiveArtifacts artifacts: 'target/*.war', fingerprint: true
        stash name: 'app', includes: 'target/*.war'
      }
    }
    stage('Use it elsewhere') {
      agent { label 'built-in' }
      steps { unstash 'app'; sh 'pwd; ls -l target' }
    }
  }
}
X
  cat > $H/Jenkinsfile.wrong-label <<'X'
pipeline {
  agent { label 'windows' }
  stages { stage('Hello') { steps { echo 'hello' } } }
}
X
  echo "Written to $H: Jenkinsfile.test, Jenkinsfile.app, Jenkinsfile.wrong-label";;
down) pkill -u agent -f agent.jar 2>/dev/null; rm -rf $H
  echo "Agent process stopped and lab files removed. Delete the node and the three jobs in Jenkins. Remove the user with: sudo userdel -r agent";;
*) echo "usage: lab160.sh up|agent|files|down";;
esac
