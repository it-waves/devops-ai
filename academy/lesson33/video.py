import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 33  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 33', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
def chip(s, col, size=40, padx=22, pady=10):
    return badge(s, ImageFont.truetype(MONO, size), INK, col, padx=padx, pady=pady, r=18)
def _lab(title, sub, first, badge_, steps):
    def f(C, D, dur):
        E = head(title, sub, C[first]); E.append(real(C[first] + 0.2, badge_, 1260, 286))
        E.append(Pop(card(1100, 640, ACC, '', [], 4), 100, 330, C[first]))
        n = len(steps); gap = min(120, (1035 - 345) // n); fs_t, fs_s = (30, 25) if n <= 6 else (27, 23)
        for i, (cid, t, sb, col) in enumerate(steps): E.append(Pop(card(560, gap - 12, col, t, [(sb, TXT)], fs_t, fs_s), 1260, 345 + i * gap, C[cid] + 0.2))
        return E
    return f
def grid6(E, C, it, y0=330):
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, y0 + (i // 3) * 245, C[cid]))

RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
SCENES = [
 ('hook', [
  c('h1', "A server is only useful if it has room to work. When a disk fills up, things stop."),
  c('h2', "A disk holds a filesystem. A filesystem is mounted on a folder, called the mount point. That is how a disk becomes part of the folder tree you already know."),
  c('h3', "Today you check free space, format and mount a practice disk, fill it up on purpose, and grow it."),
 ]),
 ('see', [
  c('s1', "First, how full is this machine? Type: df -hT /home. D F means disk free. Dash h is human readable. Dash capital T adds the filesystem type.", "First, how full is this machine? Type: D F, dash h, capital T, slash home. D F means disk free. Dash h is human readable. Dash capital T adds the filesystem type."),
  c('s2', "Size is the whole filesystem. Used and available are what is taken and what is left. The last column is the mount point."),
  c('s3', "Watch the use percent. Above ninety, plan ahead. At one hundred, writes fail."),
  c('s4', "Now, what is using the space? Type: du -sh /usr/share. D U means disk usage. Dash s gives one total for the folder.", "Now, what is using the space? Type: D U, dash s h, slash U S R, slash share. D U means disk usage. Dash s gives one total for the folder."),
  c('s5', "That is the whole folder, in human units. It can take a few seconds, because du reads every file."),
  c('s6', "To find the biggest folders, sort them. Type: du -sh /usr/* | sort -h | tail -n 3.", "To find the biggest folders, sort them. Type: D U, dash s h, slash U S R, slash star, pipe, sort, dash h, pipe, tail, dash n, three. The part with two greater than hides error messages. This may take a moment."),
  c('s7', "The biggest folders come last. When space runs out, start with them."),
 ]),
 ('make', [
  c('m1', "Never practise on a real disk. So we make a pretend one, an ordinary file. Type: truncate -s 100M disk.img.", "Never practise on a real disk. So we make a pretend one, an ordinary file. Type: truncate, dash s, one hundred M, disk dot img."),
  c('m2', "Check it. Type: ls -lh disk.img.", "Check it. Type: L S, dash l h, disk dot img."),
  c('m3', "One hundred megabytes of empty space. To Linux, a disk is just somewhere to store blocks, and a file can play that part."),
  c('m4', "Now give it a filesystem. Type: mkfs.ext4 -q disk.img. Mkfs means make filesystem, and dash q keeps it quiet.", "Now give it a filesystem. Type: M K F S, dot E X T four, dash q, disk dot img. M K F S means make filesystem, and dash q keeps it quiet."),
  c('m5', "No news is good news. Formatting erases what was there, so on a real disk, check the device name twice."),
  c('m6', "Read the label. Type: sudo blkid -s TYPE -s UUID disk.img.", "Read the label. Type: sue do, block I D, dash s, TYPE, dash s, U U I D, disk dot img."),
  c('m7', "The type is E X T four, and the U U I D is its unique I D. Real systems mount by U U I D, because device names can change."),
 ]),
 ('mount', [
  c('t1', "A filesystem is not usable until it is mounted. First, make a folder to mount it on. Type: mkdir mnt.", "A filesystem is not usable until it is mounted. First, make a folder to mount it on. Type: make dir, M N T."),
  c('t2', "Now mount it. Type: sudo mount disk.img mnt. Because it is a file, Linux attaches it to a loop device for you.", "Now mount it. Type: sue do, mount, disk dot img, M N T. Because it is a file, Linux attaches it to a loop device for you."),
  c('t3', "Check it. Type: df -h mnt.", "Check it. Type: D F, dash h, M N T."),
  c('t4', "A new filesystem, mounted on mnt. About ninety megabytes, because the filesystem keeps some for itself. Used is almost nothing."),
  c('t5', "Now list the block devices. Type: lsblk -o NAME,SIZE,TYPE,MOUNTPOINTS | grep loop.", "Now list the block devices. Type: L S B L K, dash o, name, size, type, mount points, pipe, grep, loop."),
  c('t6', "Loop zero is the device, one hundred megabytes, mounted on your folder. A real disk looks the same, with a name like S D A or N V M E."),
 ]),
 ('full', [
  c('u1', "Now see what a full disk does. Reserve a sixty megabyte file. Type: fallocate -l 60M mnt/big.bin.", "Now see what a full disk does. Reserve a sixty megabyte file. Type: F allocate, dash l, sixty M, M N T, slash big dot bin."),
  c('u2', "Check the space. Type: df -h mnt.", "Check the space. Type: D F, dash h, M N T."),
  c('u3', "Seventy-three percent used, and twenty-three megabytes left."),
  c('u4', "Now ask for forty more, which will not fit. Type: fallocate -l 40M mnt/more.bin.", "Now ask for forty more, which will not fit. Type: F allocate, dash l, forty M, M N T, slash more dot bin."),
  c('u5', "No space left on device. That is what every program sees on a full disk: failed writes, failed logs, crashed databases."),
  c('u6', "Free the space. Type: rm mnt/big.bin mnt/more.bin.", "Free the space. Type: R M, M N T, slash big dot bin, M N T, slash more dot bin."),
  c('u7', "And check again. Type: df -h mnt.", "And check again. Type: D F, dash h, M N T."),
  c('u8', "The space is back. Deleting is the fix, but first find what is big, with D U, as you saw."),
 ]),
 ('grow', [
  c('g1', "Disks get too small. Growing has two parts: make the disk bigger, then make the filesystem bigger. First, the size now. Type: df -h mnt.", "Disks get too small. Growing has two parts: make the disk bigger, then make the filesystem bigger. First, the size now. Type: D F, dash h, M N T."),
  c('g2', "About ninety megabytes. Unmount it, so the filesystem is quiet. Type: sudo umount mnt.", "About ninety megabytes. Unmount it, so the filesystem is quiet. Type: sue do, U mount, M N T."),
  c('g3', "Make the disk bigger. Type: truncate -s 200M disk.img. On a cloud server, this is where you grow the volume in the console.", "Make the disk bigger. Type: truncate, dash s, two hundred M, disk dot img. On a cloud server, this is where you grow the volume in the console."),
  c('g4', "Check the filesystem before you resize it. Type: sudo e2fsck -fy disk.img 2>&1 | tail -n 1. The 2>&1 part joins the messages, and tail keeps the last line.", "Check the filesystem before you resize it. Type: sue do, E two F S C K, dash f y, disk dot img, then two greater than and one, pipe, tail, dash n, one. The two greater than and one part joins the messages, and tail keeps the last line."),
  c('g5', "Clean means no problems found. Now grow the filesystem to fill the disk. Type: sudo resize2fs disk.img 2>&1 | grep now.", "Clean means no problems found. Now grow the filesystem to fill the disk. Type: sue do, resize two F S, disk dot img, then two greater than and one, pipe, grep, now."),
  c('g6', "It now fills the bigger disk. Mount it again. Type: sudo mount disk.img mnt.", "It now fills the bigger disk. Mount it again. Type: sue do, mount, disk dot img, M N T."),
  c('g7', "And check. Type: df -h mnt.", "And check. Type: D F, dash h, M N T."),
  c('g8', "About one hundred eighty-four megabytes. Same disk, more room, nothing lost. On a real server, you grow the partition or volume first, then resize the filesystem."),
 ]),
 ('fstab', [
  c('k1', "A mount you make by hand is gone after a reboot. To keep it, add one line to the file slash E T C slash F S tab.", "A mount you make by hand is gone after a reboot. To keep it, add one line to the file slash E T C slash F S tab."),
  c('k2', "Each line has six fields: what to mount, where, the filesystem type, options, and two numbers for backup and check order."),
  c('k3', "Use the U U I D from blkid, not the device name, because device names can change."),
  c('k4', "A wrong line can stop a server booting. So after editing, run sudo mount dash a, and fix any error before you reboot. The option nofail lets the boot continue if the disk is missing.", "A wrong line can stop a server booting. So after editing, run sue do, mount, dash a, and fix any error before you reboot. The option no fail lets the boot continue if the disk is missing."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: delete a file and the space always returns. No. If a program still holds it open, the space stays used until the program closes it."),
  c('my3', "Myth two: formatting is safe to try. No. It erases the disk, so check the device name first."),
  c('my4', "Myth three: a bigger disk means a bigger filesystem. No. You must resize the filesystem too."),
  c('my5', "Myth four: if it mounted, it will mount at boot. No. Only the F S tab file does that."),
  c('my6', "Check, mount, grow, then make it permanent."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Check free space with D F, and say what the use percent means."),
  c('b3', "Find the biggest folders with D U, and sort them."), c('b4', "Make a filesystem on a practice disk, and read its U U I D."),
  c('b5', "Mount it, and prove it with D F and L S B L K."), c('b6', "Fill it, read the error, and free the space."),
  c('b7', "Grow it: bigger disk, check, resize, mount. And say what goes in F S tab."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. Everything here uses a practice file, never a real disk."),
  c('z2', "One: run D F dash h T and D U, and name your fullest mount."),
  c('z3', "Two: make a one hundred megabyte image with truncate, and format it with M K F S dot E X T four."),
  c('z4', "Three: read its U U I D with block I D, then mount it and prove it with D F."),
  c('z5', "Four: fill it with F allocate, read the error, and free the space."),
  c('z6', "Five: unmount it, grow it to two hundred megabytes, check, resize, and mount it again."),
  c('z7', "Six: write down the F S tab line you would add, using the U U I D."),
  c('z8', "Last, clean up. Unmount, then delete the image. Then mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which command shows free space on a filesystem?"), c('f13', "Which command finds what is using the space?"),
  c('f14', "Which two steps grow a filesystem?"), c('f15', "Which file makes a mount permanent?"),
  c('f16', "Objective covered: MC04-O08.", "Objective covered: M C zero four, objective eight, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: Linux networking and security."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 's3': 0.4, 's5': 5.0, 's6': 3.0, 's7': 0.5, 'm3': 0.4, 'm5': 0.4, 'm7': 0.5, 't4': 0.5, 't6': 0.5, 'u3': 0.4, 'u5': 0.5, 'u8': 0.5, 'g2': 0.3, 'g5': 0.4, 'g8': 0.5, 'k4': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'see': 'Free space and who uses it', 'make': 'Make a practice disk', 'mount': 'Mount it', 'full': 'Fill it, then free it', 'grow': 'Grow a disk', 'fstab': 'Mount at boot', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))


def s_hook(C, D, dur):
    E = [El(T('A disk is only useful with room to spare.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Disk', 'where the data lives', ACC), ('Filesystem', 'the structure that holds files', VIO), ('Mount point', 'the folder it appears in', WARN)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 2.8))
    E.append(takeaway('Check. Mount. Grow.', 850, C['h3'], GOOD, 1600)); return E
s_see = _lab('Free space, and who uses it', 'Check before it fills.', 's1', RB, [('s1', 'df -hT', 'Free space, per filesystem', ACC), ('s4', 'du -sh', 'Size of one folder', VIO), ('s6', 'sort -h | tail', 'Biggest folders last', WARN)])
s_make = _lab('Make a practice disk', 'A file plays the disk. Nothing real is at risk.', 'm1', RB, [('m1', 'truncate', 'A 100 MB pretend disk', ACC), ('m4', 'mkfs.ext4', 'Give it a filesystem', VIO), ('m6', 'blkid', 'Type and UUID', GOOD)])
s_mount = _lab('Mount it', 'A filesystem is usable only once mounted.', 't1', RB, [('t1', 'mkdir', 'A folder to mount on', ACC), ('t2', 'mount', 'Attach the filesystem', VIO), ('t3', 'df -h', 'Prove it is there', GOOD), ('t5', 'lsblk', 'The block devices', WARN)])
s_full = _lab('Fill it, then free it', 'What a full disk looks like.', 'u1', RB, [('u1', 'fallocate 60M', 'Reserve space', ACC), ('u2', 'df -h', 'About 73 percent used', WARN), ('u4', 'fallocate 40M', 'Does not fit', BAD), ('u6', 'rm, then df', 'The space returns', GOOD)])
s_grow = _lab('Grow a disk', 'Bigger disk first, then bigger filesystem.', 'g1', RB, [('g1', 'df -h', 'Before: about 90 MB', ACC), ('g3', 'truncate', 'Make the disk bigger', VIO), ('g4', 'e2fsck', 'Check first', WARN), ('g5', 'resize2fs', 'Grow the filesystem', PINK), ('g6', 'mount, df', 'After: about 184 MB', GOOD)])
def s_fstab(C, D, dur):
    E = head('Mount at boot', 'One line in /etc/fstab.', C['k1']); E.append(ill(C['k1'] + 0.2, 1260, 286))
    mono_panel(E, 100, 330, 1700, [('UUID=3a369b8a-cf9c-455d-9036-d1e37a94634b  /data  ext4  defaults,nofail  0  2', TXT)], C['k1'] + 0.4, fs=30, lh=60)
    it = [('1  What', 'UUID of the filesystem', ACC), ('2  Where', 'the mount point', VIO), ('3  Type', 'ext4, xfs, ...', GOOD), ('4  Options', 'defaults, nofail', WARN), ('5  Dump', 'backup flag, usually 0', PINK), ('6  Pass', 'check order at boot', ACC)]
    for i, (n, s, col) in enumerate(it): E.append(Pop(card(540, 160, col, n, [(s, TXT)], 40, 30, True), 100 + (i % 3) * 590, 500 + (i // 3) * 185, C['k2'] + i * 0.35))
    E.append(takeaway('Test with sudo mount -a before you reboot.', 880, C['k4'], GOOD, 1700)); return E
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: delete frees space', 'Not while a program holds it open.', 'my2'), ('Myth: formatting is safe', 'It erases the disk.', 'my3'), ('Myth: bigger disk, bigger fs', 'Resize the filesystem too.', 'my4'), ('Myth: mounted means permanent', 'Only /etc/fstab does that.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Check. Mount. Grow. Persist.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Free space with df', 'b2'), ('Biggest folders with du', 'b3'), ('Format and read the UUID', 'b4'), ('Mount and prove it', 'b5'), ('Fill it, then free it', 'b6'), ('Grow it, and fstab', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'A practice file only. Never a real disk.', C['z1'])
    it = [('1  Look', 'df -hT and du', PINK, 'z2'), ('2  Format', 'truncate, mkfs.ext4', ACC, 'z3'), ('3  Mount', 'blkid, mount, df', WARN, 'z4'), ('4  Fill', 'fallocate, read the error', BAD, 'z5'), ('5  Grow', 'umount, e2fsck, resize2fs', VIO, 'z6'), ('6  Persist', 'write the fstab line', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command shows free space?', 'f12'), ('Which command finds what is big?', 'f13'), ('Which two steps grow a filesystem?', 'f14'), ('Which file makes a mount permanent?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O08', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: networking and security', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, see=s_see, make=s_make, mount=s_mount, full=s_full, grow=s_grow, fstab=s_fstab, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(see=('eye', GOOD), make=('gear', ACC), mount=('eye', GOOD), full=('eye', GOOD), grow=('gear', ACC), fstab=('board', WARN), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'see': [('s2', 2, 1, 330, 590, ''), ('s3', 2, 1, 590, 665, ''), ('s5', 1, 1, 4, 300, ''), ('s7', 3, 1, 4, 300, '')],
 'make': [('m3', 1, 1, 430, 510, ''), ('m7', 1, 1, 150, 985, '')],
 'mount': [('t4', 2, 1, 4, 860, ''), ('t6', 1, 1, 4, 530, '')],
 'full': [('u3', 2, 1, 4, 860, ''), ('u5', 1, 1, 4, 790, ''), ('u8', 2, 1, 4, 860, '')],
 'grow': [('g2', 2, 1, 250, 322, ''), ('g5', 1, 1, 4, 985, ''), ('g6', 1, 1, 4, 860, ''), ('g8', 2, 1, 240, 318, '')],
}
