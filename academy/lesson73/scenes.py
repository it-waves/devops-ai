def s_hook(C, D, dur):
    E = [El(T('Is the shop OK?', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(840, 140, ACC, 'Three in the morning', [('nobody is watching the shop', TXT)], 44, 32), 100, 330, C['h1'] + 1.2))
    E.append(Pop(card(840, 110, BAD, 'Customers see errors', [], 44, 32), 100, 500, C['h1'] + 5.0))
    E.append(Pop(card(840, 110, WARN, 'Who finds out first?', [], 44, 32), 100, 630, C['h1'] + 8.0))
    mv = [('Health check', 'is it alive?', ACC), ('Readiness', 'can it work now?', VIO), ('Logs, metrics', 'what, and how much', GOOD), ('Errors', 'caught, labelled, logged', PINK)]
    for i, (n, s_, col) in enumerate(mv): E.append(Pop(card(420, 170, col, n, [(s_, TXT)], 36, 26, True), 1000 + (i % 2) * 440, 330 + (i // 2) * 200, C['h3'] + 2.0 + i * 2.4))
    E.append(Pop(badge('ALIVE?', F('x', 52), INK, ACC, padx=34, pady=18), 100, 800, C['h2'] + 3.0)); E.append(Pop(badge('READY?', F('x', 52), INK, VIO, padx=34, pady=18), 400, 800, C['h2'] + 5.5)); E.append(Pop(badge('WHY?', F('x', 52), INK, WARN, padx=34, pady=18), 700, 800, C['h2'] + 8.0))
    E.append(takeaway('Break it. Watch it explain itself.', 980, C['h4'] + 1.0, GOOD, 1700)); return E
s_probes = _lab('Alive or ready?', 'Two questions a machine can ask your program.', 'p1', RB, [('p2', './start.sh', 'start the shop', ACC), ('p3', './probe.sh', 'ask both questions', VIO), ('p4', 'alive 200  ·  ready 200', 'all is well', GOOD), ('p6', 'database file away', 'a failed disk, on purpose', BAD), ('p8b', 'ready: 503', 'alive, but not ready', WARN), ('p10', 'file back', 'ready again, no restart', GOOD)])
s_errors = _lab('Errors travel upward', 'Catch, label, log, show a safe message.', 'e1', RB, [('e4', 'database fails', 'the file is moved away', BAD), ('e5', 'customer asks', 'request ID: demo-42', VIO), ('e6', 'safe message', 'no secrets, no crash', GOOD), ('e7', 'grep the ID', 'search the log', ACC), ('e8', 'the real cause', 'no such table: products', WARN), ('e10', 'repaired', 'back to normal', GOOD)])
s_logs = _lab('Logs: the diary', 'One line per event: time, level, request ID.', 'l1', RB, [('l4', 'INFO  200', 'normal: a product served', GOOD), ('l5', 'WARN  404', 'a missing product', WARN), ('l6', 'WARN  401', 'not logged in', WARN), ('l7', 'cat api.log', 'read the diary', ACC), ('l9', 'time, level, ID', 'every line has them', VIO), ('l10', 'no passwords', 'never log secrets', BAD)])
s_metrics = _lab('Metrics: the numbers', 'Counters that only ever go up.', 'm1', RB, [('m4', 'traffic.sh', 'five pretend customers', VIO), ('m5', '/metrics', 'ask for the numbers', ACC), ('m6', 'requests: 5', 'three good, one 4xx, one 5xx', GOOD), ('m7', '5xx = our failures', 'the number to watch', BAD), ('m8', 'grep 5xx', 'one number on its own', WARN)])
def s_models(C, D, dur):
    E = head('Putting it together', 'Know if it is alive, ready, busy, or failing.', C['o1']); E.append(ill(C['o1'] + 0.2, 1400, 170))
    E.append(Pop(card(840, 150, ACC, 'Health check', [('is it alive?  no: restart it', TXT)], 40, 30), 100, 340, C['o2']))
    E.append(Pop(card(840, 150, VIO, 'Readiness', [('not ready? stop sending customers', TXT)], 40, 28), 980, 340, C['o3']))
    E.append(Pop(card(840, 190, GOOD, 'Logs', [('the diary of events', TXT), ('time, level, request ID', TXT)], 40, 28), 100, 530, C['o4']))
    E.append(Pop(card(840, 190, WARN, 'Metrics', [('numbers over time', TXT), ('latency, traffic, errors, saturation', TXT)], 40, 28), 980, 530, C['o5']))
    E.append(Pop(card(840, 140, BAD, 'Error propagation', [('catch, label, log, safe message', TXT)], 40, 28), 100, 750, C['o6']))
    E.append(Pop(card(840, 140, PINK, 'Request ID', [('one label follows the request', TXT)], 40, 28), 980, 750, C['o7']))
    E.append(takeaway('Kubernetes probes, Prometheus metrics, central logs.', 950, C['o8'], WARN, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab73.sh starts CloudCart. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab73.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Healthy', [('probe.sh  >  up.txt', TXT)], 'k3', GOOD), ('2  Broken', [('db file away', TXT), ('probe.sh  >  down.txt', TXT)], 'k4', BAD), ('3  Trace', [('request ID lab-73', TXT), ('its log line  >  rid.txt', TXT)], 'k5', VIO), ('4  Count', [('/metrics  >  metrics.txt', TXT)], 'k6', WARN), ('5  Answer', [('restart: healthz', TXT), ('traffic: readyz', TXT)], 'k7', PINK), ('6  Repair', [('database back, ready again', TXT)], 'k8', ACC)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 230, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Six PASS lines', 'q2'), ('Alive versus ready', 'q3'), ('Follow a request ID', 'q4'), ('Read the 5xx counter', 'q5'), ('Safe error, cause in log', 'q6'), ('lab down, nothing listening', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Probe', 'healthy, then broken', BAD, 'z3'), ('3  Trace', 'one request ID in the log', VIO, 'z4'), ('4  Count', 'save the metrics', WARN, 'z5'), ('5  Repair', 'answers, database back', ACC, 'z6'), ('6  Check', 'lab check, lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Alive and ready: what differs?', 'f12'), ('What does a request ID connect?', 'f13'), ('Logs or metrics: how much?', 'f14'), ('What should the customer see?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC08-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: draw the shop, trace a request', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, probes=s_probes, errors=s_errors, logs=s_logs, metrics=s_metrics, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(probes=('test', GOOD), errors=('doc', BAD), logs=('doc', ACC), metrics=('board', WARN), models=('board', ACC), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'probes': [('p4', 1, 2, 0, 1060, ''), ('p8', 1, 1, 0, 1060, ''), ('p8b', 2, 1, 0, 1060, ''), ('p12', 1, 2, 0, 1060, '')],
 'errors': [('e6', 2, 1, 0, 900, ''), ('e8', 1, 1, 676, 1046, '')],
 'logs': [('l8', 1, 1, 0, 690, 'INFO'), ('l8b', 2, 2, 0, 690, 'WARN')],
 'metrics': [('m6', 3, 1, 0, 480, 'ALL REQUESTS'), ('m7', 6, 1, 0, 480, 'OUR FAILURES')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson73/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
