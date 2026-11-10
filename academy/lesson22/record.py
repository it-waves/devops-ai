"""Record Lesson 22 live terminal demos in the real 3-namespace lab (client shell, rt = run on router). usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson22')
from term import *
import video as V
LD = '/home/claude/academy/lesson22'
def stage(scene, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    subprocess.run('/usr/local/bin/lab22.sh up', shell=True); time.sleep(1)
    p = xterm_start(prefix=['ip', 'netns', 'exec', 'client']); focus(); r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; /usr/local/bin/lab22.sh down; true', shell=True)
W = 'curl -s http://10.0.2.2:8080/whoami'; B = 'curl -sS -m 2 http://10.0.2.2:8080'
STAGES = {
 'routedemo': [('cmd', 't1', 'rt ip route'), ('cmd', 't3', 'rt sysctl net.ipv4.ip_forward'), ('cmd', 't5', 'rt sysctl -w net.ipv4.ip_forward=0'), ('cmd', 't6', 'ping -c 1 -W 1 10.0.2.2'), ('cmd', 't8', 'rt sysctl -w net.ipv4.ip_forward=1')],
 'natdemo': [('cmd', 'n1', W), ('cmd', 'n3', 'rt iptables -t nat -A POSTROUTING -j MASQUERADE'), ('cmd', 'n4', W), ('cmd', 'n6', 'rt iptables -t nat -S POSTROUTING')],
 'fwdemo': [('cmd', 'f1', 'rt iptables -A FORWARD -p tcp --dport 8080 -j DROP'), ('cmd', 'f2', B), ('cmd', 'f4', 'rt iptables -F FORWARD'), ('cmd', 'f5', 'rt iptables -A FORWARD -p tcp --dport 8080 -j REJECT'), ('cmd', 'f6', B), ('cmd', 'f8', 'rt iptables -S FORWARD')],
 'lbdemo': [('cmd', 'l1', 'for i in 1 2 3 4; do curl -s 10.0.1.1; done'), ('cmd', 'l4', 'rt ss -ltn')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
