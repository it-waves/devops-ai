def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('REST APIs from Python', 'x', 72), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Authentication', 'a token in a header, from the environment', ACC), ('Timeouts', 'never wait forever on a server', GOOD), ('Pagination', 'follow every page, not just the first', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 2.4))
    E.append(takeaway('Three habits for every API call.', 850, C['h3'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('What a REST API is', 'A web address that answers with data.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 215, ACC, 'GET', [('read data', TXT), ('POST creates data', MUTED)], 44, 32, True), 100, 340, C['w2']))
    E.append(Pop(card(540, 215, VIO, '200', [('success', TXT), ('401 not logged in', MUTED)], 44, 32, True), 690, 340, C['w3']))
    E.append(Pop(card(540, 215, WARN, '500+', [('server problem', TXT), ('retry later', MUTED)], 44, 32, True), 1280, 340, C['w3'] + 3.0))
    E.append(Pop(card(1700, 150, GOOD, 'requests + JSON', [('r = requests.get(url, timeout=5)    ->    r.json()', TXT)], 38, 30), 100, 620, C['w4']))
    E.append(takeaway('Prove who you are. Never wait forever. Ask for every page.', 850, C['w5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Get the lab and task', 'Everything is in the repository.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 't2', ACC), ('Folder', 'academy/lesson50', 't3', VIO), ('Files', 'TASK.md  api06.py  check50.sh', 't3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 't3'), ('cd devops-ai/academy/lesson50 && pip install requests', 't3'), ('# write fetch.py: token + timeout + all pages', 't4'), ('bash check50.sh .      # four PASS lines', 't5')]
    E.append(Pop(glass(1700, 4 * 46 + 48, WARN), 100, 700, C['t3']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, python3, your venv. Your own machine only. No peeking at the solution first.', 'm', 26, MUTED, maxw=1700), 100, 960, C['t6'], anim='fade')); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['r1'])
    items = [('Checker: four PASS', 'r2'), ('Token from env, clear error', 'r3'), ('timeout= on every call', 'r4'), ('raise_for_status()', 'r5'), ('All pages collected', 'r6'), ('Complete report, own VM', 'r7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['r8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only.', C['z1'])
    it = [('1  Get files', 'lesson50 folder, pip install requests', PINK, 'z2'), ('2  Run the API', 'api06.py, then export API_TOKEN', ACC, 'z3'), ('3  Request', 'header + timeout=5', WARN, 'z4'), ('4  Pages', 'loop until next_page is None', VIO, 'z5'), ('5  Print', 'servers and stopped', BAD, 'z6'), ('6  Check', 'four PASS, then report', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which header carries a bearer token?', 'f12'), ('What if a request has no timeout?', 'f13'), ('What does raise_for_status() do?', 'f14'), ('How do you know there are more pages?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC06-O04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: exceptions, logging, retries', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_basics = _lab('A first request', 'GET, a status code, and JSON.', 'b1', RB, [('b2', 'import requests', 'installed in the venv', ACC), ('b3', 'requests.get(url, timeout=5)', 'always set a timeout', VIO), ('b4', 'r.status_code', '200 means success', GOOD), ('b5', 'r.json()', 'decoded to a dict', WARN)])
s_auth = _lab('Authentication with a token', 'A header, and a token from the environment.', 'a1', RB, [('a1', 'export API_TOKEN=...', 'lab token, not a real one', ACC), ('a5', 'no token', '401: not authorized', BAD), ('a6', 'Authorization: Bearer', 'header with the token', VIO), ('a7', 'with the header', '200: we are in', GOOD), ('a8', '.json()["total"]', 'ten servers', WARN)])
s_timeout = _lab('Timeouts', 'Never wait forever on a server.', 'o1', RB, [('o1', 'cat timeout.py', 'try / except Timeout', ACC), ('o2', 'timeout=1', 'gave up after one second', BAD), ('o3', 'sed: timeout=5', 'edit in place', VIO), ('o4', 'timeout=5', 'ok 200', GOOD)])
s_pages = _lab('Pagination', 'Follow next_page until it is None.', 'g1', RB, [('g1', 'cat pages.py', 'while page: ...', ACC), ('g2', 'raise_for_status()', 'bad status stops the script', WARN), ('g2', 'page = data["next_page"]', 'follow every page', VIO), ('g3', '10 servers', 'four pages of three', GOOD)])
FN = dict(hook=s_hook, why=s_why, basics=s_basics, auth=s_auth, timeout=s_timeout, pages=s_pages, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('board', ACC), basics=('gear', ACC), auth=('test', VIO), timeout=('gear', WARN), pages=('board', GOOD), task=('gear', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'basics': [('b5', 1, 1, 4, 50, ''), ('b6', 1, 1, 4, 250, '')],
 'auth': [('a6', 1, 1, 4, 50, ''), ('a8', 1, 1, 4, 50, ''), ('a9', 1, 1, 4, 36, '')],
 'timeout': [('o3', 1, 1, 4, 508, ''), ('o5', 1, 1, 4, 98, '')],
 'pages': [('g3', 1, 1, 4, 386, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson50/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
