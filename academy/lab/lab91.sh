#!/bin/sh
# lab91.sh : publish snapshot and release artifacts to a repository (MC10-O07). Run with sudo, in your own Ubuntu virtual machine.
#   up | check | down | status        Needs a JDK, Maven and python3 (sudo apt install -y openjdk-21-jdk-headless maven python3). Maven downloads its own plugins once.
# Mission: publish a snapshot, then a release, find out why a release can never be published twice, read the proof in the repository web page, and ship the next version.
D=${LAB91_DIR:-/opt/lab91}
U=${SUDO_USER:-root}
PORT=8092
stopsrv() { [ -f $D/srv.pid ] && kill $(cat $D/srv.pid) 2>/dev/null; rm -f $D/srv.pid; true; }
down() { stopsrv; pkill -f "$D/srv.py" 2>/dev/null; rm -rf $D /tmp/lab91-chk; true; }
startsrv() {
  if ! curl -s -o /dev/null http://127.0.0.1:$PORT/ 2>/dev/null; then
    nohup python3 $D/srv.py $D/store dev "$(cat $D/pass.txt)" $PORT >/dev/null 2>&1 &
    echo $! > $D/srv.pid; sleep 1
  fi
}
up() {
  command -v javac >/dev/null 2>&1 && command -v mvn >/dev/null 2>&1 && command -v python3 >/dev/null 2>&1 || { echo "javac, mvn or python3 not found: run  sudo apt install -y openjdk-21-jdk-headless maven python3"; exit 1; }
  down; mkdir -p $D/shop/src/main/java/cloudcart $D/store
  cat > $D/srv.py <<'EOF_S'
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
.wrap{padding:22px 28px}h1{margin:0 0 14px;font-size:32px}
.card{display:inline-block;vertical-align:top;width:410px;background:#12303a;border:2px solid #2d6a78;border-radius:14px;padding:14px 22px;margin:0 22px 18px 0}
.card h2{margin:4px 0 4px;font-size:28px}.card a{color:#7fe0d0}
.pill{display:inline-block;border-radius:8px;padding:2px 12px;font-size:18px;font-weight:bold;color:#10242a}.snap{background:#f2c46d}.rel{background:#7fe0d0}.bad{background:#ff8a80}
table{border-collapse:collapse;width:100%}th{text-align:left;color:#9fb8bc;font-weight:normal;border-bottom:2px solid #2d6a78;padding:6px 10px}td{padding:8px 10px;border-bottom:1px solid #1e4a55}
a{color:#7fe0d0}.mono{font-family:"DejaVu Sans Mono",monospace;font-size:18px}.red td{color:#ff8a80;font-weight:bold}.mut{color:#9fb8bc}
input[type=text],input[type=password]{font:22px "DejaVu Sans",sans-serif;padding:10px;width:420px;border-radius:8px;border:2px solid #2d6a78;background:#0b1a1e;color:#e4f0f1;margin:6px 0 12px}
label.r{display:block;margin:4px 0;font-size:22px}input[type=radio]{width:22px;height:22px;vertical-align:middle;margin-right:10px}
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
            return self._send(200, page('Browse', '<h1>Repositories</h1>%s<p><a class=btn href="/ui/create">Create repository</a></p>' % cards, 'b'))
        if p == '/ui/create':
            return self._send(200, page('Create repository', '<h1>Create repository</h1><form method=post action=/ui/create>Name<br><input type=text name=name autofocus><br>Type<br><label class=r><input type=radio name=type value=release checked>Release</label><label class=r><input type=radio name=type value=snapshot>Snapshot</label><div style="height:8px"></div>Deployment policy<br><label class=r><input type=radio name=policy value=disable checked>Disable redeploy</label><label class=r><input type=radio name=policy value=allow>Allow redeploy</label><div style="height:10px"></div><button>Create repository</button></form>', 'b'))
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
EOF_S
  printf 'corp-%s\n' "$(date +%s | sha256sum | cut -c1-12)" > $D/pass.txt; chmod 600 $D/pass.txt
  cat > $D/shop/pom.xml <<EOF_P
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.cloudcart</groupId>
  <artifactId>cart-core</artifactId>
  <version>1.0.0-SNAPSHOT</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
  </properties>

  <distributionManagement>
    <snapshotRepository>
      <id>corp</id>
      <url>http://localhost:$PORT/repository/corp-snapshots</url>
    </snapshotRepository>
    <repository>
      <id>corp</id>
      <url>http://localhost:$PORT/repository/corp-releases</url>
    </repository>
  </distributionManagement>

  <build>
    <plugins>
      <plugin><artifactId>maven-clean-plugin</artifactId><version>3.2.0</version></plugin>
      <plugin><artifactId>maven-resources-plugin</artifactId><version>3.3.0</version></plugin>
      <plugin><artifactId>maven-compiler-plugin</artifactId><version>3.10.1</version></plugin>
      <plugin><artifactId>maven-surefire-plugin</artifactId><version>2.22.3</version></plugin>
      <plugin><artifactId>maven-jar-plugin</artifactId><version>3.3.0</version></plugin>
      <plugin><artifactId>maven-install-plugin</artifactId><version>3.1.1</version></plugin>
      <plugin><artifactId>maven-deploy-plugin</artifactId><version>3.1.1</version></plugin>
    </plugins>
  </build>
</project>
EOF_P
  cat > $D/shop/src/main/java/cloudcart/Cart.java <<'EOF_G'
package cloudcart;

public class Cart {
    public static String banner() {
        return "cloudcart";
    }
}
EOF_G
  cat > $D/shop/settings.xml <<'EOF_X'
<settings>
  <servers>
    <server>
      <id>corp</id>
      <username>dev</username>
      <password>${env.CORP_PASS}</password>
    </server>
  </servers>
</settings>
EOF_X
  chmod 600 $D/shop/settings.xml
  cat > $D/TASKS.txt <<'EOF_K'
LAB 91 : publish cart-core to the company repository (a small local stand-in for a repository manager, with a web page).   Work in /opt/lab91/shop

Web page: http://localhost:8092     user: dev     password: cat /opt/lab91/pass.txt
First, in a terminal:  export CORP_PASS=$(cat /opt/lab91/pass.txt)
Always:                mvn -B -s settings.xml ...      (the login is already in settings.xml)

1  Repositories.  In the web page, click "Create repository" twice:
                    name corp-snapshots   type Snapshot   policy Allow redeploy
                    name corp-releases    type Release    policy Disable redeploy
2  Snapshot.      Deploy 1.0.0-SNAPSHOT:   mvn -B -s settings.xml deploy      (find it in the web page: Browse, corp-snapshots)
3  Release.       Change the version in pom.xml to 1.0.0 (no SNAPSHOT) and deploy it.
4  Again.         Deploy 1.0.0 a second time. It must fail. Save the error line:
                    mvn -B -s settings.xml deploy 2>&1 | grep -o 'status code.*' > conflict.txt
                  Then open the Events page, find a red REJECTED line, and write its event id (like E0007) into ui.txt.
5  Next + why.    Change the version to 1.0.1 and deploy it. Write one sentence in why.txt about why a release is never
                  published twice. It must contain the word  release  and one of  immutable, reproducible, overwrite, changed.

Then:  lab check     (all 5 must pass)       and later:  lab down
EOF_K
  chown -R $U $D 2>/dev/null; chown root:root $D/srv.py $D/store 2>/dev/null; chmod 777 $D/store
  startsrv
  echo "lab91 ready: cd $D/shop   (task list: $D/TASKS.txt)"
}
check() {
  [ -d $D/shop ] || { echo "lab not set up: run  lab up"; exit 1; }
  startsrv
  cd $D/shop; ok=0; S=$D/store
  pass() { echo "PASS  $1"; ok=$((ok+1)); }
  fail() { echo "FAIL  $1"; }
  RJ=$S/.repos.json
  if python3 -c "import json,sys;r={x['name']:x for x in json.load(open('$RJ'))};a=r['corp-snapshots'];b=r['corp-releases'];sys.exit(0 if a['type']=='snapshot' and a['redeploy'] and b['type']=='release' and not b['redeploy'] else 1)" 2>/dev/null; then pass "1 repositories corp-snapshots and corp-releases are created with the right type and policy"; else fail "1 repositories corp-snapshots and corp-releases are created with the right type and policy"; fi
  if ls $S/corp-snapshots/com/cloudcart/cart-core/1.0.0-SNAPSHOT/cart-core-1.0.0-*.jar >/dev/null 2>&1; then pass "2 a snapshot of 1.0.0 is in corp-snapshots"; else fail "2 a snapshot of 1.0.0 is in corp-snapshots"; fi
  EIDS=$(python3 -c "import json;print(' '.join(e['id'] for e in json.load(open('$S/.events.json')) if e['status']==409))" 2>/dev/null); EID=none; for x in $EIDS; do [ -f ui.txt ] && grep -q "$x" ui.txt && EID=$x; done
  if [ -f $S/corp-releases/com/cloudcart/cart-core/1.0.0/cart-core-1.0.0.jar ] && [ -f conflict.txt ] && grep -q '409' conflict.txt && [ "$EID" != none ]; then pass "3 release 1.0.0 is published, the redeploy failed with 409, and ui.txt has the rejected event id"; else fail "3 release 1.0.0 is published, the redeploy failed with 409, and ui.txt has the rejected event id"; fi
  if [ -f $S/corp-releases/com/cloudcart/cart-core/1.0.1/cart-core-1.0.1.jar ] && grep -q '<version>1.0.1</version>' pom.xml; then pass "4 release 1.0.1 is published and the pom says 1.0.1"; else fail "4 release 1.0.1 is published and the pom says 1.0.1"; fi
  if [ -f why.txt ] && grep -qi 'release' why.txt && grep -qiE 'immutable|reproducible|overwrite|changed' why.txt; then pass "5 why.txt explains release immutability"; else fail "5 why.txt explains release immutability"; fi
  echo "$ok/5 checks passed"; [ $ok -eq 5 ]
}
status() { [ -d $D ] && echo "lab91 is set up in $D" || echo "lab91 is not set up"; }
case "$1" in up) up;; check) check;; down) down; echo "lab91 removed";; status) status;; *) echo "usage: lab91.sh up|check|down|status"; exit 2;; esac
