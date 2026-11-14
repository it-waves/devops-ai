"""Record Lesson 94 live terminal demo: four real Maven failures, on real Maven Central and a real Nexus. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson94')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson94'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab94.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'ACCEPT_NEXUS_EULA=yes SUDO_USER=student sh {LAB} up > /tmp/lab94up.log 2>&1', shell=True)
    p = xterm_start(PFX); term.WIN[:] = [1080, 600]; focus()
    for _ in range(400):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(2); key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run(f'pkill -u student; SUDO_USER=student sh {LAB} down >/dev/null 2>&1; true', shell=True)
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab94/cart-core'), ('cmd', 'p1', 'export CORP_PASS=$(cat ../pass.txt)'), ('cmd', 'p2', 'ls'),
  ('cmd', 'b1', "mvn -B clean package | grep -oE 'Cart.java.*symbol|symbol: .*' | head -2"),
  ('cmd', 'd1', "mvn -B dependency:tree | grep -o 'commons-lang3:jar:[0-9.]*'"),
  ('cmd', 'd2', "sed -i 's#<version>3.4</version>#<version>3.14.0</version>#' pom.xml"),
  ('cmd', 'b2', "mvn -B clean package | grep -om1 'expected.*'"),
  ('cmd', 'f1', "sed -i 's#name, 4#name, 5#' src/main/java/cloudcart/Cart.java"),
  ('cmd', 'b3', "mvn -B clean package | grep -E 'Tests run:|BUILD' | tail -2"),
  ('cmd', 'r1', "for n in 1 2; do mvn -B -q clean package >/dev/null; sha256sum target/*.jar | cut -c1-16; sleep 2; done"),
  ('cmd', 'r2', "sed -i '/<properties>/a <project.build.outputTimestamp>2024-01-01T00:00:00Z</project.build.outputTimestamp>' pom.xml"),
  ('cmd', 'r3', "for n in 1 2; do mvn -B -q clean package >/dev/null; sha256sum target/*.jar | cut -c1-16; sleep 2; done"),
  ('cmd', 'u1', "mvn -B -s settings.xml clean deploy | grep -oE 'cart-core-[0-9.]*-[0-9.]*-[0-9]*.jar' | sort -u"),
  ('cmd', 'u2', "curl -s -u admin:$CORP_PASS 'localhost:8081/service/rest/v1/search/assets?repository=corp-snapshots&maven.extension=jar' | grep -c '\"path\"'"),
  ('cmd', 'u3', 'grep -c "$CORP_PASS" pom.xml settings.xml'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
