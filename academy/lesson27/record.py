"""Record Lesson 27 live terminal demos in a clean standard-layout root. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson27')
from term import *
import video as V
LD = '/home/claude/academy/lesson27'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
H = '/home/student'
def w(path, txt=''):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(txt)
def fixtures(level):
    w(H + '/shopping.txt', 'milk\neggs\nbread\nrice\ncoffee\ntea\napples\nsoap\n')
    w(H + '/projects/cloudcart/app/cart.py', 'print("cart")\n'); w(H + '/projects/cloudcart/config/app.conf', 'port=8080\n')
    if level >= 1:
        os.makedirs(H + '/lab27/docs/old', exist_ok=True); w(H + '/lab27/hello.txt'); w(H + '/lab27/notes.txt')
    if level >= 2: w(H + '/lab27/shopping.txt', 'milk\neggs\nbread\nrice\ncoffee\ntea\napples\nsoap\n')
    subprocess.run(['chown', '-R', 'student:student', H])
def stage(scene, level, steps, cd=False):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); fixtures(level)
    focus()
    if cd: typ('cd lab27', 60); key('Return'); time.sleep(0.4); key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        elif st[0] == 'fn': st[1](r)
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
def at_t(r, cid, off, *acts):
    r.at(cid, off)
    for a in acts:
        if a.startswith('KEY:'): key(a[4:])
        else: typ(a, 80)
        time.sleep(0.25)
def vim1(r):
    at_t(r, 'v3', 1.5, 'i'); r.at('v4', 0.8); typ('buy milk', 80); key('Return'); typ('buy eggs', 80); key('Return'); typ('call mum', 80)
    at_t(r, 'v5', 1.2, 'KEY:Escape'); at_t(r, 'v6', 1.8, 'dd'); at_t(r, 'v7', 1.8, 'u')
    r.at('v8', 1.0); typ('/eggs', 80); time.sleep(1.0); key('Return')
    r.at('v9', 2.5); typ(':wq', 80); time.sleep(0.8); key('Return')
def vim2(r):
    r.at('v11', 0.3); key('ctrl+l'); typ('vim todo.txt', 80); key('Return')
    r.at('v11', 3.4); typ('dd', 80); r.at('v11', 5.6); typ(':q!', 80); time.sleep(0.8); key('Return')
STAGES = {
 'make': (0, False, [('cmd', 'k1', 'mkdir -p lab27/docs/old'), ('cmd', 'k2', 'cd lab27'), ('cmd', 'k3', 'touch hello.txt notes.txt'), ('cmd', 'k4', 'ls -l')]),
 'inspect': (1, True, [('cmd', 'i1', 'cp ~/shopping.txt .'), ('cmd', 'i2', 'cat shopping.txt'), ('cmd', 'i3', 'head -n 3 shopping.txt'), ('cmd', 'i4', 'tail -n 2 shopping.txt'), ('cmd', 'i5', 'wc -l shopping.txt'), ('cmd', 'i6', 'file shopping.txt')]),
 'cpmv': (2, True, [('cmd', 'c1', 'cp shopping.txt backup.txt'), ('cmd', 'c2', 'mv backup.txt docs/'), ('cmd', 'c3', 'mv notes.txt ideas.txt'), ('cmd', 'c4', 'cp -r docs docs2'), ('cmd', 'c5', 'ls -R'), ('cmd', 'c6', 'rm hello.txt'), ('cmd', 'c7', 'rm -r docs2'), ('cmd', 'c8', 'ls')]),
 'search': (2, False, [('cmd', 'f1', 'find ~ -name "*.conf"'), ('cmd', 'f3', 'find ~ -type d -name config')]),
 'vim': (1, True, [('cmd', 'v1', 'vim todo.txt'), ('fn', vim1), ('cmd', 'v10', 'cat todo.txt'), ('fn', vim2), ('cmd', 'v12', 'cat todo.txt')]),
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); lv, cd, st = STAGES[s]; stage(s, lv, st, cd)
