"""Record Lesson 61 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson61')
from term import *
import video as V
LD = '/home/claude/academy/lesson61'
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
 'clone': [('cmd', 'cl1', 'git clone /srv/git/team.git'), ('cmd', 'cl2', 'cd team'), ('cmd', 'cl3', 'git remote -v'), ('cmd', 'cl4', 'git branch -vv'), ('cmd', 'cl5', 'git branch -a')],
 'fetch': [('cmd', 'ft1', 'cd team'), ('cmd', 'ft2', 'git status'), ('cmd', 'ft3', 'git fetch'), ('cmd', 'ft4', 'git status'), ('cmd', 'ft5', 'git log --oneline main..origin/main'), ('cmd', 'ft6', 'git pull'), ('cmd', 'ft7', 'git log --oneline')],
 'push': [('cmd', 'ps1', 'cd team'), ('cmd', 'ps2', 'echo "echo ready" >> start.sh'), ('cmd', 'ps3', 'git commit -am "Print ready message"'), ('cmd', 'ps4', 'git push'), ('cmd', 'ps5', 'git pull --rebase'), ('cmd', 'ps6', 'git push'), ('cmd', 'ps7', 'git log --oneline --graph --all')],
 'tags': [('cmd', 'tg1', 'cd team'), ('cmd', 'tg2', 'git tag -a v1.0 -m "First release"'), ('cmd', 'tg3', 'git tag'), ('cmd', 'tg4', 'git show --stat v1.0'), ('cmd', 'tg5', 'git push origin v1.0'), ('cmd', 'tg6', 'git ls-remote --tags origin')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
