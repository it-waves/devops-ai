#!/bin/sh
# lab142.sh : Software Testing and QA, lesson 8: performance, load and security checks. Run with sudo.
#   up | check | down | status     Needs: python3 only
D=${LAB142_DIR:-/opt/lab142}
PORT=8142
OWNER=${SUDO_USER:-root}
AS=""; [ "$OWNER" != root ] && AS="runuser -u $OWNER --"
stop() { [ -f $D/.pid ] && kill "$(cat $D/.pid)" 2>/dev/null; pkill -f "$D/server.py" 2>/dev/null; true; }
down() { stop; rm -rf "${D:?}" 2>/dev/null; true; }
up() {
  command -v python3 >/dev/null || { echo "need python3"; exit 1; }
  [ "$(id -u)" = 0 ] || { echo "run with sudo"; exit 1; }
  down; mkdir -p $D/src $D/out $D/demo
  cat > $D/server.py <<'EOF_P'
"""A tiny CloudCart-like service. /cart is fast, /slow is not."""
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            code, body = 200, b"ok"
        elif self.path == "/cart":
            time.sleep(0.02); code, body = 200, b'{"total": 10800}'
        elif self.path == "/slow":
            time.sleep(0.5); code, body = 200, b'{"report": "big"}'
        else:
            code, body = 404, b"no"
        self.send_response(code); self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
    def log_message(self, *a): pass

ThreadingHTTPServer(("127.0.0.1", 8142), H).serve_forever()
EOF_P
  cat > $D/demo/load_demo.py <<'EOF_P'
import sys, time, math, urllib.request
from concurrent.futures import ThreadPoolExecutor
U = "http://127.0.0.1:8142"; path = sys.argv[1]
budget = float(sys.argv[2]) if len(sys.argv) > 2 else None
def hit(_):
    t = time.perf_counter()
    try: ok = urllib.request.urlopen(U + path).status == 200
    except Exception: ok = False
    return (time.perf_counter() - t) * 1000, ok
t0 = time.perf_counter()
with ThreadPoolExecutor(10) as ex: res = list(ex.map(hit, range(60)))
lat = sorted(r[0] for r in res); errs = sum(not r[1] for r in res)
p95 = lat[math.ceil(0.95 * len(lat)) - 1]
print(f"60 requests, 10 at once: p95 {p95:.0f} ms, {errs} errors")
sys.exit(1 if errs or (budget and p95 > budget) else 0)
EOF_P
  cat > $D/src/settings.py <<'EOF_P'
# CloudCart settings: secrets come from the environment, never from code.
import os
DB_HOST = os.environ.get("DB_HOST", "localhost")
API_KEY = os.environ.get("CART_API_KEY")
EOF_P
  cat > $D/TASKS.txt <<'EOF_P'
LAB 142: a load check and a secrets check. Work in /opt/lab142.
The service runs on http://127.0.0.1:8142  (/health, /cart, /slow).

1. Write load.py. It sends N requests to one path, with W workers at once.
   Options: --path (default /cart)  --n (default 60)  --workers (default 10)
            --budget-p95 MS (optional)
   Use only the python3 standard library (threads + urllib).
2. It writes out/report.json with these keys:
   path, requests, workers, errors, latencies_ms (a list), p95_ms, rps
3. p95_ms is the 95th percentile of latencies_ms (nearest rank).
4. errors counts every request that failed or did not return 200.
5. Exit code 1 if errors > 0, or if --budget-p95 is given and p95_ms is over it.
   Otherwise exit 0.
6. Write scan.sh. "sh scan.sh DIR" exits 1 and prints the file name if any file
   under DIR contains a hard-coded AWS key (AKIA + 16 capitals/digits)
   or a line like password = "..." ; otherwise exits 0.
Then: lab check, until 6 of 6.
EOF_P
  chown -R $OWNER $D 2>/dev/null
  $AS sh -c "nohup python3 $D/server.py >/dev/null 2>&1 & echo \$! > $D/.pid"
  for i in 1 2 3 4 5 6 7 8 9 10; do python3 -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:$PORT/health',timeout=1)" 2>/dev/null && break; sleep 0.5; done
  echo "lab142 ready in $D  (read TASKS.txt)"
}
P=0; T=0
ok() { T=$((T+1)); if [ "$2" = 0 ]; then P=$((P+1)); echo "  PASS  $1"; else echo "  FAIL  $1"; fi; }
check() {
  [ -d $D ] || { echo "run: lab up"; exit 1; }
  cd $D
  rm -f out/report.json
  python3 load.py --path /cart --n 60 --workers 10 >/dev/null 2>&1; rc=$?
  [ -f load.py ] && [ $rc = 0 ] && [ -f out/report.json ]; ok "load.py runs against /cart and writes out/report.json" $?
  python3 - <<'EOF_C' 2>/dev/null; ok "report has the keys, 60 requests, 10 workers, 0 errors" $?
import json
r = json.load(open("out/report.json"))
assert all(k in r for k in "path requests workers errors latencies_ms p95_ms rps".split())
assert r["requests"] == 60 and r["workers"] == 10 and r["errors"] == 0 and len(r["latencies_ms"]) == 60 and r["rps"] > 0
EOF_C
  python3 - <<'EOF_C' 2>/dev/null; ok "p95_ms is the real 95th percentile of latencies_ms" $?
import json, math
r = json.load(open("out/report.json")); L = sorted(r["latencies_ms"])
want = L[math.ceil(0.95 * len(L)) - 1]
assert abs(r["p95_ms"] - want) <= 1.0 and 15 <= r["p95_ms"] <= 400
EOF_C
  python3 load.py --path /nothere --n 10 --workers 2 >/dev/null 2>&1; rc=$?
  python3 -c "import json;r=json.load(open('out/report.json'));assert r['errors']==10" 2>/dev/null; e=$?
  [ $rc != 0 ] && [ $e = 0 ]; ok "404 responses count as errors and fail the run" $?
  python3 load.py --path /cart --budget-p95 400 >/dev/null 2>&1; a=$?
  python3 load.py --path /slow --n 20 --workers 5 --budget-p95 400 >/dev/null 2>&1; b=$?
  [ $a = 0 ] && [ $b != 0 ]; ok "budget gate: /cart passes, /slow fails the p95 budget" $?
  if [ -f scan.sh ]; then
    rm -rf /tmp/l142c; mkdir -p /tmp/l142c; cp -r src /tmp/l142c/clean; cp -r src /tmp/l142c/bad
    printf 'AWS_KEY = "AKIAABCDEFGHIJKLMNOP"\n' > /tmp/l142c/bad/leak.py
    sh scan.sh /tmp/l142c/clean >/dev/null 2>&1; c1=$?
    sh scan.sh /tmp/l142c/bad >/dev/null 2>&1; c2=$?
    printf 'password = "hunter2"\n' > /tmp/l142c/bad/leak.py; sh scan.sh /tmp/l142c/bad >/dev/null 2>&1; c3=$?
    rm -rf /tmp/l142c
    [ $c1 = 0 ] && [ $c2 != 0 ] && [ $c3 != 0 ]
  else false; fi; ok "scan.sh: clean tree passes, planted key and password fail" $?
  echo; echo "$P / $T passed"; [ $P = $T ]
}
status() { [ -d $D ] && echo "lab142 up in $D" || echo "lab142 down"; }
case "$1" in up) up;; check) check;; down) down; echo "lab142 removed";; status) status;; *) echo "usage: lab up|check|down|status";; esac
