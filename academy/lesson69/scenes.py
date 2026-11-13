def s_hook(C, D, dur):
    E = [El(T('Test any endpoint', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(1100, 140, BAD, 'Slow?  Broken?  Your mistake?', [('Do not guess. Look at the conversation.', TXT)], 44, 32), 100, 330, C['h1'] + 1.2))
    E.append(Pop(badge('curl', F('b', 56), INK, ACC, padx=40, pady=20), 1350, 350, C['h2']))
    mv = [('-v', 'see everything', ACC), ('-I  -H', 'read and send headers', VIO), ('-w', 'measure the time', WARN), ('-f', 'use the exit code', GOOD), ('X-Request-Id', 'find it in the logs', PINK)]
    for i, (n, s_, col) in enumerate(mv): E.append(Pop(card(540, 150, col, n, [(s_, TXT)], 40, 28, True), 100 + (i % 3) * 590, 530 + (i // 3) * 175, C['h3'] + 2.0 + i * 1.8))
    E.append(takeaway('Five moves. Most endpoint testing.', 960, C['h4'], GOOD, 1700)); return E
s_verbose = _lab('See everything with verbose', 'curl -v shows both directions of the conversation.', 'v1', RB, [('v2', './start.sh', 'The shop and its API start', ACC), ('v3', 'curl -sv  ...', 'show the conversation', VIO), ('v4', '>  what curl sent', 'method, path, host, accept', WARN), ('v5', '<  what came back', 'status line and headers', GOOD), ('v6', 'Two custom headers', 'X-API-Version, X-Request-Id', PINK)])
s_headers = _lab('Read and send headers', 'Headers are labels. You can read them and set them.', 'd1', RB, [('d3', 'curl -sI  ...', 'headers only, no body', ACC), ('d4', 'Response headers', 'type, length, API version', WARN), ('d5', 'curl -H "Accept: ..."', 'send a header of your own', VIO), ('d6', 'CSV, not JSON', 'the server read the header', GOOD)])
s_timing = _lab('Measure the time', 'curl -w prints exactly the numbers you ask for.', 't1', RB, [('t3', 'curl -w  .../fast', 'status code and total time', ACC), ('t4', '-o /dev/null', 'throw the body away', WARN), ('t5', 'curl -w  .../report', 'same command, new path', VIO), ('t6', 'A number, not a feeling', 'which one is slow', GOOD)])
s_exit = _lab('Exit codes', 'A 404 is success for curl. Unless you add -f.', 'e1', RB, [('e3', 'curl  .../99', '404 body, exit 0', WARN), ('e4', 'exit=0', 'curl itself worked', BAD), ('e5', 'curl -f  .../99', 'fail on a 4xx or 5xx', VIO), ('e6', 'exit=22', 'the server said error', GOOD), ('e7', 'Smoke test', 'one curl, pass or fail', ACC)])
s_trace = _lab('Request IDs and logs', 'Tag a request, then find it in the API log.', 'r1', RB, [('r3', '-H "X-Request-Id: demo-42"', 'your own label', ACC), ('r4', 'tail api.log', 'the API wrote it down', VIO), ('r5', 'id=demo-42', 'find the exact line', GOOD), ('r6', './codes.sh', 'a tiny API client', WARN), ('r7', '200  200  404  200', 'status of four endpoints', PINK)])
def s_clients(C, D, dur):
    E = head('Other API clients', 'Different tools, the same ideas.', C['c1']); E.append(ill(C['c1'] + 0.2, 1400, 170))
    it = [('Browser DevTools', 'network tab: headers and timing', ACC, 'c2'), ('Postman  ·  Bruno', 'saved requests a team can share', VIO, 'c3'), ('httpie', 'prettier output on the command line', WARN, 'c4'), ('Scripts', 'curl after every deploy', GOOD, 'c5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s_, TXT)], 44, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 230, C[cid]))
    E.append(Pop(card(1720, 110, ACC, '', [('method  ·  path  ·  headers  ·  body  ·  status  ·  timing', TXT)], 4, 40), 100, 820, C['c6']))
    E.append(takeaway('Pick any. Know the ideas.', 960, C['c6'] + 1.0, WARN, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab69.sh starts CloudCart. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab69.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Version', 'from a response header', 'k3', VIO), ('2  CSV', 'Accept header, products.csv', 'k4', WARN), ('3  Slow', 'time both, name the slow one', 'k5', PINK), ('4  smoke.sh', 'exit 0 on success, else not', 'k6', BAD), ('5  Request ID', 'lab69-trace in the log', 'k7', ACC), ('lab check', 'five PASS lines', 'k8', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 230, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Read curl -v output', 'q3'), ('Send and read a header', 'q4'), ('Measure: name the slow one', 'q5'), ('Exit 0 on a 404? Why. Fix: -f', 'q6'), ('lab down, nothing listening', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Headers', 'read the version', ACC, 'z3'), ('3  CSV', 'save products.csv', VIO, 'z4'), ('4  Time', 'name the slow one', WARN, 'z5'), ('5  Script + ID', 'smoke.sh, lab69-trace', BAD, 'z6'), ('6  Check', 'lab check, lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('curl -v: what do the two arrows mean?', 'f12'), ('How do you send a header?', 'f13'), ('Exit 0 on a 404? Why? What fixes it?', 'f14'), ('What is a request ID for?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC08-O03', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: who are you? Auth and secrets', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, verbose=s_verbose, headers=s_headers, timing=s_timing, exit=s_exit, trace=s_trace, clients=s_clients, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(verbose=('code', ACC), headers=('doc', VIO), timing=('board', WARN), exit=('test', BAD), trace=('doc', GOOD), clients=('board', ACC), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'verbose': [('v4', 2, 4, 0, 462, 'WHAT CURL SENT'), ('v5', 6, 8, 0, 492, 'WHAT CAME BACK'), ('v6', 11, 2, 0, 371, 'TWO CUSTOM HEADERS')],
 'headers': [('d4', 4, 1, 0, 462, 'WHAT THE BODY IS'), ('d4', 6, 1, 0, 310, 'API VERSION'), ('d6', 2, 1, 0, 204, 'CSV, NOT JSON')],
 'timing': [('t4', 2, 1, 0, 190, 'STATUS AND TIME'), ('t6', 2, 1, 0, 190, 'ALMOST A SECOND')],
 'exit': [('e4', 3, 1, 0, 97, 'CURL WORKED')],
 'trace': [('r5', 1, 1, 0, 584, 'YOUR REQUEST ID'), ('r7', 3, 1, 0, 325, 'THE MISSING ONE')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson69/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
