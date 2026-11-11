"""Record Lesson 31 live terminal demos in a clean standard-layout root. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson31')
from term import *
import video as V
LD = '/home/claude/academy/lesson31'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
def stage(scene, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus()
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'unit': [('cmd', 'u1', 'head -n 14 /usr/lib/systemd/system/ssh.service')],
 'mine': [('cmd', 'm1', 'cat web.service'), ('cmd', 'm3', 'systemd-analyze verify web.service 2>&1 | grep -v Bind'), ('cmd', 'm5', 'cat bad.service'), ('cmd', 'm6', 'systemd-analyze verify bad.service 2>&1 | grep -v Bind')],
 'timers': [('cmd', 't1', 'systemd-analyze calendar "*-*-* 02:00"'), ('cmd', 't3', 'systemd-analyze calendar "Mon..Fri 09:00"')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
    subprocess.run('rm -f /home/student/web.service /home/student/bad.service', shell=True)
