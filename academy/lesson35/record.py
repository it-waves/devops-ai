"""Record Lesson 35 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson35')
from term import *
import video as V
LD = '/home/claude/academy/lesson35'
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
        elif st[0] == 'type':   # typed into a prompt, no screen clear
            r.clear = False; r.cmd(st[1], st[2]); r.clear = True
        elif st[0] == 'answer':  # answer a prompt shortly after the command
            time.sleep(1.8); typ(st[2], 80); key('Return')
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True)
STAGES = {
 'perms': [('cmd', 'p1', './backup.sh'), ('cmd', 'p2', 'ls -l backup.sh'), ('cmd', 'p4', 'chmod u+x backup.sh'), ('cmd', 'p5', './backup.sh')],
 'disk': [('cmd', 'd1', 'echo hello > mnt/new.txt'), ('cmd', 'd2', 'df -h mnt'), ('cmd', 'd3', 'du -ah mnt 2>/dev/null | sort -rh | head -n 3'), ('cmd', 'd4', 'rm mnt/old-dump.log'), ('cmd', 'd5', 'echo hello > mnt/new.txt && echo saved'), ('cmd', 'd6', 'df -h mnt')],
 'net': [('cmd', 't1', 'nc -zv 127.0.0.1 8080'), ('cmd', 't2', 'ss -tln | grep 8080'), ('cmd', 't4', 'python3 -m http.server 8080 &>/dev/null &'), ('cmd', 't5', 'nc -zv 127.0.0.1 8080'), ('cmd', 't6', 'ss -tln | grep 8080')],
 'svc': [('cmd', 's1', 'cat web.service'), ('cmd', 's2', 'systemd-analyze verify web.service 2>&1 | grep web'), ('cmd', 's4', 'ls /usr/bin/python3'), ('cmd', 's5', "sed -i.bak 's/pythn3/python3/' web.service"), ('cmd', 's6', 'systemd-analyze verify web.service 2>&1 | grep web'), ('cmd', 's7', 'diff web.service.bak web.service')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
