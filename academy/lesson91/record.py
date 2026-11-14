"""Record Lesson 91 live demo: a browser (repository web page) and a terminal in one continuous recording. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson91')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson91'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def _rec(out, secs):
    return subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-draw_mouse', '1', '-framerate', '30', '-video_size', f'{term.WIN[0]}x{term.WIN[1]}', '-i', term.DISP, '-t', str(secs), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '15', '-pix_fmt', 'yuv420p', out], env=term.E97, stdin=subprocess.PIPE)
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
    elif k == 'scroll':
        for _ in range(a[1]): xt('click', 5); time.sleep(0.35)
    elif k == 'raise': raise_(a[1])
    elif k == 'park': mv(1078, 596)
def ui(r, cid, acts):
    tot = r.dur[cid] + V.EXTRA.get(cid, 0)
    for f, a in acts:
        r.at(cid, f * tot)
        do_action(a)
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f "srv.py"; true', shell=True); time.sleep(0.8)
    p = xterm_start(PFX); focus()
    for _ in range(240):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(3)
    W['xterm'] = wid('xterm')
    subprocess.run('rm -rf /tmp/chp', shell=True)
    ch = subprocess.Popen(['google-chrome', '--no-sandbox', '--incognito', '--user-data-dir=/tmp/chp', '--no-first-run', '--no-default-browser-check', '--disable-gpu', '--disable-infobars', '--window-position=0,0', f'--window-size={term.WIN[0]},{term.WIN[1]}', 'about:blank'], env=E97, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(6); W['chrome'] = wid('google-chrome') or wid('chromium') or wid('Google-chrome')
    mv(1078, 596); raise_('chrome')
    r = Run(LD, V, scene, delay=80); T[0] = r.T0
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        else: ui(r, st[1], st[2])
    r.end(); p.terminate(); ch.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f srv.py; true', shell=True)
PASSW = 'corp-7q4m2'
STAGES = {
 'deploy': [
  ('ui', 'u0', [(0.22, ('key', 'ctrl+l')), (0.3, ('type', 'localhost:8082/ui')), (0.8, ('key', 'Return'))]),
  ('ui', 'u1', [(0.12, ('type', 'dev')), (0.3, ('key', 'Tab')), (0.4, ('type', PASSW)), (0.82, ('key', 'Return'))]),
  ('ui', 'u2', [(0.9, ('move', 165, 245)), (0.95, ('click', 165, 245))]),
  ('ui', 'u3', [(0.22, ('type', 'corp-snapshots')), (0.5, ('click', 44, 397)), (0.8, ('click', 44, 492))]),
  ('ui', 'u4', [(0.12, ('click', 165, 535)), (0.55, ('click', 165, 245))]),
  ('ui', 'u5', [(0.2, ('type', 'corp-releases')), (0.5, ('click', 44, 365)), (0.78, ('click', 44, 460))]),
  ('ui', 'u6', [(0.05, ('click', 165, 535)), (0.45, ('move', 250, 385)), (0.7, ('move', 730, 385)), (0.97, ('raise', 'xterm')), (0.98, ('park',))]),
  ('cmd', 'd0', 'cd demo'), ('cmd', 'd1', 'sed -n 11,22p pom.xml'), ('cmd', 'd2', 'export REPO_PASS=$(cat ~/.corp-pass)'),
  ('cmd', 'd3', "mvn -B -q deploy; find ~/store/corp-snapshots -name '*.jar' -printf '%f\\n'"),
  ('cmd', 'd4', "mvn -B -q deploy; find ~/store/corp-snapshots -name '*.jar' -printf '%f\\n'"),
  ('cmd', 'd5', "sed -i 's/-SNAPSHOT//' pom.xml; grep -m1 '<version>' pom.xml"),
  ('cmd', 'd6', "mvn -B -q deploy; find ~/store/corp-releases -name '*.jar' -printf '%f\\n'"),
  ('cmd', 'd7', "mvn -B deploy 2>&1 | grep -o 'status code.*'"),
  ('ui', 'v0', [(0.02, ('raise', 'chrome')), (0.2, ('move', 499, 120)), (0.6, ('click', 499, 120))]),
  ('ui', 'v1', [(0.7, ('click', 90, 534))]),
  ('ui', 'v2', [(0.7, ('click', 725, 339))]),
  ('ui', 'v3', [(0.55, ('scroll', 3))]),
  ('ui', 'v4', [(0.02, ('key', 'Home')), (0.1, ('click', 499, 120)), (0.3, ('click', 570, 534)), (0.55, ('click', 800, 339))]),
  ('ui', 'v5', [(0.3, ('click', 628, 120))]),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
