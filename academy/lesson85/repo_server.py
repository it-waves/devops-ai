"""Tiny HTTP view of a Maven repository folder: dark listing, breadcrumb, GAV panel. usage: repo_server.py ROOT PORT"""
import os, sys, re, html, http.server, urllib.parse
ROOT = sys.argv[1]; PORT = int(sys.argv[2])
CSS = """body{margin:0;background:#0b1a1e;color:#e4f0f1;font:34px 'DejaVu Sans',sans-serif}header{padding:28px 60px;background:#10272d;border-bottom:6px solid #7fe0d0}
h1{margin:0 0 10px;font-size:30px;color:#7fe0d0;letter-spacing:2px}.crumb{font:bold 40px 'DejaVu Sans Mono',monospace;color:#fff}.crumb span{color:#ffd24a}
main{padding:30px 60px}a{display:block;padding:14px 22px;margin:8px 0;background:#13313a;border-left:8px solid #7fe0d0;border-radius:10px;color:#e4f0f1;text-decoration:none;font:bold 38px 'DejaVu Sans Mono',monospace}
a:hover{background:#1d4a56}.gav{display:flex;gap:30px;margin:0 0 24px}.gav div{padding:14px 26px;background:#10272d;border:4px solid #ffd24a;border-radius:14px;font:bold 34px 'DejaVu Sans Mono',monospace}.gav small{display:block;font:24px 'DejaVu Sans';color:#9fbcc0}
pre{background:#10272d;padding:24px 34px;border-radius:14px;font:28px/1.35 'DejaVu Sans Mono',monospace;white-space:pre-wrap;border-left:8px solid #ffd24a}"""
def gav(parts):
    # find version dir: last dir whose parent holds a jar/pom named parent-version
    if len(parts) >= 3:
        v, a, g = parts[-1], parts[-2], '.'.join(parts[:-2])
        if os.path.exists(os.path.join(ROOT, *parts, f'{a}-{v}.pom')): return g, a, v
    return None
class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(s):
        p = urllib.parse.unquote(s.path.split('?')[0]); parts = [x for x in p.split('/') if x]; fs = os.path.join(ROOT, *parts)
        if os.path.isfile(fs):
            b = open(fs, 'rb').read()
            if fs.endswith(('.pom', '.xml')):
                body = f"<style>{CSS}</style><header><h1>MAVEN REPOSITORY  ·  local copy</h1><div class=crumb>/ {' / '.join(parts)}</div></header><main><pre>{html.escape(re.sub(r'<!--.*?-->\s*', '', b.decode(errors='replace'), count=1, flags=re.S))}</pre></main>".encode()
            elif fs.endswith('.sha1'):
                body = f"<style>{CSS}</style><header><h1>MAVEN REPOSITORY  ·  local copy</h1><div class=crumb>/ {' / '.join(parts)}</div></header><main><pre>{html.escape(b.decode())}</pre></main>".encode()
            else: body = b
            s.send_response(200); s.send_header('Content-Type', 'text/html; charset=utf-8'); s.end_headers(); s.wfile.write(body); return
        if not os.path.isdir(fs): s.send_error(404); return
        items = sorted(os.listdir(fs)); items = [i for i in items if not i.startswith('.')]
        crumb = ' <span>/</span> '.join(['repository'] + [html.escape(x) for x in parts])
        g = gav(parts); panel = ''
        if g: panel = "<div class=gav>" + ''.join(f"<div><small>{n}</small>{html.escape(v)}</div>" for n, v in zip(['groupId', 'artifactId', 'version'], g)) + "</div>"
        links = ''.join(f"<a href='{html.escape(urllib.parse.quote('/' + '/'.join(parts + [i])))}{'/' if os.path.isdir(os.path.join(fs, i)) else ''}'>{html.escape(i)}{'/' if os.path.isdir(os.path.join(fs, i)) else ''}</a>" for i in items if not (g and i.endswith('.sha1') and False))
        body = f"<style>{CSS}</style><header><h1>MAVEN REPOSITORY  ·  local copy, not Maven Central</h1><div class=crumb>{crumb}</div></header><main>{panel}{links}</main>".encode()
        s.send_response(200); s.send_header('Content-Type', 'text/html; charset=utf-8'); s.end_headers(); s.wfile.write(body)
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H).serve_forever()
