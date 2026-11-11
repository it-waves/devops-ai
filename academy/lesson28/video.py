import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 28  ·  DEVOPS BOOTCAMP'
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
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O03': 'M C zero four, objective three', 'grep': 'grep', 'tar': 'tar', 'sort': 'sort', 'uniq': 'unique', 'echo': 'echo', 'gz': 'G Z', 'tgz': 'T G Z', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 28', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "A server talks in text."),
  c('h2', "Logs, lists, configs. Far too much to read by hand."),
  c('h3', "Today you steer it: redirect, pipe, search, count, and pack it all up."),
 ]),
 ('redirect', [
  c('r1', "First, save output in a file. Type: echo hello server > hello.txt. The arrow sends output into the file.",
    "First, save output in a file. Type: echo, hello server, greater than, hello dot text. The arrow sends output into the file."),
  c('r2', "Nothing printed on screen. It went into the file. Read it with: cat hello.txt.", "Nothing printed on screen. It went into the file. Read it with: cat, hello dot text."),
  c('r3', "One arrow replaces the file. Two arrows add to the end. Type: echo second line >> hello.txt. Two arrows.",
    "One arrow replaces the file. Two arrows add to the end. Type: echo, second line, greater than, greater than, hello dot text."),
  c('r4', "Check it. Type: cat hello.txt. Both lines are there.", "Check it. Type: cat, hello dot text. Both lines are there."),
  c('r5', "Errors travel on their own channel, number two. Type: ls nothere 2> errors.txt.",
    "Errors travel on their own channel, number two. Type: L S, nothere, then two, greater than, errors dot text."),
  c('r6', "The error went into the file, not the screen. Type: cat errors.txt.", "The error went into the file, not the screen. Type: cat, errors dot text."),
 ]),
 ('pipe', [
  c('p1', "A pipe sends one command's output into the next command. Type: ls /etc | head -n 5.",
    "A pipe sends one command's output into the next command. Type: L S, slash, E T C, pipe, head, dash n, five."),
  c('p2', "Only the first five lines. Head read what L S produced.", "Only the first five lines. Head read what L S produced."),
  c('p3', "Now count how many entries there are. Type: ls /etc | wc -l.", "Now count how many entries there are. Type: L S, slash, E T C, pipe, W C, dash l."),
  c('p4', "One number. Two small tools, joined. This is the Linux way."),
  c('p5', "Pipes chain as far as you like. Type: find . -name \"*.log\" | wc -l.", "Pipes chain as far as you like. Type: find, dot, dash name, quote, star, dot log, quote, pipe, W C, dash l."),
  c('p6', "How many log files live under here? Four. One line answered it.", "How many log files livz under here? Four. One line answered it."),
 ]),
 ('grep', [
  c('g1', "Here is an application log. Type: grep ERROR app.log. Grep prints only the lines that match.", "Here is an application log. Type: grep, ERROR, app dot log. Grep prints only the lines that match."),
  c('g2', "Two errors, and nothing else. Now count them. Type: grep -c ERROR app.log.", "Two errors, and nothing else. Now count them. Type: grep, dash c, ERROR, app dot log."),
  c('g3', "Add line numbers. Type: grep -n ERROR app.log. Now you know where to look.", "Add line numbers. Type: grep, dash n, ERROR, app dot log. Now you know where to look."),
  c('g4', "Ignore upper and lower case with dash i. Type: grep -i warning app.log.", "Ignore upper and lower case with dash i. Type: grep, dash i, warning, app dot log."),
  c('g5', "Everything except a word. Dash v inverts the match. Type: grep -v INFO app.log.", "Everything except a word. Dash v inverts the match. Type: grep, dash v, INFO, app dot log."),
  c('g6', "And search a whole folder. Dash r is recursive. Type: grep -r timeout .", "And search a whole folder. Dash r is recursive. Type: grep, dash r, timeout, then a dot."),
  c('g7', "Every match, with its file name in front. That is how you find which config mentions a setting."),
 ]),
 ('sortcut', [
  c('t1', "Text tools clean up lists. Type: sort fruits.txt. Sort puts the lines in order.", "Text tools clean up lists. Type: sort, fruits dot text. Sort puts the lines in order."),
  c('t2', "To count repeats, sort first, then pipe into unique dash c. Type: sort fruits.txt | uniq -c.",
    "To count repeats, sort first, then pipe into unique dash c. Type: sort, fruits dot text, pipe, unique, dash c."),
  c('t3', "Unique only collapses neighbours, so sorting first matters. Apple appears three times."),
  c('t4', "Biggest count first. Add a pipe: | sort -rn.", "Biggest count first. Add a pipe to sort, dash r n."),
  c('t5', "Now a table. Type: cut -d, -f1 users.csv. Cut takes one column.", "Now a table. Type: cut, dash d, comma, dash f, one, users dot C S V. Cut takes one column."),
  c('t6', "Dash d sets the divider, a comma. Dash f picks the field. Field one is the name."),
 ]),
 ('archive', [
  c('a1', "To back up or ship a folder, pack it with tar. Type: tar -czf backup.tar.gz project.", "To back up or ship a folder, pack it with tar. Type: tar, dash c z f, backup dot tar dot G Z, project."),
  c('a2', "C creates, Z compresses, F names the file. No output means success. Check the size with: ls -lh.", "C creates, Z compresses, F names the file. No output means success. Check the size with: L S, dash l h."),
  c('a3', "Look inside without unpacking. Type: tar -tzf backup.tar.gz. T means table of contents.", "Look inside without unpacking. Type: tar, dash t z f, backup dot tar dot G Z. T means table of contents."),
  c('a4', "Restore it somewhere safe. Type: mkdir restore.", "Restore it somewhere safe. Type: make dir, restore."),
  c('a5', "Then: tar -xzf backup.tar.gz -C restore. X extracts, capital C sets the target folder.", "Then: tar, dash x z f, backup dot tar dot G Z, dash capital C, restore. X extracts, capital C sets the target folder."),
  c('a6', "Check with: ls restore. The project is back."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: one arrow adds to a file. No. One arrow replaces it. Two arrows add."),
  c('my3', "Myth two: a pipe saves output to a file. No. A pipe feeds the next command. An arrow feeds a file."),
  c('my4', "Myth three: grep changes the file. No. It only reads, and prints matches."),
  c('my5', "Myth four: tar compresses by itself. It only packs. The Z flag compresses.", "Myth four: tar compresses by itself. It only packs. The Z flag compresses."),
  c('my6', "Arrow to file. Pipe to command."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Redirect output into a file, and append to it."),
  c('b3', "Chain two commands with a pipe."), c('b4', "Search with grep, using at least two flags."),
  c('b5', "Sort and count repeats."), c('b6', "Pack and unpack a tar archive."),
  c('b7', "Say what each tar flag does."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. Work only inside a practice folder."),
  c('z2', "One: save the output of L S slash etc into a file, then append the date to it.", "One: save the output of L S, slash, E T C, into a file, then append the date to it."),
  c('z3', "Two: use a pipe to count the lines in that file."),
  c('z4', "Three: write a small log with a few ERROR lines, then use grep to count and number them."),
  c('z5', "Four: make a list with repeats, and show a count of each, biggest first."),
  c('z6', "Five: pack a folder with tar, list the archive, and restore it into a new folder."),
  c('z7', "Six: compare the restored folder with the original, and write one sentence about what you found."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which arrow adds to the end of a file?"), c('f13', "What does a pipe connect?"),
  c('f14', "Which grep flag counts matching lines?"), c('f15', "Which tar flag extracts?"),
  c('f16', "Objective covered: MC04-O03.", "Objective covered: M C zero four, objective three, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: users, permissions and S S H keys.", "Next lesson: users, permissions and S S H keys."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'t4': 0.4, 'h3': 0.5, 'r6': 0.5, 'p4': 0.5, 'p6': 0.5, 'g7': 0.5, 't3': 0.3, 't6': 0.5, 'a6': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'redirect': 'Redirect output', 'pipe': 'Pipes', 'grep': 'Search with grep', 'sortcut': 'Sort, count and cut', 'archive': 'Pack with tar', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def s_hook(C, D, dur):
    E = [El(T('A server is made of files.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Configs', 'settings as text', ACC), ('Logs', 'what happened', VIO), ('Scripts and data', 'what it runs on', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('Make. Read. Move. Edit. Safely.', 850, C['h3'], GOOD, 1600)); return E
def s_hook(C, D, dur):
    E = [El(T('A server talks in text.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Logs', 'thousands of lines', VIO), ('Lists', 'names, files, users', ACC), ('Configs', 'settings as text', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('Redirect. Pipe. Search. Count. Pack.', 850, C['h3'], GOOD, 1600)); return E
s_redirect = _lab('Redirect output', 'Send output to a file instead of the screen.', 'r1', RB, [('r1', '>', 'Replace the file', ACC), ('r3', '>>', 'Add to the end', VIO), ('r5', '2>', 'Errors only', WARN)])
s_pipe = _lab('Pipes', 'Output of one command feeds the next.', 'p1', RB, [('p1', 'a | b', 'Pipe into next', ACC), ('p3', '| wc -l', 'Count the lines', VIO), ('p5', 'find | wc -l', 'Chain commands', WARN)])
s_grep = _lab('Search with grep', 'Print only the lines that match.', 'g1', RB, [('g1', 'grep word file', 'Matching lines', ACC), ('g2', '-c', 'Count matches', VIO), ('g3', '-n', 'Line numbers', WARN), ('g4', '-i', 'Ignore case', PINK), ('g5', '-v', 'Everything else', GOOD), ('g6', '-r', 'Whole folder', BAD)])
s_sortcut = _lab('Sort, count and cut', 'Small tools for lists and tables.', 't1', RB, [('t1', 'sort', 'Put in order', ACC), ('t2', 'uniq -c', 'Count repeats', VIO), ('t4', 'sort -rn', 'Biggest first', WARN), ('t5', 'cut -d, -f1', 'One column', PINK)])
s_archive = _lab('Pack with tar', 'Back up a folder in one file.', 'a1', RB, [('a1', 'tar -czf', 'Create, compress', ACC), ('a3', 'tar -tzf', 'List contents', VIO), ('a5', 'tar -xzf -C', 'Extract to a folder', WARN)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: > adds to a file', 'One arrow replaces. Two add.', 'my2'), ('Myth: a pipe saves a file', 'A pipe feeds a command.', 'my3'), ('Myth: grep edits the file', 'It only reads and prints.', 'my4'), ('Myth: tar compresses alone', 'The z flag compresses.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Arrow to file. Pipe to command.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Redirect: > and >>', 'b2'), ('Chain commands with a pipe', 'b3'), ('grep with two flags', 'b4'), ('sort and count repeats', 'b5'), ('Pack and unpack with tar', 'b6'), ('Explain each tar flag', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine. Practice folder only.', C['z1'])
    it = [('1  Redirect', 'ls /etc > and >>', PINK, 'z2'), ('2  Pipe', 'count the lines', ACC, 'z3'), ('3  grep', 'count, number', WARN, 'z4'), ('4  Count', 'sort, uniq -c', VIO, 'z5'), ('5  tar', 'pack, list, restore', GOOD, 'z6'), ('6  Compare', 'one sentence', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which arrow adds to the end of a file?', 'f12'), ('What does a pipe connect?', 'f13'), ('Which grep flag counts matching lines?', 'f14'), ('Which tar flag extracts?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O03', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: users, permissions and SSH keys', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, redirect=s_redirect, pipe=s_pipe, grep=s_grep, sortcut=s_sortcut, archive=s_archive, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(redirect=('eye', GOOD), pipe=('steps', ACC), grep=('eye', GOOD), sortcut=('eye', GOOD), archive=('eye', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'grep': [('g2', 1, 2, 4, 400, ''), ('g3', 1, 1, 4, 300, '')],
 'sortcut': [('t3', 1, 1, 4, 330, '')],
}
