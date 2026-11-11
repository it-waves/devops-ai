"""Record Lesson 39 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson39')
from term import *
import video as V
LD = '/home/claude/academy/lesson39'
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
 'if': [('cmd', 'd1', 'cat age.sh'), ('cmd', 'd2', './age.sh 20'), ('cmd', 'd3', './age.sh 10'), ('cmd', 'd4', '[ 5 -gt 3 ]; echo $?'), ('cmd', 'd5', '[ 5 -gt 9 ]; echo $?')],
 'tests': [('cmd', 'q1', '[ -f notes.txt ] && echo "file exists"'), ('cmd', 'q2', '[ -d docs ] && echo "directory exists"'), ('cmd', 'q3', '[ -d nodir ] || echo "no such directory"'), ('cmd', 'q4', 'name=Sam'), ('cmd', 'q5', '[ "$name" = Sam ] && echo "same name"'), ('cmd', 'q6', '[ 7 -lt 10 ] && echo "seven is less"'), ('cmd', 'q7', '[ $empty = x ]'), ('cmd', 'q8', '[ "$empty" = x ] || echo "quoted is safe"')],
 'case': [('cmd', 'm1', 'cat menu.sh'), ('cmd', 'm2', './menu.sh start'), ('cmd', 'm3', './menu.sh stop'), ('cmd', 'm4', './menu.sh jump')],
 'loops': [('cmd', 'l1', 'cat for.sh'), ('cmd', 'l2', './for.sh'), ('cmd', 'l3', 'for f in *.log; do echo "found $f"; done'), ('cmd', 'l4', 'cat count.sh'), ('cmd', 'l5', './count.sh')],
 'func': [('cmd', 'u1', 'cat func.sh'), ('cmd', 'u2', './func.sh')],
 'build': [('cmd', 'w1', 'cat health.sh'), ('cmd', 'w2', './health.sh notes.txt app.log'), ('cmd', 'w3', './health.sh notes.txt gone.txt')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
