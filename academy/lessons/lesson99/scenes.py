def s_hook(C, D, dur):
    E = [El(T('Skip. Restore. Reproduce.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(760, 140, ACC, 'runs in C I', [('hundreds of times a day', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(760, 160, VIO, '3 ideas', [('up-to-date · cache · reproducible', TXT)], 52, 30), 100, 480, C['h3']))
    E.append(Pop(card(760, 160, WARN, 'live on Gradle 8.14.3', [('catch the timestamp', TXT)], 46, 30), 900, 440, C['h4']))
    E.append(Pop(card(1100, 140, GOOD, 'prove the jar is identical', [('then you do it alone', TXT)], 46, 30), 100, 700, C['h5']))
    E.append(takeaway('Same inputs, same outputs: skip.', 900, C['h6'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f

s_parts = _list('Three ideas of a fast build', 'Fast and trustworthy builds have these.', 'a1', [('1  up-to-date', 'same inputs and outputs: skip the task', ACC, 'a2'), ('2  build cache', 'result stored by key: restored after clean', VIO, 'a3'), ('3  reproducible', 'same source, same jar, byte for byte', GOOD, 'a4')], 'A changing input (a timestamp) breaks all three.', 'a5', h=125, gap=145)
def s_task(C, D, dur):
    E = head('Your lab task', 'lab99.sh: a build that never skips. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Cache on', [('org.gradle.caching=true', TXT), ('in gradle.properties', TXT)], 'k2', ACC), ('2  Skip', [('remove the value', TXT), ('that changes each build', TXT)], 'k3', WARN), ('3  Restore', [('clean, then build', TXT), ('compileJava FROM-CACHE', TXT)], 'k4', VIO), ('4  Reproduce', [('same sha256sum', TXT), ('on two clean builds', TXT)], 'k5', GOOD), ('5  Notes', [('3 lines', TXT), ('up-to-date, cache, repro', TXT)], 'k6', PINK)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab99.sh   and   shortcuts99.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab99.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts99.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, curl, python3, 1 GB memory, internet', PINK, 'i6'), ('6  Cleanup', 'lab down removes everything. Your own VM only.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('Build cache switched on', 'q3x'), ('2nd build skips, clean restores', 'q4x'), ('Same jar on two builds', 'q5x'), ('Notes answer 3 questions', 'q6x'), ('lab down, nothing left', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, build twice', PINK, 'z2'), ('2  Cache', 'on, and remove the stamp', ACC, 'z3'), ('3  Restore', 'clean, build, FROM-CACHE', VIO, 'z4'), ('4  Same jar', 'compare two fingerprints', WARN, 'z5'), ('5  Notes', 'three lines, then check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    _unused = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Build', 'each project, first error', ACC, 'z3'), ('3  Name it', 'the cause, in your words', VIO, 'z4'), ('4  Fix', 'fix the cause, rebuild', WARN, 'z5'), ('5  Notes + check', 'report.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What makes a task UP-TO-DATE?', 'f12'), ('FROM-CACHE: does it survive clean?', 'f13'), ('Why does a timestamp break a repro build?', 'f14'), ('Which 2 jar settings fix it?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC11-O05 Gradle', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: Gradle in CI', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: skip work, restore from cache, same jar twice', 'A real Gradle 8.14.3 build on a small CloudCart project.', 'p0', RB, [('b1', '1  first build', 'every task runs', ACC), ('b2', '2  build again', 'the jar runs again: why?', BAD), ('w2', '3  remove the stamp', 'Built-At out of the manifest', WARN), ('w4', '4  UP-TO-DATE', 'nothing executes', GOOD), ('c2', '5  cache on', 'clean, build, store', VIO), ('c3', '6  FROM-CACHE', 'restored after clean', PINK), ('r1', '7  same jar', 'no timestamps, fixed order', GOOD)])
FN = dict(hook=s_hook, parts=s_parts, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(parts=('board', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [('b1b', 7, 1, 0, 470, 'EVERY TASK RAN', 500, 7), ('b2b', 4, 1, 0, 175, 'THE JAR RAN AGAIN', 205, 4), ('w1b', 1, 1, 345, 505, 'THE STAMP', 535, 1), ('w3b', 4, 1, 0, 175, 'RAN ONCE', 205, 4), ('w4b', 7, 1, 0, 505, 'NOTHING EXECUTED', 535, 7), ('c2b', 2, 1, 0, 300, 'COMPILED, THEN STORED', 330, 2), ('c3b', 2, 1, 0, 470, 'RESTORED, NOT COMPILED', 500, 2), ('h1b', 1, 1, 0, 190, 'FINGERPRINT A', 220, 1), ('h3b', 1, 1, 0, 190, 'A DIFFERENT JAR', 220, 1), ('r1tb', 2, 2, 0, 520, 'NO TIMES, FIXED ORDER', 550, 2), ('r5b', 1, 1, 0, 190, 'THE SAME JAR', 220, 1)]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson99/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
