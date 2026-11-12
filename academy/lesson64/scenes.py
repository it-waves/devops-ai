def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h



def s_hook(C, D, dur):
    E = [El(T('Keep your secrets secret', 'x', 72), 100, 130, C['y1'])]
    E.append(Pop(card(1100, 140, BAD, 'One leaked password', [('bots scan public repositories, often within minutes', TXT)], 44, 32), 100, 290, C['y1'] + 2.0))
    for i, (a, b, col) in enumerate([('Secrets', 'keep them out of Git, rotate if leaked', ACC), ('SSH keys + tokens', 'prove who you are, safely', VIO), ('Roles', 'give the smallest access that works', GOOD)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 470 + i * 150, C['y3'] + i * 1.6))
    E.append(takeaway('Lab and checker at the end.', 960, C['y4'], GOOD, 1700)); return E
def s_model(C, D, dur):
    E = head('Secrets, and three rules', 'Git never forgets.', C['d1']); E.append(ill(C['d1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 105, BAD, 'A secret', [('password · API key · token · private key', TXT)], 38, 30), 100, 340, C['d1']))
    E.append(Pop(card(1700, 105, WARN, 'Git never forgets', [('deleting the file later does not remove it from history', TXT)], 38, 30), 100, 465, C['d2']))
    it = [('1  Keep secrets out', 'env variables, an ignored .env file, a secret manager', ACC, 'd3'), ('2  Leaked? Rotate first', 'new secret, kill the old one, then clean history', BAD, 'd4'), ('3  Least access', 'SSH key pair, small token scopes, small roles', GOOD, 'd5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 120, col, n, [(s_, TXT)], 40, 30), 100, 610 + i * 145, C[cid]))
    return E
s_leak = _lab('A leaked password', 'Untrack it, then rewrite history.', 'lk1', RB, [('lk3', 'cat .env', 'A password in Git', BAD), ('lk4', 'echo .env >> .gitignore', 'Ignore it (rotate first!)', WARN), ('lk5', 'git rm --cached', 'Untrack, keep the file', ACC), ('lk8', 'git log -S', 'Still in history', BAD), ('lk9', 'git filter-repo', 'Rewrite history', VIO), ('lk10', 'git log -S', 'Gone', GOOD)])
s_ssh = _lab('SSH keys', 'A key pair: share only the public half.', 'ss1', RB, [('ss2', 'ssh-keygen -t ed25519', 'Make a key pair', ACC), ('ss3', 'ls ~/.ssh', 'Two files', VIO), ('ss4', 'cat key.pub', 'Public: share it', GOOD), ('ss5', 'head -n 1 key', 'Private: never share', BAD)])
def _ui(name):
    def f(C, D, dur): return []
    return f
s_token = _ui('token'); s_access = _ui('access')
def s_task(C, D, dur):
    E = head('Your lab task', 'lab64.sh builds it. lab check judges it.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['t2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab64.sh', 'mono', 32, TXT, align='left'), 140, 360, C['t2'] + 0.3, anim='fade'))
    steps = [('lab up', 'a fake password committed by mistake', 't3', ACC), ('1  untrack', '.env ignored and untracked', 't4', VIO), ('2  rewrite', 'secret gone from every commit', 't5', WARN), ('3  SSH key', 'ed25519, named lab64_key', 't6', PINK), ('4  answers.txt', 'first thing to do: rotate', 't7', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540 if i < 3 else 830, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590 if i < 3 else 100 + (i - 3) * 880, 470 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Rotate, then clean.', 930, C['t8'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['rb1'])
    items = [('Four PASS lines', 'rb2'), ('Secret gone from history', 'rb3'), ('Private key stays private', 'rb4'), ('Rotate before cleaning', 'rb5'), ('Smallest scope and role', 'rb6'), ('lab down, removed', 'rb7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['rb8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Untrack', 'ignore .env', ACC, 'z3'), ('3  Rewrite', 'git filter-repo', WARN, 'z4'), ('4  SSH key', 'ssh-keygen ed25519', VIO, 'z5'), ('5  Check', 'answers.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why does deleting a file keep the secret?', 'f12'), ('First step when a secret leaks?', 'f13'), ('Which half of an SSH key do you share?', 'f14'), ('What is least access?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC07-O08', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: a team release workflow', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, model=s_model, leak=s_leak, ssh=s_ssh, token=s_token, access=s_access, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(model=('board', ACC), leak=('code', GOOD), ssh=('doc', VIO), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson64/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
