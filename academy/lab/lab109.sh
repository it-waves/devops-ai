#!/bin/sh
# lab109.sh : MC12-O06 Put nginx in front of Tomcat: a reverse proxy with TLS termination. Run with sudo, on any Linux machine with nginx, openssl, a JDK, curl.
#   up | check | down | status
# Needs: sudo apt install -y nginx openssl openjdk-21-jdk-headless curl   (nginx is only used from this lab folder: the system nginx service is left alone)
#        internet (Tomcat 14 MB), about 1 GB of memory, ports 8084, 8085 and 8443 free.
# Mission: Tomcat listens only on 127.0.0.1:8084. Publish it through nginx on https://localhost:8443 with your own certificate, redirect plain http (8085) to https, and pass the real scheme and client address to the app.
D=${LAB109_DIR:-/opt/lab109}
OWNER=${SUDO_USER:-root}
TV=10.1.34
TB=${LAB109_TOMCAT_BASE:-https://archive.apache.org/dist/tomcat/tomcat-10/v$TV/bin}
F=apache-tomcat-$TV.tar.gz
down() {
  [ -f $D/nginx/nginx.pid ] && kill "$(cat $D/nginx/nginx.pid)" 2>/dev/null
  pkill -f "nginx: master process nginx -p $D/nginx" 2>/dev/null
  pkill -f "catalina.base=$D/tomcat" 2>/dev/null; sleep 1
  rm -rf "${D:?}"; true
}
up() {
  for t in java curl tar nginx openssl; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y nginx openssl openjdk-21-jdk-headless curl"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  for p in 8084 8085 8443; do if curl -sk -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D
  echo "downloading Tomcat $TV (about 14 MB) ..."
  curl -fL --progress-bar -o $D/t.tgz "$TB/$F" || { echo "download failed"; exit 1; }
  mkdir -p $D/tomcat && tar xzf $D/t.tgz -C $D/tomcat --strip-components=1 || { echo "unpack failed"; exit 1; }; rm -f $D/t.tgz
  sed -i 's#<Connector port="8080"#<Connector port="8084" address="127.0.0.1"#' $D/tomcat/conf/server.xml
  rm -rf $D/tomcat/webapps/docs $D/tomcat/webapps/examples $D/tomcat/webapps/host-manager $D/tomcat/webapps/manager
  A=$D/tomcat/webapps/cart; mkdir -p $A/WEB-INF
  cat > $A/index.html <<'EOF_I'
<!DOCTYPE html><html><head><title>CloudCart</title></head><body><h1>CloudCart 1.0</h1><p>The cart service is running.</p></body></html>
EOF_I
  cat > $A/whoami.jsp <<'EOF_H'
scheme=<%= request.getScheme() %> forwarded-proto=<%= request.getHeader("X-Forwarded-Proto") %> client=<%= request.getHeader("X-Forwarded-For") %> peer=<%= request.getRemoteAddr() %>
EOF_H
  cat > $A/WEB-INF/web.xml <<'EOF_W'
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee" version="6.0"><display-name>cart</display-name></web-app>
EOF_W
  mkdir -p $D/nginx/conf.d $D/nginx/logs $D/tls
  cat > $D/nginx/nginx.conf <<EOF_N
worker_processes 1;
pid $D/nginx/nginx.pid;
error_log $D/nginx/logs/error.log;
events { worker_connections 64; }
http {
  access_log $D/nginx/logs/access.log;
  client_body_temp_path $D/nginx/tmp/body; proxy_temp_path $D/nginx/tmp/proxy; fastcgi_temp_path $D/nginx/tmp/fcgi; uwsgi_temp_path $D/nginx/tmp/uwsgi; scgi_temp_path $D/nginx/tmp/scgi;
  include $D/nginx/conf.d/*.conf;
}
EOF_N
  mkdir -p $D/nginx/tmp; chown -R "$OWNER": $D; chmod 755 $D
  cat > $D/TASKS.txt <<EOF_K
LAB 109 : MC12 Reverse proxy and TLS termination.   Everything is in /opt/lab109
Tomcat is unpacked in tomcat/ and listens ONLY on 127.0.0.1:8084. nginx has a base file, nginx/nginx.conf, that includes everything in nginx/conf.d/*.conf.
Neither is running. All commands run as you (no sudo): the ports are above 1024.

1  Start Tomcat:  tomcat/bin/startup.sh     then  curl localhost:8084/cart/  answers 200
2  Make a certificate for localhost, valid 30 days, in tls/:
     openssl req -x509 -newkey rsa:2048 -nodes -keyout tls/cart.key -out tls/cart.crt -days 30 -subj /CN=localhost
3  Create nginx/conf.d/cart.conf with a server that listens on 8443 with ssl, uses the two files, and proxies everything to http://127.0.0.1:8084
   Add:  proxy_set_header X-Forwarded-Proto \$scheme;   and   proxy_set_header X-Forwarded-For \$remote_addr;
   Test it:  nginx -p $D/nginx -c nginx.conf -t     Start:  nginx -p $D/nginx -c nginx.conf
   then  curl -k https://localhost:8443/cart/whoami.jsp  must show  forwarded-proto=https  and  client=127.0.0.1
4  Add a second server to cart.conf: listen 8085, and return 301 https://localhost:8443\$request_uri;
   then reload:  nginx -p $D/nginx -c nginx.conf -s reload
Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown "$OWNER": $D/TASKS.txt
  echo "lab109 ready: cd $D   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/tomcat ] || { echo "lab not set up: run  lab up"; exit 1; }
  ok=0
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  c=$(curl -s -m 5 -o /dev/null -w '%{http_code}' localhost:8084/cart/ 2>/dev/null)
  if [ "$c" = 200 ]; then pass "1 Tomcat answers 200 on 127.0.0.1:8084"; else fail "1 start Tomcat: tomcat/bin/startup.sh (8084 answers ${c:-nothing})"; fi
  K=$D/tls/cart.key; C=$D/tls/cart.crt
  if [ -f $K ] && [ -f $C ] && openssl x509 -in $C -noout -subject 2>/dev/null | grep -q 'CN *= *localhost' && openssl x509 -in $C -noout -checkend 86400 >/dev/null 2>&1 && [ "$(openssl x509 -in $C -noout -pubkey 2>/dev/null | openssl md5)" = "$(openssl pkey -in $K -pubout 2>/dev/null | openssl md5)" ]; then pass "2 tls/cart.crt is for CN=localhost, is still valid, and matches tls/cart.key"; else fail "2 make tls/cart.key and tls/cart.crt with openssl req -x509 ... -subj /CN=localhost"; fi
  c=$(curl -sk -m 5 -o /dev/null -w '%{http_code}' https://localhost:8443/cart/ 2>/dev/null); b=$(curl -sk -m 5 https://localhost:8443/cart/ 2>/dev/null)
  if [ "$c" = 200 ] && echo "$b" | grep -q CloudCart; then pass "3 https://localhost:8443/cart/ answers 200 through nginx"; else fail "3 https://localhost:8443/cart/ answers ${c:-nothing}: start nginx with your cart.conf"; fi
  w=$(curl -sk -m 5 https://localhost:8443/cart/whoami.jsp 2>/dev/null)
  if echo "$w" | grep -q 'forwarded-proto=https' && echo "$w" | grep -q 'client=127.0.0.1'; then pass "4 the app sees forwarded-proto=https and the client address"; else fail "4 whoami.jsp must show forwarded-proto=https and client=127.0.0.1: add the two proxy_set_header lines"; fi
  r=$(curl -s -m 5 -o /dev/null -w '%{http_code} %{redirect_url}' localhost:8085/cart/ 2>/dev/null)
  if [ "$r" = "301 https://localhost:8443/cart/" ]; then pass "5 http on 8085 redirects (301) to https on 8443"; else fail "5 http://localhost:8085/cart/ must answer 301 to https://localhost:8443/cart/ (now: ${r:-nothing})"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab109 is set up in $D" || echo "lab109 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab109 removed";; status) status;; *) echo "usage: lab109.sh up|check|down|status"; exit 2;; esac
