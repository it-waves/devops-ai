def s_hook(C, D, dur):
    E = [El(T('Works here. Fails there.', 'x', 72), 100, 130, C['h1'])]
    errs = [('NoClassDefFoundError', 'h2', 0.0, BAD), ('package com.cloudcart.pricing does not exist', 'h2', 3.5, WARN), ('Could not find or load main class', 'h2', 7.0, VIO)]
    for i, (e, cid, dt, col) in enumerate(errs): E.append(Pop(card(1500, 100, col, '', [(e, TXT)], 4, 40), 100, 300 + i * 125, C[cid] + dt))
    ws = [('package', ACC), ('class path', VIO), ('dependency', GOOD), ('config', WARN)]
    x = 100
    for i, (w, col) in enumerate(ws):
        b = chip(w, col, 40); E.append(Pop(b, x, 720, C['h3'] + 1.0 + i * 1.5)); x += b.width + 30
    E.append(takeaway('Read it. It tells you where.', 900, C['h4'], GOOD, 1700)); return E
def s_ideas(C, D, dur):
    E = head('Four ideas', 'Package, class path, dependency, configuration.', C['u1']); E.append(ill(C['u1'] + 0.2, 1400, 170))
    it = [('1  Package', 'com.cloudcart.Main   =   com/cloudcart/Main.java', ACC, 'u2'), ('2  Class path', 'folders and jars, joined by colons', VIO, 'u3'), ('3  Dependency', 'a jar file you add to the class path', GOOD, 'u4'), ('4  Configuration', 'env vars and -D properties, outside the code', WARN, 'u5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 135, col, n, [(s_, TXT)], 44, 34), 100, 330 + i * 160, C[cid]))
    E.append(takeaway('Same program. Different environment. Different result.', 985, C['u6'], GOOD, 1700, 38)); return E
s_build = _lab('Packages and the class path', 'Fail at compile time, add the jar, then run.', 'b0', RB, [('b3', 'javac -d out Main.java', 'package does not exist', BAD), ('b4', 'javac -cp lib/pricing.jar', 'jar on the class path', ACC), ('b5', 'find out -type f', 'folders match package', VIO), ('b6', 'jar tf pricing.jar', 'a jar is an archive', WARN), ('b7', 'java -cp out:lib/pricing.jar', 'Total: 108.0', GOOD)])
s_config = _lab('Break it, then configure it', 'Two classic failures, then change behavior from outside.', 'g0', RB, [('g2', 'java -cp out Main', 'NoClassDefFoundError', BAD), ('g3', 'java com.cloudcart.Main', 'main class not found', WARN), ('g4', 'STORE_NAME=Bean java ...', 'env variable', ACC), ('g5', 'java -Dcurrency=EUR ...', 'a property', VIO)])
def s_models(C, D, dur):
    E = head('Three messages, three fixes', 'Read the message. It names the fix.', C['o1'])
    it = [('package does not exist', 'compile time: add the jar with javac -cp', VIO, 'o2'), ('NoClassDefFoundError', 'run time: add the jar to the java class path', WARN, 'o3'), ('Could not find main class', 'use the full class name, and the out folder', BAD, 'o4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 180, C[cid]))
    E.append(takeaway('Check configuration before you change code.', 900, C['o5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab78.sh builds a project and its jar. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab78.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Compile', [('javac -cp lib/pricing.jar', TXT), ('-d out  Main.java', TXT)], 'k3', ACC), ('2  Run', [('java -cp out:lib/pricing.jar', TXT), ('> run.txt', TXT)], 'k4', VIO), ('3  Configure', [('STORE_NAME=Bean', TXT), ('-Dcurrency=EUR > config.txt', TXT)], 'k5', GOOD), ('4  Break it', [('java -cp out  (no jar)', TXT), ('2> fail.txt', TXT)], 'k6', BAD), ('5  Answers', [('package: folder path', TXT), ('classpath: where java looks', TXT), ('dependency: a jar', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Package = folder path', 'q3'), ('Build a class path', 'q4'), ('Jar: compile and run', 'q5'), ('Env var and property', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Compile', 'with the jar on the class path', ACC, 'z3'), ('3  Run', 'plain, then configured', VIO, 'z4'), ('4  Break', 'drop the jar, keep the error', WARN, 'z5'), ('5  Check', 'answers, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('How does a package map to disk?', 'f12'), ('What goes in the class path?', 'f13'), ('Dependency: compile time or run time?', 'f14'), ('Two ways to configure from outside?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC09-O03', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: inspect a running Java process', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ideas=s_ideas, build=s_build, config=s_config, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ideas=('board', ACC), models=('gear', VIO), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'build': [('b3b', 1, 2, 0, 1060, 'COMPILE TIME'), ('b5b', 1, 1, 0, 380, 'MATCHES PACKAGE')],
 'config': [('g2b', 1, 2, 0, 190, 'PRINTS FIRST')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson78/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
