"""Record Lesson 90 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson90')
from term import *
import video as V
LD = '/home/claude/academy/lesson90'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5 + (18 if scene in ('mirror',) else 0))
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'mirror': [('cmd', 'm0', 'cd demo'), ('cmd', 'm1', 'cat ~/.m2/settings.xml'), ('cmd', 'm2', "mvn -B -q clean package 2>&1 | grep -o 'corp (http.*' | head -1"), ('cmd', 'm3', 'export REPO_PASS=$(cat ~/.corp-pass)'), ('cmd', 'm4', 'mvn -B -q clean package && ls target/*.jar'), ('cmd', 'm5', "grep -rl \"$REPO_PASS\" . ~/.m2/settings.xml || echo 'password is in no file'"), ('cmd', 'm6', "chmod 600 ~/.m2/settings.xml && stat -c '%A %n' ~/.m2/settings.xml ~/.corp-pass")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
