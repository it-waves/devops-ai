"""Record Lesson 49 live terminal demos (files, JSON, YAML, CSV, env vars) in a private-mount chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson49')
from term import *
import video as V
LD = '/home/claude/academy/lesson49'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'files': [('cmd', 'fl1', 'cat files.py'), ('cmd', 'fl2', 'python3 files.py'), ('cmd', 'fl3', 'cat notes.txt')],
 'json': [('cmd', 'j1', 'cat servers.json'), ('cmd', 'j2', 'python3 -q'), ('cmd', 'j3', 'import json'), ('cmd', 'j4', 'd = json.load(open("servers.json"))'), ('cmd', 'j5', 'd["servers"][1]["name"]'), ('cmd', 'j6', 'json.dumps(d["servers"][0])'), ('cmd', 'j7', 'exit()')],
 'yaml': [('cmd', 'y1', 'cat config.yaml'), ('cmd', 'y2', 'python3 -q'), ('cmd', 'y3', 'import yaml'), ('cmd', 'y4', 'cfg = yaml.safe_load(open("config.yaml"))'), ('cmd', 'y5', 'cfg["limit"]'), ('cmd', 'y6', 'cfg["hosts"]'), ('cmd', 'y7', 'exit()')],
 'csv': [('cmd', 's1', 'cat servers.csv'), ('cmd', 's2', 'python3 -q'), ('cmd', 's3', 'import csv'), ('cmd', 's4', 'rows = list(csv.DictReader(open("servers.csv")))'), ('cmd', 's5', 'len(rows)'), ('cmd', 's6', 'rows[1]'), ('cmd', 's7', 'int(rows[1]["cpu"])'), ('cmd', 's8', 'exit()')],
 'env': [('cmd', 'e1', 'export LIMIT=80'), ('cmd', 'e2', 'python3 -q'), ('cmd', 'e3', 'import os'), ('cmd', 'e4', 'os.getenv("LIMIT")'), ('cmd', 'e5', 'int(os.getenv("LIMIT", "50"))'), ('cmd', 'e6', 'os.getenv("REGION", "eu-west-1")'), ('cmd', 'e7', 'os.environ["TOKEN"]')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
