"""Record Lesson 37 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson37')
from term import *
import video as V
LD = '/home/claude/academy/lesson37'
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
        elif st[0] == 'type':   # typed into a prompt, no screen clear
            r.clear = False; r.cmd(st[1], st[2]); r.clear = True
        elif st[0] == 'answer':  # answer a prompt shortly after the command
            time.sleep(1.8); typ(st[2], 80); key('Return')
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True)
STAGES = {
 'run': [('cmd', 'r1', 'cat hi.sh'), ('cmd', 'r2', 'bash hi.sh'), ('cmd', 'r3', './hi.sh'), ('cmd', 'r4', 'chmod u+x hi.sh'), ('cmd', 'r5', './hi.sh')],
 'quote': [('cmd', 'q1', 'name=Sam'), ('cmd', 'q2', 'echo "Hi $name"'), ('cmd', 'q3', "echo 'Hi $name'"), ('cmd', 'q4', 'ls'), ('cmd', 'q5', 'rm my notes.txt'), ('cmd', 'q6', 'rm "my notes.txt" && echo removed')],
 'expand': [('cmd', 'e1', 'echo ~'), ('cmd', 'e2', 'echo "today is $(date +%A)"'), ('cmd', 'e3', 'echo *.txt'), ('cmd', 'e4', 'echo file-{a,b,c}.log'), ('cmd', 'e5', 'echo $((6 * 7))')],
 'env': [('cmd', 'v1', 'GREETING=hello'), ('cmd', 'v2', 'bash -c \'echo "child sees: $GREETING"\''), ('cmd', 'v3', 'export GREETING'), ('cmd', 'v4', 'bash -c \'echo "child sees: $GREETING"\''), ('cmd', 'v5', 'echo $PATH')],
 'exit': [('cmd', 'x1', 'ls /etc/hostname'), ('cmd', 'x2', 'echo $?'), ('cmd', 'x3', 'ls /nope'), ('cmd', 'x4', 'echo $?'), ('cmd', 'x5', 'grep -q root /etc/passwd && echo found'), ('cmd', 'x6', 'grep -q zzzz /etc/passwd || echo missing')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
