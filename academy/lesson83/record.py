"""Record Lesson 83 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson83')
from term import *
import video as V
LD = '/home/claude/academy/lesson83'
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
 'vermem': [('cmd', 'a0', 'cd shop'), ('cmd', 'a1', 'sh run-version.sh'), ('cmd', 'a2', 'java --version | head -1'), ('cmd', 'a3', 'od -An -tu1 -j7 -N1 ver/classes/cloudcart/Greeter.class'), ('cmd', 'a4', 'javac -d ver/classes ver/src/cloudcart/Greeter.java'), ('cmd', 'a5', 'sh run-version.sh'), ('cmd', 'a6', 'sh run-memory.sh'), ('cmd', 'a7', 'grep Xmx run-memory.sh'), ('cmd', 'a8', "sed -i 's/-Xmx16m/-Xmx256m/' run-memory.sh"), ('cmd', 'a9', 'sh run-memory.sh')],
 'portcp': [('cmd', 'p0', 'cd shop'), ('cmd', 'p1', 'sh run-port.sh 2>&1 | head -4'), ('cmd', 'p2', 'grep Server run-port.sh'), ('cmd', 'p3', "sed -i 's/Server 18083 ||/Server 18084 ||/' run-port.sh"), ('cmd', 'p4', 'sh run-port.sh'), ('cmd', 'p5', 'sh run-classpath.sh 2>&1 | head -4'), ('cmd', 'p6', 'grep java run-classpath.sh'), ('cmd', 'p7', 'ls cp/lib'), ('cmd', 'p8', "sed -i 's|-cp cp/classes |-cp cp/classes:cp/lib/helper.jar |' run-classpath.sh"), ('cmd', 'p9', 'sh run-classpath.sh')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
