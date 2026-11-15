#!/bin/sh
# lab108.sh : MC12-O05 Read Tomcat's logs and fix two failures. Run with sudo, on any Linux machine with a JDK (no systemd needed).
#   up | check | down | status
# Needs: JDK, curl, tar (sudo apt install -y openjdk-21-jdk-headless curl), internet (Tomcat 14 MB), about 1 GB of memory, port 8082 free.
# Mission: Tomcat starts but the cart app is dead and its health page fails. Read the logs, name both causes, fix both, count the errors.
D=${LAB108_DIR:-/opt/lab108}
OWNER=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB108_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
F=apache-tomcat-$TV.tar.gz
down() {
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1
  rm -rf "${D:?}"; true
}
up() {
  for t in java curl tar; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  if curl -s -o /dev/null -m 2 localhost:8082; then echo "port 8082 is already in use: stop what uses it first"; exit 1; fi
  down; mkdir -p $D
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  sed -i 's#<Connector port="8080"#<Connector port="8082"#' $D/tomcat/conf/server.xml
  sed -i 's#prefix="localhost_access_log"#buffered="false" prefix="localhost_access_log"#' $D/tomcat/conf/server.xml
  rm -rf $D/tomcat/webapps/docs $D/tomcat/webapps/examples $D/tomcat/webapps/host-manager $D/tomcat/webapps/manager
  A=$D/tomcat/webapps/cart; mkdir -p $A/WEB-INF
  cat > $A/index.html <<'EOF_I'
<!DOCTYPE html><html><head><title>CloudCart</title></head><body><h1>CloudCart 1.0</h1><p>The cart service is running.</p></body></html>
EOF_I
  cat > $A/health.jsp <<'EOF_H'
<%@ page import="java.nio.file.*" %>
<% String env = new String(Files.readAllBytes(Paths.get("/opt/lab108/config/cart.properties"))).trim(); out.print("OK " + env); %>
EOF_H
  cat > $A/WEB-INF/web.xml <<'EOF_W'
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee" version="6.0">
  <display-name>cart</display-name>
  <listener>
    <listener-class>com.cloudcart.StartupListner</listener-class>
  </listener>
</web-app>
EOF_W
  mkdir -p $D/config; chown -R "$OWNER": $D; chmod 755 $D
  cat > $D/TASKS.txt <<EOF_K
LAB 108 : MC12 Read the logs and fix two failures.   Everything is in /opt/lab108
Tomcat is unpacked in tomcat/ (port 8082) and is NOT running. The cart app is in tomcat/webapps/cart. Logs go to tomcat/logs.

1  Start it:  tomcat/bin/startup.sh     then   curl localhost:8082   answers 200   (the home page; the cart app is not up yet)
2  curl -i localhost:8082/cart/  is 404. Read tomcat/logs/catalina.*.log, find the SEVERE line, and follow it to tomcat/logs/localhost.*.log for the exception.
   Fix the cause in tomcat/webapps/cart/WEB-INF/web.xml, restart Tomcat (shutdown.sh then startup.sh); /cart/ must answer 200.
3  curl -i localhost:8082/cart/health.jsp  is 500. Request it three times, then read tomcat/logs/localhost.*.log for the exception and the missing file.
   Create that file with one line:  staging   Then /cart/health.jsp answers 200 and prints OK staging.
4  Write what you found in /opt/lab108/diagnosis.txt, two lines (the exact exception class names from the logs):
     startup: <the exception that stopped the cart app from starting>
     health: <the exception behind the 500>
5  Count the 500 answers in tomcat/logs/localhost_access_log.*.txt and write one line in /opt/lab108/report.txt:   500s: <number>
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown "$OWNER": $D/TASKS.txt
  echo "lab108 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/tomcat ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8082/ 2>/dev/null)
  if [ "$c" = 200 ]; then pass "1 Tomcat is running and answers 200 on port 8082"; else fail "1 start Tomcat: tomcat/bin/startup.sh (localhost:8082 answers ${c:-nothing})"; fi
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8082/cart/ 2>/dev/null)
  if [ "$c" = 200 ]; then pass "2 /cart/ answers 200: the startup failure is fixed"; else fail "2 /cart/ answers ${c:-nothing}: read catalina.*.log and localhost.*.log, fix web.xml, restart Tomcat"; fi
  b=$(curl -s -m 5 localhost:8082/cart/health.jsp 2>/dev/null | tr -d '\n ')
  if [ "$b" = "OKstaging" ]; then pass "3 /cart/health.jsp prints OK staging"; else fail "3 /cart/health.jsp must print OK staging: read localhost.*.log for the missing file"; fi
  X=$D/diagnosis.txt
  if [ -f $X ] && grep -qi '^startup:.*ClassNotFoundException' $X && grep -qi '^health:.*NoSuchFileException' $X && cat $D/tomcat/logs/localhost.*.log | grep -q ClassNotFoundException && cat $D/tomcat/logs/localhost.*.log | grep -q NoSuchFileException; then pass "4 diagnosis.txt names both exceptions, and both are in the logs"; else fail "4 diagnosis.txt needs the lines  startup: <exception>  and  health: <exception>  taken from the logs"; fi
  n=$(cat $D/tomcat/logs/localhost_access_log.*.txt 2>/dev/null | grep -c '" 500 ')
  if [ "${n:-0}" -ge 1 ] && grep -qx "500s: $n" $D/report.txt 2>/dev/null; then pass "5 report.txt has the right count of 500 answers ($n)"; else fail "5 report.txt must hold the line  500s: N  where N counts the 500 answers in the access log (now ${n:-0})"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab108 is set up in $D" || echo "lab108 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab108 removed";; status) status;; *) echo "usage: lab108.sh up|check|down|status"; exit 2;; esac
