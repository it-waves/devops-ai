"""Record Lesson 17 live terminal demos. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson17')
from term import *
import video as V
LD = '/home/claude/academy/lesson17'
def netup():
    netdown()
    for c in ['ip link add enp0s3 type bridge', 'ip link add vb0 type veth peer name vb1', 'ip link set vb0 master enp0s3', 'ip link set vb0 up', 'ip link set vb1 up',
              'ip addr add 192.168.1.25/24 dev enp0s3', 'ip link set enp0s3 up', 'ip route add default via 192.168.1.1 dev enp0s3 metric 900']:
        subprocess.run(c, shell=True)
    time.sleep(1.0)
def netdown(): subprocess.run('ip link del enp0s3 2>/dev/null; ip link del vb0 2>/dev/null; true', shell=True)
def prep(): subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
def stage(scene, steps):
    prep()
    if scene == 'ipdemo': netup()
    p = xterm_start(); focus(); r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        elif st[0] == 'keys': r.keys(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5); subprocess.run('pkill -u student; true', shell=True); netdown()
STAGES = {
 'ipdemo': [('cmd', 'i1', 'ip -br addr show enp0s3'), ('cmd', 'i5', 'ip route show dev enp0s3')],
 'privdemo': [('cmd', 'v1', 'ipwhat 192.168.1.25'), ('cmd', 'v3', 'ipwhat 172.20.5.9'), ('cmd', 'v5', 'ipwhat 8.8.8.8')],
 'cidrdemo': [('cmd', 'u1', 'subnet 192.168.1.0/24'), ('cmd', 'u4', 'subnet 192.168.1.0/26'), ('cmd', 'u6', 'subnet 10.0.0.0/16')],
 'gwdemo': [('cmd', 'w1', 'inside 192.168.1.0/24 192.168.1.200'), ('cmd', 'w3', 'inside 192.168.1.0/24 8.8.8.8'), ('cmd', 'w5', 'grep nameserver /etc/resolv.conf')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
