"""Record Lesson 78 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson78')
from term import *
import video as V
LD = '/home/claude/academy/lesson78'
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
 'build': [('cmd', 'b0', 'cd shop'), ('cmd', 'b1', 'find src lib -type f | sort'), ('cmd', 'b2', 'cat src/com/cloudcart/Main.java'), ('cmd', 'b3', 'javac -d out src/com/cloudcart/Main.java'), ('cmd', 'b4', 'javac -cp lib/pricing.jar -d out src/com/cloudcart/Main.java'), ('cmd', 'b5', 'find out -type f'), ('cmd', 'b6', 'jar tf lib/pricing.jar'), ('cmd', 'b7', 'java -cp out:lib/pricing.jar com.cloudcart.Main')],
 'config': [('cmd', 'g0', 'cd shop'), ('cmd', 'g1', 'javac -cp lib/pricing.jar -d out src/com/cloudcart/Main.java'), ('cmd', 'g2', 'java -cp out com.cloudcart.Main 2>&1 | head -n 5'), ('cmd', 'g3', 'java com.cloudcart.Main'), ('cmd', 'g4', 'STORE_NAME=Bean java -cp out:lib/pricing.jar com.cloudcart.Main'), ('cmd', 'g5', 'java -Dcurrency=EUR -cp out:lib/pricing.jar com.cloudcart.Main')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
