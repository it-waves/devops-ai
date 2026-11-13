"""Record Lesson 74 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson74')
from term import *
import video as V
LD = '/home/claude/academy/lesson74'
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
 'parts': [('cmd', 'm1', "cd cloudcart"), ('cmd', 'm2', "./start.sh"), ('cmd', 'm4', "ss -ltn"), ('cmd', 'm7', "./layers.sh")],
 'trace': [('cmd', 't1', "cd cloudcart"), ('cmd', 't2', "./start.sh"), ('cmd', 't4', "curl -s -H 'X-Request-Id: trace-1' \\\n  localhost:8080 > /dev/null"), ('cmd', 't6', "curl -s -H 'X-Request-Id: trace-1' \\\n  localhost:5000/api/products"), ('cmd', 't8', "grep trace-1 web.log api.log"), ('cmd', 't10', "python3 showdb.py")],
 'layers': [('cmd', 'y1', "cd cloudcart"), ('cmd', 'y2', "./start.sh"), ('cmd', 'y3', "./layers.sh"), ('cmd', 'y5', "./api.sh stop"), ('cmd', 'y6', "./layers.sh"), ('cmd', 'y8', "./api.sh start"), ('cmd', 'y9', "./layers.sh")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
