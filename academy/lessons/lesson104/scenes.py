def s_hook(C, D, dur):
    E = [El(T('Apache Tomcat', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(760, 150, ACC, 'runs Java web apps', [('free, open source, 20+ years', TXT)], 52, 32), 100, 320, C['h2']))
    E.append(Pop(card(760, 150, VIO, 'you will use it', [('install, deploy, secure, fix', TXT)], 52, 32), 100, 500, C['h3']))
    E.append(Pop(card(760, 160, WARN, 'five pieces', [('JVM, container, connector,', TXT), ('context, war', TXT)], 46, 30), 900, 410, C['h4']))
    E.append(Pop(card(1100, 140, GOOD, 'then a real Tomcat', [('start it, deploy to it', TXT)], 46, 30), 100, 720, C['h5']))
    E.append(takeaway('Learn the pieces. Run the real thing.', 900, C['h5'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
def s_parts(C, D, dur):
    E = head('The five pieces', 'A request travels through all of them.', C['a1'])
    E.append(Pop(card(1740, 560, MUTED, 'JVM  (a Java process)', [], 36), 90, 300, C['a2']))
    E.append(Pop(card(1640, 440, VIO, 'Tomcat  (servlet container)', [], 34), 140, 370, C['a3']))
    E.append(Pop(card(400, 190, ACC, 'Connector', [(':8080  HTTP', TXT)], 38, 30), 190, 450, C['a4']))
    E.append(Pop(card(400, 190, WARN, 'Context', [('/hello', TXT)], 38, 30), 700, 450, C['a5']))
    E.append(Pop(card(400, 190, GOOD, 'Servlet', [('Java code answers', TXT)], 38, 28), 1210, 450, C['a3'] + 0.5))
    E.append(El(T('>', 'x', 64, TXT), 620, 505, C['a5'])); E.append(El(T('>', 'x', 64, TXT), 1130, 505, C['a5'] + 0.3))
    E.append(Pop(card(1500, 130, PINK, 'WAR file', [('one zip: pages, classes, WEB-INF/web.xml, dropped in webapps', TXT)], 36, 28), 190, 690, C['a6']))
    E.append(Pop(card(1700, 120, ACC, '', [('connector > context > servlet, inside Tomcat, inside a JVM', TXT)], 4, 34), 100, 880, C['a7'])); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab104.sh: a real Tomcat on your VM. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Start', [('startup.sh, then', TXT), (':8080 gives 200', TXT)], 'k2', ACC), ('2  Deploy', [('hello.war into', TXT), ('webapps, /hello/', TXT)], 'k3', WARN), ('3  Inside the war', [('unzip -l', TXT), ('save the list', TXT)], 'k4', VIO), ('4  Connector', [('find the port in', TXT), ('server.xml', TXT)], 'k5', PINK), ('5  facts.txt', [('jvm: connector:', TXT), ('context: war:', TXT)], 'k6', GOOD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab104.sh   and   shortcuts104.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab104.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts104.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, curl, unzip, 1 GB, internet', PINK, 'i6'), ('6  Check + cleanup', 'lab check builds on your machine. lab down removes all.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('Tomcat answers 200', 'q3x'), ('hello.war deployed', 'q4x'), ('war list saved', 'q5x'), ('facts.txt, real port', 'q6x'), ('lab down stops Tomcat', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the tasks', PINK, 'z2'), ('2  Run', 'startup.sh, check 200', ACC, 'z3'), ('3  Deploy', 'hello.war, wait', WARN, 'z4'), ('4  Look', 'unzip -l, find the port', VIO, 'z5'), ('5  Write + check', 'facts.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does a connector do?', 'f12'), ('What is a context?', 'f13'), ('What is inside a WAR?', 'f14'), ('Why does Tomcat need a JVM?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC12-O01 Tomcat basics', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: install and run Tomcat', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: a real Tomcat', 'Real Apache Tomcat 10.1.34 on a Linux host.', 'p0', RB, [('l1', '1  look inside', 'bin conf lib logs webapps', ACC), ('l2', '2  the connector', 'port 8080, HTTP', WARN), ('l3', '3  start it', 'one JVM process', VIO), ('l6', '4  contexts', 'one folder each', PINK), ('l8', '5  a WAR is a zip', 'index.html, web.xml', GOOD), ('l10', '6  deploy it', '/hello/ answers', ACC)])
FN = dict(hook=s_hook, parts=s_parts, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(parts=('board', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': []}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson104/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
