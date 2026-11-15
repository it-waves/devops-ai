"""Record Lesson 103 live terminal demo: fix, prove and publish a Gradle release. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson103')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson103'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab103.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB103_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip SUDO_USER=student sh {LAB} up > /tmp/lab103up.log 2>&1', shell=True)
    p = xterm_start(PFX); term.WIN[:] = [1080, 600]; focus()
    for _ in range(400):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(2); key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run(f'pkill -u student; pkill -f GradleDaemon; SUDO_USER=student sh {LAB} down >/dev/null 2>&1; true', shell=True)
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab103/cartcore'),
  ('cmd', 'f1', "./gradlew build 2>&1 | grep -A3 'went wrong'"),
  ('cmd', 'f2', "sed -i 's/5.10.99/5.10.2/' build.gradle"),
  ('cmd', 'f3', "./gradlew build 2>&1 | grep -E 'FAILED|tests completed'"),
  ('cmd', 'f4', "sed -i 's/cents + /cents - /' src/main/java/com/cloudcart/Cart.java"),
  ('cmd', 'f5', "./gradlew build 2>&1 | tail -n 3"),
  ('cmd', 'r1', "for n in 1 2; do ./gradlew -q clean build; sha256sum build/libs/*.jar | cut -c1-16; sleep 2; done"),
  ('cmd', 'r2', "echo 'tasks.withType(AbstractArchiveTask){preserveFileTimestamps=false;reproducibleFileOrder=true}' >> build.gradle"),
  ('cmd', 'r3', "for n in 1 2; do ./gradlew -q clean build; sha256sum build/libs/*.jar | cut -c1-16; sleep 2; done"),
  ('cmd', 's1', "grep -n releaseKey build.gradle"),
  ('cmd', 's2', "sed -i \"s/releaseKey = '.*'/releaseKey = System.getenv('REPO_PASS')/\" build.gradle"),
  ('cmd', 's3', "./gradlew publish 2>&1 | grep -E 'no release key|BUILD'"),
  ('cmd', 's4', 'export REPO_PASS=$(cat ../pass.txt)'),
  ('cmd', 's5', "./gradlew publish 2>&1 | grep -E 'releasing|BUILD'"),
  ('cmd', 's6', "ls ../repo/com/cloudcart/cartcore/2.0 | grep -E 'jar$|pom$'"),
  ('cmd', 's7', 'grep -c "$REPO_PASS" build.gradle'),
  ('cmd', 'x1', "printf 'problems: four, all found\\nfixes: four, all tested\\ncleanup: run lab down at the end\\n' > report.txt"),
  ('cmd', 'x2', "lab check | tail -n 1"),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
