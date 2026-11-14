import http.server, base64, sys, os, functools, json, time, hashlib, html, threading, re, shutil
from urllib.parse import urlparse, parse_qs, quote, unquote
ROOT, USER, PW, PORT = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
tok = 'Basic ' + base64.b64encode((USER + ':' + PW).encode()).decode()
SID = hashlib.sha256((USER + PW + 'sid').encode()).hexdigest()[:24]
EVF = os.path.join(ROOT, '.events.json'); RPF = os.path.join(ROOT, '.repos.json'); LOCK = threading.Lock()
def _load(f):
    try: return json.load(open(f))
    except Exception: return []
def events(): return _load(EVF)
def repos(): return _load(RPF)
def repo_of(name): return next((r for r in repos() if r['name'] == name), None)
def log_event(repo, path, status, note):
    base = os.path.basename(path)
    if base.endswith(('.sha1', '.md5', '.sha256', '.sha512', '.asc')) or base.startswith('maven-metadata'): return
    with LOCK:
        ev = events(); ev.append({'id': 'E%04d' % (len(ev) + 1), 'time': time.strftime('%H:%M:%S'), 'user': USER, 'repo': repo, 'file': base, 'status': status, 'note': note})
        json.dump(ev, open(EVF, 'w'))
CSS = '''body{margin:0;background:#0b1a1e;color:#e4f0f1;font:21px/1.35 "DejaVu Sans",sans-serif}
.top{background:#12303a;padding:14px 28px;display:flex;gap:28px;align-items:center;border-bottom:3px solid #7fe0d0}
.top b{font-size:26px;color:#7fe0d0}.top a{color:#e4f0f1;text-decoration:none;padding:6px 14px;border-radius:8px}.top a.on{background:#1e4a55}
.top span{margin-left:auto;color:#9fb8bc;font-size:19px}.top span.tag{margin-left:0}.tag{background:#f2c46d;color:#10242a;border-radius:8px;padding:2px 12px;font-size:18px;font-weight:bold}
.wrap{padding:16px 28px}h1{margin:0 0 8px;font-size:30px}
.card{display:inline-block;vertical-align:top;width:410px;background:#12303a;border:2px solid #2d6a78;border-radius:14px;padding:14px 22px;margin:0 22px 18px 0}
.card h2{margin:4px 0 4px;font-size:28px}.card a{color:#7fe0d0}
.pill{display:inline-block;border-radius:8px;padding:2px 12px;font-size:18px;font-weight:bold;color:#10242a}.snap{background:#f2c46d}.rel{background:#7fe0d0}.bad{background:#ff8a80}
table{border-collapse:collapse;width:100%}th{text-align:left;color:#9fb8bc;font-weight:normal;border-bottom:2px solid #2d6a78;padding:6px 10px}td{padding:8px 10px;border-bottom:1px solid #1e4a55}
a{color:#7fe0d0}.mono{font-family:"DejaVu Sans Mono",monospace;font-size:18px}.red td{color:#ff8a80;font-weight:bold}.mut{color:#9fb8bc}
input[type=text],input[type=password]{font:22px "DejaVu Sans",sans-serif;padding:10px;width:420px;border-radius:8px;border:2px solid #2d6a78;background:#0b1a1e;color:#e4f0f1;margin:6px 0 12px}
label.r{display:block;margin:2px 0;font-size:22px}input[type=radio]{width:22px;height:22px;vertical-align:middle;margin-right:10px}
button,.btn{font:bold 22px "DejaVu Sans",sans-serif;background:#7fe0d0;color:#10242a;border:0;border-radius:8px;padding:10px 28px;text-decoration:none;display:inline-block;cursor:pointer}a.btn{color:#10242a}
pre{background:#12303a;border:2px solid #2d6a78;border-radius:10px;padding:10px 16px;font:17px/1.3 "DejaVu Sans Mono",monospace;margin:8px 0}'''
def page(title, body, nav='', login=False):
    n = lambda k, t, h: '<a class="%s" href="%s">%s</a>' % ('on' if nav == k else '', h, t)
    top = '<b>Corp Repository</b><span class=tag>STAND-IN</span>' + ('' if login else n('b', 'Browse', '/ui') + n('e', 'Events', '/ui/events') + '<span>signed in as %s</span>' % USER)
    return ('<!doctype html><meta charset=utf-8><title>%s</title><style>%s</style><div class=top>%s</div><div class=wrap>%s</div>' % (html.escape(title), CSS, top, body)).encode()
def scan(repo):
    out = {}; base = os.path.join(ROOT, repo)
    for d, _, fs in os.walk(base):
        rel = os.path.relpath(d, base).split(os.sep)
        if len(rel) < 3 or rel == ['.']: continue
        if not [f for f in fs if f.endswith(('.jar', '.pom'))]: continue
        out.setdefault('/'.join(rel[:-2]) + ':' + rel[-2], {})[rel[-1]] = sorted(fs)
    return out
