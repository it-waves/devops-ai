import http.server, ssl, sys
class H(http.server.BaseHTTPRequestHandler):
    server_version = 'lab/1.0'; sys_version = ''; protocol_version = 'HTTP/1.1'
    def log_message(self, *a): pass
    def do_GET(self):
        b = b'cart service OK\n'; self.send_response(200); self.send_header('Content-Type', 'text/plain'); self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)
    do_HEAD = do_GET
port = int(sys.argv[1]); s = http.server.HTTPServer(('10.0.2.2', port), H)
if len(sys.argv) > 3:
    c = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER); c.load_cert_chain(sys.argv[2], sys.argv[3]); s.socket = c.wrap_socket(s.socket, server_side=True)
s.serve_forever()
