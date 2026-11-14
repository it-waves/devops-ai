def s_hook(C, D, dur):
    E = [El(T('It worked yesterday. Today it fails.', 'x', 66), 100, 130, C['h1'])]
    E.append(Pop(card(700, 140, ACC, 'your pom', [('liba   libb', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(700, 140, WARN, 'liba needs', [('util 1.0', TXT)], 46, 30), 100, 480, C['h2'] + 2.5))
    E.append(Pop(card(700, 140, BAD, 'libb needs', [('util 2.0', TXT)], 46, 30), 100, 660, C['h2'] + 4.0))
    E.append(Pop(card(760, 180, VIO, 'Only one wins', [('Which one?', TXT)], 52, 40), 900, 440, C['h3']))
    E.append(takeaway('Read the tree. Choose on purpose.', 900, C['h4'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
def s_trans(C, D, dur):
    E = head('Transitive dependencies', 'Libraries need libraries.', C['a1']); E.append(ill(C['a1'] + 0.2, 1400, 170))
    E.append(Pop(card(500, 120, ACC, 'your project', [], 40), 100, 360, C['a1']))
    E.append(Pop(card(400, 110, VIO, 'liba 1.0', [('direct', TXT)], 40, 28), 760, 330, C['a3'])); E.append(Pop(card(400, 110, VIO, 'libb 1.0', [('direct', TXT)], 40, 28), 760, 470, C['a3']))
    E.append(Pop(card(400, 110, WARN, 'util 1.0', [('transitive', TXT)], 40, 28), 1300, 330, C['a3'] + 1.5)); E.append(Pop(card(400, 110, BAD, 'util 2.0', [('transitive', TXT)], 40, 28), 1300, 470, C['a3'] + 3.0))
    E.append(Pop(card(1700, 120, WARN, 'Only one util can be on the classpath', [], 40), 100, 700, C['a4']))
    E.append(takeaway('A clash: a version conflict.', 900, C['a5'], BAD, 1700)); return E
def s_rules(C, D, dur):
    E = head('How Maven chooses', 'Not the newest. The nearest.', C['b1'])
    E.append(Pop(card(1700, 140, ACC, '1  Nearest wins', [('closest to your project in the tree', TXT)], 44, 32), 100, 330, C['b1']))
    E.append(Pop(card(1700, 140, VIO, '2  Tie: first declared wins', [('same distance, the earlier dependency in the pom', TXT)], 44, 32), 100, 500, C['b2']))
    E.append(Pop(card(1700, 140, WARN, 'Here: a tie, liba is first', [('so util 1.0 wins; the code needs 2.0', TXT)], 44, 32), 100, 670, C['b3']))
    E.append(takeaway('The newest does not win.', 900, C['b4'], BAD, 1700)); return E
s_fixes = _list('Three ways to fix it', 'Pin, exclude, or declare.', 'x1', [('1  dependencyManagement', 'pin the version for the whole project, in one place', GOOD, 'x2'), ('2  exclusion', 'from this dependency, leave that library out', VIO, 'x3'), ('3  declare it directly', 'a direct dependency is nearest, so it wins', WARN, 'x4')], 'We use the first one.', 'x5')
def s_task(C, D, dur):
    E = head('Your lab task', 'lab88.sh gives a build with a version conflict. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab88.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Find', [('-Dverbose | grep omitted', TXT), ('conflict.txt', TXT)], 'k3', ACC), ('2  Pin', [('dependencyManagement', TXT), ('util 2.0', TXT)], 'k4', VIO), ('3  Build', [('mvn clean package', TXT), ('BUILD SUCCESS', TXT)], 'k5', GOOD), ('4  tree.txt', [('util 2.0 only', TXT), ('no util 1.0', TXT)], 'k6', WARN), ('5  why.txt', [('one sentence', TXT), ('nearest or first', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', BAD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Read a dependency tree', 'q3'), ('Nearest wins, then first', 'q4'), ('Three ways to fix', 'q5'), ('Find it with -Dverbose', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Find', 'conflict.txt, before any fix', ACC, 'z3'), ('3  Pin', 'dependencyManagement block', VIO, 'z4'), ('4  Build', 'package, then tree.txt', WARN, 'z5'), ('5  Explain, check', 'why.txt, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What is a transitive dependency?', 'f12'), ('Which version wins?', 'f13'), ('Two ways to fix a conflict?', 'f14'), ('Which flag shows omitted?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC10-O04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: package as a WAR', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_tree = _lab('Live: find and fix a conflict', 'Read the tree, see what was omitted, pin the version.', 't0', RB, [('t1', 'dependency:tree', 'util 1.0 under liba', VIO), ('t2', '-Dverbose | grep omitted', 'util 2.0 omitted for conflict', BAD), ('t3', '-Dincludes=...util', 'only the path to util', ACC), ('t4', 'mvn compile', 'cannot find symbol: shout', BAD), ('t6', 'dependencyManagement', 'pin util 2.0', WARN), ('t7', 'dependency:tree', 'util 2.0 now', GOOD), ('t8', 'mvn compile', 'built', GOOD)])
FN = dict(hook=s_hook, trans=s_trans, rules=s_rules, fixes=s_fixes, tree=s_tree, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(trans=('link', ACC), rules=('gear', VIO), fixes=('gear', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'tree': [('t1b', 3, 1, 0, 800, 'UTIL 1.0 WINS'), ('t2b', 2, 2, 0, 1070, 'OMITTED: LOST'), ('t3b', 4, 1, 0, 800, 'ONE PATH'), ('t4b', 2, 2, 0, 1070, 'THE REAL ERROR'), ('t7b', 3, 1, 0, 800, 'UTIL 2.0 NOW'), ('t8b', 1, 1, 0, 100, 'BUILT')]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson88/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
