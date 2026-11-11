"""Record Lesson 30 live terminal demos in a clean standard-layout root with its own process namespace. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson30')
from term import *
import video as V
LD = '/home/claude/academy/lesson30'
PFX = ['unshare', '-m', '-p', '-f', 'sh', LD + '/enter.sh']
def stage(scene, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus()
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'ps': [('cmd', 'p1', 'ps'), ('cmd', 'p3', 'ps -eo pid,user,comm'), ('cmd', 'p5', 'ps -eo pid,pcpu,pmem,comm')],
 'signals': [('cmd', 's1', 'sleep 300 &'), ('cmd', 's2', 'jobs'), ('cmd', 's3', 'kill %1'), ('cmd', 's4', 'jobs'), ('cmd', 's5', 'yes > /dev/null &'), ('cmd', 's6', 'ps -eo pid,pcpu,comm --sort=-pcpu | head -n 4'), ('cmd', 's7', 'kill -9 %1')],
 'resources': [('cmd', 'r1', 'uptime'), ('cmd', 'r3', 'nproc'), ('cmd', 'r4', 'free -h | column -t')],
 'running': [('cmd', 'u1', 'sleep 300 &'), ('cmd', 'u2', 'pgrep -a sleep'), ('cmd', 'u3', 'pkill sleep'), ('cmd', 'u4', 'pgrep sleep'), ('cmd', 'u5', 'echo $?')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
