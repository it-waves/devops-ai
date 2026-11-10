"""Record Lesson 15 live terminal demos. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson15')
from term import *
import video as V
LD = '/home/claude/academy/lesson15'
def S(cmd): subprocess.run(['runuser', '-u', 'student', '--', 'bash', '-c', cmd], cwd='/home/student', capture_output=True)
def prep(scene):
    subprocess.run('pkill -u student; umount /home/student/data 2>/dev/null; true', shell=True); time.sleep(0.5)
def setup(scene):
    if scene == 'memdemo':
        S('printf "data = bytearray(500 * 1024 * 1024)\\nprint(\\"got 500 MB\\")\\n" > hog.py')
    if scene == 'diskdemo':
        S('mkdir -p data')
        subprocess.run('mount -t tmpfs -o size=10m,uid=$(id -u student),gid=$(id -g student) tmpfs /home/student/data', shell=True)
    if scene == 'logdemo':
        S('(python3 -m http.server 8080 > server.log 2>&1 & echo $! > .pid; sleep 1.5; curl -s localhost:8080 >/dev/null; curl -s localhost:8080/nope >/dev/null; curl -s localhost:8080 >/dev/null; sleep 0.5; kill $(cat .pid); rm .pid)')
def stage(scene, steps):
    prep(scene); p = xterm_start(); setup(scene); focus(); r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        elif st[0] == 'keys': r.keys(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5); subprocess.run('pkill -u student; umount /home/student/data 2>/dev/null; true', shell=True)
PS = 'ps -u student -o pid,pcpu,comm --sort=-pcpu'
STAGES = {
 'cpudemo': [('cmd', 'r2', 'nproc'), ('cmd', 'r4', 'yes > /dev/null &'), ('cmd', 'r6', PS), ('cmd', 'r8', 'kill %1'), ('keys', 'r9', ['ctrl+l', 'Up', 'Up', 'Return'])],
 'memdemo': [('cmd', 't1', 'free -h'), ('cmd', 't3', 'cat hog.py'), ('cmd', 't5', '(ulimit -v 200000; python3 hog.py) 2>&1 | tail -1')],
 'diskdemo': [('cmd', 'v2', 'df -h data'), ('cmd', 'v4', 'dd if=/dev/zero of=data/big.bin bs=1M count=20'), ('cmd', 'v6', 'df -h data'), ('cmd', 'v8', 'du -sh data/*'), ('cmd', 'v10', 'rm data/big.bin'), ('cmd', 'v11', 'df -h data')],
 'svcdemo': [('cmd', 'x2', 'python3 -m http.server 8080 >server.log 2>&1 &'), ('cmd', 'x3', 'curl -sI localhost:8080 | head -1'), ('cmd', 'x5', 'curl -sI localhost:8080/nope | head -1'),
             ('cmd', 'x7', 'python3 -m http.server 8080 2>&1 | tail -1'), ('cmd', 'x9', 'ss -ltn sport = :8080'), ('cmd', 'x10', 'kill %1'), ('cmd', 'x11', 'curl -sS localhost:8080')],
 'logdemo': [('cmd', 'z2', 'tail -n 4 server.log'), ('cmd', 'z4', 'grep 404 server.log'), ('cmd', 'z6', 'grep -c 404 server.log')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
