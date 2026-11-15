def s_hook(C, D, dur):
    E = [El(T('Maven or Gradle?', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(760, 150, ACC, 'Maven', [('pom.xml', TXT)], 52, 32), 100, 320, C['h2']))
    E.append(Pop(card(760, 150, VIO, 'Gradle', [('build.gradle', TXT)], 52, 32), 100, 500, C['h2'] + 0.4))
    E.append(Pop(card(760, 160, WARN, 'same project', [('same library, same jar', TXT)], 46, 30), 900, 410, C['h4']))
    E.append(Pop(card(1100, 140, GOOD, 'decide with evidence', [('not with a feeling', TXT)], 46, 30), 100, 720, C['h3']))
    E.append(takeaway('Build both. Then choose.', 900, C['h5'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
def s_parts(C, D, dur):
    E = head('Same job, two tools', 'Compile, test, fetch libraries, make a jar.', C['a1'])
    E.append(Pop(badge('MAVEN', F('x', 44), INK, ACC, padx=40, pady=14, r=26), 480, 320, C['a1'] + 0.3)); E.append(Pop(badge('GRADLE', F('x', 44), INK, VIO, padx=40, pady=14, r=26), 1160, 320, C['a1'] + 0.6))
    rows = [('build file', 'pom.xml  (data)', 'build.gradle  (code)', 'a2', 'a3'), ('how it runs', 'fixed life cycle', 'graph of tasks', 'a4', 'a4'), ('libraries', 'Maven Central', 'Maven Central', 'a5', 'a5'), ('jar goes to', 'target/', 'build/libs/', 'a6', 'a6')]
    for i, (n, m, g, c1, c2) in enumerate(rows):
        y = 410 + i * 120
        E.append(El(T(n, 'b', 30, MUTED, maxw=340), 100, y + 30, C[c1] if i != 1 else C['a4']))
        E.append(Pop(card(620, 100, ACC, '', [(m, TXT)], 4, 34), 480, y, C[c1])); E.append(Pop(card(620, 100, VIO, '', [(g, TXT)], 4, 34), 1160, y, C[c2] + (0.0 if c1 != c2 else 0.5)))
    E.append(takeaway('Same libraries. Different style.', 940, C['a6'], GOOD, 1700)); return E
def s_decide(C, D, dur):
    E = head('How to choose', 'Both work. Choose on evidence.', C['v1'])
    E.append(Pop(card(850, 190, ACC, 'Pick Maven', [('standard layout, readable file', TXT)], 52, 32), 100, 330, C['v2']))
    E.append(Pop(card(850, 190, VIO, 'Pick Gradle', [('custom steps, big builds, cache', TXT)], 52, 32), 1000, 330, C['v3']))
    E.append(Pop(card(1750, 150, WARN, 'Measure, do not guess', [('on a small project both take seconds', TXT)], 46, 30), 100, 570, C['v4']))
    E.append(Pop(card(1750, 150, GOOD, 'In this bootcamp: Maven by default', [('Gradle only where a lesson says so', TXT)], 46, 30), 100, 760, C['v5'])); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab102.sh: one project, two build files. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Maven', [('add the library', TXT), ('to pom.xml', TXT)], 'k2', ACC), ('2  Gradle', [('add the library', TXT), ('to build.gradle', TXT)], 'k3', VIO), ('3  Evidence', [('second Gradle run', TXT), ('says UP-TO-DATE', TXT)], 'k4', WARN), ('4  Same jars', [('Main and Cart in', TXT), ('both jars', TXT)], 'k5', BAD), ('5  Decision', [('maven: gradle:', TXT), ('choice: 3 lines', TXT)], 'k6', GOOD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab102.sh   and   shortcuts102.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab102.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts102.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, Maven, curl, python3, 1 GB, internet', PINK, 'i6'), ('6  Check + cleanup', 'lab check builds on your machine. lab down removes all.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('Maven builds the jar', 'q3x'), ('Gradle builds the jar', 'q4x'), ('Second run: UP-TO-DATE', 'q5x'), ('decision.txt: 3 lines', 'q6x'), ('lab down, nothing left', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read both files', PINK, 'z2'), ('2  Maven', 'add library, mvn package', ACC, 'z3'), ('3  Gradle', 'add library, build', VIO, 'z4'), ('4  Evidence', 'save the second run', WARN, 'z5'), ('5  Decide + check', 'three lines, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which file describes each project?', 'f12'), ('Where does each tool put the jar?', 'f13'), ('What does UP-TO-DATE mean?', 'f14'), ('When Maven? When Gradle?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC11-O08 Maven vs Gradle', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: Gradle mastery lesson', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: the same project, built both ways', 'Real Maven 3.9 and Gradle 8.14.3 on the CloudCart cartcore project.', 'p0', RB, [('w1', '1  two build files', '12 lines of XML, 10 of Gradle', ACC), ('m1', '2  library, Maven', 'five lines in the pom', VIO), ('m2', '3  mvn package', 'BUILD SUCCESS', GOOD), ('g1', '4  library, Gradle', 'one line in build.gradle', WARN), ('g2', '5  gradlew build', 'jar in build/libs', PINK), ('r1', '6  second run', 'both skip the work', BAD)])
FN = dict(hook=s_hook, parts=s_parts, live=s_live, decide=s_decide, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(parts=('board', ACC), decide=('test', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [
 ('w1b', 1, 1, 126, 157, '12 LINES OF XML', 220, 1), ('w1b', 2, 1, 204, 236, '10 LINES OF GRADLE', 266, 2),
 ('w2b', 2, 3, 94, 700, 'THE LIBRARY NAME', 730, 3),
 ('m2b', 1, 1, 110, 314, 'MAVEN BUILT IT', 344, 1), ('m2b', 2, 1, 298, 424, 'ABOUT 2 SECONDS', 454, 2),
 ('g2b', 1, 1, 0, 346, 'GRADLE BUILT IT', 376, 1), ('g2b', 2, 1, 0, 471, 'TWO TASKS RAN', 501, 2),
 ('g3b', 1, 1, 0, 251, 'SAME NAME, OTHER FOLDER', 281, 1),
 ('r1b', 1, 1, 110, 863, 'MAVEN SKIPS WORK TOO', 344, 2),
 ('r2b', 1, 7, 0, 480, 'EVERY STEP SKIPPED', 510, 4)]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson102/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
