def s_hook(C, D, dur):
    E = [El(T('It builds here. On the server: 401.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(700, 140, BAD, 'HTTP 401', [('Unauthorized', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(700, 140, ACC, 'private repository', [('needs a login', TXT)], 46, 30), 100, 480, C['h2'] + 2.5))
    E.append(Pop(card(760, 180, VIO, 'Never in git', [('the password', TXT)], 52, 40), 900, 440, C['h3']))
    E.append(takeaway('Mirror it. Lock it. Keep it secret.', 900, C['h4'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
s_what = _list('Repositories and mirrors', 'A mirror is a detour.', 'a1', [('1  repository', 'where Maven downloads libraries from', ACC, 'a1'), ('2  mirror', 'Maven asks the mirror instead of the original', VIO, 'a2'), ('3  why', 'speed, control, and a cache of everything', WARN, 'a3'), ('4  mirrorOf', 'matches by id: libs goes to the mirror', GOOD, 'a4')], 'The pom keeps the address. Settings choose the route.', 'a5')
s_settings = _list('settings.xml vs the pom', 'Project file, or your own file.', 'b1', [('pom.xml', 'belongs to the project, lives in git', ACC, 'b1'), ('~/.m2/settings.xml', 'belongs to you, never in git: mirrors and servers', VIO, 'b2'), ('server id = mirror id', 'the id links the password to the mirror', WARN, 'b4')], 'One wrong letter in an id: 401.', 'b5')
s_secrets = _list('Keeping passwords safe', 'Three rules.', 'x1', [('1  never in the pom', 'or any file in git', BAD, 'x2'), ('2  ${env.NAME}', 'the value stays outside the file', GOOD, 'x3'), ('3  chmod 600', 'only you can read the file', VIO, 'x4')], 'Better still: a secret store.', 'x5')
def s_task(C, D, dur):
    E = head('Your lab task', 'lab90.sh: a project and a repo with a login. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab90.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Server', [('id corp, user dev', TXT), ('${env.CORP_PASS}', TXT)], 'k3', ACC), ('2  Mirror', [('id corp, libs', TXT), ('port 8091', TXT)], 'k4', VIO), ('3  Lock', [('chmod 600', TXT), ('settings.xml', TXT)], 'k5', WARN), ('4  Build', [('export CORP_PASS', TXT), ('mvn -s settings.xml', TXT)], 'k6', GOOD), ('5  why.txt', [('one sentence', TXT), ('pom + git', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', BAD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('What a mirror does', 'q3'), ('Server id = mirror id', 'q4'), ('No password in any file', 'q5'), ('settings.xml mode 600', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Server, mirror', 'settings.xml blocks', ACC, 'z3'), ('3  Lock', 'chmod 600', VIO, 'z4'), ('4  Build', 'export, then mvn -s', WARN, 'z5'), ('5  Explain, check', 'why.txt, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does a mirror do?', 'f12'), ('Which file holds credentials?', 'f13'), ('Keep a password out of files?', 'f14'), ('What does 401 mean?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC10-O06', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: publish artifacts', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_mirror = _lab('Live: mirror, login and 401', 'See the 401, give the password safely, prove it is in no file.', 'm0', RB, [('m1', 'settings.xml', 'server + mirror, same id', ACC), ('m2', 'build, no password', '401 Unauthorized', BAD), ('m3', 'export REPO_PASS', 'read from a locked file', VIO), ('m4', 'build again', 'a jar, with the login', GOOD), ('m5', 'grep for the password', 'in no file', GOOD), ('m6', 'chmod 600', 'both files locked', WARN)])
FN = dict(hook=s_hook, what=s_what, settings=s_settings, secrets=s_secrets, mirror=s_mirror, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(what=('link', ACC), settings=('gear', VIO), secrets=('test', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'mirror': [('m1b', 4, 1, 0, 500, 'SAME ID'), ('m1b', 11, 1, 0, 500, ''), ('m1b', 6, 1, 0, 800, 'FROM ENV'), ('m2b', 2, 2, 0, 1070, '401'), ('m4b', 1, 1, 0, 600, 'A JAR'), ('m5b', 2, 1, 0, 600, 'NOT FOUND'), ('m6b', 2, 2, 0, 1070, 'LOCKED')]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson90/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
