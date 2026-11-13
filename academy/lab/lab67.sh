#!/bin/sh
# lab67.sh : Application architecture lab (MC08-O01). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs python3 and curl. Uses ports 8080 and 5000 on 127.0.0.1.
# Mission: split the CloudCart monolith into a frontend and a backend service, then four checks say PASS.
D=/opt/lab67
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
<html><body>
<h1>CloudCart</h1>
<ul id="list"></ul>
<script>
fetch(window.API + '/api/products').then(r => r.json()).then(items => {
  document.getElementById('list').innerHTML = items.map(p => '<li>' + p.name + ' $' + p.price + '</li>').join('');
});
</script>
</body></html>
EOF_index.html
  put app.py <<'EOF_app.py'
# The monolith: page, logic and database access in ONE process
import json, sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/products':
            rows = sqlite3.connect('shop.db').execute('SELECT id, name, price FROM products').fetchall()
            body, kind = json.dumps([{'id': i, 'name': n, 'price': p} for i, n, p in rows]).encode(), 'application/json'
        else:
            body, kind = open('index.html').read().replace('window.API', "''").encode(), 'text/html'
        self.send_response(200); self.send_header('Content-Type', kind); self.end_headers(); self.wfile.write(body)
    def log_message(self, *a): pass
HTTPServer(('127.0.0.1', 8080), H).serve_forever()
EOF_app.py
  put api.py <<'EOF_api.py'
# The backend service: only data, as JSON, on port 5000
import json, sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        rows = sqlite3.connect('shop.db').execute('SELECT id, name, price FROM products').fetchall()
        body = json.dumps([{'id': i, 'name': n, 'price': p} for i, n, p in rows]).encode()
        self.send_response(200); self.send_header('Content-Type', 'application/json'); self.send_header('Access-Control-Allow-Origin', '*'); self.end_headers(); self.wfile.write(body)
    def log_message(self, *a): pass
HTTPServer(('127.0.0.1', 5000), H).serve_forever()
EOF_api.py
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
  put start.sh <<'EOF_start.sh'
#!/bin/sh
# usage: ./start.sh mono | split
./stop.sh
case "$1" in
  mono)  python3 app.py & echo "monolith started" ;;
  split) python3 api.py & python3 web.py & echo "api and web started" ;;
  *) echo "usage: ./start.sh mono|split" ;;
esac
sleep 1
EOF_start.sh
  put stop.sh <<'EOF_stop.sh'
#!/bin/sh
pkill -f "python3 (app|api|web).py" 2>/dev/null; sleep 0.5; exit 0
EOF_stop.sh
  chmod +x $D/start.sh $D/stop.sh
  cd $D && python3 initdb.py && : > answers.txt
  chown -R $U $D
  (cd $D && sudo -u $U nohup python3 app.py > /dev/null 2>&1 &)
  sleep 1
  cat <<MSG
Lab 67 is ready: the app is in $D and CloudCart is running as ONE process (a monolith) on port 8080. Four things need your work:
  1. A backend service must answer on port 5000 with the product list as JSON (try: curl 127.0.0.1:5000/api/products)
  2. A separate frontend service must serve the page on port 8080, and the page must call the backend on port 5000
  3. Frontend and backend must be different processes
  4. In $D/answers.txt write one line: db: api   (or db: web), naming the service that talks to the database
Hint: cd $D and read start.sh. Then run: lab check
MSG
}
listen_pid() { ss -ltnpH "sport = :$1" 2>/dev/null | sed -n 's/.*pid=\([0-9]*\).*/\1/p' | head -1; }
check() {
  p=0
  if curl -s --max-time 3 127.0.0.1:5000/api/products | python3 -c 'import sys,json; d=json.load(sys.stdin); assert len(d)==3 and d[0]["name"]' 2>/dev/null; then echo "PASS  1 the backend answers on port 5000 with the product list as JSON"; p=$((p+1)); else echo "FAIL  1 the backend answers on port 5000 with the product list as JSON"; fi
  page=$(curl -s --max-time 3 127.0.0.1:8080/)
  if echo "$page" | grep -q CloudCart && echo "$page" | grep -q 127.0.0.1:5000; then echo "PASS  2 the frontend on port 8080 serves a page that calls the backend on port 5000"; p=$((p+1)); else echo "FAIL  2 the frontend on port 8080 serves a page that calls the backend on port 5000"; fi
  a=$(listen_pid 5000); b=$(listen_pid 8080)
  if [ -n "$a" ] && [ -n "$b" ] && [ "$a" != "$b" ]; then echo "PASS  3 frontend and backend are different processes"; p=$((p+1)); else echo "FAIL  3 frontend and backend are different processes"; fi
  if grep -qi '^db: *api\(\.py\)\? *$' $D/answers.txt 2>/dev/null; then echo "PASS  4 answers.txt names the service that talks to the database"; p=$((p+1)); else echo "FAIL  4 answers.txt names the service that talks to the database"; fi
  echo "$p of 4 pass"
}
case "$1" in
  up) up;; check) check;; down) down; echo "lab removed";; status) ls $D 2>/dev/null || echo "not installed";;
  *) echo "usage: lab67.sh up|check|down|status";;
esac
