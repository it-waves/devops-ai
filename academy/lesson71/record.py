"""Record Lesson 71 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson71')
from term import *
import video as V
LD = '/home/claude/academy/lesson71'
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
 'layers': [('cmd', 'y1', "cd cloudcart"), ('cmd', 'y2', "./start.sh"), ('cmd', 'y3', "cat app.conf"), ('cmd', 'y5', "curl -s localhost:5000/api/config | jq")],
 'env': [('cmd', 'e1', "cd cloudcart"), ('cmd', 'e2', "STORE_NAME=\"Blue Shop\" ./start.sh"), ('cmd', 'e4', "curl -s localhost:5000/api/config | jq"), ('cmd', 'e6', "./start.sh"), ('cmd', 'e7', "curl -s localhost:5000/api/config | jq -r .store_name")],
 'flags': [('cmd', 'f1', "cd cloudcart"), ('cmd', 'f1a', "./start.sh"), ('cmd', 'f2', "curl -s localhost:5000/api/products | jq -c '.[0]'"), ('cmd', 'f4', "FLAG_DISCOUNT=on ./start.sh"), ('cmd', 'f5', "curl -s localhost:5000/api/products | jq -c '.[0]'")],
 'failfast': [('cmd', 'x1', "cd cloudcart"), ('cmd', 'x2', "PORT=abc python3 api.py"), ('cmd', 'x4', "echo $?")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
