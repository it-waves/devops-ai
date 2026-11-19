#!/bin/sh
# Lesson 156 lab: four ready-made Jenkins files (declarative pipelines) to paste into a Pipeline job.
# Usage: lab156.sh files | show N | clean     (N = 1..4). Use it with the Jenkins from lesson 155 (lab155.sh up).
H=$HOME/jenkins-lab156
case "$1" in
files)
  mkdir -p $H
  cat > $H/Jenkinsfile.v1 <<'X'
pipeline {
  agent any
  stages {
    stage('Hello') {
      steps {
        echo 'Hello from my first pipeline'
      }
    }
  }
}
X
  cat > $H/Jenkinsfile.v2 <<'X'
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo Building CloudCart'
      }
    }
    stage('Test') {
      steps {
        sh 'echo Running tests'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo Deploying to staging'
      }
    }
  }
}
X
  sed '$d' $H/Jenkinsfile.v2 > $H/Jenkinsfile.v3
  cat >> $H/Jenkinsfile.v3 <<'X'
  post {
    always { echo 'Pipeline finished' }
    success { echo 'Everything passed' }
    failure { echo 'Something failed: tell the team' }
  }
}
X
  sed "s/echo Running tests'/echo Running tests; exit 1'/" $H/Jenkinsfile.v3 > $H/Jenkinsfile.v4
  echo "Written to $H: Jenkinsfile.v1 .. v4. Paste one into a Pipeline job (Definition: Pipeline script).";;
show) cat $H/Jenkinsfile.v${2:-1};;
clean) rm -rf $H; echo "lab files removed";;
*) echo "usage: lab156.sh files|show N|clean";;
esac
