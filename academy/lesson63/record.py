"""Record Lesson 63 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson63')
from term import *
import video as V
LD = '/home/claude/academy/lesson63'
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
 'restore': [('cmd', 'rs1', 'cd site'), ('cmd', 'rs2', 'echo "<p>oops</p>" >> index.html'), ('cmd', 'rs3', 'git status -s'), ('cmd', 'rs4', 'git restore index.html'), ('cmd', 'rs5', 'git status -s'), ('cmd', 'rs6', 'echo "<p>draft</p>" >> index.html'), ('cmd', 'rs7', 'git add index.html'), ('cmd', 'rs8', 'git restore --staged index.html'), ('cmd', 'rs9', 'git status -s'), ('cmd', 'rs10', 'git restore index.html'), ('cmd', 'rs11', 'git restore --source=HEAD~2 index.html'), ('cmd', 'rs12', 'git diff')],
 'revert': [('cmd', 'rv1', 'cd site'), ('cmd', 'rv2', 'git log --oneline'), ('cmd', 'rv3', 'git revert --no-edit HEAD'), ('cmd', 'rv4', 'git log --oneline'), ('cmd', 'rv5', 'cat index.html')],
 'reset': [('cmd', 'rt1', 'cd site'), ('cmd', 'rt2', 'git log --oneline'), ('cmd', 'rt3', 'git reset --soft HEAD~1'), ('cmd', 'rt4', 'git status -s'), ('cmd', 'rt5', 'git reset'), ('cmd', 'rt6', 'git status -s'), ('cmd', 'rt7', 'git reset --hard HEAD~1'), ('cmd', 'rt8', 'git log --oneline')],
 'reflog': [('cmd', 'rl1', 'cd site'), ('cmd', 'rl2', 'git reset --hard HEAD~2'), ('cmd', 'rl3', 'git log --oneline'), ('cmd', 'rl4', 'git reflog'), ('cmd', 'rl5', 'git reset --hard HEAD@{1}'), ('cmd', 'rl6', 'git log --oneline')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
