"""Record Lesson 80 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson80')
from term import *
import video as V
LD = '/home/claude/academy/lesson80'
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
 'jar': [('cmd', 'j0', 'cd shop'), ('cmd', 'j1', 'javac -d out src/com/cloudcart/Hello.java'), ('cmd', 'j2', 'jar cf app.jar -C out .'), ('cmd', 'j3', 'java -jar app.jar'), ('cmd', 'j4', 'jar cfe app.jar com.cloudcart.Hello -C out .'), ('cmd', 'j5', 'java -jar app.jar'), ('cmd', 'j6', 'unzip -p app.jar META-INF/MANIFEST.MF')],
 'war': [('cmd', 'w0', 'cd shop'), ('cmd', 'w1', 'find war -type f | sort'), ('cmd', 'w2', 'jar cf shop.war -C war .'), ('cmd', 'w3', 'jar tf shop.war'), ('cmd', 'w4', 'java -jar shop.war'), ('cmd', 'w5', 'unzip -p shop.war WEB-INF/web.xml | head -n 3')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
