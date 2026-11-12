#!/usr/bin/env python3
"""api06.py : a tiny inventory REST API for the MC06 Python for DevOps lessons. Standard library only.
Run in your own virtual machine:  python3 api06.py [port]     (default 8081, listens on 127.0.0.1 only)
  GET /servers?page=1&per_page=3   needs header  Authorization: Bearer lab-token-123   -> JSON with a Link-style next page
  GET /flaky                        fails twice with 503, then answers 200 (for retry practice; resets after success)
  GET /slow                         answers after 3 seconds (for timeout practice)
  GET /health                       no auth needed"""
import json, sys, time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
TOKEN = 'lab-token-123'
SERVERS = [{'id': i, 'name': f'web-{i:02d}', 'env': 'prod' if i % 3 else 'staging', 'cpu': 2 * (1 + i % 4), 'state': 'running' if i % 5 else 'stopped'} for i in range(1, 11)]
FLAKY = {'n': 0}
class H(BaseHTTPRequestHandler):
    def send(self, code, obj, extra=None):
        b = json.dumps(obj).encode(); self.send_response(code); self.send_header('Content-Type', 'application/json'); self.send_header('Content-Length', str(len(b)))
        for k, v in (extra or {}).items(): self.send_header(k, v)
        self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        if u.path == '/health': return self.send(200, {'status': 'ok'})
        if u.path == '/flaky':
            FLAKY['n'] += 1
            if FLAKY['n'] <= 2: return self.send(503, {'error': 'try again'}, {'Retry-After': '1'})
            FLAKY['n'] = 0; return self.send(200, {'status': 'recovered'})
        if u.path == '/slow': time.sleep(3); return self.send(200, {'status': 'slow but ok'})
        if u.path == '/servers':
            if self.headers.get('Authorization') != f'Bearer {TOKEN}': return self.send(401, {'error': 'missing or bad token'})
            page = int(q.get('page', ['1'])[0]); per = int(q.get('per_page', ['3'])[0]); chunk = SERVERS[(page - 1) * per: page * per]
            nxt = {'next_page': page + 1} if page * per < len(SERVERS) else {'next_page': None}
            return self.send(200, {'items': chunk, 'page': page, **nxt, 'total': len(SERVERS)})
        self.send(404, {'error': 'not found'})
    def log_message(self, *a): pass
if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8081
    HTTPServer(('127.0.0.1', port), H).serve_forever()
