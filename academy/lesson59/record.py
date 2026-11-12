"""Record Lesson 59 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson59')
from term import *
import video as V
LD = '/home/claude/academy/lesson59'
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
 'branch': [('cmd', 'br1', 'cd site'), ('cmd', 'br2', 'git branch'), ('cmd', 'br3', 'git switch -c feature'), ('cmd', 'br4', 'git branch'), ('cmd', 'br5', 'echo "Owner: Sam" >> index.html'), ('cmd', 'br6', 'git commit -am "Add owner line"'), ('cmd', 'br7', 'git log --oneline --graph --all'), ('cmd', 'br8', 'git switch main'), ('cmd', 'br9', 'cat index.html')],
 'merge': [('cmd', 'mg1', 'cd site'), ('cmd', 'mg2', 'git log --oneline --graph --all'), ('cmd', 'mg3', 'git merge --no-edit feature'), ('cmd', 'mg4', 'git log --oneline --graph'), ('cmd', 'mg5', 'git branch -d feature'), ('cmd', 'mg6', 'git branch')],
 'conflict': [('cmd', 'cf1', 'cd site'), ('cmd', 'cf2', 'git merge --no-edit feature'), ('cmd', 'cf3', 'git status -s'), ('cmd', 'cf4', 'git merge --abort'), ('cmd', 'cf5', 'git status -s'), ('cmd', 'cf6', 'git merge --no-edit feature'), ('cmd', 'cf7', 'cat app.conf'), ('cmd', 'cf8', "printf 'port=8080\\ntimeout=5\\n' > app.conf"), ('cmd', 'cf9', 'git add app.conf'), ('cmd', 'cf10', 'git commit --no-edit'), ('cmd', 'cf11', 'git log --oneline --graph')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
