"""Record Lesson 45 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson45')
from term import *
import video as V
LD = '/home/claude/academy/lesson45'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True)
STAGES = {
 'layout': [('cmd', 'l1', 'ls releases'), ('cmd', 'l2', 'ls -l current'), ('cmd', 'l3', 'curl -s localhost:8080/version'), ('cmd', 'l4', 'curl -fs localhost:8080/health')],
 'script': [('cmd', 'sc1', 'cat release.sh'), ('cmd', 'sc2', 'shellcheck release.sh && echo clean')],
 'deploy': [('cmd', 'd1', 'bash release.sh v2'), ('cmd', 'd2', 'curl -s localhost:8080/version'), ('cmd', 'd3', 'readlink current'), ('cmd', 'd4', 'bash release.sh v2')],
 'rollback': [('cmd', 'r1', 'bash release.sh v3'), ('cmd', 'r2', 'echo $?'), ('cmd', 'r3', 'curl -s localhost:8080/version'), ('cmd', 'r4', 'readlink current'), ('cmd', 'r5', 'bash release.sh v1'), ('cmd', 'r6', 'curl -s localhost:8080/version')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
