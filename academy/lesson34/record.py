"""Record Lesson 34 live terminal demos in a private-network chroot. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson34')
from term import *
import video as V
LD = '/home/claude/academy/lesson34'
PFX = ['unshare', '-mnu', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; pkill sshd; true', shell=True); time.sleep(0.5)
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
    subprocess.run('pkill -u student; pkill sshd; true', shell=True)
STAGES = {
 'net': [('cmd', 'n1', 'ip -br addr'), ('cmd', 'n3', 'ip route'), ('cmd', 'n5', 'ping -c 2 10.0.2.2'), ('cmd', 'n7', 'sudo ss -tlnp')],
 'ssh': [('cmd', 'k1', 'ssh-keygen -q -t ed25519 -N "" -f ~/.ssh/id_ed25519'), ('cmd', 'k2', 'ls ~/.ssh'), ('cmd', 'k4', 'cat ~/.ssh/*.pub >> ~/.ssh/authorized_keys'), ('cmd', 'k5', 'chmod 600 ~/.ssh/authorized_keys'), ('cmd', 'k6', 'ssh localhost hostname'), ('type', 'k7', 'yes')],
 'harden': [('cmd', 'r1', 'grep -h ^P /etc/ssh/sshd_config.d/*'), ('cmd', 'r3', 'sudo sshd -T | grep -E "^(password|permitroot)"'), ('cmd', 'r5', 'ssh -o PubkeyAuthentication=no localhost'), ('cmd', 'r7', 'sudo sshd -t && echo config ok')],
 'fw': [('cmd', 'w1', 'sudo ufw status'), ('cmd', 'w3', 'sudo ufw allow 22/tcp'), ('cmd', 'w4', 'sudo ufw allow 80/tcp'), ('cmd', 'w5', 'sudo ufw enable'), ('cmd', 'w7', 'sudo ufw status numbered'), ('cmd', 'w9', 'sudo ufw delete allow 80/tcp')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
