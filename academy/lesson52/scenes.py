def s_hook(C, D, dur):
    E = [El(T('A script that speaks to the command line', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Arguments', 'argparse reads and checks them', ACC), ('Exit codes', '0 means success, anything else, failure', GOOD), ('Two channels', 'results out, problems to standard error', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 3.0))
    E.append(takeaway('Make your script a proper tool.', 850, C['h3'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('Arguments, exit codes, two channels', 'What a pipeline needs from your script.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 215, ACC, 'argparse', [('host  port  -q', TXT), ('checks types, writes help', MUTED)], 44, 32, True), 100, 340, C['w2']))
    E.append(Pop(card(540, 215, GOOD, 'exit code', [('0 success', TXT), ('1 failure   2 bad usage', MUTED)], 44, 32, True), 690, 340, C['w3']))
    E.append(Pop(card(540, 215, WARN, 'two channels', [('out: results', TXT), ('error: problems', MUTED)], 44, 32, True), 1280, 340, C['w4']))
    E.append(Pop(card(1700, 150, VIO, 'a pipeline', [('cannot read your words, it reads the exit code', TXT)], 38, 30), 100, 620, C['w3'] + 3.0))
    E.append(takeaway('Arguments in. Exit code out. Problems to standard error.', 850, C['w5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Get the lab and task', 'Everything is in the repository.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 't2', ACC), ('Folder', 'academy/lesson52', 't3', VIO), ('Files', 'TASK.md  api06.py  check52.sh', 't3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 't3'), ('cd devops-ai/academy/lesson52 && pip install requests', 't3'), ('# write svc_check.py: argparse, exit codes 0 / 1 / 2', 't4'), ('bash check52.sh .      # six PASS lines', 't5')]
    E.append(Pop(glass(1700, 4 * 46 + 48, WARN), 100, 700, C['t3']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, python3, your venv. Your own machine only. No peeking at the solution first.', 'm', 26, MUTED, maxw=1700), 100, 960, C['t6'], anim='fade')); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['r1'])
    items = [('Checker: six PASS', 'r2'), ('Exit codes 0, 1 and 2', 'r3'), ('Results out, problems to stderr', 'r4'), ('argparse and timeout=', 'r5'), ('No traceback, no bare except', 'r6'), ('Complete report, own VM', 'r7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['r8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only.', C['z1'])
    it = [('1  Get files', 'lesson52 folder, activate venv', PINK, 'z2'), ('2  Run the API', 'python3 api06.py', ACC, 'z3'), ('3  argparse', 'url, -t timeout, -q', WARN, 'z4'), ('4  Call it', 'timeout=, RequestException', VIO, 'z5'), ('5  Report', 'UP out, DOWN to stderr, 0 or 1', BAD, 'z6'), ('6  Check', 'six PASS, then report', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does exit code 0 mean?', 'f12'), ('Which channel carries the problems?', 'f13'), ('Which exit code means wrong usage?', 'f14'), ('Why does a pipeline read the exit code?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC06-O06', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: tests with pytest and mocks', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_cli = _lab('argparse and exit codes', 'A tool that reports with a number.', 'a1', RB, [('a1', 'cat portcheck.py', 'argparse, try, except', ACC), ('a3', '-h', 'help written for you', VIO), ('a5', 'exit code 0', 'port open: success', GOOD), ('a7', 'exit code 1', 'port closed: failure', BAD), ('a8', 'port "abc"', 'argparse refuses it', WARN), ('a9', 'exit code 2', 'wrong usage', PINK)])
s_shell = _lab('Exit codes in the shell', 'The shell chooses from the number.', 'b1', RB, [('b1', '2>/dev/null', 'throw away standard error', VIO), ('b2', '&& echo up', 'run on success', GOOD), ('b3', '|| echo down', 'run on failure', BAD), ('b4', 'the number decides', 'pipelines read exit codes', ACC)])
FN = dict(hook=s_hook, why=s_why, cli=s_cli, shell=s_shell, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('gear', ACC), cli=('test', WARN), shell=('board', VIO), task=('gear', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'cli': [('a3', 1, 1, 4, 580, ''), ('a4', 1, 1, 4, 292, ''), ('a5', 1, 1, 4, 30, ''), ('a6', 1, 1, 4, 383, ''), ('a7', 1, 1, 4, 30, ''), ('a8', 2, 1, 4, 913, ''), ('a9', 1, 1, 4, 30, '')],
 'shell': [('b3', 1, 1, 4, 40, ''), ('b4', 1, 1, 4, 70, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson52/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
