def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def s_hook(C, D, dur):
    E = [El(T('Control what goes into Git', 'x', 72), 100, 130, C['y1'])]
    E.append(Pop(card(1100, 140, BAD, 'secrets.env', [('committed, pushed, now in history forever', TXT)], 44, 32), 100, 290, C['y1'] + 3.0))
    for i, (a, b, col) in enumerate([('Staging', 'one clean change per commit', ACC), ('History', 'who changed what, and why', VIO), ('Ignore files', 'junk and secrets stay out', GOOD)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 470 + i * 150, C['y3'] + i * 3.5))
    E.append(takeaway('Lab and checker at the end.', 960, C['y4'], GOOD, 1700)); return E
def s_flow(C, D, dur):
    E = head('Three snapshots', 'Each diff command compares two of them.', C['d1']); E.append(ill(C['d1'] + 0.2, 1400, 170))
    it = [('Working tree', 'files you edit', ACC, 560), ('Staging area', 'the next commit', VIO, 1020), ('Last commit', 'HEAD', GOOD, 1480)]
    for i, (n, s_, col, x) in enumerate(it): E.append(Pop(card(380, 170, col, n, [(s_, TXT)], 38, 30), x - 460, 340, C['d1'] + i * 0.4))
    E.append(Pop(chip('git diff', ACC, 30, 16, 8), 130, 560, C['d2'])); E.append(El(T('working tree  vs  staging area', 'm', 30, TXT, align='left'), 350, 566, C['d2'] + 0.3, anim='fade'))
    E.append(Pop(chip('git diff --staged', VIO, 30, 16, 8), 130, 660, C['d3'])); E.append(El(T('staging area  vs  last commit  =  what you will commit', 'm', 30, TXT, align='left'), 600, 666, C['d3'] + 0.3, anim='fade'))
    E.append(Pop(chip('git diff HEAD', GOOD, 30, 16, 8), 130, 760, C['d4'])); E.append(El(T('working tree  vs  last commit', 'm', 30, TXT, align='left'), 440, 766, C['d4'] + 0.3, anim='fade'))
    E.append(takeaway('Before every commit: git diff --staged', 900, C['d5'], WARN, 1700)); return E
s_stage = _lab('Stage with confidence', 'Status, diff, add, restore.', 's1', RB, [('s2', 'git status -s', 'Two columns', ACC), ('s3', 'git diff', 'Not staged yet', WARN), ('s4', 'git add', 'Stage one file', VIO), ('s6', 'diff --staged', 'The next commit', GOOD), ('s8', 'git restore --staged', 'Unstage, edit kept', PINK)])
def s_msg(C, D, dur):
    E = head('Good commit messages', 'A history others can read.', C['m1']); E.append(ill(C['m1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 150, GOOD, '1  Subject', [('about 50 characters, imperative:  Add stylesheet', TXT)], 40, 32), 100, 330, C['m2']))
    E.append(Pop(card(1700, 150, VIO, '2  Body (optional)', [('blank line first; explain why, not what', TXT)], 40, 32), 100, 510, C['m3']))
    E.append(Pop(card(1700, 150, WARN, '3  One logical change', [('if the subject needs "and", it is two commits', TXT)], 40, 32), 100, 690, C['m4']))
    E.append(Pop(card(820, 110, BAD, 'Bad', [('fix   |   stuff   |   wip', TXT)], 32, 30), 100, 880, C['m5'])); E.append(Pop(card(820, 110, GOOD, 'Good', [('Fix port typo in app.conf', TXT)], 32, 30), 980, 880, C['m5'] + 1.0)); return E
s_hist = _lab('Read the history', 'Log, show, file history, blame.', 'h1', RB, [('h2', 'log --oneline', 'Compact view', ACC), ('h3', 'log -n 2', 'Who, when, why', VIO), ('h4', 'show --stat HEAD', 'What changed', GOOD), ('h5', 'log -- file', 'One file only', WARN), ('h6', 'show HEAD~3:file', 'The file in the past', PINK), ('h7', 'git blame', 'Last change per line', ACC)])
s_ignore = _lab('Ignore files', 'Keep junk and secrets out.', 'g1', RB, [('g3', '.gitignore', 'Patterns, one per line', ACC), ('g6', 'check-ignore -v', 'Which rule matched', VIO), ('g8', 'still modified', 'Tracked files ignore ignores', WARN), ('g9', 'rm --cached', 'Untrack, keep on disk', GOOD)])
def s_task(C, D, dur):
    E = head('Your lab task', 'lab58.sh builds it. lab check judges it.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['t2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab58.sh', 'mono', 32, TXT, align='left'), 140, 360, C['t2'] + 0.3, anim='fade'))
    steps = [('lab up', 'a repo with junk and a mistake', 't3', ACC), ('1  .gitignore', 'debug.log, secrets.env, build/', 't4', VIO), ('2  untrack', 'cache.tmp, keep the file', 't5', WARN), ('3  commit', 'only app.conf, clear message', 't6', PINK), ('4  answers.txt', 'commits before yours', 't7', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540 if i < 3 else 830, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590 if i < 3 else 100 + (i - 3) * 880, 470 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Review: git diff --staged', 930, C['t8'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Four PASS lines', 'b2'), ('diff --staged first', 'b3'), ('Clear commit message', 'b4'), ('Tracked files, ignore', 'b5'), ('Answer number right', 'b6'), ('lab down, removed', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Ignore', '.gitignore + check-ignore', ACC, 'z3'), ('3  Untrack', 'git rm --cached', WARN, 'z4'), ('4  Commit', 'only app.conf', VIO, 'z5'), ('5  Check', 'answers.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command shows the next commit?', 'f12'), ('How do you unstage a file?', 'f13'), ('Why does ignoring a tracked file fail?', 'f14'), ('How do you follow one file?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC07-O02', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: branches, merging, conflicts', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, flow=s_flow, stage=s_stage, msg=s_msg, hist=s_hist, ignore=s_ignore, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(flow=('board', ACC), stage=('code', GOOD), msg=('doc', WARN), hist=('eye', VIO), ignore=('test', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson58/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
