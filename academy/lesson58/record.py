"""Record Lesson 58 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson58')
from term import *
import video as V
LD = '/home/claude/academy/lesson58'
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
 'stage': [('cmd', 's1', 'cd site'), ('cmd', 's2', 'git status -s'), ('cmd', 's3', 'git diff'), ('cmd', 's4', 'git add index.html'), ('cmd', 's5', 'git diff'), ('cmd', 's6', 'git diff --staged'), ('cmd', 's7', 'git status -s'), ('cmd', 's8', 'git restore --staged index.html'), ('cmd', 's9', 'git status -s')],
 'hist': [('cmd', 'h1', 'cd site'), ('cmd', 'h2', 'git log --oneline'), ('cmd', 'h3', 'git log -n 2'), ('cmd', 'h4', 'git show --stat HEAD'), ('cmd', 'h5', 'git log --oneline -- index.html'), ('cmd', 'h6', 'git show HEAD~3:index.html'), ('cmd', 'h7', 'git blame index.html')],
 'ignore': [('cmd', 'g1', 'cd site'), ('cmd', 'g2', 'git status -s'), ('cmd', 'g3', 'echo debug.log > .gitignore'), ('cmd', 'g4', 'echo build/ >> .gitignore'), ('cmd', 'g5', 'git status -s'), ('cmd', 'g6', 'git check-ignore -v debug.log'), ('cmd', 'g7', 'echo cache.tmp >> .gitignore'), ('cmd', 'g8', 'git status -s'), ('cmd', 'g9', 'git rm --cached cache.tmp'), ('cmd', 'g10', 'git status -s')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
