def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h

def s_hook(C, D, dur):
    E = [El(T('Work in parallel, safely', 'x', 72), 100, 130, C['y1'])]
    E.append(Pop(card(1100, 140, BAD, 'Same file, two people', [('one save overwrites the other', TXT)], 44, 32), 100, 290, C['y1'] + 3.0))
    for i, (a, b, col) in enumerate([('Branch', 'experiments stay safe', ACC), ('Merge', 'finished work comes home', VIO), ('Conflicts', 'a five minute job, not a disaster', GOOD)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 470 + i * 150, C['y3'] + i * 3.5))
    E.append(takeaway('Lab and checker at the end.', 960, C['y4'], GOOD, 1700)); return E
def s_model(C, D, dur):
    E = head('What a branch is', 'A name that points at a commit.', C['d1']); E.append(ill(C['d1'] + 0.2, 1400, 170))
    for i in range(4): E.append(Pop(chip('commit', MUTED, 30, 16, 8), 130 + i * 300, 420, C['d1'] + i * 0.5))
    E.append(Pop(chip('main', ACC, 34, 20, 10), 130 + 3 * 300, 540, C['d3'])); E.append(El(T('moves forward with every commit', 'm', 30, TXT, align='left'), 130, 640, C['d3'] + 0.3, anim='fade'))
    E.append(Pop(chip('feature', VIO, 34, 20, 10), 130 + 1 * 300, 300, C['d2'])); E.append(El(T('a branch is a pointer, nothing is copied', 'm', 30, TXT, align='left'), 130, 740, C['d2'] + 0.3, anim='fade'))
    E.append(Pop(chip('HEAD = you are here', WARN, 34, 20, 10), 130, 840, C['d4']))
    E.append(takeaway('Failed experiment? Delete the branch.', 960, C['d5'], GOOD, 1700)); return E
def s_kinds(C, D, dur):
    E = head('Three kinds of merge', 'What Git does when you merge.', C['e1']); E.append(ill(C['e1'] + 0.2, 1400, 170))
    it = [('Fast-forward', 'main has not moved: the pointer just slides, no new commit', GOOD, 'e2'), ('True merge', 'both moved, different places: a merge commit with two parents', VIO, 'e3'), ('Conflict', 'same lines changed: Git stops and asks you', WARN, 'e4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, f'{i + 1}  {n}', [(s_, TXT)], 40, 30), 100, 340 + i * 190, C[cid]))
    E.append(takeaway('Two of three need nothing from you.', 930, C['e5'], GOOD, 1700)); return E
s_branch = _lab('Create and switch branches', 'Branch, switch, commit, compare.', 'br1', RB, [('br2', 'git branch', 'List branches', ACC), ('br3', 'git switch -c', 'Create and switch', VIO), ('br6', 'git commit -am', 'Work on the branch', GOOD), ('br7', 'log --graph --all', 'See the shape', WARN), ('br8', 'git switch main', 'Files swap back', PINK)])
s_merge = _lab('Merge and clean up', 'Merge feature into main.', 'mg1', RB, [('mg2', 'log --graph --all', 'Two lines of work', ACC), ('mg3', 'git merge feature', 'Run it on main', VIO), ('mg4', 'merge commit', 'Two parents', GOOD), ('mg5', 'git branch -d', 'Delete when merged', WARN)])
def s_marks(C, D, dur):
    E = head('Conflict markers', 'What Git writes into the file.', C['x1']); E.append(ill(C['x1'] + 0.2, 1400, 170))
    rows = [('<<<<<<< HEAD', WARN), ('port=9090', TXT), ('=======', MUTED), ('port=8080', TXT), ('>>>>>>> feature', VIO)]
    mono_panel(E, 100, 340, 1000, rows, C['x1'] + 1.0, fs=40, lh=64)
    it = [('1  Decide', 'what the right result is', ACC, 'x3'), ('2  Delete markers', 'keep the right content', WARN, 'x3'), ('3  git add', 'mark it resolved', VIO, 'x3'), ('4  git commit', 'finish the merge', GOOD, 'x3')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(560, 100, col, n, [(s_, TXT)], 30, 24), 1260, 340 + i * 112, C[cid] + i * 1.2))
    E.append(Pop(badge('Not ready?  git merge --abort', F('b', 40), INK, PINK, padx=30, pady=16), 100, 880, C['x4'])); return E
s_conflict = _lab('Fix a real conflict', 'Merge, inspect, resolve, commit.', 'cf1', RB, [('cf2', 'git merge', 'CONFLICT, Git waits', WARN), ('cf3', 'status -s', 'UU = unmerged', ACC), ('cf4', 'merge --abort', 'The escape hatch', PINK), ('cf7', 'cat app.conf', 'See the markers', VIO), ('cf9', 'git add', 'Mark resolved', GOOD), ('cf10', 'git commit', 'Finish the merge', GOOD)])
def s_task(C, D, dur):
    E = head('Your lab task', 'lab59.sh builds it. lab check judges it.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['t2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab59.sh', 'mono', 32, TXT, align='left'), 140, 360, C['t2'] + 0.3, anim='fade'))
    steps = [('lab up', 'main plus two feature branches', 't3', ACC), ('1  merge logging', 'feature/logging into main', 't4', VIO), ('2  merge port', 'resolve it, keep 8080', 't5', WARN), ('3  clean up', 'delete both branches', 't6', PINK), ('4  answers.txt', 'merge commits on main', 't7', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540 if i < 3 else 830, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590 if i < 3 else 100 + (i - 3) * 880, 470 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Before you merge: git status', 930, C['t8'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['rb1'])
    items = [('Four PASS lines', 'rb2'), ('On main, git status first', 'rb3'), ('No markers left', 'rb4'), ('Merge vs fast-forward', 'rb5'), ('Answer number right', 'rb6'), ('lab down, removed', 'rb7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['rb8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Merge', 'feature/logging', ACC, 'z3'), ('3  Resolve', 'feature/port conflict', WARN, 'z4'), ('4  Delete', 'both merged branches', VIO, 'z5'), ('5  Check', 'answers.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What is a branch, really?', 'f12'), ('Which merge needs no new commit?', 'f13'), ('What do the marker lines mean?', 'f14'), ('How do you back out of a merge?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC07-O03', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: rebasing', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, model=s_model, kinds=s_kinds, branch=s_branch, merge=s_merge, marks=s_marks, conflict=s_conflict, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(model=('board', ACC), kinds=('board', VIO), branch=('code', GOOD), merge=('code', VIO), marks=('doc', WARN), conflict=('test', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson59/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
