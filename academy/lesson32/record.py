"""Record Lesson 32 live terminal demos in a clean standard-layout root. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson32')
from term import *
import video as V
LD = '/home/claude/academy/lesson32'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
def stage(scene, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus()
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
SRC = '/etc/apt/sources.list.d/ubuntu.sources'
STAGES = {
 'repo': [('cmd', 'q1', 'grep ^URIs ' + SRC), ('cmd', 'q3', 'grep ^Suites ' + SRC), ('cmd', 'q5', 'apt-cache policy curl | head -n 4')],
 'installed': [('cmd', 'd1', 'dpkg -s curl | head -n 4'), ('cmd', 'd3', 'dpkg -S /usr/bin/curl'), ('cmd', 'd5', 'dpkg -L curl | grep bin')],
 'plan': [('cmd', 'n1', 'apt-get -s install cowsay | tail -n 6'), ('cmd', 'n4', 'apt-get -s remove curl | tail -n 4'), ('cmd', 'n6', 'apt-get -s upgrade | grep "^[0-9]"')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
