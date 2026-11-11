#!/bin/bash
# lab26.sh : MC02 mastery lab (computer fundamentals). Needs Linux, python3, curl. No sudo, everything lives in /tmp/lab26.
#   ./lab26.sh up | check | down
D=/tmp/lab26
down() {
  pkill -f "$D/shop.py" 2>/dev/null; pkill -f "$D/nightly-report.py" 2>/dev/null
  rm -rf "$D"; echo "lab removed"
}
up() {
  down >/dev/null; mkdir -p "$D/logs" "$D/data"
  cat > "$D/shop.py" <<'PY'
import os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
data = os.environ.get("SHOP_DATA")
if not data:
    print("ERROR: SHOP_DATA is not set. Set it to the folder that holds products.txt", flush=True); sys.exit(1)
class H(BaseHTTPRequestHandler):
    def do_GET(s):
        if s.path != "/products": s.send_response(404); s.end_headers(); s.wfile.write(b"not found\n"); return
        raw = open(os.path.join(data, "products.txt"), "rb").read()
        if b"\r" in raw:
            s.send_response(500); s.end_headers(); s.wfile.write(b"bad data: carriage return in products.txt\n"); return
        s.send_response(200); s.send_header("Content-Type", "text/plain"); s.end_headers(); s.wfile.write(raw)
    def log_message(s, *a): pass
print("shop listening on 8090", flush=True); HTTPServer(("127.0.0.1", 8090), H).serve_forever()
PY
  cat > "$D/start-shop.sh" <<SH
#!/bin/sh
nohup python3 $D/shop.py >> $D/logs/shop.log 2>&1 &
echo "shop starting, output goes to $D/logs/shop.log"
SH
  chmod +x "$D/start-shop.sh"
  printf 'bread\r\nmilk\r\neggs\r\n' > "$D/data/products.txt"
  echo 'while True: pass' > "$D/nightly-report.py"
  fallocate -l 150M "$D/logs/old-requests.log" 2>/dev/null || head -c 150000000 /dev/zero > "$D/logs/old-requests.log"
  nohup python3 "$D/nightly-report.py" >/dev/null 2>&1 &
  sleep 1; echo "lab is up. Four things are wrong with the shop server. Mission: curl http://localhost:8090/products must answer 200."
}
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fi; }
check() {
  chk "1 no runaway process" "! pgrep -f $D/nightly-report.py"
  chk "2 logs under 5 MB" "[ \$(du -sk $D/logs | cut -f1) -lt 5000 ]"
  chk "3 shop is running" "pgrep -f $D/shop.py"
  chk "4 /products answers 200" "[ \"\$(curl -s --noproxy '*' -m 2 -o /dev/null -w %{http_code} http://localhost:8090/products)\" = 200 ]"
}
case "$1" in up) up;; check) check;; down) down;; *) echo "usage: ./lab26.sh up|check|down";; esac
