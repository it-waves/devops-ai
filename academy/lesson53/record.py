"""Record Lesson 53 live terminal demos (exceptions, logging, retries) against the local lab API. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson53')
from term import *
import video as V
LD = '/home/claude/academy/lesson53'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    api = subprocess.Popen(['python3', LD + '/lab/api06.py', '8081'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
    p = xterm_start(PFX); focus(); time.sleep(16)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    api.terminate()
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'pytest': [('cmd', 'p1', 'cat inventory.py'), ('cmd', 'p2', 'cat test_inventory.py'), ('cmd', 'p3', 'pytest -q'), ('cmd', 'p4', "sed -i '8s/web-01/web-09/' test_inventory.py"), ('cmd', 'p5', 'pytest -q --tb=short'), ('cmd', 'p6', "sed -i '8s/web-09/web-01/' test_inventory.py"), ('cmd', 'p7', 'pytest -q')],
 'mock': [('cmd', 'm1', 'cat test_health.py'), ('cmd', 'm2', 'pytest -q'), ('cmd', 'm3', 'pytest -v'), ('cmd', 'm4', 'pytest -q -k down')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
