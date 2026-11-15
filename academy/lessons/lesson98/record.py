"""Record Lesson 98 live terminal demo: Gradle build, test and dependency inspection. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson98')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson98'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab98.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB98_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip SUDO_USER=student sh {LAB} up > /tmp/lab98up.log 2>&1', shell=True)
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
  ('cmd', 'p0', 'cd /opt/lab98/cartcore'),
  ('cmd', 'f1', 'cat gradle.properties'),
  ('cmd', 's1', './gradlew -q showConfig'),
  ('cmd', 'r1', "sed -i '/repoPassword/d' gradle.properties"),
  ('cmd', 's2', './gradlew -q showConfig'),
  ('cmd', 'g1', "echo 'greeting=Welcome to CloudCart' >> gradle.properties"),
  ('cmd', 'g2', './gradlew -q showConfig'),
  ('cmd', 'o1', './gradlew -q showConfig -Pgreeting=Hello'),
  ('cmd', 'e1', 'ORG_GRADLE_PROJECT_repoPassword=test123 ./gradlew -q showConfig'),
  ('cmd', 'c1', 'grep -r test123 . | wc -l'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
