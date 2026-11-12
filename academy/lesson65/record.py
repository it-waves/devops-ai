"""Record Lesson 65 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson65')
from term import *
import video as V
LD = '/home/claude/academy/lesson65'
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
 'checks': [('cmd', 'ck1', 'cd shop'), ('cmd', 'ck2', 'cat check.sh'), ('cmd', 'ck3', './check.sh'), ('cmd', 'ck4', 'echo "oops (" >> shop.sh'), ('cmd', 'ck5', './check.sh'), ('cmd', 'ck6', 'echo $?'), ('cmd', 'ck7', 'git restore shop.sh'), ('cmd', 'ck8', './check.sh')],
 'gate': [('cmd', 'g1', 'cd shop'), ('cmd', 'g2', 'cat .githooks/pre-push'), ('cmd', 'g3', 'git config core.hooksPath .githooks'), ('cmd', 'g4', 'echo "oops (" >> shop.sh'), ('cmd', 'g5', 'git commit -am "Quick change"'), ('cmd', 'g6', 'git push origin main'), ('cmd', 'g7', 'git reset --hard HEAD~1'), ('cmd', 'g8', 'echo "Free shipping" >> notes.txt'), ('cmd', 'g9', 'git add notes.txt'), ('cmd', 'g10', 'git commit -m "Add shipping note"'), ('cmd', 'g11', 'git push origin main')],
 'ci': [('cmd', 'cw0', 'cd shop'), ('cmd', 'cw1', 'cat .github/workflows/ci.yml')],
 'release': [('cmd', 'r1', 'cd shop'), ('cmd', 'r2', 'git tag'), ('cmd', 'r3', 'git log --oneline v1.0.0..HEAD'), ('cmd', 'r4', 'git describe --tags'), ('cmd', 'r5', 'git tag -a v1.1.0 -m "Add discount option"'), ('cmd', 'r6', 'git push origin v1.1.0'), ('cmd', 'r7', 'git ls-remote --tags origin')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
