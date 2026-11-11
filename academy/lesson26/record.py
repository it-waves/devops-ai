"""Record Lesson 26 live terminal demos in a clean standard-layout root. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson26')
from term import *
import video as V
LD = '/home/claude/academy/lesson26'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
def fixtures():
    h = '/home/student'
    for d in ('projects/cloudcart/app', 'projects/cloudcart/config'): os.makedirs(f'{h}/{d}', exist_ok=True)
    open(h + '/notes.txt', 'w').write('shopping list\n'); open(h + '/.profile', 'w').write('# ~/.profile\n')
    open(h + '/projects/cloudcart/app/cart.py', 'w').write('print("cart")\n'); open(h + '/projects/cloudcart/config/app.conf', 'w').write('port=8080\n')
    subprocess.run(['chown', '-R', 'student:student', h])
def stage(scene, steps):
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); fixtures()
    focus(); r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        elif st[0] == 'fn': st[1](r)
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
def tab(r):
    r.at('m7', r.dur['m7'] - 4.5); key('ctrl+l'); time.sleep(0.2); typ('cd pro', 80); time.sleep(0.5); key('Tab'); time.sleep(0.9); typ('cl', 80); time.sleep(0.5); key('Tab'); time.sleep(1.0); key('Return')
def man_ls(r):
    r.at('d5', max(0.3, r.dur['d5'] - 1.4)); key('ctrl+l'); typ('man ls', 80); key('Return')
    r.at('d6', 1.5); key('space'); r.at('d6', 4.0); typ('/recursive', 80); key('Return'); r.at('d7', max(0.5, r.dur['d7'] - 1.5)); key('q')
def man_pw(r):
    r.at('d9', max(0.3, r.dur['d9'] - 2.2)); key('ctrl+l'); typ('man 5 passwd', 80); key('Return')
    r.at('d10', max(0.5, r.dur['d10'] - 1.5)); key('q')
STAGES = {
 'where': [('cmd', 'w1', 'pwd'), ('cmd', 'w3', 'ls'), ('cmd', 'w4', 'ls -a'), ('cmd', 'w6', 'ls -l')],
 'paths': [('cmd', 'm1', 'cd projects/cloudcart/app'), ('cmd', 'm2', 'pwd'), ('cmd', 'm3', 'cd ../config'), ('cmd', 'm4', 'cd /var/log'), ('cmd', 'm5', 'cd -'), ('cmd', 'm6', 'cd'), ('fn', tab)],
 'tour': [('cmd', 't1', 'ls /'), ('cmd', 't3', 'ls -ld /bin /sbin /lib'), ('cmd', 't5', 'head -3 /etc/os-release'), ('cmd', 't7', 'ls /etc/apt'), ('cmd', 't9', 'ls /var/log'), ('cmd', 't11', 'head -2 /proc/meminfo')],
 'docs': [('cmd', 'd1', 'type cd'), ('cmd', 'd2', 'type cp'), ('cmd', 'd3', 'ls --help | head -8'), ('fn', man_ls), ('cmd', 'd8', 'whatis passwd'), ('fn', man_pw), ('cmd', 'd11', "apropos -s1 'copy files'")],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
