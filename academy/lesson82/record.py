"""Record Lesson 82 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson82')
from term import *
import video as V
LD = '/home/claude/academy/lesson82'
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
 'tests': [('cmd', 't0', 'cd shop'), ('cmd', 't1', 'javac -d out/main src/main/com/cloudcart/Cart.java'), ('cmd', 't2', 'javac -cp out/main -d out/test src/test/com/cloudcart/CartTest.java'), ('cmd', 't3', 'java -cp out/main:out/test com.cloudcart.CartTest'), ('cmd', 't4', 'echo $?'), ('cmd', 't5', "sed -i 's|total / 10|total - total / 10|' src/main/com/cloudcart/Cart.java"), ('cmd', 't6', 'javac -d out/main src/main/com/cloudcart/Cart.java'), ('cmd', 't7', 'java -cp out/main:out/test com.cloudcart.CartTest'), ('cmd', 't8', 'echo $?')],
 'outputs': [('cmd', 'b0', 'cd shop'), ('cmd', 'b1', 'javac -d out/main src/main/com/cloudcart/Cart.java'), ('cmd', 'b2', 'javac -cp out/main -d out/test src/test/com/cloudcart/CartTest.java'), ('cmd', 'b3', 'find out -type f | sort'), ('cmd', 'b4', 'jar cf cloudcart.jar -C out/main .'), ('cmd', 'b5', 'jar tf cloudcart.jar'), ('cmd', 'b6', 'rm -r out cloudcart.jar'), ('cmd', 'b7', 'ls')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
