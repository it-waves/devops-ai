"""Record Lesson 52 live terminal demos (exceptions, logging, retries) against the local lab API. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson52')
from term import *
import video as V
LD = '/home/claude/academy/lesson52'
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
 'cli': [('cmd', 'a1', 'cat portcheck.py'), ('cmd', 'a2', './portcheck.py -h'), ('cmd', 'a3', './portcheck.py localhost 8081'), ('cmd', 'a4', 'echo $?'), ('cmd', 'a5', './portcheck.py localhost 1'), ('cmd', 'a6', 'echo $?'), ('cmd', 'a7', './portcheck.py localhost abc'), ('cmd', 'a8', 'echo $?')],
 'shell': [('cmd', 'b1', './portcheck.py localhost 1 2>/dev/null'), ('cmd', 'b2', './portcheck.py -q localhost 8081 && echo up'), ('cmd', 'b3', './portcheck.py -q localhost 1 || echo down')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
