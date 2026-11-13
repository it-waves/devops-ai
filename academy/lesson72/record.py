"""Record Lesson 72 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson72')
from term import *
import video as V
LD = '/home/claude/academy/lesson72'
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
 'memory': [('cmd', 'a1', "cd cloudcart"), ('cmd', 'a2', "./start.sh"), ('cmd', 'a3', "curl -s -X POST localhost:5000/api/cart/1"), ('cmd', 'a5', "curl -s localhost:5000/api/cart"), ('cmd', 'a7', "./start.sh"), ('cmd', 'a8', "curl -s localhost:5000/api/cart")],
 'scale': [('cmd', 'b1', "cd cloudcart"), ('cmd', 'b2', "./start.sh"), ('cmd', 'b3', "./second.sh"), ('cmd', 'b5', "curl -s -X POST localhost:5000/api/cart/1"), ('cmd', 'b7', "curl -s localhost:5001/api/cart")],
 'db': [('cmd', 'c1', "cd cloudcart"), ('cmd', 'c2', "STORAGE=db ./start.sh"), ('cmd', 'c3', "STORAGE=db ./second.sh"), ('cmd', 'c4', "curl -s -X POST localhost:5000/api/cart/2"), ('cmd', 'c6', "curl -s localhost:5001/api/cart"), ('cmd', 'c8', "STORAGE=db ./start.sh"), ('cmd', 'c9', "curl -s localhost:5000/api/cart"), ('cmd', 'c11', "ls -l shop.db")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
