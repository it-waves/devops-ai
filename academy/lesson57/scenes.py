def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def s_hook(C, D, dur):
    E = [El(T('Git: version control from zero', 'x', 72), 100, 130, C['h1'])]
    names = ['report.docx', 'report_final.docx', 'report_final2.docx', 'report_REALLY_final.docx']
    for i, n in enumerate(names): E.append(Pop(card(760, 100, [MUTED, MUTED, WARN, BAD][i], '', [(n, TXT)], 4, 34), 100 + (i % 2) * 800, 290 + (i // 2) * 120, C['h1'] + 2.0 + i * 1.2))
    E.append(logo_c('git', 700, 520, C['h2'], 170, 'Git')); E.append(logo_c('github', 1220, 520, C['h3'], 170, 'GitHub'))
    E.append(Pop(card(560, 140, GOOD, 'Every commit', [('who, when, why', TXT)], 40, 32), 100, 780, C['h2'] + 2.0)); E.append(Pop(card(560, 140, ACC, 'Every copy', [('the whole history', TXT)], 40, 32), 700, 780, C['h2'] + 5.0))
    E.append(takeaway('Prove it with a lab and a checker.', 960, C['h4'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('One big idea', 'Every copy is a full backup.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(840, 600, BAD, 'Central server (old way)', [], 38), 100, 330, C['w1']))
    E.append(pill('SERVER', 400, 440, C['w1'] + 0.4, BAD, INK, 38))
    for i, x in enumerate([160, 380, 600]):
        E.append(pill('dev ' + 'ABC'[i], x, 700, C['w1'] + 1.0 + i * 0.3, MUTED, INK, 30)); E.append(A([(x + 60, 690), (x + 60 if i == 1 else 490 + (x - 380) // 4, 520)], C['w1'] + 1.6 + i * 0.2, BAD, 6, 24))
    E.append(El(T('only the server has the history', 'm', 30, MUTED, maxw=760), 150, 820, C['w1'] + 3.5, anim='fade'))
    E.append(Pop(badge('SERVER DOWN: nobody can save history', F('b', 28), INK, BAD, padx=22, pady=12), 140, 880, C['w2']))
    E.append(Pop(card(840, 600, GOOD, 'Distributed (Git)', [], 38), 980, 330, C['w3']))
    for i, (x, y) in enumerate([(1060, 440), (1340, 440), (1060, 620), (1340, 620)]):
        E.append(Pop(card(240, 150, GOOD if i < 3 else ACC, 'full copy', [('all history', TXT)], 30, 26), x, y, C['w3'] + 0.4 + i * 0.35))
    E.append(Pop(badge('works offline', F('b', 28), INK, GOOD, padx=22, pady=12), 1060, 830, C['w4'])); E.append(Pop(badge('any clone can rebuild it', F('b', 28), INK, ACC, padx=22, pady=12), 1330, 830, C['w4'] + 1.5))
    E.append(Pop(badge('Git: the tool on your computer', F('b', 28), INK, ACC, padx=22, pady=12), 700, 975, C['w5'])); E.append(Pop(badge('GitHub: a website hosting copies', F('b', 28), INK, GOOD, padx=22, pady=12), 1210, 975, C['w5'] + 1.5))
    E.append(takeaway('Git is not GitHub.', 970, C['w5'] + 3.0, WARN, 560)); return E
def s_anat(C, D, dur):
    E = head('Four places for your work', 'Know where a change is, at any moment.', C['a1']); E.append(ill(C['a1'] + 0.2, 1400, 170))
    it = [('Working tree', 'files you edit', ACC, 'a2'), ('Staging area', 'next snapshot', VIO, 'a3'), ('Repository', 'the .git folder', GOOD, 'a4'), ('Remote', 'e.g. GitHub', WARN, 'a5')]
    for i, (n, s_, col, cid) in enumerate(it):
        x = 100 + i * 450; E.append(Pop(card(380, 190, col, n, [(s_, TXT)], 38, 30), x, 340, C[cid]))
    cmds = [('git add', 'a3', VIO), ('git commit', 'a4', GOOD), ('git push', 'a5', WARN)]
    for i, (t, cid, col) in enumerate(cmds):
        x = 100 + i * 450 + 380
        E.append(A([(x + 4, 435), (x + 66, 435)], C[cid] + 0.3, col, 7, 26)); E.append(Pop(chip(t, col, 24, 12, 6), x - 14, 470, C[cid] + 0.5))
    rows = [('.git/HEAD      where you are now', ACC), ('.git/config    settings for this repo', TXT), ('.git/objects/   every file and commit', GOOD), ('.git/refs/      names of branches and tags', WARN)]
    mono_panel(E, 100, 620, 1100, rows, C['a6'], 28, 44)
    E.append(Pop(badge('delete .git  =  history gone', F('b', 34), INK, BAD, padx=28, pady=16), 1260, 700, C['a7'])); return E
s_init = _lab('git init', 'A folder becomes a repository.', 'i1', RB, [('i1', 'git config', 'Name and email, once', ACC), ('i3', 'mkdir notes', 'A project folder', VIO), ('i5', 'git init', 'Make a repository', GOOD), ('i6', 'ls -a', 'Hidden .git appears', WARN), ('i7', 'ls .git', 'HEAD, objects, refs', PINK)])
s_commit = _lab('Stage and commit', 'Change, stage, commit.', 'm1', RB, [('m2', 'echo > file', 'Create a file', ACC), ('m3', 'git status -s', '?? = untracked', WARN), ('m4', 'git add', 'Stage the change', VIO), ('m5', 'git commit -m', 'Root commit, no parent', GOOD), ('m8', 'second commit', 'Parent = first commit', PINK), ('m9', 'git log --oneline', 'The history chain', ACC)])
s_objs = _lab('Inside the database', 'Everything is an object with a name.', 'o1', RB, [('o2', 'cat .git/HEAD', 'Points to branch main', ACC), ('o4', 'cat-file -t', 'Object type: commit', VIO), ('o5', 'cat-file -p', 'tree, parent, author', GOOD), ('o6', 'the tree', 'Files with blob hashes', WARN), ('o7', 'hash-object', 'Same content, same name', PINK), ('o8', 'count objects', '2 commits, 2 trees, 2 blobs', ACC)])
s_clone = _lab('git clone', 'A full copy, with the whole history.', 'k1', RB, [('k1', 'git clone', 'Files and history', ACC), ('k3', 'git log', 'Same hashes', GOOD), ('k4', 'git remote -v', 'origin: fetch and push', VIO), ('k5', 'git branch -a', 'main + origin/main', WARN)])
s_ui = _lab('The same commit on GitHub', 'A real private repository, every click shown.', 'u1', RU, [('u1', 'New file', 'Name: README.md', ACC), ('u3', 'Commit changes', 'The message', VIO), ('u4', 'History', '1 commit, short hash', GOOD), ('u6', 'Commit page', '0 parents = root', WARN), ('u7', 'Code button', 'The clone address', PINK)])
def s_task(C, D, dur):
    E = head('Your lab task', 'lab57.sh builds it. lab check judges it.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['t2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab57.sh', 'mono', 32, TXT, align='left'), 140, 360, C['t2'] + 0.3, anim='fade'))
    steps = [('lab up', 'builds origin.git with 1 commit', 't3', ACC), ('1  clone', 'origin.git into work/team', 't4', VIO), ('2  commit', 'notes.txt, your own message', 't5', WARN), ('3  answers.txt', 'root hash (7) + commit count', 't6', PINK), ('lab check', 'four PASS lines', 't7', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540 if i < 3 else 830, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590 if i < 3 else 100 + (i - 3) * 880, 470 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Symptom. Check. One change. Proof.', 930, C['t8'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Four PASS lines', 'b2'), ('Cloned, not copied', 'b3'), ('Clear commit message', 'b4'), ('Why origin has 1 commit', 'b5'), ('Root hash + count right', 'b6'), ('lab down, removed', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Clone', 'origin.git, read the log', ACC, 'z3'), ('3  Commit', 'notes.txt, stage, commit', WARN, 'z4'), ('4  Answers', 'root hash + count', VIO, 'z5'), ('5  Check', 'four PASS lines', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why do we call Git distributed?', 'f12'), ('What is the staging area for?', 'f13'), ('What does a commit contain?', 'f14'), ('Why does a root commit have no parent?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC07-O01', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: staging, history, and ignore files', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, why=s_why, anat=s_anat, init=s_init, commit=s_commit, objs=s_objs, clone=s_clone, ui=s_ui, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('board', ACC), anat=('gear', VIO), init=('gear', ACC), commit=('code', GOOD), objs=('eye', WARN), clone=('board', ACC), ui=('eye', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'init': [('i6', 1, 1, 4, 489, ''), ('i7', 1, 1, 95, 160, '')],
 'commit': [('m4', 1, 1, 4, 190, ''), ('m6', 1, 1, 95, 292, ''), ('m10', 1, 2, 4, 110, '')],
 'objs': [('o6', 2, 1, 4, 716, ''), ('o7', 2, 1, 186, 792, ''), ('o8', 1, 1, 4, 612, '')],
 'clone': [('k4', 1, 2, 4, 110, ''), ('k5', 1, 2, 4, 580, ''), ('k6', 2, 2, 4, 560, '')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson57/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
