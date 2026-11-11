def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Streams, redirects, pipes', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Three streams', 'in, out and error', ACC), ('Redirection', '> >> < 2>', VIO), ('Pipes', 'join commands', WARN), ('Temp files', 'safe and clean', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Control where data goes.', 880, C['h3'], GOOD, 1700)); return E
s_streams = _lab('The three streams', 'Standard in, out and error.', 'f1', RB, [('f1', 'ls /etc/hostname /nope', 'Two streams, one screen', ACC), ('f2', '> out.txt', 'Out to a file', GOOD), ('f3', 'cat out.txt', 'The saved output', VIO), ('f4', '2> err.txt', 'Errors to a file', WARN), ('f5', 'cat err.txt', 'The saved error', PINK)])
s_redir = _lab('Redirection', 'Send data to and from files.', 'd1', RB, [('d1', 'echo first > log.txt', '> replaces', ACC), ('d2', 'echo second >> log.txt', '>> appends', GOOD), ('d3', 'cat log.txt', 'Both lines', VIO), ('d4', 'wc -l < log.txt', '< feeds input', WARN), ('d5', '2> /dev/null', 'Throw errors away', PINK), ('d6', 'echo $?', 'Exit status', BAD)])
s_pipes = _lab('Pipes and tee', 'One command feeds the next.', 'q1', RB, [('q1', 'cat app.log', 'The log', ACC), ('q2', '| grep ERROR', 'Filter', GOOD), ('q3', '| wc -l', 'Count', VIO), ('q4', '| tee errors.txt |', 'Save a copy', WARN), ('q5', 'cat errors.txt', 'The copy', PINK)])
s_tmp = _lab('Safe temporary files', 'Random name, private, removed.', 't1', RB, [('t1', 'f=$(mktemp)', 'Ask for a safe name', ACC), ('t2', 'echo "$f"', 'Random name', GOOD), ('t3', 'grep ERROR app.log > "$f"', 'Use it', VIO), ('t4', 'wc -l < "$f"', 'Read it', WARN), ('t5', 'rm "$f"', 'Clean up', PINK), ('t6', 'ls "$f"', 'Gone', BAD)])
s_build = _lab('Put it together', 'Report to a file, errors apart.', 'w1', RB, [('w1', 'cat app.log', 'The log', ACC), ('w2', '... | uniq -c > out.txt', 'Save the report', GOOD), ('w3', 'cat out.txt', 'The report', VIO), ('w4', '2> problems.txt', 'Errors apart', WARN), ('w5', 'cat problems.txt', 'The problems', PINK)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: > adds to a file', 'It replaces. Use >> to add.', 'my2'), ('Myth: pipes carry errors', 'Standard out only. Use 2>.', 'my3'), ('Myth: /dev/null stores it', 'It discards everything.', 'my4'), ('Myth: fixed /tmp names', 'Predictable. Use mktemp.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Streams. Redirects. Pipes. Safe temp files.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Streams 0, 1, 2', 'b2'), ('> >> and <', 'b3'), ('2> and /dev/null', 'b4'), ('Pipe and tee', 'b5'), ('mktemp and rm', 'b6'), ('Exit status $?', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  Streams', 'both on screen', PINK, 'z2'), ('2  > >> <', 'write, append, count', ACC, 'z3'), ('3  2>', 'file, null, status', WARN, 'z4'), ('4  Pipe + tee', 'save a copy', VIO, 'z5'), ('5  mktemp', 'use, read, remove', BAD, 'z6'), ('6  Report', 'results and errors apart', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which number is standard error?', 'f12'), ('> versus >> ?', 'f13'), ('Does a pipe carry errors?', 'f14'), ('Which command makes a safe temp file?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O05', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: errors, traps and exit codes', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'streams': s_streams, 'redir': s_redir, 'pipes': s_pipes, 'tmp': s_tmp, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'streams': ('question', ACC), 'redir': ('board', VIO), 'pipes': ('gear', WARN), 'tmp': ('gear', GOOD), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'streams': [('f2', 1, 1, 4, 790, ''), ('f2', 2, 1, 4, 205, ''), ('f3', 1, 1, 4, 790, ''), ('f4', 1, 1, 4, 205, ''), ('f5', 1, 1, 4, 205, ''), ('f6', 1, 1, 4, 790, '')],
 'redir': [('d4', 1, 2, 4, 95, ''), ('d5', 1, 1, 4, 22, ''), ('d7', 1, 1, 4, 22, '')],
 'pipes': [('q3', 1, 2, 4, 640, ''), ('q4', 1, 1, 4, 22, ''), ('q5', 1, 1, 4, 22, ''), ('q6', 1, 2, 4, 640, '')],
 'tmp': [('t3', 1, 1, 4, 325, ''), ('t5', 1, 1, 4, 22, ''), ('t7', 1, 1, 4, 1000, '')],
 'build': [('w4', 1, 3, 4, 200, ''), ('w5', 1, 1, 4, 145, ''), ('w6', 1, 1, 4, 840, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson41/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
