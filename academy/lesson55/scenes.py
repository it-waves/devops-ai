def s_hook(C, D, dur):
    E = [El(T('A tested validation utility', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('A pure function', 'checks the data, returns errors', ACC), ('Exit codes', '0 valid, 1 problems, 2 unreadable', GOOD), ('Tests', 'edges, parametrize, red then green', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 3.5))
    E.append(takeaway('Build it, then prove it works.', 850, C['h3'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('Anatomy of a utility', 'Check, report, exit, test.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 215, ACC, 'validate()', [('pure: data in, errors out', TXT), ('easy to test', MUTED)], 44, 32, True), 100, 340, C['w2']))
    E.append(Pop(card(540, 215, GOOD, 'exit codes', [('0 valid  1 problems', TXT), ('2 cannot read', MUTED)], 44, 32, True), 690, 340, C['w3']))
    E.append(Pop(card(540, 215, WARN, 'edges', [('largest valid value', TXT), ('first invalid one', MUTED)], 44, 32, True), 1280, 340, C['w4']))
    E.append(Pop(card(1700, 150, VIO, 'red, then green', [('break the code on purpose, watch a test fail', TXT)], 38, 30), 100, 620, C['w5'] - 3.0))
    E.append(takeaway('Pure function. Clear errors. Tests with edges.', 850, C['w5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Get the lab and task', 'Everything is in the repository.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 't2', ACC), ('Folder', 'academy/lesson55', 't3', VIO), ('Files', 'TASK.md  check55.sh  broken_invcheck.py', 't3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 't3'), ('cd devops-ai/academy/lesson55 && pip install pytest', 't3'), ('# write invcheck.py and test_invcheck.py', 't4'), ('bash check55.sh .      # six PASS lines', 't6')]
    E.append(Pop(glass(1700, 4 * 46 + 48, WARN), 100, 700, C['t3']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, python3, your venv. No server, no cloud account. No peeking at the solution.', 'm', 26, MUTED, maxw=1700), 100, 960, C['t6'], anim='fade')); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['r1'])
    items = [('Checker: six PASS', 'r2'), ('One line per problem, 0/1/2', 'r3'), ('Every rule, one error each', 'r4'), ('6+ tests, parametrize', 'r5'), ('Tests fail the broken one', 'r6'), ('Complete report, own VM', 'r7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['r8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only.', C['z1'])
    it = [('1  Get files', 'lesson55 folder, venv, pytest', PINK, 'z2'), ('2  validate()', 'write it, try it in python', ACC, 'z3'), ('3  Command line', 'exit codes 0, 1, 2', VIO, 'z4'), ('4  Tests', '6+, edges, parametrize', WARN, 'z5'), ('5  Break it', 'watch a test fail', BAD, 'z6'), ('6  Check', 'six PASS, then report', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why a pure checking function?', 'f12'), ('What do exit codes 0, 1, 2 mean?', 'f13'), ('Which values should you test?', 'f14'), ('How do you prove a test can fail?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC06-O09', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: Python for DevOps mastery', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_tool = _lab('The tool and exit codes', 'Validate, report, exit.', 'e1', RB, [('e1', 'head svccheck.py', 'the checking logic', ACC), ('e3', 'services.json', '3 planted problems', VIO), ('e4', '3 problems', 'all errors, one run', GOOD), ('e5', 'exit code 1', 'problems found', WARN), ('e6', 'nope.json', 'clear error, no crash', PINK), ('e7', 'exit code 2', 'cannot read the file', BAD)])
s_tests = _lab('Tests: edges, red, green', 'Prove it works, then break it.', 'f1', RB, [('f1', 'cat test_svccheck.py', 'edges and parametrize', ACC), ('f3', '7 passed', 'all green', GOOD), ('f4', 'break it', 'upper limit plus one', WARN), ('f5', '1 failed', 'the edge test caught it', BAD), ('f7', 'fixed: green', 'red, then green', GOOD)])
FN = dict(hook=s_hook, why=s_why, tool=s_tool, tests=s_tests, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('gear', ACC), tool=('test', WARN), tests=('board', VIO), task=('gear', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'tool': [('e4', 1, 4, 4, 504, ''), ('e5', 1, 1, 4, 40, ''), ('e6', 1, 1, 4, 322, ''), ('e7', 1, 1, 4, 40, '')],
 'tests': [('f3', 2, 1, 4, 280, ''), ('f5', 3, 2, 4, 1050, ''), ('f7', 2, 1, 4, 280, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson55/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
