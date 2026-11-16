#!/bin/sh
# lab125.sh : Web servers and reverse proxies, MASTERY lesson: build, secure, balance and troubleshoot one web tier. Run with sudo, on any Linux machine with nginx, curl, openssl and python3.
#   up | check | down | status
# Needs: sudo apt install -y nginx curl openssl iproute2 python3     ports 8251, 8253, 8254 and 8255 free. (The lab runs its own private nginx from /opt/lab125; it does not touch the system nginx.)
# Mission: a half-built web tier for CloudCart. Finish it, prove every objective of the domain, document it, and clean up.
D=${LAB125_DIR:-/opt/lab125}
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
  for p in 8251 8253 8254 8255; do if curl -s -o /dev/null -m 2 localhost:$p; then echo "port $p is already in use: stop what uses it first"; exit 1; fi; done
  down; mkdir -p $D/site $D/logs $D/tmp
  cp /etc/nginx/mime.types $D/mime.types
  cat > $D/site/index.html <<'EOF_H'
<!doctype html>
<html><head><meta charset="utf-8"><title>CloudCart</title></head>
<body><h1>Welcome to CloudCart</h1></body></html>
EOF_H
  openssl req -x509 -newkey rsa:2048 -nodes -days 30 -subj /CN=wrong.example -keyout $D/key.pem -out $D/cert.pem >/dev/null 2>&1
  # a day of old traffic, to read: 40 requests
  i=0; for c in 200 200 200 404 200 502 200 200 200 504 200 200 404 200 200 503 200 200 200 200 200 502 200 404 200 200 200 504 200 200 200 200 200 500 200 200 200 404 200 502; do
    i=$((i+1)); printf '10.0.0.%s - - [01/Jan/2026:10:%02d:00 +0000] "GET /page%s HTTP/1.1" %s 512\n' $((i%9+1)) $i $i $c
  done > $D/logs/seed.log
  cat > $D/backend.py <<'EOF_B'
import sys, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
P = int(sys.argv[1]); I = sys.argv[2]
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def send(self, s):
        b = s.encode(); self.send_response(200); self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path.startswith('/report'): time.sleep(3); self.send('report from %s\n' % I)
        elif self.path.startswith('/whoami'):
            h = self.headers
            self.send('id=%s host=%s xff=%s proto=%s\n' % (I, h.get('Host', '-'), h.get('X-Forwarded-For', '-'), h.get('X-Forwarded-Proto', '-')))
        else: self.send('id=%s\n' % I)
    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0)); self.rfile.read(n); self.send('got %d bytes\n' % n)
