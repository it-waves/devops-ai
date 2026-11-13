def s_hook(C, D, dur):
    E = [El(T('The release will not ship.', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(900, 330, BAD, 'orders 1.4', [('BUILD FAILED: tests', TXT), ('no main manifest attribute', MUTED)], 44, 34), 100, 300, C['h1'] + 1.0))
    E.append(Pop(card(760, 150, BAD, 'The team sees', [('red tests, a dead jar', TXT)], 40, 30), 1100, 300, C['h1'] + 3.0))
    E.append(Pop(card(760, 150, WARN, 'Manager asks', [('what is wrong, and how do you know?', TXT)], 40, 28), 1100, 480, C['h1'] + 6.0))
    for i, (a, b, col) in enumerate([('A lab', 'four faults, built for you', ACC), ('A checker', 'PASS or FAIL for each', GOOD), ('A report', 'proof of how you thought', WARN)]):
        E.append(Pop(card(540, 140, col, a, [(b, TXT)], 40, 28), 100 + i * 560, 680, C['h2'] + i * 3.0))
    E.append(takeaway('Prove it. Someone else can check it.', 900, C['h3'], GOOD, 1700)); return E
def s_scenario(C, D, dur):
    E = head('The scenario', 'The orders service, released with four faults.', C['sc1']); E.append(ill(C['sc1'] + 0.2, 1400, 170))
    cs = [('Source', 'Orders.java', VIO, 100), ('Build + tests', 'build.sh', ACC, 550), ('Jar', 'orders.jar', GOOD, 1000), ('Run', 'run-orders.sh', WARN, 1450)]
    for i, (a, b, col, x) in enumerate(cs): E.append(Pop(card(380, 190, col, a, [(b, TXT)], 40, 28), x, 360, C['sc1'] + 1.0 + 0.5 * i))
    for i, x in enumerate([485, 935, 1385]): E.append(A([(x, 455), (x + 60, 455)], C['sc1'] + 3.0 + 0.4 * i, ACC, 6, 26))
    pins = [('1  test fails: total', 'sc2', 480, 600), ('2  jar: no main class', 'sc3', 930, 600), ('3  port: "eighty"', 'sc4', 1380, 600), ('4  heap: 8 MB', 'sc5', 1380, 690)]
    for n, cid, x, y in pins: E.append(Pop(badge(n, F('b', 30), INK, BAD, padx=22, pady=12), x, y, C[cid]))
    E.append(Pop(card(740, 110, PINK, 'orders.env', [('port and heap live here', TXT)], 34, 26), 1100, 800, C['sc4'] + 1.0))
    E.append(El(T('Goal: six PASS lines, with proof.', 'x', 44, GOOD, maxw=1500), 100, 990, C['sc7'])); return E
def s_getlab(C, D, dur):
    E = head('Get the lab', 'Everything you need, in one place.', C['g1']); E.append(ill(C['g1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 'g2', ACC), ('Lab files', 'academy/lab/lab84.sh  +  shortcuts84.sh', 'g3', VIO), ('Lesson files', 'academy/lesson84: INSTALL.txt, report_template.md', 'g3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 'g4'), ('cd devops-ai/academy/lab', 'g4'), ('sudo install -m 755 lab84.sh /usr/local/sbin/', 'g4'), ('source shortcuts84.sh      # short name: lab', 'g6'), ('lab up  |  lab check  |  lab down', 'g5')]
    E.append(Pop(glass(1700, 5 * 46 + 48, WARN), 100, 700, C['g4']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, root, a JDK (openjdk-21-jdk-headless). Your own machine only.', 'm', 26, MUTED, maxw=1700), 100, 990, C['g7'], anim='fade')); return E
s_start = _lab('Start the lab', 'Install it, build it, check it.', 'st1', RB, [('st1', 'cd lab', 'The lab folder', ACC), ('st3', 'sudo install', 'Install the script', VIO), ('st4', 'source', 'Short name: lab', WARN), ('st5', 'lab up', 'Build the faults', BAD), ('st6', 'lab check', 'Six FAIL lines', GOOD)])
def s_notes(C, D, dur):
    E = head('Four notes per fault', 'Evidence, not luck.', C['n1'])
    it = [('1  Symptom', 'the exact words', BAD, 'n2'), ('2  Cause', 'and the proving command', ACC, 'n3'), ('3  Fix', 'one change only', WARN, 'n4'), ('4  Proof', 'output after the fix', GOOD, 'n5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s_, TXT)], 44, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Notes turn a lucky fix into evidence.', 800, C['n6'], GOOD, 1700)); return E
s_fix1 = _lab('Fault 1, live', 'A failing test, found by reading the build.', 'f1', RB, [('f2', 'sh build.sh', 'tests: 750, not 1250', BAD), ('f3', 'grep -n SHIPPING', 'minus, not plus', ACC), ('f4', 'sed -i ...', 'one change', WARN), ('f5', 'sh build.sh', 'tests pass, jar built', GOOD), ('f6', 'sh run-orders.sh', 'fails: see the log', BAD), ('f7', 'head -2 logs/...', 'no main manifest: next fault', VIO), ('f8', 'lab check', 'One PASS', GOOD)])
def s_report(C, D, dur):
    E = head('The report', 'Five parts. Template in academy/lesson84.', C['r1']); E.append(ill(C['r1'] + 0.2, 1400, 170))
    it = [('Setup', 'checker output at the start', ACC, 'r2'), ('Each fault', 'its four notes', VIO, 'r3'), ('Final check', 'six PASS lines', GOOD, 'r4'), ('Where I got stuck', 'and what unstuck me', WARN, 'r5'), ('Cleanup proof', 'four proofs', PINK, 'r6')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s_, TXT)], 40, 30, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(Pop(card(1700, 110, PINK, 'Also: report.txt', [('four lines in the lab folder: test, manifest, port, heap', TXT)], 36, 28), 100, 840, C['r7'])); return E
def s_hints(C, D, dur):
    E = head('Your three faults', 'Directions only. No spoilers.', C['y1'])
    it = [('Fault 2: the jar', 'unzip -p the manifest: is there a Main-Class? jar cfe', VIO, 'y2'), ('Fault 3: the settings', 'the log names the bad value: fix it in orders.env', WARN, 'y3'), ('Fault 4: memory', 'Java heap space: raise -Xmx on the JAVA_OPTS line', PINK, 'y4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1500, 150, col, n, [(s_, TXT)], 44, 30), 100, 330 + i * 175, C[cid]))
    E.append(takeaway('Symptom. Cause. Fix one thing. Verify.', 900, C['y5'], GOOD, 1700)); return E
s_cleanup = _lab('Cleanup with proof', 'Nothing left behind.', 'c1', RB, [('c1', 'lab down', 'Remove the lab', ACC), ('c2', 'ls /opt/lab84', 'No folder', VIO), ('c3', 'ls /opt | grep -c', 'Count: 0', WARN), ('c4', 'sudo rm', 'Remove the script', PINK), ('c5', 'ls ... | wc -l', 'Nothing left', GOOD), ('c5b', 'pgrep -c java', 'No Java running', GOOD)])
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Six PASS lines', 'b2'), ('Four notes per fault', 'b3'), ('One change at a time', 'b4'), ('Complete report', 'b5'), ('Cleanup, no Java running', 'b6'), ('Own VM only', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'clone and install the lab', PINK, 'z2'), ('2  Start', 'lab up, save the output', ACC, 'z3'), ('3  Fix', 'three faults, four notes', WARN, 'z4'), ('4  Report', 'report.txt + template', VIO, 'z5'), ('5  Check', 'six PASS lines', BAD, 'z6'), ('6  Clean up', 'and paste the proof', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('No main manifest attribute: what is missing?', 'f12'), ('Why run tests before building the jar?', 'f13'), ('Which option raises the heap limit?', 'f14'), ('What proves cleanup worked?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Mastery evidence: MC09', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next masterclass: Maven', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, scenario=s_scenario, getlab=s_getlab, start=s_start, notes=s_notes, fix1=s_fix1, report=s_report, hints=s_hints, cleanup=s_cleanup, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(scenario=('board', ACC), getlab=('gear', VIO), start=('gear', ACC), notes=('board', WARN), fix1=('test', GOOD), report=('board', VIO), hints=('question', WARN), cleanup=('eye', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'fix1': [('f2b', 1, 2, 0, 1076, 'TESTS FAIL: 750, NOT 1250', 0, 5), ('f3b', 2, 1, 0, 1076, 'MINUS, NOT PLUS', 0, 4), ('f5b', 1, 3, 0, 700, 'TESTS PASS', 0, 5), ('f7b', 1, 1, 0, 1076, 'NEXT FAULT: THE JAR', 0, 3), ('f8b', 1, 1, 0, 1076, 'FIXED', 0, 9)],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson84/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
