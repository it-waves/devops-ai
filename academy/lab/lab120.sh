#!/bin/sh
# lab120.sh : Web servers and reverse proxies, lesson 3: HTTPS with TLS on nginx. Run with sudo, on any Linux machine with nginx, openssl and curl.
#   up | check | down | status
# Needs: sudo apt install -y nginx openssl curl iproute2     ports 8201 (HTTP) and 8443 (HTTPS) free. (The lab runs its own private nginx from /opt/lab120; it does not touch the system nginx.)
# Mission: make a certificate, turn on HTTPS, and redirect plain HTTP to it.
D=${LAB120_DIR:-/opt/lab120}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then RU=""; else RU="runuser -u $OWNER --"; fi
NG="nginx -p $D -e $D/logs/error.log -c $D/nginx.conf"
down() {
  [ -f $D/nginx.pid ] && kill "$(cat $D/nginx.pid)" 2>/dev/null; sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  for t in nginx openssl curl; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y nginx openssl curl iproute2"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  [ -f /etc/nginx/mime.types ] || { echo "/etc/nginx/mime.types not found: run  sudo apt install -y nginx"; exit 1; }
  for p in 8201 8443; do if curl -sk -o /dev/null -m 2 localhost:$p || curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/site $D/logs $D/tmp $D/certs
  cp /etc/nginx/mime.types $D/mime.types
  cat > $D/site/index.html <<'EOF_H'
<!doctype html>
<html><head><meta charset="utf-8"><title>CloudCart</title></head>
<body><h1>Welcome to CloudCart</h1><p>This page travelled encrypted.</p></body></html>
EOF_H
  cat > $D/nginx.conf <<EOF_C
worker_processes 1;
pid $D/nginx.pid;
events { worker_connections 64; }
http {
    include mime.types;
    server_tokens off;
    access_log $D/logs/access.log;
    client_body_temp_path $D/tmp/body;
    proxy_temp_path $D/tmp/proxy;
    fastcgi_temp_path $D/tmp/fcgi;
    uwsgi_temp_path $D/tmp/uwsgi;
    scgi_temp_path $D/tmp/scgi;
    server {
        listen 8201;
        root $D/site;
    }
    server {
        listen 8443 ssl;
        root $D/site;
    }
}
EOF_C
  cat > $D/TASKS.txt <<'EOF_T'
LAB 120  HTTPS: certificates and TLS on nginx
Open a terminal in /opt/lab120. The short name  ng  runs nginx with this lab's own config (/opt/lab120/nginx.conf).  Load it with: source shortcuts120.sh

1  Test the config:   ng -t       It fails: the HTTPS server has no certificate yet. Read the message.
2  Make a private key and a self-signed certificate (valid 30 days, for the name localhost):
     cd certs
     openssl req -x509 -nodes -newkey rsa:2048 -days 30 -keyout site.key -out site.crt -subj /CN=localhost 2>/dev/null
     cd ..
   (2>/dev/null hides the progress dots that key generation prints)
3  Look at your certificate:   openssl x509 -in certs/site.crt -noout -subject -enddate
4  In nginx.conf, inside the  listen 8443 ssl;  server block, add three lines:
     ssl_certificate     certs/site.crt;
     ssl_certificate_key certs/site.key;
     ssl_protocols       TLSv1.2 TLSv1.3;
5  Test and start:   ng -t   then   ng
6  Redirect plain HTTP. Inside the  listen 8201;  server block add:   return 301 https://localhost:8443$request_uri;
7  Apply it:   ng -t && ng -s reload
8  Prove it:   curl -I localhost:8201   (a 301 and a Location)    curl -k https://localhost:8443   (the page; -k accepts a self-signed certificate)
9  lab check   (judges you: you need all 5 PASS)
10 lab down    (stops nginx and removes everything)
If something fails, read the nginx error: it names the file and the line.
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 120 ready in $D. Read TASKS.txt, then run: ng -t"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  if [ -s $D/certs/site.key ] && [ -s $D/certs/site.crt ] && openssl x509 -in $D/certs/site.crt -noout -subject 2>/dev/null | grep -q 'CN *= *localhost' && openssl x509 -in $D/certs/site.crt -noout -checkend 86400 >/dev/null 2>&1; then ok "1 a key and a valid certificate for localhost exist in certs/"; else no "1 no valid certificate for localhost in certs/: run the openssl req command from TASKS.txt"; fi
  pid=$(cat $D/nginx.pid 2>/dev/null)
  if $RU $NG -t >/dev/null 2>&1 && [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then ok "2 the config passes  ng -t  and nginx is running"; else no "2 the config fails the test or nginx is not running: run  ng -t  and fix the line it names, then  ng"; fi
  if curl -sk -m 3 https://localhost:8443/ 2>/dev/null | grep -q 'Welcome to CloudCart'; then ok "3 HTTPS answers on port 8443 with the CloudCart page"; else no "3 https://localhost:8443 does not answer: add the three ssl lines to the 8443 server block"; fi
  pr=$($RU $NG -T 2>/dev/null | sed -n 's/^ *ssl_protocols *\(.*\);/\1/p')
  if echo "$pr" | grep -q 'TLSv1.2' && ! echo "$pr" | grep -Eq 'TLSv1( |;|$)|TLSv1\.1|SSLv'; then ok "4 only TLS 1.2 and 1.3 are enabled"; else no "4 set  ssl_protocols TLSv1.2 TLSv1.3;  and nothing older"; fi
  h=$(curl -sI -m 3 localhost:8201/x 2>/dev/null | tr -d '\r')
  if echo "$h" | head -n 1 | grep -q ' 301' && echo "$h" | grep -iq '^location: https://localhost:8443/x'; then ok "5 plain HTTP on 8201 redirects (301) to HTTPS on 8443"; else no "5 http://localhost:8201 must answer 301 with a Location on https: add  return 301 https://localhost:8443\$request_uri;"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 120 is up in $D" || echo "lab 120 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 120 removed" ;; status) status ;; *) echo "usage: lab120.sh up|check|down|status" ;; esac
