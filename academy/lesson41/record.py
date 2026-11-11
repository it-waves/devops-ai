"""Record Lesson 41 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson41')
from term import *
import video as V
LD = '/home/claude/academy/lesson41'
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
 'streams': [('cmd', 'f1', 'ls /etc/hostname /nope'), ('cmd', 'f2', 'ls /etc/hostname /nope > out.txt'), ('cmd', 'f3', 'cat out.txt'), ('cmd', 'f4', 'ls /etc/hostname /nope 2> err.txt'), ('cmd', 'f5', 'cat err.txt')],
 'redir': [('cmd', 'd1', 'echo first > log.txt'), ('cmd', 'd2', 'echo second >> log.txt'), ('cmd', 'd3', 'cat log.txt'), ('cmd', 'd4', 'wc -l < log.txt'), ('cmd', 'd5', 'ls /nope 2> /dev/null'), ('cmd', 'd6', 'echo $?')],
 'pipes': [('cmd', 'q1', 'cat app.log'), ('cmd', 'q2', 'cat app.log | grep ERROR'), ('cmd', 'q3', 'grep ERROR app.log | wc -l'), ('cmd', 'q4', 'grep ERROR app.log | tee errors.txt | wc -l'), ('cmd', 'q5', 'cat errors.txt')],
 'tmp': [('cmd', 't1', 'f=$(mktemp)'), ('cmd', 't2', 'echo "$f"'), ('cmd', 't3', 'grep ERROR app.log > "$f"'), ('cmd', 't4', 'wc -l < "$f"'), ('cmd', 't5', 'rm "$f"'), ('cmd', 't6', 'ls "$f"')],
 'build': [('cmd', 'w1', 'cat app.log'), ('cmd', 'w2', "awk '{print $3}' app.log | sort | uniq -c > out.txt"), ('cmd', 'w3', 'cat out.txt'), ('cmd', 'w4', 'grep -c ERROR app.log missing.log 2> problems.txt'), ('cmd', 'w5', 'cat problems.txt')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
