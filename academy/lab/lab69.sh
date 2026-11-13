#!/bin/sh
# lab69.sh : API testing lab (MC08-O03). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs python3 and curl. Uses ports 5000 and 8080 on 127.0.0.1.
# Mission: use curl to inspect and test the CloudCart API: headers, CSV, timing, exit codes and a request ID.
D=/opt/lab69
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
# The CloudCart backend: a small REST API on port 5000 (version 2.3)
import json, sqlite3, time, uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

def db(): return sqlite3.connect('shop.db')
def row(r): return {'id': r[0], 'name': r[1], 'price': r[2]}

class H(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    server_version = 'CloudCart'
    sys_version = ''
    def send(self, code, data=None, extra=None, raw=None, ctype='application/json'):
        body = raw if raw is not None else (b'' if data is None else json.dumps(data).encode() + b'\n')
        self.code = code
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('X-API-Version', '2.3')
        self.send_header('X-Request-Id', self.rid)
        self.send_header('Access-Control-Allow-Origin', '*')
        for k, v in (extra or {}).items(): self.send_header(k, v)
        self.end_headers()
        if self.command != 'HEAD': self.wfile.write(body)

    def start(self):
        self.t0 = time.time(); self.rid = self.headers.get('X-Request-Id') or uuid.uuid4().hex[:8]

    def done(self):
        with open('api.log', 'a') as f:
            f.write('%s %s %s %dms id=%s\n' % (self.command, self.path, self.code, (time.time() - self.t0) * 1000, self.rid))

    def pid(self):
        p = self.path.strip('/').split('/')
        return int(p[2]) if len(p) == 3 and p[:2] == ['api', 'products'] and p[2].isdigit() else None

    def get(self):
        path = self.path.split('?')[0].rstrip('/')
        if path == '/api/products':
            rows = [row(r) for r in db().execute('SELECT id, name, price FROM products')]
            if 'text/csv' in self.headers.get('Accept', ''):
                csv = 'id,name,price\n' + ''.join('%d,%s,%s\n' % (r['id'], r['name'], r['price']) for r in rows)
                return self.send(200, raw=csv.encode(), ctype='text/csv')
            return self.send(200, rows)
        if path == '/api/fast': return self.send(200, {'status': 'ok'})
        if path == '/api/report':
            time.sleep(0.9); return self.send(200, {'report': 'sales', 'rows': 3})
        n = self.pid()
        r = n and db().execute('SELECT id, name, price FROM products WHERE id=?', (n,)).fetchone()
        self.send(200, row(r)) if r else self.send(404, {'error': 'not found'})

    def do_GET(self): self.start(); self.get(); self.done()
    def do_HEAD(self): self.start(); self.get(); self.done()

    def do_POST(self):
        self.start()
        if self.path.rstrip('/') != '/api/products': self.send(404, {'error': 'no such endpoint'}); return self.done()
        try:
            d = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))) or b'{}')
            name, price = d['name'], float(d['price'])
        except (ValueError, KeyError, TypeError):
            self.send(400, {'error': 'send JSON with name and price'}); return self.done()
        c = db(); cur = c.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price)); c.commit()
        self.send(201, {'id': cur.lastrowid, 'name': name, 'price': price}, {'Location': f'/api/products/{cur.lastrowid}'}); self.done()

    def log_message(self, *a): pass

ThreadingHTTPServer(('127.0.0.1', 5000), H).serve_forever()
EOF_api.py
  put start.sh <<'EOF_start.sh'
#!/bin/sh
# usage: ./start.sh   (starts the backend on 5000 and the frontend on 8080)
./stop.sh
python3 api.py & python3 web.py &
echo "api and web started"
sleep 1
EOF_start.sh
  put stop.sh <<'EOF_stop.sh'
#!/bin/sh
pkill -f "python3 (app|api|web).py" 2>/dev/null; sleep 0.5; exit 0
EOF_stop.sh
  put codes.sh <<'EOF_codes.sh'
#!/bin/sh
# a tiny API client: print the status code of each endpoint
for p in /api/products /api/products/1 /api/products/99 /api/fast; do
  printf '%s  %s\n' "$(curl -s -o /dev/null -w '%{http_code}' localhost:5000$p)" "$p"
done
EOF_codes.sh
  chmod +x $D/start.sh $D/stop.sh $D/codes.sh
  cd $D && python3 initdb.py && : > answers.txt
  chown -R $U $D
  (cd $D && sudo -u $U nohup ./start.sh > /dev/null 2>&1 &)
  sleep 2
  cat <<MSG
Lab 69 is ready: CloudCart is running in $D (API on port 5000). Five things need your work, all with curl, from inside $D:
  1. Read the API version from a response header (curl -I) and write it in answers.txt as a line like:  version: X.Y
  2. Ask for the product list as CSV, using the Accept header, and save it to products.csv
  3. Time /api/fast and /api/report with curl -w, then write the slower one in answers.txt as:  slow: /api/...
  4. Write smoke.sh: it takes an optional URL (default http://127.0.0.1:5000/api/products), exits 0 when the answer is a success, and exits non-zero otherwise
  5. Send any request with the header  X-Request-Id: lab69-trace  so the API logs it in api.log
Hint: curl -sf URL fails with exit code 22 on a 4xx or 5xx. Then run: lab check
MSG
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  p=0
  grep -q "^version: *2\.3 *\$" $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "1 answers.txt: the API version from the header"
  { [ "$(sed -n 1p $D/products.csv 2>/dev/null)" = "id,name,price" ] && [ "$(grep -c Backpack $D/products.csv)" = 1 ]; } 2>/dev/null && r=ok || r=no; say $r "2 products.csv holds the CSV export"
  grep -q "^slow: */api/report *\$" $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "3 answers.txt: the slow endpoint"
  if [ -f $D/smoke.sh ] && sh $D/smoke.sh >/dev/null 2>&1 && ! sh $D/smoke.sh http://127.0.0.1:5000/api/products/99 >/dev/null 2>&1 && ! sh $D/smoke.sh http://127.0.0.1:5999/api/products >/dev/null 2>&1; then r=ok; else r=no; fi; say $r "4 smoke.sh passes on success and fails on 404 and on no server"
  grep -q "id=lab69-trace" $D/api.log 2>/dev/null && r=ok || r=no; say $r "5 api.log shows your request ID"
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab69.sh up|check|down|status";;
esac
