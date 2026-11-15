"""Record Lesson 105: install Tomcat in the terminal, then tour it in Chrome, one continuous screen recording. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson105')
import term
from term import *
import time, subprocess
import video as V
LD = '/home/claude/academy/lesson105'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab105.sh'
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
    elif k == 'raise': raise_(a[1])
    elif k == 'park': mv(1078, 596)
def ui(r, cid, acts):
    tot = r.dur[cid] + V.EXTRA.get(cid, 0)
    for f, a in acts:
        r.at(cid, f * tot)
        do_action(a)
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'SUDO_USER=student sh {LAB} up > /tmp/lab105up.log 2>&1', shell=True)
    p = xterm_start(PFX); term.WIN[:] = [1080, 600]; focus()
    for _ in range(400):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(2); key('ctrl+l'); time.sleep(0.4)
    W['xterm'] = wid('xterm')
    subprocess.run('rm -rf /tmp/chp', shell=True)
    ch = subprocess.Popen(['google-chrome', '--no-sandbox', '--incognito', '--user-data-dir=/tmp/chp', '--no-first-run', '--no-default-browser-check', '--disable-gpu', '--disable-infobars', '--test-type', '--window-position=0,0', f'--window-size={term.WIN[0]},{term.WIN[1]}', 'about:blank'], env=E97, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(6); W['chrome'] = wid('google-chrome') or wid('chromium') or wid('Google-chrome')
    raise_('xterm'); mv(1078, 596); time.sleep(0.5); focus(); key('ctrl+l')
    fx = subprocess.Popen(['python3', '/home/claude/academy/common/cursorfx.py'], env=E97); time.sleep(1)
    r = Run(LD, V, scene, delay=80); T[0] = r.T0
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        else: ui(r, st[1], st[2])
    r.end(); p.terminate(); ch.terminate(); fx.terminate(); time.sleep(0.5)
    subprocess.run(f'pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; pkill -f catalina.base; SUDO_USER=student sh {LAB} down >/dev/null 2>&1; true', shell=True)
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab105'),
  ('cmd', 'l1', 'ls dl'),
  ('cmd', 'l2', 'cd dl'),
  ('cmd', 'l3', 'sha512sum -c apache-tomcat-10.1.34.tar.gz.sha512'),
  ('cmd', 'l4', 'cd ..'),
  ('cmd', 'l5', 'sudo useradd -r -s /usr/sbin/nologin -d /opt/lab105/tomcat tomcat'),
  ('cmd', 'l6', 'getent passwd tomcat'),
  ('cmd', 'l7', 'sudo mkdir tomcat'),
  ('cmd', 'l8', 'sudo tar xzf dl/apache-tomcat-10.1.34.tar.gz -C tomcat --strip-components=1'),
  ('cmd', 'l9', 'ls tomcat'),
  ('cmd', 'l10', 'sudo chown -R tomcat: tomcat'),
  ('cmd', 'l11', 'ls -ld tomcat tomcat/conf tomcat/logs'),
  ('cmd', 'l12', 'sudo -u tomcat tomcat/bin/startup.sh 2>&1 | tail -n 1'),
  ('cmd', 'l13', 'ps -o user,pid,comm -C java'),
  ('cmd', 'l14', "curl -s -o /dev/null -w '%{http_code}\\n' localhost:8080"),
  ('cmd', 'l15', 'grep "Server startup" tomcat/logs/catalina.out | cut -c1-110'),
  ('ui', 'u0', [(0.02, ('raise', 'chrome')), (0.25, ('key', 'ctrl+l')), (0.4, ('type', 'localhost:8080')), (0.85, ('key', 'Return'))]),
  ('ui', 'u1', [(0.3, ('move', 540, 215)), (0.7, ('move', 540, 160))]),
  ('ui', 'u2', [(0.2, ('move', 950, 271)), (0.5, ('move', 950, 307)), (0.8, ('move', 950, 343))]),
  ('ui', 'u3', [(0.3, ('click', 950, 307))]),
  ('ui', 'u4', [(0.4, ('click', 553, 304))]),
  ('ui', 'u5', [(0.1, ('move', 400, 150)), (0.45, ('move', 300, 230)), (0.7, ('move', 300, 297))]),
  ('ui', 'u6', [(0.2, ('click', 19, 63)), (0.6, ('click', 405, 115))]),
  ('ui', 'u7', [(0.4, ('click', 106, 155))]),
  ('ui', 'u8', [(0.4, ('click', 415, 531))]),
  ('ui', 'u9', [(0.2, ('click', 19, 63)), (0.6, ('click', 679, 531))]),
  ('ui', 'u10', [(0.5, ('raise', 'xterm')), (0.6, ('park',))]),
  ('cmd', 'l16', 'sudo -u tomcat tomcat/bin/shutdown.sh >/dev/null 2>&1'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
