"""Record Lesson 87 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson87')
from term import *
import video as V
LD = '/home/claude/academy/lesson87'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5 + (18 if scene in ('cfg', 'repro') else 0))
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'cfg': [('cmd', 'p0', 'cd demo'), ('cmd', 'p1', 'sed -n 8,19p pom.xml'), ('cmd', 'p2', 'cat src/main/resources/app.properties'), ('cmd', 'p3', 'mvn -B -q package && java -jar target/shop-1.0.0.jar'), ('cmd', 'p4', 'mvn -B -q clean package -Pprod && java -jar target/shop-1.0.0.jar'), ('cmd', 'p5', 'mvn -B -q clean package -Dapp.greeting=Hi && java -jar target/shop-1.0.0.jar'), ('cmd', 'p6', 'unzip -p target/shop-1.0.0.jar META-INF/MANIFEST.MF | grep Main')],
 'repro': [('cmd', 'y0', 'cd demo'), ('cmd', 'y1', 'mvn -B -q clean package; sha256sum target/shop-1.0.0.jar | cut -c1-16'), ('cmd', 'y2', 'mvn -B -q clean package; sha256sum target/shop-1.0.0.jar | cut -c1-16'), ('cmd', 'y3', "sed -i '8a\\    <project.build.outputTimestamp>2024-01-01T00:00:00Z</project.build.outputTimestamp>' pom.xml; sed -n 8,10p pom.xml"), ('cmd', 'y4', 'mvn -B -q clean package; sha256sum target/shop-1.0.0.jar | cut -c1-16'), ('cmd', 'y5', 'mvn -B -q clean package; sha256sum target/shop-1.0.0.jar | cut -c1-16')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
