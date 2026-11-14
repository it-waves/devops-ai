import http.server, base64, sys, os, functools
ROOT, USER, PW, PORT = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
tok = 'Basic ' + base64.b64encode(f'{USER}:{PW}'.encode()).decode()
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.headers.get('Authorization') != tok:
            self.send_response(401); self.send_header('WWW-Authenticate', 'Basic realm="corp"'); self.send_header('Content-Length', '0'); self.end_headers(); return
        super().do_GET()
    def do_HEAD(self):
        if self.headers.get('Authorization') != tok:
            self.send_response(401); self.send_header('WWW-Authenticate', 'Basic realm="corp"'); self.send_header('Content-Length', '0'); self.end_headers(); return
        super().do_HEAD()
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), functools.partial(H, directory=ROOT)).serve_forever()
