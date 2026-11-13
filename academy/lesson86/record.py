"""Record Lesson 86 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson86')
from term import *
import video as V
LD = '/home/claude/academy/lesson86'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5 + (18 if scene in ('life', 'fail') else 0))
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'life': [('cmd', 'p0', 'cd demo'), ('cmd', 'p1', "mvn -B compile | grep -E '^\\[INFO\\] --- |BUILD' | cut -c8-"), ('cmd', 'p2', 'ls target'), ('cmd', 'p3', "mvn -B test | grep -E '^\\[INFO\\] --- |Tests run:.*Skipped: 0$|BUILD' | cut -c8-"), ('cmd', 'p4', "mvn -B package | grep -E '^\\[INFO\\] --- |BUILD' | cut -c8-"), ('cmd', 'p5', 'ls target'), ('cmd', 'p6', "mvn -B package -DskipTests | grep -E 'skipped|BUILD'"), ('cmd', 'p7', "mvn -B clean | grep -E '^\\[INFO\\] --- |BUILD' | cut -c8-"), ('cmd', 'p8', 'ls target')],
 'fail': [('cmd', 'x0', 'cd demo'), ('cmd', 'x1', "sed -i 's/Hello, /Hi, /' src/main/java/cloudcart/Hello.java"), ('cmd', 'x2', "mvn -B package | grep -E '^\\[INFO\\] --- |Tests run:.*Skipped: 0$|BUILD' | cut -c8-"), ('cmd', 'x3', 'ls target/*.jar'), ('cmd', 'x4', "sed -i 's/Hi, /Hello, /' src/main/java/cloudcart/Hello.java"), ('cmd', 'x5', "mvn -B clean verify | grep -E 'Tests run:.*Skipped: 0$|BUILD' | cut -c8-")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
