"""Record Lesson 55 live terminal demos (validator tool, exit codes and tests). usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson55')
from term import *
import video as V
LD = '/home/claude/academy/lesson55'
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
 'tool': [('cmd', 'e1', 'head -16 svccheck.py'), ('cmd', 'e2', 'cat services.json'), ('cmd', 'e3', './svccheck.py services.json'), ('cmd', 'e4', 'echo $?'), ('cmd', 'e5', './svccheck.py nope.json'), ('cmd', 'e6', 'echo $?')],
 'tests': [('cmd', 'f1', 'cat test_svccheck.py'), ('cmd', 'f2', 'pytest -q'), ('cmd', 'f3', "sed -i 's/65535/65536/' svccheck.py"), ('cmd', 'f4', 'pytest -q --tb=no'), ('cmd', 'f5', "sed -i 's/65536/65535/' svccheck.py"), ('cmd', 'f6', 'pytest -q')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
