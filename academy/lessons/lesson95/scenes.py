def s_hook(C, D, dur):
    E = [El(T('Gradle. The other big build tool.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(760, 140, ACC, 'a real Gradle project', [('read it file by file', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(760, 160, VIO, '4 ideas', [('project · script · wrapper · graph', TXT)], 52, 30), 100, 480, C['h3']))
    E.append(Pop(card(760, 160, WARN, 'live on Gradle 8.14.3', [('from simple to your own task', TXT)], 46, 30), 900, 440, C['h4']))
    E.append(Pop(card(1100, 140, GOOD, 'then you do it alone', [('a checker judges you', TXT)], 46, 30), 100, 700, C['h5']))
    E.append(takeaway('Everything Gradle does is a task.', 900, C['h6'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f

s_parts = _list('The four ideas of Gradle', 'Every build is made of these.', 'a1', [('1  the project', 'a folder with a settings file', ACC, 'a2'), ('2  the build script', 'build.gradle: plugins, version, libraries', VIO, 'a3'), ('3  the wrapper', 'gradlew runs the exact Gradle version', GOOD, 'a4'), ('4  the task graph', 'tasks depend on other tasks', WARN, 'a5')], 'Maven fixes the lifecycle. Gradle lets you shape the graph.', 'a6', h=125, gap=145)
def s_task(C, D, dur):
    E = head('Your lab task', 'lab95.sh: a small Gradle project. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Version', [('set 1.1', TXT), ('build the jar', TXT)], 'k2', ACC), ('2  Task', [('add report', TXT), ('prints name, version', TXT)], 'k3', WARN), ('3  Depends', [('report needs build', TXT), ('dependsOn', TXT)], 'k4', VIO), ('4  Graph', [('--dry-run', TXT), ('save graph.txt', TXT)], 'k5', GOOD), ('5  Notes', [('3 lines', TXT), ('settings, wrapper, task', TXT)], 'k6', PINK)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1']); E.append(ill(C['i1'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab95.sh   and   shortcuts95.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab95.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts95.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, curl, python3, 1 GB memory, internet', PINK, 'i6'), ('6  Cleanup', 'lab down removes everything. Your own VM only.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Version from the script', 'q3'), ('Used the wrapper', 'q4'), ('graph.txt in order', 'q5'), ('Notes in your words', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, task file', PINK, 'z2'), ('2  Look', 'open every file', ACC, 'z3'), ('3  Version', 'change it, build', VIO, 'z4'), ('4  Task', 'report + dependsOn', WARN, 'z5'), ('5  Graph + notes', 'then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    _unused = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Build', 'each project, first error', ACC, 'z3'), ('3  Name it', 'the cause, in your words', VIO, 'z4'), ('4  Fix', 'fix the cause, rebuild', WARN, 'z5'), ('5  Notes + check', 'report.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which file names the project?', 'f12'), ('What does the wrapper do?', 'f13'), ('What is a task graph?', 'f14'), ('What does up to date mean?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC11-O01 Gradle', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: build, test, dependencies', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: project, wrapper, script, task graph', 'A real Gradle 8.14.3, one terminal.', 'p0', RB, [('p1', '1  the project', 'settings.gradle names it', ACC), ('g1', '2  build script', 'plugin, version, libraries', VIO), ('w1', '3  the wrapper', 'the exact Gradle version', GOOD), ('t1', '4  task graph', 'jar runs before build', WARN), ('r1', '5  up to date', 'skip unchanged work', PINK), ('c1', '6  your own task', 'report depends on build', ACC)])
FN = dict(hook=s_hook, parts=s_parts, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(parts=('board', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [('p1b', 1, 1, 0, 1005, 'THE PROJECT FILES', 400, 2), ('s1b', 1, 1, 0, 455, 'PROJECT NAME', 485, 2), ('g1b', 2, 1, 0, 205, 'JAVA PLUGIN', 235, 3), ('w1b', 2, 2, 0, 1110, 'EXACT VERSION', 400, 4), ('v1b', 1, 2, 0, 900, 'GRADLE 8.14.3', 930, 3), ('t1b', 2, 1, 0, 645, 'THE TASK YOU USE MOST', 675, 2), ('g2b', 1, 11, 0, 300, 'THE TASK GRAPH', 330, 1), ('r1b', 1, 2, 0, 480, '2 EXECUTED', 510, 3), ('r2b', 1, 2, 0, 520, '2 UP-TO-DATE', 550, 3), ('e2b', 1, 1, 0, 535, 'NEW VERSION', 565, 1), ('c2b', 1, 1, 0, 190, 'YOUR TASK RAN', 345, 2), ('c3b', 1, 2, 0, 240, 'BUILD FIRST', 270, 3)]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson95/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
