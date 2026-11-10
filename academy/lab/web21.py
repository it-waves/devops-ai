import http.server, ssl, sys
class H(http.server.BaseHTTPRequestHandler):
    server_version = 'lab/1.0'; sys_version = ''; protocol_version = 'HTTP/1.1'
    def log_message(self, *a): pass
    def _send(self, code, body, extra=()):
        b = body.encode(); self.send_response(code); self.send_header('Content-Type', 'text/plain'); self.send_header('Content-Length', str(len(b)))
        for k, v in extra: self.send_header(k, v)
        self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        p = self.path
        if p == '/': self._send(200, 'hello from the lab\n')
        elif p == '/old': self._send(301, '', [('Location', '/')])
        elif p == '/boom': self._send(500, 'server error\n')
        else: self._send(404, 'not found\n')
    do_HEAD = do_GET
    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0)); d = self.rfile.read(n).decode(); self._send(201, 'created ' + d + '\n')
port = int(sys.argv[1]); s = http.server.HTTPServer(('10.0.2.2', port), H)
if len(sys.argv) > 2:
    c = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER); c.load_cert_chain('/opt/lab19/cert.pem', '/opt/lab19/key.pem'); s.socket = c.wrap_socket(s.socket, server_side=True)
s.serve_forever()
