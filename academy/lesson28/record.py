"""Record Lesson 28 live terminal demos in a clean standard-layout root. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson28')
from term import *
import video as V
LD = '/home/claude/academy/lesson28'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
H = '/home/student'
def w(path, txt=''):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(txt)
def fixtures():
    L = H + '/lab28'
    w(L + '/app.log', 'INFO server started\nINFO user login ok\nWARNING disk at 82 percent\nERROR timeout on db\nINFO user login ok\nERROR timeout on cache\nINFO request served\nWARNING slow response\n')
    w(L + '/fruits.txt', 'apple\nbanana\napple\ncherry\nbanana\napple\n')
    w(L + '/users.csv', 'ana,admin\nben,dev\ncy,dev\n')
    w(L + '/project/app.conf', 'port=8080\n'); w(L + '/project/notes.txt', 'ship it safely\n'); w(L + '/project/run.log', 'started\n')
    w(L + '/logs/a.log', 'a\n'); w(L + '/logs/b.log', 'b\n')
    subprocess.run(['chown', '-R', 'student:student', H])
def stage(scene, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); fixtures()
    focus(); typ('cd lab28', 60); key('Return'); time.sleep(0.4); key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'redirect': [('cmd', 'r1', 'echo hello server > hello.txt'), ('cmd', 'r2', 'cat hello.txt'), ('cmd', 'r3', 'echo second line >> hello.txt'), ('cmd', 'r4', 'cat hello.txt'), ('cmd', 'r5', 'ls nothere 2> errors.txt'), ('cmd', 'r6', 'cat errors.txt')],
 'pipe': [('cmd', 'p1', 'ls /etc | head -n 5'), ('cmd', 'p3', 'ls /etc | wc -l'), ('cmd', 'p5', 'find . -name "*.log" | wc -l')],
 'grep': [('cmd', 'g1', 'grep ERROR app.log'), ('cmd', 'g2', 'grep -c ERROR app.log'), ('cmd', 'g3', 'grep -n ERROR app.log'), ('cmd', 'g4', 'grep -i warning app.log'), ('cmd', 'g5', 'grep -v INFO app.log'), ('cmd', 'g6', 'grep -r timeout .')],
 'sortcut': [('cmd', 't1', 'sort fruits.txt'), ('cmd', 't2', 'sort fruits.txt | uniq -c'), ('cmd', 't4', 'sort fruits.txt | uniq -c | sort -rn'), ('cmd', 't5', 'cut -d, -f1 users.csv')],
 'archive': [('cmd', 'a1', 'tar -czf backup.tar.gz project'), ('cmd', 'a2', 'ls -lh backup.tar.gz'), ('cmd', 'a3', 'tar -tzf backup.tar.gz'), ('cmd', 'a4', 'mkdir restore'), ('cmd', 'a5', 'tar -xzf backup.tar.gz -C restore'), ('cmd', 'a6', 'ls restore')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
