import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 32  ·  DEVOPS BOOTCAMP'
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
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 32', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "Every server runs software that someone had to install. Doing it by hand does not scale."),
  c('h2', "On Ubuntu, a package manager does it for you. A package is a program, plus the list of what it needs. Apt finds packages in repositories, and D P K G installs them."),
  c('h3', "Today you read the repository list, inspect packages, preview an install, and learn the update routine."),
 ]),
 ('repo', [
  c('q1', "Where do packages come from? From repositories, listed in one file. Type: grep ^URIs, then the path.", "Where do packages come from? From repositories, listed in one file. Type: grep, caret, U R Is, then the path. The caret keeps only lines that start with that word."),
  c('q2', "Two addresses. The main Ubuntu archive, and a separate security archive. Each one is a repository."),
  c('q3', "Now the suites. Type: grep ^Suites, and the same path.", "Now the suites. Type: grep, caret, Suites, and the same path."),
  c('q4', "Suites are release channels. Noble is Ubuntu twenty-four oh four as released. Noble dash updates carries fixes. Noble dash security carries security fixes.", "Suites are release channels. Noble is Ubuntu twenty-four oh four as released. Noble dash updates carries fixes. Noble dash security carries security fixes."),
  c('q5', "Now ask about one package. Type: apt-cache policy curl | head -n 4.", "Now ask about one package. Type: apt cache, policy, curl, pipe, head, dash n, four."),
  c('q6', "Installed is the version you have. Candidate is the newest version the repositories offer. If they differ, an update is waiting."),
 ]),
 ('installed', [
  c('d1', "What is installed? Ask the package database. Type: dpkg -s curl | head -n 4.", "What is installed? Ask the package database. Type: D P K G, dash s, curl, pipe, head, dash n, four."),
  c('d2', "Status says install ok installed. The database is the record of what is on this machine."),
  c('d3', "Which package owns a file? Type: dpkg -S /usr/bin/curl.", "Which package owns a file? Type: D P K G, dash capital S, slash U S R, slash bin, slash curl."),
  c('d4', "The curl package owns it. Use this when you find a file and wonder where it came from."),
  c('d5', "And which files does a package put on disk? Type: dpkg -L curl | grep bin.", "And which files does a package put on disk? Type: D P K G, dash capital L, curl, pipe, grep, bin."),
  c('d6', "The bin folder, and the curl program itself."),
 ]),
 ('plan', [
  c('n1', "Always preview first. Dash s means simulate, so nothing changes. Type: apt-get -s install cowsay | tail -n 6.", "Always preview first. Dash s means simulate, so nothing changes. Type: apt get, dash s, install, cowsay, pipe, tail, dash n, six."),
  c('n2', "Two packages would be installed: cowsay, and a library it depends on. Apt works out dependencies for you."),
  c('n3', "The Inst lines are the plan, and the dependency comes first."),
  c('n4', "Now preview a removal. Type: apt-get -s remove curl | tail -n 4.", "Now preview a removal. Type: apt get, dash s, remove, curl, pipe, tail, dash n, four."),
  c('n5', "It would remove curl. Read what will be removed before you agree to anything."),
  c('n6', "How many updates are waiting? Type: apt-get -s upgrade | grep, and keep the line that starts with a number.", "How many updates are waiting? Type: apt get, dash s, upgrade, pipe, grep, and keep the line that starts with a number."),
  c('n7', "The first number is how many packages could be upgraded. Your number will differ."),
 ]),
 ('manage', [
  c('a1', "Now the commands that change the system. They need sue do and a real machine, so these screens are an illustration."),
  c('a2', "First: sudo apt update. It refreshes the package lists from the repositories. It installs nothing."),
  c('a3', "Then: sudo apt install, and the package name. Apt shows the plan, and asks you to confirm."),
  c('a4', "To bring everything current: sudo apt upgrade. Update first, then upgrade."),
  c('a5', "Remove takes the program away. Purge also deletes its configuration files."),
  c('a6', "Then: sudo apt autoremove. It removes dependencies that nothing needs any more."),
  c('a7', "Add repositories only from sources you trust. Read the plan, then answer yes."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: apt update installs updates. No. Update refreshes the list. Upgrade installs."),
  c('my3', "Myth two: remove deletes everything. No. Purge also deletes the configuration."),
  c('my4', "Myth three: any download is safe if it installs. No. Use trusted repositories."),
  c('my5', "Myth four: answer yes to every prompt. No. Read the plan first."),
  c('my6', "Update, read the plan, then upgrade."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Read the repository list, and say where packages come from."),
  c('b3', "Compare the installed and candidate versions."), c('b4', "Find which package owns a file, with D P K G."),
  c('b5', "Preview an install with a simulation, and read the plan."), c('b6', "Explain update, upgrade, remove, purge and autoremove."),
  c('b7', "Say how to add software safely."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. These tasks only read, or simulate. Nothing is installed."),
  c('z2', "One: read your repository list, and name the suites."),
  c('z3', "Two: run apt-cache policy for a package, and compare installed with candidate."),
  c('z4', "Three: use D P K G dash s and dash capital S on a program you use."),
  c('z5', "Four: simulate an install of a small package, with dash s, and read the plan."),
  c('z6', "Five: run sudo apt update, then apt list dash dash upgradable. Update only refreshes the lists.", "Five: run sue do apt update, then apt list, dash dash upgradable. Update only refreshes the lists."),
  c('z7', "Six: simulate a removal, and say what purge would add."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which command refreshes the package lists?"), c('f13', "Which flag simulates an install?"),
  c('f14', "Which D P K G option finds the owner of a file?"), c('f15', "Does remove delete configuration files?"),
  c('f16', "Objective covered: MC04-O07.", "Objective covered: M C zero four, objective seven, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: disks, filesystems and mounts."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'q3': 1.0, 'h3': 0.5, 'q2': 0.4, 'q4': 0.5, 'q6': 0.5, 'd2': 0.4, 'd4': 0.4, 'd6': 0.5, 'n2': 0.4, 'n3': 0.4, 'n5': 0.4, 'n7': 0.5, 'a1': 0.4, 'a2': 0.4, 'a5': 0.4, 'a7': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'repo': 'Repositories and versions', 'installed': 'Inspect installed packages', 'plan': 'Preview before you change', 'manage': 'Install, update, remove', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))

def s_hook(C, D, dur):
    E = [El(T('Software arrives in packages.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Package', 'a program plus what it needs', ACC), ('Repository', 'where packages are kept', VIO), ('apt and dpkg', 'find them, install them', WARN)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 2.6))
    E.append(takeaway('Preview. Then change.', 850, C['h3'], GOOD, 1600)); return E
s_repo = _lab('Repositories and versions', 'Where packages come from.', 'q1', RB, [('q1', 'sources file', 'The repository list', ACC), ('q3', 'Suites', 'Release channels', VIO), ('q5', 'apt-cache policy', 'Installed vs candidate', GOOD)])
s_installed = _lab('Inspect installed packages', 'Ask the package database.', 'd1', RB, [('d1', 'dpkg -s', 'What is installed', ACC), ('d3', 'dpkg -S', 'Who owns a file', VIO), ('d5', 'dpkg -L', 'Files it installed', WARN)])
s_plan = _lab('Preview before you change', 'Simulate with -s. Nothing changes.', 'n1', RB, [('n1', 'install -s', 'Preview an install', GOOD), ('n3', 'Inst lines', 'The plan', ACC), ('n4', 'remove -s', 'Preview a removal', BAD), ('n6', 'upgrade -s', 'Updates waiting', WARN)])
def s_manage(C, D, dur):
    E = head('Install, update, remove', 'The routine, with sudo.', C['a1']); E.append(ill(C['a1'] + 0.2, 1260, 286))
    rows = [('$ sudo apt update', GOOD), ('Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease', TXT), ('Get:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease', TXT), ('Get:3 http://security.ubuntu.com/ubuntu noble-security InRelease', TXT), ('Fetched 252 kB in 1s', TXT), ('Reading package lists... Done', TXT), ('22 packages can be upgraded.', TXT)]
    mono_panel(E, 100, 345, 1060, rows, C['a2'], fs=22, lh=38)
    hbar(E, 112, 345 + 24 + 6 * 38 - 4, 1030, 36, C['a4'], C['a4'] + dur['a4'] + 0.5, WARN)
    it = [('sudo apt update', 'Refresh the lists', ACC, 'a2'), ('sudo apt install pkg', 'Shows the plan, asks', VIO, 'a3'), ('sudo apt upgrade', 'Update, then upgrade', GOOD, 'a4'), ('remove  /  purge', 'Purge deletes config too', WARN, 'a5'), ('sudo apt autoremove', 'Unneeded dependencies', PINK, 'a6')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(560, 105, col, a, [(b, TXT)], 32, 26), 1260, 345 + i * 118, C[cid]))
    E.append(takeaway('Read the plan. Then answer yes.', 920, C['a7'], GOOD, 1100)); return E
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: update installs', 'Update = refresh the list.', 'my2'), ('Myth: remove deletes all', 'Purge deletes config.', 'my3'), ('Myth: it installs, so safe', 'Use trusted repositories.', 'my4'), ('Myth: yes to every prompt', 'Read the plan first.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Update. Read. Upgrade.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Repositories and sources', 'b2'), ('Installed vs candidate', 'b3'), ('Which package owns a file', 'b4'), ('Simulate and read the plan', 'b5'), ('Update, upgrade, purge', 'b6'), ('Add software safely', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Read and simulate only. Nothing is installed.', C['z1'])
    it = [('1  Sources', 'read the list, suites', PINK, 'z2'), ('2  Policy', 'installed vs candidate', ACC, 'z3'), ('3  Inspect', 'dpkg -s and dpkg -S', WARN, 'z4'), ('4  Preview', 'apt-get -s install', VIO, 'z5'), ('5  Update', 'apt update, upgradable', GOOD, 'z6'), ('6  Remove', 'simulate, purge', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command refreshes the lists?', 'f12'), ('Which flag simulates an install?', 'f13'), ('Which option finds a file owner?', 'f14'), ('Does remove delete config files?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: disks, filesystems, mounts', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, repo=s_repo, installed=s_installed, plan=s_plan, manage=s_manage, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(repo=('eye', GOOD), installed=('eye', GOOD), plan=('eye', GOOD), manage=('gear', ACC), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'repo': [('q2', 1, 2, 4, 592, ''), ('q4', 1, 2, 4, 652, ''), ('q6', 2, 2, 4, 450, '')],
 'installed': [('d2', 2, 1, 4, 424, ''), ('d4', 1, 1, 4, 290, ''), ('d6', 1, 2, 4, 216, '')],
 'plan': [('n2', 1, 2, 4, 948, ''), ('n3', 3, 2, 4, 1062, ''), ('n5', 1, 2, 4, 700, ''), ('n5', 4, 1, 4, 454, ''), ('n7', 1, 1, 4, 948, '')],
}
