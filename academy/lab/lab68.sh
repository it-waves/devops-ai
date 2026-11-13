#!/bin/sh
# lab68.sh : REST API lab (MC08-O02). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs python3 and curl. Uses ports 5000 and 8080 on 127.0.0.1.
# Mission: use curl to talk to the CloudCart API: create a product, delete one, and record three status codes.
D=/opt/lab68
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
# The CloudCart backend: a small REST API on port 5000
import json, sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

def db(): return sqlite3.connect('shop.db')
def row(r): return {'id': r[0], 'name': r[1], 'price': r[2]}

class H(BaseHTTPRequestHandler):
    def send(self, code, data=None, extra=None):
        body = b'' if data is None else json.dumps(data).encode() + b'\n'
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        for k, v in (extra or {}).items(): self.send_header(k, v)
        self.end_headers(); self.wfile.write(body)

    def pid(self):
        p = self.path.strip('/').split('/')
        return int(p[2]) if len(p) == 3 and p[:2] == ['api', 'products'] and p[2].isdigit() else None

    def do_GET(self):
        if self.path.rstrip('/') == '/api/products':
            return self.send(200, [row(r) for r in db().execute('SELECT id, name, price FROM products')])
        n = self.pid()
        r = n and db().execute('SELECT id, name, price FROM products WHERE id=?', (n,)).fetchone()
        self.send(200, row(r)) if r else self.send(404, {'error': 'product not found'})

    def do_POST(self):
        if self.path.rstrip('/') != '/api/products': return self.send(404, {'error': 'no such endpoint'})
        try:
            d = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))) or b'{}')
            name, price = d['name'], float(d['price'])
        except (ValueError, KeyError, TypeError):
            return self.send(400, {'error': 'send JSON with name and price'})
        c = db(); cur = c.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price)); c.commit()
        self.send(201, {'id': cur.lastrowid, 'name': name, 'price': price}, {'Location': f'/api/products/{cur.lastrowid}'})

    def do_DELETE(self):
        n = self.pid(); c = db()
        if not n or not c.execute('SELECT 1 FROM products WHERE id=?', (n,)).fetchone(): return self.send(404, {'error': 'product not found'})
        c.execute('DELETE FROM products WHERE id=?', (n,)); c.commit(); self.send(204)

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
  chmod +x $D/start.sh $D/stop.sh
  cd $D && python3 initdb.py && : > answers.txt
  chown -R $U $D
  (cd $D && sudo -u $U nohup ./start.sh > /dev/null 2>&1 &)
  sleep 2
  cat <<MSG
Lab 68 is ready: CloudCart is running in $D (backend API on port 5000, frontend on 8080). Five things need your work, all with curl:
  1. Create a product named Mug with price 9, once, using POST /api/products
  2. Delete the product with id 3 (the Notebook), using DELETE /api/products/3
  3. In $D/answers.txt write the status code the POST returned, as a line like:  created: NNN
  4. Also write the status code for asking for a product that does not exist, like:  missing: NNN
  5. Also write the status code for a POST that is missing the price, like:  bad: NNN
Hint: curl -i shows the status line. Read $D/api.py if you are stuck. Then run: lab check
MSG
}
check() {
  say() { if [ "$1" = ok ]; then echo "PASS  $2"; p=$((p+1)); else echo "FAIL  $2"; fi; }
  p=0
  n=$(curl -s --max-time 3 127.0.0.1:5000/api/products | python3 -c 'import sys,json; print(sum(1 for x in json.load(sys.stdin) if x["name"]=="Mug" and x["price"]==9))' 2>/dev/null)
  [ "$n" = 1 ] && r=ok || r=no; say $r "1 the product list has exactly one Mug, price 9"
  c=$(curl -s -o /dev/null -w '%{http_code}' --max-time 3 127.0.0.1:5000/api/products/3)
  [ "$c" = 404 ] && r=ok || r=no; say $r "2 product 3 (the Notebook) is gone"
  for pair in "created 201 3 the POST status code is recorded" "missing 404 4 the not-found status code is recorded" "bad 400 5 the bad-request status code is recorded"; do
    set -- $pair; k=$1; v=$2; i=$3; shift 3
    grep -q "^$k: *$v *\$" $D/answers.txt 2>/dev/null && r=ok || r=no; say $r "$i answers.txt: $*"
  done
  echo "$p of 5 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab68.sh up|check|down|status";;
esac
