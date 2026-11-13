#!/bin/sh
# lab75.sh : CloudCart mastery lab (MC08 mastery evidence). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs python3 and curl. Uses ports 5000 and 8080 on 127.0.0.1.
# Mission: CloudCart was released with four faults. Find each fault, fix it with one change, and prove it. lab check says PASS or FAIL for each.
D=/opt/lab75
U=${SUDO_USER:-root}
stopall() { pkill -f "python3 (app|api|web).py" 2>/dev/null; sleep 0.5; true; }
down() { stopall; rm -rf $D; true; }
put() { cat > "$D/$1"; }
up() {
  down; mkdir -p $D
  put initdb.py <<'EOF_initdb.py'
import sqlite3
db = sqlite3.connect('shop.db')
db.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
db.execute('DELETE FROM products')
db.executemany('INSERT INTO products VALUES (?,?,?)', [(1, 'Backpack', 39.0), (2, 'Water bottle', 12.5), (3, 'Notebook', 6.0)])
db.commit()
EOF_initdb.py
  put showdb.py <<'EOF_showdb.py'
import sqlite3
for row in sqlite3.connect('shop.db').execute('SELECT id, name, price FROM products'): print(row)
EOF_showdb.py
  put index.html <<'EOF_index.html'
<!doctype html>
<html><head><meta charset="utf-8"><title>CloudCart</title>
<style>
body{margin:0;font-family:system-ui,Segoe UI,Helvetica,Arial,sans-serif;background:#f4f6f8;color:#1c2733}
header{background:#0f3d4c;color:#fff;padding:22px 40px;font-size:30px;font-weight:700;letter-spacing:.5px}
header span{color:#7fe0c8}
main{padding:34px 40px}
h2{margin:0 0 20px;font-size:24px}
ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
li{background:#fff;border-radius:14px;padding:26px;box-shadow:0 2px 10px rgba(15,61,76,.12);font-size:24px;font-weight:600}
li b{display:block;margin-top:12px;color:#0f7a5a;font-size:28px}
</style></head><body>
<header>Cloud<span>Cart</span></header>
<main><h2>Today's products</h2><ul id="list"></ul></main>
<script>
fetch(window.API + '/api/products').then(r => r.json()).then(items => {
  document.getElementById('list').innerHTML = items.map(p => '<li>' + p.name + '<b>$' + p.price.toFixed(2) + '</b></li>').join('');
});
</script>
</body></html>
EOF_index.html
  put web.py <<'EOF_web.py'
# The frontend service: only the page, on port 8080. It keeps its own diary, web.log.
import time, itertools
from http.server import BaseHTTPRequestHandler, HTTPServer
RID = itertools.count(1)
LOG = open('web.log', 'a', buffering=1)
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        rid = self.headers.get('X-Request-Id') or 'w%04d' % next(RID)
        body = open('index.html').read().replace('window.API', "'http://127.0.0.1:5000'").encode()
        self.send_response(200); self.send_header('Content-Type', 'text/html'); self.send_header('X-Request-Id', rid); self.end_headers(); self.wfile.write(body)
        LOG.write('%s INFO 200 GET %s %s\n' % (time.strftime('%H:%M:%S'), self.path, rid))
    def log_message(self, *a): pass
HTTPServer(('127.0.0.1', 8080), H).serve_forever()
EOF_web.py
  put api.py <<'EOF_api.py'
# The CloudCart backend: REST API, now configured from defaults, app.conf and environment variables (version 3.3: probes, access log, metrics and clean errors)
import json, os, secrets, sqlite3, time, itertools
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

USERS = {'alice': ('ALICE_PW', 'admin'), 'bob': ('BOB_PW', 'customer')}   # passwords come from the environment, never from this file
TOKENS = {}                                                                 # token -> (user, role, expires)

DEFAULTS = {'STORE_NAME': 'CloudCart', 'CURRENCY': 'USD', 'PORT': '5000', 'FLAG_DISCOUNT': 'off', 'STORAGE': 'memory'}
def load_config():
    """Order of power: environment variable beats app.conf beats the default in this file."""
    conf = {}
    if os.path.exists('app.conf'):
        for ln in open('app.conf'):
            ln = ln.strip()
            if ln and not ln.startswith('#') and '=' in ln:
                k, v = ln.split('=', 1); conf[k.strip()] = v.strip()
    out = {}
    for k, d in DEFAULTS.items():
        if k in os.environ: out[k] = (os.environ[k], 'environment')
        elif k in conf: out[k] = (conf[k], 'app.conf')
        else: out[k] = (d, 'default')
    return out
CFG = load_config()
if not CFG['PORT'][0].isdigit():
    print("config error: PORT must be a number, got '%s'" % CFG['PORT'][0], flush=True); raise SystemExit(1)
if CFG['FLAG_DISCOUNT'][0] not in ('on', 'off'):
    print("config error: FLAG_DISCOUNT must be on or off, got '%s'" % CFG['FLAG_DISCOUNT'][0], flush=True); raise SystemExit(1)
if CFG['STORAGE'][0] not in ('memory', 'db'):
    print("config error: STORAGE must be memory or db, got '%s'" % CFG['STORAGE'][0], flush=True); raise SystemExit(1)
DISCOUNT = CFG['FLAG_DISCOUNT'][0] == 'on'
CART = []                                   # used only when STORAGE=memory: it lives and dies with this process
if CFG['STORAGE'][0] == 'db':
    _c = sqlite3.connect('shop.db'); _c.execute('CREATE TABLE IF NOT EXISTS cart (item INTEGER)'); _c.commit(); _c.close()

def db(): return sqlite3.connect('shop.db')

START = time.time()
RID = itertools.count(1)                                 # request numbers, used when the caller sends no X-Request-Id
STATS = {'requests': 0, '2xx': 0, '4xx': 0, '5xx': 0}   # counters only ever go up
LOG = open('api.log', 'a', buffering=1)
PROBES = ('/healthz', '/readyz', '/metrics')            # probes are not customer traffic: not counted, not logged
def log(code, method, path, rid, cause=''):
    level = 'ERROR' if code >= 500 else 'WARN ' if code >= 400 else 'INFO '
    LOG.write('%s %s %d %s %s %s%s\n' % (time.strftime('%H:%M:%S'), level, code, method, path, rid, ' ' + cause if cause else ''))
def row(r): return {'id': r[0], 'name': r[1], 'price': round(r[2] * 0.9, 2) if DISCOUNT else r[2]}

class H(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    server_version = 'CloudCart'
    sys_version = ''

    def send(self, code, data=None, extra=None, text=None, cause=''):
        body = (text.encode() if text is not None else b'' if data is None else json.dumps(data).encode() + b'\n')
        if self.path.split('?')[0] not in PROBES:
            STATS['requests'] += 1; STATS['%dxx' % (code // 100)] = STATS.get('%dxx' % (code // 100), 0) + 1
            log(code, self.command, self.path, self.rid, cause)
        self.send_response(code)
        self.send_header('X-Request-Id', self.rid)
        self.send_header('Content-Type', 'text/plain' if text is not None else 'application/json')
        self.send_header('Content-Length', str(len(body)))
        if code == 401: self.send_header('WWW-Authenticate', 'Bearer')
        for k, v in (extra or {}).items(): self.send_header(k, v)
        self.end_headers()
        if self.command != 'HEAD': self.wfile.write(body)

    def handle_one(self, fn):
        self.rid = self.headers.get('X-Request-Id') or ('probe' if self.path.split('?')[0] in PROBES else 'r%04d' % next(RID))
        try: fn()
        except sqlite3.Error as e:      # a failure below is turned into a clean error above, with the request id and the cause in the log
            self.send(503, {'error': 'database unavailable', 'request_id': self.rid}, cause=str(e))
        except Exception as e:
            self.send(500, {'error': 'internal error', 'request_id': self.rid}, cause=type(e).__name__ + ': ' + str(e))

    def do_GET(self): self.handle_one(self.get)
    def do_POST(self): self.handle_one(self.post)
    def do_DELETE(self): self.handle_one(self.delete)

    def who(self):
        h = self.headers.get('Authorization', '')
        t = TOKENS.get(h[7:]) if h.startswith('Bearer ') else None
        return t if t and t[2] > time.time() else None

    def need(self, role=None):
        u = self.who()
        if not u: self.send(401, {'error': 'login required'}); return None
        if role and u[1] != role: self.send(403, {'error': 'not allowed for your role'}); return None
        return u

    def get(self):
        p = self.path.rstrip('/')
        if p == '/healthz': return self.send(200, {'status': 'ok'})
        if p == '/readyz':
            try: db().execute('SELECT COUNT(*) FROM products').fetchone()
            except sqlite3.Error: return self.send(503, {'status': 'not ready', 'checks': {'database': 'fail'}})
            return self.send(200, {'status': 'ready', 'checks': {'database': 'ok'}})
        if p == '/metrics':
            lines = ['cloudcart_up 1', 'cloudcart_uptime_seconds %d' % (time.time() - START), 'cloudcart_requests_total %d' % STATS['requests']]
            lines += ['cloudcart_responses_%s %d' % (k, STATS[k]) for k in ('2xx', '4xx', '5xx')]
            return self.send(200, text='\n'.join(lines) + '\n')
        if p == '/api/cart': return self.send(200, self.cart())
        if p == '/api/config': return self.send(200, {k.lower(): '%s  (%s)' % v for k, v in CFG.items()})
        if p == '/api/products': return self.send(200, [row(r) for r in db().execute('SELECT id, name, price FROM products')])
        if p == '/api/orders':
            u = self.need()
            if u: self.send(200, {'user': u[0], 'role': u[1], 'orders': [{'id': 101, 'total': 51.5}]})
            return
        parts = p.strip('/').split('/')
        if len(parts) == 3 and parts[:2] == ['api', 'products'] and parts[2].isdigit():
            r = db().execute('SELECT id, name, price FROM products WHERE id=?', (int(parts[2]),)).fetchone()
            return self.send(200, row(r)) if r else self.send(404, {'error': 'not found'})
        self.send(404, {'error': 'not found'})

    def cart(self):
        if CFG['STORAGE'][0] == 'db': items = [r[0] for r in db().execute('SELECT item FROM cart ORDER BY rowid')]
        else: items = list(CART)
        return {'cart': items, 'instance': int(CFG['PORT'][0]), 'storage': CFG['STORAGE'][0]}

    def post(self):
        parts = self.path.strip('/').split('/')
        if len(parts) == 3 and parts[:2] == ['api', 'cart'] and parts[2].isdigit():
            if CFG['STORAGE'][0] == 'db':
                c = db(); c.execute('INSERT INTO cart VALUES (?)', (int(parts[2]),)); c.commit()
            else: CART.append(int(parts[2]))
            return self.send(201, self.cart())
        if self.path.rstrip('/') != '/api/login': return self.send(404, {'error': 'not found'})
        try:
            d = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))) or b'{}')
            env, role = USERS[d['user']]
            ok = os.environ.get(env) and secrets.compare_digest(d['password'], os.environ[env])
        except (ValueError, KeyError, TypeError):
            ok = False
        if not ok: return self.send(401, {'error': 'wrong user or password'})
        tok = secrets.token_hex(8); TOKENS[tok] = (d['user'], role, time.time() + 3600)
        self.send(200, {'token': tok, 'role': role, 'expires_in': 3600})

    def delete(self):
        if not self.need('admin'): return
        parts = self.path.strip('/').split('/')
        c = db()
        if len(parts) == 3 and parts[2].isdigit() and c.execute('SELECT 1 FROM products WHERE id=?', (int(parts[2]),)).fetchone():
            c.execute('DELETE FROM products WHERE id=?', (int(parts[2]),)); c.commit(); return self.send(204)
        self.send(404, {'error': 'not found'})

    def log_message(self, *a): pass

ThreadingHTTPServer(('127.0.0.1', int(CFG['PORT'][0])), H).serve_forever()
EOF_api.py
  put start.sh <<'EOF_start.sh'
#!/bin/sh
# usage: ./start.sh   (loads secrets.env, then starts the API; settings come from app.conf and your environment)
./stop.sh
set -a; . ./secrets.env; set +a
python3 api.py & python3 web.py &
echo "api and web started"
sleep 1
EOF_start.sh
  put layers.sh <<'EOF_layers.sh'
#!/bin/sh
# usage: ./layers.sh   asks each layer for one answer: the web page, then the API data
for p in "web 8080 /" "api 5000 /api/products"; do
  set -- $p
  printf '%-4s %s\n' $1 "$(curl -s -o /dev/null --max-time 3 -w '%{http_code}' localhost:$2$3)"
done
EOF_layers.sh
  put probe.sh <<'EOF_probe.sh'
#!/bin/sh
# usage: ./probe.sh [port]   asks the two probe questions an orchestrator asks: is it alive, is it ready
P=${1:-5000}
for e in healthz readyz; do
  r=$(curl -s -w '\n%{http_code}' localhost:$P/$e)
  printf '%-8s %s  %s\n' $e "$(echo "$r" | tail -1)" "$(echo "$r" | head -1)"
done
EOF_probe.sh
  put app.conf <<'EOF_app.conf'
# CloudCart settings. Environment variables override this file.
STORE_NAME=CloudCart
CURRENCY=USD
PORT=5050
EOF_app.conf
  put stop.sh <<'EOF_stop.sh'
#!/bin/sh
pkill -f "python3 (app|api|web).py" 2>/dev/null; sleep 0.5; exit 0
EOF_stop.sh
  put secrets.env <<'EOF_secrets.env'
ALICE_PW=blue-heron-42
BOB_PW=paper-kite-77
EOF_secrets.env
  chmod +x $D/start.sh $D/stop.sh $D/layers.sh $D/probe.sh; chmod 644 $D/secrets.env
  cd $D && python3 initdb.py && mv shop.db shop.db.off
  chown -R $U $D
  (cd $D && sudo -u $U nohup ./start.sh > /dev/null 2>&1 &)
  sleep 2
  cat <<MSG
Lab 75 is ready in $D. CloudCart was just released and it is broken. There are four faults. Work from inside $D and do not edit api.py or web.py.
Tools you already know: ./layers.sh  ./probe.sh  ss -ltn  curl  ls -l  grep  the logs api.log and web.log
Goal: lab check shows four PASS lines. Keep four notes for every fault: symptom, cause, fix, proof.
Fault 4 needs a saved trace: request the page and then /api/orders (after logging in as alice) with the request ID mc08, then:  grep mc08 web.log api.log > trace.txt
Then run: lab check
MSG
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  p=0
  [ "$(curl -s -o /dev/null --max-time 3 -w '%{http_code}' 127.0.0.1:8080/)" = 200 ] && [ "$(curl -s -o /dev/null --max-time 3 -w '%{http_code}' 127.0.0.1:5000/healthz)" = 200 ] && r=ok || r=no; say $r "1 web page loads and API answers on port 5000"
  curl -s --max-time 3 127.0.0.1:5000/readyz 2>/dev/null | grep -q '"status": "ready"' && r=ok || r=no; say $r "2 shop is ready: readyz says ready"
  [ "$(stat -c %a $D/secrets.env 2>/dev/null)" = 600 ] && grep -q '^ALICE_PW=' $D/secrets.env && r=ok || r=no; say $r "3 secrets.env is private (mode 600)"
  [ -s $D/trace.txt ] && grep -q '^web.log:.*mc08' $D/trace.txt && grep -q '^api.log:.*INFO  200 GET /api/orders mc08' $D/trace.txt && sed 's/^[a-z.]*://' $D/trace.txt | grep -qF -f /dev/stdin $D/web.log $D/api.log 2>/dev/null && r=ok || r=no; say $r "4 trace.txt: request mc08 in web.log and api.log"
  echo "$p of 4 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab75.sh up|check|down|status";;
esac
