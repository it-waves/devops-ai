"""Record Lesson 56 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson56')
from term import *
import video as V
LD = '/home/claude/academy/lesson56'
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
SED = r"""sed -i 's/1:\])/1:], key=int)/' top.py"""
PORTS = 'top.py 80 443 8080'
STAGES = {
 'start': [('cmd', 'st1', 'cd lab'), ('cmd', 'st2', 'ls'), ('cmd', 'st3', 'sudo install -m 755 lab56.sh /usr/local/sbin/'), ('cmd', 'st4', 'source shortcuts56.sh'), ('cmd', 'st5', 'lab up'), ('cmd', 'st6', 'lab check')],
 'fix1': [('cmd', 'f1', 'cd /opt/lab56/bin'), ('cmd', 'f2', 'python3 ' + PORTS), ('cmd', 'f3', """python3 -c "print(sorted(['80','443']))" """.strip()), ('cmd', 'f4', SED), ('cmd', 'f5', 'python3 ' + PORTS), ('cmd', 'f6', 'lab check')],
 'cleanup': [('cmd', 'c1', 'lab down'), ('cmd', 'c2', 'ls /opt/lab56'), ('cmd', 'c3', 'ls /opt | grep -c lab56'), ('cmd', 'c4', 'sudo rm /usr/local/sbin/lab56.sh'), ('cmd', 'c5', 'ls /usr/local/sbin | wc -l')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
