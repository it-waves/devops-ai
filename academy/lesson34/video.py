import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 34  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'ufw': 'U F W', 'sshd': 'S S H D', 'ed25519': 'E D two five five one nine', 'eth0': 'eth zero', 'MC04-O09': 'M C zero four, objective nine', 'loopback': 'loop back', 'ping': 'ping', 'ss': 'S S', 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 34', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "Every server lives on a network, and the network is its front door. Today you learn to read it, log in safely, and close the doors you do not need."),
  c('h2', "You will see your addresses and routes, check what is listening, log in with S S H keys instead of passwords, lock down the S S H server, and switch on a firewall."),
  c('h3', "It all runs on a practice network built on this computer, so nothing real is exposed."),
 ]),
 ('net', [
  c('n1', "First, your addresses. Type: ip -br addr. Dash br gives a short table.", "First, your addresses. Type: I P, dash b r, addr. Dash b r gives a short table."),
  c('n2', "Lo is the loopback, this machine talking to itself. Eth0 is the network card. Its address is 10.0.2.15, with a slash 24 mask.", "Lo is the loop back, this machine talking to itself. Eth zero is the network card. Its address is ten dot zero dot two dot fifteen, with a slash twenty-four mask."),
  c('n3', "Next, where does traffic go? Type: ip route.", "Next, where does traffic go? Type: I P, route."),
  c('n4', "The default route sends everything else to the gateway, 10.0.2.2. The second line says the local network is reached directly.", "The default route sends everything else to the gateway, ten dot zero dot two dot two. The second line says the local network is reached directly."),
  c('n5', "Can we reach the gateway? Type: ping -c 2 10.0.2.2. Dash c two sends two packets.", "Can we reach the gateway? Type: ping, dash c, two, ten dot zero dot two dot two. Dash c two sends two packets."),
  c('n6', "Two sent, two received, no loss. The time is in milliseconds."),
  c('n7', "What is listening for connections? Type: sudo ss -tlnp. T is T C P, L is listening, N is numbers, and P shows the process.", "What is listening for connections? Type: sue do, S S, dash t l n p. T is T C P, L is listening, N is numbers, and P shows the process."),
  c('n8', "The program sshd is listening on port 22, on the loopback address. Know what is listening, and you know your attack surface.", "The program S S H D is listening on port twenty-two, on the loop back address. Know what is listening, and you know your attack surface."),
 ]),
 ('ssh', [
  c('k1', "S S H keys replace passwords. Make a pair. Type: ssh-keygen -q -t ed25519 -N empty quotes -f ~/.ssh/id_ed25519. The empty passphrase is for this demo only. Use a passphrase on real keys.", "S S H keys replace passwords. Make a pair. Type: S S H keygen, dash q, dash t, E D two five five one nine, dash capital N, empty quotes, dash f, tilde slash dot S S H slash I D underscore E D two five five one nine. The empty passphrase is for this demo only. Use a passphrase on real keys."),
  c('k2', "Dash q keeps it quiet, so nothing prints. List the folder. Type: ls ~/.ssh.", "Dash q keeps it quiet, so nothing prints. List the folder. Type: L S, tilde, slash dot S S H."),
  c('k3', "Two files. The private key stays on your machine and is never shared. The dot pub file is the public key, safe to hand out."),
  c('k4', "The server decides who may log in with a file called authorized keys. Add your public key to it. Type: cat ~/.ssh/*.pub >> ~/.ssh/authorized_keys.", "The server decides who may log in with a file called authorized keys. Add your public key to it. Type: cat, tilde slash dot S S H slash star dot pub, then two greater than signs, then tilde slash dot S S H slash authorized underscore keys."),
  c('k5', "Lock the file down. Type: chmod 600 ~/.ssh/authorized_keys. S S H refuses keys that other users can read.", "Lock the file down. Type: C H mod, six hundred, tilde slash dot S S H slash authorized underscore keys. S S H refuses keys that other users can read."),
  c('k6', "Now log in. Type: ssh localhost hostname. That runs the hostname command on the server, which here is this same machine.", "Now log in. Type: S S H, local host, hostname. That runs the hostname command on the server, which here is this same machine."),
  c('k7', "The first time, S S H shows the server's fingerprint and asks whether you trust it. On a real server, compare it with a trusted copy. Then type yes."),
  c('k8', "No password was asked. The key proved who you are, and the server printed its name."),
 ]),
 ('harden', [
  c('r1', "The server's settings live in the S S H D config. Show the lab settings. Type: grep -h ^P /etc/ssh/sshd_config.d/*.", "The server's settings live in the S S H D config. Show the lab settings. Type: grep, dash h, caret P, slash E T C, slash S S H, slash S S H D underscore config dot D, slash star."),
  c('r2', "Password authentication is no, so guessing passwords gets an attacker nowhere. Permit root login is no, so nobody logs in as root directly. Pubkey authentication is yes."),
  c('r3', "What is the server really using? Type: sudo sshd -T | grep -E, and the pattern in quotes.", "What is the server really using? Type: sue do, S S H D, dash capital T, pipe, grep, dash capital E, and the pattern in quotes."),
  c('r4', "Dash capital T prints the effective settings, after every file is merged. Both say no."),
  c('r5', "Now test the lock. Try to log in without the key. Type: ssh -o PubkeyAuthentication=no localhost.", "Now test the lock. Try to log in without the key. Type: S S H, dash o, pubkey authentication equals no, local host."),
  c('r6', "Permission denied, public key. Passwords are off and no key was offered, so the door stays shut."),
  c('r7', "Before you reload a real server, test the config. Type: sudo sshd -t && echo config ok.", "Before you reload a real server, test the config. Type: sue do, S S H D, dash t, and, and, echo config ok."),
  c('r8', "No errors, so it says config ok. A typo here can lock you out, so always test, and keep a second session open."),
 ]),
 ('fw', [
  c('w1', "A firewall decides which connections may reach the machine. On Ubuntu, U F W keeps it simple. Type: sudo ufw status.", "A firewall decides which connections may reach the machine. On Ubuntu, U F W keeps it simple. Type: sue do, U F W, status."),
  c('w2', "Inactive. Nothing is filtered yet."),
  c('w3', "Allow S S H first, or you will lock yourself out. Type: sudo ufw allow 22/tcp.", "Allow S S H first, or you will lock yourself out. Type: sue do, U F W, allow, twenty-two slash T C P."),
  c('w4', "Rule added. Add web traffic too. Type: sudo ufw allow 80/tcp.", "Rule added. Add web traffic too. Type: sue do, U F W, allow, eighty slash T C P."),
  c('w5', "Now switch it on. Type: sudo ufw enable. On a machine with an S S H session open, it may ask you to confirm, because a wrong rule can cut you off. You allowed port 22, so you are safe.", "Now switch it on. Type: sue do, U F W, enable. On a machine with an S S H session open, it may ask you to confirm, because a wrong rule can cut you off. You allowed port twenty-two, so you are safe."),
  c('w6', "Active, and enabled at startup. By default it denies incoming connections and allows outgoing ones."),
  c('w7', "List the rules with numbers. Type: sudo ufw status numbered.", "List the rules with numbers. Type: sue do, U F W, status, numbered."),
  c('w8', "Two rules, ports 22 and 80, allowed in. Everything else coming in is denied.", "Two rules, ports twenty-two and eighty, allowed in. Everything else coming in is denied."),
  c('w9', "Remove a rule you no longer need. Type: sudo ufw delete allow 80/tcp.", "Remove a rule you no longer need. Type: sue do, U F W, delete, allow, eighty slash T C P."),
  c('w10', "Rule deleted. Open only what the machine needs."),
 ]),
 ('habits', [
  c('e1', "A few habits stop most attacks."),
  c('e2', "Use keys, not passwords, and turn password logins off."),
  c('e3', "No direct root login. Use sudo, so every action is tied to a person."),
  c('e4', "Open only the ports you need, and know what is listening."),
  c('e5', "Keep the system updated, with the apt routine from lesson thirty-two."),
  c('e6', "Give every user and service only the access it needs. That is least privilege."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: a firewall makes a server secure. No. It is one layer. Weak passwords and old software still get in."),
  c('my3', "Myth two: long S S H passwords are enough. No. Keys cannot be guessed, and passwords can be tried all day."),
  c('my4', "Myth three: changing the S S H port is security. No. It hides noise, but it is not a lock."),
  c('my5', "Myth four: if it is listening, it must be needed. No. Check it, and stop what you do not use."),
  c('my6', "Read it, lock it, filter it."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Read your addresses and routes, and say what the default route does."),
  c('b3', "List what is listening, and name the process."), c('b4', "Log in with a key, and say why the private key stays put."),
  c('b5', "Turn off password and root logins, and test the config before reloading."), c('b6', "Allow S S H, then enable the firewall, and list the rules."),
  c('b7', "Name three habits that cut risk."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own virtual machine. Never practise on a server you do not own, and keep a second session open when you change S S H or the firewall."),
  c('z2', "One: run ip -br addr, ip route and ss -tlnp, and write down what is listening."),
  c('z3', "Two: make a key pair, with a passphrase this time."),
  c('z4', "Three: add the public key to authorized keys, and log in with it."),
  c('z5', "Four: in a second session, turn off passwords and root login, and test with sshd dash t."),
  c('z6', "Five: allow S S H, enable the firewall, and list the rules."),
  c('z7', "Six: confirm you can still log in from the second session before you close the first."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which command shows your addresses?"), c('f13', "Which file lists the keys allowed to log in?"),
  c('f14', "Which command tests the S S H config before you reload it?"), c('f15', "What must you allow before you enable the firewall?"),
  c('f16', "Objective covered: MC04-O09.", "Objective covered: M C zero four, objective nine, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: diagnose and recover a broken system."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'n2': 0.4, 'n4': 0.4, 'n6': 0.4, 'n8': 0.5, 'k3': 0.4, 'k7': 3.0, 'k8': 0.5, 'r2': 0.4, 'r4': 0.4, 'r6': 0.4, 'r8': 0.5, 'w2': 0.3, 'w5': 1.0, 'w6': 0.4, 'w8': 0.4, 'w10': 0.5, 'e6': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'net': 'Your network, in four commands', 'ssh': 'Log in with a key', 'harden': 'Lock the SSH door', 'fw': 'A firewall in minutes', 'habits': 'Security habits', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))


def s_hook(C, D, dur):
    E = [El(T('The network is the front door.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Read it', 'addresses, routes, listeners', ACC), ('Lock it', 'SSH keys, no passwords', VIO), ('Filter it', 'a firewall with UFW', WARN)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100 + 0, 280 + i * 160, C['h2'] + i * 2.6))
    E.append(takeaway('Know it. Lock it. Filter it.', 850, C['h3'], GOOD, 1600)); return E
s_net = _lab('Your network, in four commands', 'Address, route, reach, listen.', 'n1', RB, [('n1', 'ip -br addr', 'Your addresses', ACC), ('n3', 'ip route', 'Where traffic goes', VIO), ('n5', 'ping -c 2', 'Can we reach it?', GOOD), ('n7', 'ss -tlnp', 'What is listening', WARN)])
s_ssh = _lab('Log in with a key', 'Private key stays. Public key goes.', 'k1', RB, [('k1', 'ssh-keygen', 'Make a key pair', ACC), ('k3', 'id_ed25519.pub', 'Public: safe to share', GOOD), ('k4', 'authorized_keys', 'Who may log in', VIO), ('k5', 'chmod 600', 'Lock the file down', WARN), ('k6', 'ssh localhost', 'Log in, no password', PINK)])
s_harden = _lab('Lock the SSH door', 'No passwords. No root login.', 'r1', RB, [('r1', 'sshd_config.d', 'The settings', ACC), ('r3', 'sshd -T', 'What is really used', VIO), ('r5', 'ssh, no key', 'Test the lock', BAD), ('r7', 'sshd -t', 'Test before reload', GOOD)])
s_fw = _lab('A firewall in minutes', 'Allow what you need. Deny the rest.', 'w1', RB, [('w1', 'ufw status', 'Inactive at first', ACC), ('w3', 'allow 22/tcp', 'SSH first!', WARN), ('w5', 'ufw enable', 'Switch it on', GOOD), ('w7', 'status numbered', 'List the rules', VIO), ('w9', 'delete allow', 'Remove a rule', PINK)])
def s_habits(C, D, dur):
    E = head('Security habits', 'Small habits stop most attacks.', C['e1'])
    it = [('1  Keys', 'not passwords', ACC, 'e2'), ('2  No root', 'login, use sudo', VIO, 'e3'), ('3  Few ports', 'know what listens', WARN, 'e4'), ('4  Updates', 'apt, every week', GOOD, 'e5'), ('5  Least', 'privilege for all', PINK, 'e6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    return E
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: firewall = secure', 'It is one layer only.', 'my2'), ('Myth: long passwords', 'Keys cannot be guessed.', 'my3'), ('Myth: new SSH port', 'Hides noise, not a lock.', 'my4'), ('Myth: listening = needed', 'Check it. Stop unused.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Read it. Lock it. Filter it.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Addresses and routes', 'b2'), ('What is listening', 'b3'), ('Key login', 'b4'), ('Harden SSH, test it', 'b5'), ('Firewall, SSH first', 'b6'), ('Three security habits', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Keep a second session open.', C['z1'])
    it = [('1  Look', 'ip, route, ss', PINK, 'z2'), ('2  Keys', 'with a passphrase', ACC, 'z3'), ('3  Login', 'authorized_keys', WARN, 'z4'), ('4  Harden', 'no passwords, sshd -t', VIO, 'z5'), ('5  Firewall', 'allow SSH, enable', BAD, 'z6'), ('6  Verify', 'second session first', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command shows your addresses?', 'f12'), ('Which file lists allowed keys?', 'f13'), ('Which command tests the SSH config?', 'f14'), ('What do you allow before enabling?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O09', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: diagnose and recover', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, net=s_net, ssh=s_ssh, harden=s_harden, fw=s_fw, habits=s_habits, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(net=('eye', GOOD), ssh=('gear', ACC), harden=('test', GOOD), fw=('eye', GOOD), habits=('board', WARN), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'net': [('n2', 2, 1, 4, 700, ''), ('n4', 1, 1, 4, 440, ''), ('n6', 6, 1, 4, 780, ''), ('n8', 2, 2, 4, 1060, '')],
 'ssh': [('k3', 1, 1, 4, 400, ''), ('k7', 2, 2, 4, 1065, ''), ('k8', 9, 1, 4, 70, '')],
 'harden': [('r2', 2, 2, 4, 480, ''), ('r4', 1, 2, 4, 420, ''), ('r6', 1, 1, 4, 760, ''), ('r8', 1, 1, 4, 150, '')],
 'fw': [('w2', 1, 1, 4, 260, ''), ('w6', 1, 1, 4, 740, ''), ('w8', 5, 2, 4, 600, ''), ('w10', 1, 1, 4, 160, '')],
}
