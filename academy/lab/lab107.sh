#!/bin/sh
# lab107.sh : MC12-O04 Ports, environment and a systemd service for Tomcat. Run with sudo, in your own Ubuntu virtual machine (it needs a real systemd).
#   up | check | down | status
# Needs: JDK, curl, systemd (sudo apt install -y openjdk-21-jdk-headless curl), internet (Tomcat 14 MB), about 1 GB of memory, port 8081 free.
# Mission: move Tomcat to port 8081 with an environment file, run it as a systemd service as user tomcat, and prove it restarts after a crash.
D=${LAB107_DIR:-/opt/lab107}
SVC=tomcat107
UNIT=/etc/systemd/system/$SVC.service
TV=10.1.34
TB=${LAB107_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
F=apache-tomcat-$TV.tar.gz
down() {
  systemctl stop $SVC >/dev/null 2>&1; systemctl disable $SVC >/dev/null 2>&1
  rm -f $UNIT; systemctl daemon-reload >/dev/null 2>&1; systemctl reset-failed $SVC >/dev/null 2>&1
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1
  if getent passwd tomcat >/dev/null && [ "$(getent passwd tomcat | cut -d: -f6)" = "$D/tomcat" ]; then userdel tomcat 2>/dev/null; fi
  rm -rf "${D:?}"; true
}
up() {
  for t in java curl tar systemctl; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  [ -d /run/systemd/system ] || { echo "this lab needs a real systemd (an Ubuntu virtual machine, not a plain container)"; exit 1; }
  if getent passwd tomcat >/dev/null && [ "$(getent passwd tomcat | cut -d: -f6)" != "$D/tomcat" ]; then echo "a user called tomcat already exists on this machine; this lab needs that name free"; exit 1; fi
  if curl -s -o /dev/null -m 2 localhost:8081; then echo "port 8081 is already in use: stop what uses it first"; exit 1; fi
  down; mkdir -p $D
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  useradd -r -s /usr/sbin/nologin -d $D/tomcat tomcat && chown -R tomcat: $D/tomcat
  JH=$(dirname $(dirname $(readlink -f $(command -v java))))
  sed -i 's#<Connector port="8080"#<Connector port="${http.port:-8080}"#' $D/tomcat/conf/server.xml
  cat > $D/TASKS.txt <<EOF_K
LAB 107 : MC12 Ports, environment and a systemd service.   Everything is in /opt/lab107
Tomcat is unpacked in tomcat/, owned by user tomcat, and is NOT running. Java lives in $JH
server.xml already reads its port from a property:   port="\${http.port:-8080}"   (8080 unless you set http.port)

1  Environment file:  create tomcat/bin/setenv.sh  (owned by tomcat) with three lines:
     export JAVA_HOME=$JH
     export CATALINA_PID=$D/tomcat/temp/tomcat.pid
     export CATALINA_OPTS="-Xmx256m -Dhttp.port=8081 -Dcloudcart.env=staging"
2  Unit file:  create $UNIT  with:
     [Unit]  Description=Tomcat for lab 107   and   After=network.target
     [Service]  Type=forking   User=tomcat   Group=tomcat   PIDFile=$D/tomcat/temp/tomcat.pid
                ExecStart=$D/tomcat/bin/startup.sh   ExecStop=$D/tomcat/bin/shutdown.sh   Restart=on-failure   RestartSec=3
     [Install]  WantedBy=multi-user.target
3  sudo systemctl daemon-reload ;  sudo systemctl enable --now $SVC      then   curl localhost:8081   answers 200
4  Crash it: find the main PID (systemctl show -p MainPID $SVC), sudo kill -9 it, wait about 10 seconds. systemd starts it again.
Then:  lab check     (all 5 must pass)       and later:  lab down   (it stops the service and removes everything)
EOF_K
  chmod 755 $D; echo "lab107 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/tomcat ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  S=$D/tomcat/bin/setenv.sh
  if [ -r $S ] && [ "$(stat -c %U $S)" = tomcat ] && grep -q 'http.port=8081' $S && grep -q 'cloudcart.env=staging' $S && grep -q CATALINA_PID $S; then pass "1 setenv.sh is owned by tomcat and sets the port, the environment and the PID file"; else fail "1 tomcat/bin/setenv.sh: owned by tomcat, with CATALINA_PID and CATALINA_OPTS holding http.port=8081 and cloudcart.env=staging"; fi
  if [ -f $UNIT ] && grep -q '^User=tomcat' $UNIT && grep -q '^Restart=on-failure' $UNIT && grep -q '^Type=forking' $UNIT && grep -q "$D/tomcat/bin/startup.sh" $UNIT; then pass "2 $SVC.service runs startup.sh as tomcat with Restart=on-failure"; else fail "2 $UNIT needs Type=forking, User=tomcat, ExecStart=$D/tomcat/bin/startup.sh and Restart=on-failure"; fi
  if systemctl is-active --quiet $SVC && systemctl is-enabled --quiet $SVC; then pass "3 the service is active and enabled"; else fail "3 systemctl enable --now $SVC (active: $(systemctl is-active $SVC 2>&1), enabled: $(systemctl is-enabled $SVC 2>&1))"; fi
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8081 2>/dev/null); p=$(systemctl show -p MainPID --value $SVC 2>/dev/null)
  if [ "$c" = 200 ] && [ -n "$p" ] && [ "$p" != 0 ] && [ "$(ps -o user= -p $p | tr -d ' ')" = tomcat ] && tr '\0' ' ' < /proc/$p/cmdline | grep -q 'cloudcart.env=staging'; then pass "4 port 8081 answers 200 from a java process run by tomcat with the environment set"; else fail "4 localhost:8081 answers ${c:-nothing}; java must run as tomcat with -Dcloudcart.env=staging"; fi
  n=$(systemctl show -p NRestarts --value $SVC 2>/dev/null)
  if [ "${n:-0}" -ge 1 ] 2>/dev/null && systemctl is-active --quiet $SVC; then pass "5 the service crashed and systemd restarted it ($n restart)"; else fail "5 kill -9 the main PID and let systemd restart it (restarts so far: ${n:-0})"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab107 is set up in $D" || echo "lab107 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab107 removed";; status) status;; *) echo "usage: lab107.sh up|check|down|status"; exit 2;; esac
