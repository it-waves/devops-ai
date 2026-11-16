#!/bin/sh
# lab123.sh : Web servers and reverse proxies, lesson 6: timeouts, request-size limits and secure defaults in nginx. Run with sudo, on any Linux machine with nginx, curl and python3.
#   up | check | down | status
# Needs: sudo apt install -y nginx curl iproute2 python3     ports 8231 and 8239 free. (The lab runs its own private nginx from /opt/lab123; it does not touch the system nginx.)
# Mission: a small nginx site has risky defaults. Tighten it, one setting at a time, and prove each fix with a request.
D=${LAB123_DIR:-/opt/lab123}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then RU=""; else RU="runuser -u $OWNER --"; fi
NG="nginx -p $D -e $D/logs/error.log -c $D/nginx.conf"
down() {
  [ -f $D/nginx.pid ] && kill "$(cat $D/nginx.pid)" 2>/dev/null
  pkill -f "$D/backend.py" 2>/dev/null; sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  for t in nginx curl python3; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y nginx curl iproute2 python3"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  [ -f /etc/nginx/mime.types ] || { echo "/etc/nginx/mime.types not found: run  sudo apt install -y nginx"; exit 1; }
  for p in 8231 8239; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/site $D/logs $D/tmp
  cp /etc/nginx/mime.types $D/mime.types
  cat > $D/site/index.html <<'EOF_H'
<!doctype html>
<html><head><meta charset="utf-8"><title>CloudCart</title></head>
<body><h1>Welcome to CloudCart</h1></body></html>
EOF_H
  printf 'DB_PASSWORD=hunter2\nAPI_KEY=demo-not-real\n' > $D/site/.env
  head -c 3000000 /dev/zero > $D/big.bin
  head -c 100000 /dev/zero > $D/small.bin
  cat > $D/backend.py <<'EOF_B'
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def reply(self, t):
        b = t.encode(); self.send_response(200); self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path.startswith('/slow'): time.sleep(4); self.reply('slow answer\n')
        else: self.reply('ok\n')
    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0)); self.rfile.read(n); self.reply('got %d bytes\n' % n)
ThreadingHTTPServer(('127.0.0.1', 8239), H).serve_forever()
EOF_B
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
        listen 8231;
        root $D/site;
        client_max_body_size 0;
        location /slow { proxy_pass http://127.0.0.1:8239; }
        location /upload { proxy_pass http://127.0.0.1:8239; }
    }
}
EOF_C
  cat > $D/TASKS.txt <<'EOF_T'
LAB 123  Timeouts, request-size limits and secure defaults
Open a terminal in /opt/lab123. The short name  ng  runs nginx with this lab's own config (/opt/lab123/nginx.conf).  Load it with: source shortcuts123.sh
nginx runs on port 8231. A slow app sits behind it on port 8239: the path /slow answers after 4 seconds, and /upload accepts a file.

1  Look at the risks (each one is a request):
     curl -sI localhost:8231 | grep Server                 the server version is shown to everyone
     curl -s localhost:8231/.env                           a secret file is served
     curl -s -o /dev/null -w "%{http_code}\n" --data-binary @big.bin localhost:8231/upload     a 3 MB upload is accepted
     curl -s -o /dev/null -w "%{http_code} %{time_total}\n" localhost:8231/slow                nginx waits for the slow app
2  Edit nginx.conf (vim nginx.conf), inside the server block:
     client_max_body_size 1m;                      (it is 0, which means unlimited)
     server_tokens off;
     client_header_timeout 10s;
     client_body_timeout 10s;
     keepalive_timeout 15s;
     location ~ /\. { deny all; }                  (dot files are never served)
   and in  location /slow  add:   proxy_read_timeout 2s;
   (use whole seconds, written like 10s)
3  Test and apply:   ng -t && ng -s reload
4  Repeat the four requests from step 1 and read each answer: no version, .env refused, upload 413, /slow gives 504 after about 2 seconds.
5  Prove nothing good broke:   curl -s -o /dev/null -w "%{http_code}\n" --data-binary @small.bin localhost:8231/upload     (still 200)
6  lab check   (judges you: you need all 5 PASS)
7  lab down    (stops everything and removes it all)
If something fails, read the nginx error: it names the file and the line.
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  ( $RU python3 $D/backend.py </dev/null >/dev/null 2>&1 & ) ; $RU $NG; sleep 1
  echo "lab 123 ready in $D. Read TASKS.txt, then try the first request"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  conf=$($RU $NG -T 2>/dev/null); pid=$(cat $D/nginx.pid 2>/dev/null)
  up_ok=0; $RU $NG -t >/dev/null 2>&1 && [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && up_ok=1
  code() { curl -s -m 12 -o /dev/null -w '%{http_code}' "$@" 2>/dev/null; }
  c=$(code localhost:8231/slow)
  if [ $up_ok -eq 1 ] && [ "$c" = 504 ]; then ok "1 /slow gives up with 504 instead of waiting for the app"; else no "1 add proxy_read_timeout 2s; inside location /slow, then ng -t && ng -s reload (got '$c', want 504)"; fi
  big=$(code --data-binary @$D/big.bin localhost:8231/upload); small=$(code --data-binary @$D/small.bin localhost:8231/upload)
  if [ "$big" = 413 ] && [ "$small" = 200 ]; then ok "2 big upload refused (413), small upload still works"; else no "2 set client_max_body_size 1m; (big gave '$big', want 413; small gave '$small', want 200)"; fi
  srv=$(curl -sI -m 5 localhost:8231 2>/dev/null | tr -d '\r' | sed -n 's/^[Ss]erver: //p')
  if [ "$srv" = nginx ]; then ok "3 the server version is hidden"; else no "3 add server_tokens off; (the Server header is '$srv')"; fi
  h=$(code localhost:8231/.env); i=$(code localhost:8231/index.html)
  if { [ "$h" = 403 ] || [ "$h" = 404 ]; } && [ "$i" = 200 ]; then ok "4 hidden files are refused, normal pages still work"; else no "4 add:  location ~ /\\. { deny all; }  (.env gave '$h', index.html gave '$i')"; fi
  bad=""
  for d in client_header_timeout client_body_timeout keepalive_timeout; do
    v=$(echo "$conf" | sed -n "s/^ *$d  *\([0-9][0-9]*\)s;.*/\1/p" | head -n 1)
    { [ -n "$v" ] && [ "$v" -le 15 ]; } || bad="$bad $d"
  done
  if [ -z "$bad" ]; then ok "5 slow-client timeouts are set (15 seconds or less)"; else no "5 set in whole seconds (like 10s), 15 or less:$bad"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 123 is up in $D" || echo "lab 123 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 123 removed" ;; status) status ;; *) echo "usage: lab123.sh up|check|down|status" ;; esac
