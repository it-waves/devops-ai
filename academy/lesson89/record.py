"""Record Lesson 89 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson89')
from term import *
import video as V
LD = '/home/claude/academy/lesson89'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5 + (18 if scene in ('war',) else 0))
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'war': [('cmd', 'w0', 'cd demo'), ('cmd', 'w1', 'mvn -B -q clean package && ls target'), ('cmd', 'w2', "sed -i 's/<packaging>jar/<packaging>war/' pom.xml"), ('cmd', 'w3', "sed -i '/<build>/a\\    <finalName>cloudcart</finalName>' pom.xml"), ('cmd', 'w4', 'mvn -B -q clean package && ls target'), ('cmd', 'w5', "unzip -Z1 target/cloudcart.war | grep -v '/$'"), ('cmd', 'w6', "sed -i '/<artifactId>liba/a\\      <scope>provided</scope>' pom.xml"), ('cmd', 'w7', "mvn -B -q clean package && unzip -Z1 target/cloudcart.war | grep -v '/$'")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
