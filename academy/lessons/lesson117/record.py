"""Record Lesson 117: the v0 mastery run from a clean clone. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson117')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson117'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab117.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB117_TOMCAT_BASE=file:///opt/dist LAB117_SRC_URL=file:///home/claude/devops-ai/academy/lab/assets/cloudcart-src-0.2.0.tgz SUDO_USER=student sh {LAB} up > /tmp/lab117up.log 2>&1', shell=True)
    p = xterm_start(PFX); term.WIN[:] = [1080, 600]; focus()
    for _ in range(400):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(2); key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run(f'pkill -u student; SUDO_USER=student sh {LAB} down >/dev/null 2>&1; true', shell=True)
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab117'),
  ('cmd', 'l1', 'ls'),
  ('cmd', 'l2', 'git clone origin.git work'),
  ('cmd', 'l3', 'cd work'),
  ('cmd', 'l4', 'git status -sb'),
  ('cmd', 'l5', 'git log --oneline'),
  ('cmd', 'l6', "mvn package | grep 'Tests run:' | tail -n 1"),
  ('cmd', 'l7', 'ls -l target/cloudcart.war'),
  ('cmd', 'l8', 'cp target/cloudcart.war ../tomcat/webapps/cloudcart.war'),
  ('cmd', 'l9', '../tomcat/bin/startup.sh | tail -n 1; curl localhost:8089/cloudcart/health'),
  ('cmd', 'l10', 'sleep 15; curl -s localhost:8089/cloudcart/health'),
  ('cmd', 'l11', "curl -s localhost:8089/cloudcart/api/products | grep -o '\"name\"' | wc -l"),
  ('cmd', 'l12', 'git tag cloudcart-v0'),
  ('cmd', 'l13', 'git push origin cloudcart-v0'),
  ('cmd', 'l14', 'echo "commit: $(git rev-parse --short HEAD)" > ../evidence.txt'),
  ('cmd', 'l15', 'echo "tests: 32" >> ../evidence.txt'),
  ('cmd', 'l16', 'echo "sha: $(sha256sum target/cloudcart.war | cut -c1-12)" >> ../evidence.txt'),
  ('cmd', 'l17', 'echo "version: 0.2.0" >> ../evidence.txt'),
  ('cmd', 'l18', 'cat ../evidence.txt'),
  ('cmd', 'l19', 'lab check'),
  ('cmd', 'l20', 'lab down'),
  ('cmd', 'l21', 'ss -ltn | grep -c 8089'),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
