#!/bin/sh
# Lesson 158 lab: credentials in Jenkins.  Usage: lab158.sh up | files | down
# Needs the Jenkins from lesson 155 (lab155.sh up). Files live in ~/jenkins-lab158. Fake secrets only. Not for root.
H=$HOME/jenkins-lab158
[ "$(id -u)" = 0 ] && { echo "Use a normal user, not root."; exit 1; }
case "$1" in
up) mkdir -p $H; curl -s -o /dev/null localhost:8080/login && echo "Jenkins is up. In Manage Jenkins > Credentials add: Secret text, ID deploy-token (value tok-9f3a-live-8812 is fake), and Username with password, ID registry-login." || echo "Start Jenkins first: lab155.sh up";;
files) mkdir -p $H
cat > $H/Jenkinsfile.leak <<'X'
pipeline {
  agent any
  environment { DEPLOY_TOKEN = 'tok-9f3a-live-8812' }
  stages { stage('Deploy') { steps { sh 'echo Deploying with $DEPLOY_TOKEN' } } }
}
X
cat > $H/Jenkinsfile.safe <<'X'
pipeline {
  agent any
  stages { stage('Deploy') { steps {
    withCredentials([string(credentialsId: 'deploy-token', variable: 'TOKEN')]) { sh 'echo Deploying with $TOKEN' }
  } } }
}
X
cat > $H/Jenkinsfile.both <<'X'
pipeline {
  agent any
  environment { APP_ENV = 'staging' }
  stages { stage('Deploy') { steps {
    withCredentials([string(credentialsId: 'deploy-token', variable: 'TOKEN'),
                     usernamePassword(credentialsId: 'registry-login', usernameVariable: 'REG_USER', passwordVariable: 'REG_PASS')]) {
      sh 'echo env=$APP_ENV build=$BUILD_NUMBER user=$REG_USER pass=$REG_PASS'
    }
  } } }
}
X
echo "Written to $H: Jenkinsfile.leak, Jenkinsfile.safe, Jenkinsfile.both. Paste each into a Pipeline job and read the console.";;
down) rm -rf $H; echo "lab files removed. Delete the two credentials and the secrets-demo job in the Jenkins UI."; ;;
*) echo "usage: lab158.sh up|files|down";;
esac
