#!/bin/sh
# lab104.sh : MC12-O01 Tomcat: servlet container, JVM, WAR, connectors, contexts. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless curl unzip), internet access (Tomcat about 14 MB), about 1 GB of free memory.
# Mission: start a real Tomcat, deploy a WAR, look inside the WAR, find the connector port, and explain the five pieces in your own words.
D=${LAB104_DIR:-/opt/lab104}
U=${SUDO_USER:-root}
TV=10.1.34
TURL=${LAB104_TOMCAT_URL:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin/apache-tomcat-$TV.tar.gz}
as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- "$@"; fi; }
down() {
  [ -x $D/tomcat/bin/shutdown.sh ] && as env -u JAVA_TOOL_OPTIONS $D/tomcat/bin/shutdown.sh >/dev/null 2>&1; sleep 3
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1; rm -rf "${D:?}"; true
}
up() {
  for t in java curl unzip tar; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl unzip"; exit 1; }; done
  command -v jar >/dev/null 2>&1 || { echo "jar not found: install the full JDK (openjdk-21-jdk-headless)"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/demo/w/WEB-INF
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TURL" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }
  rm -f $D/t.tgz
  printf '<h1>Hello from a WAR</h1>\n<p>This page is inside hello.war.</p>\n' > $D/demo/w/index.html
  cat > $D/demo/w/WEB-INF/web.xml <<'EOF_W'
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee" version="6.0">
  <display-name>hello</display-name>
  <welcome-file-list><welcome-file>index.html</welcome-file></welcome-file-list>
</web-app>
EOF_W
  ( cd $D/demo/w && jar cf ../hello.war . ) && rm -rf $D/demo/w
  cat > $D/TASKS.txt <<'EOF_K'
LAB 104 : MC12 Tomcat, the five pieces.   Everything is in /opt/lab104
Tomcat is unpacked in /opt/lab104/tomcat, and demo/hello.war is a tiny web application. Nothing is running yet.

1  Start Tomcat:  /opt/lab104/tomcat/bin/startup.sh   Then  curl -s -o /dev/null -w '%{http_code}\n' localhost:8080   must say 200.
2  Deploy the WAR: copy demo/hello.war into tomcat/webapps. Wait up to 20 seconds (Tomcat looks for new WARs every 10 seconds). Then  curl localhost:8080/hello/  shows "Hello from a WAR".
3  Look inside the WAR (it is a zip file):  unzip -l demo/hello.war > war-list.txt   (war-list.txt in /opt/lab104)
4  Find the connector in tomcat/conf/server.xml (hint: grep -n "<Connector" tomcat/conf/server.xml). Which port does it listen on?
5  Write facts.txt in /opt/lab104, four lines, in your own words (12+ characters each):
     jvm: ...        connector: ... (include its port number)        context: ...        war: ...
Then:  lab check     (all 5 must pass)       and later:  lab down   (it stops Tomcat and removes everything)
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab104 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/tomcat ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8080/); if [ "$c" = 200 ]; then pass "1 Tomcat is running and answers on port 8080"; else fail "1 Tomcat does not answer 200 on port 8080: start it with tomcat/bin/startup.sh"; fi
  if curl -s -m 5 localhost:8080/hello/ | grep -q 'Hello from a WAR'; then pass "2 hello.war is deployed and answers on /hello/"; else fail "2 /hello/ does not answer: copy demo/hello.war into tomcat/webapps and wait up to 20 seconds"; fi
  if grep -q 'WEB-INF/web.xml' $D/war-list.txt 2>/dev/null && grep -q 'index.html' $D/war-list.txt; then pass "3 war-list.txt shows what is inside the WAR"; else fail "3 war-list.txt must hold the output of: unzip -l demo/hello.war"; fi
  F=$D/facts.txt
  if grep -qiE '^jvm:.{12,}' $F 2>/dev/null && grep -qiE '^connector:.{12,}' $F && grep -qiE '^context:.{12,}' $F && grep -qiE '^war:.{12,}' $F; then pass "4 facts.txt has jvm, connector, context and war lines"; else fail "4 facts.txt needs four lines: jvm: ... connector: ... context: ... war: ...  (12+ characters each)"; fi
  p=$(grep -o '<Connector port="[0-9]*"' $D/tomcat/conf/server.xml | head -1 | grep -o '[0-9][0-9]*')
  if [ -n "$p" ] && grep -qiE "^connector:.*$p" $F 2>/dev/null; then pass "5 the connector line names the real port ($p)"; else fail "5 the connector: line must include the port from conf/server.xml"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab104 is set up in $D" || echo "lab104 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab104 removed";; status) status;; *) echo "usage: lab104.sh up|check|down|status"; exit 2;; esac
