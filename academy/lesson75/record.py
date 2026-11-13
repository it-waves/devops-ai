"""Record Lesson 75 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson75')
from term import *
import video as V
LD = '/home/claude/academy/lesson75'
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
 'start': [('cmd', 'st1', 'cd lab'), ('cmd', 'st2', 'ls'), ('cmd', 'st3', 'sudo install -m 755 lab75.sh /usr/local/sbin/'), ('cmd', 'st4', 'source shortcuts75.sh'), ('cmd', 'st5', 'lab up'), ('cmd', 'st6', 'lab check')],
 'fix1': [('cmd', 'f1', 'cd /opt/lab75'), ('cmd', 'f2', './layers.sh'), ('cmd', 'f3', 'ss -ltn'), ('cmd', 'f4', 'grep PORT app.conf'), ('cmd', 'f5', "sed -i 's/^PORT=.*/PORT=5000/' app.conf"), ('cmd', 'f6', './start.sh'), ('cmd', 'f7', './layers.sh'), ('cmd', 'f8', 'lab check')],
 'cleanup': [('cmd', 'c1', 'lab down'), ('cmd', 'c2', 'ls /opt/lab75'), ('cmd', 'c3', 'ls /opt | grep -c lab75'), ('cmd', 'c4', 'sudo rm /usr/local/sbin/lab75.sh'), ('cmd', 'c5', 'ls /usr/local/sbin | wc -l'), ('cmd', 'c5b', 'ss -ltn | grep -c 8080')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
