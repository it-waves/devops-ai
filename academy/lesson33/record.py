"""Record Lesson 33 live terminal demos in a clean standard-layout root. usage: record.py STAGE|all"""
import sys, os; sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson33')
from term import *
import video as V
LD = '/home/claude/academy/lesson33'
PFX = ['unshare', '-m', 'sh', LD + '/enter.sh']
os.environ['LPATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
def stage(scene, steps):
    open('/tmp/lstage', 'w').write(scene)
    subprocess.run('pkill -u student; true', shell=True); time.sleep(0.5)
    p = xterm_start(PFX); focus()
    key('ctrl+l'); time.sleep(0.4)
    r = Run(LD, V, scene, delay=80)
    for st in steps: r.cmd(st[1], st[2])
    r.end(); p.terminate(); time.sleep(0.5)
    subprocess.run('pkill -u student; true', shell=True)
STAGES = {
 'see': [('cmd', 's1', 'df -hT /home'), ('cmd', 's4', 'du -sh /usr/share'), ('cmd', 's6', 'du -sh /usr/* 2>/dev/null | sort -h | tail -n 3')],
 'make': [('cmd', 'm1', 'truncate -s 100M disk.img'), ('cmd', 'm2', 'ls -lh disk.img'), ('cmd', 'm4', 'mkfs.ext4 -q disk.img'), ('cmd', 'm6', 'sudo blkid -s TYPE -s UUID disk.img')],
 'mount': [('cmd', 't1', 'mkdir mnt'), ('cmd', 't2', 'sudo mount disk.img mnt'), ('cmd', 't3', 'df -h mnt'), ('cmd', 't5', 'lsblk -o NAME,SIZE,TYPE,MOUNTPOINTS | grep loop')],
 'full': [('cmd', 'u1', 'fallocate -l 60M mnt/big.bin'), ('cmd', 'u2', 'df -h mnt'), ('cmd', 'u4', 'fallocate -l 40M mnt/more.bin'), ('cmd', 'u6', 'rm mnt/big.bin mnt/more.bin'), ('cmd', 'u7', 'df -h mnt')],
 'grow': [('cmd', 'g1', 'df -h mnt'), ('cmd', 'g2', 'sudo umount mnt'), ('cmd', 'g3', 'truncate -s 200M disk.img'), ('cmd', 'g4', 'sudo e2fsck -fy disk.img 2>&1 | tail -n 1'), ('cmd', 'g5', 'sudo resize2fs disk.img 2>&1 | grep now'), ('cmd', 'g6', 'sudo mount disk.img mnt'), ('cmd', 'g7', 'df -h mnt')],
}
if __name__ == '__main__':
    a = sys.argv[1:] or ['all']
    for s in (STAGES if a == ['all'] else a): print('==', s, flush=True); stage(s, STAGES[s])
