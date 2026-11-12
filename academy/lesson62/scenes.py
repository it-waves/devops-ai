def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h




def s_hook(C, D, dur):
    E = [El(T('Get your branch into main, safely', 'x', 66), 100, 130, C['y1'])]
    E.append(Pop(card(1100, 140, BAD, 'Push straight to main', [('one mistake breaks it for everyone', TXT)], 44, 32), 100, 290, C['y1'] + 3.0))
    for i, (a, b, col) in enumerate([('Pull request', 'a proposal with a conversation', ACC), ('Review', 'comment, approve, request changes', VIO), ('Protected branch', 'a server rule nobody can skip', GOOD)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 470 + i * 150, C['y2'] + i * 3.5))
    E.append(takeaway('Watch it live on a real Git server.', 960, C['y4'], GOOD, 1700)); return E
def s_model(C, D, dur):
    E = head('Pull requests and protected branches', 'A proposal, a review, a rule.', C['d1']); E.append(ill(C['d1'] + 0.2, 1400, 170))
    steps = [('branch', 'your work', ACC), ('push', 'to the server', VIO), ('pull request', 'propose the merge', WARN), ('review', 'read and discuss', PINK), ('merge', 'into main', GOOD)]
    for i, (a, b, col) in enumerate(steps): E.append(Pop(card(320, 150, col, a, [(b, TXT)], 40, 28), 100 + i * 360, 340, C['d1'] + i * 0.7))
    E.append(Pop(card(540, 150, WARN, 'GitHub: pull request', [('GitLab: merge request', TXT)], 38, 28), 100, 540, C['d2']))
    for i, (n, col) in enumerate([('comment', MUTED), ('approve', GOOD), ('request changes', BAD)]): E.append(Pop(badge(n, F('b', 36), INK, col, padx=28, pady=14), 760 + i * 330, 580, C['d3'] + i * 0.8))
    E.append(Pop(card(1700, 150, VIO, 'Protected branch (a server rule)', [('no direct pushes to main  ·  one approval before a merge', TXT)], 40, 30), 100, 760, C['d4']))
    E.append(El(T('Demo on Gitea  ·  on GitHub: Settings, then Branches', 'm', 30, MUTED, maxw=1700), 100, 960, C['d5'], anim='fade')); return E
def _ui(name):
    def f(C, D, dur): return []
    return f
s_protect = _ui('protect'); s_pr = _ui('pr'); s_review = _ui('review'); s_merge = _ui('merge')
def s_task(C, D, dur):
    E = head('Your lab task', 'You build it on GitHub. lab62.sh judges it.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['t2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab62.sh', 'mono', 32, TXT, align='left'), 140, 360, C['t2'] + 0.3, anim='fade'))
    steps = [('Account', 'free GitHub, public repo', 't3', ACC), ('1  repo + branch', 'team-app, push a change', 't4', VIO), ('2  pull request', 'open it, leave a review', 't5', WARN), ('3  protect main', 'Settings, Branches', 't6', PINK), ('4  merge', 'then delete the branch', 't7', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540 if i < 3 else 830, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590 if i < 3 else 100 + (i - 3) * 880, 470 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Four PASS lines.', 930, C['t7'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['rb1'])
    items = [('Four PASS lines', 'rb2'), ('Main is protected', 'rb3'), ('Clear title and text', 'rb4'), ('Three review outcomes', 'rb5'), ('Branch deleted', 'rb6'), ('Why protect main', 'rb7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['rb8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own GitHub account. Slow and exact.', C['z1'])
    it = [('1  Create', 'repo and a branch', PINK, 'z2'), ('2  Review', 'open and review the PR', ACC, 'z3'), ('3  Protect', 'main, in Settings', WARN, 'z4'), ('4  Merge', 'then delete the branch', VIO, 'z5'), ('5  Check', 'lab check', BAD, 'z6'), ('6  Clean up', 'delete the repository', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What is a pull request?', 'f12'), ('Name the three review outcomes.', 'f13'), ('What does a protected branch stop?', 'f14'), ('Why delete the branch after merging?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC07-O06', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: restore, revert and reflog', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, model=s_model, protect=s_protect, pr=s_pr, review=s_review, merge=s_merge, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(model=('board', ACC), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson62/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
