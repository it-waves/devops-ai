#!/bin/sh
# lab110.sh : MC12-O07 Secure Tomcat's management interfaces and service permissions. Run with sudo, on any Linux machine with a JDK and curl.
#   up | check | down | status
# Needs: sudo apt install -y openjdk-21-jdk-headless curl     internet (Tomcat 14 MB), about 1 GB of memory, ports 8086 and 8096 free.
# Mission: Tomcat's Manager runs with a weak default user, open to the world, with a shutdown port and loose file permissions. Lock all of it down.
D=${LAB110_DIR:-/opt/lab110}
OWNER=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB110_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
F=apache-tomcat-$TV.tar.gz
down() {
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1
  rm -rf "${D:?}"; true
}
up() {
  for t in java curl tar; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  for p in 8086 8096; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  T=$D/tomcat
  sed -i 's#<Connector port="8080"#<Connector port="8086" address="127.0.0.1"#; s#<Server port="8005"#<Server port="8096"#' $T/conf/server.xml
  rm -rf $T/webapps/docs $T/webapps/examples $T/webapps/host-manager
  printf '%s\n' 'CATALINA_PID=$CATALINA_BASE/tomcat.pid' > $T/bin/setenv.sh; chmod 755 $T/bin/setenv.sh
  A=$T/webapps/cart; mkdir -p $A/WEB-INF
  cat > $A/index.html <<'EOF_I'
<!DOCTYPE html><html><head><title>CloudCart</title></head><body><h1>CloudCart 1.0</h1><p>The cart service is running.</p></body></html>
EOF_I
  cat > $A/WEB-INF/web.xml <<'EOF_W'
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee" version="6.0"><display-name>cart</display-name></web-app>
EOF_W
  cat > $T/conf/tomcat-users.xml <<'EOF_U'
<?xml version="1.0" encoding="UTF-8"?>
<tomcat-users xmlns="http://tomcat.apache.org/xml" version="1.0">
  <role rolename="manager-gui"/>
  <user username="admin" password="admin" roles="manager-gui"/>
</tomcat-users>
EOF_U
  cat > $T/webapps/manager/META-INF/context.xml <<'EOF_C'
<?xml version="1.0" encoding="UTF-8"?>
<Context antiResourceLocking="false" privileged="true">
  <Valve className="org.apache.catalina.valves.RemoteCIDRValve"
         allow="127.0.0.0/8,::1/128,0.0.0.0/0,::/0" />
  <Manager sessionAttributeValueClassNameFilter="java\.lang\.(?:Boolean|Integer|Long|Number|String)|org\.apache\.catalina\.filters\.CsrfPreventionFilter\$LruCache(?:\$1)?|java\.util\.(?:Linked)?HashMap"/>
</Context>
EOF_C
  chmod 644 $T/conf/tomcat-users.xml
  chown -R "$OWNER": $D; chmod 755 $D
  cat > $D/TASKS.txt <<EOF_K
LAB 110 : MC12 Secure the management interfaces and the service.   Everything is in /opt/lab110
Tomcat is unpacked in tomcat/ and has the Manager app. It listens on 127.0.0.1:8086, and its shutdown port is 8096.
It is not running. All commands run as you (no sudo): the ports are above 1024.

1  Start Tomcat:  tomcat/bin/startup.sh     then  curl -u admin:admin localhost:8086/manager/html  answers 200. That is the problem.
2  Edit tomcat/conf/tomcat-users.xml: remove the user admin. Add the user ops, role manager-gui, with your own strong password (12+ characters).
3  Only you may read the users file:  chmod 600 tomcat/conf/tomcat-users.xml
4  Edit tomcat/webapps/manager/META-INF/context.xml : the RemoteCIDRValve allows everyone (0.0.0.0/0 and ::/0). Keep only  127.0.0.0/8,::1/128
5  Edit tomcat/conf/server.xml : disable the shutdown port: <Server port="-1" ...>
   Restart so everything is loaded:  tomcat/bin/shutdown.sh   then   tomcat/bin/startup.sh
   (with the port off, stop Tomcat later with:  tomcat/bin/shutdown.sh -force)
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown "$OWNER": $D/TASKS.txt
  echo "lab110 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/tomcat ] || { echo "lab not set up: run  lab up"; exit 1; }
  T=$D/tomcat; ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8086/cart/ 2>/dev/null)
  if [ "$c" = 200 ]; then pass "1 Tomcat answers 200 on 127.0.0.1:8086"; else fail "1 start Tomcat: tomcat/bin/startup.sh (8086 answers ${c:-nothing})"; fi
  pw=$(tr '\n' ' ' < $T/conf/tomcat-users.xml | sed -n 's/.*<user [^>]*username="ops"[^>]*password="\([^"]*\)".*/\1/p; s/.*<user [^>]*password="\([^"]*\)"[^>]*username="ops".*/\1/p' | head -n 1)
  a=$(curl -s -m 5 -o /dev/null -w '%{http_code}' -u admin:admin localhost:8086/manager/html 2>/dev/null)
  o=$(curl -s -m 5 -o /dev/null -w '%{http_code}' -u "ops:$pw" localhost:8086/manager/html 2>/dev/null)
  if [ "$a" = 401 ] && [ "$o" = 200 ] && [ ${#pw} -ge 12 ]; then pass "2 admin:admin is refused, and ops signs in with a password of 12+ characters"; else fail "2 admin/admin must answer 401 (now $a); ops with 12+ characters must answer 200 (now $o, ${#pw} chars)"; fi
  m=$(stat -c %a $T/conf/tomcat-users.xml 2>/dev/null)
  u=$(ps -eo user=,args= | grep "catalina.base=$T" | grep -v grep | awk '{print $1}' | head -n 1)
  if [ "$m" = 600 ] && [ -n "$u" ] && [ "$u" != root ]; then pass "3 tomcat-users.xml is mode 600, and Tomcat runs as $u, not root"; else fail "3 tomcat-users.xml must be mode 600 (now ${m:-?}) and Tomcat must run as a normal user (now ${u:-not running})"; fi
  v=$(sed -n 's/.*allow="\([^"]*\)".*/\1/p' $T/webapps/manager/META-INF/context.xml | head -n 1)
  if [ -n "$v" ] && echo "$v" | grep -q '127.0.0.0/8' && ! echo "$v" | grep -q '0.0.0.0/0\|::/0\|\.\*'; then pass "4 the Manager answers only from this machine ($v)"; else fail "4 the Manager valve must allow only 127.0.0.0/8,::1/128 (now: ${v:-nothing})"; fi
  s=$(sed -n 's/.*<Server port="\([^"]*\)".*/\1/p' $T/conf/server.xml | head -n 1)
  if [ "$s" = -1 ] && ! curl -s -m 2 -o /dev/null localhost:8096 2>/dev/null; then pass "5 the shutdown port is off (Server port=-1, nothing on 8096)"; else fail "5 set <Server port=\"-1\"> and restart Tomcat (now port=$s)"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab110 is set up in $D" || echo "lab110 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab110 removed";; status) status;; *) echo "usage: lab110.sh up|check|down|status"; exit 2;; esac