def sha1(p): return hashlib.sha1(open(p, 'rb').read()).hexdigest()
def addr(name): return 'http://localhost:%d/repository/%s' % (PORT, name)
class H(http.server.SimpleHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    def _ok(self):
        if self.headers.get('Authorization') == tok: return True
        self.send_response(401); self.send_header('WWW-Authenticate', 'Basic realm="corp"'); self.send_header('Content-Length', '0'); self.end_headers(); return False
    def _send(self, code, body, ctype='text/html; charset=utf-8', extra=()):
        self.send_response(code); self.send_header('Content-Type', ctype); self.send_header('Content-Length', str(len(body)))
        for k, v in extra: self.send_header(k, v)
        self.end_headers(); self.wfile.write(body)
    def _redir(self, to, extra=()): self._send(302, b'', extra=(('Location', to),) + tuple(extra))
    def _ui_ok(self): return ('sid=' + SID) in (self.headers.get('Cookie') or '')
    def _ui(self, u):
        p = u.path.rstrip('/') or '/ui'
        if p == '/ui/login':
            msg = '<p style="color:#ff8a80">Wrong user name or password.</p>' if 'bad' in u.query else ''
            return self._send(200, page('Sign in', '<h1>Sign in</h1>%s<form method=post action=/ui/login>User<br><input type=text name=u autofocus><br>Password<br><input type=password name=p><br><button>Sign in</button></form><p class=mut>A small stand-in for a repository manager, built for this lesson.</p>' % msg, login=True))
        if not self._ui_ok(): return self._redir('/ui/login')
        if p == '/ui':
            cards = ''
            for r in repos():
                c = scan(r['name']); nup = sum(len([f for f in fl if f.endswith('.jar')]) for v in c.values() for fl in v.values())
                snap = r['type'] == 'snapshot'
                cards += '<div class=card><span class="pill %s">%s</span><h2>%s</h2><div class="mono mut">%s</div><p class=mut>Redeploy: %s<br>%d uploaded jar%s</p><a href="/ui/repo/%s">Browse</a></div>' % ('snap' if snap else 'rel', 'SNAPSHOT' if snap else 'RELEASE', r['name'], addr(r['name']).replace('http://', ''), 'allowed' if r['redeploy'] else 'disabled', nup, '' if nup == 1 else 's', r['name'])
            if not cards: cards = '<p class=mut>No repositories yet.</p>'
            return self._send(200, page('Browse', '<h1>Repositories</h1><p style="margin:6px 0 14px"><a class=btn href="/ui/create">Create repository</a></p>%s' % cards, 'b'))
        if p == '/ui/create':
            return self._send(200, page('Create repository', '<h1>Create repository</h1><form method=post action=/ui/create>Name<br><input type=text name=name autofocus><br>Type<br><label class=r><input type=radio name=type value=release checked>Release</label><label class=r><input type=radio name=type value=snapshot>Snapshot</label><div style="height:2px"></div>Deployment policy<br><label class=r><input type=radio name=policy value=disable checked>Disable redeploy</label><label class=r><input type=radio name=policy value=allow>Allow redeploy</label><div style="height:4px"></div><button>Create repository</button></form>', 'b'))
        if p.startswith('/ui/repo/'):
            name = p.split('/')[3]; r = repo_of(name)
            if not r: return self._send(404, page('Not found', '<h1>No such repository</h1>'))
            c = scan(name); rows = ''
            for ga, vs in sorted(c.items()):
                g, a = ga.split(':'); rows += '<tr><td class=mono>%s</td><td class=mono>%s</td><td>%s</td></tr>' % (g.replace('/', '.'), a, ', '.join('<a href="/ui/comp/%s/%s/%s">%s</a>' % (name, quote(g + '/' + a, safe=''), v, v) for v in sorted(vs)))
            return self._send(200, page(name, '<h1>%s</h1><p class="mono mut">%s</p><table><tr><th>group</th><th>artifact</th><th>versions</th></tr>%s</table>' % (name, addr(name).replace('http://', ''), rows or '<tr><td colspan=3 class=mut>empty</td></tr>'), 'b'))
        if p.startswith('/ui/comp/'):
            parts = p.split('/'); repo, ga, ver = parts[3], unquote(parts[4]), parts[5]; g, a = ga.rsplit('/', 1)
            d = os.path.join(ROOT, repo, ga, ver); rows = ''
            for f in sorted(os.listdir(d), reverse=True) if os.path.isdir(d) else []:
                if not f.endswith(('.jar', '.pom')): continue
                fp = os.path.join(d, f); rows += '<tr><td class=mono>%s</td><td>%d B</td><td class=mono>%s</td><td>%s</td></tr>' % (f, os.path.getsize(fp), sha1(fp)[:12], time.strftime('%H:%M:%S', time.localtime(os.path.getmtime(fp))))
            pill = '<span class="pill snap">SNAPSHOT</span>' if ver.endswith('SNAPSHOT') else '<span class="pill rel">RELEASE</span>'
            dep = html.escape('<dependency>\n  <groupId>%s</groupId>\n  <artifactId>%s</artifactId>\n  <version>%s</version>\n</dependency>' % (g.replace('/', '.'), a, ver))
            return self._send(200, page(ver, '<h1>%s %s</h1><p class=mut>%s &nbsp; in %s</p><table><tr><th>file</th><th>size</th><th>sha-1</th><th>uploaded</th></tr>%s</table><p class=mut>Use it in another project:</p><pre>%s</pre>' % (html.escape(a), html.escape(ver), pill, html.escape(repo), rows, dep), 'b'))
        if p == '/ui/events':
            rows = ''
            for e in reversed(events()):
                bad = e['status'] != 201; rows += '<tr class="%s"><td class=mono>%s</td><td>%s</td><td>%s</td><td class=mono>%s</td><td>%s</td></tr>' % ('red' if bad else '', e['id'], e['status'], html.escape(e['repo']), html.escape(e['file']), html.escape(e['note']))
            return self._send(200, page('Events', '<h1>Upload events</h1><table><tr><th>event</th><th>status</th><th>repository</th><th>file</th><th>result</th></tr>%s</table>' % (rows or '<tr><td colspan=5 class=mut>no uploads yet</td></tr>'), 'e'))
        return self._send(404, page('Not found', '<h1>Not found</h1>'))
    def do_POST(self):
        n = int(self.headers.get('Content-Length', 0)); form = parse_qs(self.rfile.read(n).decode())
        if self.path == '/ui/login':
            if form.get('u', [''])[0] == USER and form.get('p', [''])[0] == PW: return self._redir('/ui', (('Set-Cookie', 'sid=%s; Path=/' % SID),))
            return self._redir('/ui/login?bad=1')
        if self.path == '/ui/create' and self._ui_ok():
            name = form.get('name', [''])[0].strip(); typ = form.get('type', ['release'])[0]; pol = form.get('policy', ['disable'])[0]
            if re.fullmatch(r'[a-z0-9][a-z0-9-]{0,40}', name) and not repo_of(name):
                with LOCK: rs = repos(); rs.append({'name': name, 'type': typ, 'redeploy': pol == 'allow'}); json.dump(rs, open(RPF, 'w'))
                os.makedirs(os.path.join(ROOT, name), exist_ok=True)
            return self._redir('/ui')
        self._send(404, b'')
    def _mvn_path(self):
        m = re.match(r'/repository/([^/]+)/(.*)', self.path)
        return (m.group(1), m.group(2)) if m else (None, None)
    def do_GET(self):
        u = urlparse(self.path)
        if u.path == '/': return self._redir('/ui')
        if u.path.startswith('/ui'): return self._ui(u)
        repo, rest = self._mvn_path()
        if not repo or not self._ok(): return
        if repo_of(repo): self.path = '/' + repo + '/' + rest; super().do_GET()
        else: self._send(404, b'')
    def do_HEAD(self):
        repo, rest = self._mvn_path()
        if not repo or not self._ok(): return
        if repo_of(repo): self.path = '/' + repo + '/' + rest; super().do_HEAD()
        else: self._send(404, b'')
    def do_PUT(self):
        n = int(self.headers.get('Content-Length', 0)); data = self.rfile.read(n)
        if not self._ok(): return
        repo, rest = self._mvn_path(); r = repo_of(repo) if repo else None
        def reply(code): self.send_response(code); self.send_header('Content-Length', '0'); self.end_headers()
        if not r: return reply(404)
        base = os.path.basename(rest); parts = rest.split('/')
        ver = parts[-2] if len(parts) >= 3 else ''
        if not base.startswith('maven-metadata') and ver:
            if (r['type'] == 'snapshot') != ver.endswith('SNAPSHOT'):
                log_event(repo, rest, 400, 'REJECTED: wrong version type for this repository'); return reply(400)
        p = os.path.join(ROOT, repo, rest)
        if not r['redeploy'] and os.path.exists(p) and not base.startswith('maven-metadata'):
            log_event(repo, rest, 409, 'REJECTED: redeploy is disabled'); return reply(409)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'wb').write(data); log_event(repo, rest, 201, 'stored'); reply(201)
    def log_message(self, *a): pass
os.makedirs(ROOT, exist_ok=True)
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), functools.partial(H, directory=ROOT)).serve_forever()
