def s_hook(C, D, dur):
    E = [El(T('Red text is a map', 'x', 72), 100, 130, C['h1'])]
    errs = [("error: ';' expected", 'h2', 0.0, BAD), ('class Right is public: wrong file name', 'h2', 3.5, WARN), ('Could not find or load main class', 'h2', 7.0, VIO)]
    for i, (e, cid, dt, col) in enumerate(errs): E.append(Pop(card(1500, 100, col, '', [(e, TXT)], 4, 40), 100, 300 + i * 125, C[cid] + dt))
    ws = [('write', ACC), ('compile', VIO), ('run', GOOD), ('read the error', WARN)]
    x = 100
    for i, (w, col) in enumerate(ws):
        b = chip(w, col, 40); E.append(Pop(b, x, 720, C['h3'] + 1.0 + i * 1.5)); x += b.width + 30
    E.append(takeaway('Read it. It tells you where.', 900, C['h4'], GOOD, 1700)); return E
def s_rules(C, D, dur):
    E = head('Four small rules', 'They explain almost every beginner failure.', C['u1']); E.append(ill(C['u1'] + 0.2, 1400, 170))
    it = [('1  Names match', 'Greeter.java  holds  class Greeter', ACC, 'u2'), ('2  Start at main', 'public static void main(String[] args)', VIO, 'u3'), ('3  Two commands', 'javac Greeter.java   ›   java Greeter', GOOD, 'u4'), ('4  Words go to args', 'java Greeter Ada   ›   args[0] is Ada', WARN, 'u5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 135, col, n, [(s_, TXT)], 44, 34), 100, 330 + i * 160, C[cid]))
    E.append(takeaway('Learn four rules once. Use them forever.', 985, C['u6'], GOOD, 1700, 38)); return E
s_run = _lab('Compile and run', 'Write once, compile, run, and read the exit code.', 'r0', RB, [('r2', 'java Greeter.java Ada', 'one step, in memory', ACC), ('r4', 'javac Greeter.java', 'saves Greeter.class', VIO), ('r6', 'java Greeter Ada', 'run the bytecode', GOOD), ('r7', 'java Greeter', 'no name: usage', WARN), ('r8', 'echo $?', 'exit code: 2', PINK)])
s_errors = _lab('Break it on purpose', 'Three real mistakes, and how each one reads.', 'e0', RB, [('e1', 'javac Broken.java', "error: ';' expected", BAD), ('e2', 'sed -i 3s/$/;/', 'add the semicolon', ACC), ('e4', 'java Broken', 'now it runs', GOOD), ('e5', 'javac Wrong.java', 'file name rule', WARN), ('e6', 'java Greeter.class', 'wrong at run time', PINK)])
def s_models(C, D, dur):
    E = head('Compile time or run time?', 'Ask first: did it compile, or did it run?', C['o1'])
    it = [('Compile time  ·  javac', 'syntax errors and the file name rule. No .class is made.', VIO, 'o2'), ('Run time  ·  java', 'wrong class name or folder, or the program fails.', WARN, 'o3'), ('Your own program', 'writes to standard error, and sets an exit code.', BAD, 'o4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 180, C[cid]))
    E.append(takeaway('Where did it fail?  Then read the message.', 900, C['o5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab77.sh builds two programs. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab77.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Compile, run', [('javac Greeter.java', TXT), ('java Greeter Ada > run.txt', TXT)], 'k3', ACC), ('2  Exit code', [('java Greeter', TXT), ('echo $? > exit.txt', TXT)], 'k4', VIO), ('3  Capture error', [('javac Broken.java', TXT), ('2> error.txt', TXT)], 'k5', BAD), ('4  Fix and run', [('fix Broken.java', TXT), ('java Broken > broken.txt', TXT)], 'k6', GOOD), ('5  Answers', [('public class: file name', TXT), ('exit code: 0', TXT), ('java takes: class name', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Why names must match', 'q3'), ('Read an error: 4 parts', 'q4'), ('javac vs java arguments', 'q5'), ('Show an exit code', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Build', 'compile and run Greeter', ACC, 'z3'), ('3  Exit code', 'run it with no name', VIO, 'z4'), ('4  Fix', 'capture the error, fix Broken', WARN, 'z5'), ('5  Check', 'answers, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What must match the public class name?', 'f12'), ('javac: file or class name? And java?', 'f13'), ('Where do words after the class name go?', 'f14'), ('What does exit code 0 mean?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC09-O02', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: packages, classpath and dependencies', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, rules=s_rules, run=s_run, errors=s_errors, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(rules=('board', ACC), run=('test', GOOD), errors=('question', WARN), models=('gear', VIO), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'run': [('r1b', 5, 1, 182, 410, 'EXIT CODE 2'), ('r7b', 1, 1, 0, 370, 'STANDARD ERROR'), ('r8b', 1, 1, 0, 15, 'EXIT CODE')],
 'errors': [('e1b', 1, 1, 0, 520, 'FILE : LINE'), ('e1b', 3, 1, 775, 805, 'THE ARROW'), ('e5b', 1, 1, 319, 638, 'RULE ONE'), ('e6b', 1, 2, 0, 890, 'RULE THREE')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson77/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
