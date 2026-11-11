"""Record Lesson 25 live terminal demos in the mastery lab. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson25')
from term import *
import video as V
LD = '/home/claude/academy/lesson25'
def stage(scene, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    subprocess.run('/usr/local/bin/lab25.sh up', shell=True)
    p = xterm_start()
    focus(); r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; /usr/local/bin/lab25.sh down; true', shell=True)
P = 'ping -c 1 -W 1 10.0.2.2'
STAGES = {
 'setup': [('cmd', 'u2', 'lab check')],
 'fix1': [('cmd', 'a1', 'cl ' + P), ('cmd', 'a3', 'cl traceroute -n -w 1 -q 1 -m 3 10.0.2.2'), ('cmd', 'a5', 'rt sysctl net.ipv4.ip_forward'), ('cmd', 'a7', 'rt sysctl -w net.ipv4.ip_forward=1'), ('cmd', 'a8', 'cl ' + P), ('cmd', 'a10', 'lab check')],
 'cleanup': [('cmd', 'k1', 'lab down'), ('cmd', 'k2', 'ip netns list | wc -l'), ('cmd', 'k4', 'pgrep -fc web25.py')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
