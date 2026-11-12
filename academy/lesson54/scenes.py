def s_hook(C, D, dur):
    E = [El(T('Cloud SDKs, least privilege', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Least privilege', 'only the actions and resources needed', ACC), ('boto3 + moto', 'cloud code, free mock, no account', GOOD), ('Clean up', 'delete what you create', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 3.0))
    E.append(takeaway('Give code the least power it needs.', 850, C['h3'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('Least privilege, SDKs, moto', 'Only what is needed, tested for free.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 215, ACC, 'policy', [('Effect  Action  Resource', TXT), ('no * wildcards', MUTED)], 44, 32, True), 100, 340, C['w2']))
    E.append(Pop(card(540, 215, GOOD, 'credentials', [('env, file, role', TXT), ('never in code', MUTED)], 44, 32, True), 690, 340, C['w3']))
    E.append(Pop(card(540, 215, WARN, 'moto', [('a free fake AWS', TXT), ('no account needed', MUTED)], 44, 32, True), 1280, 340, C['w4']))
    E.append(Pop(card(1700, 150, VIO, 'real account?', [('free tier only, then delete what you made', TXT)], 38, 30), 100, 620, C['w5'] - 3.0))
    E.append(takeaway('Least power. No keys in code. Clean up.', 850, C['w5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Get the lab and task', 'Everything is in the repository.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 't2', ACC), ('Folder', 'academy/lesson54', 't3', VIO), ('Files', 'TASK.md  check54.sh', 't3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 't3'), ('cd devops-ai/academy/lesson54 && pip install boto3 moto', 't3'), ('# write policy.json and s3tools.py', 't4'), ('bash check54.sh .      # six PASS lines', 't6')]
    E.append(Pop(glass(1700, 4 * 46 + 48, WARN), 100, 700, C['t3']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, python3, your venv. moto only: no cloud account. No peeking at the solution.', 'm', 26, MUTED, maxw=1700), 100, 960, C['t6'], anim='fade')); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['r1'])
    items = [('Checker: six PASS', 'r2'), ('Read-only, no * action', 'r3'), ('One bucket only', 'r4'), ('1000+ objects, empty ok', 'r5'), ('No keys, cleanup line', 'r6'), ('Complete report, own VM', 'r7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['r8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only.', C['z1'])
    it = [('1  Get files', 'lesson54 folder, activate venv', PINK, 'z2'), ('2  Install', 'pip install boto3 moto', ACC, 'z3'), ('3  Policy', 'policy.json, no stars', WARN, 'z4'), ('4  Code', 's3tools.py, paginator', VIO, 'z5'), ('5  Break it', 'add a *, watch it fail', BAD, 'z6'), ('6  Check', 'six PASS, then report', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does least privilege mean?', 'f12'), ('Where does boto3 find credentials?', 'f13'), ('What does moto do for you?', 'f14'), ('After a real account, what next?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC06-O08', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: a tested inventory utility', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_policy = _lab('Policies and the audit', 'Least privilege, checked by a script.', 'a1', RB, [('a1', 'cat policy.json', 'list one bucket, get objects', ACC), ('a3', 'audit.py', 'flags * wildcards', VIO), ('a3', 'OK: no wildcards', 'least privilege', GOOD), ('a4', 'bad.json', '* action, * resource', BAD), ('a5', 'exit code 1', 'a pipeline can block it', WARN)])
s_sdk = _lab('boto3 against moto', 'Cloud code with a free mock.', 'd1', RB, [('d1', 'cat s3list.py', 'boto3 + moto', ACC), ('d2', 'mock_aws', 'no keys in the code', VIO), ('d3', '3 objects', 'sizes from a fake bucket', GOOD), ('d4', 'ClientError', 'catch the error', WARN), ('d5', 'NoSuchBucket', 'the code says why', PINK)])
FN = dict(hook=s_hook, why=s_why, policy=s_policy, sdk=s_sdk, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('gear', ACC), policy=('test', WARN), sdk=('board', VIO), task=('gear', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'policy': [('a3', 1, 1, 4, 505, ''), ('a4', 1, 2, 4, 460, ''), ('a5', 1, 1, 4, 40, '')],
 'sdk': [('d3', 1, 3, 4, 200, ''), ('d5', 1, 1, 4, 310, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson54/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
