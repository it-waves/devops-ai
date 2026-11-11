"""Record Lesson 43 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson43')
from term import *
import video as V
LD = '/home/claude/academy/lesson43'
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
 'secrets': [('cmd', 'se1', 'cat bad.sh'), ('cmd', 'se2', 'ls -l .env'), ('cmd', 'se3', 'chmod 600 .env'), ('cmd', 'se4', 'ls -l .env'), ('cmd', 'se5', 'cat good.sh'), ('cmd', 'se6', 'bash good.sh')],
 'perms': [('cmd', 'pe1', 'ls -l deploy.sh'), ('cmd', 'pe2', './deploy.sh'), ('cmd', 'pe3', 'chmod u+x deploy.sh'), ('cmd', 'pe4', 'ls -l deploy.sh'), ('cmd', 'pe5', './deploy.sh'), ('cmd', 'pe6', 'umask 077; touch priv.txt; ls -l priv.txt')],
 'validate': [('cmd', 'va1', 'cat validate.sh'), ('cmd', 'va2', 'bash validate.sh web01'), ('cmd', 'va3', 'bash validate.sh "web01; rm -rf /"'), ('cmd', 'va4', 'echo $?'), ('cmd', 'va5', 'bash validate.sh ../etc')],
 'inject': [('cmd', 'in1', 'cat danger.sh'), ('cmd', 'in2', 'bash danger.sh "app.log; echo INJECTED"'), ('cmd', 'in3', 'cat quoted.sh'), ('cmd', 'in4', 'bash quoted.sh "app.log; echo INJECTED"')],
 'build': [('cmd', 'bu1', 'cat secure.sh'), ('cmd', 'bu2', 'bash secure.sh web01'), ('cmd', 'bu3', 'bash secure.sh "web01; id"'), ('cmd', 'bu4', 'echo $?')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
