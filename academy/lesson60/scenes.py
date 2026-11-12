def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h


def s_hook(C, D, dur):
    E = [El(T('Keep history a straight line', 'x', 72), 100, 130, C['y1'])]
    E.append(Pop(card(1100, 140, BAD, 'Merge, merge, merge', [('a tangled ball of string', TXT)], 44, 32), 100, 290, C['y1'] + 3.0))
    for i, (a, b, col) in enumerate([('Amend', 'fix your last commit', ACC), ('Rebase', 'replay work on the latest code', VIO), ('Golden rule', 'never rebase shared commits', WARN)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 470 + i * 150, C['y3'] + i * 3.5))
    E.append(takeaway('Lab and checker at the end.', 960, C['y4'], GOOD, 1700)); return E
def s_model(C, D, dur):
    E = head('Rebase versus merge', 'Two ways to combine diverged work.', C['d1']); E.append(ill(C['d1'] + 0.2, 1400, 170))
    for i in range(3): E.append(Pop(chip('main %d' % (i + 1), MUTED, 28, 16, 8), 130 + i * 260, 360, C['d1'] + i * 0.4))
    E.append(Pop(chip('f1', VIO, 28, 16, 8), 130 + 1 * 260, 470, C['d1'] + 1.2)); E.append(Pop(chip('f2', VIO, 28, 16, 8), 130 + 2 * 260, 470, C['d1'] + 1.6))
    E.append(Pop(card(820, 130, VIO, 'Merge', [('keeps real order; adds a merge commit', TXT)], 36, 28), 100, 600, C['d2']))
    E.append(Pop(card(820, 130, ACC, 'Rebase', [('replays your commits on top of main', TXT)], 36, 28), 980, 600, C['d3']))
    E.append(Pop(card(820, 130, GOOD, 'Result', [('a straight line, no merge commit', TXT)], 36, 28), 100, 760, C['d4']))
    E.append(Pop(card(820, 130, WARN, 'Catch', [('new commits, new hashes: history rewritten', TXT)], 36, 28), 980, 760, C['d5']))
    E.append(takeaway('Rebase and amend rewrite. Use on your own work.', 960, C['d6'], WARN, 1700)); return E
s_amend = _lab('Fix the last commit', 'Amend replaces the last commit.', 'am1', RB, [('am2', 'log --oneline', 'The lazy message', ACC), ('am3', 'commit --amend -m', 'Rewrite it', VIO), ('am4', 'log --oneline', 'Same spot, new hash', GOOD), ('am5', '--amend --no-edit', 'Add a forgotten file', WARN)])
s_rebase = _lab('Rebase onto main', 'Replay your commits on the latest code.', 'rb1', RB, [('rb2', 'log --graph --all', 'Diverged branches', ACC), ('rb3', 'git rebase main', 'Replay on top', VIO), ('rb4', 'straight line', 'New hashes', GOOD), ('rb6', 'git merge feature', 'Fast-forward', WARN)])
s_rconf = _lab('Rebase conflicts', 'Same fix, one commit at a time.', 'rc1', RB, [('rc2', 'git rebase main', 'CONFLICT, rebase stops', WARN), ('rc3', 'git status', 'Rebase in progress', ACC), ('rc4', 'cat app.conf', 'Sides are swapped', VIO), ('rc6', 'git add', 'Mark resolved', GOOD), ('rc7', 'rebase --continue', 'Next commit', GOOD)])
def s_golden(C, D, dur):
    E = head('The golden rule', 'Never rebase commits others already have.', C['g1']); E.append(ill(C['g1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 150, BAD, 'Why', [('rebase makes new commits; a teammate\'s copy no longer matches yours', TXT)], 40, 30), 100, 340, C['g2']))
    E.append(Pop(card(820, 190, GOOD, 'Private work', [('rebase freely before you share', TXT)], 44, 32), 100, 540, C['g3']))
    E.append(Pop(card(820, 190, VIO, 'Shared work', [('merge instead; it rewrites nothing', TXT)], 44, 32), 980, 540, C['g3'] + 1.5))
    E.append(takeaway('In doubt? Merge.', 880, C['g4'], WARN, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab60.sh builds it. lab check judges it.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['t2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab60.sh', 'mono', 32, TXT, align='left'), 140, 360, C['t2'] + 0.3, anim='fade'))
    steps = [('lab up', 'a feature branch whose last commit says wip', 't3', ACC), ('1  amend', 'a clear message on feature', 't4', VIO), ('2  rebase', 'feature onto main', 't5', WARN), ('3  merge', 'on main, no merge commit', 't6', PINK), ('4  answers.txt', 'commits on main now', 't7', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540 if i < 3 else 830, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590 if i < 3 else 100 + (i - 3) * 880, 470 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Only rebase your own unshared work.', 930, C['t8'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['rb9'])
    items = [('Four PASS lines', 'rb10'), ('Straight line, no merge', 'rb11'), ('Clear last message', 'rb12'), ('Why hashes change', 'rb13'), ('Answer number right', 'rb14'), ('lab down, removed', 'rb15')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['rb16'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Amend', 'the last commit message', ACC, 'z3'), ('3  Rebase', 'feature onto main', WARN, 'z4'), ('4  Merge', 'on main, fast-forward', VIO, 'z5'), ('5  Check', 'answers.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does rebase do to commits?', 'f12'), ('Why does amend change the hash?', 'f13'), ('Which commits are safe to rebase?', 'f14'), ('How do you back out of a rebase?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC07-O04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: remotes, push, pull, releases', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, model=s_model, amend=s_amend, rebase=s_rebase, rconf=s_rconf, golden=s_golden, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(model=('board', ACC), amend=('code', GOOD), rebase=('code', VIO), rconf=('test', GOOD), golden=('doc', WARN), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson60/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
