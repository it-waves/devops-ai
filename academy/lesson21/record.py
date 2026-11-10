"""Record Lesson 21 live terminal demos in a real 3-namespace lab. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson21')
from term import *
import video as V
LD = '/home/claude/academy/lesson21'
def stage(scene, where, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    subprocess.run('/usr/local/bin/lab21.sh up', shell=True); time.sleep(1)
    p = xterm_start(prefix=['ip', 'netns', 'exec', where]); focus(); r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; /usr/local/bin/lab21.sh down; true', shell=True)
STAGES = {
 'ipdemo': ('client', [('cmd', 'i1', 'ip -br addr'), ('cmd', 'i3', 'ip route')]),
 'pingdemo': ('client', [('cmd', 'p1', 'ping -c 3 10.0.1.1'), ('cmd', 'p3', 'ping -c 3 10.0.2.2'), ('cmd', 'p5', 'ping -c 2 -W 1 10.0.3.9')]),
 'tracedemo': ('client', [('cmd', 't1', 'traceroute -n 10.0.2.2')]),
 'ssdemo': ('srv', [('cmd', 's1', 'ss -ltn'), ('cmd', 's3', 'ss -ltn sport = :9090')]),
 'diagdemo': ('client', [('cmd', 'd1', 'ping -c 1 wbe.lab.test'), ('cmd', 'd3', 'dig +short web.lab.test'), ('cmd', 'd5', 'ping -c 1 10.0.2.2'), ('cmd', 'd7', 'curl -sS -m 3 http://web.lab.test:9090'), ('cmd', 'd9', 'curl -s http://web.lab.test:8080')]),
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, *STAGES[s])
