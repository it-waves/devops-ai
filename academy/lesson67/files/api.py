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
