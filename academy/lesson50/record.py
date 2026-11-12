"""Record Lesson 50 live terminal demos (requests: first call, auth, timeout, pagination) against the local lab API. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson50')
from term import *
import video as V
LD = '/home/claude/academy/lesson50'
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
 'basics': [('cmd', 'b1', 'python3 -q'), ('cmd', 'b2', 'import requests'), ('cmd', 'b3', 'r = requests.get("http://127.0.0.1:8081/health", timeout=5)'), ('cmd', 'b4', 'r.status_code'), ('cmd', 'b5', 'r.json()'), ('cmd', 'b6', 'exit()')],
 'auth': [('cmd', 'a1', 'export API_TOKEN=lab-token-123'), ('cmd', 'a2', 'python3 -q'), ('cmd', 'a3', 'import os, requests'), ('cmd', 'a4', 'URL = "http://127.0.0.1:8081/servers"'), ('cmd', 'a5', 'requests.get(URL, timeout=5).status_code'), ('cmd', 'a6', 'h = {"Authorization": "Bearer " + os.environ["API_TOKEN"]}'), ('cmd', 'a7', 'requests.get(URL, headers=h, timeout=5).status_code'), ('cmd', 'a8', 'requests.get(URL, headers=h, timeout=5).json()["total"]')],
 'timeout': [('cmd', 'o1', 'cat timeout.py'), ('cmd', 'o2', 'python3 timeout.py'), ('cmd', 'o3', "sed -i 's/timeout=1/timeout=5/' timeout.py"), ('cmd', 'o4', 'python3 timeout.py')],
 'pages': [('cmd', 'g1', 'cat pages.py'), ('cmd', 'g2', 'python3 pages.py')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
