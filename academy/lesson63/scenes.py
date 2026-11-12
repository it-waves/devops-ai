def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h



def s_hook(C, D, dur):
    E = [El(T('Undo anything in Git', 'x', 72), 100, 130, C['y1'])]
    E.append(Pop(card(1100, 140, BAD, 'Something went wrong', [('a bad edit, a wrong commit, a regretted reset', TXT)], 44, 32), 100, 290, C['y1'] + 2.0))
    for i, (a, b, col) in enumerate([('restore', 'undo an uncommitted edit', ACC), ('revert', 'safely cancel a shared commit', VIO), ('reset + reflog', 'move back, and recover', GOOD)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 470 + i * 150, C['y2'] + i * 2.5))
    E.append(takeaway('Lab and checker at the end.', 960, C['y4'], GOOD, 1700)); return E
def s_model(C, D, dur):
    E = head('Which undo to use', 'First question: where is the mistake?', C['d1']); E.append(ill(C['d1'] + 0.2, 1400, 170))
    for i, (n, s_, col, cid) in enumerate([('Working folder', 'where you edit', ACC, 'd1'), ('Staging area', 'the next commit, prepared', VIO, 'd1'), ('History', 'the commits themselves', GOOD, 'd1')]):
        E.append(Pop(card(540, 150, col, n, [(s_, TXT)], 40, 28), 100 + i * 590, 340, C[cid] + 1.5 + i * 3.0))
    it = [('git restore', 'file edit not committed: put the file back', ACC, 'd3'), ('git revert', 'shared commit: add a new commit that cancels it', VIO, 'd4'), ('git reset', 'private commits: move the branch back', WARN, 'd5'), ('git reflog', 'lost something? the diary of where HEAD has been', GOOD, 'd6')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 105, col, n, [(s_, TXT)], 38, 30), 100, 540 + i * 125, C[cid]))
    return E
s_restore = _lab('Restore files', 'Discard edits, unstage, or take an old version.', 'rs1', RB, [('rs3', 'status -s', 'M in the 2nd column: unstaged', WARN), ('rs4', 'git restore FILE', 'Discards the edit', ACC), ('rs8', 'restore --staged', 'Out of staging, edit kept', VIO), ('rs11', '--source=HEAD~2', 'File from an older commit', GOOD)])
s_revert = _lab('Revert a shared commit', 'A new commit that cancels the bad one.', 'rv1', RB, [('rv2', 'git log', 'The bad commit is last', BAD), ('rv3', 'git revert HEAD', 'Adds a cancelling commit', VIO), ('rv4', 'git log', 'History kept, honest', GOOD), ('rv5', 'cat index.html', 'The ports line is back', ACC)])
s_reset = _lab('Reset: soft, mixed, hard', 'Move the branch back. Know what survives.', 'rt1', RB, [('rt3', 'reset --soft', 'Commit gone, change staged', ACC), ('rt5', 'git reset', 'Mixed: change in the file only', VIO), ('rt7', 'reset --hard', 'Throws the work away', BAD), ('rt8', 'git log', 'Head is at the older commit', GOOD)])
s_reflog = _lab('The reflog safety net', 'A diary of where HEAD has been.', 'rl1', RB, [('rl2', 'reset --hard HEAD~2', 'The slip', BAD), ('rl3', 'git log', 'Two commits vanished', WARN), ('rl4', 'git reflog', 'Every move of HEAD', VIO), ('rl5', 'reset --hard HEAD@{1}', 'Jump back', ACC), ('rl6', 'git log', 'All five commits are back', GOOD)])
def s_task(C, D, dur):
    E = head('Your lab task', 'lab63.sh builds the mess. lab check judges it.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['t2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab63.sh', 'mono', 32, TXT, align='left'), 140, 360, C['t2'] + 0.3, anim='fade'))
    steps = [('lab up', 'junk edit, shared bad commit, a lost commit', 't3', ACC), ('1  restore', 'start.sh back to clean', 't4', VIO), ('2  reflog', 'recover Add retry setting', 't5', WARN), ('3  revert', 'Add debug flag, no rewrite', 't6', PINK), ('4  answers.txt', 'commits on main now', 't7', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540 if i < 3 else 830, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590 if i < 3 else 100 + (i - 3) * 880, 470 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Restore, revert, reflog.', 930, C['t8'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['rb1'])
    items = [('Four PASS lines', 'rb2'), ('Reverted, not reset', 'rb3'), ('Lost commit recovered', 'rb4'), ('Restore, revert, reset', 'rb5'), ('Answer number right', 'rb6'), ('lab down, removed', 'rb7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['rb8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Restore', 'the junk file', ACC, 'z3'), ('3  Reflog', 'recover the lost commit', WARN, 'z4'), ('4  Revert', 'the debug flag commit', VIO, 'z5'), ('5  Check', 'answers.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command undoes an uncommitted edit?', 'f12'), ('Why revert, not reset, when shared?', 'f13'), ('Soft, mixed and hard: the difference?', 'f14'), ('Recovering after a bad hard reset?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC07-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: secrets and repository access', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, model=s_model, restore=s_restore, revert=s_revert, reset=s_reset, reflog=s_reflog, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(model=('board', ACC), restore=('code', GOOD), revert=('eye', VIO), reset=('code', WARN), reflog=('doc', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson63/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
