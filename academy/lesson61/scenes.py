def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h



def s_hook(C, D, dur):
    E = [El(T('Share your work with the team', 'x', 72), 100, 130, C['y1'])]
    E.append(Pop(card(1100, 140, BAD, 'Only on your laptop', [('lost if the laptop dies, unseen by the team', TXT)], 44, 32), 100, 290, C['y1'] + 3.0))
    for i, (a, b, col) in enumerate([('Remotes', 'a shared copy, nicknamed origin', ACC), ('Fetch, pull, push', 'the daily team rhythm', VIO), ('Tags', 'stamp a version on a commit', GOOD)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 470 + i * 150, C['y3'] + i * 3.5))
    E.append(takeaway('Lab and checker at the end.', 960, C['y4'], GOOD, 1700)); return E
def s_model(C, D, dur):
    E = head('Remotes and origin', 'Your copy, their copy, and a bookmark.', C['d1']); E.append(ill(C['d1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 190, VIO, 'origin', [('the shared copy on a server', TXT)], 44, 30), 100, 340, C['d1'])); E.append(Pop(card(540, 190, ACC, 'your clone', [('your own commits and files', TXT)], 44, 30), 1280, 340, C['d2']))
    E.append(Pop(chip('origin/main', WARN, 30, 18, 8), 720, 400, C['d3'])); E.append(El(T('a bookmark: where origin was when you last asked', 'm', 28, TXT, align='left'), 560, 470, C['d3'] + 0.3, anim='fade'))
    it = [('git fetch', 'download, move the bookmark, touch no files', ACC, 'd4'), ('git pull', 'fetch + merge or rebase: updates your branch', VIO, 'd5'), ('git push', 'upload your commits, if nobody is overwritten', GOOD, 'd6')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 120, col, n, [(s_, TXT)], 38, 30), 100, 600 + i * 150, C[cid]))
    return E
s_clone = _lab('Clone and remote tracking', 'Clone, remotes, tracking branches.', 'cl1', RB, [('cl1', 'git clone', 'Copy the shared repo', ACC), ('cl3', 'remote -v', 'The nickname: origin', VIO), ('cl4', 'branch -vv', 'main tracks origin/main', GOOD), ('cl5', 'branch -a', 'remotes/origin/*', WARN)])
s_fetch = _lab('Fetch, then pull', 'Look before you take it.', 'ft1', RB, [('ft2', 'git status', 'Only as fresh as the bookmark', WARN), ('ft3', 'git fetch', 'Ask the server', ACC), ('ft5', 'log main..origin/main', 'What is waiting', VIO), ('ft6', 'git pull', 'Fast-forward', GOOD)])
s_push = _lab('Push and rejection', 'Pull first, then push.', 'ps1', RB, [('ps3', 'git commit -am', 'Your own work', ACC), ('ps4', 'git push', 'REJECTED: fetch first', BAD), ('ps5', 'pull --rebase', 'Replay yours on top', VIO), ('ps6', 'git push', 'Accepted', GOOD), ('ps7', 'log --graph --all', 'Same commit, straight line', WARN)])
s_tags = _lab('Tags', 'Name a commit, then share the name.', 'tg1', RB, [('tg2', 'tag -a v1.0 -m', 'Annotated tag', ACC), ('tg3', 'git tag', 'List tags', VIO), ('tg4', 'show --stat v1.0', 'Tagger, message, commit', GOOD), ('tg5', 'push origin v1.0', 'Tags are not auto-pushed', WARN), ('tg6', 'ls-remote --tags', 'Confirm on the server', PINK)])
def s_task(C, D, dur):
    E = head('Your lab task', 'lab61.sh builds it. lab check judges it.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['t2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab61.sh', 'mono', 32, TXT, align='left'), 140, 360, C['t2'] + 0.3, anim='fade'))
    steps = [('lab up', 'a shared repo, your clone, a teammate commit', 't3', ACC), ('1  commit', 'release-notes.txt, one line', 't4', VIO), ('2  push', 'rejected? pull, push again', 't5', WARN), ('3  tag', 'annotated v1.0, pushed', 't6', PINK), ('4  answers.txt', 'commits on origin main', 't7', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540 if i < 3 else 830, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590 if i < 3 else 100 + (i - 3) * 880, 470 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Fetch first, look, then pull.', 930, C['t8'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['rb1'])
    items = [('Four PASS lines', 'rb2'), ('Pulled before pushing', 'rb3'), ('Tag annotated, pushed', 'rb4'), ('Fetch vs pull', 'rb5'), ('Answer number right', 'rb6'), ('lab down, removed', 'rb7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['rb8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Commit', 'release-notes.txt', ACC, 'z3'), ('3  Push', 'pull first if rejected', WARN, 'z4'), ('4  Tag', 'annotated, pushed', VIO, 'z5'), ('5  Check', 'answers.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does fetch do that pull does not?', 'f12'), ('What is origin/main?', 'f13'), ('Why was the first push rejected?', 'f14'), ('Are tags pushed automatically?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC07-O05', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: pull requests and reviews', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, model=s_model, clone=s_clone, fetch=s_fetch, push=s_push, tags=s_tags, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(model=('board', ACC), clone=('code', GOOD), fetch=('eye', VIO), push=('code', WARN), tags=('doc', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson61/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
