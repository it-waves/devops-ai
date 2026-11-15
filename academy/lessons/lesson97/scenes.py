def s_hook(C, D, dur):
    E = [El(T('Libraries. Versions. Plug ins.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(760, 140, ACC, 'one script', [('libraries and plug ins', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(760, 160, VIO, '3 problems', [('scope · versions · publish', TXT)], 52, 30), 100, 480, C['h3']))
    E.append(Pop(card(760, 160, WARN, 'live on Gradle 8.14.3', [('fix them on a project', TXT)], 46, 30), 900, 440, C['h4']))
    E.append(Pop(card(1100, 140, GOOD, 'then you do it alone', [('a checker judges you', TXT)], 46, 30), 100, 700, C['h5']))
    E.append(takeaway('Say what you need, and where.', 900, C['h6'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f

s_parts = _list('Four ideas of dependencies', 'Every Gradle build has these.', 'a1', [('1  repositories', 'where Gradle looks: mavenCentral, Nexus', ACC, 'a2'), ('2  scopes', 'implementation ships, testImplementation tests', VIO, 'a3'), ('3  version catalog', 'one file: libs.versions.toml', GOOD, 'a4'), ('4  plugins', 'java builds, maven-publish publishes', WARN, 'a5')], 'Maven uses a pom. Gradle uses a script.', 'a6', h=125, gap=145)
def s_task(C, D, dur):
    E = head('Your lab task', 'lab97.sh: a project with 3 problems. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Scope', [('JUnit ships', TXT), ('make it test-only', TXT)], 'k2', ACC), ('2  Catalog', [('libs.versions.toml', TXT), ('use libs.*', TXT)], 'k3', WARN), ('3  Publish', [('maven-publish', TXT), ('gradlew publish', TXT)], 'k4', VIO), ('4  The pom', [('commons-text yes', TXT), ('junit no', TXT)], 'k5', GOOD), ('5  Notes', [('3 lines', TXT), ('catalog, published, scope', TXT)], 'k6', PINK)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab97.sh   and   shortcuts97.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab97.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts97.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, curl, python3, 1 GB memory, internet', PINK, 'i6'), ('6  Cleanup', 'lab down removes everything. Your own VM only.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('JUnit is test-only', 'q3x'), ('Versions in the catalog', 'q4x'), ('publish really ran', 'q5x'), ('Notes name the files', 'q6x'), ('lab down, nothing left', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, task file', PINK, 'z2'), ('2  Scope', 'JUnit: test only, prove it', ACC, 'z3'), ('3  Catalog', 'write it, use it', VIO, 'z4'), ('4  Publish', 'plugin, block, publish', WARN, 'z5'), ('5  Notes', 'read the pom, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    _unused = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Build', 'each project, first error', ACC, 'z3'), ('3  Name it', 'the cause, in your words', VIO, 'z4'), ('4  Fix', 'fix the cause, rebuild', WARN, 'z5'), ('5  Notes + check', 'report.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('implementation vs testImplementation?', 'f12'), ('What does a version catalog give you?', 'f13'), ('Which plugin adds publish? Where did it go?', 'f14'), ('Why is JUnit missing from the pom?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC11-O03 Gradle', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: environment and secrets', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: scopes, a version catalog, publishing', 'A real Gradle 8.14.3 and real Maven Central libraries.', 'p0', RB, [('r1', '1  repositories', 'mavenCentral: where it looks', ACC), ('d1', '2  dependencies', 'JUnit is in the wrong scope', VIO), ('j1', '3  prove it', 'junit on the runtime classpath', BAD), ('v1', '4  the catalog', 'one file for every version', WARN), ('m1', '5  a plugin', 'maven-publish adds publish', GOOD), ('g1', '6  publish', 'jar and pom to build/repo', PINK), ('q2', '7  the pom', 'commons-text yes, junit no', ACC)])
FN = dict(hook=s_hook, parts=s_parts, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(parts=('board', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [('r1b', 2, 1, 55, 270, 'WHERE IT LOOKS', 300, 2), ('d1b', 4, 1, 55, 1000, 'A TEST LIBRARY IN THE WRONG SCOPE', 150, 8), ('j1b', 2, 1, 0, 50, 'JUNIT SHIPS', 80, 2), ('j2b', 2, 1, 0, 30, 'GONE FROM RUNTIME', 60, 2), ('v3b', 2, 1, 0, 325, 'THE NUMBER', 355, 2), ('v3b', 5, 2, 0, 980, 'THE NAME, BY REFERENCE', 300, 8), ('u2b', 1, 1, 328, 596, 'READS FROM THE CATALOG', 625, 1), ('u3b', 1, 1, 0, 300, 'STILL GREEN', 330, 1), ('m2b', 3, 1, 55, 320, 'NEW PLUGIN', 350, 3), ('g1b', 1, 1, 0, 300, 'PUBLISH CAME FROM THE PLUGIN', 330, 1), ('q1b', 2, 3, 0, 830, 'JAR, POM, MODULE FILE', 150, 6), ('q2b', 3, 2, 85, 630, 'COMMONS ONLY, NO JUNIT', 660, 3)]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson97/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
