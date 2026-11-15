"""Record Lesson 109: install Tomcat in the terminal, then tour it in Chrome, one continuous screen recording. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson109')
import term
from term import *
import time, subprocess
import video as V
LD = '/home/claude/academy/lesson109'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab109.sh'
def _rec(out, secs):
    return subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-draw_mouse', '1', '-framerate', '30', '-video_size', f'{term.WIN[0]}x{term.WIN[1]}', '-i', term.DISP, '-t', str(secs), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', out], env=term.E97, stdin=subprocess.PIPE)
term.rec_start = _rec
W = {}
T = [time.time()]
def wid(cls):
    o = subprocess.run(['xdotool', 'search', '--onlyvisible', '--class', cls], env=E97, capture_output=True, text=True).stdout.split()
    return o[-1] if o else None
def raise_(name):
    i = W[name]; xt('windowraise', i); xt('windowfocus', i)
def mv(x, y): xt('mousemove', x, y); time.sleep(0.12)
def click(x, y): mv(x, y); time.sleep(0.45); xt('click', 1)
def do_action(a):
    k = a[0]; print(round(time.time() - T[0], 1), a, flush=True)
    if k == 'type': typ(a[1], 80)
    elif k == 'key': key(a[1])
    elif k == 'click': click(a[1], a[2])
    elif k == 'move': mv(a[1], a[2])
    elif k == 'chrome':
        subprocess.run('rm -rf /tmp/chp', shell=True)
        subprocess.Popen(['google-chrome', '--no-sandbox', '--incognito', '--user-data-dir=/tmp/chp', '--no-first-run', '--no-default-browser-check', '--disable-gpu', '--disable-infobars', '--test-type', '--window-position=0,0', f'--window-size={term.WIN[0]},{term.WIN[1]}', 'about:blank'], env=E97, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(40):
            time.sleep(1.0); W['chrome'] = wid('google-chrome') or wid('chromium') or wid('Google-chrome')
            if W['chrome']: break
        time.sleep(1.5); raise_('chrome')
    elif k == 'raise':
        if a[1] == 'xterm': subprocess.run('pkill -f user-data-dir=/tmp/chp', shell=True); time.sleep(0.8)
        raise_(a[1])
    elif k == 'park': mv(1078, 596)
def ui(r, cid, acts):
    tot = r.dur[cid] + V.EXTRA.get(cid, 0)
    for f, a in acts:
        r.at(cid, f * tot)
        do_action(a)
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB109_TOMCAT_BASE=file:///opt/dist SUDO_USER=student sh {LAB} up > /tmp/lab109up.log 2>&1', shell=True)
    p = xterm_start(PFX); term.WIN[:] = [1080, 600]; focus()
    for _ in range(400):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(2); key('ctrl+l'); time.sleep(0.4)
    W['xterm'] = wid('xterm')
    raise_('xterm'); mv(1078, 596); time.sleep(0.5); focus(); key('ctrl+l')
    fx = subprocess.Popen(['python3', '/home/claude/academy/common/cursorfx.py'], env=E97); time.sleep(1)
    r = Run(LD, V, scene, delay=80); T[0] = r.T0
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        else: ui(r, st[1], st[2])
    r.end(); p.terminate(); fx.terminate(); time.sleep(0.5)
    subprocess.run(f'pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; pkill -f catalina.base; SUDO_USER=student sh {LAB} down >/dev/null 2>&1; true', shell=True)
HQ = "curl -s -o /dev/null -w '%{http_code}\\n'"
WH = "curl -sk https://localhost:8443/cart/whoami.jsp"
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab109'),
  ('cmd', 'l1', 'ls'),
  ('cmd', 'l2', 'tomcat/bin/startup.sh | tail -n 1'),
  ('cmd', 'l3', 'sleep 8; ' + HQ + ' localhost:8084/cart/'),
  ('cmd', 'l4', "grep -n 'Connector port' tomcat/conf/server.xml | cut -c1-70"),
  ('cmd', 'l5', 'openssl req -x509 -newkey rsa:2048 -nodes -keyout tls/cart.key -out tls/cart.crt -subj /CN=localhost 2>/dev/null'),
  ('cmd', 'l6', 'ls tls'),
  ('cmd', 'l7', 'openssl x509 -in tls/cart.crt -noout -subject -dates'),
  ('cmd', 'l8', 'vim nginx/conf.d/cart.conf'),
  ('ui', 'l8b', [(0.1, ('type', 'i')), (0.2, ('type', 'server {\n  listen 8443 ssl;\n'))]),
  ('ui', 'l8c', [(0.1, ('type', '  ssl_certificate /opt/lab109/tls/cart.crt;\n  ssl_certificate_key /opt/lab109/tls/cart.key;\n'))]),
  ('ui', 'l8d', [(0.05, ('type', '  location / {\n    proxy_pass http://127.0.0.1:8084;\n  }\n}')), (0.8, ('key', 'Escape')), (0.88, ('type', ':wq\n'))]),
  ('cmd', 'l9', 'ng -t'),
  ('cmd', 'l10', 'ng'),
  ('cmd', 'l11', "curl -sk -o /dev/null -w '%{http_code}\\n' https://localhost:8443/cart/"),
  ('cmd', 'l12', 'curl -sS https://localhost:8443/cart/ 2>&1 | head -n 1'),
  ('cmd', 'l13', WH),
  ('cmd', 'l14', 'vim nginx/conf.d/cart.conf'),
  ('ui', 'l14b', [(0.1, ('type', ':6\n')), (0.2, ('type', 'o')), (0.3, ('type', '    proxy_set_header X-Forwarded-Proto $scheme;\n    proxy_set_header X-Forwarded-For $remote_addr;')), (0.85, ('key', 'Escape')), (0.9, ('type', ':wq\n'))]),
  ('cmd', 'l15', 'ng -s reload'),
  ('cmd', 'l16', WH),
  ('cmd', 'l17', 'vim nginx/conf.d/cart.conf'),
  ('ui', 'l17b', [(0.05, ('type', 'Go')), (0.12, ('type', 'server {\n  listen 8085;\n  return 301 https://localhost:8443$request_uri;\n}')), (0.85, ('key', 'Escape')), (0.9, ('type', ':wq\n'))]),
  ('cmd', 'l18', 'ng -s reload'),
  ('cmd', 'l19', "curl -s -o /dev/null -w '%{http_code} %{redirect_url}\\n' localhost:8085/cart/"),
  ('ui', 'u0', [(0.0, ('chrome',)), (0.6, ('key', 'ctrl+l')), (0.7, ('type', 'https://localhost:8443/cart/')), (0.92, ('key', 'Return'))]),
  ('ui', 'u1', [(0.3, ('move', 540, 250)), (0.7, ('move', 600, 190))]),
  ('ui', 'u2', [(0.1, ('click', 243, 560)), (0.55, ('move', 282, 311)), (0.8, ('click', 282, 311))]),
  ('ui', 'u3', [(0.3, ('move', 175, 63)), (0.7, ('move', 540, 300))]),
  ('ui', 'u4', [(0.1, ('key', 'ctrl+l')), (0.2, ('type', 'localhost:8085/cart/')), (0.45, ('key', 'Return')), (0.85, ('raise', 'xterm')), (0.92, ('park',))]),
  ('cmd', 'l20', 'ng -s stop'),
  ('cmd', 'l21', 'tomcat/bin/shutdown.sh | tail -n 1'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
