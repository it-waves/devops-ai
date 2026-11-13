def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))


def s_hook(C, D, dur):
    E = [El(T('Mastery evidence: Git', 'x', 72), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('A lab', 'four faults, built for you', ACC), ('A checker', 'PASS or FAIL for each', GOOD), ('A report', 'proof of how you thought', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 3.0))
    E.append(takeaway('Prove it. Someone else can check it.', 850, C['h3'], GOOD, 1700)); return E
def s_scenario(C, D, dur):
    E = head('The scenario', 'A shop repository. Four things are wrong.', C['sc1']); E.append(ill(C['sc1'] + 0.2, 1400, 170))
    it = [('1  Secret in history: remove, ignore', 'sc3', ACC), ('2  Merge feature/discount, fix conflict', 'sc4', VIO), ('3  Team checks fail: fix, gate on', 'sc5', WARN), ('4  Push main, annotated tag v1.0.0', 'sc6', PINK)]
    for i, (n, cid, col) in enumerate(it):
        E.append(Pop(card(1100, 120, col, '', [], 4), 100, 330 + i * 140, C[cid])); E.append(El(T('FAIL', 'mono', 34, BAD, align='left'), 140, 372 + i * 140, C[cid] + 0.2, anim='fade')); E.append(El(T(n, 'b', 36, TXT, maxw=900), 280, 370 + i * 140, C[cid] + 0.3, anim='fade'))
    E.append(takeaway('Goal: four PASS lines, with proof.', 920, C['sc7'], GOOD, 1500)); return E
def s_getlab(C, D, dur):
    E = head('Get the lab', 'Everything you need, in one place.', C['g1']); E.append(ill(C['g1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 'g2', ACC), ('Lab file', 'academy/lab/lab66.sh', 'g3', VIO), ('Lesson files', 'academy/lesson66: INSTALL.txt, report_template.md', 'g3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 'g4'), ('cd devops-ai/academy/lab', 'g4'), ('sudo install -m 755 lab66.sh /usr/local/sbin/', 'g4'), ('source shortcuts66.sh', 'g6'), ('lab up  |  lab check  |  lab down', 'g5')]
    E.append(Pop(glass(1700, 5 * 46 + 48, WARN), 100, 700, C['g4']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, root, git. Your own machine only.', 'm', 26, MUTED, maxw=1700), 100, 990, C['g7'], anim='fade')); return E
s_start = _lab('Start the lab', 'Install it, build it, check it.', 'st1', RB, [('st1', 'cd lab', 'The lab folder', ACC), ('st3', 'sudo install', 'Install the script', VIO), ('st4', 'source', 'Short name: lab', WARN), ('st5', 'lab up', 'Build the faults', BAD), ('st6', 'lab check', 'Four FAIL lines', GOOD)])
def s_notes(C, D, dur):
    E = head('Four notes per fault', 'Evidence, not luck.', C['n1'])
    it = [('1  Symptom', 'the exact words', BAD, 'n2'), ('2  Cause', 'and the proving command', ACC, 'n3'), ('3  Fix', 'one change only', WARN, 'n4'), ('4  Proof', 'output after the fix', GOOD, 'n5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s_, TXT)], 44, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Notes turn a lucky fix into evidence.', 800, C['n6'], GOOD, 1700)); return E
s_fix1 = _lab('Fault 2, live', 'A merge conflict, resolved with proof.', 'f1', RB, [('f2', 'git log --graph', 'Branches apart', ACC), ('f3', 'git merge', 'CONFLICT in price.txt', BAD), ('f4', 'cat price.txt', 'Both versions shown', WARN), ('f5', 'echo ...', 'Keep both lines', PINK), ('f8', 'git commit', 'Merge finished', GOOD), ('f9', 'lab check', 'One PASS', VIO)])
def s_report(C, D, dur):
    E = head('The report', 'Five parts. Template in academy/lesson66.', C['r1']); E.append(ill(C['r1'] + 0.2, 1400, 170))
    it = [('Setup', 'checker output at the start', ACC, 'r2'), ('Each fault', 'its four notes', VIO, 'r3'), ('Final check', 'four PASS lines', GOOD, 'r4'), ('Where I got stuck', 'and what unstuck me', WARN, 'r5'), ('Cleanup proof', 'four proofs', PINK, 'r6')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s_, TXT)], 40, 30, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    return E
def s_hints(C, D, dur):
    E = head('Your three faults', 'Directions only. No spoilers.', C['y1'])
    it = [('Check 1', 'secret: untrack, ignore, amend', VIO, 'y2'), ('Check 3', 'read the failing line, new commit', WARN, 'y3'), ('Check 4', 'push, then an annotated tag', PINK, 'y4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1500, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 175, C[cid]))
    E.append(takeaway('Symptom. Check. Fix one thing. Verify.', 900, C['y5'], GOOD, 1700)); return E
s_cleanup = _lab('Cleanup with proof', 'Nothing left behind.', 'c1', RB, [('c1', 'lab down', 'Remove the lab', ACC), ('c2', 'ls /opt/lab66', 'No folder', VIO), ('c3', 'ls /opt | grep -c', 'Count: 0', WARN), ('c4', 'sudo rm', 'Remove the script', PINK), ('c5', 'ls ... | wc -l', 'Nothing left', GOOD)])
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Four PASS lines', 'b2'), ('Four notes per fault', 'b3'), ('One change at a time', 'b4'), ('Complete report', 'b5'), ('Cleanup proof', 'b6'), ('Own VM only', 'b7')]
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
    qs = [('Why remove a secret before pushing?', 'f12'), ('What is a merge conflict?', 'f13'), ('What does the pre-push gate protect?', 'f14'), ('What proves cleanup worked?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Mastery evidence: MC07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: application architecture and APIs', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, scenario=s_scenario, getlab=s_getlab, start=s_start, notes=s_notes, fix1=s_fix1, report=s_report, hints=s_hints, cleanup=s_cleanup, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(scenario=('board', ACC), getlab=('gear', VIO), start=('gear', ACC), notes=('board', WARN), fix1=('test', GOOD), report=('board', VIO), hints=('question', WARN), cleanup=('eye', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson66/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))

