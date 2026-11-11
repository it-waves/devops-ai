import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 29  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = {'TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O04': 'M C zero four, objective four', 'whoami': 'who am I', 'chmod': 'change mod', 'chown': 'change own', 'sudo': 'sue doo', 'useradd': 'user add', 'groupadd': 'group add', 'usermod': 'user mod', 'ssh': 'S S H', 'SSH': 'S S H', 'keygen': 'key gen', 'ed25519': 'E D twenty five five one nine', 'rwx': 'R W X', 'passwd': 'password', 'shadow': 'shadow', 'authorized_keys': 'authorized keys', 'groups': 'groups', 'id': 'I D', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 29', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
SCENES = [
 ('hook', [
  c('h1', "Every file on a server has an owner."),
  c('h2', "Who you are decides what you can read, change, and run."),
  c('h3', "Today you learn users, permissions, sudo, and S S H keys."),
 ]),
 ('ids', [
  c('i1', "First question on any server: who am I? Type: whoami.", "First question on any server: who am I? Type: who am I."),
  c('i2', "Now the detail. Type: id. Your user number, your group number, and every group you belong to.", "Now the detail. Type: I D. Your user number, your group number, and every group you belong to."),
  c('i3', "Every user is one line in slash etc slash password. Type: grep student /etc/passwd.", "Every user is one line in slash E T C slash passwd. Type: grep, student, slash, E T C, slash, passwd."),
  c('i4', "Fields split by colons: the name, a placeholder, the user number, the group number, a comment, the home folder, and the login shell."),
 ]),
 ('perms', [
  c('p1', "Permissions live on every file. Type: ls -l.", "Permissions live on every file. Type: L S, dash l."),
  c('p2', "Read the first column. One character for the type, then three groups of three: owner, group, and everyone else."),
  c('p3', "Each group is r for read, w for write, x for execute. A dash means no. So rw dash r dash dash r dash dash means the owner edits, everyone else only reads."),
  c('p4', "Lock a secret down. Type: chmod 600 secret.txt.", "Lock a secret down. Type: change mod, six hundred, secret dot text."),
  c('p5', "Check it. Type: ls -l secret.txt.", "Check it. Type: L S, dash l, secret dot text."),
  c('p6', "Now the owner can read and write. Nobody else can even look. Six is four for read, plus two for write."),
  c('p7', "Try running the script. Type: ./run.sh.", "Try running the script. Type: dot, slash, run dot S H."),
  c('p8', "Permission denied. The file is not executable yet. Fix it with: chmod +x run.sh.", "Permission denied. The file is not executable yet. Fix it with: change mod, plus x, run dot S H."),
  c('p9', "And run it again.", "And run it again."),
 ]),
 ('sudo', [
  c('s1', "Some files are not yours. Type: cat /etc/shadow.", "Some files are not yours. Type: cat, slash, E T C, slash, shadow."),
  c('s2', "Permission denied. That file holds password hashes, and only root may read it."),
  c('s3', "Root is the all powerful administrator. You borrow its power with sudo. Type: sudo whoami.", "Root is the all powerful administrator. You borrow its power with sue doo. Type: sue doo, who am I."),
  c('s4', "The answer is root, for that one command only. Make a new user. Type: sudo useradd -m maria.", "The answer is root, for that one command only. Make a new user. Type: sue doo, user add, dash m, maria."),
  c('s5', "Create a group. Type: sudo groupadd devs.", "Create a group. Type: sue doo, group add, devs."),
  c('s6', "Add Maria to it. Type: sudo usermod -aG devs maria. A G means append to a group.", "Add Maria to it. Type: sue doo, user mod, dash A G, devs, maria. A G means append to a group."),
  c('s7', "Check. Type: id maria.", "Check. Type: I D, maria."),
  c('s8', "Now give her a file. Type: sudo chown maria:devs notes.txt. Owner colon group.", "Now give her a file. Type: sue doo, change own, maria, colon, devs, notes dot text. Owner colon group."),
  c('s9', "Confirm with: ls -l notes.txt. New owner, new group.", "Confirm with: L S, dash l, notes dot text. New owner, new group."),
 ]),
 ('ssh', [
  c('k1', "Passwords can be guessed. Keys are far safer. Make a pair. Type: ssh-keygen -t ed25519 -f demo_key -N, then two quote marks.",
    "Passwords can be guessed. Keys are far safer. Make a pair. Type: S S H, key gen, dash t, E D twenty five five one nine, dash f, demo underscore key, dash capital N, then two quote marks."),
  c('k2', "Two files appeared. Type: ls -l demo_key demo_key.pub.", "Two files appeared. Type: L S, dash l, demo underscore key, demo underscore key dot pub."),
  c('k3', "The private key is rw only for you. It never leaves your computer. The dot pub file is the public key, safe to share."),
  c('k4', "Read the public key. Type: cat demo_key.pub. One line. This is a throwaway demo key.", "Read the public key. Type: cat, demo underscore key dot pub. One line. This is a throwaway demo key."),
  c('k5', "A server trusts you when your public key is in its authorized keys file. Type: mkdir -p ~/.ssh.", "A server trusts you when your public key is in its authorized keys file. Type: make dir, dash p, tilde, slash, dot S S H."),
  c('k6', "Add the key. Type: cat demo_key.pub, two arrows, then the authorized keys file.", "Add the key. Type: cat, demo underscore key dot pub, two arrows, tilde, slash, dot S S H, slash, authorized underscore keys."),
  c('k7', "S S H is strict. Lock the folder with chmod 700, and the file with chmod 600. Type: chmod 700 ~/.ssh.", "S S H is strict. Lock the folder with change mod seven hundred, and the file with change mod six hundred. Type: change mod, seven hundred, tilde, slash, dot S S H."),
  c('k8', "Now the file. Type: chmod 600 ~/.ssh/authorized_keys.", "Now the file. Type: change mod, six hundred, tilde, slash, dot S S H, slash, authorized underscore keys."),
  c('k9', "Check it. Type: ls -l ~/.ssh.", "Check it. Type: L S, dash l, tilde, slash, dot S S H."),
  c('k10', "Too open, and S S H refuses the key. That is the number one cause of key login failures."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: chmod 777 fixes everything. It gives everyone full access. It hides the problem, and creates a bigger one."),
  c('my3', "Myth two: use sudo for every command. No. Use it only when you must. Least power wins."),
  c('my4', "Myth three: share your private key to let a friend in. Never. Share the public key only."),
  c('my5', "Myth four: root and sudo are the same. Root is the account. Sudo borrows its power for one command."),
  c('my6', "Least power. Public key only."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Say who you are with whoami and id."),
  c('b3', "Read an ls dash l permission string.", "Read an L S, dash l permission string."), c('b4', "Change permissions with chmod, in numbers and with plus x.", "Change permissions with change mod, in numbers and with plus x."),
  c('b5', "Create a user and group, and change an owner."), c('b6', "Make an S S H key pair, and say which half is private."),
  c('b7', "Set the right permissions on the S S H folder and file."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. Use a practice folder, and a practice user."),
  c('z2', "One: run who am I and I D, and write down your groups.", "One: run who am I, and I D, and write down your groups."),
  c('z3', "Two: make a file, and use ls dash l to read its permissions.", "Two: make a file, and use L S, dash l, to read its permissions."),
  c('z4', "Three: use chmod to make it private, then check it again.", "Three: use change mod to make it private, then check it again."),
  c('z5', "Four: write a tiny script, run it, see permission denied, then fix it with chmod plus x.", "Four: write a tiny script, run it, see permission denied, then fix it with change mod, plus x."),
  c('z6', "Five: with sudo, create a user and a group, add the user to the group, and give them a file."),
  c('z7', "Six: make a throwaway key pair, and set the S S H folder to seven hundred, and the key file to six hundred.", "Six: make a throwaway key pair, and set the S S H folder to seven hundred, and the key file to six hundred."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does chmod 600 give the owner?", "What does change mod six hundred give the owner?"), c('f13', "Which command borrows root power for one command?"),
  c('f14', "Which key file is safe to share?"), c('f15', "What should the S S H folder permission be?"),
  c('f16', "Objective covered: MC04-O04.", "Objective covered: M C zero four, objective four, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: processes and signals."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'i4': 0.5, 'p6': 0.5, 'p9': 0.8, 's2': 0.5, 's9': 0.5, 'k3': 0.3, 'k10': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'ids': 'Who am I', 'perms': 'Read and change permissions', 'sudo': 'sudo, users and owners', 'ssh': 'SSH keys', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def s_hook(C, D, dur):
    E = [El(T('Every file has an owner.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Users', 'who you are', ACC), ('Permissions', 'what you may do', VIO), ('Keys', 'how you prove it', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('Who. What. Proof.', 850, C['h3'], GOOD, 1600)); return E
s_ids = _lab('Who am I', 'Users, groups and the passwd file.', 'i1', RB, [('i1', 'whoami', 'Your user name', ACC), ('i2', 'id', 'Numbers and groups', VIO), ('i3', '/etc/passwd', 'One line per user', WARN)])
s_perms = _lab('Read and change permissions', 'r, w, x for owner, group, others.', 'p1', RB, [('p1', 'ls -l', 'See permissions', ACC), ('p3', 'rwx', 'Read, write, execute', VIO), ('p4', 'chmod 600', 'Owner read and write', WARN), ('p7', './run.sh', 'Denied: not executable', BAD), ('p8', 'chmod +x', 'Make it executable', GOOD)])
s_sudo = _lab('sudo, users and owners', 'Borrow root power, one command at a time.', 's1', RB, [('s1', '/etc/shadow', 'Denied: root only', BAD), ('s3', 'sudo', 'Borrow root', ACC), ('s4', 'useradd -m', 'New user', VIO), ('s5', 'groupadd', 'New group', WARN), ('s6', 'usermod -aG', 'Add to group', PINK), ('s8', 'chown', 'New owner', GOOD)])
s_ssh = _lab('SSH keys', 'A private half and a public half.', 'k1', RB, [('k1', 'ssh-keygen', 'Make the pair', ACC), ('k3', '.pub', 'Public: share', GOOD), ('k5', '~/.ssh', 'Server key folder', VIO), ('k6', '>>', 'Append the key', WARN), ('k7', 'chmod 700', 'Folder: owner only', PINK), ('k8', 'chmod 600', 'File: owner only', BAD)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: chmod 777 fixes it', 'It hides the problem.', 'my2'), ('Myth: sudo for everything', 'Least power wins.', 'my3'), ('Myth: share the private key', 'Public key only.', 'my4'), ('Myth: root equals sudo', 'Sudo borrows root power.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Least power. Public key only.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('whoami and id', 'b2'), ('Read ls -l permissions', 'b3'), ('chmod: numbers and +x', 'b4'), ('User, group, chown', 'b5'), ('Make an SSH key pair', 'b6'), ('SSH folder and file modes', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine. Practice folder only.', C['z1'])
    it = [('1  Who', 'whoami, id', PINK, 'z2'), ('2  Read', 'ls -l a file', ACC, 'z3'), ('3  Lock', 'chmod, check', WARN, 'z4'), ('4  Run', 'denied, then +x', VIO, 'z5'), ('5  Admin', 'user, group, chown', GOOD, 'z6'), ('6  Keys', 'pair, 700, 600', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does chmod 600 give the owner?', 'f12'), ('Which command borrows root power?', 'f13'), ('Which key file is safe to share?', 'f14'), ('What mode should ~/.ssh have?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: processes and signals', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ids=s_ids, perms=s_perms, sudo=s_sudo, ssh=s_ssh, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ids=('eye', GOOD), perms=('eye', GOOD), sudo=('question', WARN), ssh=('eye', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'ids': [('i4', 1, 1, 4, 520, '')],
 'perms': [('p2', 2, 3, 4, 150, ''), ('p6', 1, 1, 4, 150, '')],
}
