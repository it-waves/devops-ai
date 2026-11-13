def s_hook(C, D, dur):
    E = [El(T('One tap. Four parts.', 'x', 72), 100, 130, C['h1'])]
    parts = [('Browser', 'the customer', VIO, C['h1'] + 1.5), ('Web service', 'hands over the page', ACC, C['h2'] + 1.0), ('API service', 'asks, decides, answers', GOOD, C['h2'] + 3.5), ('Database', 'one file of data', WARN, C['h2'] + 6.0)]
    xs = [100, 560, 1020, 1480]
    for i, (n, sb, col, t) in enumerate(parts):
        E.append(Pop(card(360, 190, col, n, [(sb, TXT)], 40, 26), xs[i], 380, t))
        if i: E.append(A([(xs[i] - 95, 475), (xs[i] - 5, 475)], t + 0.3, col, 7, 28))
    E.append(Pop(card(1100, 110, WARN, 'What happened in that second?', [], 44, 32), 100, 650, C['h1'] + 5.0))
    E.append(Pop(badge('ONE LABEL', F('x', 52), INK, PINK, padx=34, pady=18), 100, 810, C['h3'] + 4.0)); E.append(Pop(badge('FOLLOW IT', F('x', 52), INK, ACC, padx=34, pady=18), 500, 810, C['h3'] + 6.5))
    E.append(takeaway('Draw it. Trace it. Find the broken part.', 980, C['h4'] + 1.0, GOOD, 1700)); return E
def s_draw(C, D, dur):
    E = head('Draw CloudCart', 'Four parts. Seven steps. One label.', C['d1']); E.append(ill(C['d1'] + 0.2, 1400, 170))
    E.append(Pop(card(400, 260, VIO, 'Browser', [("the customer's screen", TXT), ('draws the cards', TXT)], 44, 28), 100, 450, C['d1'] + 1.0))
    E.append(Pop(card(440, 200, ACC, 'Web service', [('port 8080', TXT), ('hands over the page', TXT)], 40, 28), 700, 290, C['d2']))
    E.append(Pop(card(440, 200, GOOD, 'API service', [('port 5000', TXT), ('rules and data access', TXT)], 40, 28), 700, 690, C['d3']))
    E.append(Pop(card(400, 200, WARN, 'Database', [('shop.db', TXT), ('a file, so no port', TXT)], 40, 28), 1400, 690, C['d4']))
    arr = [((505, 490), (695, 385), 'd5', ACC, (560, 380), '1'), ((695, 445), (505, 550), 'd6', GOOD, (595, 520), '2'), ((505, 610), (695, 745), 'd7', ACC, (640, 640), '3'),
           ((1145, 760), (1395, 760), 'd8', ACC, (1235, 690), '4'), ((1395, 830), (1145, 830), 'd8b', GOOD, (1235, 850), '5')]
    for a, b, cid, col, pp, n in arr:
        E.append(A([a, b], C[cid], col, 7, 30)); E.append(pill(n, pp[0], pp[1], C[cid] + 0.3, col, size=30, padx=16, pady=6))
    t6 = C['d8b'] + 3.4
    E.append(A([(695, 805), (505, 670)], t6, GOOD, 7, 30)); E.append(pill('6', 545, 740, t6 + 0.3, GOOD, size=30, padx=16, pady=6))
    E.append(Pop(badge('7  draws the cards', F('b', 34), INK, VIO, padx=26, pady=12), 100, 740, C['d8c']))
    way = [(C['d5'], 300, 580), (C['d6'], 920, 390), (C['d6'] + 0.8, 920, 390), (C['d7'], 300, 580), (C['d7'] + 0.6, 300, 580), (C['d8'], 920, 790), (C['d8'] + 0.4, 920, 790), (C['d8b'], 1600, 790), (C['d8b'] + 0.4, 1600, 790), (C['d8b'] + 3.2, 920, 790), (C['d8b'] + 3.6, 920, 790), (C['d8c'], 300, 580)]
    E.append(Move(parcel(64), way, t_end=C['d9'] + 1.0))
    E.append(Pop(badge('X-Request-Id: trace-1  follows every step', F('b', 38), INK, WARN, padx=30, pady=14), 100, 940, C['d9'])); return E
