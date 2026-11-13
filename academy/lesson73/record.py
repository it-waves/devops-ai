"""Record Lesson 72 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson73')
from term import *
import video as V
LD = '/home/claude/academy/lesson73'
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
 'probes': [('cmd', 'p1', "cd cloudcart"), ('cmd', 'p2', "./start.sh"), ('cmd', 'p3', "./probe.sh"), ('cmd', 'p6', "mv shop.db shop.db.off"), ('cmd', 'p7', "./probe.sh"), ('cmd', 'p10', "mv shop.db.off shop.db"), ('cmd', 'p11', "./probe.sh")],
 'errors': [('cmd', 'e1', "cd cloudcart"), ('cmd', 'e2', "./start.sh"), ('cmd', 'e4', "mv shop.db shop.db.off"), ('cmd', 'e5', "curl -s -H 'X-Request-Id: demo-42' \\\n  localhost:5000/api/products"), ('cmd', 'e7', "grep demo-42 api.log"), ('cmd', 'e9', "mv shop.db.off shop.db"), ('cmd', 'e10', "curl -s localhost:5000/api/products/2")],
 'logs': [('cmd', 'l1', "cd cloudcart"), ('cmd', 'l2', "./start.sh"), ('cmd', 'l4', "curl -s localhost:5000/api/products/2"), ('cmd', 'l5', "curl -s localhost:5000/api/products/99"), ('cmd', 'l6', "curl -s localhost:5000/api/orders"), ('cmd', 'l7', "cat api.log")],
 'metrics': [('cmd', 'm1', "cd cloudcart"), ('cmd', 'm2', "./start.sh"), ('cmd', 'm4', "./traffic.sh"), ('cmd', 'm5', "curl -s localhost:5000/metrics"), ('cmd', 'm8', "curl -s localhost:5000/metrics | grep 5xx")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
