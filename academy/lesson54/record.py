"""Record Lesson 54 live terminal demos (least-privilege policy audit, boto3 against moto). usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson54')
from term import *
import video as V
LD = '/home/claude/academy/lesson54'
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
 'policy': [('cmd', 'a1', 'cat policy.json'), ('cmd', 'a2', './audit.py policy.json'), ('cmd', 'a3', './audit.py bad.json'), ('cmd', 'a4', 'echo $?')],
 'sdk': [('cmd', 'd1', 'cat s3list.py'), ('cmd', 'd2', 'python3 s3list.py'), ('cmd', 'd3', 'cat s3miss.py'), ('cmd', 'd4', 'python3 s3miss.py')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
