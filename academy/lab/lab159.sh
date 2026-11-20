#!/bin/sh
# Lesson 159 lab: triggers, a SonarQube quality gate and a Nexus release.
# Usage: lab159.sh up | repo | bug | fix | bump | files | down      Not for root. Own machine only.
# Needs: the Jenkins from lesson 155 (credentials sonar-token and nexus-deployer added as in the video),
#        SonarQube on :9000 with a gate that fails on new bugs, Nexus on :8081 with the repo corp-releases (disable redeploy), Maven.
H=$HOME/jenkins-lab159; R=$H/repo
[ "$(id -u)" = 0 ] && { echo "Use a normal user, not root."; exit 1; }
commit() { (cd $R && git add -A && git -c user.name='Dana Developer' -c user.email=dana@cloudcart.example commit -q -m "$1" && echo "committed: $1"); }
D=$R/src/main/java/academy/cloudcart
case "$1" in
up) mkdir -p $H
  for p in "Jenkins 8080" "SonarQube 9000" "Nexus 8081"; do set -- $p; curl -s -o /dev/null -m3 localhost:$2 && echo "$1 is up" || echo "$1 is NOT up on port $2"; done;;
repo) mkdir -p $H; [ -d $R ] || git clone -q https://github.com/it-waves/cloudcart $R; echo "repo ready: $R  (point the Jenkins jobs at this path)";;
bug) printf 'package academy.cloudcart;\n\npublic class Coupon {\n    public boolean isValid(int percent) {\n        return percent == percent && percent <= 100;\n    }\n}\n' > $D/Coupon.java; commit "Add coupon validation";;
fix) printf 'package academy.cloudcart;\n\npublic class Coupon {\n    public boolean isValid(int percent) {\n        return percent >= 0 && percent <= 100;\n    }\n}\n' > $D/Coupon.java; commit "Fix coupon validation: check the lower bound";;
bump) sed -i '0,/<version>0.2.0<\/version>/s//<version>0.2.1<\/version>/' $R/pom.xml; commit "Release 0.2.1";;
files) mkdir -p $H; cat > $H/Jenkinsfile.quality <<'X'
pipeline {
  agent any
  stages {
    stage('Test') { steps { sh 'mvn -B clean verify' } }
    stage('SonarQube') { steps { withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
      sh 'mvn -B org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.host.url=http://localhost:9000 -Dsonar.projectKey=cloudcart -Dsonar.qualitygate.wait=true' } } }
  }
}
X
  cat > $H/Jenkinsfile.publish <<'X'
pipeline {
  agent any
  stages { stage('Publish') { steps { withCredentials([usernamePassword(credentialsId: 'nexus-deployer', usernameVariable: 'NEXUS_USER', passwordVariable: 'NEXUS_PASS')]) {
    sh 'mvn -B -s settings.xml -DskipTests clean deploy -DaltDeploymentRepository=corp::default::http://localhost:8081/repository/corp-releases/' } } } }
}
X
  echo "Written to $H: Jenkinsfile.quality, Jenkinsfile.publish (settings.xml must map server id corp to NEXUS_USER and NEXUS_PASS).";;
down) rm -rf $H; echo "lab files removed. Delete the three jobs and the Sonar and Nexus test data in their UIs.";;
*) echo "usage: lab159.sh up|repo|bug|fix|bump|files|down";;
esac
