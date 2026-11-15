"""Record Lesson 97 live terminal demo: Gradle build, test and dependency inspection. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson97')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson97'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab97.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB97_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip SUDO_USER=student sh {LAB} up > /tmp/lab97up.log 2>&1', shell=True)
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
  ('cmd', 'p0', 'cd /opt/lab97/cartcore'),
  ('cmd', 'r1', "grep -A2 '^repositories' build.gradle"),
  ('cmd', 'd1', "grep -A5 '^dependencies' build.gradle"),
  ('cmd', 'j1', "./gradlew dependencies --configuration runtimeClasspath | grep -c junit"),
  ('cmd', 'f1', "sed -i \"s/^    implementation 'org.junit/    testImplementation 'org.junit/\" build.gradle"),
  ('cmd', 'j2', "./gradlew dependencies --configuration runtimeClasspath | grep -c junit"),
  ('cmd', 'v1', "printf '[versions]\\ncommons-text = \"1.10.0\"\\n\\n[libraries]\\n' > gradle/libs.versions.toml"),
  ('cmd', 'v2', "printf 'commons-text = { module = \"org.apache.commons:commons-text\", version.ref = \"commons-text\" }\\n' >> gradle/libs.versions.toml"),
  ('cmd', 'v3', 'cat gradle/libs.versions.toml'),
  ('cmd', 'u1', "sed -i \"s#'org.apache.commons:commons-text:1.10.0'#libs.commons.text#\" build.gradle"),
  ('cmd', 'u2', 'grep -n commons build.gradle'),
  ('cmd', 'u3', "./gradlew test 2>&1 | grep BUILD"),
  ('cmd', 'm1', "sed -i \"s/id 'java'/id 'java'\\n    id 'maven-publish'/\" build.gradle"),
  ('cmd', 'm2', "grep -A3 '^plugins' build.gradle"),
  ('cmd', 'm3', "printf '\\npublishing {\\n  publications { maven(MavenPublication) { from components.java } }\\n' >> build.gradle"),
  ('cmd', 'm4', "printf '  repositories { maven { url = layout.buildDirectory.dir(\"repo\") } }\\n}\\n' >> build.gradle"),
  ('cmd', 'g1', "./gradlew publish 2>&1 | grep BUILD"),
  ('cmd', 'q1', "find build/repo -name 'cartcore-1.2.*' | grep -v -E 'sha|md5'"),
  ('cmd', 'q2', "grep artifactId build/repo/com/cloudcart/cartcore/1.2/cartcore-1.2.pom"),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
