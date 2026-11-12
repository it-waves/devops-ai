def s_hook(C, D, dur):
    E = [El(T('Test your scripts, fake the network', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Tests', 'pytest finds them and runs them', ACC), ('assert', 'a plain assert is the check', GOOD), ('Mocks', 'fake the network, test anywhere', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 3.0))
    E.append(takeaway('Trust comes from tests that can fail.', 850, C['h3'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('Tests, asserts, mocks', 'Prove it works, and keep proving it.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 215, ACC, 'pytest', [('test_*.py  test_*()', TXT), ('plain assert', MUTED)], 44, 32, True), 100, 340, C['w2']))
    E.append(Pop(card(540, 215, GOOD, 'parametrize', [('one test, many inputs', TXT), ('pytest.raises', MUTED)], 44, 32, True), 690, 340, C['w3']))
    E.append(Pop(card(540, 215, WARN, 'mock', [('fake answer', TXT), ('fake failure', MUTED)], 44, 32, True), 1280, 340, C['w4']))
    E.append(Pop(card(1700, 150, VIO, 'red, then green', [('watch it fail first, then make it pass', TXT)], 38, 30), 100, 620, C['w4'] + 3.0))
    E.append(takeaway('Test one thing. Fake what you do not control.', 850, C['w5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Get the lab and task', 'Everything is in the repository.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 't2', ACC), ('Folder', 'academy/lesson53', 't3', VIO), ('Files', 'TASK.md  inventory_tools.py  check53.sh', 't3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 't3'), ('cd devops-ai/academy/lesson53 && pip install requests pytest', 't3'), ('# write test_tools.py: 5+ tests, parametrize, mock', 't4'), ('bash check53.sh .      # six PASS lines', 't5')]
    E.append(Pop(glass(1700, 4 * 46 + 48, WARN), 100, 700, C['t3']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, python3, your venv. Your own machine only. No peeking at the solution first.', 'm', 26, MUTED, maxw=1700), 100, 960, C['t6'], anim='fade')); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['r1'])
    items = [('Checker: six PASS', 'r2'), ('5+ tests, all pass', 'r3'), ('parametrize and raises', 'r4'), ('Network faked, no server', 'r5'), ('Tests catch broken code', 'r6'), ('Complete report, own VM', 'r7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['r8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only.', C['z1'])
    it = [('1  Get files', 'lesson53 folder, activate venv', PINK, 'z2'), ('2  Install', 'pip install requests pytest', ACC, 'z3'), ('3  Write tests', '5+, parametrize, raises', WARN, 'z4'), ('4  Fake network', 'Mock and patch', VIO, 'z5'), ('5  Break it', 'watch a test fail', BAD, 'z6'), ('6  Check', 'six PASS, then report', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('How does pytest find your tests?', 'f12'), ('What does a mock replace?', 'f13'), ('Why watch a test fail once?', 'f14'), ('Exit code when a test fails?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC06-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: cloud SDKs, least privilege', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_pytest = _lab('pytest: red to green', 'Write a test, watch it fail, make it pass.', 'p1', RB, [('p1', 'cat inventory.py', 'the code under test', ACC), ('p3', 'test_*.py', 'plain assert, parametrize', VIO), ('p4', 'pytest -q', '4 passed: all green', GOOD), ('p5', 'break it', 'change the expected name', WARN), ('p6', 'F: 1 failed', 'expected against actual', BAD), ('p8', 'fixed: green', 'red, then green', GOOD)])
s_mock = _lab('Mocks: fake the network', 'Test code that calls the network.', 'm1', RB, [('m1', 'cat test_health.py', 'Mock, patch, raises', ACC), ('m2', 'Mock()', 'a fake answer', VIO), ('m3', '6 passed', 'no network, no server', GOOD), ('m4', 'pytest -v', 'every test, by name', WARN), ('m5', '-k down', 'run only some tests', PINK)])
FN = dict(hook=s_hook, why=s_why, pytest=s_pytest, mock=s_mock, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('gear', ACC), pytest=('test', WARN), mock=('board', VIO), task=('gear', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'pytest': [('p4', 2, 1, 4, 280, ''), ('p6', 6, 1, 4, 777, ''), ('p8', 2, 1, 4, 280, '')],
 'mock': [('m3', 2, 1, 4, 280, ''), ('m4', 6, 1, 4, 262, ''), ('m5', 2, 1, 4, 474, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson53/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
