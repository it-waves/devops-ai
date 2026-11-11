import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 26  ·  DEVOPS BOOTCAMP'
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
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O01': 'M C zero four, objective one', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 26', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "You log in to a server you have never seen. No desktop. No map."),
  c('h2', "Where are you? Where does everything live? And who do you ask when you are stuck?"),
  c('h3', "This lesson gives you the map, the moves, and the manual."),
 ]),
 ('where', [
  c('w1', "First question on any server: where am I? Type: pwd, which means print working directory.", "First question on any server: where am I? Type: P W D, which means print working directory."),
  c('w2', "Slash home slash student. That is my home folder, and the prompt shows it as a tilde."),
  c('w3', "What is here? Type: ls.", "What is here? Type: L S."),
  c('w4', "A file, and a folder. But ls hides some things. Type: ls -a, where a means all.", "A file, and a folder. But L S hides some things. Type: L S, dash a, where a means all."),
  c('w5', "Names that start with a dot are hidden. The single dot is this folder, and two dots are its parent."),
  c('w6', "For details, type: ls -l. That is a long listing.", "For details, type: L S, dash l. That is a long listing."),
  c('w7', "The first letter is the type: dash for a file, d for a directory. Then permissions, owner, size, date and name. Permissions get their own lesson."),
 ]),
 ('symbols', [
  c('y1', "Four shortcuts make paths short."),
  c('y2', "A dot means here, this folder."),
  c('y3', "Two dots mean the parent, one level up."),
  c('y4', "A tilde means your home folder."),
  c('y5', "A dash, after C D, means the last folder you were in.", "A dash, after C D, means the last folder you were in."),
  c('y6', "A path that starts with a slash is absolute, and works from anywhere. Anything else is relative, and depends on where you stand."),
 ]),
 ('paths', [
  c('m1', "Now move. A path says where something is. Type: cd projects/cloudcart/app. This is a relative path, so it starts from where I stand.",
    "Now move. A path says where something is. Type: C D, projects, slash, cloudcart, slash, app. This is a relative path, so it starts from where I stand."),
  c('m2', "No output means it worked. The prompt now shows the full route. Confirm with: pwd.", "No output means it worked. The prompt now shows the full route. Confirm with: P W D."),
  c('m3', "Go sideways. Type: cd ../config. Two dots go up one folder, then down into config.", "Go sideways. Type: C D, dot dot, slash, config. Two dots go up one folder, then down into config."),
  c('m4', "Now an absolute path. It starts with a slash. Type: cd /var/log.", "Now an absolute path. It starts with a slash. Type: C D, slash, var, slash, log."),
  c('m5', "Jump back to where I was. Type: cd, space, dash.", "Jump back to where I was. Type: C D, space, dash."),
  c('m6', "It prints the folder, and takes you there. Now home, from anywhere. Type: cd, with nothing after it.", "It prints the folder, and takes you there. Now home, from anywhere. Type: C D, with nothing after it."),
  c('m7', "Last trick: let the shell type for you. Type: cd, space, p r o, then press Tab. Then c l, and Tab again.", "Last trick: let the shell type for you. Type: C D, space, p r o, then press Tab. Then c l, and Tab again."),
  c('m8', "Tab completes names. It is faster, and it prevents typos. If nothing happens, press Tab twice to see the choices."),
 ]),
 ('map', [
  c('p1', "Here is the map, in eight folders."),
  c('p2', "Slash etc: configuration, as plain text files."),
  c('p3', "Slash var: logs, caches and data that change."),
  c('p4', "Slash usr: programs and libraries."),
  c('p5', "Slash home: one folder for every user."),
  c('p6', "Slash tmp: temporary files, cleared at reboot."),
  c('p7', "Slash proc and slash dev: not real files. The kernel's live view, and devices."),
  c('p8', "Slash bin and slash sbin: on modern Ubuntu, links into slash usr."),
  c('p9', "Learn these eight, and any Linux server feels familiar."),
 ]),
 ('tour', [
  c('t1', "Linux has one tree. Everything starts at a single slash, called root. Type: ls /.", "Linux has one tree. Everything starts at a single slash, called root. Type: L S, space, slash."),
  c('t2', "No C drive, no D drive. Disks are attached inside this tree. These are the standard top level folders."),
  c('t3', "Look closer at three of them. Type: ls -ld /bin /sbin /lib", "Look closer at three of them. Type: L S, dash l d, slash bin, slash S bin, slash lib."),
  c('t4', "Each one is an arrow, pointing into slash usr. Modern Ubuntu keeps every program under usr, and the old paths are links."),
  c('t5', "Settings live in slash etc. See which Linux this is. Type: head -3 /etc/os-release", "Settings live in slash E T C. See which Linux this is. Type: head, dash three, slash E T C, slash O S, dash release."),
  c('t6', "Ubuntu, twenty four point oh four. A plain text file. Editing files like this is how you configure a server."),
  c('t7', "Package settings sit in folders here too. Type: ls /etc/apt", "Package settings sit in folders here too. Type: L S, slash E T C, slash apt."),
  c('t8', "One folder per job: sources, keys, preferences. Remember, slash etc is where to look first."),
  c('t9', "Logs live in slash var. Type: ls /var/log", "Logs live in slash var. Type: L S, slash var, slash log."),
  c('t10', "When a service misbehaves, the answer is usually in a log here. We read them in a later lesson."),
  c('t11', "One more. Slash proc is not a disk. Type: head -2 /proc/meminfo", "One more. Slash proc is not a disk. Type: head, dash two, slash proc, slash mem info."),
  c('t12', "Those numbers are real, right now, in kilobytes. No file on disk holds them. The kernel makes them up, as you read."),
 ]),
 ('docsmap', [
  c('q1', "Now the third question: who do I ask? Four tools, from fastest to deepest."),
  c('q2', "Type, and which: what is this command, and where does it live?"),
  c('q3', "Dash dash help: a short summary of the options."),
  c('q4', "Man: the full manual, split into sections."),
  c('q5', "Apropos: search the manuals by topic, when you forget the name."),
  c('q6', "Start small. Go deeper only when you need to."),
 ]),
 ('docs', [
  c('d1', "Start with what a command is. Type: type cd.", "Start with what a command is. Type: type, C D."),
  c('d2', "A shell builtin. It lives inside the shell itself. Compare. Type: type cp.", "A shell builtin. It lives inside the shell itself. Compare. Type: type, C P."),
  c('d3', "A real program, in slash usr slash bin. Now quick help. Type: ls --help | head -8", "A real program, in slash U S R, slash bin. Now quick help. Type: L S, dash dash help, pipe, head, dash eight."),
  c('d4', "Almost every command has this. Pipe it into head, so the screen does not flood."),
  c('d5', "For the full manual, type: man ls.", "For the full manual, type: man, L S."),
  c('d6', "This is a pager. Space scrolls a page. Slash, then a word, searches. And q quits."),
  c('d7', "Read three parts: the name, the synopsis, and the option you need. Square brackets mean optional."),
  c('d8', "Manuals have sections. Type: whatis passwd.", "Manuals have sections. Type: what is, passwd."),
  c('d9', "Passwd appears twice. Section one is the command. Section five is the file format. Type: man 5 passwd.", "Passwd appears twice. Section one is the command. Section five is the file format. Type: man, five, passwd."),
  c('d10', "Now it describes the file, field by field. That is the page you need when you edit it. Q to quit."),
  c('d11', "And when you forget the command name, search by topic. Type: apropos -s1 'copy files'", "And when you forget the command name, search by topic. Type: apropos, dash s one, quote, copy files, quote."),
  c('d12', "Copy a file: cp. The result tells you the name, and the section. Then man cp has the details."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: Linux has drive letters. No. One tree, and disks are attached inside it."),
  c('my3', "Myth two: man pages are only for experts. Read the name, the synopsis, then search for your option."),
  c('my4', "Myth three: run commands from anywhere. Many commands depend on where you are, so check P W D first."),
  c('my5', "Myth four: slash bin and slash usr slash bin are different. On modern Ubuntu, one is a link to the other."),
  c('my6', "Check, then act."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Say where you are, with P W D."),
  c('b3', "Move with relative, absolute, parent and home paths."), c('b4', "Say what each of the eight top level folders holds."),
  c('b5', "Tell a builtin from a program, with type."), c('b6', "Find help with dash dash help, and with man."),
  c('b7', "Choose the right manual section for a file format."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in the virtual machine you built. Everything here only reads, so nothing can break."),
  c('z2', "One: run P W D and ls -a in your home folder. Write down what you see."),
  c('z3', "Two: move to slash var slash log with an absolute path, back with C D dash, and home with C D alone."),
  c('z4', "Three: list slash, and write one line about each of the eight folders."),
  c('z5', "Four: run type on C D and on cp, and say what the difference means."),
  c('z6', "Five: with man, find which command shows free disk space, and which section describes the file slash etc slash hosts."),
  c('z7', "Six: use ls only, to find where the ssh client settings live."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which command shows where you are?"), c('f13', "What does a path that starts with a slash mean?"),
  c('f14', "Which folder holds settings, and which holds logs?"), c('f15', "Which tool searches manuals by topic?"),
  c('f16', "Objective covered: MC04-O01.", "Objective covered: M C zero four, objective one, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: files and directories."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'w7': 0.5, 'y6': 0.5, 'm8': 0.5, 'p9': 0.5, 't12': 0.5, 'q6': 0.5, 'd12': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'where': 'Where am I?', 'symbols': 'Path shortcuts', 'paths': 'Moving around', 'map': 'The filesystem map', 'tour': 'Tour of the tree', 'docsmap': 'Who do I ask?', 'docs': 'Manuals and help',
        'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def s_hook(C, D, dur):
    E = [El(T('Lost on a server?', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Where am I?', 'pwd', ACC), ('Where does it live?', 'the map', VIO), ('Who do I ask?', 'the manual', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.6))
    E.append(takeaway('The map. The moves. The manual.', 850, C['h3'], GOOD, 1600)); return E
s_where = _lab('Where am I?', 'Three commands to get your bearings.', 'w1', RB, [('w1', 'pwd', 'Where am I?', ACC), ('w3', 'ls', 'What is here?', VIO), ('w4', 'ls -a', 'Show hidden names', WARN), ('w6', 'ls -l', 'The long listing', PINK)])
def s_symbols(C, D, dur):
    E = head('Path shortcuts', 'Four symbols and two kinds of path.', C['y1'])
    for i, (a, b, col, cid) in enumerate([('.', 'here, this folder', ACC, 'y2'), ('..', 'the parent, one up', VIO, 'y3'), ('~', 'your home folder', WARN, 'y4'), ('-', 'the last folder', PINK, 'y5')]):
        E.append(Pop(card(840, 150, col, a, [(b, TXT)], 56, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 180, C[cid]))
    E.append(Pop(card(840, 150, GOOD, 'Absolute', [('/var/log  ·  works from anywhere', TXT)], 40, 30), 100, 740, C['y6']))
    E.append(Pop(card(840, 150, WARN, 'Relative', [('projects/app  ·  depends on where you stand', TXT)], 40, 30), 980, 740, C['y6'] + 3.0)); return E
s_paths = _lab('Moving around', 'Relative, absolute, back and home.', 'm1', RB, [('m1', 'cd projects/…', 'Relative path', ACC), ('m3', 'cd ../config', 'Up, then down', VIO), ('m4', 'cd /var/log', 'Absolute path', WARN), ('m5', 'cd -', 'Back where I was', PINK), ('m6', 'cd', 'Home from anywhere', GOOD), ('m7', 'Tab', 'Let the shell type', ACC)])
def s_map(C, D, dur):
    E = head('The filesystem map', 'Eight folders to learn.', C['p1'])
    it = [('/etc', 'settings', ACC, 'p2'), ('/var', 'logs and data', VIO, 'p3'), ('/usr', 'programs', WARN, 'p4'), ('/home', 'user folders', PINK, 'p5'), ('/tmp', 'temporary files', GOOD, 'p6'), ('/proc  /dev', 'kernel and devices', BAD, 'p7'), ('/bin  /sbin', 'links into /usr', ACC, 'p8')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(400, 215, col, a, [(b, TXT)], 44, 30, True), 100 + (i % 4) * 430, 330 + (i // 4) * 245, C[cid]))
    E.append(takeaway('Eight folders. One tree.', 850, C['p9'], GOOD, 1500)); return E
s_tour = _lab('Tour of the tree', 'Real folders, real files.', 't1', RB, [('t1', 'ls /', 'One tree, one root', ACC), ('t3', 'ls -ld /bin …', 'Links into /usr', VIO), ('t5', '/etc/os-release', 'Settings are text', WARN), ('t7', 'ls /etc/apt', 'One folder per job', PINK), ('t9', 'ls /var/log', 'Logs live here', GOOD), ('t11', '/proc/meminfo', 'Not a real file', BAD)])
def s_docsmap(C, D, dur):
    E = head('Who do I ask?', 'Four tools, fastest to deepest.', C['q1'])
    for i, (a, b, col, cid) in enumerate([('type  ·  which', 'What is it, and where?', ACC, 'q2'), ('--help', 'A short summary', VIO, 'q3'), ('man', 'The full manual', WARN, 'q4'), ('apropos', 'Search by topic', PINK, 'q5')]):
        E.append(Pop(card(840, 170, col, a, [(b, TXT)], 48, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 200, C[cid]))
    E.append(takeaway('Start small. Go deeper when needed.', 800, C['q6'], GOOD, 1600)); return E
s_docs = _lab('Manuals and help', 'Find the answer yourself.', 'd1', RB, [('d1', 'type cd', 'Builtin or program?', ACC), ('d3', 'ls --help', 'A quick summary', VIO), ('d5', 'man ls', 'The full manual', WARN), ('d8', 'whatis passwd', 'Sections 1 and 5', PINK), ('d9', 'man 5 passwd', 'The file format', GOOD), ('d11', 'apropos', 'Search by topic', BAD)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: drive letters', 'One tree. Disks attach inside it.', 'my2'), ('Myth: man is for experts', 'Name, synopsis, then search.', 'my3'), ('Myth: run it from anywhere', 'Check pwd before you act.', 'my4'), ('Myth: /bin is not /usr/bin', 'On Ubuntu, a link to it.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Check, then act.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Say where you are', 'b2'), ('Move with four path kinds', 'b3'), ('Name the eight folders', 'b4'), ('Builtin or program', 'b5'), ('Help and man pages', 'b6'), ('Pick the manual section', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine. Read only.', C['z1'])
    it = [('1  Where', 'pwd and ls -a', PINK, 'z2'), ('2  Move', 'absolute, cd -, cd', ACC, 'z3'), ('3  Map', 'ls /  and notes', WARN, 'z4'), ('4  Type', 'cd versus cp', VIO, 'z5'), ('5  Man', 'df, and /etc/hosts', GOOD, 'z6'), ('6  Find', 'ssh settings, ls only', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command shows where you are?', 'f12'), ('What does a leading slash mean?', 'f13'), ('Where are settings? Where are logs?', 'f14'), ('Which tool searches manuals by topic?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O01', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: files and directories', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, where=s_where, symbols=s_symbols, paths=s_paths, map=s_map, tour=s_tour, docsmap=s_docsmap, docs=s_docs, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(where=('eye', GOOD), symbols=('steps', ACC), paths=('eye', GOOD), map=('board', VIO), tour=('eye', GOOD), docsmap=('question', VIO), docs=('eye', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'where': [('w2', 1, 1, 4, 200, '')],
 'tour': [('t4', 1, 3, 570, 835, ''), ('t6', 1, 3, 4, 440, ''), ('t12', 1, 2, 4, 330, '')],
 'docs': [('d2', 1, 1, 4, 330, ''), ('d12', 1, 1, 4, 780, '')],
}
