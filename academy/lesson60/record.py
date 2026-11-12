"""Record Lesson 60 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson60')
from term import *
import video as V
LD = '/home/claude/academy/lesson60'
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
 'amend': [('cmd', 'am1', 'cd site'), ('cmd', 'am2', 'git log --oneline'), ('cmd', 'am3', 'git commit --amend -m "Add owner line"'), ('cmd', 'am4', 'git log --oneline')],
 'rebase': [('cmd', 'rb1', 'cd site'), ('cmd', 'rb2', 'git log --oneline --graph --all'), ('cmd', 'rb3', 'git rebase main'), ('cmd', 'rb4', 'git log --oneline --graph --all'), ('cmd', 'rb5', 'git switch main'), ('cmd', 'rb6', 'git merge feature'), ('cmd', 'rb7', 'git log --oneline --graph')],
 'rconf': [('cmd', 'rc1', 'cd site'), ('cmd', 'rc2', 'git rebase main'), ('cmd', 'rc3', 'git status'), ('cmd', 'rc4', 'cat app.conf'), ('cmd', 'rc5', "printf 'port=8080\\ntimeout=5\\n' > app.conf"), ('cmd', 'rc6', 'git add app.conf'), ('cmd', 'rc7', 'git rebase --continue'), ('cmd', 'rc8', 'git log --oneline --graph')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
