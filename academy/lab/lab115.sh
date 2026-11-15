#!/bin/sh
# lab115.sh : CloudCart v0, lesson 3: deploy CloudCart to Tomcat by hand and from the Manager. Run with sudo, on any Linux machine with a JDK, curl and ss.
#   up | check | down | status
# Needs: sudo apt install -y openjdk-21-jdk-headless curl iproute2     internet (Tomcat 14 MB, app 0.3 MB), about 1 GB of memory, ports 8089 and 8099 free.
# Mission: deploy the same WAR twice (drop-in by hand, then from the Manager web page), undeploy the first one, and answer three questions.
D=${LAB115_DIR:-/opt/lab115}
OWNER=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB115_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
WAR_URL=${LAB115_WAR_URL:-https://raw.githubusercontent.com/it-waves/devops-ai/main/academy/lab/assets/cloudcart-0.2.0.war}
F=apache-tomcat-$TV.tar.gz
B=localhost:8089
MU=deployer:ship-it-115
down() {
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1
  rm -rf "${D:?}"; true
}
up() {
  for t in java curl tar ss; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y openjdk-21-jdk-headless curl iproute2"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  for p in 8089 8099; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  T=$D/tomcat
  sed -i 's#<Connector port="8080"#<Connector port="8089"#; s#<Server port="8005"#<Server port="8099"#' $T/conf/server.xml
  rm -rf $T/webapps/docs $T/webapps/examples $T/webapps/host-manager $T/webapps/ROOT
  sed -i 's#</tomcat-users>#  <role rolename="manager-gui"/>\n  <role rolename="manager-script"/>\n  <user username="deployer" password="ship-it-115" roles="manager-gui,manager-script"/>\n</tomcat-users>#' $T/conf/tomcat-users.xml
  printf '%s\n' 'CATALINA_PID=$CATALINA_BASE/tomcat.pid' > $T/bin/setenv.sh; chmod 755 $T/bin/setenv.sh
  echo "downloading CloudCart 0.2.0 ..."
  curl -fL --progress-bar -o $D/cloudcart-0.2.0.war "$WAR_URL" || { echo "app download failed"; exit 1; }
  cp $D/cloudcart-0.2.0.war $D/shop.war
  cat > $D/TASKS.txt <<'EOF_T'
LAB 115  CloudCart v0: deploy it to Tomcat, by hand and from the Manager
Open a terminal in /opt/lab115. The Manager login is  deployer / ship-it-115  (see tomcat/conf/tomcat-users.xml).
Run  lab check  after each step: it remembers what it has seen.

1  Start Tomcat:  tomcat/bin/startup.sh       (it starts with no CloudCart in it)
2  By hand: copy cloudcart-0.2.0.war into tomcat/webapps as  cloudcart.war , wait, open http://localhost:8089/cloudcart/
   then run  lab check  (it must see CloudCart answer UP)
3  From the Manager (http://localhost:8089/manager/html): deploy shop.war with the context path  /shop
   ("WAR or Directory URL" box: file:/opt/lab115/shop.war), then open http://localhost:8089/shop/
4  In the Manager, Undeploy  /cloudcart  (the first copy goes away, /shop stays)
5  Write answers.txt with exactly three lines:
      apps: ...              the paths of the applications the Manager lists now, sorted, comma between, no spaces (e.g. /a,/b)
      cloudcart-folder: ...  yes or no: is tomcat/webapps/cloudcart still on disk after the Undeploy
      shop-folder: ...       yes or no: did the Manager create tomcat/webapps/shop (look with ls)
6  lab check   (judges you: you need all 5 PASS)
7  lab down    (stops Tomcat and removes everything)
EOF_T
  : > $D/answers.txt
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 115 ready in $D. Read TASKS.txt, then start Tomcat."
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D/tomcat ] || { echo "lab is not up: run  lab up"; exit 1; }
  T=$D/tomcat
  L=$(curl -s -m 3 -u $MU "$B/manager/text/list")
  case "$L" in "OK - Listed"*) ok "1 Tomcat is running and the Manager answers" ;; *) no "1 the Manager does not answer: start Tomcat and wait 10 seconds" ;; esac
  h=$(curl -s -m 3 $B/cloudcart/health)
  case "$h" in *'"status":"UP"'*) touch $D/.seen_cloudcart; chmod a+r $D/.seen_cloudcart ;; esac
  if [ -f $D/.seen_cloudcart ]; then ok "2 CloudCart was deployed by hand and answered UP"; else no "2 CloudCart has not answered UP at /cloudcart yet (copy the WAR into webapps, wait 10 seconds)"; fi
  s=$(curl -s -m 3 $B/shop/health)
  case "$s" in *'"status":"UP"'*) if printf '%s' "$L" | grep -q '^/shop:running'; then ok "3 /shop is running and listed by the Manager"; else no "3 /shop answers but the Manager does not list it as running"; fi ;; *) no "3 /shop does not answer UP yet: deploy shop.war from the Manager" ;; esac
  if [ -f $D/.seen_cloudcart ] && ! printf '%s' "$L" | grep -q '^/cloudcart:' && [ ! -e $T/webapps/cloudcart.war ] && [ "$(curl -s -o /dev/null -m 3 -w '%{http_code}' $B/cloudcart/health)" = 404 ]; then ok "4 /cloudcart was undeployed: it is gone and /shop stays"; else no "4 /cloudcart is still deployed (or was never seen): undeploy it in the Manager"; fi
  A=$D/answers.txt
  ap=$(printf '%s' "$L" | grep ':running:' | cut -d: -f1 | sort | paste -sd, -)
  if [ -n "$ap" ] && grep -qx "apps: $ap" $A 2>/dev/null && grep -qx 'cloudcart-folder: no' $A 2>/dev/null && { [ -d $T/webapps/shop ] && x=yes || x=no; grep -qx "shop-folder: $x" $A 2>/dev/null; }; then ok "5 answers.txt has the right three lines"; else no "5 answers.txt is missing a line or one is wrong"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 115 is up in $D" || echo "lab 115 is not up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 115 removed";; status) status;; *) echo "usage: sudo lab115.sh up | check | down | status";; esac
