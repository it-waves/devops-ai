"""Record Lesson 84 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson84')
from term import *
import video as V
LD = '/home/claude/academy/lesson84'
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
 'start': [('cmd', 'st1', 'cd lab'), ('cmd', 'st2', 'ls'), ('cmd', 'st3', 'sudo install -m 755 lab84.sh /usr/local/sbin/'), ('cmd', 'st4', 'source shortcuts84.sh'), ('cmd', 'st5', 'lab up'), ('cmd', 'st6', 'lab check')],
 'fix1': [('cmd', 'f1', 'cd /opt/lab84'), ('cmd', 'f2', 'sh build.sh'), ('cmd', 'f3', 'grep -n SHIPPING src/cloudcart/Orders.java'), ('cmd', 'f4', "sed -i 's/- SHIPPING/+ SHIPPING/' src/cloudcart/Orders.java"), ('cmd', 'f5', 'sh build.sh'), ('cmd', 'f6', 'sh run-orders.sh'), ('cmd', 'f7', 'head -2 logs/orders.log'), ('cmd', 'f8', 'lab check')],
 'cleanup': [('cmd', 'c1', 'lab down'), ('cmd', 'c2', 'ls /opt/lab84'), ('cmd', 'c3', 'ls /opt | grep -c lab84'), ('cmd', 'c4', 'sudo rm /usr/local/sbin/lab84.sh'), ('cmd', 'c5', 'ls /usr/local/sbin | wc -l'), ('cmd', 'c5b', 'pgrep -c java')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
