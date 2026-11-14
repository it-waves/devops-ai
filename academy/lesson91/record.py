"""Record Lesson 91 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson91')
from term import *
import video as V
LD = '/home/claude/academy/lesson91'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5 + (25 if scene in ('deploy',) else 0))
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'deploy': [('cmd', 'd0', 'cd demo'), ('cmd', 'd1', 'sed -n 11,22p pom.xml'), ('cmd', 'd2', 'export REPO_PASS=$(cat ~/.corp-pass)'), ('cmd', 'd3', "mvn -B -q deploy; find ~/store/snapshots -name '*.jar' -printf '%f\\n'"), ('cmd', 'd4', "mvn -B -q deploy; find ~/store/snapshots -name '*.jar' -printf '%f\\n'"), ('cmd', 'd5', "sed -i 's/-SNAPSHOT//' pom.xml; grep -m1 '<version>' pom.xml"), ('cmd', 'd6', "mvn -B -q deploy; find ~/store/releases -name '*.jar' -printf '%f\\n'"), ('cmd', 'd7', "mvn -B deploy 2>&1 | grep -o 'status code.*'")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
