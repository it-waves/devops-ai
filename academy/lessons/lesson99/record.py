"""Record Lesson 98 live terminal demo: Gradle build cache and reproducible builds. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson99')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson99'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab99.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB99_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip SUDO_USER=student sh {LAB} up > /tmp/lab99up.log 2>&1', shell=True)
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
  ('cmd', 'p0', 'cd /opt/lab99/cartcore'),
  ('cmd', 'b1', './gradlew jar'),
  ('cmd', 'b2', './gradlew jar'),
  ('cmd', 'w1', 'grep -n Built build.gradle'),
  ('cmd', 'w2', "sed -i '/Built-At/d' build.gradle"),
  ('cmd', 'w3', './gradlew jar'),
  ('cmd', 'w4', './gradlew jar'),
  ('cmd', 'c1', 'echo org.gradle.caching=true >> gradle.properties'),
  ('cmd', 'c2', './gradlew clean jar'),
  ('cmd', 'c3', './gradlew clean jar'),
  ('cmd', 'h1x', 'sha256sum build/libs/*.jar | cut -c1-12'),
  ('cmd', 'h2x', './gradlew -q clean jar'),
  ('cmd', 'h3x', 'sha256sum build/libs/*.jar | cut -c1-12'),
  ('cmd', 'r1', "printf 'jar {\\n  preserveFileTimestamps = false\\n  reproducibleFileOrder = true\\n}\\n' >> build.gradle"),
  ('cmd', 'r1t', 'tail -n 4 build.gradle'),
  ('cmd', 'r2', './gradlew -q clean jar'),
  ('cmd', 'r3', 'sha256sum build/libs/*.jar | cut -c1-12'),
  ('cmd', 'r4', './gradlew -q clean jar'),
  ('cmd', 'r5', 'sha256sum build/libs/*.jar | cut -c1-12'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
