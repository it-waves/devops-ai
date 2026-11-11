"""Record Lesson 40 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson40')
from term import *
import video as V
LD = '/home/claude/academy/lesson40'
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
 'grep': [('cmd', 'r1', 'cat app.log'), ('cmd', 'r2', 'grep ERROR app.log'), ('cmd', 'r3', 'grep -c INFO app.log'), ('cmd', 'r4', 'grep -v INFO app.log'), ('cmd', 'r5', 'grep -n timeout app.log'), ('cmd', 'r6', 'grep -E "WARN|ERROR" app.log')],
 'cutsort': [('cmd', 'p1', 'cat users.csv'), ('cmd', 'p2', 'cut -d, -f1 users.csv'), ('cmd', 'p3', 'sort -t, -k3 -n users.csv'), ('cmd', 'p4', 'cut -d, -f2 users.csv | sort | uniq -c')],
 'sed': [('cmd', 's1', 'cat config.txt'), ('cmd', 's2', "sed 's/dev/prod/' config.txt"), ('cmd', 's3', 'cat config.txt'), ('cmd', 's4', "sed -i 's/8080/9090/' config.txt"), ('cmd', 's5', 'cat config.txt'), ('cmd', 's6', "sed '/mode/d' config.txt")],
 'awk': [('cmd', 'a1', 'cat users.csv'), ('cmd', 'a2', "awk -F, '{print $1}' users.csv"), ('cmd', 'a3', "awk -F, 'NR > 1 && $3 > 30 {print $1, $3}' users.csv"), ('cmd', 'a4', "awk -F, 'NR > 1 {sum += $3} END {print sum / (NR - 1)}' users.csv")],
 'find': [('cmd', 'n1', 'ls -R'), ('cmd', 'n2', 'find . -name "*.log"'), ('cmd', 'n3', 'find . -name "*.log" -mtime +7'), ('cmd', 'n4', 'find . -name "*.log" -exec wc -l {} +')],
 'build': [('cmd', 'w1', 'cat app.log'), ('cmd', 'w2', "awk '{print $3}' app.log | sort | uniq -c"), ('cmd', 'w3', "grep ERROR app.log | awk '{print $2, $4}'")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
