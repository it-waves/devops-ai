import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 27  ·  DEVOPS BOOTCAMP'
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
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 27', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "Files are what a server is made of."),
  c('h2', "Configs, logs, scripts and data. Every task starts by making, reading, moving or fixing one."),
  c('h3', "Today you handle them safely, and you edit with vim."),
 ]),
 ('make', [
  c('k1', "Build a practice area. Type: mkdir -p lab27/docs/old. The dash p flag makes every parent folder in one go.",
    "Build a practice area. Type: make dir, dash p, lab twenty seven, slash, docs, slash, old. The dash p flag makes every parent folder in one go."),
  c('k2', "Step inside. Type: cd lab27.", "Step inside. Type: C D, lab twenty seven."),
  c('k3', "Now empty files. Type: touch hello.txt notes.txt. Touch creates a file when it does not exist.",
    "Now empty files. Type: touch, hello dot text, notes dot text. Touch creates a file when it does not exist."),
  c('k4', "Check with: ls -l. Look at the size column.", "Check with: L S, dash l. Look at the size column."),
  c('k5', "Zero bytes. Both files exist, and both are empty. A folder starts with the letter d."),
 ]),
 ('inspect', [
  c('i1', "Bring in a file with real content. Type: cp ~/shopping.txt . with a space, then a dot. The dot means here.",
    "Bring in a file with real content. Type: C P, tilde, slash, shopping dot text, space, dot. The dot means here."),
  c('i2', "Read it all with: cat shopping.txt. Cat prints a file.", "Read it all with: cat, shopping dot text. Cat prints a file."),
  c('i3', "For a quick peek, type: head -n 3 shopping.txt. Head shows the first lines.", "For a quick peek, type: head, dash n, three, shopping dot text. Head shows the first lines."),
  c('i4', "And the end of a file. Type: tail -n 2 shopping.txt. Tail is the one you will use on logs.", "And the end of a file. Type: tail, dash n, two, shopping dot text. Tail is the one you will use on logs."),
  c('i5', "How long is it? Type: wc -l shopping.txt. W C counts, and dash l counts lines.", "How long is it? Type: W C, dash l, shopping dot text. W C counts, and dash l counts lines."),
  c('i6', "And what kind of file is it? Type: file shopping.txt.", "And what kind of file is it? Type: file, shopping dot text."),
  c('i7', "ASCII text. Linux does not trust the end of a name. It looks inside the file."),
 ]),
 ('cpmv', [
  c('c1', "Copy with: cp shopping.txt backup.txt. Source first, then destination.", "Copy with: C P, shopping dot text, backup dot text. Source first, then destination."),
  c('c2', "Move it into a folder. Type: mv backup.txt docs/. A move takes it out of here.", "Move it into a folder. Type: M V, backup dot text, docs slash. A move takes it out of here."),
  c('c3', "The same command renames. Type: mv notes.txt ideas.txt. Same folder, new name.", "The same command renames. Type: M V, notes dot text, ideas dot text. Same folder, new name."),
  c('c4', "To copy a whole folder, add dash r, for recursive. Type: cp -r docs docs2.", "To copy a whole folder, add dash r, for recursive. Type: C P, dash r, docs, docs two."),
  c('c5', "See everything. Type: ls -R. Capital R lists every folder underneath.", "See everything. Type: L S, dash capital R. Capital R lists every folder underneath."),
  c('c6', "Now delete, carefully. Type: rm hello.txt.", "Now delete, carefully. Type: R M, hello dot text."),
  c('c7', "No question, and no recycle bin. It is gone. Next, a folder and everything in it. Type: rm -r docs2.", "No question, and no recycle bin. It is gone. Next, a folder and everything in it. Type: R M, dash r, docs two."),
  c('c8', "Check twice before you press Enter on that one. Now confirm with: ls.", "Check twice before you press Enter on that one. Now confirm with: L S."),
 ]),
 ('safety', [
  c('s1', "Four habits keep you safe."),
  c('s2', "One. Run ls first, so you know what the name matches.", "One. Run L S first, so you know what the name matches."),
  c('s3', "Two. Never use a star with rm until you have run ls with the same star."),
  c('s4', "Three. When unsure, use rm dash i. It asks before every delete.", "Three. When unsure, use R M, dash i. It asks before every delete."),
  c('s5', "Four. There is no undo. A backup is your undo."),
  c('s6', "Look twice. Delete once."),
 ]),
 ('search', [
  c('f1', "Lost a file? Use find. Type: find ~ -name \"*.conf\". The tilde means search my whole home folder.",
    "Lost a file? Use find. Type: find, tilde, dash name, quote, star, dot conf, quote. The tilde means search my whole home folder."),
  c('f2', "One match, deep inside the project. The star means anything, so star dot conf is every name ending in dot conf."),
  c('f3', "To find folders only, type: find ~ -type d -name config.", "To find folders only, type: find, tilde, dash type, d, dash name, config."),
  c('f4', "Type d means directory. The next lesson adds more filters, and grep, to search inside files."),
 ]),
 ('vimmap', [
  c('m1', "Vim is on almost every server, so learn its three modes."),
  c('m2', "Normal mode. Keys are commands. You always start here."),
  c('m3', "Insert mode. Keys are text. Press i to enter, and Escape to leave."),
  c('m4', "Command mode. Type a colon. Colon w saves. Colon q quits. Colon q bang quits without saving.", "Command mode. Type a colon. Colon w saves. Colon q quits. Colon q, bang, quits without saving."),
  c('m5', "Lost? Press Escape twice. You are back in normal mode."),
 ]),
 ('vim', [
  c('v1', "Open a new file. Type: vim todo.txt.", "Open a new file. Type: vim, todo dot text."),
  c('v2', "A blank file. Vim starts in normal mode, where keys are commands, so do not type text yet."),
  c('v3', "Press i for insert mode. Watch the bottom of the screen. It now says insert."),
  c('v4', "Now type three lines, for my to do list."),
  c('v5', "Press Escape. Back to normal mode. The word insert is gone."),
  c('v6', "Delete a line with d d. Two d's, in normal mode."),
  c('v7', "Oops. Press u to undo. The line comes back."),
  c('v8', "Search with a slash. Slash, eggs, Enter. The cursor jumps to the match."),
  c('v9', "Save and quit with colon, w, q, then Enter.", "Save and quit with colon, w, q, then Enter."),
  c('v10', "Prove it saved. Type: cat todo.txt.", "Prove it saved. Type: cat, todo dot text."),
  c('v11', "Now the escape hatch. Open the file, delete a line, then colon, q, bang, to quit without saving."),
  c('v12', "Check it. Type: cat todo.txt again.", "Check it. Type: cat, todo dot text, again."),
  c('v13', "All three lines are still there. Your change was thrown away, on purpose."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: you need an editor to make a file. Touch does it in one command."),
  c('my3', "Myth two: rm sends files to a trash. No. It deletes for good."),
  c('my4', "Myth three: vim is broken, because you cannot type. It is in normal mode. Press i."),
  c('my5', "Myth four: cp copies folders on its own. A folder needs dash r.", "Myth four: C P copies folders on its own. A folder needs dash r."),
  c('my6', "Know the mode. Know the flag."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Create folders and files."),
  c('b3', "Read a file with cat, head, tail and W C."), c('b4', "Copy, move and rename."),
  c('b5', "Delete only after looking."), c('b6', "Find a file by name."),
  c('b7', "Edit and save with vim, and quit without saving."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. Work only inside a practice folder, so nothing important is at risk."),
  c('z2', "One: build practice, slash a, slash b, slash c, with a single command."),
  c('z3', "Two: create three files, and list them with their sizes."),
  c('z4', "Three: copy slash etc slash hostname into your folder, then read it with cat, W C and file."),
  c('z5', "Four: rename one file, move another, and copy a folder with dash r."),
  c('z6', "Five: find your dot text files with find, then delete one, only after you have listed it."),
  c('z7', "Six: in vim, write three lines, undo a change, save, then reopen the file, delete a line, and quit without saving."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which flag makes missing parent folders?"), c('f13', "Which flag copies a folder?"),
  c('f14', "Which key starts insert mode in vim?"), c('f15', "How do you quit vim without saving?"),
  c('f16', "Objective covered: MC04-O02.", "Objective covered: M C zero four, objective two, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: pipes, redirects, grep and find."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'k5': 0.5, 'i7': 0.5, 'c8': 0.5, 's6': 0.5, 'f4': 0.5, 'm5': 0.5, 'v4': 2.5, 'v6': 0.5, 'v8': 1.0, 'v13': 0.5, 'v11': 2.0, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'make': 'Make folders and files', 'inspect': 'Read a file', 'cpmv': 'Copy, move, rename, delete', 'safety': 'Delete safely', 'search': 'Find a file', 'vimmap': 'The three vim modes',
        'vim': 'Edit with vim', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def s_hook(C, D, dur):
    E = [El(T('A server is made of files.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Configs', 'settings as text', ACC), ('Logs', 'what happened', VIO), ('Scripts and data', 'what it runs on', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('Make. Read. Move. Edit. Safely.', 850, C['h3'], GOOD, 1600)); return E
s_make = _lab('Make folders and files', 'mkdir and touch.', 'k1', RB, [('k1', 'mkdir -p', 'Parents in one go', ACC), ('k2', 'cd lab27', 'Step inside', VIO), ('k3', 'touch', 'Make empty files', WARN), ('k4', 'ls -l', 'Check the sizes', PINK)])
s_inspect = _lab('Read a file', 'Four ways to look inside.', 'i1', RB, [('i1', 'cp ~/… .', 'Copy it here', ACC), ('i2', 'cat', 'Print it all', VIO), ('i3', 'head -n 3', 'The first lines', WARN), ('i4', 'tail -n 2', 'The last lines', PINK), ('i5', 'wc -l', 'Count lines', GOOD), ('i6', 'file', 'What kind is it?', BAD)])
s_cpmv = _lab('Copy, move, rename, delete', 'Source first, then destination.', 'c1', RB, [('c1', 'cp a b', 'Copy a file', ACC), ('c2', 'mv a docs/', 'Move it', VIO), ('c3', 'mv old new', 'Rename it', WARN), ('c4', 'cp -r', 'Copy a folder', PINK), ('c6', 'rm', 'Delete. No undo', BAD), ('c7', 'rm -r', 'Folder and contents', BAD)])
def s_safety(C, D, dur):
    E = head('Delete safely', 'There is no recycle bin.', C['s1'])
    it = [('1  ls first', 'Know what the name matches', ACC, 's2'), ('2  No blind stars', 'Run ls with the same star', VIO, 's3'), ('3  rm -i', 'Asks before each delete', WARN, 's4'), ('4  Backups', 'A backup is your undo', GOOD, 's5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 170, col, a, [(b, TXT)], 48, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 200, C[cid]))
    E.append(takeaway('Look twice. Delete once.', 800, C['s6'], GOOD, 1600)); return E
s_search = _lab('Find a file', 'find by name and by type.', 'f1', RB, [('f1', 'find ~ -name', 'Search by name', ACC), ('f2', '*.conf', 'Star means anything', VIO), ('f3', '-type d', 'Folders only', WARN)])
def s_vimmap(C, D, dur):
    E = head('The three vim modes', 'Know which mode you are in.', C['m1'])
    it = [('Normal', 'Keys are commands', ACC, 'm2'), ('Insert', 'Keys are text  ·  i in, Esc out', VIO, 'm3'), ('Command', 'Colon: :w  :q  :q!', WARN, 'm4')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, a, [(b, TXT)], 48, 30, True), 100 + i * 590, 340, C[cid]))
    E.append(Pop(card(1700, 130, GOOD, 'Lost? Press Escape twice.', [('You are back in normal mode.', TXT)], 44, 32), 100, 630, C['m5'])); return E
s_vim = _lab('Edit with vim', 'Normal, insert, command.', 'v1', RB, [('v1', 'vim todo.txt', 'Open the file', ACC), ('v3', 'i', 'Insert mode', VIO), ('v5', 'Esc', 'Back to normal', WARN), ('v6', 'dd   u', 'Delete, undo', PINK), ('v8', '/eggs', 'Search', ACC), ('v9', ':wq   :q!', 'Save, or discard', GOOD)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: need an editor', 'touch makes a file in one command.', 'my2'), ('Myth: rm uses a trash', 'It deletes for good.', 'my3'), ('Myth: vim is broken', 'It is in normal mode. Press i.', 'my4'), ('Myth: cp copies folders', 'A folder needs dash r.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Know the mode. Know the flag.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Create folders and files', 'b2'), ('Read: cat, head, tail, wc', 'b3'), ('Copy, move and rename', 'b4'), ('Delete only after looking', 'b5'), ('Find a file by name', 'b6'), ('Edit and save in vim, :q!', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine. Practice folder only.', C['z1'])
    it = [('1  Build', 'mkdir -p a/b/c', PINK, 'z2'), ('2  Create', 'three files, ls -l', ACC, 'z3'), ('3  Read', 'cat, wc -l, file', WARN, 'z4'), ('4  Move', 'rename, move, cp -r', VIO, 'z5'), ('5  Find', 'find, then rm one', GOOD, 'z6'), ('6  Vim', 'save, then :q!', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which flag makes missing parent folders?', 'f12'), ('Which flag copies a folder?', 'f13'), ('Which key starts insert mode in vim?', 'f14'), ('How do you quit vim without saving?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O02', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: pipes, redirects, grep and find', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, make=s_make, inspect=s_inspect, cpmv=s_cpmv, safety=s_safety, search=s_search, vimmap=s_vimmap, vim=s_vim, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(make=('eye', GOOD), inspect=('eye', GOOD), cpmv=('eye', GOOD), safety=('question', BAD), search=('eye', GOOD), vimmap=('steps', ACC), vim=('eye', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'inspect': [('i6', 1, 1, 4, 200, ''), ('i7', 1, 1, 4, 420, '')],
 'search': [('f2', 1, 1, 4, 620, '')],
}
