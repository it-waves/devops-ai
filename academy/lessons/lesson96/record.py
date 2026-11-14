"""Record Lesson 96 live terminal demo: Gradle build, test and dependency inspection. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson96')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson96'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab96.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB96_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip SUDO_USER=student sh {LAB} up > /tmp/lab96up.log 2>&1', shell=True)
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
  ('cmd', 'p0', 'cd /opt/lab96/cartcore'), ('cmd', 'p1', "find src -name '*.java'"),
  ('cmd', 'd1', "grep -A5 '^dependencies' build.gradle"),
  ('cmd', 'b1', "./gradlew build 2>&1 | grep -E 'FAILED|completed|BUILD'"),
  ('cmd', 'b2', "./gradlew test 2>&1 | grep -o 'expected.*'"),
  ('cmd', 'c1', 'grep -n -A2 totalWith src/main/java/cloudcart/Cart.java'),
  ('cmd', 'f1', "sed -i 's#total() - percent#total() * (1 - percent / 100)#' src/main/java/cloudcart/Cart.java"),
  ('cmd', 't2', "./gradlew test 2>&1 | grep -E 'FAILED|BUILD'"),
  ('cmd', 'x1', "grep -oh 'tests=\"[0-9]*\" skipped=\"[0-9]*\" failures=\"[0-9]*\"' build/test-results/test/*.xml"),
  ('cmd', 'r1', 'ls build/reports/tests/test'),
  ('cmd', 'y1', "./gradlew dependencies --configuration runtimeClasspath | grep -E 'runtime|commons'"),
  ('cmd', 'i1', "./gradlew dependencyInsight --dependency commons-lang3 --configuration runtimeClasspath | grep -E 'reasons|conflict'"),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
