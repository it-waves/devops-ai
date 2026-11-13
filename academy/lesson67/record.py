"""Record Lesson 67 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson67')
from term import *
import video as V
LD = '/home/claude/academy/lesson67'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'mono': [('cmd', 'm1', 'cd cloudcart'), ('cmd', 'm2', 'ls'), ('cmd', 'm3', './start.sh mono'), ('cmd', 'm4', 'curl -s localhost:8080 | head -4'), ('cmd', 'm5', 'curl -s localhost:8080/api/products | jq -c ".[]"'), ('cmd', 'm7', 'python3 showdb.py'), ('cmd', 'm8', 'ss -ltn')],
 'split': [('cmd', 'p0', 'cd cloudcart'), ('cmd', 'p1', './start.sh split'), ('cmd', 'p2', 'ss -ltn'), ('cmd', 'p3', 'curl -s localhost:5000/api/products | jq -c ".[0]"'), ('cmd', 'p4', 'curl -s localhost:8080 | grep 5000'), ('cmd', 'p5', './stop.sh')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
