def s_hook(C, D, dur):
    E = [El(T('Red or green?', 'x', 72), 100, 130, C['h1'])]
    errs = [('FAIL 10 percent off 200: expected 180 got 20', 'h1', 2.0, BAD), ('exit code: 1', 'h2', 2.0, WARN), ('exit code: 0', 'h3', 2.0, GOOD)]
    for i, (e, cid, dt, col) in enumerate(errs): E.append(Pop(card(1500, 100, col, '', [(e, TXT)], 4, 40), 100, 300 + i * 125, C[cid] + dt))
    ws = [('run', ACC), ('read', VIO), ('fix', GOOD), ('rebuild', WARN)]
    x = 100
    for i, (w, col) in enumerate(ws):
        b = chip(w, col, 40); E.append(Pop(b, x, 720, C['h3'] + 1.0 + i * 1.5)); x += b.width + 30
    E.append(takeaway('One number decides.', 900, C['h4'], GOOD, 1700)); return E
def s_ideas(C, D, dur):
    E = head('Four facts', 'Tests and builds, in plain words.', C['u1']); E.append(ill(C['u1'] + 0.2, 1400, 170))
    it = [('1  A test is a program', 'runs your code, compares to what you expect, prints pass or fail', ACC, 'u2'), ('2  Failure = non-zero exit code', 'zero means green, anything else means red', VIO, 'u3'), ('3  Pipelines read the exit code', 'non-zero stops the build', GOOD, 'u4'), ('4  Output is disposable', 'classes and jars live in out/. Delete, then rebuild.', WARN, 'u5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 135, col, n, [(s_, TXT)], 44, 34), 100, 330 + i * 160, C[cid]))
    E.append(takeaway('Source is precious. Output is disposable.', 985, C['u6'], GOOD, 1700, 38)); return E
s_tests = _lab('Red, fix, green', 'Build, run, read the failure, fix, run again.', 't0', RB, [('t1', 'javac -d out/main ...', 'compile main', ACC), ('t3', 'java -cp out/main:out/test ...', '2 pass, 1 FAIL', BAD), ('t4', 'echo $?', 'exit code: 1 = red', VIO), ('t5', 'sed -i ...', 'fix the bug', WARN), ('t7', 'java -cp ... CartTest', '3 passed, 0 failed', GOOD), ('t8', 'echo $?', 'exit code: 0 = green', GOOD)])
s_outputs = _lab('Build outputs', 'Where the build puts its files, and why you can delete them.', 'b0', RB, [('b1', 'javac -d out/main ...', 'main classes', ACC), ('b3', 'find out -type f | sort', 'main and test apart', VIO), ('b4', 'jar cf cloudcart.jar', 'package main only', GOOD), ('b5', 'jar tf cloudcart.jar', 'no test inside', WARN), ('b6', 'rm -r out cloudcart.jar', 'throw the build away', BAD), ('b7', 'ls', 'only source remains', GOOD)])
def s_models(C, D, dur):
    E = head('Reading a build', 'In this order.', C['o1'])
    it = [('1  Exit code', 'echo $?  :  zero is green, anything else is red.', VIO, 'o2'), ('2  Test output', 'which test failed, expected, returned.', WARN, 'o3'), ('3  Output folder', 'classes, jars, reports. Delete and rebuild.', GOOD, 'o4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 180, C[cid]))
    E.append(takeaway('Red says something is wrong. The output says what.', 900, C['o5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab82.sh gives you a buggy class and its test. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab82.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Compile', [('javac -d out/main ...', TXT), ('javac -cp out/main -d out/test ...', TXT)], 'k3', ACC), ('2  Test before', [('run CartTest', TXT), ('> test-before.txt', TXT)], 'k4', VIO), ('3  Fix the bug', [('edit Cart.java', TXT), ('rebuild main', TXT)], 'k5', GOOD), ('4  Test after, jar', [('... > test-after.txt', TXT), ('jar cf cloudcart.jar -C out/main .', TXT)], 'k6', BAD), ('5  Answers', [('answers.txt, 3 lines:', TXT), ('exit code, output folder,', TXT), ('what the jar holds', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('What a test is', 'q3'), ('Read a failing test', 'q4'), ('Explain exit codes', 'q5'), ('Find, rebuild output', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Test', 'compile, run, save result', ACC, 'z3'), ('3  Fix', 'edit, rebuild', VIO, 'z4'), ('4  Green', 'rerun, build the jar', WARN, 'z5'), ('5  Check', 'answers, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What is a test?', 'f12'), ('Which exit code is green?', 'f13'), ('What does a pipeline read?', 'f14'), ('Why delete the output?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC09-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: diagnose Java failures', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ideas=s_ideas, tests=s_tests, outputs=s_outputs, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ideas=('board', ACC), models=('gear', VIO), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'tests': [('t3b', 3, 1, 0, 780, 'THE BUG'), ('t4b', 1, 1, 0, 30, 'NOT ZERO = RED'), ('t7b', 4, 1, 0, 320, 'GREEN'), ('t8b', 1, 1, 0, 30, 'ZERO = GREEN')],
 'outputs': [('b3b', 1, 2, 0, 580, 'MAIN + TEST APART'), ('b5b', 5, 1, 0, 380, 'CART ONLY'), ('b7b', 1, 1, 0, 60, 'ONLY SOURCE')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson82/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
