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