s_parts = _lab('Check the parts', 'The drawing is a claim. Test it on the machine.', 'm1', RB, [('m2', './start.sh', 'start the shop', ACC), ('m4', 'ss -ltn', 'which ports listen', VIO), ('m5', 'ports 5000, 8080', 'no port for the database', GOOD), ('m7', './layers.sh', 'ask each layer', ACC), ('m8', 'web  200', 'the page is served', GOOD), ('m8b', 'api  200', 'the data is served', GOOD)])
s_trace = _lab('Trace one request', 'One label, two diaries, one road.', 't1', RB, [('t4', 'page request', 'label: trace-1', ACC), ('t6', 'data request', 'same label: trace-1', VIO), ('t7', 'JSON comes back', 'three products', GOOD), ('t8', 'grep trace-1', 'search both diaries', WARN), ('t9b', 'web.log + api.log', 'one label, two lines', PINK), ('t10', 'showdb.py', 'the rows at the end', ACC)])
s_layers = _lab('Which layer broke?', 'Ask each layer. The first to fail is the suspect.', 'y1', RB, [('y3', './layers.sh', 'ask each layer', ACC), ('y5', 'api.sh stop', 'break one layer', BAD), ('y7', 'web  200', 'the page still loads', GOOD), ('y7b', 'api  000', 'nobody is listening', WARN), ('y8', 'api.sh start', 'repair it', VIO), ('y10', 'web 200  api 200', 'whole again', GOOD)])
def s_models(C, D, dur):
    E = head('Putting it together', 'A map, a path, a label, a method.', C['o1']); E.append(ill(C['o1'] + 0.2, 1400, 170))
    E.append(Pop(card(840, 150, ACC, 'The map', [('browser, web service, API, database', TXT)], 40, 28), 100, 340, C['o2']))
    E.append(Pop(card(840, 150, VIO, 'The path', [('page: web  ·  data: API  ·  rows: DB', TXT)], 40, 28), 100, 530, C['o3']))
    E.append(Pop(card(840, 150, PINK, 'The label', [('one request ID in every diary', TXT)], 40, 28), 100, 720, C['o4']))
    E.append(Pop(card(840, 150, BAD, 'No page at all', [('suspect the web service', TXT)], 40, 28), 980, 340, C['o6'] + 0.5))
    E.append(Pop(card(840, 150, WARN, 'Page, but no products', [('suspect the API', TXT)], 40, 28), 980, 530, C['o6'] + 3.5))
    E.append(Pop(card(840, 150, GOOD, 'API answers, not ready', [('suspect the database', TXT)], 40, 28), 980, 720, C['o6'] + 7.0))
    E.append(Pop(badge('THE METHOD:  symptom, then one layer at a time', F('b', 34), INK, ACC, padx=28, pady=14), 100, 900, C['o5']))
    E.append(takeaway('A diagram you can trace is a system you can fix.', 985, C['o7'], WARN, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab74.sh starts CloudCart. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab74.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Ports', [('ss -ltn  >  parts.txt', TXT)], 'k3', ACC), ('2  Healthy', [('layers.sh  >  layers-up.txt', TXT)], 'k4', GOOD), ('3  Trace', [('request ID lab-74', TXT), ('grep  >  trace.txt', TXT)], 'k5', VIO), ('4  Break', [('api.sh stop', TXT), ('layers.sh  >  layers-down.txt', TXT)], 'k6', BAD), ('5  Answer', [('page: web', TXT), ('data: api', TXT), ('rows: database', TXT)], 'k7', PINK), ('6  Repair', [('api.sh start', TXT), ('then lab check', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 230, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Six PASS lines', 'q2'), ('Draw the four parts', 'q3'), ('Follow a request ID', 'q4'), ('Name the broken layer', 'q5'), ('Why the DB has no port', 'q6'), ('lab down, nothing listening', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Ports', 'list them, ask each layer', ACC, 'z3'), ('3  Trace', 'your ID in both diaries', VIO, 'z4'), ('4  Break', 'stop the API, ask again', BAD, 'z5'), ('5  Repair', 'answers, API started', WARN, 'z6'), ('6  Check', 'lab check, lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Name the four parts and their jobs', 'f12'), ('What does a request ID let you do?', 'f13'), ('Page loads, no products: which layer?', 'f14'), ('Why has the database no port?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC08-O08', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: the MC08 mastery lesson', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, draw=s_draw, parts=s_parts, trace=s_trace, layers=s_layers, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(draw=('board', ACC), parts=('test', GOOD), trace=('doc', ACC), layers=('board', WARN), models=('board', ACC), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'parts': [('m5', 2, 2, 0, 1020, ''), ('m8', 1, 1, 0, 140, 'PAGE'), ('m8b', 2, 1, 0, 140, 'DATA')],
 'trace': [('t7', 2, 2, 0, 1070, ''), ('t9', 1, 1, 0, 610, 'WEB'), ('t9b', 2, 1, 0, 810, 'API'), ('t11', 1, 3, 0, 400, '')],
 'layers': [('y7', 1, 1, 0, 140, 'PAGE OK'), ('y7b', 2, 1, 0, 140, 'NO ANSWER'), ('y10', 1, 2, 0, 140, 'WHOLE')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson74/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
