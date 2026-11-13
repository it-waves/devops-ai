# The CloudCart backend: REST API, now configured from defaults, app.conf and environment variables (version 3.3: probes, access log, metrics and clean errors)
import json, os, secrets, sqlite3, time, itertools
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

USERS = {'alice': ('ALICE_PW', 'admin'), 'bob': ('BOB_PW', 'customer')}   # passwords come from the environment, never from this file
TOKENS = {}                                                                 # token -> (user, role, expires)

DEFAULTS = {'STORE_NAME': 'CloudCart', 'CURRENCY': 'USD', 'PORT': '5000', 'FLAG_DISCOUNT': 'off', 'STORAGE': 'memory'}
def load_config():
    """Order of power: environment variable beats app.conf beats the default in this file."""
    conf = {}
    if os.path.exists('app.conf'):
        for ln in open('app.conf'):
            ln = ln.strip()
            if ln and not ln.startswith('#') and '=' in ln:
                k, v = ln.split('=', 1); conf[k.strip()] = v.strip()
    out = {}
    for k, d in DEFAULTS.items():
        if k in os.environ: out[k] = (os.environ[k], 'environment')
        elif k in conf: out[k] = (conf[k], 'app.conf')
        else: out[k] = (d, 'default')
    return out
CFG = load_config()
if not CFG['PORT'][0].isdigit():
    print("config error: PORT must be a number, got '%s'" % CFG['PORT'][0], flush=True); raise SystemExit(1)
if CFG['FLAG_DISCOUNT'][0] not in ('on', 'off'):
    print("config error: FLAG_DISCOUNT must be on or off, got '%s'" % CFG['FLAG_DISCOUNT'][0], flush=True); raise SystemExit(1)
if CFG['STORAGE'][0] not in ('memory', 'db'):
    print("config error: STORAGE must be memory or db, got '%s'" % CFG['STORAGE'][0], flush=True); raise SystemExit(1)
DISCOUNT = CFG['FLAG_DISCOUNT'][0] == 'on'
CART = []                                   # used only when STORAGE=memory: it lives and dies with this process
if CFG['STORAGE'][0] == 'db':
    _c = sqlite3.connect('shop.db'); _c.execute('CREATE TABLE IF NOT EXISTS cart (item INTEGER)'); _c.commit(); _c.close()

def db(): return sqlite3.connect('shop.db')

START = time.time()
RID = itertools.count(1)                                 # request numbers, used when the caller sends no X-Request-Id
STATS = {'requests': 0, '2xx': 0, '4xx': 0, '5xx': 0}   # counters only ever go up
LOG = open('api.log', 'a', buffering=1)
PROBES = ('/healthz', '/readyz', '/metrics')            # probes are not customer traffic: not counted, not logged
def log(code, method, path, rid, cause=''):
    level = 'ERROR' if code >= 500 else 'WARN ' if code >= 400 else 'INFO '
    LOG.write('%s %s %d %s %s %s%s\n' % (time.strftime('%H:%M:%S'), level, code, method, path, rid, ' ' + cause if cause else ''))
def row(r): return {'id': r[0], 'name': r[1], 'price': round(r[2] * 0.9, 2) if DISCOUNT else r[2]}

