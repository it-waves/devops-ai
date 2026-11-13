def s_hook(C, D, dur):
    E = [El(T('Jar or war?', 'x', 72), 100, 130, C['h1'])]
    errs = [('Dev: ship the jar.', 'h1', 2.0, BAD), ('Ops: it is a war.', 'h1', 5.0, WARN), ('The server: silence.', 'h1', 8.0, VIO)]
    for i, (e, cid, dt, col) in enumerate(errs): E.append(Pop(card(1500, 100, col, '', [(e, TXT)], 4, 40), 100, 300 + i * 125, C[cid] + dt))
    ws = [('build both', ACC), ('open both', VIO), ('run both', GOOD), ('choose right', WARN)]
    x = 100
    for i, (w, col) in enumerate(ws):
        b = chip(w, col, 40); E.append(Pop(b, x, 720, C['h3'] + 1.0 + i * 1.5)); x += b.width + 30
    E.append(takeaway('Same zip. Different contract.', 900, C['h4'], GOOD, 1700)); return E
def s_ideas(C, D, dur):
    E = head('Four facts', 'Jar and war: same zip format, different contract.', C['u1']); E.append(ill(C['u1'] + 0.2, 1400, 170))
    it = [('1  A jar', 'a zip of class files, plus META-INF/MANIFEST.MF', ACC, 'u2'), ('2  A runnable jar', 'Main-Class in the manifest   =   java -jar app.jar', VIO, 'u3'), ('3  A war', 'WEB-INF/web.xml, WEB-INF/lib   =   needs a servlet container', GOOD, 'u4'), ('4  A fat jar', 'carries its own web server, runs by itself', WARN, 'u5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 135, col, n, [(s_, TXT)], 44, 34), 100, 330 + i * 160, C[cid]))
    E.append(takeaway('Check the manifest. Check the layout. Then choose.', 985, C['u6'], GOOD, 1700, 38)); return E
s_jar = _lab('Build and run a jar', 'Pack classes, fail, add an entry point, run.', 'j0', RB, [('j2', 'jar cf app.jar -C out .', 'pack the classes', ACC), ('j3', 'java -jar app.jar', 'no main manifest', BAD), ('j4', 'jar cfe app.jar com.cloudcart.Hello', 'adds Main-Class', VIO), ('j5', 'java -jar app.jar', 'CloudCart is ready', GOOD), ('j6', 'unzip -p ... MANIFEST.MF', 'the one line that matters', WARN)])
s_war = _lab('Build and open a war', 'A web app layout, packed and inspected.', 'w0', RB, [('w1', 'find war -type f', 'index + WEB-INF', ACC), ('w2', 'jar cf shop.war -C war .', 'same tool, same zip', VIO), ('w3', 'jar tf shop.war', 'the contract: WEB-INF', GOOD), ('w4', 'java -jar shop.war', 'no main: not a program', BAD), ('w5', 'unzip -p ... web.xml', 'config for the container', WARN)])
def s_models(C, D, dur):
    E = head('Which one does your server need?', 'Three shapes, three contracts.', C['o1'])
    it = [('Jar with a main class', 'java -jar app.jar. Common for services and tools.', VIO, 'o2'), ('War', 'a web app for a servlet container such as Tomcat.', WARN, 'o3'), ('Fat jar', 'a jar with the web server and libraries inside. Runs alone.', GOOD, 'o4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 180, C[cid]))
    E.append(takeaway('Do not guess by the file name.', 900, C['o5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab80.sh gives you a source file and a web folder. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab78.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Compile', [('javac -d out', TXT), ('src/com/cloudcart/Hello.java', TXT)], 'k3', ACC), ('2  Runnable jar', [('jar cfe app.jar ...', TXT), ('java -jar app.jar > jar-run.txt', TXT)], 'k4', VIO), ('3  Build a war', [('jar cf shop.war', TXT), ('-C war .', TXT)], 'k5', GOOD), ('4  List it', [('jar tf shop.war', TXT), ('> war-list.txt', TXT)], 'k6', BAD), ('5  Answers', [('jar runs with: java -jar', TXT), ('war needs: a servlet container', TXT), ('manifest holds: main class', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('What a jar holds', 'q3'), ('Make a jar runnable', 'q4'), ('What a war needs', 'q5'), ('Read manifest, layout', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Jar', 'compile, build, make it run', ACC, 'z3'), ('3  War', 'build it, list it', VIO, 'z4'), ('4  Compare', 'java -jar on the war', WARN, 'z5'), ('5  Check', 'answers, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What is a jar?', 'f12'), ('What makes a jar runnable?', 'f13'), ('What does a war need to run?', 'f14'), ('What is a fat jar?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC09-O05', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: stack traces and logs', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ideas=s_ideas, jar=s_jar, war=s_war, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ideas=('board', ACC), models=('gear', VIO), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'jar': [('j3b', 1, 1, 0, 600, 'NO ENTRY POINT'), ('j6b', 3, 1, 0, 470, 'MAIN-CLASS')],
 'war': [('w3b', 6, 1, 0, 240, 'THE CONTRACT'), ('w4b', 1, 1, 0, 590, 'NOT A PROGRAM')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson78/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
