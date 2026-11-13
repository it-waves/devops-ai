"""Record Lesson 81 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson81')
from term import *
import video as V
LD = '/home/claude/academy/lesson81'
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
 'trace': [('cmd', 't0', 'cd shop'), ('cmd', 't1', 'javac -d out src/com/cloudcart/Checkout.java'), ('cmd', 't2', 'java -cp out com.cloudcart.Checkout'), ('cmd', 't3', 'echo $?'), ('cmd', 't4', "java -cp out com.cloudcart.Checkout 2>&1 | grep -n 'Caused by'")],
 'logs': [('cmd', 'l0', 'cd shop'), ('cmd', 'l1', 'tail -n 5 app.log'), ('cmd', 'l2', 'grep -c ERROR app.log'), ('cmd', 'l3', 'grep ERROR app.log'), ('cmd', 'l4', 'grep -A2 ERROR app.log'), ('cmd', 'l5', 'grep WARN app.log')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
