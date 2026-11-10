"""Record Lesson 23 live terminal demos in the real lab (client shell; ctr = run in container c1; hst/hnat/publish = host). usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson23')
from term import *
import video as V
LD = '/home/claude/academy/lesson23'
def stage(scene, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    subprocess.run('/usr/local/bin/lab23.sh up', shell=True); time.sleep(1)
    p = xterm_start(prefix=['ip', 'netns', 'exec', 'client']); focus(); r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; /usr/local/bin/lab23.sh down; true', shell=True)
Z = 'ctr curl -sS -m 2 10.0.3.2:8080/whoami'
STAGES = {
 'bdemo': [('cmd', 'd1', 'ip route get 10.0.1.1'), ('cmd', 'd3', 'ip route get 10.0.2.2'), ('cmd', 'd5', 'ping -c 1 -W 1 172.18.0.2')],
 'ctrdemo': [('cmd', 'm1', 'ctr ip -br addr'), ('cmd', 'm3', 'ctr ip route'), ('cmd', 'm5', 'ctr ping -c 1 172.18.0.3'), ('cmd', 'm6', Z), ('cmd', 'm8', 'hnat -A POSTROUTING -s 172.18.0.0/24 -j MASQUERADE'), ('cmd', 'm9', Z)],
 'pubdemo': [('cmd', 'q1', 'curl -sS -m 2 10.0.2.2:8080'), ('cmd', 'q3', 'publish 8080 8000'), ('cmd', 'q4', 'curl -s 10.0.2.2:8080/whoami'), ('cmd', 'q6', 'hnat -S PREROUTING')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
