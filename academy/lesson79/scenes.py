def s_hook(C, D, dur):
    E = [El(T('Stop guessing. Ask the process.', 'x', 72), 100, 130, C['h1'])]
    errs = [('Is the heap too small?', 'h1', 2.0, BAD), ('Is it the wrong port?', 'h1', 5.0, WARN), ('Who knows?', 'h1', 8.0, VIO)]
    for i, (e, cid, dt, col) in enumerate(errs): E.append(Pop(card(1500, 100, col, '', [(e, TXT)], 4, 40), 100, 300 + i * 125, C[cid] + dt))
    ws = [('is it running', ACC), ('how started', VIO), ('what settings', GOOD), ('what is hidden', WARN)]
    x = 100
    for i, (w, col) in enumerate(ws):
        b = chip(w, col, 40); E.append(Pop(b, x, 720, C['h3'] + 1.0 + i * 1.5)); x += b.width + 30
    E.append(takeaway('Ask the process.', 900, C['h4'], GOOD, 1700)); return E
def s_ideas(C, D, dur):
    E = head('Four questions', 'Four questions, four tools, one live process.', C['u1']); E.append(ill(C['u1'] + 0.2, 1400, 170))
    it = [('1  Is it running?', 'jps -l      pgrep -a java', ACC, 'u2'), ('2  How was it started?', '/proc/PID/cmdline      jcmd PID VM.command_line', VIO, 'u3'), ('3  What settings?', 'jcmd PID VM.flags      jcmd PID VM.system_properties', GOOD, 'u4'), ('4  What is hidden?', 'machine defaults      JAVA_TOOL_OPTIONS', WARN, 'u5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 135, col, n, [(s_, TXT)], 44, 34), 100, 330 + i * 160, C[cid]))
    E.append(takeaway('-X for the JVM.   -XX for tuning.   -D for your program.', 985, C['u6'], GOOD, 1700, 38)); return E
s_inspect = _lab('Find the process', 'Start a service, find it, read how it was started.', 'i0', RB, [('i2', 'jps -l', 'Java processes', ACC), ('i3', 'pgrep -a java', 'PID and full command', VIO), ('i5', "tr < /proc/PID/cmdline", 'the real command line', GOOD), ('i6', 'jcmd PID VM.command_line', 'flags, class, class path', WARN)])
s_settings = _lab('Read its real settings', 'Flags in use, properties, defaults, hidden options.', 's0', RB, [('s2', 'jcmd Server VM.flags', 'MaxHeapSize, G1', ACC), ('s3', 'VM.system_properties', '-D values arrive', VIO), ('s4', 'PrintFlagsFinal', 'default heap', WARN), ('s5', 'JAVA_TOOL_OPTIONS', 'Picked up silently', BAD)])
def s_models(C, D, dur):
    E = head('Three flag families', 'Read the flag. It names the family.', C['o1'])
    it = [('-X  ·  JVM', '-Xmx256m is the biggest heap. -Xms64m is the start.', VIO, 'o2'), ('-D  ·  your program', 'a property, before the class name: -Dserver.port=9090', WARN, 'o3'), ('-XX  ·  tuning', 'garbage collector and more. Keep defaults until you measure.', BAD, 'o4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 180, C[cid]))
    E.append(takeaway('Inspect first.  Change second.', 900, C['o5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab79.sh gives you a service to inspect. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab78.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Start', [('java -Xmx192m', TXT), ('-Dserver.port=9191 -Dmode=prod', TXT)], 'k3', ACC), ('2  Command line', [('tr < /proc/PID/cmdline', TXT), ('> cmdline.txt', TXT)], 'k4', VIO), ('3  Flags', [('jcmd Server VM.flags', TXT), ('> flags.txt', TXT)], 'k5', GOOD), ('4  Property', [('VM.system_properties', TXT), ('| grep mode > property.txt', TXT)], 'k6', BAD), ('5  Answers', [('heap flag: -Xmx', TXT), ('property flag: -D', TXT), ('inspect tool: jcmd', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Find the PID', 'q3'), ('Read the command line', 'q4'), ('Three flag families', 'q5'), ('Flags from a live JVM', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Start', 'the server with the task flags', ACC, 'z3'), ('3  Inspect', 'command line, flags, property', VIO, 'z4'), ('4  Compare', 'try JAVA_TOOL_OPTIONS', WARN, 'z5'), ('5  Check', 'answers, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which tool lists Java processes?', 'f12'), ('Where is the real command line?', 'f13'), ('Which flag: max heap? a property?', 'f14'), ('What is JAVA_TOOL_OPTIONS?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC09-O04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: JAR versus WAR', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ideas=s_ideas, inspect=s_inspect, settings=s_settings, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ideas=('board', ACC), models=('gear', VIO), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'inspect': [('i2b', 2, 1, 0, 170, 'MAIN CLASS'), ('i5b', 1, 1, 0, 680, 'TRUE COMMAND LINE')],
 'settings': [('s2b', 2, 4, 0, 400, 'IN USE NOW'), ('s5b', 2, 1, 0, 590, 'PICKED UP')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson78/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
