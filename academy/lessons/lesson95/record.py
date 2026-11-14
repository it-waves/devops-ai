"""Record Lesson 95 live terminal demo: a real Gradle project, wrapper and task graph. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson95')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson95'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab95.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB95_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip SUDO_USER=student sh {LAB} up > /tmp/lab95up.log 2>&1', shell=True)
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
  ('cmd', 'p0', 'cd /opt/lab95/cartcore'), ('cmd', 'p1', 'ls'), ('cmd', 's1', 'cat settings.gradle'),
  ('cmd', 'g1', "grep -v '^$' build.gradle"),
  ('cmd', 'w1', 'grep distributionUrl gradle/wrapper/gradle-wrapper.properties'),
  ('cmd', 'v1', "./gradlew --version | grep -E '^Gradle|Launcher'"),
  ('cmd', 't1', "./gradlew tasks --group=build | grep ' - '"),
  ('cmd', 'g2', './gradlew build -m | head -n 12'),
  ('cmd', 'r1', "./gradlew build | grep -E 'BUILD|actionable'"),
  ('cmd', 'r2', "./gradlew build | grep -E 'BUILD|actionable'"),
  ('cmd', 'e1', "sed -i \"s/^version = .*/version = '1.1'/\" build.gradle"),
  ('cmd', 'e2', './gradlew build -q; ls build/libs'),
  ('cmd', 'c1', "echo 'tasks.register(\"report\") {dependsOn \"build\"; doLast {println \"$project.name $project.version\"}}' >> build.gradle"),
  ('cmd', 'c2', './gradlew -q report'),
  ('cmd', 'c3', "./gradlew report -m | grep -E ':build|:report'"),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
