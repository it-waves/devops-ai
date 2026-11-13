def s_hook(C, D, dur):
    E = [El(T('One file runs the build', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(560, 150, ACC, 'pom.xml', [('what Maven reads', TXT)], 46, 28), 100, 300, C['h2']))
    its = [('name', 'h2', 0.8, VIO), ('folders', 'h2', 2.8, WARN), ('libraries', 'h2', 4.6, GOOD), ('build steps', 'h2', 6.2, PINK)]
    for i, (n, cid, dt, col) in enumerate(its): E.append(Pop(card(560, 100, col, '', [(n, TXT)], 4, 44), 900, 270 + i * 120, C[cid] + dt))
    E.append(takeaway('Read the pom. Understand the build.', 840, C['h3'], GOOD, 1700)); return E
def s_ideas(C, D, dur):
    E = head('Anatomy of a pom', 'Four parts matter first.', C['u1']); E.append(ill(C['u1'] + 0.2, 1400, 170))
    it = [('1  Coordinates', 'groupId, artifactId, version: the GAV that names the project.', ACC, 'u2'), ('2  Properties', 'settings written once, like the Java release.', VIO, 'u3'), ('3  Dependencies', 'libraries by their own coordinates, plus a scope.', GOOD, 'u4'), ('4  Build', 'plugins that compile, test, package. Pin the versions.', WARN, 'u5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 135, col, n, [(s_, TXT)], 44, 34), 100, 330 + i * 160, C[cid]))
    E.append(takeaway('Convention over configuration.', 985, C['u6'], GOOD, 1700, 38)); return E
s_tour = _lab('Layout and coordinates', 'Read the pom, see the folders, hit the first error.', 't0', RB, [('t1', 'head -16 pom.xml', 'the coordinates', VIO), ('t2', 'find src -type f', 'src/main/java, src/test/java', ACC), ('t3', 'mvn -v | head -1', 'Maven 3.9.11', GOOD), ('t4', 'mvn -B -q package', 'package does not exist', BAD)])
s_deps = _lab('Dependencies', 'Declare a library, build, and see where it lands.', 'd0', RB, [('d1', 'grep import ...', 'the code needs commons-lang3', VIO), ('d3', 'sed -i ... dep.xml pom.xml', 'declare the dependency', WARN), ('d4', 'mvn -B package', 'Tests run: 1, BUILD SUCCESS', GOOD), ('d5', 'ls target/*.jar', 'artifactId-version.jar', ACC), ('d6', 'mvn dependency:tree', 'compile and test scope', VIO), ('d7', 'find ~/.m2 ...', 'cached in the local repo', GOOD)])
def s_models(C, D, dur):
    E = head('How Maven finds a library', 'In this order.', C['o1'])
    it = [('1  Local repository', '~/.m2/repository on your own computer. If the jar is there, use it.', VIO, 'o2'), ('2  Remote repository', 'Maven Central by default. Download it, and keep a copy.', WARN, 'o3'), ('3  The path is the coordinates', 'group, artifact, version: the same folders everywhere.', GOOD, 'o4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 180, C[cid]))
    E.append(takeaway('Pin your versions.', 900, C['o5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab85.sh gives you a project that will not build. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab85.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Coordinates', [('com.cloudcart', TXT), ('cart-api  1.0.0', TXT)], 'k3', ACC), ('2  Layout', [('src/main/java', TXT), ('src/test/java', TXT)], 'k4', VIO), ('3  Dependencies', [('commons-lang3 3.14.0', TXT), ('junit 4.13.2, test', TXT)], 'k5', GOOD), ('4  Build', [('mvn package', TXT), ('cart-api-1.0.0.jar', TXT)], 'k6', BAD), ('5  tree.txt', [('mvn dependency:tree', TXT), ('save the output', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Name the 3 coordinates', 'q3'), ('Explain the folders', 'q4'), ('Compile vs test scope', 'q5'), ('Where Maven caches', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Read', 'mvn package, first error only', ACC, 'z3'), ('3  Fix', 'coordinates and folders', VIO, 'z4'), ('4  Fix', 'the two dependencies', WARN, 'z5'), ('5  Check', 'tree.txt, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('The three coordinates?', 'f12'), ('Where does main code live?', 'f13'), ('Which scope is not shipped?', 'f14'), ('Where is a library cached?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC10-O01', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: the Maven lifecycle', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ideas=s_ideas, tour=s_tour, deps=s_deps, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ideas=('board', ACC), models=('gear', VIO), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'tour': [('t1b', 4, 3, 0, 600, 'THE COORDINATES: GROUP, ARTIFACT, VERSION', 0, 18), ('t2b', 1, 2, 0, 600, 'STANDARD LAYOUT', 0, 4), ('t3b', 1, 1, 0, 300, 'MAVEN 3.9.11', 0, 3), ('t4b', 2, 3, 0, 1076, 'LIBRARY NOT DECLARED IN THE POM', 0, 7)],
 'deps': [('d1b', 1, 1, 0, 660, 'THE CODE NEEDS COMMONS-LANG3', 0, 3), ('d2b', 2, 3, 0, 620, 'THREE COORDINATES', 0, 7), ('d4b', 3, 2, 0, 700, 'ONE TEST, ZERO FAILURES', 0, 6), ('d5b', 1, 1, 0, 440, 'ARTIFACTID - VERSION . JAR', 0, 3), ('d6b', 2, 1, 0, 940, 'COMPILE: SHIPPED', 0, 6), ('d6b', 3, 2, 0, 940, 'TEST: NOT SHIPPED', 0, 7), ('d7b', 1, 2, 0, 1076, 'CACHED IN YOUR LOCAL REPOSITORY', 0, 4)],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson85/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
