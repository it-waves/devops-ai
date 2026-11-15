def s_hook(C, D, dur):
    E = [El(T('Build CloudCart', 'x', 66), 100, 130, C['h1'])]
    E.append(Pop(card(900, 150, ACC, 'one command', [('source code in, web app out', TXT)], 52, 32), 100, 320, C['h1'] + 1.0))
    E.append(Pop(card(900, 150, VIO, 'lesson two of five', [('layout and the Maven build', TXT)], 52, 32), 100, 500, C['h2']))
    for i, (n, s_, col) in enumerate([('you read the project', 'folders and pom.xml', ACC), ('you run the build', 'test, then package', WARN), ('you open the WAR', 'without Tomcat', GOOD), ('four answers', 'checked by one command', PINK)]):
        E.append(Pop(card(740, 120, col, n, [(s_, TXT)], 40, 28), 1060, 320 + i * 140, C['h3'] + i * 0.9))
    E.append(Pop(card(900, 140, GOOD, 'last time: use it', [('today: make it', TXT)], 46, 30), 100, 700, C['h4']))
    E.append(takeaway('Look, read, build, open.', 900, C['h4'], GOOD, 1700)); return E
def s_plan(C, D, dur):
    E = head('What to expect', 'From the first minute to the last.', C['a1']); E.append(ill(C['a1'] + 0.2, 1400, 170))
    st = [('1  Look', 'folders, and what lives in each', ACC, 'a2'), ('2  Read', 'pom.xml, the one recipe', VIO, 'a3'), ('3  Build', 'test, then package', WARN, 'a4'), ('4  Open', 'inside the WAR', GOOD, 'a5'), ('5  Your turn', 'bump the version, a lab checks', PINK, 'a6')]
    for i, (n, sb, col, cid) in enumerate(st): E.append(Pop(card(330, 280, col, n, [(sb, TXT)], 38, 24), 100 + i * 350, 330, C[cid]))
    rm = [('L113  Meet it', MUTED), ('L114  Build it', VIO), ('L115  Deploy it', WARN), ('L116  Run it, fix it', GOOD), ('L117  Prove it', PINK)]
    for i, (n, col) in enumerate(rm): E.append(Pop(card(330, 110, col, n, [], 30), 100 + i * 345, 690, C['a7'] + i * 0.8))
    E.append(takeaway('Look, read, build, open.', 880, C['a8'], GOOD, 1700)); return E
def s_maven(C, D, dur):
    E = head('What is Maven?', 'Pom, Central, life cycle.', C['m1']); E.append(ill(C['m1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 215, VIO, 'pom.xml', [('the one file that', TXT), ('describes the project', TXT)], 44, 30, True), 100, 330, C['m2']))
    E.append(Pop(card(540, 215, WARN, 'Maven Central', [('free public store', TXT), ('of libraries', TXT)], 44, 30, True), 690, 330, C['m3']))
    E.append(Pop(card(540, 215, ACC, 'life cycle', [('fixed steps,', TXT), ('in a fixed order', TXT)], 44, 30, True), 1280, 330, C['m4']))
    steps = [('compile', ACC), ('test', WARN), ('package', GOOD)]
    for i, (n, col) in enumerate(steps):
        E.append(Pop(card(400, 130, col, n, [], 46), 100 + i * 520, 640, C['m4'] + 0.6 + i * 0.5))
        if i: E.append(El(T('>', 'x', 90, ACC), 100 + i * 520 - 100, 660, C['m4'] + 0.9 + i * 0.5))
    E.append(Pop(badge('a failed step stops the build', F('b', 36), INK, BAD, padx=28, pady=14), 100, 830, C['m5']))
    E.append(takeaway('pom  +  Central  +  life cycle', 920, C['m6'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab114.sh: build the WAR. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Start', [('lab up,', TXT), ('real source', TXT)], 'k2', ACC), ('2  Build', [('mvn package,', TXT), ('read the summary', TXT)], 'k3', WARN), ('3  Bump', [('vim pom.xml,', TXT), ('version 0.2.1', TXT)], 'k4', VIO), ('4  Open', [('unzip the WAR,', TXT), ('answers.txt, 4 lines', TXT)], 'k5', PINK), ('5  Check', [('lab check,', TXT), ('five of five, lab down', TXT)], 'k6', GOOD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab114.sh   and   shortcuts114.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab114.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts114.sh  then: lab', WARN, 'i5'), ('5  You need', 'JDK, Maven, curl, unzip, 1 GB RAM, internet', PINK, 'i6'), ('6  Rules', 'lab check judges you.  lab down removes it all.', BAD, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Five points. All five to pass.', C['q1x'])
    items = [('WAR exists, valid zip', 'q2x'), ('pom + WAR say 0.2.1', 'q3x'), ('tests: your count is right', 'q4x'), ('lib + provided are right', 'q5x'), ('built: from inside the WAR', 'q6x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all five', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own machine only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read tasks', PINK, 'z2'), ('2  Build', 'look, then mvn package', ACC, 'z3'), ('3  Bump', 'vim pom.xml, 0.2.1', WARN, 'z4'), ('4  Answers', 'open the WAR, 4 lines', VIO, 'z5'), ('5  Check', 'lab check, 5 of 5', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which file tells Maven everything?', 'f12'), ('Why is the servlet API not in the WAR?', 'f13'), ('What did the test step stop before?', 'f14'), ('Where did the build time come from?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('CloudCart v0: layout and the Maven build', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: deploy it to Tomcat', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: read the project, build it, open the WAR', 'Real Maven, real Maven Central, one terminal.', 'p0', RB, [('d2', '1  layout', 'src, pom.xml', ACC), ('x2', '2  pom', 'dependencies and scopes', VIO), ('b1', '3  test', 'life cycle, 32 tests', WARN), ('b3', '4  package', 'the WAR is built', GOOD), ('w1', '5  open', 'inside the WAR', PINK), ('v3', '6  bump', 'version 0.2.1', ACC)])
FN = dict(hook=s_hook, plan=s_plan, maven=s_maven, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(plan=('board', ACC), maven=('board', VIO), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [('b1b', 7, 2, 0, 760, 'TESTS PASS', 780), ('b3b', 3, 2, 0, 1000, 'WAR BUILT', 780, 5), ('b4b', 1, 1, 0, 1020, 'SMALL', 1040), ('w3b', 2, 2, 0, 380, 'FILLED IN', 400), ('w4b', 1, 1, 0, 40, 'NOT IN THE WAR', 60), ('v3b', 2, 2, 0, 380, 'NEW VERSION', 400)]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson114/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
