"""Record Lesson 100 live terminal demo: a broken GitHub Actions workflow, the Gradle build the runner would run, and the repaired workflow. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson100')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson100'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab100.sh'
DEMO = '/home/claude/devops-ai/.github/workflows/gradle-ci.yml'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB100_GRADLE_ZIP_URL=file:///opt/dist/gradle-8.14.3-bin.zip SUDO_USER=student sh {LAB} up > /tmp/lab100up.log 2>&1', shell=True)
    subprocess.run(f'mkdir -p /opt/lab100/demo && cp {DEMO} /opt/lab100/demo/gradle-ci.yml && chmod -R a+rX /opt/lab100/demo', shell=True)
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
  ('cmd', 'p0', 'cd /opt/lab100/cartcore'),
  ('cmd', 't1', 'cat .github/workflows/ci.yml'),
  ('cmd', 't2', "grep -n -E 'branches|java-version|REPO_PASSWORD' .github/workflows/ci.yml"),
  ('cmd', 't3', "./gradlew build | grep -v '^$'"),
  ('cmd', 't4', 'ls build/libs'),
  ('cmd', 't5', 'cat -n ../demo/gradle-ci.yml | head -n 14'),
  ('cmd', 't6', 'cat -n ../demo/gradle-ci.yml | tail -n 14'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
