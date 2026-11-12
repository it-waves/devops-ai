"""Record Lesson 57 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson57')
from term import *
import video as V
LD = '/home/claude/academy/lesson57'
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
 'init': [('cmd', 'i1', 'git config --global user.name "Sam Lee"'), ('cmd', 'i2', 'git config --global user.email sam@example.com'), ('cmd', 'i3', 'mkdir notes'), ('cmd', 'i4', 'cd notes'), ('cmd', 'i5', 'git init'), ('cmd', 'i6', 'ls -a'), ('cmd', 'i7', 'ls .git')],
 'commit': [('cmd', 'm1', 'cd notes'), ('cmd', 'm2', 'echo "# ports" > README.md'), ('cmd', 'm3', 'git status -s'), ('cmd', 'm4', 'git add README.md'), ('cmd', 'm5', 'git commit -m "Start the notes"'), ('cmd', 'm6', 'echo "ports: 80 443" > ports.txt'), ('cmd', 'm7', 'git add ports.txt'), ('cmd', 'm8', 'git commit -m "Add ports list"'), ('cmd', 'm9', 'git log --oneline')],
 'objs': [('cmd', 'o1', 'cd notes'), ('cmd', 'o2', 'cat .git/HEAD'), ('cmd', 'o3', 'git log --oneline'), ('cmd', 'o4', 'git cat-file -t HEAD'), ('cmd', 'o5', 'git cat-file -p HEAD'), ('cmd', 'o6', 'git cat-file -p HEAD^{tree}'), ('cmd', 'o7', 'echo ports: 80 443 | git hash-object --stdin'), ('cmd', 'o8', 'find .git/objects -type f | wc -l')],
 'clone': [('cmd', 'k1', 'git clone /srv/git/notes.git'), ('cmd', 'k2', 'cd notes'), ('cmd', 'k3', 'git log --oneline'), ('cmd', 'k4', 'git remote -v'), ('cmd', 'k5', 'git branch -a')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
