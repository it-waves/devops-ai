def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Feed your script', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Variables', 'named boxes for values', ACC), ('Arguments', 'words after the script name', VIO), ('read', 'ask the user', WARN), ('$( )', 'capture a command output', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.2))
    E.append(takeaway('Same script, different input.', 880, C['h3'], GOOD, 1700)); return E
s_vars = _lab('Variables', 'Named boxes for values.', 'a1', RB, [('a1', 'city=Paris', 'No spaces', ACC), ('a2', 'echo "$city"', 'Read it back', GOOD), ('a4', '${city}land', 'Braces end the name', VIO), ('a5', '${name:-stranger}', 'Default value', WARN), ('a6', 'city = Paris', 'Spaces: fails', BAD)])
s_args = _lab('Positional arguments', 'Words after the script name.', 'g1', RB, [('g1', 'cat greet.sh', '$1  $#  $@', ACC), ('g2', './greet.sh Sam', 'One argument', GOOD), ('g3', './greet.sh Sam Lee Kim', 'Three arguments', VIO), ('g4', '"Sam Lee" Kim', 'Quotes group', WARN), ('g5', './greet.sh', 'None: empty, 0', BAD)])
s_input = _lab('Reading input', 'Ask the user, or read a pipe.', 'i1', RB, [('i1', 'cat ask.sh', 'read -p', ACC), ('i2', './ask.sh', 'Answer by keyboard', GOOD), ('i3', 'echo Lee | ./ask.sh', 'Answer from a pipe', VIO)])
s_subst = _lab('Command substitution', 'Capture a command output.', 's1', RB, [('s1', 'today=$(date +%F)', 'Store the output', ACC), ('s2', 'backup-$today.tar', 'Use it in text', GOOD), ('s3', 'ls | wc -l', 'Count lines', VIO), ('s4', 'count=$(ls | wc -l)', 'Store the count', WARN), ('s5', 'There are $count', 'Use it', PINK)])
s_build = _lab('Put it together', 'One script, three ideas.', 't1', RB, [('t1', 'cat backup.sh', 'Read the script', ACC), ('t2', './backup.sh', 'Default: data', GOOD), ('t3', './backup.sh photos', 'Argument: photos', VIO)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: spaces around =', 'Spaces make it a command.', 'my2'), ('Myth: $1 is the script', '$0 is the script, $1 the first argument.', 'my3'), ('Myth: quotes are optional', 'A space in the value splits it.', 'my4'), ('Myth: read needs a keyboard', 'It reads pipes and files too.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Set it. Pass it. Ask for it. Capture it.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Assign and print', 'b2'), ('Braces and defaults', 'b3'), ('$0 $1 $# $@', 'b4'), ('Quote spaced args', 'b5'), ('read: keyboard, pipe', 'b6'), ('Capture with $( )', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  Variables', 'two, in a sentence', PINK, 'z2'), ('2  Arguments', 'first, count, all', ACC, 'z3'), ('3  Spaces', 'quoted and not', WARN, 'z4'), ('4  Read', 'by hand, then piped', VIO, 'z5'), ('5  Capture', 'date and file count', BAD, 'z6'), ('6  Default', 'with and without', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does $# hold?', 'f12'), ('Keep a spaced argument as one?', 'f13'), ('Which command asks for input?', 'f14'), ('What does $( ) do?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O02', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: conditions and loops', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, vars=s_vars, args=s_args, input=s_input, subst=s_subst, build=s_build, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(vars=('board', ACC), args=('gear', VIO), input=('question', WARN), subst=('gear', GOOD), build=('test', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'vars': [('a3', 1, 1, 4, 240, ''), ('a5', 1, 1, 4, 150, ''), ('a6', 1, 1, 4, 135, ''), ('a7', 1, 1, 4, 450, '')],
 'args': [('g2', 2, 3, 4, 270, ''), ('g3', 1, 2, 4, 170, ''), ('g4', 1, 3, 4, 260, ''), ('g5', 1, 2, 4, 200, ''), ('g6', 1, 3, 4, 150, '')],
 'input': [('i2', 2, 1, 4, 430, ''), ('i3', 1, 2, 4, 260, ''), ('i4', 1, 1, 4, 195, '')],
 'subst': [('s3', 1, 1, 4, 325, ''), ('s4', 1, 1, 4, 30, ''), ('s6', 1, 1, 4, 265, '')],
 'build': [('t2', 2, 2, 4, 270, ''), ('t3', 1, 1, 4, 540, ''), ('t4', 1, 1, 4, 570, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson38/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
