"""Record Lesson 107: install Tomcat in the terminal, then tour it in Chrome, one continuous screen recording. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson107')
import term
from term import *
import time, subprocess
import video as V
LD = '/home/claude/academy/lesson107'
PFX = []
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab107.sh'
def _rec(out, secs):
    return subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-draw_mouse', '1', '-framerate', '30', '-video_size', f'{term.WIN[0]}x{term.WIN[1]}', '-i', term.DISP, '-t', str(secs), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', out], env=term.E97, stdin=subprocess.PIPE)
term.rec_start = _rec
W = {}
T = [time.time()]
def wid(cls):
    o = subprocess.run(['xdotool', 'search', '--onlyvisible', '--class', cls], env=E97, capture_output=True, text=True).stdout.split()
    return o[-1] if o else None
def raise_(name):
    i = W[name]; o = W.get('chrome' if name == 'xterm' else 'xterm')
    xt('windowraise', i); xt('windowfocus', i)
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
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; pkill -9 -f "unshare -mpfu"; pkill -9 -f "[u]sr/lib/systemd/systemd --system"; rm -f /home/student/.ready; true', shell=True); time.sleep(1.5)
    bp = subprocess.Popen(['setsid', 'unshare', '-mpfu', 'sh', LD + '/boot.sh'], stdout=open('/tmp/boot107.log', 'w'), stderr=subprocess.STDOUT)
    for _ in range(120):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(3)
    pid = subprocess.run("pgrep -P $(pgrep -f '[u]nshare -mpfu sh .*boot.sh' | head -n1) | head -n1", shell=True, capture_output=True, text=True).stdout.strip()
    for _ in range(60):
        pid = subprocess.run("pgrep -P $(pgrep -f '[u]nshare -mpfu sh .*boot.sh' | head -n1) | head -n1", shell=True, capture_output=True, text=True).stdout.strip()
        if pid and open('/proc/%s/comm' % pid).read().strip() == 'systemd': break
        time.sleep(1)
    time.sleep(2)
    NS = ['nsenter', '-t', pid, '-m', '-p', '-u', '-r', '-w', '--']
    for _ in range(60):
        o = subprocess.run(NS + ['systemctl', 'is-system-running'], capture_output=True, text=True).stdout.strip()
        if o in ('running', 'degraded'): break
        time.sleep(2)
    subprocess.run(NS + ['sh', '-c', 'LAB107_TOMCAT_BASE=file:///opt/dist SUDO_USER=student sh /usr/local/sbin/lab107.sh up'], stdout=open('/tmp/lab107up.log', 'w'), stderr=subprocess.STDOUT)
    PFX[:] = NS
    p = xterm_start(PFX); term.WIN[:] = [1080, 600]; focus()
    time.sleep(2); key('ctrl+l'); time.sleep(0.4)
    W['xterm'] = wid('xterm')
    if not W['xterm']:
        print('DBG pid', pid, NS, flush=True); subprocess.run('ps aux | grep -E "xterm|nsenter" | head -n 5', shell=True); raise SystemExit('xterm window missing: aborting this take')
    ch = None
    raise_('xterm'); mv(1078, 596); time.sleep(0.5); focus(); key('ctrl+l')
    fx = subprocess.Popen(['python3', '/home/claude/academy/common/cursorfx.py'], env=E97); time.sleep(1)
    r = Run(LD, V, scene, delay=80); T[0] = r.T0
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        else: ui(r, st[1], st[2])
    r.end(); p.terminate(); fx.terminate(); time.sleep(0.5)
    subprocess.run(NS + ['sh', '-c', 'sh /usr/local/sbin/lab107.sh down >/dev/null 2>&1'])
    subprocess.run('pkill -u student; pkill -f user-data-dir=/tmp/chp; pkill -f cursorfx.py; pkill -f "systemd --system"; pkill -f catalina.base; true', shell=True)
HQ = "curl -s -o /dev/null -w '%{http_code}\\n' localhost:8081"
MP = "$(systemctl show -p MainPID --value tomcat107)"
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab107'),
  ('cmd', 'l1', 'ls'),
  ('cmd', 'l2', "sudo grep -n 'Connector port' tomcat/conf/server.xml"),
  ('cmd', 'l3', 'sudo -u tomcat vim tomcat/bin/setenv.sh'),
  ('ui', 'l3b', [(0.3, ('type', 'i'))]),
  ('ui', 'l3c', [(0.02, ('type', 'export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64\n')), (0.3, ('type', 'export CATALINA_PID=/opt/lab107/tomcat/temp/tomcat.pid\n')), (0.55, ('type', 'export CATALINA_OPTS="-Xmx256m -Dhttp.port=8081 -Dcloudcart.env=staging"')), (0.9, ('key', 'Escape')), (0.94, ('type', ':wq\n'))]),
  ('cmd', 'l4', 'sudo cat tomcat/bin/setenv.sh'),
  ('cmd', 'l5', 'sudo vim /etc/systemd/system/tomcat107.service'),
  ('ui', 'l5b', [(0.05, ('type', 'i')), (0.2, ('type', '[Unit]\nDescription=Tomcat for lab 107\nAfter=network.target\n'))]),
  ('ui', 'l5c', [(0.02, ('type', '\n[Service]\nType=forking\nUser=tomcat\nGroup=tomcat\nPIDFile=/opt/lab107/tomcat/temp/tomcat.pid\nExecStart=/opt/lab107/tomcat/bin/startup.sh\nExecStop=/opt/lab107/tomcat/bin/shutdown.sh\n'))]),
  ('ui', 'l5d', [(0.1, ('type', 'Restart=on-failure\nRestartSec=3\n'))]),
  ('ui', 'l5e', [(0.05, ('type', '\n[Install]\nWantedBy=multi-user.target')), (0.85, ('key', 'Escape')), (0.9, ('type', ':wq\n'))]),
  ('cmd', 'l6', 'sudo systemctl daemon-reload'),
  ('cmd', 'l7', 'sudo systemctl enable --now tomcat107'),
  ('cmd', 'l8', 'sleep 10; systemctl status tomcat107 --no-pager | head -n 6'),
  ('cmd', 'l9', HQ),
  ('cmd', 'l10', 'ps -o user,pid,comm -C java'),
  ('cmd', 'l11', "sudo grep -o -- '-Dcloudcart[^ ]*' tomcat/logs/catalina.out"),
  ('ui', 'u0', [(0.0, ('chrome',)), (0.6, ('key', 'ctrl+l')), (0.7, ('type', 'localhost:8081')), (0.92, ('key', 'Return'))]),
  ('ui', 'u1', [(0.3, ('move', 540, 200)), (0.7, ('move', 540, 130))]),
  ('ui', 'u2', [(0.1, ('key', 'ctrl+l')), (0.2, ('type', 'localhost:8080')), (0.4, ('key', 'Return')), (0.8, ('raise', 'xterm')), (0.9, ('park',))]),
  ('cmd', 'l12', 'systemctl show -p MainPID tomcat107'),
  ('cmd', 'l13', 'sudo kill -9 ' + MP),
  ('cmd', 'l14', 'sleep 10; systemctl show -p MainPID,NRestarts tomcat107'),
  ('cmd', 'l15', HQ),
  ('cmd', 'l16', "sudo journalctl -u tomcat107 --no-pager | grep -oE 'Main process exited.*|Scheduled restart.*'"),
  ('cmd', 'l17', 'sudo systemctl stop tomcat107'),
  ('cmd', 'l18', 'systemctl is-enabled tomcat107'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
