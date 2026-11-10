"""Record Lesson 20 live terminal demos. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson20')
from term import *
import video as V
LD = '/home/claude/academy/lesson20'
def bg(cmd): subprocess.Popen(['su', 'student', '-c', cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True)
def prep():
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    subprocess.run('rm -f /home/student/udp.log', shell=True)
def stage(scene, steps):
    prep()
    orig = open('/etc/resolv.conf').read()
    dns = subprocess.Popen(['python3', '/usr/local/bin/dns20.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True)
    try:
        open('/etc/resolv.conf', 'w').write('nameserver 127.0.0.1\n'); time.sleep(1.5)
        if scene == 'e2edemo': bg('python3 /usr/local/bin/web19.py 8080'); time.sleep(1.5)
        p = xterm_start(); focus(); r = Run(LD, V, scene, delay=80)
        for st in steps:
            if st[0] == 'cmd': r.cmd(st[1], st[2])
            elif st[0] == 'keys': r.keys(st[1], st[2])
        r.end(); p.terminate(); time.sleep(0.5)
    finally:
        open('/etc/resolv.conf', 'w').write(orig); dns.terminate(); subprocess.run('pkill -u student; pkill -f dns20.py; true', shell=True)
STAGES = {
 'digdemo': [('cmd', 'g1', 'cat /etc/resolv.conf'), ('cmd', 'g3', 'dig www.lab.test +noall +answer'), ('cmd', 'g6', 'dig lab.test MX +noall +answer'), ('cmd', 'g8', 'dig nope.lab.test | grep status')],
 'e2edemo': [('cmd', 'e1', 'getent hosts www.lab.test'), ('cmd', 'e3', 'curl -s http://www.lab.test:8080'), ('cmd', 'e5', 'curl -sv www.lab.test:8080 2>&1 | grep -i connected')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
