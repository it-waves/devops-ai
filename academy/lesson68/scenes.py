def s_hook(C, D, dur):
    E = [El(T('Every tap asks a question', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(1100, 140, WARN, 'Request', [('"What is the weather in Boston?"', TXT)], 44, 32), 100, 330, C['h2']))
    E.append(Pop(card(1100, 140, GOOD, 'Response', [('"61 degrees, cloudy"', TXT)], 44, 32), 100, 500, C['h2'] + 2.6))
    E.append(Pop(badge('REQUEST  →', F('b', 40), INK, WARN, padx=28, pady=14), 1300, 360, C['h3']))
    E.append(Pop(badge('←  RESPONSE', F('b', 40), INK, GOOD, padx=28, pady=14), 1300, 530, C['h3'] + 1.8))
    E.append(Pop(card(1100, 140, ACC, 'Read both, line by line', [('real commands, real output', TXT)], 44, 32), 100, 700, C['h3'] + 4.0))
    E.append(takeaway('First check when an app breaks.', 960, C['h4'], GOOD, 1700)); return E
def s_anatomy(C, D, dur):
    E = head('Request and response', 'Two messages. Every single time.', C['a1']); E.append(ill(C['a1'] + 0.2, 1400, 170))
    E.append(El(T('REQUEST  ·  what the client sends', 'b', 32, ACC), 100, 320, C['a1'] + 0.3)); E.append(El(T('RESPONSE  ·  what the server sends back', 'b', 32, GOOD), 980, 320, C['a5']))
    rq = [('Method', 'GET  (read)     POST  (create)     DELETE  (remove)', ACC, 'a2'), ('Path', '/api/products/1', VIO, 'a3'), ('Headers', 'Content-Type: application/json', WARN, 'a4'), ('Body', '{"name": "Mug", "price": 9}   (optional)', PINK, 'a4')]
    for i, (n, s_, col, cid) in enumerate(rq): E.append(Pop(card(840, 125, col, n, [(s_, TXT)], 34, 26), 100, 375 + i * 135, C[cid] + (1.8 if i == 3 else 0)))
    rs = [('Status code', '200 O K   ·   404 Not Found   ·   500 Error', GOOD, 'a6'), ('Headers', 'Content-Type: application/json', WARN, 'a5'), ('Body', '{"id": 1, "name": "Backpack"}', PINK, 'a5')]
    for i, (n, s_, col, cid) in enumerate(rs): E.append(Pop(card(840, 125, col, n, [(s_, TXT)], 34, 26), 980, 375 + i * 135, C[cid] + (0.9 if cid == 'a5' and i == 2 else 0)))
    E.append(Pop(badge('READ THE STATUS CODE FIRST', F('b', 38), INK, GOOD, padx=30, pady=16), 980, 790, C['a6'] + 1.0))
    E.append(takeaway('Method and path go in. Status and body come out.', 940, C['a6'] + 1.5, WARN, 1700)); return E
s_get = _lab('Your first request', 'One request, one response, read line by line.', 'g1', RB, [('g2', './start.sh', 'The shop and its API start', ACC), ('g3', 'curl -i  .../products/1', 'Ask for one product', VIO), ('g4', 'Status line', '200 O K = it worked', GOOD), ('g5', 'Headers', 'type and length', WARN), ('g7', 'curl  .../products', 'No id: the whole list', PINK)])
def s_json(C, D, dur):
    E = head('Reading JSON', 'The body of almost every API response.', C['j1']); E.append(real(C['j1'] + 0.2, 'REAL OUTPUT  ·  from the API', 1330, 170))
    lines = ['{', '  "id": 1,', '  "name": "Backpack",', '  "price": 39.0', '}']
    E.append(Pop(card(820, 330, ACC, '', [], 4), 100, 330, C['j1']))
    for i, s_ in enumerate(lines): E.append(El(T(s_, 'mono', 36, TXT, align='left'), 150, 360 + i * 58, C['j1'] + 0.3 + i * 0.25, anim='fade'))
    leg = [('{ }   Object', 'one thing, with named fields', ACC, 0.0), ('"name"   Key', 'the field name, always in quotes', VIO, 1.6), ('"Backpack"   Text', 'text goes in quotes', GOOD, 3.4), ('39.0   Number', 'numbers have no quotes', WARN, 5.2)]
    for i, (n, s_, col, off) in enumerate(leg): E.append(Pop(card(880, 120, col, n, [(s_, TXT)], 36, 28), 980, 330 + i * 135, C['j3'] + off))
    E.append(Pop(card(820, 230, PINK, '', [], 4), 100, 690, C['j4']))
    E.append(El(T('[', 'mono', 36, TXT, align='left'), 150, 705, C['j4'] + 0.3, anim='fade')); E.append(El(T('  {"id": 1, ...},', 'mono', 36, TXT, align='left'), 150, 752, C['j4'] + 0.5, anim='fade')); E.append(El(T('  {"id": 2, ...}', 'mono', 36, TXT, align='left'), 150, 799, C['j4'] + 0.8, anim='fade')); E.append(El(T(']', 'mono', 36, TXT, align='left'), 150, 846, C['j4'] + 1.0, anim='fade'))
    E.append(Pop(card(880, 120, PINK, '[ ]   List', [('items in a row, commas between', TXT)], 36, 28), 980, 870, C['j4'] + 0.5))
    E.append(Pop(badge('jq  =  JSON, tidy', F('b', 38), INK, GOOD, padx=30, pady=16), 100, 960, C['j5'])); return E
s_status = _lab('Status codes', 'The first thing to read in any response.', 's1', RB, [('s3', 'GET  .../products/99', 'A product that is not there', ACC), ('s4', '404 Not Found', 'your request is wrong', BAD), ('s5', 'The body', 'explains the error', WARN), ('s6', 'POST, no price', 'an incomplete request', VIO), ('s7', '400 Bad Request', 'the fault is in what you sent', BAD)])
def s_rest(C, D, dur):
    E = head('REST endpoints', 'One noun. Four verbs.', C['x1']); E.append(ill(C['x1'] + 0.2, 1400, 170))
    rows = [('GET', '/api/products', 'read the list', '200', ACC), ('GET', '/api/products/1', 'read one', '200', VIO), ('POST', '/api/products', 'create one', '201', WARN), ('DELETE', '/api/products/3', 'remove one', '204', PINK)]
    E.append(El(T('METHOD', 'b', 26, MUTED), 150, 322, C['x1'] + 0.3)); E.append(El(T('PATH', 'b', 26, MUTED), 470, 322, C['x1'] + 0.3)); E.append(El(T('MEANING', 'b', 26, MUTED), 1010, 322, C['x1'] + 0.3)); E.append(El(T('SUCCESS CODE', 'b', 26, MUTED), 1440, 322, C['x1'] + 0.3))
    for i, (m, p, mean, code, col) in enumerate(rows):
        t = C['x3'] + i * dur['x3'] / 4.2; y = 360 + i * 135
        E.append(Pop(card(1700, 115, col, '', [], 4), 100, y, t))
        E.append(El(chip(m, col, 32, 20, 8), 130, y + 22, t + 0.2, anim='fade')); E.append(El(T(p, 'mono', 32, TXT, align='left'), 470, y + 36, t + 0.2, anim='fade'))
        E.append(El(T(mean, 'm', 32, TXT, maxw=380), 1010, y + 36, t + 0.2, anim='fade')); E.append(El(chip(code, GOOD, 32, 22, 8), 1440, y + 22, t + 0.2, anim='fade'))
    E.append(Pop(badge('noun:  products', F('b', 34), INK, ACC, padx=28, pady=14), 100, 940, C['x2']))
    E.append(El(T('Same address, different verb, different action.', 'b', 36, WARN, maxw=1100), 640, 945, C['x4'], anim='fade'))
    E.append(El(T('PUT and PATCH update things. Not today.', 'm', 28, MUTED, maxw=900), 640, 1005, C['x5'], anim='fade')); return E
s_write = _lab('Create and delete', 'POST adds data. DELETE removes it.', 'w1', RB, [('w3', 'POST  .../products', 'create a mug, price 9', ACC), ('w4', '201 Created', 'the new id is 4', GOOD), ('w5', 'GET the list again', 'the mug is there', VIO), ('w6', 'DELETE  .../4', 'remove the mug', WARN), ('w7', '204 No Content', 'success, nothing to say', GOOD), ('w8', 'jq length', 'three products left', PINK)])
from PIL import Image as _Im, ImageDraw as _ID
def _frame(path, url, w, crop_h, src_w=1100):
    im = _Im.open('/home/claude/academy/lesson68/shots/' + path).convert('RGB').crop((0, 0, src_w, crop_h)); sc = w / src_w; im = im.resize((w, int(crop_h * sc)))
    H = im.height + 56; out = _Im.new('RGBA', (w, H), (0, 0, 0, 0)); d = _ID.Draw(out)
    d.rounded_rectangle([0, 0, w - 1, H - 1], radius=18, fill=(34, 44, 52, 255), outline=(120, 140, 150, 255), width=3)
    for i, col in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]): d.ellipse([20 + i * 30, 18, 38 + i * 30, 36], fill=col)
    d.rounded_rectangle([130, 10, w - 24, 46], radius=18, fill=(18, 26, 32, 255)); d.text((150, 16), url, font=ImageFont.truetype(MONO, 22), fill=(200, 225, 220, 255))
    out.paste(im, (0, 56)); return out
