"""Record Lesson 19 live terminal demos. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson19')
from term import *
import video as V
LD = '/home/claude/academy/lesson19'
def bg(cmd): subprocess.Popen(['su', 'student', '-c', cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True)
def prep():
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    subprocess.run('rm -f /home/student/udp.log', shell=True)
def stage(scene, steps):
    prep()
    if scene in ('methoddemo', 'statusdemo'): bg('python3 /usr/local/bin/web19.py 8080'); time.sleep(1.5)
    if scene == 'tlsdemo': bg('python3 /usr/local/bin/web19.py 8443 tls'); time.sleep(1.5)
    p = xterm_start()
    if scene == 'tlsdemo': subprocess.run('mkdir -p /home/student/tls && cp /opt/lab19/cert.pem /home/student/tls/ && chown -R student /home/student/tls', shell=True)
    focus(); r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        elif st[0] == 'keys': r.keys(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5); subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'methoddemo': [('cmd', 'd1', 'curl -i localhost:8080'), ('cmd', 'd5', 'curl -s -X POST -d name=ana localhost:8080/form')],
 'statusdemo': [('cmd', 't1', 'curl -sI localhost:8080/missing | head -1'), ('cmd', 't3', 'curl -sI localhost:8080/old | grep -i "^HTTP\\|^loc"'), ('cmd', 't5', 'curl -sI localhost:8080/boom | head -1')],
 'tlsdemo': [('cmd', 'l1', 'curl -sSI https://localhost:8443 2>&1 | head -1'), ('cmd', 'l3', 'curl -skI https://localhost:8443 | head -1'), ('cmd', 'l5', 'openssl x509 -in tls/cert.pem -noout -subject -dates')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
