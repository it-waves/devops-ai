def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Decide, repeat, reuse', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('if / test', 'make a decision', ACC), ('case', 'pick one of many', VIO), ('for / while', 'repeat work', WARN), ('function', 'reuse a block', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Scripts that think.', 880, C['h3'], GOOD, 1700)); return E
s_if = _lab('If and else', 'A test picks a branch.', 'd1', RB, [('d1', 'cat age.sh', 'if / else', ACC), ('d2', './age.sh 20', 'Test true: adult', GOOD), ('d3', './age.sh 10', 'Test false: minor', VIO), ('d4', '[ 5 -gt 3 ]; echo $?', '0 means true', WARN), ('d5', '[ 5 -gt 9 ]; echo $?', '1 means false', BAD)])
s_tests = _lab('Tests', 'Files, strings and numbers.', 'q1', RB, [('q1', '[ -f notes.txt ]', 'File exists', ACC), ('q2', '[ -d docs ]', 'Directory exists', GOOD), ('q3', '|| echo ...', 'Runs if test fails', VIO), ('q5', '[ "$name" = Sam ]', 'Strings: =', WARN), ('q6', '[ 7 -lt 10 ]', 'Numbers: -lt -gt -eq', PINK), ('q7', '[ $empty = x ]', 'Unquoted: error', BAD)])
s_case = _lab('The case statement', 'One value, many answers.', 'm1', RB, [('m1', 'cat menu.sh', 'case ... esac', ACC), ('m2', './menu.sh start', 'Pattern: start)', GOOD), ('m3', './menu.sh stop', 'Pattern: stop)', VIO), ('m4', './menu.sh jump', 'Pattern: *)  default', WARN)])
s_loops = _lab('For and while loops', 'Repeat work, then stop.', 'l1', RB, [('l1', 'cat for.sh', 'for name in list', ACC), ('l2', './for.sh', 'One round per word', GOOD), ('l3', 'for f in *.log', 'One round per file', VIO), ('l4', 'cat count.sh', 'while test', WARN), ('l5', './count.sh', 'Stops when false', PINK)])
s_func = _lab('Functions', 'A named block you can reuse.', 'u1', RB, [('u1', 'cat func.sh', 'name() { ... }', ACC), ('u2', './func.sh', 'Call with arguments', GOOD)])
s_build = _lab('Put it together', 'Function, test, loop, count.', 'w1', RB, [('w1', 'cat health.sh', 'Read the script', ACC), ('w2', './health.sh notes.txt app.log', 'All present', GOOD), ('w3', './health.sh notes.txt gone.txt', 'One missing', BAD)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: [ ] is syntax', 'It is a command: spaces required.', 'my2'), ('Myth: -eq is =', '-eq compares numbers, = compares text.', 'my3'), ('Myth: while stops alone', 'Only when its test turns false.', 'my4'), ('Myth: functions return text', 'They print text, and return a status.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Test it. Choose it. Repeat it. Reuse it.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('if and else', 'b2'), ('Three kinds of test', 'b3'), ('case with *', 'b4'), ('for and while', 'b5'), ('Functions', 'b6'), ('Combine them', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  if / else', 'age check', PINK, 'z2'), ('2  Tests', 'file, dir, text, number', ACC, 'z3'), ('3  case', 'start, stop, default', WARN, 'z4'), ('4  Loops', 'for, for *.log, while', VIO, 'z5'), ('5  Function', 'call it twice', BAD, 'z6'), ('6  Health check', 'found and missing', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What are [ ] really?', 'f12'), ('Which case pattern is the default?', 'f13'), ('What ends a while loop?', 'f14'), ('How do you pass values to a function?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O03', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: text processing', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'if': s_if, 'tests': s_tests, 'case': s_case, 'loops': s_loops, 'func': s_func, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'if': ('test', ACC), 'tests': ('question', WARN), 'case': ('board', VIO), 'loops': ('gear', GOOD), 'func': ('gear', ACC), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'if': [('d2', 3, 1, 4, 372, ''), ('d3', 1, 1, 4, 84, ''), ('d4', 1, 1, 4, 84, ''), ('d5', 1, 1, 4, 22, ''), ('d6', 1, 1, 4, 22, '')],
 'tests': [('q2', 1, 1, 4, 172, ''), ('q3', 1, 1, 4, 247, ''), ('q4', 1, 1, 4, 262, ''), ('q6', 1, 1, 4, 141, ''), ('q7', 1, 1, 4, 202, ''), ('q8', 1, 1, 4, 552, ''), ('q9', 1, 1, 4, 217, '')],
 'case': [('m2', 3, 3, 4, 600, ''), ('m3', 1, 1, 4, 126, ''), ('m4', 1, 1, 4, 126, ''), ('m5', 1, 1, 4, 416, '')],
 'loops': [('l2', 2, 2, 4, 432, ''), ('l3', 1, 3, 4, 220, ''), ('l4', 1, 2, 4, 205, ''), ('l5', 3, 1, 4, 388, ''), ('l5', 5, 1, 4, 190, ''), ('l6', 1, 3, 4, 112, '')],
 'func': [('u2', 2, 3, 4, 300, ''), ('u3', 1, 3, 4, 250, '')],
 'build': [('w2', 11, 3, 4, 285, ''), ('w3', 1, 3, 4, 220, ''), ('w4', 1, 3, 4, 220, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson39/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
