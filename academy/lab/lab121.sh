#!/bin/sh
# lab121.sh : Web servers and reverse proxies, lesson 4: health checks and basic load balancing with nginx. Run with sudo, on any Linux machine with nginx, python3 and curl.
#   up | check | down | status | stop a|b|c | start a|b|c
# Needs: sudo apt install -y nginx python3 curl iproute2     ports 8211 (nginx) and 8212 8213 8214 (three backends) free. (The lab runs its own private nginx and three tiny backends from /opt/lab121; it does not touch the system nginx.)
# Mission: one backend is a single point of failure. Build a pool of three, share the traffic, survive a failure, and keep one as a backup.
D=${LAB121_DIR:-/opt/lab121}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then RU=""; else RU="runuser -u $OWNER --"; fi
NG="nginx -p $D -e $D/logs/error.log -c $D/nginx.conf"
port() { case "$1" in a) echo 8212 ;; b) echo 8213 ;; c) echo 8214 ;; *) echo "use a, b or c" >&2; return 1 ;; esac; }
bstart() { p=$(port "$1") || return 1; n=$(echo "$1" | tr a-c A-C); [ -f $D/pids/$1.pid ] && kill -0 "$(cat $D/pids/$1.pid)" 2>/dev/null && { echo "backend $n is already running"; return 0; }; ( cd $D && nohup $RU python3 $D/backend.py $n $p >/dev/null 2>&1 & echo $! > $D/pids/$1.pid ); sleep 0.7; echo "backend $n started on port $p"; }
bstop() { p=$(port "$1") || return 1; n=$(echo "$1" | tr a-c A-C); [ -f $D/pids/$1.pid ] && kill "$(cat $D/pids/$1.pid)" 2>/dev/null; rm -f $D/pids/$1.pid; sleep 0.5; echo "backend $n stopped"; }
down() {
  [ -f $D/nginx.pid ] && kill "$(cat $D/nginx.pid)" 2>/dev/null
  for n in a b c; do [ -f $D/pids/$n.pid ] && kill "$(cat $D/pids/$n.pid)" 2>/dev/null; done; sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  for t in nginx python3 curl; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y nginx python3 curl iproute2"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  [ -f /etc/nginx/mime.types ] || { echo "/etc/nginx/mime.types not found: run  sudo apt install -y nginx"; exit 1; }
  for p in 8211 8212 8213 8214; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/logs $D/tmp $D/pids
  cp /etc/nginx/mime.types $D/mime.types
  cat > $D/backend.py <<'EOF_B'
# CloudCart backend (stand-in app server): says its own name. Usage: backend.py NAME PORT
import sys, http.server
NAME, PORT = sys.argv[1], int(sys.argv[2])
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = ("backend %s\n" % NAME).encode()
        self.send_response(200); self.send_header("Content-Type", "text/plain"); self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
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
        listen 8211;
        location / {
            proxy_pass http://127.0.0.1:8212;
        }
    }
}
EOF_C
  cat > $D/TASKS.txt <<'EOF_T'
LAB 121  Health checks and basic load balancing with nginx
Open a terminal in /opt/lab121. The short name  ng  runs nginx with this lab's own config (/opt/lab121/nginx.conf).  Load it with: source shortcuts121.sh
Three backends are running: A on 8212, B on 8213, C on 8214. nginx listens on 8211 and sends everything to A only.
Handy:   lab stop b   (stops backend B)     lab start b   (starts it again)

1  Ask nginx six times:   for i in 1 2 3 4 5 6; do curl -s localhost:8211; done      Always A. If A dies, the site dies.
2  In nginx.conf, above the  server {  line, add a pool (inside http):
     upstream cart {
         server 127.0.0.1:8212;
         server 127.0.0.1:8213;
         server 127.0.0.1:8214;
     }
   and change the proxy_pass line to:   proxy_pass http://cart;
   Test and apply:   ng -t && ng -s reload      Repeat step 1: A, B, C, A, B, C (round robin).
3  Break one on purpose:   lab stop b   then repeat step 1. No errors: nginx skips the dead one. Then:   lab start b
4  Make failure handling explicit. On the A and B lines add   max_fails=2 fail_timeout=5s   (fail_timeout must be 10s or less)
   and on the C line add the word   backup   (C only serves when A and B are both down).
   Test and apply, then repeat step 1: only A and B answer.
5  Prove the backup:   lab stop a ; lab stop b   then step 1 again: only C answers. Then   lab start a ; lab start b
6  lab check   (judges you: you need all 5 PASS. It stops and starts backends by itself and takes about 20 seconds)
7  lab down    (stops nginx and all three backends and removes everything)
If something fails, read the nginx error: it names the file and the line. Passive health checks: nginx learns a backend is down only when a real request to it fails.
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  for n in a b c; do bstart $n >/dev/null; done
  $RU $NG; sleep 0.5
  echo "lab 121 ready in $D. Read TASKS.txt, then run: ng -t"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
hit() { i=0; while [ $i -lt $1 ]; do curl -s -m 3 localhost:8211/ 2>/dev/null; i=$((i+1)); done; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  for n in a b c; do bstart $n >/dev/null; done
  conf=$($RU $NG -T 2>/dev/null); pid=$(cat $D/nginx.pid 2>/dev/null)
  ns=$(echo "$conf" | grep -cE '^ *server 127\.0\.0\.1:821[234]')
  if $RU $NG -t >/dev/null 2>&1 && [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null && [ "$ns" -eq 3 ] && echo "$conf" | grep -Eq 'proxy_pass http://[a-z_]+;'; then ok "1 nginx runs with a pool of three servers"; else no "1 need a running nginx, an upstream with the three servers and proxy_pass http://cart;"; fi
  r=$(hit 6 | sort | uniq -c | tr -s ' ' | tr '\n' ',')
  if [ "$r" = " 3 backend A, 3 backend B," ]; then ok "2 traffic is shared by A and B only"; else no "2 six requests must give 3 x A and 3 x B and no C, got:$r"; fi
  nf=$(echo "$conf" | grep -cE '^ *server 127\.0\.0\.1:821[23] .*max_fails=[0-9]+ .*fail_timeout=([0-9]|10)s')
  if [ "$nf" -ge 2 ] && echo "$conf" | grep -Eq 'server 127\.0\.0\.1:8214 .*backup'; then ok "3 max_fails, fail_timeout and a backup are set"; else no "3 put max_fails= and fail_timeout=10s-or-less on A and B, and backup on C"; fi
  bstop b >/dev/null; r=$(hit 4 | sort | uniq -c | tr -s ' ' | tr '\n' ','); bstart b >/dev/null
  if [ "$r" = " 4 backend A," ] && [ "$ns" -eq 3 ]; then ok "4 with B down, every request still succeeds"; else no "4 with B stopped, 4 requests must all be answered by A, got:$r"; fi
  bstop a >/dev/null; bstop b >/dev/null; r=$(hit 3 | sort | uniq -c | tr -s ' ' | tr '\n' ','); bstart a >/dev/null; bstart b >/dev/null
  if [ "$r" = " 3 backend C," ]; then ok "5 with A and B down, the backup C answers"; else no "5 with A and B stopped, the backup C must answer, got:$r"; fi
  sleep 11
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 121 is up in $D" || echo "lab 121 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 121 removed" ;; status) status ;; stop) bstop "$2" ;; start) bstart "$2" ;; *) echo "usage: lab121.sh up|check|down|status|stop a|b|c|start a|b|c" ;; esac
