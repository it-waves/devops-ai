import sys, re; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 11  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps
MONO = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 28)
_SP = {'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'mkdir': 'make dir', 'etc': 'E T C', 'tmp': 'temp'}
def _say(cap):
    s = re.sub(r'\b(' + '|'.join(_SP) + r')\b', lambda m: _SP[m.group(1)], cap)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "You open a terminal, and see a blinking cursor."), c('h2', "No icons. No buttons. Only a prompt."),
  c('h3', "Most servers have no screen at all, so this is how you work."),
  c('h4', "Today you learn to move around: the shell, the filesystem tree, paths, and a handful of commands."),
 ]),
 ('shell', [
  c('s1', "First, the terminal and the shell."), c('s2', "The terminal is the window. The shell is the program inside it."),
  c('s3', "The shell reads what you type."), c('s4', "You type a command, press enter, and the shell runs it."),
  c('s5', "On most Linux servers, the shell is called bash."),
 ]),
 ('tree', [
  c('t1', "Next, the filesystem."), c('t2', "Linux organizes everything as one tree of folders."),
  c('t3', "At the top is the root, written as a single slash."), c('t4', "Inside it are folders such as home, etc, var, and tmp."),
  c('t5', "Every file has exactly one place in this tree."),
 ]),
 ('paths', [
  c('p1', "Now, paths."), c('p2', "A path is the address of a file in the tree."),
  c('p3', "An absolute path starts at the root, with a slash. It works from anywhere."),
  c('p4', "A relative path starts from where you are now."),
  c('p5', "Two dots mean the parent folder. One dot means this folder."), c('p6', "A tilde means your home folder."),
 ]),
 ('nav', [
  c('n1', "Three commands do most of the navigating."), c('n2', "pwd prints where you are."), c('n3', "ls lists what is here."),
  c('n4', "cd takes you somewhere else."), c('n5', "Where am I, what is here, and take me there."),
 ]),
 ('files', [
  c('f1', "Four more commands change things."), c('f2', "mkdir creates a folder."), c('f3', "touch creates an empty file."),
  c('f4', "cp copies, and mv moves or renames."), c('f5', "rm removes, and there is no recycle bin."), c('f6', "Check twice before you remove."),
 ]),
 ('options', [
  c('o1', "Commands take options, written with a dash."), c('o2', "ls dash l gives a long listing, with sizes and dates.", "L S dash L gives a long listing, with sizes and dates."),
  c('o3', "ls dash a also shows hidden files, whose names start with a dot.", "L S dash A also shows hidden files, whose names start with a dot."),
  c('o4', "When you forget, the man command shows the manual."),
 ]),
 ('demo', [
  c('e1', "Now let us see this for real, in a disposable Linux sandbox."), c('e2', "These outputs are real captures, not an illustration."),
  c('e3', "First: pwd shows where we are, and ls shows three items."),
  c('e4', "Next, cd projects slash app goes down two levels, using a relative path."),
  c('e5', "Then cd dot dot, dot dot, slash logs goes up two levels and into logs.", "Then C D dot dot slash dot dot slash logs goes up two levels and into logs."),
  c('e6', "Last, a wrong path. The shell says: no such file or directory, and the exit status is two."),
  c('e7', "A clear error message, and a number you can check."),
 ]),
 ('symptoms', [
  c('k1', "Three errors you will meet on day one."), c('k2', "No such file or directory: the path is wrong, or you are in a different folder."),
  c('k3', "Permission denied: you are not allowed, so check who you are, and who owns the file."),
  c('k4', "Command not found: a typo, or the program is not installed."), c('k5', "First run pwd, then read the message slowly."),
 ]),
 ('myths', [
  c('w1', "Watch out for four common myths."),
  c('w2', "Myth one: the terminal and the shell are the same. In fact, the terminal is the window, and the shell runs the commands."),
  c('w3', "Myth two: cd moves a file. In fact, cd changes your location, and nothing else."),
  c('w4', "Myth three: a leading slash does not matter. In fact, it turns a relative path into an absolute one."),
  c('w5', "Myth four: rm sends files to a recycle bin. In fact, they are gone."), c('w6', "Read before you press enter."),
 ]),
 ('rubric', [
  c('u1', "Here is how you check your own understanding."), c('u2', "Imagine a teammate is lost in a terminal."),
  c('u3', "Explain the terminal and the shell."), c('u4', "Describe the tree, and the root."), c('u5', "Explain absolute and relative paths, with one example each."),
  c('u6', "Use pwd, ls, and cd to move around."), c('u7', "Create a folder and a file."), c('u8', "Read a no such file error, and fix it."),
  c('u9', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('y1', "Your turn."), c('y2', "Open a terminal on Linux or Mac, or use a Linux sandbox."),
  c('y3', "One: run pwd, then ls, and note where you are."), c('y4', "Two: make a folder called practice, go inside, and create a file."),
  c('y5', "Three: return to your home folder using a relative path, then using an absolute path."), c('y6', "Mark yourself on the rubric."), c('y7', "Pause the video, and do it now."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "What is the difference between the terminal and the shell?"), c('z3', "What is the difference between an absolute and a relative path?"),
  c('z4', "Which three commands do most of the navigating?"), c('z8', "What does a no such file error usually mean?"),
  c('z9', "Objective covered: MC02-O03.", "Objective covered: number three, in the I T fundamentals masterclass."),
  c('z5', "Pause the video, and describe where you are in the tree."), c('z6', "Next lesson: virtualization and containers."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h4': 0.5, 's5': 0.5, 't5': 0.5, 'p6': 0.5, 'n5': 0.5, 'f6': 0.5, 'o4': 0.5, 'e7': 0.5, 'k5': 0.5, 'w6': 0.5, 'u9': 0.5, 'y7': 12.0, 'z5': 10.0}
CHAP = {'shell': 'Terminal and shell', 'tree': 'The filesystem tree', 'paths': 'Absolute and relative paths', 'nav': 'pwd, ls, cd', 'files': 'Making and removing', 'options': 'Options and help', 'demo': 'Real demo',
        'symptoms': 'Common errors', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Fundamentals  ·  Lesson 11', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def defn(E, t, col, text, y=330): E.append(Pop(card(1720, 130, col, 'Definition', [(text, TXT)], 36, 38), 100, y, t))
def trio(E, C, items, ids, y=520, h=230, w=540):
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def photo(path, w, h, col):
    im = Image.open(path).convert('RGB'); im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.5))
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=tuple(col)[:3] + (255,))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=20, fill=255)
    out.paste(im, (6, 6), m); return out
PHOTO = '/home/claude/academy/lesson11/assets/photo_l11_laptop_code.jpg'

def s_hook(C, D, dur):
    E = [El(T('Lost in the terminal?', 'x', 64), 100, 130, C['h1'])]
    E.append(Pop(photo(PHOTO, 740, 500, ACC), 1080, 250, C['h1']))
    E.append(El(T('Photo: Negative Space  ·  CC0  ·  via Wikimedia Commons', 'm', 24, MUTED, maxw=700), 1080, 770, C['h1'] + 0.5, anim='fade'))
    E.append(Pop(card(900, 190, WARN, 'A blinking cursor', [('No icons. No buttons.', TXT)], 50, 36), 100, 250, C['h1']))
    E.append(Pop(card(900, 190, ACC, 'Servers have no screen', [('This is how you work on them.', TXT)], 50, 36), 100, 480, C['h3']))
    bs = [badge(n, F('b', 34), INK, col, padx=26, pady=14, r=26) for n, col in [('Shell', ACC), ('The tree', GOOD), ('Paths', WARN), ('Commands', VIO)]]
    E.append(El(T('Today', 'b', 32, MUTED), 100, 740, C['h4'], anim='fade'))
    bx = 100
    for i, b in enumerate(bs): E.append(Pop(b, bx, 800, C['h4'] + 0.3 + i * 0.6)); bx += b.width + 30
    E.append(takeaway('Move around with confidence.', 930, C['h4'] + 1.2, GOOD, 1600)); return E
def s_shell(C, D, dur):
    E = head('Terminal and shell', 'A window, and the program in it.', C['s1']); defn(E, C['s2'], ACC, 'Terminal: the window.  Shell: the program that runs your commands.')
    trio(E, C, [('The shell', 'Reads what you type', ACC, ), ('A command', 'Type it, press enter', GOOD), ('bash', 'The usual Linux shell', WARN)], ['s3', 's4', 's5'])
    E.append(takeaway('Type, enter, result.', 860, C['s5'] + 0.4, GOOD, 1600)); return E
def s_tree(C, D, dur):
    E = head('The filesystem tree', 'One tree, one root.', C['t1'])
    E.append(Pop(card(600, 110, ACC, 'Root  /', [], 50), 660, 330, C['t3']))
    names = [('home', 'People', GOOD), ('etc', 'Settings', WARN), ('var', 'Logs and data', VIO), ('tmp', 'Temporary files', PINK)]
    for i, (n, s, col) in enumerate(names):
        x = 100 + i * 440; E.append(Pop(card(400, 170, col, n, [(s, TXT)], 44, 32), x, 560, C['t4'] + i * 0.4))
        E.append(A([(960, 445), (x + 200, 545)], C['t4'] + i * 0.4, MUTED, 6, 22))
    E.append(takeaway('Every file has exactly one place.', 840, C['t5'], GOOD, 1600)); return E
def s_paths(C, D, dur):
    E = head('Paths', 'The address of a file.', C['p1'])
    E.append(Pop(card(840, 190, ACC, 'Absolute', [('Starts at the root: /home/user/notes.txt', TXT)], 44, 32), 100, 330, C['p3']))
    E.append(Pop(card(840, 190, GOOD, 'Relative', [('Starts from here: projects/app/main.py', TXT)], 44, 32), 980, 330, C['p4']))
    items = [('..  two dots', 'Parent folder', WARN, 'p5'), ('.  one dot', 'This folder', VIO, 'p5'), ('~  tilde', 'Your home folder', PINK, 'p6')]
    for i, (n, s, col, cid) in enumerate(items): E.append(Pop(card(540, 190, col, n, [(s, TXT)], 44, 34), 100 + i * 590, 590, C[cid] + (0.6 if i == 1 else 0)))
    E.append(takeaway('Slash first: absolute. Otherwise: relative.', 860, C['p6'] + 0.4, GOOD, 1700)); return E
def s_nav(C, D, dur):
    E = head('Moving around', 'Three commands.', C['n1'])
    trio(E, C, [('pwd  print', 'Where am I?', ACC), ('ls  list', 'What is here?', GOOD), ('cd  change', 'Take me there', WARN)], ['n2', 'n3', 'n4'], y=400, h=300)
    E.append(takeaway('Where, what, go.', 820, C['n5'], GOOD, 1600)); return E
def s_files(C, D, dur):
    E = head('Changing things', 'Make, copy, move, remove.', C['f1'])
    it = [('mkdir', 'Create a folder', ACC, 'f2'), ('touch', 'Create an empty file', GOOD, 'f3'), ('cp  mv', 'Copy, or move and rename', WARN, 'f4'), ('rm', 'Remove. No recycle bin', BAD, 'f5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(400, 300, col, n, [(s, TXT)], 46, 32), 100 + i * 440, 400, C[cid]))
    E.append(takeaway('Check twice before you remove.', 820, C['f6'], WARN, 1600)); return E
def s_options(C, D, dur):
    E = head('Options and help', 'Dashes change what a command does.', C['o1'])
    trio(E, C, [('ls -l', 'Long listing: sizes and dates', ACC), ('ls -a', 'Also show hidden files', GOOD), ('man ls', 'Read the manual', WARN)], ['o2', 'o3', 'o4'], y=400, h=300)
    E.append(takeaway('Forgot an option? Ask the manual.', 820, C['o4'] + 0.4, GOOD, 1600)); return E
def mono(s, col):
    im = Image.new('RGBA', (int(MONO.getlength(s)) + 10, 44), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), s, font=MONO, fill=tuple(col)[:3] + (255,)); return im
def s_demo(C, D, dur):
    E = head('Real demo', 'pwd, ls, cd, and an error.', C['e1']); E.append(real(C['e2'], 'REAL OUTPUT  ·  captured in a Linux sandbox', 1260, 296))
    E.append(Pop(card(1100, 640, ACC, '', [], 4), 100, 330, C['e1'] + 0.3))
    blocks = [('e3', [('$ pwd', ACC), ('/tmp/home11', TXT), ('$ ls', ACC), ('logs', TXT), ('notes.txt', TXT), ('projects', TXT)]),
              ('e4', [('$ cd projects/app', ACC), ('$ pwd', ACC), ('/tmp/home11/projects/app', GOOD)]),
              ('e5', [('$ cd ../../logs', ACC), ('$ pwd', ACC), ('/tmp/home11/logs', GOOD)]),
              ('e6', [('$ ls /nonexistent', ACC), ("ls: cannot access '/nonexistent': No such file or directory", WARN)])]
    y = 365; ys = []
    for cid, lines in blocks:
        ys.append(y)
        for j, (s, col) in enumerate(lines): E.append(El(mono(s, col), 130, y + j * 36, C[cid] + j * 0.4, anim='fade'))
        y += len(lines) * 36 + 20
    ann = [('Where and what', 'a folder with three items', ACC, 'e3', ys[0]), ('Down', 'relative path, two levels', GOOD, 'e4', ys[1]), ('Up', 'two dots, twice, then logs', VIO, 'e5', ys[2]), ('Error', 'wrong path, exit status 2', WARN, 'e6', ys[3])]
    for n, s, col, cid, yy in ann: E.append(Pop(card(560, 100, col, '', [(n + ': ' + s, TXT)], 4, 26), 1260, yy, C[cid]))
    return E
def s_symptoms(C, D, dur):
    E = head('Common errors', 'Three messages, three meanings.', C['k1'])
    it = [('No such file or directory', 'Wrong path, or wrong folder', WARN, 'k2'), ('Permission denied', 'Not allowed: check who owns it', BAD, 'k3'), ('Command not found', 'A typo, or not installed', VIO, 'k4'), ('The habit', 'Run pwd, then read slowly', GOOD, 'k5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s, TXT)], 40, 30), 100 + (i % 2) * 880, 330 + (i // 2) * 220, C[cid]))
    E.append(takeaway('The message tells you what is wrong.', 860, C['k5'] + 0.4, GOOD, 1500)); return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['w1'])
    it = [('Myth: terminal and shell are the same', 'Reality: a window, and the program in it.', WARN, 'w2'), ('Myth: cd moves a file', 'Reality: it changes where you are.', BAD, 'w3'),
          ('Myth: a leading slash does not matter', 'Reality: it makes the path absolute.', VIO, 'w4'), ('Myth: rm uses a recycle bin', 'Reality: removed means gone.', GOOD, 'w5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Read before you press enter.', 860, C['w6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['u1'])
    items = [('Explains terminal and shell', 'u3'), ('Describes the tree and root', 'u4'), ('Absolute and relative, with examples', 'u5'), ('Moves around the tree', 'u6'), ('Creates a folder and a file', 'u7'), ('Reads and fixes a path error', 'u8')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid] + (i % 2) * 0.5))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + (i % 2) * 0.5 + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['u9'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Move around a real computer.', C['y1'])
    E.append(Pop(card(1720, 150, WARN, 'Any Linux or Mac terminal, or a Linux sandbox', [('Do it yourself: do not just watch.', TXT)], 46, 36), 100, 330, C['y2']))
    it = [('1  Look', 'Print where you are, then list', ACC, 'y3'), ('2  Make', 'A folder, then a file in it', VIO, 'y4'), ('3  Return', 'Home, relative then absolute', GOOD, 'y5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 270, col, n, [(s, TXT)], 44, 32, True), 100 + i * 590, 540, C[cid]))
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['y7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    qs = [('What is the difference between the terminal and the shell?', 'z2'), ('What is the difference between an absolute and a relative path?', 'z3'), ('Which three commands do most of the navigating?', 'z4'), ('What does a no such file error usually mean?', 'z8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['z9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC02-O03  ·  command line, filesystem', 'b', 30, TXT, maxw=960), 220, 748, C['z9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  say where you are', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['z5']))
    E.append(El(T('Next: virtualization and containers', 'x', 46, ACC, maxw=1500), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['z7']))
    return E
FN = dict(hook=s_hook, shell=s_shell, tree=s_tree, paths=s_paths, nav=s_nav, files=s_files, options=s_options, demo=s_demo, symptoms=s_symptoms, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(shell=('screen', ACC), tree=('branch', GOOD), paths=('link', WARN), nav=('steps', VIO), files=('doc', PINK), options=('gear', ACC), demo=('eye', GOOD), symptoms=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
