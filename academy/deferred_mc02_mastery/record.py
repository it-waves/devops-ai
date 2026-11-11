"""Record Lesson 26 live terminal demos. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson26')
from term import *
import video as V
LD = '/home/claude/academy/lesson26'
def sh(c): subprocess.run(c, shell=True)
def stage(scene):
    sh('pkill -u student; true'); time.sleep(0.5)
    sh("su student -c 'cd ~ && ./lab26.sh down >/dev/null; ./lab26.sh up >/dev/null'"); time.sleep(1)
    pid = subprocess.run("pgrep -u student -f nightly-report.py | head -1", shell=True, capture_output=True, text=True).stdout.strip()
    PS = 'ps -u $USER -o pid,pcpu,comm --sort=-pcpu | head -4'
    STAGES = {
     'setup': [('cmd', 'u2', './lab26.sh check')],
     'fix1': [('cmd', 'a1', PS), ('cmd', 'a3', f'ps -o pid,etime,args -p {pid}'), ('cmd', 'a5', f'kill {pid}'), ('cmd', 'a6', PS), ('cmd', 'a8', './lab26.sh check')],
     'cleanup': [('cmd', 'k1', './lab26.sh down'), ('cmd', 'k2', 'ls /tmp/lab26'), ('cmd', 'k4', 'pgrep -fc /tmp/lab26')],
    }
    p = xterm_start(); focus(); r = Run(LD, V, scene, delay=80)
    for st in STAGES[scene]: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    sh("su student -c 'cd ~ && ./lab26.sh down >/dev/null'; pkill -u student; true")
if __name__ == '__main__':
    a = sys.argv[1:] or ['setup', 'fix1', 'cleanup']
    for s in a: print('==', s, flush=True); stage(s)
