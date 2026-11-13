"""Record Lesson 77 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson77')
from term import *
import video as V
LD = '/home/claude/academy/lesson77'
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
 'run': [('cmd', 'r0', 'cd shop'), ('cmd', 'r1', 'cat Greeter.java'), ('cmd', 'r2', 'java Greeter.java Ada'), ('cmd', 'r3', 'ls'), ('cmd', 'r4', 'javac Greeter.java'), ('cmd', 'r5', 'ls'), ('cmd', 'r6', 'java Greeter Ada'), ('cmd', 'r7', 'java Greeter'), ('cmd', 'r8', 'echo $?')],
 'errors': [('cmd', 'e0', 'cd shop'), ('cmd', 'e1', 'javac Broken.java'), ('cmd', 'e2', "sed -i '3s/$/;/' Broken.java"), ('cmd', 'e3', 'javac Broken.java'), ('cmd', 'e4', 'java Broken'), ('cmd', 'e5', 'javac Wrong.java'), ('cmd', 'e6', 'java Greeter.class')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
