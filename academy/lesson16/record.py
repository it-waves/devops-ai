"""Record Lesson 16 live terminal demos. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson16')
from term import *
import video as V
LD = '/home/claude/academy/lesson16'
APP = '''import time
from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health': code, body = 200, '{"status": "ok"}'
        elif self.path == '/crash': code, body = 500, '{"error": "internal error"}'
        elif self.path == '/slow': time.sleep(2); code, body = 200, '{"status": "ok"}'
        else: code, body = 404, '{"error": "not found"}'
        self.send_response(code); self.send_header('Content-Type', 'application/json'); self.end_headers(); self.wfile.write((body + '\\n').encode())
    def log_message(self, *a): pass
HTTPServer(('127.0.0.1', 5000), H).serve_forever()
'''
TIMING = 'dns: %{time_namelookup}\\n\\nconnect: %{time_connect}\\n\\nfirst byte: %{time_starttransfer}\\n\\ntotal: %{time_total}\\n'
def prep():
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
def setup(scene):
    open('/tmp/app16.py', 'w').write(APP); os.chmod('/tmp/app16.py', 0o644)
    subprocess.Popen(['runuser', '-u', 'student', '--', 'python3', '/tmp/app16.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True); time.sleep(1.2)
    if scene == 'tracedemo':
        t = 'dns: %{time_namelookup}\\n\nconnect: %{time_connect}\\n\nfirst byte: %{time_starttransfer}\\n\ntotal: %{time_total}\\n\n'
        open('/home/student/timing.txt', 'w').write(t); subprocess.run(['chown', 'student:student', '/home/student/timing.txt'])
def stage(scene, steps):
    prep(); p = xterm_start(); setup(scene); focus(); r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        elif st[0] == 'keys': r.keys(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5); subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'dnsdemo': [('cmd', 'n2', 'curl web:5000/health'), ('cmd', 'n4', 'curl --resolve web:5000:127.0.0.1 web:5000/health'), ('cmd', 'n7', 'getent hosts localhost')],
 'reqdemo': [('cmd', 'r2', "curl -sv localhost:5000/health 2>&1 | grep '^>'"), ('cmd', 'r5', "curl -sv localhost:5000/health 2>&1 | grep '^<'"), ('cmd', 'r8', 'curl -s localhost:5000/health')],
 'statusdemo': [('cmd', 't1', 'curl -si localhost:5000/health | head -1'), ('cmd', 't3', 'curl -si localhost:5000/nope | head -1'), ('cmd', 't5', 'curl -si localhost:5000/crash | head -1')],
 'tracedemo': [('cmd', 'x1', 'cat timing.txt'), ('cmd', 'x3', 'curl -so /dev/null -w @timing.txt localhost:5000/health'), ('cmd', 'x5', 'curl -so /dev/null -w @timing.txt localhost:5000/slow')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
