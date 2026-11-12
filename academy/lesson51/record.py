"""Record Lesson 51 live terminal demos (exceptions, logging, retries) against the local lab API. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson51')
from term import *
import video as V
LD = '/home/claude/academy/lesson51'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    api = subprocess.Popen(['python3', LD + '/lab/api06.py', '8081'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
    p = xterm_start(PFX); focus(); time.sleep(1.5)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    api.terminate()
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'exceptions': [('cmd', 'e1', 'python3 -q'), ('cmd', 'e2', 'int("eight")'), ('cmd', 'e3', 'exit()'), ('cmd', 'e4', 'cat load.py'), ('cmd', 'e5', 'python3 load.py'), ('cmd', 'e6', "echo '{\"retries\": 5}' > settings.json"), ('cmd', 'e7', 'python3 load.py'), ('cmd', 'e8', "echo '{bad' > settings.json"), ('cmd', 'e9', 'python3 load.py')],
 'logging': [('cmd', 'l1', 'cat logdemo.py'), ('cmd', 'l2', 'python3 logdemo.py'), ('cmd', 'l3', "sed -i 's/INFO/WARNING/' logdemo.py"), ('cmd', 'l4', 'python3 logdemo.py')],
 'retry': [('cmd', 'y1', 'cat retry.py'), ('cmd', 'y2', 'python3 retry.py'), ('cmd', 'y3', "sed -i 's/range(1, 5)/range(1, 3)/' retry.py"), ('cmd', 'y4', 'python3 retry.py'), ('cmd', 'y5', 'echo $?')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
