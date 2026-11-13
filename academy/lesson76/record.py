"""Record Lesson 76 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson76')
from term import *
import video as V
LD = '/home/claude/academy/lesson76'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'tools': [('cmd', 't1', 'cd shop'), ('cmd', 't2', 'java -version'), ('cmd', 't3', 'javac -version'), ('cmd', 't4', 'dpkg -L openjdk-21-jre-headless | grep /bin/'), ('cmd', 't5', 'dpkg -L openjdk-21-jdk-headless | grep -c /bin/')],
 'compile': [('cmd', 'c0', 'cd shop'), ('cmd', 'c1', 'cat Hello.java'), ('cmd', 'c2', 'javac Hello.java'), ('cmd', 'c3', 'ls'), ('cmd', 'c4', 'xxd -l 8 Hello.class'), ('cmd', 'c5', 'java Hello')],
 'bytecode': [('cmd', 'b0', 'cd shop'), ('cmd', 'b0a', 'javac Hello.java'), ('cmd', 'b1', 'javap -c Hello | cut -c1-70 | head -n 13')],
 'process': [('cmd', 'p0', 'cd shop'), ('cmd', 'p1', 'javac ShopApp.java'), ('cmd', 'p2', 'java ShopApp > app.log &'), ('cmd', 'p3', 'jps -l'), ('cmd', 'p4', 'ps -C java -o pid,rss,args'), ('cmd', 'p5', 'kill %1'), ('cmd', 'p6', 'jps -l')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
