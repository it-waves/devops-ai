"""Record Lesson 108: install Tomcat in the terminal, then tour it in Chrome, one continuous screen recording. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson108')
import term
from term import *
import time, subprocess
import video as V
LD = '/home/claude/academy/lesson108'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab108.sh'
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
    subprocess.run(f'LAB108_TOMCAT_BASE=file:///opt/dist SUDO_USER=student sh {LAB} up > /tmp/lab108up.log 2>&1', shell=True)
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
HQ = "curl -s -o /dev/null -w '%{http_code}\\n' localhost:8082"
LG = 'tomcat/logs/'
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab108'),
  ('cmd', 'l1', 'ls'),
  ('cmd', 'l2', 'tomcat/bin/startup.sh | tail -n 1'),
  ('cmd', 'l3', HQ),
  ('cmd', 'l4', HQ + '/cart/'),
  ('cmd', 'l5', 'ls tomcat/logs'),
  ('cmd', 'l6', "grep -h SEVERE tomcat/logs/catalina.*.log | sed 's/.*startInternal //'"),
  ('cmd', 'l7', 'grep -h -m1 ClassNotFound tomcat/logs/localhost.*.log'),
  ('cmd', 'l8', 'vim tomcat/webapps/cart/WEB-INF/web.xml'),
  ('ui', 'l8c', [(0.1, ('type', ':4,6d\n')), (0.7, ('type', ':wq\n'))]),
  ('cmd', 'l9', 'tomcat/bin/shutdown.sh | tail -n 1'),
  ('cmd', 'l10', 'tomcat/bin/startup.sh | tail -n 1'),
  ('cmd', 'l11', 'sleep 8; ' + HQ + '/cart/'),
  ('cmd', 'l12', "for i in 1 2 3; do " + HQ + "/cart/health.jsp; done"),
  ('ui', 'u0', [(0.0, ('chrome',)), (0.6, ('key', 'ctrl+l')), (0.7, ('type', 'localhost:8082/cart/health.jsp')), (0.92, ('key', 'Return'))]),
  ('ui', 'u1', [(0.3, ('move', 540, 200)), (0.7, ('move', 540, 130))]),
  ('ui', 'u2', [(0.2, ('move', 540, 300)), (0.8, ('raise', 'xterm')), (0.9, ('park',))]),
  ('cmd', 'l13', "grep -h -m1 'Caused by' tomcat/logs/localhost.*.log"),
  ('cmd', 'l14', "tail -n 4 tomcat/logs/localhost_access_log.*.txt | cut -c44-"),
  ('cmd', 'l15', "grep -c '\" 500 ' tomcat/logs/localhost_access_log.*.txt"),
  ('cmd', 'l16', 'echo staging > config/cart.properties'),
  ('cmd', 'l17', 'curl -s localhost:8082/cart/health.jsp'),
  ('cmd', 'l18', 'tomcat/bin/shutdown.sh | tail -n 1'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
