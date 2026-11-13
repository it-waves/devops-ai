def s_hook(C, D, dur):
    E = [El(T('One tap, three programs', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(1100, 140, WARN, 'You tap Buy', [('a spinner, half a second, then: done', TXT)], 44, 32), 100, 290, C['h1'] + 2.0))
    for i, (a, b, col) in enumerate([('Frontend', 'what you see and touch', ACC), ('Backend', 'the rules and the decisions', VIO), ('Database', 'the memory', GOOD)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 470 + i * 150, C['h2'] + i * 2.4))
    E.append(takeaway('Know which is which.', 960, C['h4'], GOOD, 1700)); return E
def s_roles(C, D, dur):
    E = head('Three roles', 'A restaurant, in software.', C['r1']); E.append(ill(C['r1'] + 0.2, 1400, 170))
    it = [('Frontend', 'the dining room', 'pages, buttons, forms: runs in the browser', ACC, 'r2'), ('Backend', 'the kitchen', 'rules, prices, decisions', VIO, 'r3'), ('Database', 'the pantry', 'remembers: products, users, orders', GOOD, 'r4')]
    for i, (n, a, s_, col, cid) in enumerate(it):
        E.append(Pop(card(540, 250, col, n, [(a, WARN), (s_, TXT)], 48, 32), 100 + i * 590, 340, C[cid]))
    E.append(Pop(card(1700, 150, WARN, 'The order of the journey', [], 36), 100, 640, C['r5']))
    E.append(El(T('browser   →   backend   →   database   →   back to the browser', 'mono', 34, TXT, align='left'), 140, 722, C['r5'] + 0.6, anim='wipe', d=2.4))
    E.append(Pop(card(840, 130, PINK, 'Monolith', [('everything in one process', TXT)], 40, 30), 100, 830, C['r6']))
    E.append(Pop(card(840, 130, ACC, 'Service', [('a small program with one job', TXT)], 40, 30), 960, 830, C['r7'])); return E
s_mono = _lab('One process: a monolith', 'Page, rules and data from one program.', 'm1', RB, [('m3', './start.sh mono', 'One program starts', ACC), ('m4', 'curl :8080', 'The frontend: HTML', VIO), ('m5', 'curl :8080/api/products', 'The backend: JSON data', WARN), ('m7', 'showdb.py', 'The database: a file', GOOD), ('m8', 'ss -ltn', 'One listener: port 8080', PINK)])
s_split = _lab('Two services', 'The same shop, split in two.', 'p0', RB, [('p1', './start.sh split', 'Two programs start', ACC), ('p2', 'ss -ltn', 'Two listeners: 5000 and 8080', VIO), ('p3', 'curl :5000', 'Backend: data only', WARN), ('p4', 'grep 5000', 'The page calls the backend', PINK), ('p5', './stop.sh', 'Nothing left running', GOOD)])
from PIL import Image as _Im, ImageDraw as _ID
def _frame(path, url, w, crop_h, src_w=1100):
    im = _Im.open('/home/claude/academy/lesson67/shots/' + path).convert('RGB').crop((0, 0, src_w, crop_h)); sc = w / src_w; im = im.resize((w, int(crop_h * sc)))
    H = im.height + 56; out = _Im.new('RGBA', (w, H), (0, 0, 0, 0)); d = _ID.Draw(out)
    d.rounded_rectangle([0, 0, w - 1, H - 1], radius=18, fill=(34, 44, 52, 255), outline=(120, 140, 150, 255), width=3)
    for i, col in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]): d.ellipse([20 + i * 30, 18, 38 + i * 30, 36], fill=col)
    d.rounded_rectangle([130, 10, w - 24, 46], radius=18, fill=(18, 26, 32, 255)); d.text((150, 16), url, font=ImageFont.truetype(MONO, 22), fill=(200, 225, 220, 255))
    mask = _Im.new('L', im.size, 255); md = _ID.Draw(mask); md.rectangle([0, 0, im.width, im.height], fill=255)
    out.paste(im, (0, 56)); return out
