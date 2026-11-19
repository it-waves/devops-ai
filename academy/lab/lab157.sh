#!/bin/sh
# Lesson 157 lab: build and test CloudCart with Maven in Jenkins.  Usage: lab157.sh up | repo | bad | fix | down
# Needs the Jenkins from lesson 155 (lab155.sh up), Java, Maven and git. Everything lives in ~/jenkins-lab157. Not for root.
H=$HOME/jenkins-lab157; R=$H/cloudcart-repo; J=$HOME/jenkins-lab155
[ "$(id -u)" = 0 ] && { echo "Use a normal user, not root."; exit 1; }
case "$1" in
up) # restart Jenkins so that it may check out a repository on this machine (labs only)
  pkill -f "$J/jenkins.war"; sleep 3
  JENKINS_HOME=$J/home nohup java -Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true -jar $J/jenkins.war --httpPort=8080 > $J/jenkins.log 2>&1 &
  until curl -s -o /dev/null localhost:8080/login; do sleep 3; done; echo "Jenkins is up. Install the plugin 'Maven Integration' if it is missing.";;
repo) # a fresh CloudCart repository that contains a Jenkinsfile
  mkdir -p $H/src && rm -rf $R && git clone -q --depth 1 https://github.com/it-waves/devops-ai $H/src/all 2>/dev/null || (cd $H/src/all && git pull -q)
  mkdir -p $R && cp -r $H/src/all/cloudcart/. $R/ && rm -rf $R/target $R/e2e
  cat > $R/Jenkinsfile <<'X'
pipeline {
  agent any
  tools { maven 'maven-3.9' }
  environment { MVN = 'mvn -B -ntp -Dmaven.repo.local=$HOME/jenkins-lab157/m2' }
  stages {
    stage('Build') { steps { sh '$MVN -DskipTests clean compile' } }
    stage('Test') {
      steps { sh '$MVN test' }
      post { always { junit 'target/surefire-reports/*.xml' } }
    }
    stage('Package') {
      steps {
        sh '$MVN -DskipTests package'
        archiveArtifacts artifacts: 'target/*.war', fingerprint: true
      }
    }
  }
  post { failure { echo 'Build failed: read the Test stage first' } }
}
X
  (cd $R && printf 'target/\n' > .gitignore && git init -q -b main && git add -A && git commit -q -m "CloudCart with a Jenkinsfile")
  echo "Repository: $R   (use this path as the Repository URL, branch */main)";;
bad) sed -i 's/subtotal >= FREE_SHIPPING_CENTS/subtotal > FREE_SHIPPING_CENTS/' $R/src/main/java/academy/cloudcart/Pricing.java && (cd $R && git commit -qam "Shipping: free shipping only above the threshold") && echo "bad commit made: build now, the Test stage should fail";;
fix) sed -i 's/subtotal > FREE_SHIPPING_CENTS/subtotal >= FREE_SHIPPING_CENTS/' $R/src/main/java/academy/cloudcart/Pricing.java && (cd $R && git commit -qam "Fix: free shipping starts AT the threshold") && echo "fixed: build again";;
down) rm -rf $H; echo "lab files removed (Jenkins from lesson 155 is untouched)";;
*) echo "usage: lab157.sh up|repo|bad|fix|down";;
esac
