#!/bin/sh
# lab105.sh : MC12-O02 Install and run Tomcat the proper way. Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status
# Needs: a JDK (sudo apt install -y openjdk-21-jdk-headless curl), internet access (Tomcat about 14 MB), about 1 GB of free memory.
# Mission: verify the download, make a dedicated tomcat user, unpack, set owners, start Tomcat as that user, and prove it with the log.
D=${LAB105_DIR:-/opt/lab105}
U=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB105_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
F=apache-tomcat-$TV.tar.gz
as() { if [ "$U" = root ]; then "$@"; else runuser -u $U -- "$@"; fi; }
down() {
  [ -x $D/tomcat/bin/shutdown.sh ] && runuser -u tomcat -- env -u JAVA_TOOL_OPTIONS $D/tomcat/bin/shutdown.sh >/dev/null 2>&1; sleep 3
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1
  h=$(getent passwd tomcat | cut -d: -f6); case "$h" in "$D"/*) userdel tomcat 2>/dev/null;; esac
  rm -rf "${D:?}"; true
}
up() {
  for t in java curl sha512sum tar; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  if getent passwd tomcat >/dev/null; then h=$(getent passwd tomcat | cut -d: -f6); case "$h" in "$D"/*) ;; *) echo "a user called tomcat already exists on this machine: this lab needs that name free"; exit 1;; esac; fi
  down; mkdir -p $D/dl
  echo "downloading Tomcat $TV (about 14 MB) and its checksum ..."
  curl -fL --progress-bar -o $D/dl/$F "$TB/$F" || { echo "download failed"; exit 1; }
  curl -fsL -o $D/dl/$F.sha512 "$TB/$F.sha512" || { echo "checksum download failed"; exit 1; }
  cat > $D/TASKS.txt <<'EOF_K'
LAB 105 : MC12 Install and run Tomcat.   Everything is in /opt/lab105
dl/ holds the Tomcat download and its published checksum. Nothing is installed yet. Use sudo for the steps that need it.

1  Verify the download:  cd dl   then   sha512sum -c apache-tomcat-10.1.34.tar.gz.sha512 > ../checksum.txt   (it must say OK)
2  Make a dedicated user that cannot log in:  sudo useradd -r -s /usr/sbin/nologin -d /opt/lab105/tomcat tomcat
3  Unpack into /opt/lab105/tomcat:  sudo mkdir /opt/lab105/tomcat  then  sudo tar xzf dl/apache-tomcat-10.1.34.tar.gz -C tomcat --strip-components=1
4  Give the files to the user:  sudo chown -R tomcat: tomcat
5  Start Tomcat AS that user:  sudo -u tomcat tomcat/bin/startup.sh    then check  curl -s -o /dev/null -w '%{http_code}\n' localhost:8080   (200)
6  Prove it from the log:  grep "Server startup" tomcat/logs/catalina.out > startup.txt
Then:  lab check     (all 5 must pass)       and later:  lab down   (it stops Tomcat, removes the tomcat user and everything)
EOF_K
  chown -R $U $D; chmod 755 $D
  echo "lab105 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/dl ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  if grep -q 'OK$' $D/checksum.txt 2>/dev/null && ( cd $D/dl && sha512sum -c $F.sha512 >/dev/null 2>&1 ); then pass "1 the download was verified against the published checksum"; else fail "1 checksum.txt must hold the OK line of: sha512sum -c apache-tomcat-10.1.34.tar.gz.sha512"; fi
  sh=$(getent passwd tomcat | cut -d: -f7); if [ -n "$sh" ] && { [ "$sh" = /usr/sbin/nologin ] || [ "$sh" = /sbin/nologin ] || [ "$sh" = /bin/false ]; }; then pass "2 user tomcat exists and cannot log in"; else fail "2 make user tomcat with a nologin shell: sudo useradd -r -s /usr/sbin/nologin -d $D/tomcat tomcat"; fi
  if [ -x $D/tomcat/bin/startup.sh ] && [ "$(stat -c %U $D/tomcat/conf $D/tomcat/logs $D/tomcat/webapps 2>/dev/null | sort -u)" = tomcat ]; then pass "3 Tomcat is unpacked and owned by tomcat"; else fail "3 unpack into $D/tomcat and run: sudo chown -R tomcat: $D/tomcat"; fi
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8080/); r=$(ps -o user= -C java 2>/dev/null | sort -u | tr -d ' ')
  if [ "$c" = 200 ] && [ "$r" = tomcat ]; then pass "4 Tomcat answers 200 and runs as the tomcat user"; else fail "4 start it as tomcat: sudo -u tomcat $D/tomcat/bin/startup.sh (answer=$c, java runs as: ${r:-nobody})"; fi
  if grep -q 'Server startup in' $D/startup.txt 2>/dev/null; then pass "5 startup.txt holds the Server startup line from catalina.out"; else fail "5 startup.txt must hold: grep \"Server startup\" tomcat/logs/catalina.out"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab105 is set up in $D" || echo "lab105 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab105 removed";; status) status;; *) echo "usage: lab105.sh up|check|down|status"; exit 2;; esac
