"""Record Lesson 36 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson36')
from term import *
import video as V
LD = '/home/claude/academy/lesson36'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; pkill -f [h]ttp.server.8080; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True); time.sleep(0.5)
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
    subprocess.run('pkill -u student; pkill -f [h]ttp.server.8080; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True)
STAGES = {
 'start': [('cmd', 'st1', 'cd lab'), ('cmd', 'st2', 'ls'), ('cmd', 'st3', 'sudo install -m 755 lab36.sh /usr/local/sbin/'), ('cmd', 'st4', 'source shortcuts36.sh'), ('cmd', 'st5', 'lab up'), ('cmd', 'st6', 'lab check')],
 'fix1': [('cmd', 'f1', '/opt/lab36/bin/report.sh'), ('cmd', 'f2', 'ls -l /opt/lab36/bin'), ('cmd', 'f4', 'chmod u+x /opt/lab36/bin/report.sh'), ('cmd', 'f5', '/opt/lab36/bin/report.sh'), ('cmd', 'f6', 'lab check')],
 'cleanup': [('cmd', 'c1', 'lab down'), ('cmd', 'c2', 'mount | grep -c lab36'), ('cmd', 'c3', 'pgrep -fc "http.server 8080"'), ('cmd', 'c4', 'sudo iptables -S | grep -c 8080'), ('cmd', 'c5', 'ls /opt/lab36')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
