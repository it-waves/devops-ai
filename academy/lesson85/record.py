"""Record Lesson 85 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson85')
from term import *
import video as V
LD = '/home/claude/academy/lesson85'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5 + (18 if scene == 'deps' else 0))
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'tour': [('cmd', 't0', 'cd demo'), ('cmd', 't1', 'head -16 pom.xml'), ('cmd', 't2', 'find src -type f'), ('cmd', 't3', 'mvn -v | head -1'), ('cmd', 't4', 'mvn -B -q package 2>&1 | head -3')],
 'deps': [('cmd', 'd0', 'cd demo'), ('cmd', 'd1', 'grep import src/main/java/cloudcart/Hello.java'), ('cmd', 'd2', 'cat dep.xml'), ('cmd', 'd3', "sed -i '/<dependencies>/r dep.xml' pom.xml"), ('cmd', 'd4', "mvn -B package | grep -E 'Tests run:|BUILD'"), ('cmd', 'd5', 'ls target/*.jar'), ('cmd', 'd6', "mvn -B dependency:tree | grep 'jar:'"), ('cmd', 'd7', "find ~/.m2 -name 'commons-lang3-3*.jar'")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
