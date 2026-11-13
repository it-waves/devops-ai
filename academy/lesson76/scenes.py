def s_hook(C, D, dur):
    E = [El(T('Which part is missing?', 'x', 72), 100, 130, C['h1'])]
    errs = [('java: command not found', 'h1', 1.0, BAD), ('wrong class file version', 'h1', 4.0, WARN), ('works on my laptop', 'h1', 7.0, VIO)]
    for i, (e, cid, dt, col) in enumerate(errs): E.append(Pop(card(1500, 100, col, '', [(e, TXT)], 4, 40), 100, 300 + i * 125, C[cid] + dt))
    ws = [('source', ACC), ('bytecode', GOOD), ('JDK', VIO), ('JRE', WARN), ('JVM', PINK)]
    x = 100
    for i, (w, col) in enumerate(ws):
        b = chip(w, col, 40); E.append(Pop(b, x, 720, C['h2'] + 2.5 + i * 1.2)); x += b.width + 30
    E.append(takeaway('Separate the five. Prove each one.', 900, C['h4'], GOOD, 1700)); return E
def s_map(C, D, dur):
    E = head('The journey of a program', 'Five steps, from your text file to a running process.', C['m1']); E.append(ill(C['m1'] + 0.2, 1400, 170))
    it = [('1  Source', 'Hello.java', 'text you write', ACC, 'm2'), ('2  javac', 'the compiler', 'lives in the JDK', VIO, 'm3'), ('3  Bytecode', 'Hello.class', 'same everywhere', GOOD, 'm4'), ('4  JVM', 'the virtual machine', 'ships in the JRE', WARN, 'm5'), ('5  Process', 'java Hello', 'the OS runs it', PINK, 'm6')]
    xs = [100, 460, 820, 1180, 1540]
    for i, (n, a, b, col, cid) in enumerate(it):
        E.append(Pop(card(280, 230, col, n, [(a, TXT), (b, MUTED)], 36, 26), xs[i], 340, C[cid]))
        if i: E.append(A([(xs[i] - 75, 455), (xs[i] - 8, 455)], C[cid] + 0.3, col, 7, 28))
    way = [(C['m2'], 160, 600), (C['m3'], 520, 600), (C['m4'], 880, 600), (C['m5'], 1240, 600), (C['m6'], 1600, 600), (C['m6'] + 2.0, 1600, 600)]
    E.append(Move(parcel(56), way, t_end=C['m7']))
    t = C['m7']
    E.append(Pop(card(1700, 118, VIO, 'JDK', [('JRE + compiler and tools (javac, jar, jps, jcmd ...)', TXT)], 34, 26), 100, 590, t))
    E.append(Pop(card(1300, 118, WARN, 'JRE', [('JVM + the standard libraries', TXT)], 34, 26), 300, 712, t + 1.2))
    E.append(Pop(card(900, 118, PINK, 'JVM', [('reads the bytecode and runs it', TXT)], 34, 26), 500, 834, t + 2.4))
    E.append(takeaway('Build = JDK.   Run only = JRE.', 985, C['m8'], GOOD, 1700, 40)); return E
s_tools = _lab('JDK or JRE?', 'Ask the machine what it really has.', 't1', RB, [('t2', 'java -version', 'the runtime', ACC), ('t3', 'javac -version', 'the compiler', VIO), ('t4', 'dpkg -L ...jre... | grep', 'only 4 tools, no javac', WARN), ('t5', 'dpkg -L ...jdk... | grep -c', '24 tools in the JDK', GOOD)])
s_compile = _lab('Compile and run', 'Source in, bytecode out, then the JVM runs it.', 'c0', RB, [('c1', 'cat Hello.java', 'the source: text', ACC), ('c2', 'javac Hello.java', 'silence = success', VIO), ('c3', 'ls', 'Hello.class appears', WARN), ('c4', 'xxd -l 8', 'cafe babe 0041', PINK), ('c5', 'java Hello', 'the JVM runs it', GOOD)])
s_bytecode = _lab('Inside the bytecode', 'Small steps for an imaginary computer.', 'b0', RB, [('b0a', 'javac Hello.java', 'compile again', VIO), ('b1', 'javap -c Hello', 'disassemble', ACC), ('b1b', 'getstatic, ldc', 'get, load', WARN), ('b1c', 'invokevirtual', 'calls println', GOOD)])
s_process = _lab('The process', 'A program on disk is not a process.', 'p0', RB, [('p2', 'java ShopApp &', 'start in background', ACC), ('p3', 'jps -l', 'Java tool: the PID', VIO), ('p4', 'ps -C java', 'the OS: same PID', WARN), ('p5', 'kill %1', 'stop it', BAD), ('p6', 'jps -l', 'process gone', GOOD)])
def s_models(C, D, dur):
    E = head('Reading the errors', 'Each message points at one part of the journey.', C['o1'])
    it = [('java: command not found', 'no runtime: install a JRE or JDK', BAD, 'o2'), ('javac: command not found', 'runtime only: install the JDK', WARN, 'o3'), ('Unsupported class file major version', 'bytecode newer than the JVM', VIO, 'o4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 180, cid and C[cid]))
    E.append(takeaway('One message. One part. One fix.', 900, C['o5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab76.sh builds the programs. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab76.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Versions', [('java and javac', TXT), ('>  versions.txt', TXT)], 'k3', ACC), ('2  Compile', [('javac both files', TXT), ('java Hello', TXT)], 'k4', VIO), ('3  Bytecode', [('javap -c Hello', TXT), ('>  bytecode.txt', TXT)], 'k5', GOOD), ('4  Process', [('java ShopApp &', TXT), ('jps -l > process.txt', TXT)], 'k6', WARN), ('5  Answers', [('javac: JDK', TXT), ('bytecode: .class', TXT), ('process: java', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', BAD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Name the five parts', 'q3'), ('JDK vs JRE', 'q4'), ('Show cafe babe', 'q5'), ('Show a PID two ways', 'q6'), ('lab down, nothing running', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Build', 'versions, compile, run', ACC, 'z3'), ('3  Read', 'the disassembly', VIO, 'z4'), ('4  Process', 'start it, list it', WARN, 'z5'), ('5  Check', 'answers, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What turns source into bytecode?', 'f12'), ('What do the first 4 bytes say?', 'f13'), ('Which part runs the bytecode?', 'f14'), ('Program or process: same thing?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC09-O01', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: compile and run a small Java program', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, map=s_map, tools=s_tools, compile=s_compile, bytecode=s_bytecode, process=s_process, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(map=('board', ACC), tools=('gear', VIO), compile=('test', GOOD), bytecode=('doc', ACC), process=('eye', WARN), models=('question', WARN), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'compile': [('c4b', 1, 1, 150, 292, 'MAGIC')],
 'process': [('p3b', 2, 1, 0, 190, 'PID'), ('p4b', 2, 1, 0, 360, 'SAME PID')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson76/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
