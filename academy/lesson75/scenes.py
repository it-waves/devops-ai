def s_hook(C, D, dur):
    E = [El(T('The shop is down.', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(900, 330, MUTED, 'CloudCart', [('Today\'s products', TXT), ('(nothing here)', MUTED)], 44, 34), 100, 300, C['h1'] + 1.0))
    E.append(Pop(card(760, 150, BAD, 'Customer sees', [('an empty page', TXT)], 40, 30), 1100, 300, C['h1'] + 3.0))
    E.append(Pop(card(760, 150, WARN, 'Manager asks', [('which part broke, and how do you know?', TXT)], 40, 28), 1100, 480, C['h1'] + 6.0))
    for i, (a, b, col) in enumerate([('A lab', 'four faults, built for you', ACC), ('A checker', 'PASS or FAIL for each', GOOD), ('A report', 'proof of how you thought', WARN)]):
        E.append(Pop(card(540, 140, col, a, [(b, TXT)], 40, 28), 100 + i * 560, 680 + 0 * i, C['h2'] + i * 3.0))
    E.append(takeaway('Prove it. Someone else can check it.', 900, C['h3'], GOOD, 1700)); return E
def s_scenario(C, D, dur):
    E = head('The scenario', 'CloudCart, released with four faults.', C['sc1']); E.append(ill(C['sc1'] + 0.2, 1400, 170))
    E.append(Pop(card(380, 190, VIO, 'Browser', [('the customer', TXT)], 40, 28), 100, 470, C['sc1'] + 1.0))
    E.append(Pop(card(440, 170, ACC, 'Web service', [('port 8080', TXT)], 40, 28), 620, 350, C['sc1'] + 1.5))
    E.append(Pop(card(440, 170, GOOD, 'API service', [('port 5000', TXT)], 40, 28), 620, 690, C['sc1'] + 2.0))
    E.append(Pop(card(400, 170, WARN, 'Database', [('shop.db', TXT)], 40, 28), 1300, 690, C['sc1'] + 2.5))
    E.append(Pop(card(400, 170, PINK, 'Secrets', [('secrets.env', TXT)], 40, 28), 1300, 350, C['sc1'] + 3.0))
    E.append(A([(485, 540), (615, 450)], C['sc1'] + 3.5, ACC, 6, 26)); E.append(A([(840, 525), (840, 685)], C['sc1'] + 4.0, GOOD, 6, 26)); E.append(A([(1065, 775), (1295, 775)], C['sc1'] + 4.5, WARN, 6, 26)); E.append(A([(1065, 740), (1295, 470)], C['sc1'] + 5.0, PINK, 6, 26))
    pins = [('1  wrong port 5050', 'sc2', 620, 880), ('2  shop.db missing', 'sc3', 1300, 880), ('3  mode 644, not private', 'sc4', 1300, 560), ('4  no traced request', 'sc5', 100, 700)]
    for n, cid, x, y in pins: E.append(Pop(badge(n, F('b', 32), INK, BAD, padx=24, pady=12), x, y, C[cid]))
    E.append(El(T('Goal: four PASS lines, with proof.', 'x', 44, GOOD, maxw=1500), 100, 990, C['sc7'])); return E
def s_getlab(C, D, dur):
    E = head('Get the lab', 'Everything you need, in one place.', C['g1']); E.append(ill(C['g1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 'g2', ACC), ('Lab file', 'academy/lab/lab75.sh', 'g3', VIO), ('Lesson files', 'academy/lesson75: INSTALL.txt, report_template.md', 'g3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 'g4'), ('cd devops-ai/academy/lab', 'g4'), ('sudo install -m 755 lab75.sh /usr/local/sbin/', 'g4'), ('source shortcuts75.sh', 'g6'), ('lab up  |  lab check  |  lab down', 'g5')]
    E.append(Pop(glass(1700, 5 * 46 + 48, WARN), 100, 700, C['g4']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, root, python3, curl. Ports 5000 and 8080. Your own machine only.', 'm', 26, MUTED, maxw=1700), 100, 990, C['g7'], anim='fade')); return E
s_start = _lab('Start the lab', 'Install it, build it, check it.', 'st1', RB, [('st1', 'cd lab', 'The lab folder', ACC), ('st3', 'sudo install', 'Install the script', VIO), ('st4', 'source', 'Short name: lab', WARN), ('st5', 'lab up', 'Build the faults', BAD), ('st6', 'lab check', 'Four FAIL lines', GOOD)])
def s_notes(C, D, dur):
    E = head('Four notes per fault', 'Evidence, not luck.', C['n1'])
    it = [('1  Symptom', 'the exact words', BAD, 'n2'), ('2  Cause', 'and the proving command', ACC, 'n3'), ('3  Fix', 'one change only', WARN, 'n4'), ('4  Proof', 'output after the fix', GOOD, 'n5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s_, TXT)], 44, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Notes turn a lucky fix into evidence.', 800, C['n6'], GOOD, 1700)); return E
s_fix1 = _lab('Fault 1, live', 'A wrong port, found by asking each layer.', 'f1', RB, [('f2', './layers.sh', 'api  000: no answer', BAD), ('f3', 'ss -ltn', '5050, not 5000', ACC), ('f4', 'grep PORT app.conf', 'the config is wrong', WARN), ('f5', 'sed -i ...', 'one change', PINK), ('f6', './start.sh', 'restart the API', VIO), ('f7', './layers.sh', 'api 503: next fault', GOOD), ('f8', 'lab check', 'One PASS', GOOD)])
def s_report(C, D, dur):
    E = head('The report', 'Five parts. Template in academy/lesson75.', C['r1']); E.append(ill(C['r1'] + 0.2, 1400, 170))
    it = [('Setup', 'checker output at the start', ACC, 'r2'), ('Each fault', 'its four notes', VIO, 'r3'), ('Final check', 'four PASS lines', GOOD, 'r4'), ('Where I got stuck', 'and what unstuck me', WARN, 'r5'), ('Cleanup proof', 'four proofs', PINK, 'r6')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s_, TXT)], 40, 30, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    return E
def s_hints(C, D, dur):
    E = head('Your three faults', 'Directions only. No spoilers.', C['y1'])
    it = [('Check 2', 'API up but not ready: which endpoint says why?', VIO, 'y2'), ('Check 3', 'a secrets file must be private: stat, one command', WARN, 'y3'), ('Check 4', 'log in, label the request, search both diaries', PINK, 'y4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1500, 150, col, n, [(s_, TXT)], 44, 30), 100, 330 + i * 175, C[cid]))
    E.append(takeaway('Symptom. Layer. Fix one thing. Verify.', 900, C['y5'], GOOD, 1700)); return E
s_cleanup = _lab('Cleanup with proof', 'Nothing left behind.', 'c1', RB, [('c1', 'lab down', 'Remove the lab', ACC), ('c2', 'ls /opt/lab75', 'No folder', VIO), ('c3', 'ls /opt | grep -c', 'Count: 0', WARN), ('c4', 'sudo rm', 'Remove the script', PINK), ('c5', 'ls ... | wc -l', 'Nothing left', GOOD), ('c5b', 'ss -ltn | grep -c', 'Nothing listening', GOOD)])
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Four PASS lines', 'b2'), ('Four notes per fault', 'b3'), ('One change at a time', 'b4'), ('Complete report', 'b5'), ('Cleanup, nothing listening', 'b6'), ('Own VM only', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'clone and install the lab', PINK, 'z2'), ('2  Start', 'lab up, save the output', ACC, 'z3'), ('3  Fix', 'three faults, four notes', WARN, 'z4'), ('4  Report', 'from the template', VIO, 'z5'), ('5  Check', 'four PASS lines', BAD, 'z6'), ('6  Clean up', 'and paste the proof', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Page loads, no products: which layer?', 'f12'), ('Why can a fix change the symptom?', 'f13'), ('What does one request label let you do?', 'f14'), ('What proves cleanup worked?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Mastery evidence: MC08', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: the next masterclass', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
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
 'fix1': [('f2b', 2, 1, 0, 140, 'NO ANSWER'), ('f3b', 3, 1, 0, 1070, 'WRONG PORT'), ('f4b', 1, 1, 0, 140, 'THE CAUSE'), ('f7b', 2, 1, 0, 140, 'NEXT FAULT'), ('f8b', 1, 1, 0, 800, 'FIXED'), ('f8b', 2, 3, 0, 920, '')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson75/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
