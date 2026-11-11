def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))



def s_hook(C, D, dur):
    E = [El(T('How the shell reads a line', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Running', 'shebang and execute bit', ACC), ('Quoting', 'single, double, none', VIO), ('Expansion', 'changed before the command runs', WARN), ('Exit status', 'zero means success', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.2))
    E.append(takeaway('Understand the line, then write the script.', 880, C['h3'], GOOD, 1700)); return E
def s_order(C, D, dur):
    E = head('How the shell reads a line', 'Four steps, always in this order.', C['o1']); E.append(ill(C['o1'] + 0.2, 1400, 170))
    it = [('1  Split', 'the line into words', ACC, 'o2'), ('2  Expand', 'variables, $( ), *, ~', WARN, 'o3'), ('3  Run', 'the command with those words', VIO, 'o4'), ('4  Exit status', 'a number: 0 means success', GOOD, 'o5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s_, TXT)], 44, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Strange results start at step 1 or 2.', 800, C['o6'], GOOD, 1700)); return E
s_run = _lab('How a script runs', 'A text file, a shebang, an execute bit.', 'r1', RB, [('r1', 'cat hi.sh', 'Read the script', ACC), ('r2', 'bash hi.sh', 'Name the program', VIO), ('r3', './hi.sh', 'Symptom: denied', BAD), ('r4', 'chmod u+x', 'Add execute', WARN), ('r5', './hi.sh', 'Runs directly', GOOD)])
s_quote = _lab('Quoting', 'Which characters are plain text?', 'q1', RB, [('q1', 'name=Sam', 'A variable', ACC), ('q2', 'echo "Hi $name"', 'Double: expands', GOOD), ('q3', "echo 'Hi $name'", 'Single: literal', WARN), ('q5', 'rm my notes.txt', 'No quotes: split', BAD), ('q6', 'rm "my notes.txt"', 'Quoted: works', VIO)])
s_expand = _lab('Expansion', 'Rewritten before the command runs.', 'e1', RB, [('e1', 'echo ~', 'Tilde: home', ACC), ('e2', 'echo "$(date +%A)"', 'Command output', VIO), ('e3', 'echo *.txt', 'Wildcard', WARN), ('e4', 'echo file-{a,b,c}.log', 'Brace list', PINK), ('e5', 'echo $((6 * 7))', 'Arithmetic', GOOD)])
s_env = _lab('Environment variables', 'What a child program can see.', 'v1', RB, [('v1', 'GREETING=hello', 'Shell only', ACC), ('v2', 'bash -c ...', 'Child: empty', BAD), ('v3', 'export GREETING', 'Share it', WARN), ('v4', 'bash -c ...', 'Child: hello', GOOD), ('v5', 'echo $PATH', 'Command search', VIO)])
s_exit = _lab('Exit status', 'Zero is success. Anything else is not.', 'x1', RB, [('x1', 'ls /etc/hostname', 'A command that works', ACC), ('x2', 'echo $?', 'Status: 0', GOOD), ('x3', 'ls /nope', 'A command that fails', BAD), ('x4', 'echo $?', 'Status: 2', WARN), ('x5', '&&   ||', 'Decide by status', VIO)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: scripts end in .sh', 'The shebang and execute bit matter.', 'my2'), ("Myth: ' and \" are the same", 'Double expands, single is literal.', 'my3'), ('Myth: zero means false', 'In the shell, zero is success.', 'my4'), ('Myth: quotes are optional', 'A space in a name will break it.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Quote it. Expand it. Check the exit status.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Run two ways, shebang', 'b2'), ('Single vs double quotes', 'b3'), ('Four expansions', 'b4'), ('export and children', 'b5'), ('$? with && and ||', 'b6'), ('Quote a spaced name', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  Script', 'bash it, then chmod and run', PINK, 'z2'), ('2  Spaces', 'break rm, then quote it', ACC, 'z3'), ('3  Quotes', "single vs double", WARN, 'z4'), ('4  Expand', 'date and a brace list', VIO, 'z5'), ('5  Export', 'child shell, before and after', BAD, 'z6'), ('6  Status', 'one success, one failure', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does the shebang line do?', 'f12'), ('Which quotes expand a variable?', 'f13'), ('What does exit status zero mean?', 'f14'), ('Why must you export a variable?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O01', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: variables and arguments', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, order=s_order, run=s_run, quote=s_quote, expand=s_expand, env=s_env, exit=s_exit, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(order=('board', ACC), run=('gear', ACC), quote=('question', WARN), expand=('gear', VIO), env=('eye', GOOD), exit=('test', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'run': [('r3', 1, 1, 4, 262, ''), ('r4', 1, 1, 4, 490, ''), ('r6', 1, 1, 4, 285, '')],
 'quote': [('q3', 1, 1, 4, 100, ''), ('q4', 1, 1, 4, 135, ''), ('q5', 1, 1, 4, 225, ''), ('q6', 1, 2, 4, 870, ''), ('q7', 1, 1, 4, 120, '')],
 'expand': [('e2', 1, 1, 4, 210, ''), ('e3', 1, 1, 4, 290, ''), ('e4', 1, 1, 4, 185, ''), ('e5', 1, 1, 4, 500, ''), ('e6', 1, 1, 4, 40, '')],
 'env': [('v3', 1, 1, 4, 180, ''), ('v5', 1, 1, 4, 270, ''), ('v6', 1, 1, 4, 940, '')],
 'exit': [('x2', 1, 1, 4, 215, ''), ('x3', 1, 1, 4, 30, ''), ('x4', 1, 1, 4, 805, ''), ('x5', 1, 1, 4, 30, ''), ('x6', 1, 1, 4, 85, ''), ('x7', 1, 1, 4, 110, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson37/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
