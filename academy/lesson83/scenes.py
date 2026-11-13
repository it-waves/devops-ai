def s_hook(C, D, dur):
    E = [El(T('Four ways Java fails', 'x', 72), 100, 130, C['h1'])]
    errs = [('UnsupportedClassVersionError', 'h2', 0.5, BAD), ('OutOfMemoryError', 'h3', 0.5, WARN), ('BindException', 'h3', 3.5, VIO), ('NoClassDefFoundError', 'h3', 6.5, ACC)]
    for i, (e, cid, dt, col) in enumerate(errs): E.append(Pop(card(1500, 100, col, '', [(e, TXT)], 4, 40), 100, 280 + i * 125, C[cid] + dt))
    E.append(takeaway('Read the first line. Name it. Fix it.', 900, C['h4'], GOOD, 1700)); return E
def s_ideas(C, D, dur):
    E = head('Four failures', 'The first line names each one.', C['u1']); E.append(ill(C['u1'] + 0.2, 1400, 170))
    it = [('1  Unsupported class version', 'built by a newer Java than the one running. Rebuild with this Java.', BAD, 'u2'), ('2  OutOfMemoryError: heap space', 'wanted more than its limit. Raise -Xmx, or use less.', WARN, 'u3'), ('3  BindException: address in use', 'another program owns the port. Free it or pick another.', VIO, 'u4'), ('4  NoClassDefFoundError', 'a class is missing from the class path. Add its jar to -cp.', ACC, 'u5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 135, col, n, [(s_, TXT)], 44, 34), 100, 330 + i * 160, C[cid]))
    E.append(takeaway('Read the first line. It names the problem.', 985, C['u6'], GOOD, 1700, 38)); return E
s_vermem = _lab('Version and memory', 'Read the first line, find the cause, fix one thing.', 'a0', RB, [('a1', 'sh run-version.sh', 'UnsupportedClassVersionError', BAD), ('a3', 'od ... Greeter.class', 'class version 69 > 65', VIO), ('a4', 'javac -d ver/classes ...', 'rebuild with this Java', GOOD), ('a6', 'sh run-memory.sh', 'OutOfMemoryError', BAD), ('a8', 'sed -i ... -Xmx256m', 'raise the limit', WARN), ('a9', 'sh run-memory.sh', 'OK memory', GOOD)])
s_portcp = _lab('Port and class path', 'Two more failures, same method.', 'p0', RB, [('p1', 'sh run-port.sh', 'BindException', BAD), ('p3', 'sed -i ... 18084', 'second server, new port', WARN), ('p4', 'sh run-port.sh', 'OK port 18083 + 18084', GOOD), ('p5', 'sh run-classpath.sh', 'NoClassDefFoundError', BAD), ('p8', 'sed -i ... helper.jar', 'jar on the class path', WARN), ('p9', 'sh run-classpath.sh', 'OK classpath', GOOD)])
def s_models(C, D, dur):
    E = head('How to diagnose', 'In this order.', C['o1'])
    it = [('1  Read the first error line', 'it names the failure.', VIO, 'o2'), ('2  Find the cause', 'version, limit, port owner, or class path.', WARN, 'o3'), ('3  Change one thing, run again', 'then you know what fixed it.', GOOD, 'o4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 180, C[cid]))
    E.append(takeaway('One change at a time.', 900, C['o5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab83.sh gives you four broken scripts. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab83.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Version', [('run-version.sh', TXT), ('rebuild the class', TXT)], 'k3', ACC), ('2  Memory', [('run-memory.sh', TXT), ('-Xmx256m', TXT)], 'k4', VIO), ('3  Port', [('run-port.sh', TXT), ('second server: 18084', TXT)], 'k5', GOOD), ('4  Class path', [('run-classpath.sh', TXT), ('add cp/lib/helper.jar', TXT)], 'k6', BAD), ('5  diag.txt', [('4 lines, one', TXT), ('exception name each', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Name each exception', 'q3'), ('Explain version mismatch', 'q4'), ('Explain port in use', 'q5'), ('Explain class path', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Read', 'run each script, first line only', ACC, 'z3'), ('3  Fix', 'version and memory', VIO, 'z4'), ('4  Fix', 'port and class path', WARN, 'z5'), ('5  Check', 'diag.txt, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Built by a newer Java?', 'f12'), ('What does -Xmx set?', 'f13'), ('Address already in use?', 'f14'), ('Missing class: where to look?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC09-O08', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: Java mastery lab', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ideas=s_ideas, vermem=s_vermem, portcp=s_portcp, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ideas=('board', ACC), models=('gear', VIO), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'vermem': [('a1b', 2, 4, 0, 1076, 'BUILT FOR 69  ·  THIS JAVA RUNS UP TO 65', 0, 7), ('a2b', 1, 1, 0, 440, 'JAVA 21 = UP TO 65'), ('a3b', 1, 1, 0, 70, 'VERSION 69 = JAVA 25'), ('a5b', 1, 1, 0, 160, 'FIXED'), ('a6b', 1, 1, 0, 1075, 'LIMIT TOO LOW', 0, 4), ('a7b', 1, 1, 76, 190, '16 MB LIMIT', 76, 3), ('a9b', 1, 1, 0, 300, 'FIXED')],
 'portcp': [('p1b', 2, 2, 0, 1076, 'ADDRESS ALREADY IN USE', 0, 7), ('p2b', 1, 2, 590, 690, 'SAME PORT', 590, 4), ('p4b', 1, 2, 0, 300, 'TWO PORTS'), ('p5b', 1, 2, 0, 1076, 'HELPER IS NOT ON THE CLASS PATH', 0, 8), ('p6b', 1, 1, 76, 290, 'ONLY CLASSES', 76, 3), ('p7b', 1, 1, 0, 110, 'IT EXISTS'), ('p9b', 1, 1, 0, 200, 'FIXED')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson83/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
