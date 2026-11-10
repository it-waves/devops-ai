"""Record Lesson 14 live terminal demos. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson14')
from term import *
import video as V
LD = '/home/claude/academy/lesson14'
def stage(scene, steps):
    p = xterm_start(); focus(); r = Run(LD, V, scene, delay=80)
    for st in steps:
        if st[0] == 'cmd': r.cmd(st[1], st[2])
        elif st[0] == 'keys': r.keys(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
STAGES = {
 'xxd': [('cmd', 'x3', 'echo -n A | xxd -b'), ('cmd', 'x6', 'echo -n A | xxd'), ('cmd', 'x9', 'echo -n Hi | xxd')],
 'kinds': [('cmd', 'k2', 'echo "hello" > hello.txt'), ('cmd', 'k3', 'file hello.txt'), ('cmd', 'k5', 'file -b /bin/ls | cut -d, -f1-2'), ('cmd', 'k7', 'head -c 16 /bin/ls | xxd')],
 'encdemo': [('cmd', 'n2', "printf 'cafe' | xxd"), ('cmd', 'n4', "printf 'café' | xxd"), ('cmd', 'n6', "printf 'café' | wc -c"), ('cmd', 'n7', "printf 'café' | wc -m"), ('cmd', 'n9', "echo café | iconv -f latin1 -t utf8")],
 'eoldemo': [('cmd', 'o2', r"printf 'one\r\ntwo\r\n' > win.txt"), ('cmd', 'o3', 'file win.txt'), ('cmd', 'o5', 'cat -A win.txt'), ('cmd', 'o8', r"printf '#!/bin/bash\r\necho hi\r\n' > run.sh"), ('cmd', 'o9', 'chmod +x run.sh'),
             ('cmd', 'o10', './run.sh'), ('cmd', 'o13', r"sed -i 's/\r$//' run.sh"), ('cmd', 'o14', './run.sh')],
 'pathdemo': [('cmd', 'a1', 'mkdir -p project/docs'), ('cmd', 'a2', 'cd project/docs'), ('cmd', 'a3', 'pwd'), ('cmd', 'a4', 'cd ..'), ('cmd', 'a5', 'pwd'), ('cmd', 'a6', 'cd ~'), ('cmd', 'a7', 'ls project'), ('cmd', 'a8', 'ls /home/student/project')],
 'envdemo': [('cmd', 'm2', 'echo $HOME'), ('cmd', 'm3', 'GREETING=hello'), ('cmd', 'm4', 'echo $GREETING'), ('cmd', 'm5', '''bash -c 'echo "child sees: $GREETING"' '''.strip()), ('cmd', 'm7', 'export GREETING'), ('keys', 'm8', ['Up', 'Up', 'Return'])],
 'pathrun': [('cmd', 'u1', 'echo $PATH'), ('cmd', 'u3', 'which ls'), ('cmd', 'u4', 'mkdir -p ~/bin'), ('cmd', 'u5', r'''printf '#!/bin/bash\necho "Hello!"\n' > ~/bin/hello'''), ('cmd', 'u6', 'chmod +x ~/bin/hello'),
             ('cmd', 'u7', 'hello'), ('cmd', 'u9', 'export PATH="$HOME/bin:$PATH"'), ('cmd', 'u10', 'hello'), ('cmd', 'u11', 'which hello')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
