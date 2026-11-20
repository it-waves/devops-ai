#!/bin/sh
# Lesson 161 lab: approval gates, promotion, rollback and notifications in Jenkins.
# Usage: lab161.sh up | hook | files | down      Own machine only. Needs the Jenkins from lesson 155 and Maven.
H=$HOME/jenkins-lab161
case "$1" in
up) mkdir -p $H/deploy/dev $H/deploy/staging $H/deploy/prod
  curl -s -o /dev/null -m3 localhost:8080 && echo "Jenkins is up" || echo "Jenkins is NOT up on port 8080"
  command -v mvn >/dev/null && echo "Maven found" || echo "Maven is missing"
  echo "Deploy folders: $H/deploy/{dev,staging,prod}";;
hook) mkdir -p $H
  cat > $H/hook.py <<'X'
import http.server, json, time, html, os
F = os.path.expanduser('~/jenkins-lab161/inbox.json')
def load():
    try: return json.load(open(F))
    except Exception: return []
class H(http.server.BaseHTTPRequestHandler):
    def log_message(s, *a): pass
    def do_POST(s):
        b = s.rfile.read(int(s.headers.get('Content-Length', 0))).decode(); m = load(); m.append({'t': time.strftime('%H:%M:%S'), 'm': b}); json.dump(m, open(F, 'w')); s.send_response(200); s.end_headers(); s.wfile.write(b'ok')
    def do_GET(s):
        rows = ''.join('<p>%s  %s</p>' % (html.escape(x['t']), html.escape(x['m'])) for x in reversed(load())) or '<p>No notifications yet.</p>'
        s.send_response(200); s.send_header('Content-Type', 'text/html; charset=utf-8'); s.end_headers(); s.wfile.write(('<meta http-equiv=refresh content=2><h1>Team notifications</h1>' + rows).encode())
http.server.ThreadingHTTPServer(('127.0.0.1', 8099), H).serve_forever()
X
  (setsid nohup python3 $H/hook.py >/dev/null 2>&1 </dev/null &) ; echo "Inbox running: http://localhost:8099";;
files) mkdir -p $H
  cat > $H/Jenkinsfile.approval <<'X'
pipeline {
  agent any
  stages {
    stage('Build') { steps { echo 'Building CloudCart' } }
    stage('Approve') { steps { input message: 'Deploy to staging?', ok: 'Approve' } }
    stage('Deploy') { steps { echo 'Deployed to staging' } }
  }
}
X
  cat > $H/Jenkinsfile.release <<'X'
pipeline {
  agent any
  environment { DEPLOY = "$HOME/jenkins-lab161/deploy" }
  stages {
    stage('Build') {
      steps {
        git url: 'https://github.com/it-waves/cloudcart', branch: 'main'
        sh 'mvn -B -ntp -DskipTests clean package'
        archiveArtifacts artifacts: 'target/*.war'
      }
    }
    stage('Deploy DEV') { steps { sh 'cp target/*.war $DEPLOY/dev/cloudcart-$BUILD_NUMBER.war' } }
    stage('Approve STAGING') { steps { timeout(time: 1, unit: 'HOURS') { input message: 'Promote to staging?', ok: 'Approve' } } }
    stage('Deploy STAGING') { steps { sh 'cp target/*.war $DEPLOY/staging/cloudcart-$BUILD_NUMBER.war' } }
    stage('Approve PROD') { steps { timeout(time: 1, unit: 'HOURS') { input message: 'Release to production?', ok: 'Release', submitter: 'admin' } } }
    stage('Deploy PROD') {
      steps {
        sh 'cp target/*.war $DEPLOY/prod/cloudcart-$BUILD_NUMBER.war'
        sh 'ln -sfn $DEPLOY/prod/cloudcart-$BUILD_NUMBER.war $DEPLOY/prod/current.war'
        sh 'ls -l $DEPLOY/prod'
      }
    }
  }
  post {
    success { sh 'curl -s -d "cloudcart-release #$BUILD_NUMBER is live in production" http://localhost:8099/notify' }
    aborted { sh 'curl -s -d "cloudcart-release #$BUILD_NUMBER was stopped by a person" http://localhost:8099/notify' }
    failure { sh 'curl -s -d "cloudcart-release #$BUILD_NUMBER FAILED" http://localhost:8099/notify' }
  }
}
X
  cat > $H/Jenkinsfile.rollback <<'X'
pipeline {
  agent any
  environment { DEPLOY = "$HOME/jenkins-lab161/deploy" }
  parameters { choice(name: 'VERSION', choices: ['2', '1'], description: 'Release number to go back to') }
  stages {
    stage('Rollback') {
      steps {
        sh 'ln -sfn $DEPLOY/prod/cloudcart-${VERSION:-2}.war $DEPLOY/prod/current.war'
        sh 'readlink $DEPLOY/prod/current.war'
      }
    }
  }
  post { success { sh 'curl -s -d "production rolled back to release #${VERSION:-2}" http://localhost:8099/notify' } }
}
X
  echo "Written to $H: Jenkinsfile.approval, Jenkinsfile.release, Jenkinsfile.rollback";;
down) pkill -f jenkins-lab161/hook.py; rm -rf $H
  echo "Inbox stopped and lab files removed. Delete the three jobs in Jenkins.";;
*) echo "usage: lab161.sh up|hook|files|down";;
esac
