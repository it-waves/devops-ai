def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Fail safely, leave a record', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Exit codes', '0 is success', ACC), ('Strict mode', 'set -euo pipefail', VIO), ('Traps', 'clean up on EXIT', WARN), ('Logging', 'timestamps on stderr', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Stop. Clean up. Tell the truth.', 880, C['h3'], GOOD, 1700)); return E
s_exitcodes = _lab('Exit codes', 'Zero is success, anything else fails.', 'e1', RB, [('e1', 'ls /etc/hostname', 'A command that works', ACC), ('e2', 'echo $?', 'Exit code: 0', GOOD), ('e3', 'ls /nope', 'A command that fails', BAD), ('e4', 'echo $?', 'Exit code: 2', WARN), ('e5', 'cat check.sh', 'exit 1 if ERROR found', VIO), ('e6', 'bash check.sh', 'Run the script', PINK), ('e7', 'echo $?', 'Exit code: 1', WARN)])
s_strict = _lab('Strict mode', 'Stop at the first failure.', 's1', RB, [('s1', 'cat loose.sh', 'No safety net', ACC), ('s2', 'bash loose.sh', 'Carries on after an error', BAD), ('s3', 'cat strict.sh', 'set -euo pipefail', GOOD), ('s4', 'bash strict.sh', 'Stops at the cd', VIO), ('s5', 'echo $?', 'Exit code: 1', WARN), ('s6', 'cat unset.sh', 'set -u', PINK), ('s7', 'bash unset.sh', 'Unbound variable', BAD)])
s_trap = _lab('Clean up with trap', 'Runs however the script ends.', 't1', RB, [('t1', 'cat trap.sh', 'trap ... EXIT', ACC), ('t2', 'bash trap.sh', 'Fails, then cleans up', GOOD), ('t3', 'echo $?', 'Still a failure: 1', WARN), ('t4', 'ls /tmp', 'Nothing left behind', VIO)])
s_logging = _lab('Logging', 'Timestamps on standard error.', 'l1', RB, [('l1', 'cat log.sh', 'A log function', ACC), ('l2', 'bash log.sh', 'Time, level, message', GOOD), ('l3', '2> run.log', 'Logs to a file', VIO), ('l4', 'cat run.log', 'The record', WARN)])
s_build = _lab('Put it together', 'One safe script.', 'w1', RB, [('w1', 'cat safe.sh', 'Strict, trap, exit code', ACC), ('w2', 'bash safe.sh', '|| true allows no match', GOOD), ('w3', 'echo $?', 'Exit code: 1', WARN)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: exit 0 means failure', 'Zero means success.', 'my2'), ('Myth: set -e catches all', 'Not in if tests or after ||.', 'my3'), ('Myth: trap is for Ctrl-C', 'EXIT runs on every exit.', 'my4'), ('Myth: logs go to stdout', 'Logs go to stderr.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Exit codes. Strict mode. Traps. Logs.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Read $?', 'b2'), ('exit N', 'b3'), ('set -euo pipefail', 'b4'), ('trap ... EXIT', 'b5'), ('Timestamped logs', 'b6'), ('|| true', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  $?', 'works and fails', PINK, 'z2'), ('2  exit', '0 or 1 by a test', ACC, 'z3'), ('3  set -euo', 'prove it stops', WARN, 'z4'), ('4  trap', 'no temp left', VIO, 'z5'), ('5  log', 'timestamps to a file', BAD, 'z6'), ('6  || true', 'survive no match', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which exit code means success?', 'f12'), ('What does set -u do?', 'f13'), ('When does a trap on EXIT run?', 'f14'), ('Where do log messages go?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O06', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: secrets and safe input', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'exitcodes': s_exitcodes, 'strict': s_strict, 'trap': s_trap, 'logging': s_logging, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'exitcodes': ('question', ACC), 'strict': ('test', VIO), 'trap': ('gear', WARN), 'logging': ('board', GOOD), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'exitcodes': [('e2', 1, 1, 4, 205, ''), ('e3', 1, 1, 4, 22, ''), ('e4', 1, 1, 4, 790, ''), ('e5', 1, 1, 4, 22, ''), ('e6', 4, 1, 4, 125, ''), ('e7', 1, 1, 4, 190, ''), ('e8', 1, 1, 4, 22, '')],
 'strict': [('s3', 1, 1, 4, 900, ''), ('s3', 3, 1, 4, 240, ''), ('s4', 2, 1, 4, 260, ''), ('s5', 1, 1, 4, 840, ''), ('s6', 1, 1, 4, 22, ''), ('s7', 2, 1, 4, 100, ''), ('s8', 1, 1, 4, 610, '')],
 'trap': [('t2', 4, 1, 4, 630, ''), ('t3', 2, 1, 4, 160, ''), ('t4', 1, 1, 4, 22, '')],
 'logging': [('l2', 2, 1, 4, 655, ''), ('l3', 1, 2, 4, 400, ''), ('l5', 1, 2, 4, 400, '')],
 'build': [('w2', 5, 1, 4, 535, ''), ('w3', 1, 1, 4, 145, ''), ('w4', 1, 1, 4, 22, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson42/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
