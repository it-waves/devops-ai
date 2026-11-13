#!/bin/sh
# lab70.sh : Authentication lab (MC08-O04). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs python3 and curl. Uses ports 5000 and 8080 on 127.0.0.1.
# Mission: log in, use a token, meet 401 and 403, act as an admin, and protect a secrets file.
D=/opt/lab70
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
# The frontend service: only the page, on port 8080
from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = open('index.html').read().replace('window.API', "'http://127.0.0.1:5000'").encode()
        self.send_response(200); self.send_header('Content-Type', 'text/html'); self.end_headers(); self.wfile.write(body)
    def log_message(self, *a): pass
HTTPServer(('127.0.0.1', 8080), H).serve_forever()
EOF_web.py
  put api.py <<'EOF_api.py'
# The CloudCart backend: REST API on port 5000, now with login, tokens and roles (version 3.0)
import json, os, secrets, sqlite3, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

USERS = {'alice': ('ALICE_PW', 'admin'), 'bob': ('BOB_PW', 'customer')}   # passwords come from the environment, never from this file
TOKENS = {}                                                                 # token -> (user, role, expires)

def db(): return sqlite3.connect('shop.db')
def row(r): return {'id': r[0], 'name': r[1], 'price': r[2]}

class H(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    server_version = 'CloudCart'
    sys_version = ''

    def send(self, code, data=None, extra=None):
        body = b'' if data is None else json.dumps(data).encode() + b'\n'
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        if code == 401: self.send_header('WWW-Authenticate', 'Bearer')
        for k, v in (extra or {}).items(): self.send_header(k, v)
        self.end_headers()
        if self.command != 'HEAD': self.wfile.write(body)

    def who(self):
        h = self.headers.get('Authorization', '')
        t = TOKENS.get(h[7:]) if h.startswith('Bearer ') else None
        return t if t and t[2] > time.time() else None

    def need(self, role=None):
        u = self.who()
        if not u: self.send(401, {'error': 'login required'}); return None
        if role and u[1] != role: self.send(403, {'error': 'not allowed for your role'}); return None
        return u

    def do_GET(self):
        p = self.path.rstrip('/')
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

    def do_POST(self):
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

    def do_DELETE(self):
        if not self.need('admin'): return
        parts = self.path.strip('/').split('/')
        c = db()
        if len(parts) == 3 and parts[2].isdigit() and c.execute('SELECT 1 FROM products WHERE id=?', (int(parts[2]),)).fetchone():
            c.execute('DELETE FROM products WHERE id=?', (int(parts[2]),)); c.commit(); return self.send(204)
        self.send(404, {'error': 'not found'})

    def log_message(self, *a): pass

ThreadingHTTPServer(('127.0.0.1', 5000), H).serve_forever()
EOF_api.py
  put start.sh <<'EOF_start.sh'
#!/bin/sh
# usage: ./start.sh   (loads secrets.env into the environment, then starts the API on 5000)
./stop.sh
set -a; . ./secrets.env; set +a
python3 api.py & python3 web.py &
echo "api and web started"
sleep 1
EOF_start.sh
  put stop.sh <<'EOF_stop.sh'
#!/bin/sh
pkill -f "python3 (app|api|web).py" 2>/dev/null; sleep 0.5; exit 0
EOF_stop.sh
  put secrets.env <<'EOF_secrets.env'
ALICE_PW=blue-heron-42
BOB_PW=paper-kite-77
EOF_secrets.env
  chmod +x $D/start.sh $D/stop.sh; chmod 644 $D/secrets.env
  cd $D && python3 initdb.py && : > answers.txt
  chown -R $U $D
  (cd $D && sudo -u $U nohup ./start.sh > /dev/null 2>&1 &)
  sleep 2
  cat <<MSG
Lab 70 is ready: CloudCart is running in $D with login, tokens and roles. Bob is a customer and his password is paper-kite-77. Alice is the admin: her password is in secrets.env. Five things need your work, all with curl, from inside $D:
  1. Log in as bob (POST /api/login) and save his token, on its own, in token.txt
  2. GET /api/orders with no token, and write the status code in answers.txt as:  nologin: NNN
  3. As bob, try DELETE /api/products/1, and write the status code as:  forbidden: NNN
  4. Log in as alice and use her token to DELETE /api/products/3
  5. secrets.env is readable by everyone. Make it private to its owner (mode 600)
Hint: curl -H "Authorization: Bearer TOKEN"  and  jq -r .token. Then run: lab check
MSG
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  p=0
  t=$(cat $D/token.txt 2>/dev/null | tr -d ' \n')
  curl -s --max-time 3 -H "Authorization: Bearer $t" 127.0.0.1:5000/api/orders | grep -q '"user": "bob"' && r=ok || r=no; say $r "1 token.txt holds a valid token for bob"
  grep -q "^nologin: *401 *\$" $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "2 answers.txt: the status code without a token"
  { grep -q "^forbidden: *403 *\$" $D/answers.txt 2>/dev/null && [ "$(curl -s -o /dev/null -w '%{http_code}' --max-time 3 127.0.0.1:5000/api/products/1)" = 200 ]; } && r=ok || r=no; say $r "3 answers.txt: the 403 for bob, and product 1 is still there"
  [ "$(curl -s -o /dev/null -w '%{http_code}' --max-time 3 127.0.0.1:5000/api/products/3)" = 404 ] && r=ok || r=no; say $r "4 alice deleted product 3"
  [ "$(stat -c %a $D/secrets.env 2>/dev/null)" = 600 ] && r=ok || r=no; say $r "5 secrets.env is private (mode 600)"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab70.sh up|check|down|status";;
esac
