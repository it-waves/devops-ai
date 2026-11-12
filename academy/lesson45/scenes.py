def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Deploy, check, roll back', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Release', 'a new version, one switch', ACC), ('Health check', 'is it really working?', VIO), ('Rollback', 'back to the last good one', WARN), ('Repeatable', 'same steps every time', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Never leave a broken release live.', 880, C['h3'], GOOD, 1700)); return E
s_layout = _lab('Releases and a link', 'One folder per version.', 'l1', RB, [('l1', 'ls releases', 'v1, v2, v3', ACC), ('l2', 'ls -l current', 'The live version', VIO), ('l3', 'curl .../version', 'Which version is live', GOOD), ('l4', 'curl -f .../health', 'Health: ok', WARN)])
s_script = _lab('The deploy script', 'Switch, check, roll back.', 'sc1', RB, [('sc1', 'cat release.sh', 'Switch, check, roll back', ACC), ('sc2', 'shellcheck release.sh', 'Clean', GOOD)])
s_deploy = _lab('A good deploy', 'Release v2 and prove it.', 'd1', RB, [('d1', 'bash release.sh v2', 'deployed v2', GOOD), ('d2', 'curl .../version', 'v2 is live', ACC), ('d3', 'readlink current', 'releases/v2', VIO), ('d4', 'bash release.sh v2', 'Repeat is harmless', WARN)])
s_rollback = _lab('A bad deploy', 'The script rolls back.', 'r1', RB, [('r1', 'bash release.sh v3', 'Health check fails', BAD), ('r2', 'echo $?', 'Exit code: 1', WARN), ('r3', 'curl .../version', 'Still v2', GOOD), ('r4', 'readlink current', 'releases/v2', VIO), ('r5', 'bash release.sh v1', 'Manual rollback', ACC), ('r6', 'curl .../version', 'v1 is live', PINK)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: script ended = worked', 'Only a health check proves it.', 'my2'), ('Myth: rollback needs a backup', 'Move the link to the old one.', 'my3'), ('Myth: happy path is enough', 'Plan and test the failure.', 'my4'), ('Myth: health checks are complex', 'Start with one simple request.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Release. Check. Roll back.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('One folder per release', 'b2'), ('Switch the link', 'b3'), ('Health check after deploy', 'b4'), ('Automatic rollback', 'b5'), ('Exit non-zero on failure', 'b6'), ('Test a bad release', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  releases', '3 folders + link', PINK, 'z2'), ('2  server', 'python3 -m http.server', ACC, 'z3'), ('3  script', 'check + rollback', WARN, 'z4'), ('4  good deploy', 'prove it with curl', VIO, 'z5'), ('5  bad deploy', 'watch it roll back', BAD, 'z6'), ('6  clean up', 'exit code, stop server', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why one folder per release?', 'f12'), ('What proves a deploy worked?', 'f13'), ('What if the health check fails?', 'f14'), ('How does rollback work here?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O09', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: the Bash scripting mastery scenario', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'layout': s_layout, 'script': s_script, 'deploy': s_deploy, 'rollback': s_rollback, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'layout': ('board', ACC), 'script': ('test', VIO), 'deploy': ('gear', GOOD), 'rollback': ('question', BAD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'layout': [('l2', 1, 1, 4, 162, ''), ('l3', 1, 1, 4, 1028, ''), ('l4', 1, 1, 4, 50, ''), ('l5', 1, 1, 4, 50, '')],
 'script': [('sc2', 4, 1, 4, 478, ''), ('sc2', 5, 1, 4, 480, ''), ('sc2', 6, 1, 4, 790, ''), ('sc2', 10, 1, 4, 385, ''), ('sc3', 1, 1, 4, 85, '')],
 'deploy': [('d2', 1, 1, 4, 190, ''), ('d3', 1, 1, 4, 50, ''), ('d4', 1, 1, 4, 175, ''), ('d5', 1, 1, 4, 190, '')],
 'rollback': [('r2', 1, 2, 4, 725, ''), ('r3', 1, 1, 4, 22, ''), ('r4', 1, 1, 4, 50, ''), ('r5', 1, 1, 4, 175, ''), ('r6', 1, 1, 4, 190, ''), ('r7', 1, 1, 4, 50, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson45/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
