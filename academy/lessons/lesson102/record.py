"""Record Lesson 102 live terminal demo: a broken GitHub Actions workflow, the Gradle build the runner would run, and the repaired workflow. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson102')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson102'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab102.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB102_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip SUDO_USER=student sh {LAB} up > /tmp/lab102up.log 2>&1', shell=True)
    subprocess.run('mkdir -p /opt/lab102/demo && printf "    <dependency>\\n      <groupId>org.apache.commons</groupId>\\n      <artifactId>commons-lang3</artifactId>\\n      <version>3.12.0</version>\\n    </dependency>\\n" > /opt/lab102/demo/dep.xml && chown -R student /opt/lab102', shell=True)
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
  ('cmd', 'p0', 'cd /opt/lab102/cartcore'),
  ('cmd', 'w1', 'grep -c . pom.xml build.gradle'),
  ('cmd', 'w2', 'cat ../demo/dep.xml'),
  ('cmd', 'm1', "sed -i '/<dependencies>/r ../demo/dep.xml' pom.xml"),
  ('cmd', 'm2', "mvn package 2>&1 | grep -E 'BUILD|Total time'"),
  ('cmd', 'm3', 'ls target/*.jar'),
  ('cmd', 'g1', "sed -i \"/^dependencies {/a \\    implementation 'org.apache.commons:commons-lang3:3.12.0'\" build.gradle"),
  ('cmd', 'g2', "./gradlew build 2>&1 | grep -E 'BUILD|actionable'"),
  ('cmd', 'g3', 'ls build/libs'),
  ('cmd', 'r1', "mvn package 2>&1 | grep -E 'Nothing|BUILD'"),
  ('cmd', 'r2', "./gradlew build 2>&1 | grep -E 'UP-TO-DATE|BUILD'"),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
