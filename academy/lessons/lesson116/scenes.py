def s_hook(C, D, dur):
    E = [El(T('Run it. Fix it.', 'x', 66), 100, 130, C['h1'])]
    E.append(Pop(card(900, 150, ACC, 'an app that went silent', [('customers get nothing', TXT)], 52, 32), 100, 320, C['h1'] + 1.0))
    E.append(Pop(card(900, 150, VIO, 'lesson four of five', [('you work the incident', TXT)], 52, 32), 100, 500, C['h2']))
    for i, (n, s_, col) in enumerate([('wrong Java path', 'Tomcat will not start', ACC), ('a stranger on the port', 'someone else answers', WARN), ('a damaged war', 'the app is missing', BAD), ('five checks', 'judged by one command', PINK)]):
        E.append(Pop(card(740, 120, col, n, [(s_, TXT)], 40, 28), 1060, 320 + i * 140, C['h3'] + i * 0.9))
    E.append(Pop(card(900, 140, GOOD, 'evidence, not guesses', [('read, find, fix, prove', TXT)], 46, 30), 100, 700, C['h4']))
    E.append(takeaway('Read it, find it, fix it, prove it.', 900, C['h4'], GOOD, 1700)); return E
def s_plan(C, D, dur):
    E = head('What to expect', 'From the first minute to the last.', C['a1']); E.append(ill(C['a1'] + 0.2, 1400, 170))
    st = [('1  No start', 'Tomcat will not start', ACC, 'a2'), ('2  A stranger', 'who holds the port?', VIO, 'a3'), ('3  No app', 'read the log, compare', WARN, 'a4'), ('4  Your turn', 'customer check, lab', GOOD, 'a5')]
    for i, (n, sb, col, cid) in enumerate(st): E.append(Pop(card(410, 280, col, n, [(sb, TXT)], 40, 26), 100 + i * 430, 330, C[cid]))
    rm = [('L113  Meet it', ACC), ('L114  Build it', VIO), ('L115  Deploy it', WARN), ('L116  Run it, fix it', GOOD), ('L117  Prove it', PINK)]
    for i, (n, col) in enumerate(rm): E.append(Pop(card(330, 110, col, n, [], 30), 100 + i * 345, 690, C['a6'] + i * 0.8))
    E.append(takeaway('Read it, find it, fix it, prove it.', 880, C['a7'], GOOD, 1700)); return E
def s_arch(C, D, dur):
    E = head('The incident method', 'Every incident, the same five steps.', C['r1']); E.append(ill(C['r1'] + 0.2, 1400, 170))
    parts = [('symptom', 'what the customer sees', ACC, 'r2'), ('evidence', 'output, log, ports', VIO, 'r3'), ('cause', 'one sentence', WARN, 'r4'), ('fix', 'the smallest change', GOOD, 'r5')]
    for i, (n, sb, col, cid) in enumerate(parts):
        E.append(Pop(card(360, 300, col, n, [(sb, TXT)], 44, 26), 100 + i * 460, 370, C[cid]))
        if i: E.append(El(T('>', 'x', 90, ACC), 100 + i * 460 - 78, 470, C[cid] + 0.3))
    E.append(takeaway('symptom  >  evidence  >  cause  >  fix  >  proof', 760, C['r6'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab116.sh: three faults. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Java path', [('startup.sh fails,', TXT), ('fix setenv.sh', TXT)], 'k2', ACC), ('2  The port', [('who answers?', TXT), ('stop it, restart', TXT)], 'k3', WARN), ('3  The war', [('read the log,', TXT), ('replace the war', TXT)], 'k4', BAD), ('4  Answers', [('answers.txt,', TXT), ('three causes', TXT)], 'k5', VIO), ('5  Check', [('lab check,', TXT), ('5 of 5', TXT)], 'k6', GOOD), ('6  Clean up', [('lab down,', TXT), ('port free', TXT)], 'k6', PINK)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab116.sh   and   shortcuts116.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab116.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts116.sh  then: lab', WARN, 'i5'), ('5  You need', 'JDK, curl, ss, python3, 1 GB RAM, ports 8089 and 8099', PINK, 'i6'), ('6  Rules', 'lab up starts the faults. lab down removes it all.', BAD, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 318 + i * 118; E.append(Pop(card(1700, 88, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 22, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Five points. All five to pass.', C['q1x'])
    items = [('Java home fixed, Tomcat up', 'q2x'), ('Port 8089 is Tomcat', 'q3x'), ('CloudCart health is UP', 'q4x'), ('The war is the good file', 'q5x'), ('answers.txt: 3 causes right', 'q6x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all five', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own machine only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the error', PINK, 'z2'), ('2  Java path', 'fix setenv.sh, vim', ACC, 'z3'), ('3  The port', 'stop the stranger', WARN, 'z4'), ('4  The war', 'replace the file', VIO, 'z5'), ('5  Check', 'answers, 5 of 5', BAD, 'z6'), ('6  Clean up', 'lab down, port free', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What are the five steps of the method?', 'f12'), ('How did you know Tomcat was not answering?', 'f13'), ('Which command shows who holds a port?', 'f14'), ('What did the log say about the damaged war?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('CloudCart v0: run it, fix it', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: prove it, clean copy', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: three faults, found and fixed', 'Read the evidence. Fix one cause at a time.', 'p0', RB, [('l2', '1  no start', 'wrong java home', ACC), ('l6', '2  a stranger', 'python holds the port', WARN), ('l13', '3  bad war', 'zip exception', BAD), ('l17', '4  customer', 'twelve products', VIO), ('l19', '5  judge', 'lab check, 5 of 5', GOOD), ('l20', '6  clean up', 'lab down, port free', PINK)])
FN = dict(hook=s_hook, plan=s_plan, arch=s_arch, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(plan=('board', ACC), arch=('board', VIO), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': []}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson116/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
