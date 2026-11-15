#!/bin/sh
# lab112.sh : MC12 mastery evidence: take over an inherited Tomcat, repair it, harden it and prove it. Run with sudo, on any Linux machine with a JDK, curl and ss.
#   up | check | down | status
# Needs: sudo apt install -y openjdk-21-jdk-headless curl iproute2     internet (Tomcat 14 MB), about 1 GB of memory, ports 8088 and 8098 free.
# Mission: a colleague left a Tomcat behind. The cart does not load, the server listens on every network, and its stop word is the default. Fix it, harden it, prove it, write a report.
D=${LAB112_DIR:-/opt/lab112}
OWNER=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB112_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
F=apache-tomcat-$TV.tar.gz
down() {
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1
  rm -rf "${D:?}"; true
}
mkwar() { # output-file  good|bad   (health.jsp comes from stdin)
  w=$D/build/w; rm -rf $w; mkdir -p $w/WEB-INF
  printf '<!DOCTYPE html><html><head><title>CloudCart</title><style>body{font-family:sans-serif;background:#0f2a2e;color:#eaf4f4;text-align:center;padding-top:18vh}h1{font-size:64px;color:#f0c987}p{font-size:28px}b{background:#7ee6a0;color:#0b2023;padding:6px 18px;border-radius:12px}</style></head><body><h1>CloudCart</h1><p><b>Release 1.0</b></p><p>The cart service is running.</p></body></html>\n' > $w/index.html
  if [ "$2" = good ]; then
    printf '<?xml version="1.0" encoding="UTF-8"?>\n<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee" version="6.0">\n  <display-name>cart</display-name>\n</web-app>\n' > $w/WEB-INF/web.xml
  else
    printf '<?xml version="1.0" encoding="UTF-8"?>\n<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee" version="6.0">\n  <display-name>cart</display-name>\n' > $w/WEB-INF/web.xml
  fi
  cat > $w/health.jsp
  ( cd $w && jar cf "$1" . )
}
up() {
  for t in java jar curl tar ss; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl iproute2"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  for p in 8088 8098; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/releases $D/data $D/build
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  T=$D/tomcat
  # the inherited server: port 8088 on every network, default stop word SHUTDOWN
  sed -i 's#<Connector port="8080"#<Connector port="8088"#; s#<Server port="8005"#<Server port="8098"#; s#<Engine name="Catalina" defaultHost="localhost">#<Engine name="Catalina" defaultHost="localhost" backgroundProcessorDelay="2">#' $T/conf/server.xml
  rm -rf $T/webapps/docs $T/webapps/examples $T/webapps/host-manager $T/webapps/manager $T/webapps/ROOT
  printf '%s\n' 'CATALINA_PID=$CATALINA_BASE/tomcat.pid' > $T/bin/setenv.sh; chmod 755 $T/bin/setenv.sh
  echo 'currency=USD' > $D/data/app.properties
  cat > $D/build/health.jsp <<'EOF_J'
<%@ page contentType="text/plain" import="java.io.*,java.util.*" %><%
Properties p = new Properties();
try (FileInputStream in = new FileInputStream(System.getProperty("catalina.base") + "/../data/app.properties")) { p.load(in); } catch (Exception e) { }
if (p.getProperty("shop.name") == null) {
  application.log("health FAIL: shop.name is missing in data/app.properties");
  response.setStatus(503);
  out.print("DOWN: shop.name missing");
} else {
  out.print("UP " + p.getProperty("shop.name"));
}
%>
EOF_J
  mkwar $D/releases/cart-1.0.war good < $D/build/health.jsp
  mkwar $T/webapps/cart.war bad < $D/build/health.jsp
  rm -rf $D/build
  chown -R "$OWNER": $D; chmod 755 $D
  cat > $D/TASKS.txt <<EOF_K
LAB 112 : MC12 mastery. Take over an inherited Tomcat.   Everything is in /opt/lab112
Tomcat is unpacked in tomcat/ and is not running. Its port is 8088 (stop port 8098). A colleague left a broken release in webapps/cart.war.
releases/cart-1.0.war is the last known good release. The app reads data/app.properties. All commands run as you (no sudo).

1  Start it:  tomcat/bin/startup.sh     then  curl -si localhost:8088/cart/ | head -n 1     the cart does not answer 200. Read why:
   grep -m1 -o 'XML document.*' tomcat/logs/catalina.*.log
2  Redeploy the good release:  cp releases/cart-1.0.war tomcat/webapps/cart.war      wait 6 seconds, then  curl -s localhost:8088/cart/health.jsp
   Health says DOWN. Read why in the log (grep health tomcat/logs/localhost.*.log), then add the missing setting to data/app.properties  (shop.name=CloudCart).
3  Look at who can reach the port:  ss -ltn | grep 8088      It listens on every network. Stop Tomcat, and in tomcat/conf/server.xml
   add  address="127.0.0.1"  to the Connector, and change the stop word SHUTDOWN in the Server line to a word of your own. Start Tomcat again.
4  Write  health.sh  here (chmod +x): it prints  health: <code>  and exits 0 only when /cart/health.jsp answers 200.
5  Write  report.txt  with four lines that start with  FOUND:  FIXED:  PROOF:  CLEANUP:
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown "$OWNER": $D/TASKS.txt
  echo "lab112 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/tomcat ] || { echo "lab not set up: run  lab up"; exit 1; }
  T=$D/tomcat; ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8088/cart/ 2>/dev/null)
  if [ "$c" = 200 ] && cat $T/logs/catalina.*.log 2>/dev/null | grep -q 'XML document structures'; then pass "1 the broken release is found in the log and cart answers 200"; else fail "1 start Tomcat, read why cart fails in the log, redeploy cart-1.0.war (cart answers ${c:-nothing})"; fi
  l=$(ss -ltn 2>/dev/null | grep ':8088 ')
  if echo "$l" | grep -q '127.0.0.1:8088' && ! echo "$l" | grep -Eq '(\*|0.0.0.0|\[::\]):8088'; then pass "2 port 8088 listens on 127.0.0.1 only"; else fail "2 bind the Connector to 127.0.0.1 and restart (ss shows: ${l:-nothing})"; fi
  w=$(grep -o 'shutdown="[^"]*"' $T/conf/server.xml | head -n 1)
  if [ -n "$w" ] && [ "$w" != 'shutdown="SHUTDOWN"' ] && [ "$w" != 'shutdown=""' ]; then pass "3 the stop word is no longer the default"; else fail "3 change the stop word SHUTDOWN in conf/server.xml, then restart"; fi
  b=$(curl -s -m 5 localhost:8088/cart/health.jsp 2>/dev/null)
  if grep -Eq '^shop.name=.' $D/data/app.properties && echo "$b" | grep -q '^UP'; then pass "4 the setting shop.name is set and health says UP"; else fail "4 add shop.name=CloudCart to data/app.properties (health says: $(echo "${b:-nothing}" | head -c 30))"; fi
  if [ -x $D/health.sh ] && (cd $D && ./health.sh >/dev/null 2>&1) && [ "$(grep -c -E '^(FOUND|FIXED|PROOF|CLEANUP):' $D/report.txt 2>/dev/null)" -ge 4 ]; then pass "5 health.sh exits 0, report.txt has its 4 lines"; else fail "5 write health.sh (chmod +x, exit 0 while healthy) and report.txt with FOUND: FIXED: PROOF: CLEANUP: lines"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab112 is set up in $D" || echo "lab112 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab112 removed";; status) status;; *) echo "usage: lab112.sh up|check|down|status"; exit 2;; esac
