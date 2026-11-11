def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Run it twice, safely', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Idempotent', 'same result every run', ACC), ('Check first', 'then change', VIO), ('ShellCheck', 'finds bugs before you run', WARN), ('Prove it', 'run it twice', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Same result. Every run.', 880, C['h3'], GOOD, 1700)); return E
s_idem = _lab('Why repeats break', 'A script that is not idempotent.', 'id1', RB, [('id1', 'cat bad.sh', 'mkdir and >>', ACC), ('id2', 'bash bad.sh', 'First run: fine', GOOD), ('id3', 'bash bad.sh', 'Second run: error', BAD), ('id4', 'cat app.conf', 'Line is duplicated', WARN)])
s_fix = _lab('Idempotent version', 'Same result every run.', 'g1', RB, [('g1', 'cat good.sh', 'mkdir -p and grep', ACC), ('g2', 'bash good.sh', 'First run', GOOD), ('g3', 'bash good.sh', 'Second run: silent', VIO), ('g4', 'cat app.conf', 'Still one line', WARN)])
s_state = _lab('Repeat-safe commands', 'Built-in idempotent switches.', 'st1', RB, [('st1', 'mkdir -p twice', 'Exit code: 0', ACC), ('st2', 'rm -f missing file', 'Exit code: 0', GOOD), ('st3', 'ln -sfn twice', 'One link, no error', VIO)])
s_finds = _lab('ShellCheck', 'Find mistakes before you run.', 'fi1', RB, [('fi1', 'cat typo.sh', 'nmae, not name', ACC), ('fi2', 'shellcheck typo.sh', 'SC2154 reported', BAD), ('fi3', 'echo $?', 'Exit code: 1', WARN)])
s_fixes = _lab('Fix with ShellCheck', 'Let the diff show the fix.', 'd1', RB, [('d1', 'cat buggy.sh', 'Unquoted $f', ACC), ('d2', 'shellcheck -f diff', 'Shows the fix', VIO), ('d3', '... | patch', 'Applies the fix', GOOD), ('d4', 'cat buggy.sh', 'Quotes added', PINK), ('d5', 'shellcheck && echo', 'Clean', WARN)])
s_build = _lab('Put it together', 'Idempotent and clean.', 'bu1', RB, [('bu1', 'cat site.sh', 'Folder, setting, link', ACC), ('bu2', 'shellcheck site.sh', 'Clean', GOOD), ('bu3', 'bash site.sh', 'First run', VIO), ('bu4', 'run again, wc -l', 'Still one line', WARN)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: it worked once, so fine', 'Run it twice to be sure.', 'my2'), ('Myth: ShellCheck finds all', 'It cannot know your intent.', 'my3'), ('Myth: lint clean is safe', 'Test on a copy first.', 'my4'), ('Myth: idempotent is idle', 'Work once, then no change.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Same result. Check first. Lint first.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Idempotent in one line', 'b2'), ('mkdir -p, rm -f, ln -sfn', 'b3'), ('Check before you change', 'b4'), ('Read ShellCheck output', 'b5'), ('Fix until clean', 'b6'), ('Prove it: run twice', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  run twice', 'see it break', PINK, 'z2'), ('2  fix it', 'mkdir -p + grep', ACC, 'z3'), ('3  safe forms', 'rm -f, ln -sfn', WARN, 'z4'), ('4  typo', 'let ShellCheck find it', VIO, 'z5'), ('5  quotes', 'diff and patch', BAD, 'z6'), ('6  your script', 'fix every finding', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does idempotent mean?', 'f12'), ('Which flag makes mkdir repeatable?', 'f13'), ('Exit code when ShellCheck finds issues?', 'f14'), ('How do you prove idempotence?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O08', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: deploy, health check, rollback', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'idem': s_idem, 'fix': s_fix, 'state': s_state, 'finds': s_finds, 'fixes': s_fixes, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'idem': ('gear', BAD), 'fix': ('test', GOOD), 'state': ('board', VIO), 'finds': ('question', WARN), 'fixes': ('test', ACC), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'idem': [('id2', 2, 2, 4, 480, ''), ('id4', 1, 1, 4, 810, ''), ('id5', 1, 2, 4, 200, '')],
 'fix': [('g2', 3, 1, 4, 250, ''), ('g2', 5, 1, 4, 810, ''), ('g5', 1, 1, 4, 190, '')],
 'state': [('st2', 1, 1, 4, 22, ''), ('st3', 1, 1, 4, 22, ''), ('st4', 1, 1, 4, 840, '')],
 'finds': [('fi2', 3, 1, 4, 190, ''), ('fi3', 4, 1, 4, 1010, ''), ('fi4', 1, 1, 4, 22, '')],
 'fixes': [('d2', 3, 2, 4, 150, ''), ('d3', 6, 2, 4, 160, ''), ('d3', 8, 2, 4, 190, ''), ('d4', 1, 1, 4, 340, ''), ('d5', 3, 2, 4, 190, ''), ('d6', 1, 1, 4, 85, '')],
 'build': [('bu2', 3, 1, 4, 285, ''), ('bu2', 5, 1, 4, 985, ''), ('bu2', 6, 1, 4, 315, ''), ('bu3', 1, 1, 4, 85, ''), ('bu4', 1, 1, 4, 115, ''), ('bu5', 2, 1, 4, 250, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson44/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
