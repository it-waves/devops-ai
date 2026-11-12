"""Record Lesson 47 live terminal demos in a private-mount chroot (host network kept for pip). usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson47')
from term import *
import video as V
LD = '/home/claude/academy/lesson47'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
IMP = '''python3 -c "import sys; print(sys.prefix)"'''
STAGES = {
 'setup': [('cmd', 's1', 'python3 --version'), ('cmd', 's2', IMP), ('cmd', 's3', 'mkdir inventory'), ('cmd', 's4', 'cd inventory'), ('cmd', 's5', 'python3 -m venv .venv'), ('cmd', 's6', 'ls -a')],
 'activate': [('cmd', 'a1', 'source .venv/bin/activate'), ('cmd', 'a2', 'which python'), ('cmd', 'a3', 'pip install -q requests'), ('cmd', 'a4', 'pip list'), ('cmd', 'a5', 'pip show requests | grep Version')],
 'deps': [('cmd', 'd1', 'pip freeze'), ('cmd', 'd2', 'pip freeze > requirements.txt'), ('cmd', 'd3', 'cat requirements.txt'), ('cmd', 'd4', 'deactivate'), ('cmd', 'd5', 'python3 -c "import requests"')],
 'repro': [('cmd', 'r1', 'ls'), ('cmd', 'r2', 'python3 -m venv .venv'), ('cmd', 'r3', 'source .venv/bin/activate'), ('cmd', 'r4', 'pip install -q -r requirements.txt'), ('cmd', 'r5', 'pip freeze | diff - requirements.txt'), ('cmd', 'r6', 'echo $?')],
 'layout': [('cmd', 'l1', 'mkdir -p src/inventory tests'), ('cmd', 'l2', 'touch src/inventory/__init__.py'), ('cmd', 'l3', 'echo .venv/ > .gitignore'), ('cmd', 'l4', 'find . -path ./.venv -prune -o -print'), ('cmd', 'l5', 'bash ../check47.sh .')],
 'cleanup': [('cmd', 'c1', 'ls -a'), ('cmd', 'c2', 'cd ..'), ('cmd', 'c3', 'rm -rf inventory'), ('cmd', 'c4', 'ls')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
