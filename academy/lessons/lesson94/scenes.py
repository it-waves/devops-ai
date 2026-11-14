def s_hook(C, D, dur):
    E = [El(T('Red text. Broken build.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(700, 140, BAD, 'BUILD FAILURE', [('forty lines of red', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(700, 140, ACC, 'read it in 10 seconds', [('first ERROR line only', TXT)], 46, 30), 100, 480, C['h3']))
    E.append(Pop(card(760, 180, WARN, '4 real failures', [('404 · offline · tests · 401', TXT)], 52, 38), 900, 440, C['h4']))
    E.append(Pop(card(1100, 140, VIO, 'real Maven Central  +  real Nexus', [('then you fix them yourself', TXT)], 46, 30), 100, 660, C['h5']))
    E.append(takeaway('Read the cause. Fix the cause. Never hide it.', 900, C['h6'], GOOD, 1700)); return E
def s_hook(C, D, dur):
    E = [El(T('Maven mastery. One real job.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(760, 140, BAD, 'cart-core is broken', [('compile · test · jar changes', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(760, 140, ACC, 'ship it to Nexus', [('real login, real repository', TXT)], 46, 30), 100, 480, C['h3']))
    E.append(Pop(card(760, 180, WARN, '3 planted problems', [('version · test · timestamp', TXT)], 52, 38), 900, 440, C['h4']))
    E.append(Pop(card(1100, 140, VIO, 'watch me, then do it alone', [('a checker judges you', TXT)], 46, 30), 100, 660, C['h4']))
    E.append(takeaway('Everything you learned in Maven, in one scenario.', 900, C['h5'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f

s_skills = _list('The six skills of Maven mastery', 'One scenario proves them all.', 'a1', [('1  read a failed build', 'name the cause · lesson 92', ACC, 'a2'), ('2  dependency tree', 'find and fix a version · lessons 89, 91', VIO, 'a3'), ('3  lifecycle and tests', 'a test proves the code · lesson 86', GOOD, 'a4'), ('4  reproducible build', 'same input, same jar · lesson 87', WARN, 'a5'), ('5  publish safely', 'Nexus, password outside files · lessons 90, 91', PINK, 'a6'), ('6  document it', 'result, trouble, cleanup', ACC, 'a7')], h=120, gap=125, y0=290)
def s_task(C, D, dur):
    E = head('Your mastery task', 'lab94.sh: one broken project, a real Nexus. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Compile', [('read the first ERROR', TXT), ('fix the cause', TXT)], 'k2', ACC), ('2  Test', [('fix the code', TXT), ('not the test', TXT)], 'k3', WARN), ('3  Reproducible', [('same sha256 twice', TXT), ('output timestamp', TXT)], 'k4', VIO), ('4  Publish', [('deploy to Nexus', TXT), ('password in a variable', TXT)], 'k5', GOOD), ('5  Report', [('result · trouble · cleanup', TXT), ('report.txt', TXT)], 'k6', PINK)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1']); E.append(ill(C['i1'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab94.sh   and   shortcuts94.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab94.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts94.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, Maven, curl, python3, 3 GB memory, internet', PINK, 'i6'), ('6  Cleanup', 'lab down removes everything. Your own VM only.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Fix the cause each time', 'q3'), ('Test untouched, not skipped', 'q4'), ('Same checksum twice', 'q5'), ('Password in no file', 'q6'), ('report.txt + lab down', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Build', 'each project, first error', ACC, 'z3'), ('3  Name it', 'the cause, in your words', VIO, 'z4'), ('4  Fix', 'fix the cause, rebuild', WARN, 'z5'), ('5  Notes + check', 'report.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which tool shows a library version?', 'f12'), ('Why a reproducible build?', 'f13'), ('Where does the password live?', 'f14'), ('What goes in the report?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Domain mastery: MC10 Maven', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: Gradle', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: ship cart-core, from broken to published', 'Real Maven Central, a real Nexus, one terminal.', 'p0', RB, [('b1', '1  compile error', 'cannot find symbol', BAD), ('d1', '2  dependency tree', 'lang3 3.4 is too old', VIO), ('b2', '3  failing test', 'expected Cloud, was Clou', WARN), ('r1', '4  not reproducible', 'two different checksums', PINK), ('r3', '5  reproducible', 'same checksum twice', GOOD), ('u1', '6  published', 'real Nexus, password in env', ACC)])
FN = dict(hook=s_hook, skills=s_skills, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(skills=('test', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [('b1b', 2, 2, 0, 700, 'CANNOT FIND SYMBOL', 730, 4), ('d1b', 2, 1, 0, 330, 'VERSION 3.4', 360, 3), ('b2b', 1, 1, 0, 450, 'WRONG LENGTH', 480, 2), ('b3b', 2, 2, 0, 690, 'ALL GREEN', 720, 4), ('r1b', 2, 2, 0, 330, 'DIFFERENT', 360, 4), ('r3b', 2, 2, 0, 330, 'SAME', 360, 4), ('u1b', 2, 1, 0, 700, 'UPLOADED', 730, 3), ('u2b', 3, 1, 0, 60, 'ONE JAR', 90, 4), ('u3b', 1, 2, 0, 400, 'ZERO = SAFE', 430, 3)]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson94/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
