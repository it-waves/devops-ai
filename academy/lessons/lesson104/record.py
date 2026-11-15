"""Record Lesson 104 live terminal demo: a real Tomcat. usage: record.py STAGE"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson104')
import term
from term import *
import video as V
LD = '/home/claude/academy/lesson104'
PFX = ['unshare', '-mu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
LAB = '/home/claude/devops-ai/academy/lab/lab104.sh'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; rm -f /home/student/.ready; true', shell=True); time.sleep(0.8)
    subprocess.run(f'LAB104_TOMCAT_URL=file:///opt/dist/apache-tomcat-10.1.34.tar.gz SUDO_USER=student sh {LAB} up > /tmp/lab104up.log 2>&1', shell=True)
    p = xterm_start(PFX); term.WIN[:] = [1080, 600]; focus()
    for _ in range(400):
        if os.path.exists('/home/student/.ready'): break
        time.sleep(1)
    time.sleep(2); key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run(f'pkill -u student; pkill -f catalina.base; SUDO_USER=student sh {LAB} down >/dev/null 2>&1; true', shell=True)
STAGES = {
 'live': [
  ('cmd', 'p0', 'cd /opt/lab104/tomcat'),
  ('cmd', 'l1', 'ls -d bin conf lib logs webapps work'),
  ('cmd', 'l2', "grep -n -m1 -A2 '<Connector' conf/server.xml"),
  ('cmd', 'l3', 'bin/startup.sh 2>&1 | tail -n 1'),
  ('cmd', 'l4', 'ps -o pid,rss,comm -C java'),
  ('cmd', 'l5', "curl -s -o /dev/null -w '%{http_code}\\n' localhost:8080"),
  ('cmd', 'l6', 'ls webapps'),
  ('cmd', 'l7', "curl -s localhost:8080/examples/servlets/servlet/HelloWorldExample | grep -o '<h1>.*</h1>'"),
  ('cmd', 'l8', 'unzip -l ../demo/hello.war'),
  ('cmd', 'l9', 'cp ../demo/hello.war webapps/'),
  ('cmd', 'l10', 'sleep 15; ls webapps | tr "\\n" " "'),
  ('cmd', 'l11', "curl -s localhost:8080/hello/ | head -n 1"),
  ('cmd', 'l12', 'bin/shutdown.sh >/dev/null 2>&1'),
  ('cmd', 'l13', "sleep 3; curl -s -o /dev/null -w '%{http_code}\\n' localhost:8080"),
 ],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
