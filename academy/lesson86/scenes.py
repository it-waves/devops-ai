def s_hook(C, D, dur):
    E = [El(T('Package is a chain, not a step', 'x', 68), 100, 130, C['h1'])]
    chain = [('compile', ACC), ('test', VIO), ('package', GOOD)]
    E.append(Pop(card(560, 150, WARN, 'mvn package', [('one command', TXT)], 46, 28), 100, 300, C['h2']))
    for i, (n, col) in enumerate(chain): E.append(Pop(card(560, 100, col, '', [(f'{i + 1}   {n}', TXT)], 4, 44), 900, 270 + i * 120, C['h2'] + 1.5 + i * 1.6))
    E.append(takeaway('A fixed order. Learn it once.', 840, C['h3'], GOOD, 1700)); return E
def s_ideas(C, D, dur):
    E = head('The three life cycles', 'clean, default, site. Default is the one you live in.', C['u1']); E.append(ill(C['u1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 130, WARN, 'clean', [('delete target/', TXT)], 44, 30), 100, 330, C['u2']))
    E.append(Pop(card(540, 130, MUTED, 'site', [('documentation', TXT)], 44, 30), 100, 480, C['u1'] + 4))
    ph = [('validate', MUTED), ('compile', ACC), ('test', VIO), ('package', GOOD), ('verify', WARN), ('install', MUTED), ('deploy', MUTED)]
    for i, (n, col) in enumerate(ph): E.append(Pop(chip(n, col, 30, 18, 10), 700 + (i % 4) * 280, 345 + (i // 4) * 110, C['u3'] + 0.3 + 0.5 * i))
    E.append(Pop(card(1100, 120, GOOD, 'Run a phase, run every phase before it', [], 38), 700, 600, C['u4']))
    E.append(Pop(card(1100, 110, VIO, 'mvn package  =  validate, compile, test, package', [], 34), 700, 740, C['u5']))
    E.append(takeaway('A phase alone is an empty slot.', 940, C['u6'], WARN, 1700, 40)); return E
def s_bind(C, D, dur):
    E = head('Phases and goals', 'A plugin goal is bound to each phase.', C['b1'])
    rows = [('compile', 'compiler:compile', ACC, 'b2'), ('test', 'surefire:test', VIO, 'b3'), ('package', 'jar:jar', GOOD, 'b4'), ('before compile', 'resources:resources, testResources', WARN, 'b5')]
    for i, (p, g, col, cid) in enumerate(rows):
        y = 340 + i * 150
        E.append(Pop(card(520, 120, col, '', [(p, TXT)], 4, 40), 100, y, C[cid])); E.append(El(T('→', 'x', 64, col), 665, y + 20, C[cid] + 0.3))
        E.append(Pop(card(960, 120, col, '', [(g, TXT)], 4, 38), 760, y, C[cid] + 0.4))
    E.append(takeaway('Phase, then the goal bound to it.', 960, C['b6'], GOOD, 1700)); return E
def s_flags(C, D, dur):
    E = head('Five habits', 'Small flags, big difference.', C['g1'])
    it = [('1  clean package', 'a fresh build every time', ACC, 'g2'), ('2  -DskipTests', 'skips tests, never hides a failure', WARN, 'g3'), ('3  -B', 'batch mode: plain text for pipelines', VIO, 'g4'), ('4  -q', 'quiet: errors only', GOOD, 'g5'), ('5  First error', 'phase and goal tell you where', BAD, 'g6')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 120, col, n, [(s_, TXT)], 42, 32), 100, 330 + i * 140, C[cid]))
    return E

def s_task(C, D, dur):
    E = head('Your lab task', 'lab86.sh gives you a project whose tests fail. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab86.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Fix', [('mvn test', TXT), ('3 tests pass', TXT)], 'k3', BAD), ('2  goals.txt', [('mvn package', TXT), ('save the goals', TXT)], 'k4', ACC), ('3  skip.txt', [('-DskipTests', TXT), ('tests are skipped', TXT)], 'k5', VIO), ('4  Verify', [('mvn clean verify', TXT), ('makes the jar', TXT)], 'k6', GOOD), ('5  Clean', [('mvn clean', TXT), ('target is gone', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('List the default phases', 'q3'), ('Why package runs tests', 'q4'), ('Goals for compile/test/package', 'q5'), ('What clean deletes', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Read', 'mvn test, first failure only', ACC, 'z3'), ('3  Fix', 'until 3 tests pass', VIO, 'z4'), ('4  Save', 'goals.txt and skip.txt', WARN, 'z5'), ('5  Clean, check', 'mvn clean, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('The default phases, in order?', 'f12'), ('Why does package run tests?', 'f13'), ('Which goal is bound to package?', 'f14'), ('What does clean delete?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC10-O02', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: plugins and profiles', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_life = _lab('Live: compile, test, package, clean', 'One phase at a time, and what each leaves behind.', 'p0', RB, [('p1', 'mvn compile', 'resources, compiler:compile', ACC), ('p3', 'mvn test', 'runs compile first, then surefire:test', VIO), ('p4', 'mvn package', 'adds jar:jar', GOOD), ('p5', 'ls target', 'jar, test-classes, reports', WARN), ('p6', '-DskipTests', 'Tests are skipped', PINK), ('p7', 'mvn clean', 'target/ is deleted', BAD)])
s_fail = _lab('When a phase fails', 'A broken test stops the chain before the jar.', 'x0', RB, [('x1', 'sed ... Hi, ...', 'the code and test now disagree', WARN), ('x2', 'mvn package', 'surefire:test fails', BAD), ('x3', 'ls target/*.jar', 'no jar: later phases never ran', BAD), ('x4', 'sed ... Hello, ...', 'fix the greeting', GOOD), ('x5', 'mvn clean verify', 'BUILD SUCCESS', GOOD)])
FN = dict(hook=s_hook, ideas=s_ideas, bind=s_bind, life=s_life, fail=s_fail, flags=s_flags, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ideas=('gear', ACC), bind=('gear', VIO), flags=('board', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'life': [('p1b', 2, 2, 0, 860, 'COMPILE GOALS'), ('p2b', 1, 1, 0, 620, 'CLASSES ONLY'), ('p3b', 6, 2, 0, 770, 'SUREFIRE = TESTS'), ('p4b', 7, 1, 0, 770, 'JAR = PACKAGE'), ('p5b', 1, 3, 0, 860, 'ALL OUTPUT', 872, 2), ('p6b', 1, 1, 0, 400, 'TESTS SKIPPED'), ('p7b', 2, 1, 0, 740, 'ONE GOAL'), ('p8b', 1, 1, 0, 815, 'GONE')],
 'fail': [('x2b', 7, 2, 0, 760, 'TEST FAILED'), ('x3b', 1, 1, 0, 894, 'NO JAR'), ('x5b', 2, 2, 0, 700, 'ALL GREEN')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson86/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
