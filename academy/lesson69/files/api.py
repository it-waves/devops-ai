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
