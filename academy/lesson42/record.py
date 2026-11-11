"""Record Lesson 42 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson42')
from term import *
import video as V
LD = '/home/claude/academy/lesson42'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True)
STAGES = {
 'exitcodes': [('cmd', 'e1', 'ls /etc/hostname'), ('cmd', 'e2', 'echo $?'), ('cmd', 'e3', 'ls /nope'), ('cmd', 'e4', 'echo $?'), ('cmd', 'e5', 'cat check.sh'), ('cmd', 'e6', 'bash check.sh'), ('cmd', 'e7', 'echo $?')],
 'strict': [('cmd', 's1', 'cat loose.sh'), ('cmd', 's2', 'bash loose.sh'), ('cmd', 's3', 'cat strict.sh'), ('cmd', 's4', 'bash strict.sh'), ('cmd', 's5', 'echo $?'), ('cmd', 's6', 'cat unset.sh'), ('cmd', 's7', 'bash unset.sh')],
 'trap': [('cmd', 't1', 'cat trap.sh'), ('cmd', 't2', 'bash trap.sh'), ('cmd', 't3', 'echo $?'), ('cmd', 't4', 'ls /tmp')],
 'logging': [('cmd', 'l1', 'cat log.sh'), ('cmd', 'l2', 'bash log.sh'), ('cmd', 'l3', 'bash log.sh 2> run.log'), ('cmd', 'l4', 'cat run.log')],
 'build': [('cmd', 'w1', 'cat safe.sh'), ('cmd', 'w2', 'bash safe.sh'), ('cmd', 'w3', 'echo $?')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
