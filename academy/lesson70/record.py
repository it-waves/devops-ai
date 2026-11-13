"""Record Lesson 70 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson70')
from term import *
import video as V
LD = '/home/claude/academy/lesson70'
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
 'authn': [('cmd', 'a1', "cd cloudcart"), ('cmd', 'a2', "./start.sh"), ('cmd', 'a3', "curl -si -X POST -d '{\"user\":\"bob\",\"password\":\"wrong\"}' localhost:5000/api/login | head -1"), ('cmd', 'a5', "curl -s -X POST -d '{\"user\":\"bob\",\"password\":\"paper-kite-77\"}' localhost:5000/api/login")],
 'access': [('cmd', 'c1', "cd cloudcart"), ('cmd', 'c2', "./start.sh"), ('cmd', 'c3', "curl -si localhost:5000/api/orders | head -1"), ('cmd', 'c5', "TOKEN=$(curl -s -X POST -d '{\"user\":\"bob\",\"password\":\"paper-kite-77\"}' localhost:5000/api/login | jq -r .token)"), ('cmd', 'c6', "curl -s -H \"Authorization: Bearer $TOKEN\" localhost:5000/api/orders"), ('cmd', 'c8', "curl -si -X DELETE -H \"Authorization: Bearer $TOKEN\" localhost:5000/api/products/1 | head -1"), ('cmd', 'c10', "TOKEN=$(curl -s -X POST -d '{\"user\":\"alice\",\"password\":\"blue-heron-42\"}' localhost:5000/api/login | jq -r .token)"), ('cmd', 'c11', "curl -si -X DELETE -H \"Authorization: Bearer $TOKEN\" localhost:5000/api/products/2 | head -1")],
 'secrets': [('cmd', 's1', "cd cloudcart"), ('cmd', 's2', "ls -l secrets.env"), ('cmd', 's4', "chmod 600 secrets.env"), ('cmd', 's5', "ls -l secrets.env"), ('cmd', 's6', "grep -c paper-kite api.py")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
