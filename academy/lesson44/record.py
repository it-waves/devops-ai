"""Record Lesson 44 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson44')
from term import *
import video as V
LD = '/home/claude/academy/lesson44'
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
 'idem': [('cmd', 'id1', 'cat bad.sh'), ('cmd', 'id2', 'bash bad.sh'), ('cmd', 'id3', 'bash bad.sh'), ('cmd', 'id4', 'cat app.conf')],
 'fix': [('cmd', 'g1', 'cat good.sh'), ('cmd', 'g2', 'bash good.sh'), ('cmd', 'g3', 'bash good.sh'), ('cmd', 'g4', 'cat app.conf')],
 'state': [('cmd', 'st1', 'mkdir -p logs; mkdir -p logs; echo $?'), ('cmd', 'st2', 'rm -f nothing.txt; echo $?'), ('cmd', 'st3', 'ln -sfn logs cur; ln -sfn logs cur; ls -l cur')],
 'finds': [('cmd', 'fi1', 'cat typo.sh'), ('cmd', 'fi2', 'shellcheck typo.sh'), ('cmd', 'fi3', 'echo $?')],
 'fixes': [('cmd', 'd1', 'cat buggy.sh'), ('cmd', 'd2', 'shellcheck -f diff buggy.sh'), ('cmd', 'd3', 'shellcheck -f diff buggy.sh | patch buggy.sh'), ('cmd', 'd4', 'cat buggy.sh'), ('cmd', 'd5', 'shellcheck buggy.sh && echo clean')],
 'build': [('cmd', 'bu1', 'cat site.sh'), ('cmd', 'bu2', 'shellcheck site.sh && echo clean'), ('cmd', 'bu3', 'bash site.sh'), ('cmd', 'bu4', 'bash site.sh; wc -l conf/app.conf')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
