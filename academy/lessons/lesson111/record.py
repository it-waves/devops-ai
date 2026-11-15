"""Record Lesson 111: ship a bad Tomcat release, watch its health and recover, with a full screen Chrome comparison, one continuous screen recording. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson111')
import term
term.XSIZE = '1920x1080'
from term import *
import time, subprocess
import video as V
LD = '/home/claude/academy/lesson111'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab111.sh'
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
        subprocess.Popen(['google-chrome', '--no-sandbox', '--incognito', '--user-data-dir=/tmp/chp', '--no-first-run', '--no-default-browser-check', '--disable-gpu', '--disable-infobars', '--test-type', '--window-position=0,0', '--force-device-scale-factor=1.25', '--window-size=1536,864', 'about:blank'], env=E97, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(40):
            time.sleep(1.0); W['chrome'] = wid('google-chrome') or wid('chromium') or wid('Google-chrome')
            if W['chrome']: break
        time.sleep(1.5); raise_('chrome')
    elif k == 'raise':
        if a[1] == 'xterm': subprocess.run('pkill -f user-data-dir=/tmp/chp', shell=True); time.sleep(0.8)
        raise_(a[1])
    elif k == 'park': mv(1900, 1060)
    elif k == 'scroll':
        for _ in range(a[1]): xt('click', '5' if a[1] > 0 else '4'); time.sleep(0.12)
    elif k == 'up':
        for _ in range(a[1]): xt('click', '4'); time.sleep(0.05)
def ui(r, cid, acts):
    tot = r.dur[cid] + V.EXTRA.get(cid, 0)
    for f, a in acts:
        r.at(cid, f * tot)
        do_action(a)
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB111_TOMCAT_BASE=file:///opt/dist SUDO_USER=student sh {LAB} up > /tmp/lab111up.log 2>&1', shell=True)
    subprocess.run('pkill -f "Xvfb :97"; true', shell=True); time.sleep(1.0)
    p = xterm_start(PFX); term.WIN[:] = [1920, 1080]; focus()
    for _ in range(400):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(2); key('ctrl+l'); time.sleep(0.4)
    W['xterm'] = wid('xterm')
    raise_('xterm'); time.sleep(0.5); focus(); key('ctrl+l'); mv(1900, 1060)
    fx = subprocess.Popen(['python3', '/home/claude/academy/common/cursorfx.py'], env=E97); time.sleep(1)
    r = Run(LD, V, scene, delay=80); T[0] = r.T0
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        else: ui(r, st[1], st[2])
    r.end(); p.terminate(); fx.terminate(); time.sleep(0.5)
    subprocess.run(f'pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; pkill -f catalina.base; SUDO_USER=student sh {LAB} down >/dev/null 2>&1; true', shell=True)
LOOP = 'for i in 1 2 3; do sleep 2; ./health.sh; done'
HC = 'curl -s localhost:8087/cart/health.jsp'
W1 = 'cp releases/cart-1.0.war tomcat/webapps/cart.war'
W2 = 'cp releases/cart-2.0.war tomcat/webapps/cart.war'
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab111'),
  ('cmd', 'l1', 'ls'),
  ('cmd', 'l2', 'ls releases'),
  ('cmd', 'l3', 'cat data/db.properties'),
  ('cmd', 'l4', 'tomcat/bin/startup.sh | tail -n 1'),
  ('cmd', 'l5', 'sleep 8; ' + HC),
  ('cmd', 'l6', 'vim health.sh'),
  ('ui', 'l6b', [(0.1, ('type', 'i')), (0.18, ('type', "#!/bin/sh\nu=localhost:8087/cart/health.jsp\nc=$(curl -s -o /dev/null -w '%{http_code}' $u)\n"))]),
  ('ui', 'l6c', [(0.05, ('type', 'echo "health: $c"\n[ "$c" = 200 ]')), (0.6, ('key', 'Escape')), (0.75, ('type', ':wq\n'))]),
  ('cmd', 'l7', 'chmod +x health.sh'),
  ('cmd', 'l8', './health.sh'),
  ('cmd', 'l9', LOOP),
  ('cmd', 'l10', W2),
  ('cmd', 'l11', LOOP),
  ('cmd', 'l12', "curl -s localhost:8087/cart/ | grep -o '<h1.*h1>'"),
  ('cmd', 'l13', HC),
  ('cmd', 'l14', "grep -o 'health FAIL.*' tomcat/logs/localhost.*.log"),
  ('ui', 'u0', [(0.0, ('chrome',)), (0.55, ('key', 'ctrl+l')), (0.62, ('type', 'localhost:8087/cart/')), (0.9, ('key', 'Return'))]),
  ('ui', 'u1', [(0.15, ('move', 768, 330)), (0.45, ('move', 768, 440)), (0.75, ('move', 768, 540))]),
  ('ui', 'u2', [(0.1, ('key', 'ctrl+l')), (0.2, ('type', 'localhost:8087/cart/health.jsp')), (0.7, ('key', 'Return'))]),
  ('ui', 'u3', [(0.1, ('move', 150, 130)), (0.45, ('move', 330, 130)), (0.75, ('park',)), (0.85, ('raise', 'xterm'))]),
  ('cmd', 'l15', W1),
  ('cmd', 'l16', LOOP),
  ('cmd', 'l17', HC),
  ('cmd', 'l18', 'echo pool.size=10 >> data/db.properties'),
  ('cmd', 'l19', 'cat data/db.properties'),
  ('cmd', 'l20', W2),
  ('cmd', 'l21', 'sleep 6; ' + HC),
  ('cmd', 'l22', "grep -c 'cart.war.*finished' tomcat/logs/catalina.*.log"),
  ('cmd', 'l23', 'tomcat/bin/shutdown.sh | tail -n 1'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
