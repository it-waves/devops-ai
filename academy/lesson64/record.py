"""Record Lesson 64 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson64')
from term import *
import video as V
LD = '/home/claude/academy/lesson64'
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
 'leak': [('cmd', 'lk1', 'cd app'), ('cmd', 'lk2', 'git log --oneline'), ('cmd', 'lk3', 'cat .env'), ('cmd', 'lk4', 'echo ".env" >> .gitignore'), ('cmd', 'lk5', 'git rm --cached .env'), ('cmd', 'lk6', 'git add .gitignore'), ('cmd', 'lk7', 'git commit -m "Stop tracking .env"'), ('cmd', 'lk8', 'git log -S demo-secret --oneline'), ('cmd', 'lk9', 'git filter-repo --path .env --invert-paths --force'), ('cmd', 'lk10', 'git log -S demo-secret --oneline'), ('cmd', 'lk11', 'git log --oneline')],
 'ssh': [('cmd', 'ss1', 'mkdir -p ~/.ssh'), ('cmd', 'ss2', 'ssh-keygen -t ed25519 -C sam@example.com -f ~/.ssh/lab64_key -N ""'), ('cmd', 'ss3', 'ls ~/.ssh'), ('cmd', 'ss4', 'cat ~/.ssh/lab64_key.pub'), ('cmd', 'ss5', 'head -n 1 ~/.ssh/lab64_key')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
