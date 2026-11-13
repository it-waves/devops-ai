"""Record Lesson 68 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson68')
from term import *
import video as V
LD = '/home/claude/academy/lesson68'
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
 'get': [('cmd', 'g1', 'cd cloudcart'), ('cmd', 'g2', './start.sh'), ('cmd', 'g3', 'curl -i localhost:5000/api/products/1'), ('cmd', 'g7', 'curl -s localhost:5000/api/products | jq -c ".[]"')],
 'status': [('cmd', 's1', 'cd cloudcart'), ('cmd', 's2', './start.sh'), ('cmd', 's3', 'curl -si localhost:5000/api/products/99 | head -1'), ('cmd', 's5', 'curl -s localhost:5000/api/products/99'), ('cmd', 's6', "curl -si -X POST -d '{\"name\":\"Mug\"}' localhost:5000/api/products | head -1")],
 'write': [('cmd', 'w1', 'cd cloudcart'), ('cmd', 'w2', './start.sh'), ('cmd', 'w3', "curl -i -X POST -H 'Content-Type: application/json' -d '{\"name\":\"Mug\",\"price\":9}' localhost:5000/api/products"), ('cmd', 'w5', 'curl -s localhost:5000/api/products | jq -c ".[]"'), ('cmd', 'w6', 'curl -si -X DELETE localhost:5000/api/products/4 | head -1'), ('cmd', 'w8', 'curl -s localhost:5000/api/products | jq length'), ('cmd', 'w9', './stop.sh')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
