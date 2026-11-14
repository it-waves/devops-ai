"""Record Lesson 88 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson88')
from term import *
import video as V
LD = '/home/claude/academy/lesson88'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5 + (18 if scene in ('tree',) else 0))
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'tree': [('cmd', 't0', 'cd demo'), ('cmd', 't1', "mvn -B dependency:tree | grep 'jar:' | cut -c8-"), ('cmd', 't2', "mvn -B dependency:tree -Dverbose | grep omitted | cut -c8-"), ('cmd', 't3', "mvn -B dependency:tree -Dincludes=com.cloudcart.lib:util | grep 'jar:' | cut -c8-"), ('cmd', 't4', 'mvn -B -q compile 2>&1 | head -4'), ('cmd', 't5', 'cat dm.xml'), ('cmd', 't6', "sed -i '/<\\/properties>/r dm.xml' pom.xml"), ('cmd', 't7', "mvn -B dependency:tree | grep 'jar:' | cut -c8-"), ('cmd', 't8', 'mvn -B -q compile && echo built')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