class H(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    server_version = 'CloudCart'
    sys_version = ''

    def send(self, code, data=None, extra=None, text=None, cause=''):
        body = (text.encode() if text is not None else b'' if data is None else json.dumps(data).encode() + b'\n')
        if self.path.split('?')[0] not in PROBES:
            STATS['requests'] += 1; STATS['%dxx' % (code // 100)] = STATS.get('%dxx' % (code // 100), 0) + 1
            log(code, self.command, self.path, self.rid, cause)
        self.send_response(code)
        self.send_header('X-Request-Id', self.rid)
        self.send_header('Content-Type', 'text/plain' if text is not None else 'application/json')
        self.send_header('Content-Length', str(len(body)))
        if code == 401: self.send_header('WWW-Authenticate', 'Bearer')
        for k, v in (extra or {}).items(): self.send_header(k, v)
        self.end_headers()
        if self.command != 'HEAD': self.wfile.write(body)

    def handle_one(self, fn):
        self.rid = self.headers.get('X-Request-Id') or ('probe' if self.path.split('?')[0] in PROBES else 'r%04d' % next(RID))
        try: fn()
        except sqlite3.Error as e:      # a failure below is turned into a clean error above, with the request id and the cause in the log
            self.send(503, {'error': 'database unavailable', 'request_id': self.rid}, cause=str(e))
        except Exception as e:
            self.send(500, {'error': 'internal error', 'request_id': self.rid}, cause=type(e).__name__ + ': ' + str(e))

    def do_GET(self): self.handle_one(self.get)
    def do_POST(self): self.handle_one(self.post)
    def do_DELETE(self): self.handle_one(self.delete)

    def who(self):
        h = self.headers.get('Authorization', '')
        t = TOKENS.get(h[7:]) if h.startswith('Bearer ') else None
        return t if t and t[2] > time.time() else None

    def need(self, role=None):
        u = self.who()
        if not u: self.send(401, {'error': 'login required'}); return None
        if role and u[1] != role: self.send(403, {'error': 'not allowed for your role'}); return None
        return u

    def get(self):
        p = self.path.rstrip('/')
        if p == '/healthz': return self.send(200, {'status': 'ok'})
        if p == '/readyz':
            try: db().execute('SELECT COUNT(*) FROM products').fetchone()
            except sqlite3.Error: return self.send(503, {'status': 'not ready', 'checks': {'database': 'fail'}})
            return self.send(200, {'status': 'ready', 'checks': {'database': 'ok'}})
        if p == '/metrics':
            lines = ['cloudcart_up 1', 'cloudcart_uptime_seconds %d' % (time.time() - START), 'cloudcart_requests_total %d' % STATS['requests']]
            lines += ['cloudcart_responses_%s %d' % (k, STATS[k]) for k in ('2xx', '4xx', '5xx')]
            return self.send(200, text='\n'.join(lines) + '\n')
        if p == '/api/cart': return self.send(200, self.cart())
        if p == '/api/config': return self.send(200, {k.lower(): '%s  (%s)' % v for k, v in CFG.items()})
        if p == '/api/products': return self.send(200, [row(r) for r in db().execute('SELECT id, name, price FROM products')])
        if p == '/api/orders':
            u = self.need()
            if u: self.send(200, {'user': u[0], 'role': u[1], 'orders': [{'id': 101, 'total': 51.5}]})
            return
        parts = p.strip('/').split('/')
        if len(parts) == 3 and parts[:2] == ['api', 'products'] and parts[2].isdigit():
            r = db().execute('SELECT id, name, price FROM products WHERE id=?', (int(parts[2]),)).fetchone()
            return self.send(200, row(r)) if r else self.send(404, {'error': 'not found'})
        self.send(404, {'error': 'not found'})

    def cart(self):
        if CFG['STORAGE'][0] == 'db': items = [r[0] for r in db().execute('SELECT item FROM cart ORDER BY rowid')]
        else: items = list(CART)
        return {'cart': items, 'instance': int(CFG['PORT'][0]), 'storage': CFG['STORAGE'][0]}

    def post(self):
        parts = self.path.strip('/').split('/')
        if len(parts) == 3 and parts[:2] == ['api', 'cart'] and parts[2].isdigit():
            if CFG['STORAGE'][0] == 'db':
                c = db(); c.execute('INSERT INTO cart VALUES (?)', (int(parts[2]),)); c.commit()
            else: CART.append(int(parts[2]))
            return self.send(201, self.cart())
        if self.path.rstrip('/') != '/api/login': return self.send(404, {'error': 'not found'})
        try:
            d = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))) or b'{}')
            env, role = USERS[d['user']]
            ok = os.environ.get(env) and secrets.compare_digest(d['password'], os.environ[env])
        except (ValueError, KeyError, TypeError):
            ok = False
        if not ok: return self.send(401, {'error': 'wrong user or password'})
        tok = secrets.token_hex(8); TOKENS[tok] = (d['user'], role, time.time() + 3600)
        self.send(200, {'token': tok, 'role': role, 'expires_in': 3600})

    def delete(self):
        if not self.need('admin'): return
        parts = self.path.strip('/').split('/')
        c = db()
        if len(parts) == 3 and parts[2].isdigit() and c.execute('SELECT 1 FROM products WHERE id=?', (int(parts[2]),)).fetchone():
            c.execute('DELETE FROM products WHERE id=?', (int(parts[2]),)); c.commit(); return self.send(204)
        self.send(404, {'error': 'not found'})

    def log_message(self, *a): pass

ThreadingHTTPServer(('127.0.0.1', int(CFG['PORT'][0])), H).serve_forever()
