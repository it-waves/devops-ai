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
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; true', shell=True); time.sleep(0.8)
    p = xterm_start(PFX); focus()
    for _ in range(240):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(3)
    W['xterm'] = wid('xterm')
    subprocess.run('rm -rf /tmp/chp', shell=True)
    ch = subprocess.Popen(['google-chrome', '--no-sandbox', '--incognito', '--user-data-dir=/tmp/chp', '--no-first-run', '--no-default-browser-check', '--disable-gpu', '--disable-infobars', '--test-type', '--window-position=0,0', f'--window-size={term.WIN[0]},{term.WIN[1]}', 'about:blank'], env=E97, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(6); W['chrome'] = wid('google-chrome') or wid('chromium') or wid('Google-chrome')
    raise_('chrome'); xt('key', 'ctrl+l'); typ('localhost:8081/#/login', 40); key('Return'); time.sleep(5); key('ctrl+minus'); time.sleep(0.5); key('ctrl+minus'); time.sleep(1); key('ctrl+l'); typ('about:blank', 40); key('Return'); time.sleep(1.5)
    mv(1078, 596); raise_('chrome')
    r = Run(LD, V, scene, delay=80); T[0] = r.T0
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        else: ui(r, st[1], st[2])
    r.end(); p.terminate(); ch.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; true', shell=True)
PW1 = open('/tmp/nx/sonatype-work/nexus3/admin.password').read().strip()
PW2 = 'Corp-7q4m2-Nexus1'
DEP = "mvn -B -s settings.xml deploy | grep -o 'corp-[a-z]*/.*jar' | sort -u"
def _create(first, name, snap):
    pass
STAGES = {
 'deploy': [
  ('ui', 'u0', [(0.1, ('key', 'ctrl+l')), (0.25, ('type', 'localhost:8081')), (0.8, ('key', 'Return'))]),
  ('ui', 'u1', [(0.3, ('click', 540, 465)), (0.36, ('type', 'admin')), (0.45, ('key', 'Tab')), (0.5, ('type', PW1)), (0.92, ('key', 'Return'))]),
  ('ui', 'u2', [(0.04, ('click', 719, 531)), (0.3, ('click', 540, 314)), (0.34, ('type', PW2)), (0.55, ('click', 540, 380)), (0.6, ('type', PW2)), (0.9, ('click', 738, 531))]),
  ('ui', 'u3', [(0.08, ('key', 'ctrl+l')), (0.14, ('type', 'localhost:8081/#/login')), (0.3, ('key', 'Return')), (0.5, ('click', 540, 384)), (0.57, ('type', 'admin')), (0.65, ('key', 'Tab')), (0.7, ('type', PW2)), (0.95, ('key', 'Return'))]),
  ('ui', 'u4', [(0.2, ('click', 719, 531)), (0.8, ('click', 738, 531))]),
  ('ui', 'u5', [(0.5, ('click', 338, 481)), (0.85, ('click', 738, 531))]),
  ('ui', 'u6', [(0.8, ('click', 737, 531))]),
  ('ui', 'u7', [(0.08, ('move', 540, 400)), (0.12, ('scroll', 6)), (0.5, ('click', 338, 483)), (0.9, ('click', 733, 531))]),
  ('ui', 't1', [(0.3, ('move', 23, 160)), (0.42, ('move', 23, 194)), (0.54, ('move', 23, 227)), (0.64, ('move', 23, 261)), (0.74, ('move', 23, 294)), (0.88, ('move', 23, 380))]),
  ('ui', 't2', [(0.15, ('click', 815, 109)), (0.35, ('click', 887, 303)), (0.6, ('click', 23, 348)), (0.85, ('click', 123, 247))]),
  ('ui', 't3', [(0.2, ('move', 330, 222)), (0.38, ('move', 415, 222)), (0.55, ('move', 500, 222)), (0.7, ('move', 680, 222)), (0.88, ('move', 775, 248))]),
  ('ui', 't4', [(0.25, ('move', 415, 301)), (0.55, ('move', 415, 248)), (0.8, ('move', 415, 275))]),
  ('ui', 't5', [(0.15, ('move', 380, 248)), (0.4, ('move', 380, 275)), (0.62, ('move', 380, 301)), (0.8, ('move', 380, 327))]),
  ('ui', 'r1', [(0.04, ('click', 335, 191)), (0.35, ('move', 660, 400)), (0.4, ('scroll', 5)), (0.85, ('click', 350, 326))]),
  ('ui', 'r2', [(0.05, ('click', 652, 223)), (0.1, ('type', 'corp-snapshots')), (0.5, ('click', 610, 356)), (0.75, ('click', 323, 396))]),
  ('ui', 'r3', [(0.03, ('move', 660, 450)), (0.06, ('scroll', 3)), (0.35, ('click', 610, 399)), (0.5, ('click', 345, 418)), (0.62, ('scroll', 12)), (0.85, ('click', 339, 560))]),
  ('ui', 'r4', [(0.03, ('click', 335, 191)), (0.28, ('move', 660, 400)), (0.31, ('scroll', 5)), (0.6, ('click', 350, 326)), (0.78, ('click', 652, 223)), (0.82, ('type', 'corp-releases'))]),
  ('ui', 'r5', [(0.05, ('move', 610, 356)), (0.3, ('move', 660, 450)), (0.33, ('scroll', 3)), (0.6, ('move', 610, 399)), (0.72, ('scroll', 12)), (0.9, ('click', 339, 560))]),
  ('ui', 'r6', [(0.4, ('move', 777, 248)), (0.6, ('move', 777, 274)), (0.97, ('raise', 'xterm')), (0.98, ('park',))]),
  ('cmd', 'd0', 'cd demo'), ('cmd', 'd1', 'sed -n 12,21p pom.xml'), ('cmd', 'd2', 'export NEXUS_PASS=$(cat ~/.corp-pass)'),
  ('cmd', 'd3', "mvn -B -s settings.xml deploy | grep -o 'corp-[a-z]*/.*jar' | sort -u"), ('cmd', 'd4', "mvn -B -s settings.xml deploy | grep -o 'corp-[a-z]*/.*jar' | sort -u"),
  ('cmd', 'd5', "sed -i 's/-SNAPSHOT//' pom.xml; grep -m1 '<version>' pom.xml"),
  ('cmd', 'd6', "mvn -B -s settings.xml deploy | grep -o 'corp-[a-z]*/.*jar' | sort -u"),
  ('cmd', 'd7', "mvn -B -s settings.xml deploy | grep -o 'status code.*'"),
  ('ui', 'v0', [(0.02, ('raise', 'chrome')), (0.3, ('move', 23, 227)), (0.6, ('click', 23, 227))]),
  ('ui', 'v1', [(0.5, ('click', 610, 268))]),
  ('ui', 'v2', [(0.3, ('click', 108, 280)), (0.8, ('click', 126, 324))]),
  ('ui', 'v3', [(0.5, ('click', 270, 346))]),
  ('ui', 'v3b', [(0.1, ('move', 860, 450)), (0.15, ('scroll', 9))]),
  ('ui', 'v4', [(0.05, ('click', 23, 227)), (0.35, ('click', 610, 247)), (0.7, ('click', 108, 282))]),
  ('ui', 'x1', [(0.9, ('park',))]),
  ('ui', 'x2', [(0.1, ('click', 23, 348)), (0.3, ('click', 123, 247)), (0.55, ('click', 360, 327)), (0.75, ('move', 660, 450)), (0.8, ('scroll', 6))]),
  ('ui', 'x3', [(0.5, ('raise', 'xterm')), (0.55, ('park',))]),
  ('cmd', 'x3', 'sed -n 1,10p settings-mirror.xml'),
  ('cmd', 'x4', 'mvn -B -s settings-mirror.xml -Dmaven.repo.local=/tmp/m2x package | grep -c Downloaded'),
  ('ui', 'x5', [(0.02, ('raise', 'chrome')), (0.2, ('click', 23, 227)), (0.45, ('click', 610, 290))]),
  ('ui', 'x6', [(0.9, ('park',))]),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
