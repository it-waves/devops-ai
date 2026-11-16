#!/bin/sh
# lab124.sh : Web servers and reverse proxies, lesson 7: troubleshoot nginx 502, 503, 504 and TLS errors. Run with sudo, on any Linux machine with nginx, curl, openssl and python3.
#   up | check | down | status
# Needs: sudo apt install -y nginx curl openssl iproute2 python3     ports 8241, 8243 and 8248 free. (The lab runs its own private nginx from /opt/lab124; it does not touch the system nginx.)
# Mission: four things are broken in one nginx setup. Read the evidence, find each cause, and fix them all.
D=${LAB124_DIR:-/opt/lab124}
OWNER=${SUDO_USER:-root}
if [ "$OWNER" = root ]; then RU=""; else RU="runuser -u $OWNER --"; fi
NG="nginx -p $D -e $D/logs/error.log -c $D/nginx.conf"
down() {
  [ -f $D/nginx.pid ] && kill "$(cat $D/nginx.pid)" 2>/dev/null
  pkill -f "$D/backend.py" 2>/dev/null; sleep 1
  rm -rf "${D:?}"/* "${D:?}"/.[!.]* 2>/dev/null; rmdir "$D" 2>/dev/null; true
}
up() {
  for t in nginx curl openssl python3; do command -v $t >/dev/null 2>&1 || { echo "$t not found: run  sudo apt install -y nginx curl openssl iproute2 python3"; exit 1; }; done
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  [ -f /etc/nginx/mime.types ] || { echo "/etc/nginx/mime.types not found: run  sudo apt install -y nginx"; exit 1; }
  for p in 8241 8243 8248; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/site $D/logs $D/tmp
  cp /etc/nginx/mime.types $D/mime.types
  cat > $D/site/index.html <<'EOF_H'
<!doctype html>
<html><head><meta charset="utf-8"><title>CloudCart</title></head>
<body><h1>Welcome to CloudCart</h1></body></html>
EOF_H
  openssl req -x509 -newkey rsa:2048 -nodes -days 30 -subj /CN=wrong.example -keyout $D/key.pem -out $D/cert.pem >/dev/null 2>&1
  touch $D/maintenance.flag
  cat > $D/backend.py <<'EOF_B'
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        if self.path.startswith('/report'): time.sleep(3)
        b = b'ok\n'; self.send_response(200); self.send_header('Content-Length', '3'); self.end_headers(); self.wfile.write(b)
ThreadingHTTPServer(('127.0.0.1', 8248), H).serve_forever()
EOF_B
  cat > $D/probe.sh <<'EOF_P'
#!/bin/sh
# asks each of the four things in turn and prints the status code
cd "$(dirname "$0")"
c() { curl -s -o /dev/null -m 8 -w '%{http_code}' "$@" 2>/dev/null; }
for p in app report shop; do printf '%-8s %s\n' $p "$(c localhost:8241/$p)"; done
s=$(c --cacert cert.pem https://localhost:8243/); [ "$s" = 000 ] && s="fail"; printf '%-8s %s\n' https "$s"
EOF_P
  chmod +x $D/probe.sh
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
        listen 8241;
        root $D/site;
        location /app { proxy_pass http://127.0.0.1:8249; }
        location /report {
            proxy_pass http://127.0.0.1:8248;
            proxy_read_timeout 1s;
        }
        location /shop {
            if (-f $D/maintenance.flag) { return 503; }
            proxy_pass http://127.0.0.1:8248;
        }
    }
    server {
        listen 8243 ssl;
        root $D/site;
        ssl_certificate $D/cert.pem;
        ssl_certificate_key $D/key.pem;
    }
}
EOF_C
  cat > $D/TASKS.txt <<'EOF_T'
LAB 124  Troubleshoot 502, 503, 504 and TLS errors
Open a terminal in /opt/lab124. The short name  ng  runs nginx with this lab's own config (/opt/lab124/nginx.conf).  Load it with: source shortcuts124.sh
nginx serves two sites: http on port 8241 (paths /app, /report, /shop, each proxied to a small app on port 8248) and https on port 8243. Four things are broken.

1  See the symptoms:   ./probe.sh      (prints the status of /app, /report, /shop and https)
2  For each problem, find the cause in the evidence. Do not guess: read.
   502 on /app:     grep -o 'connect() failed ([^)]*)' logs/error.log | head -n 1       and see what listens:   ss -ltn | grep -o '824[0-9]'
   504 on /report:  grep -o 'upstream timed out ([^)]*)' logs/error.log | head -n 1
   503 on /shop:    there is no error in the log: nginx answers 503 on purpose. Look in the config:   grep -n maintenance nginx.conf    and   ls
   https fails:     openssl x509 -in cert.pem -noout -subject      (which name does the certificate hold?)
3  Write three answers into  answers.txt  BEFORE you fix anything, one per line, one word each:
     line 1: the one-word reason for the 502: the last word of the message, after  111: Connection
     line 2: the one-word reason for the 504: the word between  upstream  and  out  in the message
     line 3: the name the certificate holds (the word after  CN = )
4  Fix the four problems:
     502:  in nginx.conf, the /app proxy_pass points at the wrong port: use the port the app listens on (8248)
     504:  in nginx.conf, proxy_read_timeout 1s is shorter than the report takes: set it to 10s
     503:  remove the maintenance flag:   rm maintenance.flag
     TLS:  make a new certificate for the name localhost:
       openssl req -x509 -newkey rsa:2048 -nodes -days 30 -subj /CN=localhost -addext subjectAltName=DNS:localhost -keyout key.pem -out cert.pem
5  Test and apply:   ng -t && ng -s reload
6  ./probe.sh   should now show 200 four times
7  lab check   (judges you: you need all 5 PASS)
8  lab down    (stops everything and removes it all)
If something fails, read the nginx error: it names the file and the line.
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  ( $RU python3 $D/backend.py </dev/null >/dev/null 2>&1 & ) ; $RU $NG; sleep 1
  echo "lab 124 ready in $D. Read TASKS.txt, then run: ./probe.sh"
}
pass=0; total=5
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  code() { curl -s -m 12 -o /dev/null -w '%{http_code}' "$@" 2>/dev/null; }
  c=$(code localhost:8241/app)
  if [ "$c" = 200 ]; then ok "1 /app works: the 502 is fixed"; else no "1 /app gives '$c': proxy_pass must point at the port the app listens on (see ss -ltn)"; fi
  c=$(code localhost:8241/report)
  if [ "$c" = 200 ]; then ok "2 /report works: the 504 is fixed"; else no "2 /report gives '$c': proxy_read_timeout must be longer than the report takes (3 seconds)"; fi
  c=$(code localhost:8241/shop)
  if [ "$c" = 200 ]; then ok "3 /shop works: the 503 is fixed"; else no "3 /shop gives '$c': nginx answers 503 on purpose, look in the config for why"; fi
  c=$(code --cacert $D/cert.pem https://localhost:8243/)
  if [ "$c" = 200 ]; then ok "4 https verifies and works: the TLS problem is fixed"; else no "4 https failed ('$c'): the certificate must be valid for the name localhost"; fi
  a1=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r' | tr A-Z a-z); a2=$(sed -n 2p $D/answers.txt 2>/dev/null | tr -d ' \r' | tr A-Z a-z); a3=$(sed -n 3p $D/answers.txt 2>/dev/null | tr -d ' \r' | tr A-Z a-z)
  if [ "$a1" = refused ] && [ "$a2" = timed ] && [ "$a3" = wrong.example ]; then ok "5 your three diagnoses are right"; else no "5 answers.txt needs 3 lines: the 502 reason, the 504 reason, the name in the old certificate (got '$a1' '$a2' '$a3')"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 124 is up in $D" || echo "lab 124 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 124 removed" ;; status) status ;; *) echo "usage: lab124.sh up|check|down|status" ;; esac
