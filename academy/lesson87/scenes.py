def s_hook(C, D, dur):
    E = [El(T('Same code. Two builds. Two jars.', 'x', 68), 100, 130, C['h1'])]
    E.append(Pop(card(560, 150, WARN, 'build 1', [('jar  934f0400', TXT)], 46, 28), 100, 300, C['h1'] + 2.5))
    E.append(Pop(card(560, 150, BAD, 'build 2', [('jar  7e4f4f6e', TXT)], 46, 28), 100, 480, C['h1'] + 3.5))
    for i, (n, col) in enumerate([('dates inside the jar', VIO), ('settings per machine', ACC), ('tool versions', GOOD)]): E.append(Pop(card(760, 100, col, '', [(n, TXT)], 4, 40), 900, 300 + i * 130, C['h2'] + 1.0 + i * 2.0))
    E.append(takeaway('Tighten the loose ends.', 840, C['h3'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
s_plug = _list('Plugins', 'Maven does little. Plugins do the work.', 'a1', [('Goals', 'compiler:compile, surefire:test, jar:jar run inside phases', ACC, 'a2'), ('Configuration', 'tune a plugin inside its own configuration block', VIO, 'a3'), ('Manifest mainClass', 'tells java -jar where to start', WARN, 'a4')], 'Pin every plugin version.', 'a5')
s_props = _list('Properties', 'Define once, use everywhere.', 'r1', [('Define', '<app.env>dev</app.env> inside properties', ACC, 'r2'), ('Use', '${app.env} anywhere in the pom or in filtered files', VIO, 'r3'), ('Filtering', 'copies a file into the jar and fills in the ${names}', GOOD, 'r4')], 'The command line beats the pom:  -Dapp.greeting=Hi', 'r5')
s_prof = _list('Profiles', 'A named set of changes, switched on on demand.', 'f1', [('Define', 'a profile with an id and its own properties', ACC, 'f1'), ('Switch on', 'mvn package -Pprod', VIO, 'f2'), ('Keep few and small', 'dev vs prod differences only', GOOD, 'f3')], 'No passwords in the pom.', 'f4')
def s_task(C, D, dur):
    E = head('Your lab task', 'lab87.sh gives a jar that cannot run. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab87.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Plugin', [('jar plugin', TXT), ('mainClass', TXT)], 'k3', ACC), ('2  Properties', [('app.env, app.greeting', TXT), ('filtering true', TXT)], 'k4', VIO), ('3  Profile', [('id prod', TXT), ('-Pprod', TXT)], 'k5', WARN), ('4  Timestamp', [('outputTimestamp', TXT), ('identical jar', TXT)], 'k6', GOOD), ('5  sha.txt', [('sha256sum', TXT), ('save the hash', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', BAD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('What plugin config does', 'q3'), ('-D beats the pom', 'q4'), ('Switch on a profile', 'q5'), ('Why builds differ, the fix', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Manifest', 'main class, run the jar', ACC, 'z3'), ('3  Properties', 'values and filtering', VIO, 'z4'), ('4  Profile', 'prod, and the timestamp', WARN, 'z5'), ('5  Hash, check', 'sha.txt, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does plugin config do?', 'f12'), ('Which wins: pom or -D?', 'f13'), ('How to switch on a profile?', 'f14'), ('What makes a build reproducible?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC10-O03', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: dependency trees', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_cfg = _lab('Live: plugin, property, profile', 'One pom, three ways to change a build.', 'p0', RB, [('p1', 'sed -n 8,19p pom.xml', 'properties and the prod profile', VIO), ('p3', 'mvn package, java -jar', '[dev] Hello', GOOD), ('p4', '-Pprod', '[prod] Hello', WARN), ('p5', '-Dapp.greeting=Hi', 'command line beats the pom', PINK), ('p6', 'unzip -p ... MANIFEST.MF', 'Main-Class from the jar plugin', ACC)])
s_repro = _lab('Reproducible builds', 'Same input, same bytes.', 'y0', RB, [('y1', 'sha256sum  build 1', 'a fingerprint of the jar', VIO), ('y2', 'sha256sum  build 2', 'different: build time inside', BAD), ('y3', 'outputTimestamp', 'a fixed date, one property', WARN), ('y4', 'sha256sum  build 3', 'a fingerprint', GOOD), ('y5', 'sha256sum  build 4', 'identical to build 3', GOOD)])
FN = dict(hook=s_hook, plug=s_plug, props=s_props, prof=s_prof, cfg=s_cfg, repro=s_repro, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(plug=('gear', ACC), props=('board', VIO), prof=('gear', WARN), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'repro': [('y1b', 2, 1, 0, 250, 'BUILD 1'), ('y2b', 2, 1, 0, 250, 'DIFFERENT'), ('y3b', 4, 2, 0, 1070, '', 0, 0), ('y4b', 2, 1, 0, 250, 'BUILD 3'), ('y5b', 2, 1, 0, 250, 'SAME HASH')],
 'cfg': [('p1b', 3, 2, 0, 560, 'TWO PROPERTIES'), ('p1b', 8, 4, 0, 830, 'PROFILE'), ('p2b', 1, 2, 0, 370, 'FILLED IN LATER'), ('p3b', 1, 1, 0, 400, 'DEV'), ('p4b', 2, 1, 0, 420, 'PROD'), ('p5b', 2, 1, 0, 360, 'HI WINS'), ('p6b', 2, 1, 0, 430, 'MAIN CLASS SET')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson87/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
