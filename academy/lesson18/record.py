"""Record Lesson 18 live terminal demos. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson18')
from term import *
import video as V
LD = '/home/claude/academy/lesson18'
def bg(cmd): subprocess.Popen(['su', 'student', '-c', cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True)
def prep():
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    subprocess.run('rm -f /home/student/udp.log', shell=True)
def stage(scene, steps):
    prep()
    if scene in ('servicedemo', 'statedemo', 'conflictdemo'): bg('cd /tmp && python3 -m http.server 8080 --bind 127.0.0.1'); time.sleep(1.5)
    if scene == 'statedemo': bg('python3 /usr/local/bin/hold18.py'); time.sleep(1.0)
    if scene == 'udpdemo': bg('python3 /usr/local/bin/udp18.py'); time.sleep(1.0)
    p = xterm_start(); focus(); r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        elif st[0] == 'keys': r.keys(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5); subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'servicedemo': [('cmd', 's1', 'getent services ssh http https'), ('cmd', 's3', "ss -ltn 'sport = :8080'"), ('cmd', 's5', 'curl -sI localhost:8080 | head -1')],
 'statedemo': [('cmd', 'n1', "ss -tn 'sport = :8080'"), ('cmd', 'n3', 'curl -s localhost:8080 >/dev/null'), ('cmd', 'n4', "ss -tan 'sport = :8080'")],
 'udpdemo': [('cmd', 'u1', "ss -lun 'sport = :9999'"), ('cmd', 'u3', 'echo hello | nc -u -w1 127.0.0.1 9999'), ('cmd', 'u5', 'cat udp.log')],
 'conflictdemo': [('cmd', 'q2', 'curl -s localhost:8081; echo "exit code $?"'), ('cmd', 'q4', 'python3 -m http.server 8080 2>&1 | tail -1')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
