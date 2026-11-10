"""Record Lesson 24 live terminal demos in a real 3-namespace lab with a fault injected in advance. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson24')
from term import *
import video as V
LD = '/home/claude/academy/lesson24'
def stage(scene, pre, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    subprocess.run('/usr/local/bin/lab24.sh up', shell=True); time.sleep(1)
    if pre: subprocess.run(pre, shell=True)
    p = xterm_start(prefix=['ip', 'netns', 'exec', 'client'])
    subprocess.run('cp /opt/lab24/ca.pem /home/student/ca.pem; chown student /home/student/ca.pem', shell=True)
    focus(); r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; /usr/local/bin/lab24.sh down; true', shell=True)
H = 'http://web.lab.test:8080'
STAGES = {
 'dns': (None, [('cmd', 'n1', 'curl -sS -m 3 http://shop.lab.test:8080'), ('cmd', 'n3', 'dig +short shop.lab.test'), ('cmd', 'n5', 'dig +short web.lab.test')]),
 'port': ("pkill -f 'web24.py 8080'", [('cmd', 'p1', 'curl -sS -m 3 ' + H), ('cmd', 'p3', 'sv ss -ltn'), ('cmd', 'p5', 'sv startweb'), ('cmd', 'p6', 'curl -s ' + H)]),
 'fw': ('ip netns exec srv iptables -A INPUT -p tcp --dport 8080 -j DROP', [('cmd', 'f1', 'curl -sS -m 3 ' + H), ('cmd', 'f4', 'ping -c 1 10.0.2.2'), ('cmd', 'f6', 'sv iptables -S INPUT'), ('cmd', 'f8', 'sv iptables -D INPUT 1'), ('cmd', 'f9', 'curl -s ' + H)]),
 'tls': (None, [('cmd', 't1', 'get https://web.lab.test:8443'), ('cmd', 't3', 'cert web.lab.test:8443'), ('cmd', 't5', 'get --cacert ca.pem https://web.lab.test:8443'), ('cmd', 't7', 'get --cacert ca.pem https://10.0.2.2:8443')]),
 'route': ('ip -n client route del default; ip netns exec r1 sysctl -qw net.ipv4.ip_forward=0', [('cmd', 'r1', 'ping -c 1 -W 1 10.0.2.2'), ('cmd', 'r3', 'ip route'), ('cmd', 'r5', 'sudo ip route add default via 10.0.1.1'), ('cmd', 'r6', 'ping -c 1 -W 1 10.0.2.2'), ('cmd', 'r8', 'traceroute -n -w 1 -q 1 -m 3 10.0.2.2'), ('cmd', 'r10', 'rt sysctl net.ipv4.ip_forward'), ('cmd', 'r11', 'rt sysctl -w net.ipv4.ip_forward=1'), ('cmd', 'r12', 'ping -c 1 -W 1 10.0.2.2')]),
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, *STAGES[s])
