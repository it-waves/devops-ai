def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Safe scripts, safe systems', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Secrets', 'never inside the script', ACC), ('Permissions', 'least access, chmod 600', VIO), ('Validation', 'allow only what you expect', WARN), ('Injection', 'input is never code', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Least access. Trust no input.', 880, C['h3'], GOOD, 1700)); return E
s_secrets = _lab('Keep secrets out', 'Fake secrets only, made up for this lesson.', 'se1', RB, [('se1', 'cat bad.sh', 'Password in the script', BAD), ('se2', 'ls -l .env', 'Anyone can read it', WARN), ('se3', 'chmod 600 .env', 'Owner only', ACC), ('se4', 'ls -l .env', 'Now private', GOOD), ('se5', 'cat good.sh', 'Loads it with source', VIO), ('se6', 'bash good.sh', 'Last four characters only', PINK)])
s_perms = _lab('Permissions', 'Give only what is needed.', 'pe1', RB, [('pe1', 'ls -l deploy.sh', 'No x: not executable', ACC), ('pe2', './deploy.sh', 'Permission denied', BAD), ('pe3', 'chmod u+x deploy.sh', 'Execute for the owner', GOOD), ('pe4', 'ls -l deploy.sh', 'rwx for the owner', VIO), ('pe5', './deploy.sh', 'Now it runs', PINK), ('pe6', 'umask 077', 'New files stay private', WARN)])
s_validate = _lab('Validate input', 'Allow what you expect. Refuse the rest.', 'va1', RB, [('va1', 'cat validate.sh', 'A regular expression', ACC), ('va2', 'validate.sh web01', 'Accepted', GOOD), ('va3', 'validate.sh hostile', 'Refused', BAD), ('va4', 'echo $?', 'Exit code: 2', WARN), ('va5', 'validate.sh ../etc', 'Refused too', VIO)])
s_inject = _lab('Injection', 'Input must never become code.', 'in1', RB, [('in1', 'cat danger.sh', 'Uses eval on input', BAD), ('in2', 'bash danger.sh ...', 'The hidden command ran', WARN), ('in3', 'cat quoted.sh', 'Quoted, no eval', GOOD), ('in4', 'bash quoted.sh ...', 'Treated as a name only', ACC)])
s_build = _lab('Put it together', 'One safer script.', 'bu1', RB, [('bu1', 'cat secure.sh', 'All four habits', ACC), ('bu2', 'bash secure.sh web01', 'Works, secret hidden', GOOD), ('bu3', 'secure.sh "web01; id"', 'Refused', BAD), ('bu4', 'echo $?', 'Exit code: 2', WARN)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: private repo is safe', 'Keep secrets out of code.', 'my2'), ('Myth: chmod 777 fixes it', 'Grant only what is needed.', 'my3'), ('Myth: quotes are optional', 'Quote every variable.', 'my4'), ('Myth: block the bad input', 'Allow only the expected.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Secrets. Permissions. Validation. No eval.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Secrets in a 600 file', 'b2'), ('chmod, never 777', 'b3'), ('umask 077', 'b4'), ('Allow-list validation', 'b5'), ('Quote, no eval', 'b6'), ('Never print secrets', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  .env 600', 'fake token, locked', PINK, 'z2'), ('2  source', 'last four only', ACC, 'z3'), ('3  chmod u+x', 'owner only', WARN, 'z4'), ('4  umask 077', 'private files', VIO, 'z5'), ('5  validate', 'refuse a semicolon', BAD, 'z6'), ('6  quote', 'no eval, no code', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Where does a password belong?', 'f12'), ('Which mode locks a secret file?', 'f13'), ('What does an allow list do?', 'f14'), ('Why avoid eval on input?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: idempotent scripts and ShellCheck', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'secrets': s_secrets, 'perms': s_perms, 'validate': s_validate, 'inject': s_inject, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'secrets': ('gear', ACC), 'perms': ('test', VIO), 'validate': ('question', WARN), 'inject': ('board', BAD), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'secrets': [('se2', 2, 1, 4, 270, ''), ('se3', 1, 1, 4, 160, ''), ('se5', 1, 1, 4, 160, ''), ('se6', 3, 1, 4, 210, ''), ('se7', 1, 1, 4, 285, '')],
 'perms': [('pe2', 1, 1, 4, 160, ''), ('pe3', 1, 1, 4, 560, ''), ('pe5', 1, 1, 4, 160, ''), ('pe6', 1, 1, 4, 145, ''), ('pe7', 1, 1, 4, 160, '')],
 'validate': [('va2', 3, 1, 4, 355, ''), ('va2', 4, 1, 4, 795, ''), ('va3', 1, 1, 4, 220, ''), ('va4', 1, 1, 4, 115, ''), ('va5', 1, 1, 4, 22, ''), ('va6', 1, 1, 4, 115, '')],
 'inject': [('in2', 2, 1, 4, 235, ''), ('in3', 2, 1, 4, 130, ''), ('in4', 2, 1, 4, 205, ''), ('in5', 1, 1, 4, 1055, '')],
 'build': [('bu2', 3, 1, 4, 145, ''), ('bu2', 5, 1, 4, 825, ''), ('bu2', 6, 1, 4, 210, ''), ('bu2', 7, 1, 4, 595, ''), ('bu3', 1, 1, 4, 445, ''), ('bu4', 1, 1, 4, 115, ''), ('bu5', 1, 1, 4, 22, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson43/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
