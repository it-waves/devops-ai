"""Record Lesson 29 live terminal demos in a clean standard-layout root (private copy of /etc). usage: record.py STAGE|all"""
import sys, os, shutil; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson29')
from term import *
import video as V
LD = '/home/claude/academy/lesson29'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
H = '/home/student'
def w(path, txt='', mode=0o644):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(txt); os.chmod(path, mode)
def fixtures():
    L = H + '/lab29'
    w(L + '/notes.txt', 'deploy at noon\n'); w(L + '/run.sh', '#!/bin/sh\necho deploy script ran\n'); w(L + '/secret.txt', 'demo-token-not-real\n')
    subprocess.run(['chown', '-R', 'student:student', H])
def stage(scene, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); fixtures()
    focus(); typ('cd lab29', 60); key('Return'); time.sleep(0.4); key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True); shutil.rmtree('/home/maria', ignore_errors=True)
STAGES = {
 'ids': [('cmd', 'i1', 'whoami'), ('cmd', 'i2', 'id'), ('cmd', 'i3', 'grep student /etc/passwd')],
 'perms': [('cmd', 'p1', 'ls -l'), ('cmd', 'p4', 'chmod 600 secret.txt'), ('cmd', 'p5', 'ls -l secret.txt'), ('cmd', 'p7', './run.sh'), ('cmd', 'p8', 'chmod +x run.sh'), ('cmd', 'p9', './run.sh')],
 'sudo': [('cmd', 's1', 'cat /etc/shadow'), ('cmd', 's3', 'sudo whoami'), ('cmd', 's4', 'sudo useradd -m maria'), ('cmd', 's5', 'sudo groupadd devs'), ('cmd', 's6', 'sudo usermod -aG devs maria'), ('cmd', 's7', 'id maria'), ('cmd', 's8', 'sudo chown maria:devs notes.txt'), ('cmd', 's9', 'ls -l notes.txt')],
 'ssh': [('cmd', 'k1', 'ssh-keygen -t ed25519 -f demo_key -N "" -q'), ('cmd', 'k2', 'ls -l demo_key demo_key.pub'), ('cmd', 'k4', 'cat demo_key.pub'), ('cmd', 'k5', 'mkdir -p ~/.ssh'), ('cmd', 'k6', 'cat demo_key.pub >> ~/.ssh/authorized_keys'), ('cmd', 'k7', 'chmod 700 ~/.ssh'), ('cmd', 'k8', 'chmod 600 ~/.ssh/authorized_keys'), ('cmd', 'k9', 'ls -l ~/.ssh')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