def s_browser(C, D, dur):
    E = head('The page shows it', 'Created and deleted with curl. Seen in the browser.', C['b1']); E.append(real(C['b1'] + 0.2, 'REAL SCREENSHOT  ·  Chrome', 1330, 170))
    E.append(El(T('BEFORE', 'b', 34, MUTED), 100, 330, C['b1'])); E.append(El(T('AFTER', 'b', 34, GOOD), 980, 330, C['b2']))
    E.append(Pop(_frame('before.png', 'http://127.0.0.1:8080/', 840, 495, 1650), 100, 380, C['b1'] + 0.3))
    E.append(Pop(_frame('after.png', 'http://127.0.0.1:8080/', 840, 495, 1650), 980, 380, C['b2'] + 0.8))
    E.append(Pop(card(840, 120, ACC, 'Backpack, Water bottle, Notebook', [('3 products', TXT)], 34, 28), 100, 730, C['b1'] + 0.8))
    E.append(Pop(card(840, 120, GOOD, 'Backpack, Water bottle, Mug', [('POST added the Mug, DELETE removed the Notebook', TXT)], 34, 24), 980, 730, C['b2'] + 1.6))
    E.append(takeaway('Only the data changed. The page code did not.', 940, C['b3'], WARN, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab68.sh starts CloudCart. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab68.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('lab up', 'the API starts on port 5000', 'k3', ACC), ('1  POST', 'create a Mug, price 9, once', 'k4', VIO), ('2  DELETE', 'remove product 3', 'k5', WARN), ('3  created:', 'the status code of your POST', 'k6', PINK), ('4+5  more codes', 'missing: and bad:', 'k7', BAD), ('lab check', 'five PASS lines', 'k8', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 230, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['r1'])
    items = [('Five PASS lines', 'r2'), ('Method, path, status: found', 'r3'), ('4xx versus 5xx explained', 'r4'), ('Create and delete with curl', 'r5'), ('JSON: object, list, text, number', 'r6'), ('lab down, nothing listening', 'r7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['r8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Read', 'curl -i: the status line', ACC, 'z3'), ('3  Create', 'POST the mug', VIO, 'z4'), ('4  Delete', 'product 3', WARN, 'z5'), ('5  Check', 'answers.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Method and path: what are they?', 'f12'), ('404: what does it mean? Whose fault?', 'f13'), ('4xx versus 5xx?', 'f14'), ('Which method creates? Which code?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC08-O02', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: testing endpoints like a pro', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, anatomy=s_anatomy, get=s_get, json=s_json, status=s_status, rest=s_rest, write=s_write, browser=s_browser, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(anatomy=('doc', ACC), get=('code', WARN), json=('doc', GOOD), status=('test', BAD), rest=('board', ACC), write=('code', VIO), browser=('doc', ACC), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'get': [('g4', 1, 1, 0, 240, 'STATUS CODE'), ('g5', 4, 2, 0, 470, 'HEADERS'), ('g6', 8, 1, 0, 680, 'THE BODY')],
 'status': [('s4', 2, 1, 0, 345, 'YOUR request is wrong'), ('s7', 2, 1, 0, 376, 'the fault is in what you sent')],
 'write': [('w4', 2, 1, 0, 315, 'CREATED'), ('w4', 8, 1, 0, 392, 'where it lives'), ('w4', 10, 1, 0, 590, 'new id'), ('w6', 5, 1, 0, 515, 'the new one'), ('w7', 2, 1, 0, 360, 'success, no body')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson68/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
