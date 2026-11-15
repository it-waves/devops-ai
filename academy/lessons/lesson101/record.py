"""Record Lesson 100 live terminal demo: a broken GitHub Actions workflow, the Gradle build the runner would run, and the repaired workflow. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson101')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson101'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab101.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB101_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip SUDO_USER=student sh {LAB} up > /tmp/lab101up.log 2>&1', shell=True)
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
  ('cmd', 'p0', 'cd /opt/lab101/cartcore'),
  ('cmd', 'd1', "./gradlew jar 2>&1 | grep -A1 'went wrong'"),
  ('cmd', 'd2', 'cat gradle.properties'),
  ('cmd', 'd3', 'echo org.gradle.jvmargs=-Xmx512m > gradle.properties'),
  ('cmd', 'b1', "./gradlew jar 2>&1 | grep -A3 'went wrong'"),
  ('cmd', 'b2', './gradlew -q dependencies --configuration compileClasspath'),
  ('cmd', 'b3', "sed -i 's/3.99.1/3.12.0/' build.gradle"),
  ('cmd', 'c1', "./gradlew build 2>&1 | grep -A2 'went wrong'"),
  ('cmd', 'c2', 'grep -n percent src/main/java/com/cloudcart/Cart.java'),
  ('cmd', 'c3', "sed -i 's/cents + /cents - /' src/main/java/com/cloudcart/Cart.java"),
  ('cmd', 'c4', './gradlew build 2>&1 | tail -n 3'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
