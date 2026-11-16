#!/bin/sh
# lab116.sh : CloudCart v0, lesson 4: run it like a customer, fix it like an engineer. Run with sudo, on any Linux machine with a JDK, curl, ss and python3.
#   up | check | down | status
# Needs: sudo apt install -y openjdk-21-jdk-headless curl iproute2 python3     internet (Tomcat 14 MB, app 0.3 MB), about 1 GB of memory, ports 8089 and 8099 free.
# Mission: Tomcat is broken in three ways. Find each cause in the output and the logs, fix it, and get CloudCart answering again.
D=${LAB116_DIR:-/opt/lab116}
OWNER=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB116_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
WAR_URL=${LAB116_WAR_URL:-https://raw.githubusercontent.com/it-waves/devops-ai/main/academy/lab/assets/cloudcart-0.2.0.war}
F=apache-tomcat-$TV.tar.gz
B=localhost:8089/cloudcart
if [ "$OWNER" = root ]; then RU=""; else RU="runuser -u $OWNER --"; fi
down() {
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; pkill -f "http.server 8089 --bind 0.0.0.0 --directory $D/www" 2>/dev/null; sleep 1
  rm -rf "${D:?}"; true
}
up() {
  for t in java curl tar ss python3; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl iproute2 python3"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  for p in 8089 8099; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/good $D/www
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  T=$D/tomcat
  sed -i 's#<Connector port="8080"#<Connector port="8089"#; s#<Server port="8005"#<Server port="8099"#' $T/conf/server.xml
  rm -rf $T/webapps/docs $T/webapps/examples $T/webapps/host-manager $T/webapps/manager $T/webapps/ROOT
  echo "downloading CloudCart 0.2.0 ..."
  curl -fL --progress-bar -o $D/good/cloudcart.war "$WAR_URL" || { echo "app download failed"; exit 1; }
  head -c 100000 $D/good/cloudcart.war > $T/webapps/cloudcart.war
  printf '%s\n' 'JAVA_HOME=/opt/java-gone' 'CATALINA_PID=$CATALINA_BASE/tomcat.pid' > $T/bin/setenv.sh; chmod 755 $T/bin/setenv.sh
  echo "nothing to see here" > $D/www/index.html
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  (cd $D/www && setsid nohup $RU python3 -m http.server 8089 --bind 0.0.0.0 --directory $D/www >/dev/null 2>&1 &)
  sleep 1
  cat > $D/TASKS.txt <<'EOF_T'
LAB 116  CloudCart v0: run it like a customer, fix it like an engineer
Open a terminal in /opt/lab116. Tomcat is broken in three ways. Fix them one at a time, in this order of symptoms.
Before you fix anything, write down what you find: you need it for answers.txt.

1  Start Tomcat:  tomcat/bin/startup.sh      Read what it prints. Find the cause in tomcat/bin/setenv.sh and fix it (vim).
2  Start Tomcat again. Ask for http://localhost:8089/cloudcart/health with  curl -si  and look at the first lines.
   Who is answering? Read tomcat/logs/catalina.out, find out who holds port 8089 (ss -ltnp), stop it, restart Tomcat.
3  CloudCart still gives 404. Read the log again: what is wrong with tomcat/webapps/cloudcart.war ?
   A good copy is in /opt/lab116/good/cloudcart.war . Put it in place and wait 15 seconds.
4  Be a customer: curl -s localhost:8089/cloudcart/api/products  (twelve products) and the health page.
5  Write answers.txt with exactly three lines:
      javahome: ...     the wrong JAVA_HOME path you found in setenv.sh
      portholder: ...   the name of the program that held port 8089
      exception: ...    the Java exception class in the log for the broken war (just the class name)
6  lab check   (judges you: you need all 5 PASS)
7  lab down    (stops Tomcat and removes everything)
EOF_T
  : > $D/answers.txt
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 116 ready in $D. Read TASKS.txt, then start Tomcat."
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D/tomcat ] || { echo "lab is not up: run  lab up"; exit 1; }
  T=$D/tomcat
  if ! grep -q 'java-gone' $T/bin/setenv.sh && pgrep -f "catalina.base=$D/tomcat" >/dev/null; then ok "1 JAVA_HOME is fixed and Tomcat is running"; else no "1 Tomcat is not running, or setenv.sh still has the wrong JAVA_HOME"; fi
  if ss -ltnp 2>/dev/null | grep ':8089 ' | grep -q java; then ok "2 port 8089 belongs to Tomcat"; else no "2 port 8089 is not held by Tomcat (java) yet"; fi
  h=$(curl -s -m 3 $B/health)
  case "$h" in *'"status":"UP"'*) ok "3 CloudCart answers and its health is UP" ;; *) no "3 CloudCart does not answer UP at /cloudcart/health" ;; esac
  if cmp -s $D/good/cloudcart.war $T/webapps/cloudcart.war && unzip -tq $T/webapps/cloudcart.war >/dev/null 2>&1; then ok "4 cloudcart.war is the good, complete file"; else no "4 cloudcart.war is still broken or incomplete"; fi
  A=$D/answers.txt
  if grep -qx 'javahome: /opt/java-gone' $A 2>/dev/null && grep -qx 'portholder: python3' $A 2>/dev/null && grep -Eqx 'exception: (java\.util\.zip\.)?ZipException' $A 2>/dev/null; then ok "5 answers.txt has the three right causes"; else no "5 answers.txt is missing a line or one is wrong"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 116 is up in $D" || echo "lab 116 is not up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 116 removed";; status) status;; *) echo "usage: sudo lab116.sh up | check | down | status";; esac
