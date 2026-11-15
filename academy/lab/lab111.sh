#!/bin/sh
# lab111.sh : MC12-O08 Monitor Tomcat's health and recover a failed deployment. Run with sudo, on any Linux machine with a JDK and curl.
#   up | check | down | status
# Needs: sudo apt install -y openjdk-21-jdk-headless curl     internet (Tomcat 14 MB), about 1 GB of memory, ports 8087 and 8097 free.
# Mission: release 2.0 of the cart is about to ship broken. Watch the health endpoint, read the log, roll back, fix the cause and ship again.
D=${LAB111_DIR:-/opt/lab111}
OWNER=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB111_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
F=apache-tomcat-$TV.tar.gz
down() {
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1
  rm -rf "${D:?}"; true
}
mkwar() { # name version body-of-health.jsp
  w=$D/build/$1; rm -rf $w; mkdir -p $w/WEB-INF
  printf '<!DOCTYPE html><html><head><title>CloudCart</title><style>body{font-family:sans-serif;background:#0f2a2e;color:#eaf4f4;text-align:center;padding-top:18vh}h1{font-size:64px;color:#f0c987}p{font-size:28px}b{background:#7ee6a0;color:#0b2023;padding:6px 18px;border-radius:12px}</style></head><body><h1>CloudCart %s</h1><p><b>Release %s</b></p><p>The cart service is running.</p></body></html>\n' "$2" "$2" > $w/index.html
  cat > $w/WEB-INF/web.xml <<'EOF_W'
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee" version="6.0"><display-name>cart</display-name></web-app>
EOF_W
  cat > $w/health.jsp
  ( cd $w && jar cf $D/releases/cart-$2.war . )
}
up() {
  for t in java jar curl tar; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  for p in 8087 8097; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/releases $D/data
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  T=$D/tomcat
  sed -i 's#<Connector port="8080"#<Connector port="8087" address="127.0.0.1"#; s#<Server port="8005"#<Server port="8097"#; s#<Engine name="Catalina" defaultHost="localhost">#<Engine name="Catalina" defaultHost="localhost" backgroundProcessorDelay="2">#' $T/conf/server.xml
  rm -rf $T/webapps/docs $T/webapps/examples $T/webapps/host-manager $T/webapps/manager $T/webapps/ROOT
  printf '%s\n' 'CATALINA_PID=$CATALINA_BASE/tomcat.pid' > $T/bin/setenv.sh; chmod 755 $T/bin/setenv.sh
  echo 'db.url=jdbc:h2:mem:cart' > $D/data/db.properties
  mkwar v1 1.0 <<'EOF_J1'
<%@ page contentType="text/plain" %><% out.print("UP version 1.0"); %>
EOF_J1
  mkwar v2 2.0 <<'EOF_J2'
<%@ page contentType="text/plain" import="java.io.*,java.util.*" %><%
Properties p = new Properties();
try (FileInputStream in = new FileInputStream(System.getProperty("catalina.base") + "/../data/db.properties")) { p.load(in); } catch (Exception e) { }
if (p.getProperty("pool.size") == null) {
  application.log("health FAIL: setting pool.size is missing in data/db.properties");
  response.setStatus(503);
  out.print("DOWN version 2.0: pool.size missing");
} else {
  out.print("UP version 2.0 pool=" + p.getProperty("pool.size"));
}
%>
EOF_J2
  rm -rf $D/build
  cp $D/releases/cart-1.0.war $T/webapps/cart.war
  chown -R "$OWNER": $D; chmod 755 $D
  cat > $D/TASKS.txt <<EOF_K
LAB 111 : MC12 Monitor the health and recover a failed deployment.   Everything is in /opt/lab111
Tomcat is unpacked in tomcat/ and listens on 127.0.0.1:8087 (shutdown port 8097). It is not running.
releases/ holds cart-1.0.war (working) and cart-2.0.war (new, but it needs a setting that is missing). The app reads data/db.properties.
All commands run as you (no sudo): the ports are above 1024.

1  Start Tomcat:  tomcat/bin/startup.sh    then  curl localhost:8087/cart/health.jsp  answers  UP version 1.0
2  Write a script  health.sh  in this folder (chmod +x): it prints  health: <code>  from  curl -s -o /dev/null -w '%{http_code}' localhost:8087/cart/health.jsp
   and exits 0 only when the code is 200.   Watch it:  for i in 1 2 3; do ./health.sh; sleep 1; done
3  Ship release 2.0:  cp releases/cart-2.0.war tomcat/webapps/cart.war      Wait 5 seconds. The home page says 2.0, but health answers 503. Read why:
   curl localhost:8087/cart/health.jsp      and      grep health tomcat/logs/localhost.*.log
4  Roll back at once:  cp releases/cart-1.0.war tomcat/webapps/cart.war      health is 200 again.
5  Fix the cause:  echo pool.size=10 >> data/db.properties      then ship 2.0 again and confirm  UP version 2.0 pool=10
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown "$OWNER": $D/TASKS.txt
  echo "lab111 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/tomcat ] || { echo "lab not set up: run  lab up"; exit 1; }
  T=$D/tomcat; ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8087/cart/ 2>/dev/null)
  if [ "$c" = 200 ]; then pass "1 Tomcat answers 200 on 127.0.0.1:8087"; else fail "1 start Tomcat: tomcat/bin/startup.sh (8087 answers ${c:-nothing})"; fi
  if [ -x $D/health.sh ] && (cd $D && ./health.sh >/dev/null 2>&1); then pass "2 health.sh exists, is executable and exits 0 when healthy"; else fail "2 write health.sh, chmod +x, and it must exit 0 while the app is healthy"; fi
  n=$(cat $T/logs/catalina.*.log 2>/dev/null | grep -c 'Deployment of web application archive .*cart.war.* has finished')
  if [ "$n" -ge 4 ]; then pass "3 cart.war was deployed $n times: 1.0, bad 2.0, the rollback, and 2.0 again"; else fail "3 cart.war must be deployed 4 times: 1.0, 2.0, rollback to 1.0, 2.0 again (so far $n)"; fi
  if cat $T/logs/localhost.*.log 2>/dev/null | grep -q 'pool.size is missing'; then pass "4 the failure is in the log: pool.size is missing"; else fail "4 ship cart-2.0.war before the fix, so the log records why health failed"; fi
  b=$(curl -s -m 5 localhost:8087/cart/health.jsp 2>/dev/null)
  if grep -Eq '^pool.size=[0-9]+' $D/data/db.properties && echo "$b" | grep -q 'UP version 2.0'; then pass "5 the cause is fixed and release 2.0 is healthy"; else fail "5 add pool.size=10 to data/db.properties and ship 2.0 again (health says: ${b:-nothing})"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab111 is set up in $D" || echo "lab111 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab111 removed";; status) status;; *) echo "usage: lab111.sh up|check|down|status"; exit 2;; esac
