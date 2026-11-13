# The frontend service: only the page, on port 8080. It keeps its own diary, web.log.
import time, itertools
from http.server import BaseHTTPRequestHandler, HTTPServer
RID = itertools.count(1)
LOG = open('web.log', 'a', buffering=1)
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        rid = self.headers.get('X-Request-Id') or 'w%04d' % next(RID)
        body = open('index.html').read().replace('window.API', "'http://127.0.0.1:5000'").encode()
        self.send_response(200); self.send_header('Content-Type', 'text/html'); self.send_header('X-Request-Id', rid); self.end_headers(); self.wfile.write(body)
        LOG.write('%s INFO 200 GET %s %s\n' % (time.strftime('%H:%M:%S'), self.path, rid))
    def log_message(self, *a): pass
HTTPServer(('127.0.0.1', 8080), H).serve_forever()
