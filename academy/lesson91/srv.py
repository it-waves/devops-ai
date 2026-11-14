import http.server, base64, sys, os, functools
ROOT, USER, PW, PORT = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
tok = 'Basic ' + base64.b64encode((USER + ':' + PW).encode()).decode()
class H(http.server.SimpleHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    def _ok(self):
        if self.headers.get('Authorization') == tok: return True
        self.send_response(401); self.send_header('WWW-Authenticate', 'Basic realm="corp"'); self.send_header('Content-Length', '0'); self.end_headers(); return False
    def do_GET(self):
        if self._ok(): super().do_GET()
    def do_HEAD(self):
        if self._ok(): super().do_HEAD()
    def do_PUT(self):
        n = int(self.headers.get('Content-Length', 0)); data = self.rfile.read(n)
        if not self._ok(): return
        p = self.translate_path(self.path); rel = self.path.lstrip('/')
        base = os.path.basename(p)
        if rel.startswith('releases/') and os.path.exists(p) and not base.startswith('maven-metadata'):
            self.send_response(409); self.send_header('Content-Length', '0'); self.end_headers(); return
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'wb').write(data)
        self.send_response(201); self.send_header('Content-Length', '0'); self.end_headers()
    def log_message(self, *a): pass
os.makedirs(os.path.join(ROOT, 'releases'), exist_ok=True); os.makedirs(os.path.join(ROOT, 'snapshots'), exist_ok=True)
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), functools.partial(H, directory=ROOT)).serve_forever()