def s_browser(C, D, dur):
    E = head('The browser view', 'The same shop, seen by a customer and by a program.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E[-1] = El(badge('REAL SCREENSHOT  ·  Chrome', F('b', 24), INK, GOOD, padx=16, pady=8), 1400, 170, C['w1'] + 0.2, anim='fade')
    E.append(Pop(_frame('page.png', 'http://127.0.0.1:8080/', 1000, 330), 100, 330, C['w2']))
    E.append(Pop(_frame('json.png', 'http://127.0.0.1:5000/api/products', 1000, 120, 1140), 100, 730, C['w4']))
    E.append(Pop(card(640, 150, ACC, 'Frontend', [('for people: the page', TXT)], 44, 32), 1180, 340, C['w2'] + 0.8))
    E.append(Pop(card(640, 150, VIO, 'Backend', [('for programs: the data', TXT)], 44, 32), 1180, 740, C['w4'] + 0.8))
    E.append(Pop(card(640, 190, WARN, 'The journey', [('page asks backend', TXT), ('backend asks database', TXT)], 40, 30), 1180, 540, C['w3']))
    E.append(takeaway('People: page. Programs: data.', 940, C['w5'], GOOD, 1700)); return E
def s_trade(C, D, dur):
    E = head('The trade-off', 'Neither shape is better. It is a trade.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(El(T('Benefits of splitting', 'b', 36, GOOD), 100, 330, C['t2']))
    for i, (a, b, cid) in enumerate([('Scale separately', 'more backend copies, small frontend', 't2'), ('Deploy separately', 'fix a button, leave the backend alone', 't3'), ('Fail separately', 'one part down, not everything', 't4')]):
        E.append(Pop(card(840, 130, GOOD, a, [(b, TXT)], 40, 30), 100, 390 + i * 150, C[cid]))
    E.append(El(T('Cost of splitting', 'b', 36, BAD), 1000, 330, C['t5']))
    E.append(Pop(card(820, 280, BAD, 'More moving parts', [('more programs', TXT), ('more ports and network calls', TXT), ('more places to look', TXT)], 40, 30), 1000, 390, C['t5']))
    E.append(takeaway('Start simple. Split when it hurts.', 870, C['t6'], WARN, 1700))
    E.append(Pop(card(1700, 90, ACC, 'ss shows who listens   ·   curl shows what each one says', [], 34), 100, 940, C['t7'])); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab67.sh starts the monolith. lab check judges your split.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab67.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('lab up', 'cloud cart starts as one process', 'k3', ACC), ('1  backend', 'port 5000 answers JSON', 'k4', VIO), ('2  frontend', 'port 8080 page calls 5000', 'k5', WARN), ('3  separate', 'two different processes', 'k6', PINK), ('4  answers.txt', 'db: and the service name', 'k7', BAD), ('lab check', 'four PASS lines', 'k8', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 230, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Four PASS lines', 'b2'), ('Backend alone, with curl', 'b3'), ('Who listens: ss', 'b4'), ('Three roles in a sentence', 'b5'), ('One benefit, one cost', 'b6'), ('lab down, nothing listening', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Find', 'ss -ltn: the monolith', ACC, 'z3'), ('3  Split', 'with start.sh', WARN, 'z4'), ('4  Ask', 'curl both ports', VIO, 'z5'), ('5  Check', 'answers.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Frontend: what and where?', 'f12'), ('What does the backend do?', 'f13'), ('Why a database?', 'f14'), ('One benefit, one cost of splitting?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC08-O01', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: requests, REST and JSON', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, roles=s_roles, mono=s_mono, split=s_split, browser=s_browser, trade=s_trade, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(roles=('board', ACC), mono=('code', WARN), split=('code', VIO), browser=('doc', ACC), trade=('board', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson67/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
