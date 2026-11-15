"""Record Lesson 114 live terminal demo: CloudCart project layout and the Maven build on real Maven Central. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson114')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson114'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab114.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB114_SRC_URL=file:///home/claude/devops-ai/academy/lab/assets/cloudcart-src-0.2.0.tgz SUDO_USER=student sh {LAB} up > /tmp/lab114up.log 2>&1', shell=True)
    p = xterm_start(PFX); term.WIN[:] = [1080, 600]; focus()
    for _ in range(400):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(2); key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run(f'pkill -u student; SUDO_USER=student sh {LAB} down >/dev/null 2>&1; true', shell=True)
FLT = "sed 's/\\[INFO\\] //; s/ (default-.*//'"
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab114/cloudcart'),
  ('cmd', 'd1', 'ls'),
  ('cmd', 'd2', 'find src/main -type f | sort | cut -c10-'),
  ('cmd', 'd3', 'find src/test -type f'),
  ('cmd', 'x1', 'sed -n 5,9p pom.xml'),
  ('cmd', 'x2', 'sed -n 15,27p pom.xml'),
  ('cmd', 'b1', "mvn -B test | grep -E '^.INFO. (--- [a-z]|Tests run: 32|BUILD)' | " + FLT),
  ('cmd', 'b2', 'ls target'),
  ('cmd', 'b3', "mvn -B package | grep -E '^.INFO. (--- war|Building war|BUILD)' | " + FLT),
  ('cmd', 'b4', 'ls -lh target/cloudcart.war'),
  ('cmd', 'w1', "unzip -Z1 target/cloudcart.war | grep -v '/$' | grep -v classes/academy"),
  ('cmd', 'w2', "unzip -Z1 target/cloudcart.war | grep -c '.class$'"),
  ('cmd', 'w3', 'unzip -p target/cloudcart.war WEB-INF/classes/version.properties'),
  ('cmd', 'w4', 'unzip -Z1 target/cloudcart.war | grep -c servlet'),
  ('cmd', 'v1', "sed -i 's#<version>0.2.0#<version>0.2.1#' pom.xml"),
  ('cmd', 'v2', 'mvn -B -q clean package'),
  ('cmd', 'v3', 'unzip -p target/cloudcart.war WEB-INF/classes/version.properties'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
