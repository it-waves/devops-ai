"""Record Lesson 93 live demo: a terminal and a browser (real Nexus) in one continuous recording. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson93')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson93'
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
ANCH = [0, 0]
def click(x, y): mv(x, y); time.sleep(0.45); xt('click', 1)
def do_action(a):
    k = a[0]; print(round(time.time() - T[0], 1), a, flush=True)
    if k == 'type': typ(a[1], 80)
    elif k == 'key': key(a[1])
    elif k == 'click': click(a[1], a[2])
    elif k == 'move': mv(a[1], a[2])
    elif k == 'scroll':
        for _ in range(a[1]): xt('click', 5); time.sleep(0.35)
    elif k == 'find':
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-video_size', f'{term.WIN[0]}x{term.WIN[1]}', '-i', term.DISP, '-frames:v', '1', '/tmp/find.png'], env=term.E97)
        import cv2
        im = cv2.imread('/tmp/find.png', 0); tp = cv2.imread(LD + '/tpl/' + a[1] + '.png', 0)
        _, mx, _, loc = cv2.minMaxLoc(cv2.matchTemplate(im, tp, cv2.TM_CCOEFF_NORMED))
        if mx < 0.75: print('WARN find', a[1], round(mx, 2), 'using default', a[2], a[3], flush=True); click(a[2], a[3])
        else: click(loc[0] + tp.shape[1] // 2, loc[1] + tp.shape[0] // 2)
    elif k == 'f':
        import cv2
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-video_size', f'{term.WIN[0]}x{term.WIN[1]}', '-i', term.DISP, '-frames:v', '1', '/tmp/find.png'], env=term.E97)
        im = cv2.imread('/tmp/find.png', 0); tp = cv2.imread(LD + '/tpl/' + a[1] + '.png', 0)
        _, mx, _, loc = cv2.minMaxLoc(cv2.matchTemplate(im, tp, cv2.TM_CCOEFF_NORMED))
        if mx < 0.75: print('WARN find', a[1], round(mx, 2), 'using default', a[5], a[6], flush=True); cx, cy = a[5] - a[3], a[6] - a[4]
        else: cx, cy = loc[0] + tp.shape[1] // 2, loc[1] + tp.shape[0] // 2
        ANCH[:] = [cx, cy]; (click if a[2] == 'click' else mv)(cx + a[3], cy + a[4])
    elif k == 'r': (click if a[1] == 'click' else mv)(ANCH[0] + a[2], ANCH[1] + a[3])
    elif k == 'ensure':
        import cv2
        click(a[1], a[2]); time.sleep(0.7)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-video_size', f'{term.WIN[0]}x{term.WIN[1]}', '-i', term.DISP, '-frames:v', '1', '/tmp/find.png'], env=term.E97)
        im = cv2.imread('/tmp/find.png', 0); tp = cv2.imread(LD + '/tpl/list.png', 0)
        mx = cv2.minMaxLoc(cv2.matchTemplate(im, tp, cv2.TM_CCOEFF_NORMED))[1]
        print('list match', round(mx, 2), flush=True)
        if mx < 0.6: click(992, a[2])
    elif k == 'raise': raise_(a[1])
    elif k == 'park': mv(1078, 596)
def ui(r, cid, acts):
    tot = r.dur[cid] + V.EXTRA.get(cid, 0)
    for f, a in acts:
        r.at(cid, f * tot)
        do_action(a)
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; true', shell=True); time.sleep(0.8)
    if not os.environ.get('NOPREP'): subprocess.run('sh /home/claude/academy/lesson93_prep.sh', shell=True, check=True)
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
    mv(1078, 596); raise_('xterm')
    fx = subprocess.Popen(['python3', '/home/claude/academy/common/cursorfx.py'], env=E97); time.sleep(1)
    r = Run(LD, V, scene, delay=80); T[0] = r.T0
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        else: ui(r, st[1], st[2])
    r.end(); p.terminate(); ch.terminate(); fx.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; true', shell=True)
PW = 'Corp-7q4m2-Nexus1'
STAGES = {
 'live': [
  ('cmd', 'l0', 'cd demo'), ('cmd', 'l1', 'export NEXUS_PASS=$(cat ~/.corp-pass)'), ('cmd', 'l2', "for n in 1 2 3 4; do mvn -B -s settings.xml deploy | grep -o 'cart-core-[0-9.]*-[0-9.]*-[0-9]*.jar' | sort -u; done"),
  ('ui', 'u0', [(0.02, ('raise', 'chrome')), (0.25, ('key', 'ctrl+l')), (0.4, ('type', 'localhost:8081')), (0.85, ('key', 'Return'))]),
  ('ui', 'u1', [(0.15, ('click', 540, 384)), (0.3, ('type', 'admin')), (0.45, ('key', 'Tab')), (0.5, ('type', PW)), (0.93, ('key', 'Return'))]),
  ('ui', 'u2', [(0.04, ('click', 719, 531)), (0.2, ('click', 738, 531)), (0.4, ('move', 540, 400)), (0.44, ('scroll', 6)), (0.66, ('click', 338, 483)), (0.8, ('click', 733, 531)), (0.94, ('click', 733, 531))]),
  ('ui', 't2', [(0.2, ('click', 815, 109)), (0.55, ('click', 887, 303))]),
  ('ui', 't3', [(0.2, ('move', 23, 194)), (0.38, ('move', 23, 227)), (0.55, ('move', 23, 261)), (0.75, ('move', 23, 348))]),
  ('ui', 'v0', [(0.2, ('move', 23, 227)), (0.6, ('click', 23, 227))]),
  ('ui', 'v1', [(0.3, ('click', 610, 247))]),
  ('ui', 'v2', [(0.1, ('click', 108, 281)), (0.4, ('move', 150, 303)), (0.52, ('move', 150, 324)), (0.64, ('move', 150, 346)), (0.76, ('move', 150, 367))]),
  ('ui', 's1', [(0.2, ('click', 23, 348)), (0.7, ('click', 119, 273))]),
  ('ui', 's2', [(0.25, ('move', 663, 355)), (0.6, ('move', 795, 355))]),
  ('ui', 'k1', [(0.1, ('click', 150, 566)), (0.35, ('move', 150, 400)), (0.4, ('scroll', 4)), (0.78, ('find', 'tasks', 103, 520))]),
  ('ui', 'k2', [(0.1, ('move', 318, 222)), (0.25, ('move', 490, 222)), (0.4, ('move', 595, 222)), (0.5, ('move', 678, 222)), (0.6, ('move', 760, 222)), (0.72, ('move', 910, 222)), (0.85, ('move', 1015, 222))]),
  ('ui', 'k3', [(0.05, ('click', 318, 191)), (0.4, ('click', 990, 220)), (0.52, ('type', 'SNAPSHOT'))]),
  ('ui', 'k4', [(0.4, ('click', 380, 276))]),
  ('ui', 'k5', [(0.4, ('click', 600, 289)), (0.55, ('type', 'Delete old snapshots'))]),
  ('ui', 'k6', [(0.3, ('move', 600, 355))]),
  ('ui', 'k7', [(0.25, ('click', 912, 487)), (0.7, ('click', 332, 526))]),
  ('ui', 'k8', [(0.1, ('move', 650, 300)), (0.15, ('scroll', 4)), (0.6, ('move', 600, 231))]),
  ('ui', 'k9', [(0.3, ('f', 'ret', 'click', 134, 42, 366, 241)), (0.4, ('key', 'ctrl+a')), (0.5, ('type', '0'))]),
  ('ui', 'k10', [(0.4, ('f', 'rem', 'move', -64, 22, 354, 306))]),
  ('ui', 'k11', [(0.25, ('f', 'freq', 'click', 160, 0, 440, 501)), (0.5, ('r', 'move', -130, -120)), (0.6, ('r', 'move', -130, -81)), (0.7, ('r', 'move', -130, -42)), (0.8, ('r', 'move', -110, -22))]),
  ('ui', 'k12', [(0.5, ('r', 'click', -135, -81))]),
  ('ui', 'k13', [(0.06, ('move', 650, 400)), (0.1, ('scroll', 4)), (0.25, ('f', 'cancel', 'move', 0, 0, 398, 575)), (0.38, ('r', 'click', 514, -45)), (0.58, ('r', 'click', -92, -130)), (0.82, ('r', 'click', -76, 0))]),
  ('ui', 'k14', [(0.3, ('move', 678, 298)), (0.55, ('move', 760, 298))]),
  ('ui', 'r1', [(0.2, ('click', 340, 298)), (0.65, ('click', 396, 190))]),
  ('ui', 'r2', [(0.5, ('click', 507, 380))]),
  ('ui', 'r3', [(0.12, ('move', 352, 350)), (0.55, ('click', 983, 109))]),
  ('ui', 'r4', [(0.15, ('click', 326, 155)), (0.5, ('move', 920, 298)), (0.8, ('move', 1015, 298))]),
  ('ui', 'p1', [(0.1, ('click', 23, 227)), (0.6, ('click', 610, 247))]),
  ('ui', 'p2', [(0.1, ('click', 108, 281)), (0.5, ('move', 150, 303))]),
  ('ui', 'p3', [(0.2, ('click', 23, 348)), (0.7, ('click', 119, 273))]),
  ('ui', 'p4', [(0.2, ('move', 663, 355)), (0.35, ('move', 795, 355)), (0.7, ('move', 400, 420)), (0.93, ('raise', 'xterm')), (0.96, ('park',))]),
  ('cmd', 'y1', "curl -s -u admin:$NEXUS_PASS 'localhost:8081/service/rest/v1/search/assets?repository=corp-snapshots&maven.extension=jar' | grep -c '\"path\"'"), ('cmd', 'y2', "curl -s -u admin:$NEXUS_PASS localhost:8081/service/rest/v1/tasks | grep -A9 'Delete old' | grep -E 'Result|nextRun|schedule'"),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
