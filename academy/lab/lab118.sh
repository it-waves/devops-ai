#!/bin/sh
# lab118.sh : Web servers and reverse proxies, lesson 1: install and configure nginx to serve a static site. Run with sudo, on any Linux machine with nginx and curl.
#   up | check | down | status
# Needs: sudo apt install -y nginx curl iproute2     port 8181 free. (The lab runs its own private nginx from /opt/lab118; it does not touch the system nginx.)
# Mission: the config has a mistake. Make  ng -t  pass, start nginx, serve the CloudCart page, give a friendly 404, and hide the version.
D=${LAB118_DIR:-/opt/lab118}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then RU=""; else RU="runuser -u $OWNER --"; fi
B=localhost:8181
NG="nginx -p $D -e $D/logs/error.log -c $D/nginx.conf"
down() {
  [ -f $D/nginx.pid ] && kill "$(cat $D/nginx.pid)" 2>/dev/null; sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  for t in nginx curl; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y nginx curl iproute2"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  [ -f /etc/nginx/mime.types ] || { echo "/etc/nginx/mime.types not found: run  sudo apt install -y nginx"; exit 1; }
  if curl -s -o /dev/null -m 2 localhost:8181; then echo "port 8181 is already in use: stop what uses it first"; exit 1; fi
  down; mkdir -p $D/site $D/logs $D/tmp
  cp /etc/nginx/mime.types $D/mime.types
  cat > $D/site/index.html <<'EOF_H'
<!doctype html>
<html><head><meta charset="utf-8"><title>CloudCart</title><link rel="stylesheet" href="/style.css"></head>
<body><h1>Welcome to CloudCart</h1><p>Served by nginx, straight from a folder. No application code at all.</p></body></html>
EOF_H
  printf '%s\n' 'body { font-family: sans-serif; background: #0e1f24; color: #e8f4f2; padding: 2rem; }' 'h1 { color: #3fd0c9; }' > $D/site/style.css
  cat > $D/site/404.html <<'EOF_4'
<!doctype html>
<html><head><meta charset="utf-8"><title>Not found</title><link rel="stylesheet" href="/style.css"></head>
<body><h1>Page not found</h1><p>That page does not exist. <a href="/">Back to CloudCart</a></p></body></html>
EOF_4
  echo ok > $D/site/health.txt
  cat > $D/nginx.conf <<EOF_C
worker_processes 1;
pid $D/nginx.pid;
events { worker_connections 64; }
http {
    include mime.types;
    access_log $D/logs/access.log;
    client_body_temp_path $D/tmp/body;
    proxy_temp_path $D/tmp/proxy;
    fastcgi_temp_path $D/tmp/fcgi;
    uwsgi_temp_path $D/tmp/uwsgi;
    scgi_temp_path $D/tmp/scgi;
    server {
        listen 8181
        root $D/site;
    }
}
EOF_C
  cat > $D/TASKS.txt <<'EOF_T'
LAB 118  Web servers: serve a static site with nginx
Open a terminal in /opt/lab118. The short name  ng  runs nginx with this lab's own config (/opt/lab118/nginx.conf).  Load it with: source shortcuts118.sh

1  Test the config:   ng -t       It fails: read the line number in the message, open nginx.conf in vim, and fix the mistake.
2  Test again until it says "test is successful".
3  Start nginx:       ng          then check it:   curl -I localhost:8181
4  Make a friendly 404: inside the server block add the line   error_page 404 /404.html;
5  Hide the nginx version: inside the http block (above the server block) add   server_tokens off;
6  Apply your changes without stopping nginx:   ng -t    then    ng -s reload
7  Prove it:   curl -s localhost:8181   (the CloudCart page)    curl -s localhost:8181/missing   (your 404 page)    curl -I localhost:8181   (Server: nginx, no version)
8  lab check   (judges you: you need all 5 PASS)
9  lab down    (stops nginx and removes everything)
If something fails, read the nginx error: it names the file and the line.
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  echo "lab 118 ready in $D. Read TASKS.txt, then run: ng -t"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  if $RU $NG -t >/dev/null 2>&1; then ok "1 the config passes  ng -t"; else no "1 the config fails the test: run  ng -t  and fix the line it names"; fi
  pid=$(cat $D/nginx.pid 2>/dev/null)
  code=$(curl -s -o /dev/null -m 3 -w '%{http_code}' $B/ 2>/dev/null)
  if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && [ "$code" = 200 ]; then ok "2 nginx is running and answers on port 8181"; else no "2 nginx is not answering on port 8181: start it with  ng"; fi
  if curl -s -m 3 $B/ 2>/dev/null | grep -q 'Welcome to CloudCart'; then ok "3 the CloudCart page is served"; else no "3 the CloudCart page is not served: check the root folder in the server block"; fi
  c4=$(curl -s -o /dev/null -m 3 -w '%{http_code}' $B/missing 2>/dev/null)
  if [ "$c4" = 404 ] && curl -s -m 3 $B/missing 2>/dev/null | grep -q 'Page not found'; then ok "4 a missing page gives a 404 with your friendly page"; else no "4 /missing must be a 404 that shows the friendly page: add  error_page 404 /404.html;  then ng -s reload"; fi
  sv=$(curl -sI -m 3 $B/ 2>/dev/null | tr -d '\r' | sed -n 's/^[Ss]erver: *//p')
  if [ "$sv" = nginx ]; then ok "5 the Server header hides the version"; else no "5 the Server header shows '${sv:-nothing}': add  server_tokens off;  in the http block, then ng -s reload"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 118 is up in $D" || echo "lab 118 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 118 removed" ;; status) status ;; *) echo "usage: lab118.sh up|check|down|status" ;; esac
