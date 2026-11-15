def s_hook(C, D, dur):
    E = [El(T('Settings. Flags. Secrets.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(760, 140, ACC, 'a real password', [('wanted by a repository', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(760, 160, VIO, '3 places', [('file · flag · environment', TXT)], 52, 30), 100, 480, C['h3']))
    E.append(Pop(card(760, 160, WARN, 'live on Gradle 8.14.3', [('remove a leaked secret', TXT)], 46, 30), 900, 440, C['h4']))
    E.append(Pop(card(1100, 140, GOOD, 'then you do it alone', [('a checker judges you', TXT)], 46, 30), 100, 700, C['h5']))
    E.append(takeaway('Settings: files. Secrets: environment.', 900, C['h6'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f

s_parts = _list('Four ideas of config and secrets', 'Every safe Gradle build has these.', 'a1', [('1  gradle.properties', 'settings, not secret, shared by the team', ACC, 'a2'), ('2  -P on the command line', 'overrides a setting for one run', VIO, 'a3'), ('3  the environment', 'secrets: ORG_GRADLE_PROJECT_name', GOOD, 'a4'), ('4  read, never print', 'a build log is public', WARN, 'a5')], 'Real Nexus needs a password: this is the way in.', 'a6', h=125, gap=145)
def s_task(C, D, dur):
    E = head('Your lab task', 'lab98.sh: a build with a leaked password. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Remove', [('password in a file', TXT), ('take it out', TXT)], 'k2', ACC), ('2  Setting', [('greeting=...', TXT), ('in gradle.properties', TXT)], 'k3', WARN), ('3  Override', [('-Pgreeting=Hello', TXT), ('save override.txt', TXT)], 'k4', VIO), ('4  Secret', [('from the environment', TXT), ('save secret.txt', TXT)], 'k5', GOOD), ('5  Notes', [('3 lines', TXT), ('where, why, override', TXT)], 'k6', PINK)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab98.sh   and   shortcuts97.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab98.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts97.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, curl, python3, 1 GB memory, internet', PINK, 'i6'), ('6  Cleanup', 'lab down removes everything. Your own VM only.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('Password in no file', 'q3x'), ('Setting + -P override', 'q4x'), ('Secret from the environment', 'q5x'), ('Notes answer 3 questions', 'q6x'), ('lab down, nothing left', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, task file', PINK, 'z2'), ('2  Remove', 'the password from the file', ACC, 'z3'), ('3  Setting', 'greeting, then -P once', VIO, 'z4'), ('4  Secret', 'through the environment', WARN, 'z5'), ('5  Notes', 'where, why, override, check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    _unused = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Build', 'each project, first error', ACC, 'z3'), ('3  Name it', 'the cause, in your words', VIO, 'z4'), ('4  Fix', 'fix the cause, rebuild', WARN, 'z5'), ('5  Notes + check', 'report.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Settings vs secrets: where do they go?', 'f12'), ('Which flag overrides a property?', 'f13'), ('How does an env variable become a property?', 'f14'), ('Why print set, not the value?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC11-O04 Gradle', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: build cache, reproducible', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: remove a secret, override a setting', 'A real Gradle 8.14.3 build. The password in the lab is a made-up test value.', 'p0', RB, [('f1', '1  the leak', 'a password in a plain file', BAD), ('s1', '2  what Gradle sees', 'showConfig: password=set', VIO), ('r1', '3  remove it', 'delete the line', WARN), ('g1', '4  a setting', 'greeting in gradle.properties', GOOD), ('o1', '5  override', '-Pgreeting=Hello, one run', PINK), ('e1', '6  the secret', 'from the environment', ACC), ('c1', '7  prove it', 'in no file: 0 matches', GOOD)])
FN = dict(hook=s_hook, parts=s_parts, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(parts=('board', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [('f1b', 1, 1, 0, 365, 'A SECRET IN A FILE', 395, 1), ('s1b', 2, 1, 0, 190, 'FOUND IN THE FILE', 220, 2), ('s2b', 2, 1, 0, 250, 'NO LONGER LEAKS', 280, 2), ('g2b', 1, 1, 0, 440, 'FROM THE FILE', 470, 1), ('o1b', 1, 1, 0, 220, 'THE FLAG WINS', 250, 1), ('e1b', 3, 1, 0, 190, 'FROM THE ENVIRONMENT', 220, 3), ('c1b', 1, 1, 0, 16, 'IN NO FILE', 50, 1)]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson98/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
