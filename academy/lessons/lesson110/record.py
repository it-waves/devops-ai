"""Record Lesson 110: lock down the Tomcat Manager in the terminal, then tour it full screen in Chrome, one continuous screen recording. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson110')
import term
term.XSIZE = '1920x1080'
from term import *
import time, subprocess
import video as V
LD = '/home/claude/academy/lesson110'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab110.sh'
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
    subprocess.run(f'LAB110_TOMCAT_BASE=file:///opt/dist SUDO_USER=student sh {LAB} up > /tmp/lab110up.log 2>&1', shell=True)
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
HQ = "curl -s -o /dev/null -w '%{http_code}\\n'"
PW = 'Harbor-Lantern-4821'
UF = 'tomcat/conf/tomcat-users.xml'
CX = 'tomcat/webapps/manager/META-INF/context.xml'
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab110'),
  ('cmd', 'l1', 'ls'),
  ('cmd', 'l2', 'tomcat/bin/startup.sh | tail -n 1'),
  ('cmd', 'l3', 'sleep 8; ' + HQ + ' localhost:8086/cart/'),
  ('cmd', 'l4', HQ + ' localhost:8086/manager/html'),
  ('cmd', 'l5', HQ + ' -u admin:admin localhost:8086/manager/html'),
  ('cmd', 'l6', 'cat ' + UF),
  ('cmd', 'l7', 'vim ' + UF),
  ('ui', 'l7b', [(0.1, ('type', ':4\n')), (0.2, ('type', 'cc')), (0.3, ('type', '  <user username="ops"\n        password="' + PW + '"\n        roles="manager-gui"/>'))]),
  ('ui', 'l7c', [(0.05, ('key', 'Escape')), (0.55, ('type', ':wq\n'))]),
  ('cmd', 'l8', 'ls -l ' + UF + ' | cut -c1-10'),
  ('cmd', 'l9', 'chmod 600 ' + UF),
  ('cmd', 'l10', 'ls -l ' + UF + ' | cut -c1-10'),
  ('cmd', 'l11', 'ps -o user=,pid= -C java'),
  ('cmd', 'l12', 'grep allow ' + CX),
  ('cmd', 'l13', 'vim ' + CX),
  ('ui', 'l13b', [(0.1, ('type', '/0.0.0.0\n')), (0.5, ('type', ':s#,0.0.0.0/0,::/0##\n'))]),
  ('ui', 'l13c', [(0.2, ('type', ':wq\n'))]),
  ('cmd', 'l14', 'grep allow ' + CX),
  ('cmd', 'l15', 'ss -ltn | grep 8096'),
  ('cmd', 'l16', 'echo SHUTDOWN > /dev/tcp/localhost/8096'),
  ('cmd', 'l17', 'sleep 3; ' + HQ + ' localhost:8086/cart/'),
  ('cmd', 'l18', 'vim tomcat/conf/server.xml'),
  ('ui', 'l18b', [(0.1, ('type', '/Server port\n')), (0.35, ('type', ':s/8096/-1/\n')), (0.7, ('type', ':wq\n'))]),
  ('cmd', 'l19', 'tomcat/bin/startup.sh | tail -n 1'),
  ('cmd', 'l20', 'sleep 8; ' + HQ + ' localhost:8086/cart/'),
  ('cmd', 'l21', HQ + ' -u admin:admin localhost:8086/manager/html'),
  ('cmd', 'l22', HQ + ' -u ops:' + PW + ' localhost:8086/manager/html'),
  ('cmd', 'l23', 'echo SHUTDOWN > /dev/tcp/localhost/8096'),
  ('ui', 'u0', [(0.0, ('chrome',)), (0.55, ('key', 'ctrl+l')), (0.62, ('type', 'localhost:8086/manager/html')), (0.9, ('key', 'Return'))]),
  ('ui', 'u1', [(0.3, ('type', 'admin')), (0.45, ('key', 'Tab')), (0.5, ('type', 'admin')), (0.8, ('key', 'Return'))]),
  ('ui', 'u2', [(0.1, ('type', 'ops')), (0.2, ('key', 'Tab')), (0.25, ('type', PW)), (0.6, ('key', 'Return'))]),
  ('ui', 'u3', [(0.1, ('move', 940, 290)), (0.4, ('move', 230, 355)), (0.7, ('move', 600, 443))]),
  ('ui', 'u4', [(0.1, ('move', 30, 584)), (0.4, ('move', 600, 660)), (0.58, ('move', 1225, 565)), (0.72, ('move', 1296, 565)), (0.86, ('move', 1395, 565))]),
  ('ui', 'u5', [(0.04, ('move', 960, 600)), (0.08, ('scroll', 4)), (0.3, ('move', 740, 275)), (0.5, ('move', 780, 485)), (0.65, ('scroll', 6)), (0.84, ('park',)), (0.9, ('raise', 'xterm'))]),
  ('cmd', 'l24', 'tomcat/bin/shutdown.sh -force 2>&1 | tail -n 1'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
