"""Record Lesson 115: start CloudCart on Tomcat, then a full screen browser tour. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson115')
import term
term.XSIZE = '1920x1080'
from term import *
import time, subprocess
import video as V
LD = '/home/claude/academy/lesson115'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab115.sh'
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
        raise_(a[1])
        if a[1] == 'xterm': time.sleep(0.4); focus()
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
    subprocess.run(f'LAB115_TOMCAT_BASE=file:///opt/dist LAB115_WAR_URL=file:///home/claude/devops-ai/academy/lab/assets/cloudcart-0.2.0.war SUDO_USER=student sh {LAB} up > /tmp/lab115up.log 2>&1', shell=True)
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
sys.path.insert(0, LD)
from tour import TOUR1, TOUR2
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab115'),
  ('cmd', 'l1', 'ls'),
  ('cmd', 'l2', 'ls tomcat/webapps'),
  ('cmd', 'l3', 'tomcat/bin/startup.sh | tail -n 1'),
  ('cmd', 'l4', 'sleep 6; curl -si localhost:8089/cloudcart/ | head -n 1'),
 ] + [('ui', cid, acts) for cid, acts in TOUR1] + [
  ('cmd', 't1', 'cp cloudcart-0.2.0.war tomcat/webapps/cloudcart.war'),
  ('cmd', 't2', 'sleep 10; ls tomcat/webapps'),
 ] + [('ui', cid, acts) for cid, acts in TOUR2] + [
  ('cmd', 'e1', 'ls tomcat/webapps'),
  ('cmd', 'e2', 'tomcat/bin/shutdown.sh | tail -n 1'),
  ('cmd', 'e3', 'ss -ltn | grep -c 8089'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
