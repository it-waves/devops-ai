def s_hook(C, D, dur):
    E = [El(T('Wall of text?', 'x', 72), 100, 130, C['h1'])]
    errs = [('Exception in thread "main" ...', 'h1', 2.0, BAD), ('at com.cloudcart.Checkout...', 'h1', 5.0, WARN), ('Caused by: ...', 'h2', 2.0, VIO)]
    for i, (e, cid, dt, col) in enumerate(errs): E.append(Pop(card(1500, 100, col, '', [(e, TXT)], 4, 40), 100, 300 + i * 125, C[cid] + dt))
    ws = [('what', ACC), ('where', VIO), ('mine', GOOD), ('why', WARN)]
    x = 100
    for i, (w, col) in enumerate(ws):
        b = chip(w, col, 40); E.append(Pop(b, x, 720, C['h3'] + 1.0 + i * 1.5)); x += b.width + 30
    E.append(takeaway('A map, not noise.', 900, C['h4'], GOOD, 1700)); return E
def s_ideas(C, D, dur):
    E = head('Four questions', 'Every stack trace answers them.', C['u1']); E.append(ill(C['u1'] + 0.2, 1400, 170))
    it = [('1  What happened?', 'the first line: exception name, then message', ACC, 'u2'), ('2  Where?', 'the "at" lines: top = failure, below = who called it', VIO, 'u3'), ('3  Which code is mine?', 'first line with your own package name', GOOD, 'u4'), ('4  Why, really?', 'the last "Caused by" is the root cause', WARN, 'u5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 135, col, n, [(s_, TXT)], 44, 34), 100, 330 + i * 160, C[cid]))
    E.append(takeaway('Then confirm it in the log: time, level, message.', 985, C['u6'], GOOD, 1700, 38)); return E
s_trace = _lab('Read a stack trace', 'Run, read, check the exit code, scan.', 't0', RB, [('t1', 'javac -d out ...', 'compile', ACC), ('t2', 'java -cp out ...Checkout', 'it crashes', BAD), ('t3', 'echo $?', 'exit code: not zero', VIO), ('t4', '2>&1 | grep -n Caused', 'scan for the cause', GOOD)])
s_logs = _lab('Read the log', 'Newest lines, counts, errors, context, warnings.', 'l0', RB, [('l1', 'tail -n 5 app.log', 'time, level, message', ACC), ('l2', 'grep -c ERROR app.log', 'count the errors', VIO), ('l3', 'grep ERROR app.log', 'the failed orders', BAD), ('l4', 'grep -A2 ERROR app.log', 'lines after the error', GOOD), ('l5', 'grep WARN app.log', 'early signals', WARN)])
def s_models(C, D, dur):
    E = head('Where to look', 'In this order.', C['o1'])
    it = [('1  Exit code', 'echo $?  :  zero is success, anything else failed.', VIO, 'o2'), ('2  The log', 'grep ERROR, grep -c ERROR, grep -A2 ERROR.', WARN, 'o3'), ('3  The trace', 'what, where, which line is mine, last Caused by.', GOOD, 'o4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 180, C[cid]))
    E.append(takeaway('Facts first. Fixes second.', 900, C['o5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab81.sh gives you a crashing program and a log. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab81.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Compile', [('javac -d out', TXT), ('src/com/cloudcart/Checkout.java', TXT)], 'k3', ACC), ('2  Run, save errors', [('java -cp out com.cloudcart.Checkout', TXT), ('2> crash.txt', TXT)], 'k4', VIO), ('3  Error lines', [('grep ERROR app.log', TXT), ('> errors.txt', TXT)], 'k5', GOOD), ('4  Error count', [('grep -c ERROR app.log', TXT), ('> count.txt', TXT)], 'k6', BAD), ('5  Answers', [('answers.txt, 3 lines:', TXT), ('top exception, root cause,', TXT), ('bad value', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('What happened', 'q3'), ('Find the root cause', 'q4'), ('Find my own code', 'q5'), ('Same failure in the log', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Run', 'compile, run, save errors', ACC, 'z3'), ('3  Log', 'grep errors, count them', VIO, 'z4'), ('4  Read', 'root cause and bad value', WARN, 'z5'), ('5  Check', 'answers, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does the first line tell you?', 'f12'), ('Which line is the root cause?', 'f13'), ('How do you find your own code?', 'f14'), ('How do you count errors in a log?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC09-O06', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: Java tests and builds', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ideas=s_ideas, trace=s_trace, logs=s_logs, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ideas=('board', ACC), models=('gear', VIO), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'trace': [('t2b', 1, 2, 0, 1076, 'WHAT HAPPENED', 140, 2), ('t2c', 5, 1, 0, 1010, 'ROOT CAUSE', 870, 4), ('t2d', 10, 1, 0, 851, 'YOUR CODE'), ('t3b', 1, 1, 0, 30, 'NOT ZERO = FAILED'), ('t4b', 2, 1, 0, 1010, 'ROOT CAUSE, LINE 4', 420, 3)],
 'logs': [('l1b', 2, 1, 0, 836, 'ERROR = FAILURE'), ('l2b', 1, 1, 0, 30, 'TWO ERRORS'), ('l3b', 1, 1, 0, 836, 'ORDER 1042'), ('l4b', 2, 1, 0, 836, 'TRACE MATCH'), ('l5b', 1, 2, 0, 897, 'EARLY')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson81/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
