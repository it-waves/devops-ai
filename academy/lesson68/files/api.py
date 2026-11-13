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
