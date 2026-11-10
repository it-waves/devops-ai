import http.server, sys
class H(http.server.BaseHTTPRequestHandler):
    server_version = 'lab/1.0'; sys_version = ''; protocol_version = 'HTTP/1.1'
    def log_message(self, *a): pass
    def do_GET(self):
        b = (sys.argv[2] + '\n').encode(); self.send_response(200); self.send_header('Content-Type', 'text/plain'); self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)
http.server.HTTPServer(('10.0.2.2', int(sys.argv[1])), H).serve_forever()