ThreadingHTTPServer(('127.0.0.1', P), H).serve_forever()
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
    client_max_body_size 100m;
    upstream pool {
        server 127.0.0.1:8254;
        server 127.0.0.1:8256;
    }
    server {
        listen 8251;
        root $D/sitee;
        location /api/ { proxy_pass http://pool/; }
        location /report { proxy_pass http://pool; proxy_read_timeout 1s; }
    }
    server {
        listen 8253 ssl;
        root $D/site;
        ssl_certificate $D/cert.pem;
        ssl_certificate_key $D/key.pem;
    }
}
EOF_C
  cat > $D/TASKS.txt <<'EOF_T'
LAB 125  MASTERY: build, secure, balance and troubleshoot one web tier
Open a terminal in /opt/lab125. The short name  ng  runs nginx with this lab's own config (/opt/lab125/nginx.conf).  Load it with: source shortcuts125.sh
CloudCart's web tier is half built. nginx listens on http 8251 and https 8253. Two small apps, A and B, listen on 8254 and 8255. Prove every objective of the domain.

  site:   /          static files        /api/...  proxied to the apps        /report  a slow report (3 seconds)
  files:  nginx.conf (the config)   site/index.html   logs/seed.log (a day of old traffic)   cert.pem + key.pem

1  Static serving (O01, O02):   / must serve the CloudCart page, and  ng -t  must pass.      The root path in nginx.conf is wrong: ls  shows the real folder.
2  Proxy headers (O03):         the app must see the real Host, X-Forwarded-For and X-Forwarded-Proto.   curl localhost:8251/api/whoami   shows what the app sees.
                                 In the /api/ location add:  proxy_set_header Host $host;   X-Forwarded-For $proxy_add_x_forwarded_for;   X-Forwarded-Proto $scheme;
3  HTTPS (O04):                 https must verify for the name localhost.   openssl x509 -in cert.pem -noout -subject   then make a new certificate (-subj /CN=localhost -addext subjectAltName=DNS:localhost).
4  Health + balancing (O05):    both apps must answer:   for i in 1 2 3 4 5 6; do curl -s localhost:8251/api/; done      (a wrong port is in the upstream block)
                                 and add a health endpoint:   location = /health { return 200 "ok\n"; }
5  Logs (O06):                  read logs/seed.log, then write two lines in answers.txt:  line 1: how many requests failed with a 5xx status;  line 2: the 5xx status that happened most often.
                                 hint: grep, then  awk '{print $9}' | sort | uniq -c
6  Limits (O07):                uploads over 1 MB must be refused with 413, small ones accepted, and the Server header must not show a version:   client_max_body_size 1m;   server_tokens off;
7  Troubleshoot (O08):          /report gives a 504. Read the error log (grep 'timed out' logs/error.log), then make the timeout longer than the 3 seconds the report takes.
8  Document:                    write notes.txt with three lines that start with:  results:   troubleshooting:   cleanup:   and a short sentence after each.

Test and apply:   ng -t && ng -s reload        Then:   lab check  (8 checks, you need all 8)       Last:   lab down  (stops everything and removes it all)
If something fails, read the nginx error: it names the file and the line.
EOF_T
  chown -R $OWNER $D 2>/dev/null; chmod -R a+rX $D
  ( $RU python3 $D/backend.py 8254 A </dev/null >/dev/null 2>&1 & ) ; ( $RU python3 $D/backend.py 8255 B </dev/null >/dev/null 2>&1 & ); $RU $NG; sleep 1
  echo "lab 125 ready in $D. Read TASKS.txt, then start with: curl -i localhost:8251/"
}
pass=0; total=8
ok() { pass=$((pass+1)); echo "  PASS  $1"; }
no() { echo "  FAIL  $1"; }
check() {
  [ -d $D ] || { echo "lab is not up: run  lab up"; exit 1; }
  code() { curl -s -m 12 -o /dev/null -w '%{http_code}' "$@" 2>/dev/null; }
  c=$(code localhost:8251/); b=$(curl -s -m 8 localhost:8251/ 2>/dev/null)
  if [ "$c" = 200 ] && echo "$b" | grep -q CloudCart && $NG -t >/dev/null 2>&1; then ok "1 static site served and the config tests OK (O01, O02)"; else no "1 / gives '$c': the root path must be the folder that holds index.html, and ng -t must pass"; fi
  w=$(curl -s -m 8 localhost:8251/api/whoami 2>/dev/null)
  if echo "$w" | grep -q 'host=localhost' && ! echo "$w" | grep -q 'xff=-' && echo "$w" | grep -q 'proto=http'; then ok "2 the app sees the real Host and forwarded headers (O03)"; else no "2 the app sees: '$w' : set Host, X-Forwarded-For and X-Forwarded-Proto in the /api/ location"; fi
  c=$(code --cacert $D/cert.pem https://localhost:8253/)
  if [ "$c" = 200 ]; then ok "3 https verifies and works (O04)"; else no "3 https failed ('$c'): the certificate must be valid for the name localhost"; fi
  s=$(for i in 1 2 3 4 5 6; do curl -s -m 8 localhost:8251/api/ 2>/dev/null; done | sort -u | tr '\n' ' '); h=$(curl -s -m 8 localhost:8251/health 2>/dev/null)
  if [ "$s" = "id=A id=B " ] && [ "$h" = ok ]; then ok "4 both apps answer and /health says ok (O05)"; else no "4 apps seen: '$s' health: '$h' : fix the upstream port, and add location = /health"; fi
  a1=$(sed -n 1p $D/answers.txt 2>/dev/null | tr -d ' \r'); a2=$(sed -n 2p $D/answers.txt 2>/dev/null | tr -d ' \r')
  if [ "$a1" = 7 ] && [ "$a2" = 502 ]; then ok "5 your reading of the logs is right (O06)"; else no "5 answers.txt needs 2 lines: how many 5xx failed, and which 5xx was most common (got '$a1' '$a2')"; fi
  big=$(head -c 2000000 /dev/zero | curl -s -m 12 -o /dev/null -w '%{http_code}' --data-binary @- localhost:8251/api/upload 2>/dev/null); small=$(curl -s -m 8 -o /dev/null -w '%{http_code}' --data-binary hello localhost:8251/api/upload 2>/dev/null)
  sv=$(curl -sI -m 8 localhost:8251/ 2>/dev/null | tr -d '\r' | grep -i '^server:' | cut -d' ' -f2-)
  if [ "$big" = 413 ] && [ "$small" = 200 ] && [ "$sv" = nginx ]; then ok "6 big upload refused, small accepted, no version shown (O07)"; else no "6 big '$big' small '$small' server '$sv' : client_max_body_size 1m; and server_tokens off;"; fi
  c=$(code localhost:8251/report)
  if [ "$c" = 200 ]; then ok "7 /report works: the 504 is fixed (O08)"; else no "7 /report gives '$c': proxy_read_timeout must be longer than the 3 seconds the report takes"; fi
  n=0; for w in results troubleshooting cleanup; do grep -qiE "^$w: *[^ ]{3,}" $D/notes.txt 2>/dev/null && n=$((n+1)); done
  if [ $n = 3 ]; then ok "8 notes.txt documents results, troubleshooting and cleanup"; else no "8 notes.txt needs 3 lines starting results:  troubleshooting:  cleanup:  each with a sentence"; fi
  echo; echo "$pass / $total passed"; [ $pass -eq $total ]
}
status() { [ -d $D ] && echo "lab 125 is up in $D" || echo "lab 125 is not up"; }
case "$1" in up) up ;; check) check ;; down) down; echo "lab 125 removed" ;; status) status ;; *) echo "usage: lab125.sh up|check|down|status" ;; esac
