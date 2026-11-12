def s_hook(C, D, dur):
    E = [El(T('Fail well: exceptions, logs, retries', 'x', 68), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Exceptions', 'catch the failures you expect, by name', ACC), ('Logging', 'say what happened, with a level', GOOD), ('Retries', 'try again, but never forever', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 2.6))
    E.append(takeaway('Turn a crash into a controlled result.', 850, C['h3'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('Exceptions, logging, retries', 'Three habits for scripts that run unattended.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 215, ACC, 'try / except', [('else, finally', TXT), ('catch by name', MUTED)], 44, 32, True), 100, 340, C['w2']))
    E.append(Pop(card(540, 215, VIO, 'logging', [('debug  info', TXT), ('warning  error', MUTED)], 44, 32, True), 690, 340, C['w3']))
    E.append(Pop(card(540, 215, WARN, 'retries', [('wait 1s, 2s, 4s', TXT), ('then give up', MUTED)], 44, 32, True), 1280, 340, C['w4']))
    E.append(Pop(card(1700, 150, GOOD, 'no catch', [('Traceback (most recent call last): ...   the script stops', TXT)], 38, 30), 100, 620, C['w1'] + 3.0))
    E.append(takeaway('Catch what you expect. Say what happened. Retry what can recover.', 850, C['w5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Get the lab and task', 'Everything is in the repository.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 't2', ACC), ('Folder', 'academy/lesson51', 't3', VIO), ('Files', 'TASK.md  api06.py  check51.sh', 't3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 't3'), ('cd devops-ai/academy/lesson51 && pip install requests', 't3'), ('# write fetch_retry.py: 4 tries, logging, back off', 't4'), ('bash check51.sh .      # four PASS lines', 't5')]
    E.append(Pop(glass(1700, 4 * 46 + 48, WARN), 100, 700, C['t3']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, python3, your venv. Your own machine only. No peeking at the solution first.', 'm', 26, MUTED, maxw=1700), 100, 960, C['t6'], anim='fade')); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['r1'])
    items = [('Checker: four PASS', 'r2'), ('Every attempt logged', 'r3'), ('RequestException, no bare except', 'r4'), ('timeout= and growing wait', 'r5'), ('Gave up: message, exit 1', 'r6'), ('Complete report, own VM', 'r7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['r8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only.', C['z1'])
    it = [('1  Get files', 'lesson51 folder, activate venv', PINK, 'z2'), ('2  Run the API', 'python3 api06.py', ACC, 'z3'), ('3  Loop', '4 attempts, timeout=2', WARN, 'z4'), ('4  Catch + log', 'RequestException, logging', VIO, 'z5'), ('5  Back off', 'wait 1, 2, 4, then exit 1', BAD, 'z6'), ('6  Check', 'four PASS, then report', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why is a bare except a bad idea?', 'f12'), ('Which level for a failed attempt?', 'f13'), ('Why does the wait grow between retries?', 'f14'), ('Which failures are worth retrying?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC06-O05', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: CLI tools and exit codes', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_exceptions = _lab('try, except, else, finally', 'Catch the failures you expect, by name.', 'e1', RB, [('e2', 'int("eight")', 'a word is not a number', ACC), ('e3', 'ValueError', 'the last line names the exception', BAD), ('e4', 'cat load.py', 'one except per failure', VIO), ('e5', 'no file', 'FileNotFoundError, handled', WARN), ('e7', 'valid file', 'else, then finally', GOOD), ('e9', 'bad JSON', 'caught, explained, no crash', PINK)])
s_logging = _lab('Logging levels', 'Tell operators what happened.', 'l1', RB, [('l1', 'cat logdemo.py', 'debug, info, warning, error', ACC), ('l2', 'level="INFO"', 'debug stays hidden', VIO), ('l3', 'log.exception', 'message and traceback', BAD), ('l4', 'sed: WARNING', 'turn the detail down', WARN), ('l5', 'less noise', 'only warning and error', GOOD)])
s_retry = _lab('Retries with back off', 'Wait, try again, wait longer.', 'y1', RB, [('y1', 'cat retry.py', 'four attempts, logged', ACC), ('y2', 'wait 1s, 2s, 4s', 'exponential back off', VIO), ('y3', 'attempt 3 ok', 'two warnings, then success', GOOD), ('y4', 'only two tries', 'let it give up', WARN), ('y5', 'echo $?', '1 means failure', BAD)])
FN = dict(hook=s_hook, why=s_why, exceptions=s_exceptions, logging=s_logging, retry=s_retry, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('gear', ACC), exceptions=('test', WARN), logging=('board', VIO), retry=('gear', GOOD), task=('gear', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'exceptions': [('e3', 3, 1, 4, 883, ''), ('e6', 1, 1, 4, 595, ''), ('e8', 3, 1, 4, 171, ''), ('e10', 1, 1, 4, 913, '')],
 'logging': [('l3', 3, 1, 4, 292, ''), ('l5', 1, 1, 4, 398, '')],
 'retry': [('y3', 3, 1, 4, 262, ''), ('y5', 3, 1, 4, 443, ''), ('y6', 1, 1, 4, 30, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson51/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
