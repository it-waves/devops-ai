#!/bin/sh
# lab119.sh : Web servers and reverse proxies, lesson 2: route traffic to a backend and pass the proxy headers. Run with sudo, on any Linux machine with nginx, python3 and curl.
#   up | check | down | status
# Needs: sudo apt install -y nginx python3 curl iproute2     ports 8191 and 8192 free. (The lab runs its own private nginx and its own tiny backend from /opt/lab119; it does not touch the system nginx.)
# Mission: nginx serves the CloudCart page, but /api/ goes nowhere. Proxy it to the backend and pass the real client details along.
D=${LAB119_DIR:-/opt/lab119}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then RU=""; else RU="runuser -u $OWNER --"; fi
B=localhost:8191
NG="nginx -p $D -e $D/logs/error.log -c $D/nginx.conf"
down() {
  [ -f $D/nginx.pid ] && kill "$(cat $D/nginx.pid)" 2>/dev/null
  [ -f $D/backend.pid ] && kill "$(cat $D/backend.pid)" 2>/dev/null; sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  for t in nginx python3 curl; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y nginx python3 curl iproute2"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  [ -f /etc/nginx/mime.types ] || { echo "/etc/nginx/mime.types not found: run  sudo apt install -y nginx"; exit 1; }
  for p in 8191 8192; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/site $D/logs $D/tmp
  cp /etc/nginx/mime.types $D/mime.types
  cat > $D/site/index.html <<'EOF_H'
<!doctype html>
<html><head><meta charset="utf-8"><title>CloudCart</title></head>
<body><h1>Welcome to CloudCart</h1><p>Static pages come from nginx. The API lives behind it.</p></body></html>
EOF_H
  cat > $D/backend.py <<'EOF_B'
# CloudCart backend (stand-in app server): tells you exactly what it received.
import http.server
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        h = self.headers
        body = "backend says hello\npath=%s\nHost: %s\nX-Real-IP: %s\nX-Forwarded-For: %s\nX-Forwarded-Proto: %s\n" % (
            self.path, h.get("Host", "-"), h.get("X-Real-IP", "-"), h.get("X-Forwarded-For", "-"), h.get("X-Forwarded-Proto", "-"))
        b = body.encode()
        self.send_response(200); self.send_header("Content-Type", "text/plain"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def log_message(self, *a): pass
http.server.HTTPServer(("127.0.0.1", 8192), H).serve_forever()
EOF_B
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
        listen 8191;
        root $D/site;
        location /api/ {
        }
    }
}
EOF_C
  cat > $D/TASKS.txt <<'EOF_T'
LAB 119  Reverse proxy: route traffic to a backend
Open a terminal in /opt/lab119. The short name  ng  runs nginx with this lab's own config (/opt/lab119/nginx.conf).  Load it with: source shortcuts119.sh
The CloudCart backend is already running on port 8192. nginx is running on port 8191.

1  See the problem:   curl -s localhost:8191/api/hello     (nginx has no idea where /api/ goes, so you get a 404)
2  See the backend on its own:   curl -s localhost:8192/hello
3  In nginx.conf, inside  location /api/ { }  add:   proxy_pass http://127.0.0.1:8192/;   (the slash at the end matters: it removes /api from the path)
4  Apply it:   ng -t && ng -s reload      then   curl -s localhost:8191/api/hello
5  Look at the Host line the backend received: it is 127.0.0.1:8192, not the name the visitor used (localhost). Add:   proxy_set_header Host $host;   to the same location block.
6  Pass the visitor's address and protocol. Add these three lines too:
     proxy_set_header X-Real-IP $remote_addr;
     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
     proxy_set_header X-Forwarded-Proto $scheme;
7  Apply and prove it:   ng -t && ng -s reload     then   curl -s localhost:8191/api/hello
8  lab check   (judges you: you need all 5 PASS)
9  lab down    (stops nginx and the backend and removes everything)
If something fails, read the nginx error: it names the file and the line.
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  $RU nginx -p $D -e $D/logs/error.log -c $D/nginx.conf >/dev/null 2>&1
  ( cd $D && nohup $RU python3 $D/backend.py >/dev/null 2>&1 & echo $! > $D/backend.pid ) 
  sleep 1; chown $OWNER $D/backend.pid 2>/dev/null
  echo "lab 119 ready in $D. Read TASKS.txt, then run: curl -s localhost:8191/api/hello"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  pid=$(cat $D/nginx.pid 2>/dev/null)
  if $RU $NG -t >/dev/null 2>&1 && [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && curl -s -m 3 $B/ 2>/dev/null | grep -q 'Welcome to CloudCart' && [ "$(curl -s -o /dev/null -m 3 -w '%{http_code}' $B/api/hello 2>/dev/null)" = 200 ]; then ok "1 the config passes  ng -t,  the page is served and /api/ answers 200"; else no "1 not yet: the config must pass  ng -t,  the page must be served and /api/hello must answer 200"; fi
  r=$(curl -s -m 3 $B/api/hello 2>/dev/null)
  if echo "$r" | grep -q 'backend says hello'; then ok "2 /api/hello is answered by the backend"; else no "2 /api/hello does not reach the backend: add  proxy_pass http://127.0.0.1:8192/;  in location /api/, then ng -s reload"; fi
  if echo "$r" | grep -q '^path=/hello$'; then ok "3 the backend sees the path /hello (the /api prefix was removed)"; else no "3 the backend must see path=/hello: end the proxy_pass address with a slash"; fi
  if echo "$r" | grep -q '^Host: localhost$'; then ok "4 the backend sees the visitor's Host header"; else no "4 the backend sees '$(echo "$r" | sed -n 's/^Host: //p')' as Host: add  proxy_set_header Host \$host;"; fi
  if echo "$r" | grep -q '^X-Real-IP: 127.0.0.1$' && echo "$r" | grep -q '^X-Forwarded-For: 127.0.0.1$' && echo "$r" | grep -q '^X-Forwarded-Proto: http$'; then ok "5 the backend sees the client address and protocol (X-Real-IP, X-Forwarded-For, X-Forwarded-Proto)"; else no "5 the three forwarding headers are not all arriving: add X-Real-IP, X-Forwarded-For and X-Forwarded-Proto with proxy_set_header"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 119 is up in $D" || echo "lab 119 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 119 removed" ;; status) status ;; *) echo "usage: lab119.sh up|check|down|status" ;; esac
