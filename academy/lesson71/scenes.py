def s_hook(C, D, dur):
    E = [El(T('Same code, three places', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(840, 140, BAD, 'Edit the code per place?', [('you will ship the wrong settings', TXT)], 44, 32), 100, 330, C['h1'] + 1.2))
    E.append(Pop(card(840, 110, WARN, 'Laptop, test, production', [], 44, 32), 100, 500, C['h2']))
    E.append(Pop(card(840, 110, WARN, 'One build, different settings', [], 44, 32), 100, 630, C['h2'] + 1.8))
    mv = [('Config', 'lives outside the code', ACC), ('Env variables', 'override the file', VIO), ('Feature flags', 'switch features on and off', GOOD), ('Fail fast', 'refuse a bad setting', PINK)]
    for i, (n, s_, col) in enumerate(mv): E.append(Pop(card(420, 170, col, n, [(s_, TXT)], 38, 26, True), 1000 + (i % 2) * 440, 330 + (i // 2) * 200, C['h3'] + 2.0 + i * 2.2))
    E.append(Pop(badge('laptop', F('x', 52), INK, ACC, padx=34, pady=18), 100, 800, C['h4'])); E.append(Pop(badge('test', F('x', 52), INK, WARN, padx=34, pady=18), 380, 800, C['h4'] + 0.6)); E.append(Pop(badge('prod', F('x', 52), INK, GOOD, padx=34, pady=18), 600, 800, C['h4'] + 1.2))
    E.append(takeaway('Change behaviour, without changing code.', 980, C['h4'] + 1.4, GOOD, 1700)); return E
s_layers = _lab('Config: three layers', 'Default in the code, a settings file, the environment.', 'y1', RB, [('y2', './start.sh', 'start the shop', ACC), ('y3', 'cat app.conf', 'a plain text file', VIO), ('y5', '/api/config', 'what the API really uses', WARN), ('y6', 'app.conf or default', 'each value shows its source', GOOD), ('y7', 'three layers', 'default, file, environment', PINK)])
s_env = _lab('Environment variables', 'A setting you hand to one program at start.', 'e1', RB, [('e2', 'STORE_NAME=... ./start.sh', 'a variable before the command', ACC), ('e4', '/api/config', 'ask the API again', VIO), ('e5', 'environment wins', 'environment, file, default', GOOD), ('e6', './start.sh', 'start with no variable', WARN), ('e8', 'back to the file', 'same build, other settings', PINK)])
s_flags = _lab('Feature flags', 'Switch a feature on or off, without new code.', 'f1', RB, [('f2', 'price: 39.0', 'flag off: the old price', ACC), ('f4', 'FLAG_DISCOUNT=on', 'switch it on', WARN), ('f6', 'price: 35.1', 'ten percent off', GOOD), ('f7', 'deploy is not release', 'flip it back in seconds', PINK)])
s_failfast = _lab('Fail fast', 'A bad setting must stop the program at the door.', 'x1', RB, [('x2', 'PORT=abc', 'not a number', BAD), ('x3', 'config error', 'a clear message', WARN), ('x4', 'echo $?', 'the exit code', VIO), ('x5', 'exit 1', 'not zero means failure', GOOD)])
def s_models(C, D, dur):
    E = head('Twelve factor ideas', 'Settings outside the code, one build everywhere.', C['m1']); E.append(ill(C['m1'] + 0.2, 1400, 170))
    E.append(Pop(card(840, 150, ACC, 'Config outside code', [('a file, or the environment', TXT)], 40, 30), 100, 340, C['m2']))
    E.append(Pop(card(840, 150, VIO, 'Order of power', [('environment, then file, then default', TXT)], 40, 30), 980, 340, C['m3']))
    E.append(Pop(card(840, 190, WARN, 'One build, everywhere', [('build once, run in test and prod', TXT), ('only the settings change', TXT)], 40, 28), 100, 530, C['m4']))
    E.append(Pop(card(840, 190, GOOD, 'Feature flags', [('ship dark, release by flipping', TXT), ('roll back by flipping back', TXT)], 40, 28), 980, 530, C['m5']))
    E.append(Pop(card(840, 140, PINK, 'Secrets', [('never in the file, never in git', TXT)], 40, 28), 100, 750, C['m6']))
    E.append(Pop(card(840, 140, BAD, 'Fail fast', [('check every setting at startup', TXT)], 40, 28), 980, 750, C['m7']))
    E.append(takeaway('Docker, Kubernetes and clouds inject these for you.', 950, C['m8'], WARN, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab71.sh starts CloudCart. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab71.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Env', 'Blue Shop, save env.txt', 'k3', VIO), ('2  Flag', 'discount on, save flag.txt', 'k4', WARN), ('3  Fail fast', 'bad PORT, exit code', 'k5', BAD), ('4  File', 'CURRENCY=EUR in app.conf', 'k6', PINK), ('5  No code', 'api.py stays untouched', 'k7', ACC), ('lab check', 'five PASS lines', 'k8', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 230, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Config outside the code', 'q3'), ('Environment, file, default', 'q4'), ('Flags: deploy is not release', 'q5'), ('Fail fast and exit codes', 'q6'), ('lab down, nothing listening', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Env', 'Blue Shop, env.txt', ACC, 'z3'), ('3  Flag', 'discount on, flag.txt', VIO, 'z4'), ('4  Break', 'bad PORT, exit code', BAD, 'z5'), ('5  File', 'CURRENCY=EUR', WARN, 'z6'), ('6  Check', 'lab check, lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which wins: env, file or default?', 'f12'), ('Flip a feature without a deploy?', 'f13'), ('Why one build everywhere?', 'f14'), ('Bad setting: what should happen?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC08-O05', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: stateful and stateless', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, layers=s_layers, env=s_env, flags=s_flags, failfast=s_failfast, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(layers=('doc', ACC), env=('code', VIO), flags=('test', GOOD), failfast=('test', BAD), models=('board', ACC), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'layers': [('y6', 2, 1, 0, 620, 'FROM THE FILE'), ('y6', 4, 1, 0, 512, 'DEFAULT')],
 'env': [('e5', 2, 1, 0, 680, 'ENVIRONMENT WINS')],
 'flags': [('f3', 2, 1, 0, 604, 'FLAG OFF'), ('f6', 2, 1, 0, 604, 'FLAG ON')],
 'failfast': [('x3', 1, 1, 0, 710, 'FAILS FAST'), ('x5', 1, 1, 0, 40, 'NOT ZERO')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson71/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
