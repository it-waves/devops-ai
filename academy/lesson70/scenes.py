def s_hook(C, D, dur):
    E = [El(T('Who is asking?', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(840, 140, BAD, 'Anyone can send a request', [('so how does the API know who is asking?', TXT)], 44, 32), 100, 330, C['h1'] + 1.2))
    E.append(Pop(card(840, 110, WARN, 'Anyone could read every order', [], 44, 32), 100, 500, C['h2']))
    E.append(Pop(card(840, 110, WARN, 'Anyone could delete your products', [], 44, 32), 100, 630, C['h2'] + 1.8))
    mv = [('Authentication', 'who you are', ACC), ('Authorization', 'what you may do', VIO), ('Tokens', 'proof on every request', GOOD), ('Secrets', 'never let them leak', PINK)]
    for i, (n, s_, col) in enumerate(mv): E.append(Pop(card(420, 170, col, n, [(s_, TXT)], 38, 28, True), 1000 + (i % 2) * 440, 330 + (i // 2) * 200, C['h3'] + 2.0 + i * 2.2))
    E.append(Pop(badge('401', F('x', 60), INK, BAD, padx=36, pady=18), 100, 800, C['h4'])); E.append(Pop(badge('403', F('x', 60), INK, WARN, padx=36, pady=18), 360, 800, C['h4'] + 0.8))
    E.append(takeaway('Two numbers every DevOps engineer reads.', 980, C['h4'] + 1.2, GOOD, 1700)); return E
s_authn = _lab('Log in: authentication', 'Prove who you are, and get a token.', 'a1', RB, [('a2', './start.sh', 'passwords come from secrets.env', ACC), ('a3', 'POST /api/login', 'wrong password', VIO), ('a4', '401 Unauthorized', 'I do not know who you are', BAD), ('a5', 'POST /api/login', 'the right password', WARN), ('a6', 'a token', 'role: customer, 1 hour', GOOD)])
s_access = _lab('Tokens, 401 and 403', 'Send the token. Roles decide what you may do.', 'c1', RB, [('c3', 'GET /api/orders', 'no token', ACC), ('c4', '401', 'no token, no entry', BAD), ('c6', 'Authorization: Bearer', 'send the token', VIO), ('c7', '200 + orders', 'the server knows Bob', GOOD), ('c9', '403 Forbidden', 'Bob may not delete', WARN), ('c12', '204 as Alice', 'admin role: allowed', GOOD)])
s_secrets = _lab('Keeping secrets', 'Passwords live outside the code, and stay private.', 's1', RB, [('s2', 'ls -l secrets.env', 'who can read it?', ACC), ('s3', '-rw-r--r--', 'everyone: a leak', BAD), ('s4', 'chmod 600', 'owner only', WARN), ('s6', 'grep -c paper-kite', 'zero: not in the code', VIO), ('s8', 'Never in code or git', 'env or a private file', GOOD)])
def s_models(C, D, dur):
    E = head('Sessions and tokens', 'Who are you, what may you do, and how is it remembered?', C['m1']); E.append(ill(C['m1'] + 0.2, 1400, 170))
    E.append(Pop(card(840, 150, ACC, 'Authentication', [('who are you?  failure: 401', TXT)], 40, 30), 100, 340, C['m2']))
    E.append(Pop(card(840, 150, VIO, 'Authorization', [('what may you do?  failure: 403', TXT)], 40, 30), 980, 340, C['m3']))
    E.append(Pop(card(840, 190, WARN, 'Session', [('the server remembers you', TXT), ('you carry a cookie with its number', TXT)], 40, 28), 100, 530, C['m5']))
    E.append(Pop(card(840, 190, GOOD, 'Token', [('you carry the proof yourself', TXT), ('Authorization: Bearer ...', TXT)], 40, 28), 980, 530, C['m6']))
    E.append(Pop(card(1720, 110, PINK, '', [('a token is a password with a short life: protect it, let it expire', TXT)], 4, 34), 100, 760, C['m7']))
    E.append(takeaway('Real systems add MFA and hashed passwords.', 940, C['m8'], WARN, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab70.sh starts CloudCart. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab70.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Log in', 'save Bob token in token.txt', 'k3', VIO), ('2  No token', 'nologin: the status code', 'k4', BAD), ('3  Forbidden', 'Bob tries a delete', 'k5', WARN), ('4  Admin', 'Alice deletes product 3', 'k6', PINK), ('5  Secrets', 'chmod 600 secrets.env', 'k7', ACC), ('lab check', 'five PASS lines', 'k8', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 230, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('AuthN versus AuthZ', 'q3'), ('401 versus 403', 'q4'), ('Send a Bearer token', 'q5'), ('Secrets: out of code and git', 'q6'), ('lab down, nothing listening', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Log in', 'Bob, save the token', ACC, 'z3'), ('3  401, 403', 'write them down', VIO, 'z4'), ('4  Admin', 'Alice deletes 3', WARN, 'z5'), ('5  Lock', 'secrets.env', BAD, 'z6'), ('6  Check', 'lab check, lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('AuthN versus AuthZ?', 'f12'), ('401 or 403: who are you?', 'f13'), ('How does a Bearer token travel?', 'f14'), ('Why keep secrets out of code?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC08-O04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: config and feature flags', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, authn=s_authn, access=s_access, secrets=s_secrets, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(authn=('code', ACC), access=('test', BAD), secrets=('doc', GOOD), models=('board', ACC), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'authn': [('a4', 2, 1, 0, 386, 'NOT AUTHENTICATED'), ('a6', 2, 1, 0, 462, 'THE TOKEN')],
 'access': [('c4', 1, 1, 0, 386, 'NO TOKEN'), ('c9', 2, 1, 0, 340, 'ROLE NOT ALLOWED'), ('c12', 2, 1, 0, 356, 'ALLOWED')],
 'secrets': [('s3', 1, 1, 0, 158, 'EVERYONE CAN READ')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson70/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
