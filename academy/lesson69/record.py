"""Record Lesson 69 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson69')
from term import *
import video as V
LD = '/home/claude/academy/lesson69'
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
def pre(a, b): return [('cmd', a, 'cd cloudcart'), ('cmd', b, './start.sh')]
STAGES = {
 'verbose': pre('v1', 'v2') + [('cmd', 'v3', "curl -sv localhost:5000/api/products/1 2>&1 | grep '^[<>] [A-Z]'")],
 'headers': pre('d1', 'd2') + [('cmd', 'd3', 'curl -sI localhost:5000/api/products'), ('cmd', 'd5', "curl -s -H 'Accept: text/csv' localhost:5000/api/products")],
 'timing': pre('t1', 't2') + [('cmd', 't3', "curl -s -o /dev/null -w '%{http_code} %{time_total}\\n' localhost:5000/api/fast"), ('cmd', 't5', "curl -s -o /dev/null -w '%{http_code} %{time_total}\\n' localhost:5000/api/report")],
 'exit': pre('e1', 'e2') + [('cmd', 'e3', 'curl -s localhost:5000/api/products/99; echo "exit=$?"'), ('cmd', 'e5', 'curl -sf localhost:5000/api/products/99; echo "exit=$?"')],
 'trace': pre('r1', 'r2') + [('cmd', 'r3', "curl -s -H 'X-Request-Id: demo-42' -o /dev/null localhost:5000/api/products/1"), ('cmd', 'r4', 'tail -n 1 api.log'), ('cmd', 'r6', './codes.sh'), ('cmd', 'r8', './stop.sh')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
