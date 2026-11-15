#!/bin/sh
# lab113.sh : CloudCart v0, lesson 1: meet the app and use it like a customer. Run with sudo, on any Linux machine with a JDK, curl and ss.
#   up | check | down | status
# Needs: sudo apt install -y openjdk-21-jdk-headless curl iproute2     internet (Tomcat 14 MB, app 0.3 MB), about 1 GB of memory, ports 8089 and 8099 free.
# Mission: start CloudCart, shop like a customer (demo account), place one exact order, and answer five questions about what you saw.
D=${LAB113_DIR:-/opt/lab113}
OWNER=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB113_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
WAR_URL=${LAB113_WAR_URL:-https://raw.githubusercontent.com/it-waves/devops-ai/main/academy/lab/assets/cloudcart-0.2.0.war}
F=apache-tomcat-$TV.tar.gz
B=localhost:8089/cloudcart
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
  rm -rf $T/webapps/docs $T/webapps/examples $T/webapps/host-manager $T/webapps/manager $T/webapps/ROOT
  printf '%s\n' 'CATALINA_PID=$CATALINA_BASE/tomcat.pid' > $T/bin/setenv.sh; chmod 755 $T/bin/setenv.sh
  echo "downloading CloudCart 0.2.0 ..."
  curl -fL --progress-bar -o $T/webapps/cloudcart.war "$WAR_URL" || { echo "app download failed"; exit 1; }
  cat > $D/TASKS.txt <<'EOF_T'
LAB 113  CloudCart v0: meet the app and use it like a customer
Open a terminal in /opt/lab113 and a browser at http://localhost:8089/cloudcart/ once Tomcat runs.

1  Start Tomcat:  tomcat/bin/startup.sh     (stop it later with tomcat/bin/shutdown.sh)
2  Sign in with the demo account:  student@cloudcart.test  /  learn-cloudcart
3  Place ONE order with exactly:  2 x Dot-Grid Notebook  and  1 x Insulated Steel Bottle
   (use any made-up address, the ZIP must be 5 digits)
4  Write answers.txt with exactly five lines:
      order: CC-....          the order number on the confirmation page
      total: 71.79            the total you were charged (demo, nothing is really charged)
      soldout: ...            the product that cannot be added to the cart
      lowstock: ...           the product that shows "Only 3 left"
      version: ...            the version shown in the footer of the shop
5  lab check   (judges you: 5 lines, you need all 5 PASS)
6  lab down    (stops Tomcat and removes everything)
EOF_T
  : > $D/answers.txt
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 113 ready in $D. Read TASKS.txt, then start Tomcat."
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D/tomcat ] || { echo "lab is not up: run  lab up"; exit 1; }
  h=$(curl -s -m 3 $B/health)
  case "$h" in *'"status":"UP"'*) ok "1 CloudCart answers and its health is UP" ;; *) no "1 CloudCart does not answer yet: start Tomcat and wait 10 seconds" ;; esac
  j=$(mktemp); curl -s -m 3 -c $j -o /dev/null -X POST -H 'Content-Type: application/json' -d '{"email":"student@cloudcart.test","password":"learn-cloudcart"}' $B/api/auth/login
  orders=$(curl -s -m 3 -b $j $B/api/orders); rm -f $j
  mine=$(printf '%s' "$orders" | sed 's/{"id":"CC-/\n{"id":"CC-/g' | grep -F '"productId":10,"name":"Dot-Grid Notebook","priceCents":1600,"quantity":2' | grep -F '"productId":9,"name":"Insulated Steel Bottle","priceCents":2800,"quantity":1' | head -n 1)
  if [ -n "$mine" ]; then ok "2 an order has 2 x Dot-Grid Notebook and 1 x Insulated Steel Bottle"; else no "2 no order with exactly those two items for the demo account"; fi
  case "$mine" in *'"totalCents":7179'*) ok "3 that order totals 71.79 (items, shipping, tax)" ;; *) no "3 the order total is not 71.79" ;; esac
  id=$(printf '%s' "$mine" | grep -o '"id":"CC-[0-9]*"' | head -n 1 | cut -d'"' -f4)
  A=$D/answers.txt
  if [ -n "$id" ] && grep -qx "order: $id" $A 2>/dev/null && grep -Eqx 'total: \$?71\.79' $A 2>/dev/null; then ok "4 answers.txt has the right order number and total"; else no "4 answers.txt order or total line is missing or wrong"; fi
  if grep -qx 'soldout: USB Podcast Microphone' $A 2>/dev/null && grep -qx 'lowstock: Full-HD Webcam' $A 2>/dev/null && grep -qx 'version: 0.2.0' $A 2>/dev/null; then ok "5 soldout, lowstock and version lines are right"; else no "5 soldout, lowstock or version line is missing or wrong"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 113 is up in $D" || echo "lab 113 is not up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab 113 removed";; status) status;; *) echo "usage: sudo lab113.sh up | check | down | status";; esac
