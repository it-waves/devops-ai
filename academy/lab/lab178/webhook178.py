import http.server, json, time
class H(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        b = self.rfile.read(int(self.headers.get('Content-Length', 0))).decode()
        try: t = json.loads(b)['text']
        except Exception: t = b
        open('/tmp/chat178.log', 'a').write(time.strftime('%H:%M:%S') + '  #deploys  ' + t + '\n')
        self.send_response(200); self.end_headers(); self.wfile.write(b'ok')
    def log_message(self, *a): pass
http.server.HTTPServer(('127.0.0.1', 9300), H).serve_forever()
