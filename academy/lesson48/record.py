"""Record Lesson 48 live terminal demos (Python REPL and scripts) in a private-mount chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson48')
from term import *
import video as V
LD = '/home/claude/academy/lesson48'
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
STAGES = {
 'repl': [('cmd', 'r1', 'python3 -q'), ('cmd', 'r2', 'port = 8080'), ('cmd', 'r3', 'type(port)'), ('cmd', 'r4', 'name = "web1"'), ('cmd', 'r5', 'type(name)'), ('cmd', 'r6', 'port == "8080"'), ('cmd', 'r7', 'int("8080") + 1'), ('cmd', 'r8', 'exit()')],
 'coll': [('cmd', 'c1', 'python3 -q'), ('cmd', 'c2', 'ports = [80, 443, 8080]'), ('cmd', 'c3', 'ports.append(22)'), ('cmd', 'c4', 'ports'), ('cmd', 'c5', 'ports[0]'), ('cmd', 'c6', 'server = {"name": "web1", "cpu": 72}'), ('cmd', 'c7', 'server["cpu"]'), ('cmd', 'c8', 'server.get("mem", "n/a")'), ('cmd', 'c9', 'server["mem"]')],
 'script': [('cmd', 'p1', 'cat check.py'), ('cmd', 'p2', 'python3 check.py')],
 'func': [('cmd', 'f1', 'cat funcs.py'), ('cmd', 'f2', 'python3 funcs.py')],
 'mod': [('cmd', 'm1', '''python3 -c "import json; print(json.dumps({'a': 1}))"'''), ('cmd', 'm2', 'python3 -c "import funcs"'), ('cmd', 'm3', 'python3 -c "import nothere"')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
