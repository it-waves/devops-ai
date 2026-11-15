def s_hook(C, D, dur):
    E = [El(T('Deploy CloudCart', 'x', 66), 100, 130, C['h1'])]
    E.append(Pop(card(900, 150, ACC, 'run it on Tomcat', [('the war file goes live', TXT)], 52, 32), 100, 320, C['h1'] + 1.0))
    E.append(Pop(card(900, 150, VIO, 'lesson three of five', [('today you deploy it', TXT)], 52, 32), 100, 500, C['h2']))
    for i, (n, s_, col) in enumerate([('an empty Tomcat', 'runs, no app inside', ACC), ('copied by hand', 'one command, it starts', WARN), ('the Manager', 'deploy and remove, mouse', GOOD), ('five checks', 'judged by one command', PINK)]):
        E.append(Pop(card(740, 120, col, n, [(s_, TXT)], 40, 28), 1060, 320 + i * 140, C['h3'] + i * 0.9))
    E.append(Pop(card(900, 140, GOOD, 'two copies, one removed', [('on purpose', TXT)], 46, 30), 100, 700, C['h4']))
    E.append(takeaway('See it, copy it, click it, prove it.', 900, C['h4'], GOOD, 1700)); return E
def s_plan(C, D, dur):
    E = head('What to expect', 'From the first minute to the last.', C['a1']); E.append(ill(C['a1'] + 0.2, 1400, 170))
    st = [('1  See', 'empty Tomcat, no app', ACC, 'a2'), ('2  Copy', 'by hand, one command', VIO, 'a3'), ('3  Click', 'the Manager page', WARN, 'a4'), ('4  Your turn', 'a lab, one check', GOOD, 'a5')]
    for i, (n, sb, col, cid) in enumerate(st): E.append(Pop(card(410, 280, col, n, [(sb, TXT)], 40, 26), 100 + i * 430, 330, C[cid]))
    rm = [('L113  Meet it', ACC), ('L114  Build it', VIO), ('L115  Deploy it', WARN), ('L116  Run it, fix it', GOOD), ('L117  Prove it', PINK)]
    for i, (n, col) in enumerate(rm): E.append(Pop(card(330, 110, col, n, [], 30), 100 + i * 345, 690, C['a6'] + i * 0.8))
    E.append(takeaway('See it, copy it, click it, prove it.', 880, C['a7'], GOOD, 1700)); return E
def s_arch(C, D, dur):
    E = head('How Tomcat finds an app', 'One folder, one file name, one address.', C['r1']); E.append(ill(C['r1'] + 0.2, 1400, 170))
    parts = [('webapps', 'the one folder Tomcat watches', ACC, 'r2'), ('file name', 'cloudcart.war  >  /cloudcart', VIO, 'r3'), ('unpack', 'a folder with the same name', WARN, 'r4'), ('start', 'remove the war: it stops', GOOD, 'r5')]
    for i, (n, sb, col, cid) in enumerate(parts):
        E.append(Pop(card(360, 300, col, n, [(sb, TXT)], 44, 26), 100 + i * 460, 370, C[cid]))
        if i: E.append(El(T('>', 'x', 90, ACC), 100 + i * 460 - 78, 470, C[cid] + 0.3))
    E.append(takeaway('file name  >  address  >  unpack  >  start', 760, C['r6'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab115.sh: deploy two ways. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Start', [('lab up,', TXT), ('startup.sh', TXT)], 'k2', ACC), ('2  By hand', [('cp the war,', TXT), ('open /cloudcart', TXT)], 'k3', WARN), ('3  Manager', [('deploy shop.war', TXT), ('path /shop', TXT)], 'k4', VIO), ('4  Undeploy', [('remove', TXT), ('/cloudcart', TXT)], 'k5', BAD), ('5  Answers', [('answers.txt,', TXT), ('three lines', TXT)], 'k6', PINK), ('6  Check', [('lab check, 5 of 5,', TXT), ('lab down', TXT)], 'k7', GOOD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab115.sh   and   shortcuts115.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab115.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts115.sh  then: lab', WARN, 'i5'), ('5  You need', 'JDK, curl, ss, 1 GB RAM, ports 8089 and 8099', PINK, 'i6'), ('6  Manager login', 'deployer  /  ship-it-115   (lab value only)', ACC, 'i8'), ('7  Rules', 'lab check judges you.  lab down removes it all.', BAD, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 318 + i * 106; E.append(Pop(card(1700, 88, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 22, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Five points. All five to pass.', C['q1x'])
    items = [('Tomcat up, Manager answers', 'q2x'), ('Deployed by hand, UP', 'q3x'), ('/shop runs in the Manager', 'q4x'), ('/cloudcart undeployed', 'q5x'), ('answers.txt: 3 lines right', 'q6x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all five', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own machine only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, startup.sh', PINK, 'z2'), ('2  By hand', 'cp the war, open it', ACC, 'z3'), ('3  Manager', 'deploy shop.war', WARN, 'z4'), ('4  Undeploy', 'remove /cloudcart', VIO, 'z5'), ('5  Check', 'answers, 5 of 5', BAD, 'z6'), ('6  Clean up', 'lab down, port free', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which folder does Tomcat watch for new apps?', 'f12'), ('What decides the address of a war you copy in?', 'f13'), ('Which button removes an app? Which only stops it?', 'f14'), ('What did the Manager do with shop.war on disk?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('CloudCart v0: deploy to Tomcat', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: run it, fix it', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: deploy by hand, then from the Manager', 'One real Tomcat, two ways to deploy.', 'p0', RB, [('l3', '1  start', 'Tomcat, no app inside', ACC), ('u3', '2  Manager', 'sign in, tour the page', VIO), ('t1', '3  by hand', 'cp the war, it starts', WARN), ('v4', '4  deploy', 'shop.war as /shop', GOOD), ('v8', '5  undeploy', 'remove /cloudcart', BAD), ('e2', '6  stop', 'shutdown, port free', PINK)])
FN = dict(hook=s_hook, plan=s_plan, arch=s_arch, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(plan=('board', ACC), arch=('board', VIO), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [('l2b', 1, 1, 4, 124, 'only the manager'), ('l3b', 1, 1, 4, 250, 'started, but empty'), ('l4b', 2, 1, 4, 200, '404: no app here'), ('t2b', 1, 1, 4, 520, 'the war + a new folder'), ('e1b', 1, 1, 4, 360, 'cloudcart is gone')]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson115/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
