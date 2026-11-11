"""Record Lesson 38 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson38')
from term import *
import video as V
LD = '/home/claude/academy/lesson38'
PFX = ['unshare', '-mn', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus(); time.sleep(1.5)
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        elif st[0] == 'type':   # typed into a prompt, no screen clear
            r.clear = False; r.cmd(st[1], st[2]); r.clear = True
        elif st[0] == 'answer':  # answer a prompt shortly after the command
            time.sleep(1.8); typ(st[2], 80); key('Return')
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; umount /tmp/lroot/home/student/mnt 2>/dev/null; true', shell=True)
STAGES = {
 'vars': [('cmd', 'a1', 'city=Paris'), ('cmd', 'a2', 'echo "I live in $city"'), ('cmd', 'a3', 'echo "$cityland"'), ('cmd', 'a4', 'echo "${city}land"'), ('cmd', 'a5', 'echo "${name:-stranger}"'), ('cmd', 'a6', 'city = Paris')],
 'args': [('cmd', 'g1', 'cat greet.sh'), ('cmd', 'g2', './greet.sh Sam'), ('cmd', 'g3', './greet.sh Sam Lee Kim'), ('cmd', 'g4', './greet.sh "Sam Lee" Kim'), ('cmd', 'g5', './greet.sh')],
 'input': [('cmd', 'i1', 'cat ask.sh'), ('cmd', 'i2', './ask.sh'), ('answer', 'i2', 'Maya'), ('cmd', 'i3', 'echo Lee | ./ask.sh')],
 'subst': [('cmd', 's1', 'today=$(date +%F)'), ('cmd', 's2', 'echo "backup-$today.tar"'), ('cmd', 's3', 'ls | wc -l'), ('cmd', 's4', 'count=$(ls | wc -l)'), ('cmd', 's5', 'echo "There are $count files"')],
 'build': [('cmd', 't1', 'cat backup.sh'), ('cmd', 't2', './backup.sh'), ('cmd', 't3', './backup.sh photos')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
