def s_hook(C, D, dur):
    E = [El(T('Gradle mastery', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(760, 150, ACC, 'cartcore 2.0', [('must ship today', TXT)], 52, 32), 100, 320, C['h2']))
    E.append(Pop(card(760, 150, BAD, 'does not build', [('and it is not safe to release', TXT)], 52, 32), 100, 500, C['h3']))
    E.append(Pop(card(760, 160, VIO, 'four problems', [('dependency, test, jar, secret', TXT)], 46, 30), 900, 410, C['h4']))
    E.append(Pop(card(1100, 140, GOOD, 'the whole domain in one job', [('start to finish, with proof', TXT)], 46, 30), 100, 720, C['h5']))
    E.append(takeaway('Fix it. Prove it. Publish it.', 900, C['h5'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
def s_scenario(C, D, dur):
    E = head('The job: four problems', 'Fix them in order. Prove each fix with a command.', C['a1'])
    it = [('1  Build fails', 'junit version 5.10.99 does not exist (O07)', BAD, 'a2'), ('2  Test fails', 'the discount is added, not taken off', WARN, 'a3'), ('3  Jar differs', 'a release must be reproducible (O05)', VIO, 'a4'), ('4  Key in file', 'secrets belong in the environment (O04)', PINK, 'a5')]
    for i, (n, t, col, cid) in enumerate(it): E.append(Pop(card(1700, 120, col, n, [(t, TXT)], 44, 32), 100, 330 + i * 150, C[cid]))
    E.append(takeaway('Same order every time: fix, prove, move on.', 960, C['a6'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab103.sh: cartcore 2.0. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Fix build', [('junit version,', TXT), ('then the test', TXT)], 'k2', BAD), ('2  Reproducible', [('same jar hash', TXT), ('on two builds', TXT)], 'k3', VIO), ('3  Publish', [('jar + pom in', TXT), ('the repository', TXT)], 'k4', WARN), ('4  No secret', [('key from the', TXT), ('environment', TXT)], 'k5', PINK), ('5  Report', [('problems: fixes:', TXT), ('cleanup: 3 lines', TXT)], 'k6', GOOD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab103.sh   and   shortcuts103.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab103.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts103.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, curl, python3, 1 GB, internet', PINK, 'i6'), ('6  Check + cleanup', 'lab check builds on your machine. lab down removes all.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('Build passes, tests green', 'q3x'), ('Same jar hash twice', 'q4x'), ('Jar + pom published', 'q5x'), ('No key in any file', 'q6x'), ('lab down, nothing left', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read what failed', PINK, 'z2'), ('2  Fix build', 'version, then the test', ACC, 'z3'), ('3  Reproducible', 'compare two hashes', VIO, 'z4'), ('4  Publish', 'key from environment', WARN, 'z5'), ('5  Report + check', 'three lines, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Dependency or task failure?', 'f12'), ('How is a jar made reproducible?', 'f13'), ('Why is a key in a file a problem?', 'f14'), ('What proves a release is safe?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Mastery evidence: MC11, the whole domain', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: MC12  Tomcat', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: fix, prove and publish', 'One continuous job, real Gradle 8.14.3 on cartcore 2.0.', 'p0', RB, [('f1', '1  build fails', 'library version not found', BAD), ('f3', '2  test fails', 'the discount is added', WARN), ('r1', '3  jar differs', 'two builds, two hashes', VIO), ('s1', '4  key in file', 'plain text in build.gradle', PINK), ('s5', '5  publish', 'key from the environment', GOOD), ('x2', '6  lab check', '5/5 passed', ACC)])
FN = dict(hook=s_hook, scenario=s_scenario, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(scenario=('board', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [
 ('f1b', 5, 1, 316, 932, 'VERSION 5.10.99 DOES NOT EXIST', 316, 6),
 ('f3b', 3, 1, 0, 521, 'THE FAILING TEST', 551, 3), ('f3b', 4, 1, 0, 427, 'ONE OF TWO FAILED', 457, 4),
 ('f5b', 2, 1, 0, 348, 'ALL GREEN', 378, 2),
 ('r1b', 2, 2, 0, 253, 'TWO DIFFERENT HASHES', 283, 2),
 ('r3b', 2, 2, 0, 253, 'THE SAME HASH TWICE', 283, 2),
 ('s1b', 1, 1, 316, 632, 'THE KEY, IN PLAIN TEXT', 662, 1),
 ('s3b', 2, 1, 0, 490, 'NO KEY, NO PUBLISH', 520, 2),
 ('s5b', 2, 1, 0, 506, 'ONLY THE END OF THE KEY', 536, 2), ('s5b', 3, 1, 0, 348, 'RELEASED', 378, 3),
 ('s6b', 2, 2, 0, 253, 'JAR AND POM', 283, 2),
 ('s7b', 1, 1, 0, 16, 'ZERO COPIES OF THE KEY', 46, 1),
 ('x2b', 1, 1, 0, 269, 'ALL FIVE PASSED', 299, 1)]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson103/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
