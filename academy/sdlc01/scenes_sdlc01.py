import sys; sys.path.insert(0, '/home/claude/osi'); sys.path.insert(0, '/home/claude/academy/sdlc01')
import theme
from engine import *
from PIL import Image, ImageDraw
PINK = (198, 172, 240); VIO = (140, 164, 240)
def T(s, w='m', size=34, color=TXT, maxw=None, align='left', lh=1.32): return text_img(s, F(w, size), color, maxw, lh, align)
STAGES = ['Plan', 'Requirements', 'Design', 'Build', 'Test', 'Deploy', 'Operate']
def card(w, h, col, title, lines, tsize=36, lsize=30):
    im = rrect(w, h, 18, fill=PANEL, outline=col, width=3); d = ImageDraw.Draw(im)
    d.text((28, 22), title, font=F('b', tsize), fill=col); y = 22 + tsize + 22
    for s, c in lines:
        t = T(s, 'm', lsize, c, maxw=w - 40); im.alpha_composite(t, (28, y)); y += t.height + 8
    return im
def tracker(active):
    x = 100; E = []
    im = canvas(1720, 54); d = ImageDraw.Draw(im); f = F('s', 22); x = 0
    for i, n in enumerate(STAGES):
        lab = f'{i + 1}  {n}'; w = int(f.getlength(lab)) + 36
        if i == active: fill, fg, ol = ACC, (12, 18, 28), ACC
        elif i < active: fill, fg, ol = tint(GOOD, 50), GOOD, GOOD
        else: fill, fg, ol = PANEL, DIM, EDGE
        d.rounded_rectangle([x, 4, x + w, 46], radius=21, fill=fill, outline=ol, width=2); d.text((x + 18, 13), lab, font=f, fill=fg); x += w + 14
    return El(im, 100, 96, 0.15, anim='fade')
def stage_title(n, title, sub, t):
    return [El(T(f'Stage {n}', 'b', 30, ACC), 100, 175, t), El(T(title, 'x', 64), 100, 215, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=760), 100, 305, t + 0.3)]
def ill(t, x=1400, y=170): return El(badge('ILLUSTRATION  ·  not a capture', F('b', 24), (12, 18, 28), WARN, padx=16, pady=8), x, y, t, anim='fade')
def real(t, label, x=1100, y=170): return El(badge(label, F('b', 24), (12, 18, 28), GOOD, padx=16, pady=8), x, y, t, anim='fade')
def arrow(x0, y0, x1, y1, col=ACC, lw=6):
    import math
    pad = 24; x = min(x0, x1) - pad; y = min(y0, y1) - pad; w = abs(x1 - x0) + 2 * pad; h = abs(y1 - y0) + 2 * pad
    im = canvas(w, h); d = ImageDraw.Draw(im); a, b = (x0 - x, y0 - y), (x1 - x, y1 - y)
    d.line([a, b], fill=col, width=lw); ang = math.atan2(b[1] - a[1], b[0] - a[0])
    for s in (2.6, -2.6):
        d.line([b, (b[0] - 26 * math.cos(ang + s * 0.2 + 0), b[1] - 26 * math.sin(ang + s * 0.2))], fill=col, width=lw)
    return im, x, y
def termbox(w, h, title, lines, ts, x, y, fs=27):
    base = term_frame(w, h, title); E = [El(base, x, y, ts[0] - 0.4, anim='fade', d=0.3)]; yy = y + 70
    for ln, t, col in zip(lines, ts, [l[1] for l in lines] if False else [None] * len(lines)): pass
    return base, E
def lines_el(lines, x, y, fs=27, lh=None):
    lh = lh or int(fs * 1.55); out = []
    for i, (txt, t, col) in enumerate(lines):
        out.append(El(T(txt, 'mono', fs, col, maxw=None), x, y + i * lh, t, anim='fade', d=0.25))
    return out


import math
def arrow2(pts, col=ACC, lw=7, head=30):
    """polyline arrow with a filled triangular head that follows the last segment."""
    pad = head + lw
    xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
    x0, y0 = min(xs) - pad, min(ys) - pad; w = int(max(xs) - min(xs) + 2 * pad); h = int(max(ys) - min(ys) + 2 * pad)
    S = 3; im = canvas(w * S, h * S); d = ImageDraw.Draw(im)
    P = [((q[0] - x0) * S, (q[1] - y0) * S) for q in pts]
    (ax, ay), (bx, by) = P[-2], P[-1]; ang = math.atan2(by - ay, bx - ax); hl = head * S
    base = (bx - hl * 0.9 * math.cos(ang), by - hl * 0.9 * math.sin(ang))
    d.line(P[:-1] + [base], fill=col, width=lw * S, joint='curve')
    wing = hl * 0.52
    tri = [(bx, by), (base[0] + wing * math.sin(ang), base[1] - wing * math.cos(ang)), (base[0] - wing * math.sin(ang), base[1] + wing * math.cos(ang))]
    d.polygon(tri, fill=col)
    return El(im.resize((w, h), Image.LANCZOS), 0, 0, 0), x0, y0
def A(pts, t, col=ACC, lw=7, head=30, anim='fade', d=0.5):
    e, x0, y0 = arrow2(pts, col, lw, head); return El(e.img, x0, y0, t, anim=anim, d=d)
def arc_pts(cx, cy, r, a0, a1, n=24):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
def outside(pt, boxes, m=14):
    return all(not (b[0] - m <= pt[0] <= b[2] + m and b[1] - m <= pt[1] <= b[3] + m) for b in boxes)

def s_hook(C, D, dur):
    t = C['h1']; E = []
    E.append(El(icon('browser', 300, TXT, ACC), 1050, 250, t, anim='fade'))
    E.append(El(badge('  Buy  ', F('x', 44), (12, 18, 28), GOOD, padx=40, pady=18, r=18), 1110, 640, t + 1.5))
    E.append(El(T("Every app starts as an idea", 'x', 66, maxw=880), 100, 250, t))
    E.append(ill(t, 100, 130))
    E.append(El(T('Who built this?', 'b', 52, PINK), 100, 520, C['h2']))
    E.append(El(T('How did it get to you?', 'b', 52, PINK), 100, 600, C['h2'] + 1.8))
    E.append(El(T('The software development life cycle (SDLC)', 'm', 36, MUTED, maxw=820), 100, 720, C['h2'] + 4.5))
    return E
def s_roadmap(C, D, dur):
    t = C['r1']; E = [El(T('One shop. Seven stages.', 'x', 64), 100, 130, t), ill(t, 1400, 140)]
    cols = [ACC, VIO, GOOD, WARN, PINK, ACC, VIO]; cw, gap, y = 205, 47, 330
    for i, n in enumerate(STAGES):
        x = 100 + i * (cw + gap); tt = t + 1.5 + i * 0.9
        E.append(El(card(cw, 190, cols[i], f'{i + 1}', [(n, TXT)], 60, 22), x, y, tt, anim='fade'))
        if i < 6: E.append(A([(x + cw + 6, y + 95), (x + cw + gap - 6, y + 95)], tt + 0.5, MUTED, 5, 18))
    E.append(El(T('Then the cycle repeats.', 'b', 34, MUTED), 640, 585, t + 8.0))
    E.append(A([(1940 - 100, 540), (1940 - 100, 540)], 999)) if False else None
    E.append(A([(1700, 540), (1700, 560), (180, 560), (180, 530)], t + 8.2, MUTED, 5, 18))
    E.append(El(card(900, 190, GOOD, 'CloudCart', [('our example online shop, from idea to customer', MUTED)], 44), 100, 640, C['r2']))
    E.append(El(T('Name each stage  ·  say what happens  ·  see where DevOps fits', 'm', 34, MUTED, maxw=760), 1050, 680, C['r2'] + 1.0))
    return [e for e in E if e is not None]

def s_plan(C, D, dur):
    t = C['p1']; E = [tracker(0)] + stage_title(1, 'Plan', 'Agree on the problem before writing code.', t) + [ill(t)]
    notes = [('Owner', '"I want to sell online."', WARN), ('Customer', '"I want to find things fast."', ACC), ('Developer', '"I need a clear goal."', VIO)]
    for i, (who, say, col) in enumerate(notes):
        tt = t + 3.0 + i * 1.6; y = 250 + i * 175
        E.append(El(card(520, 150, col, who, [(say, TXT)], 32), 1300, y, tt, anim='left'))
        E.append(A([(1290, y + 75), (1090, 610)], tt + 0.6, col, 6, 26))
    E.append(El(card(980, 190, GOOD, 'The goal', [('Customers browse products and place an order.', TXT)], 38), 100, 520, C['p2'] + 0.5))
    E.append(El(T('A written plan avoids building the wrong thing.', 'b', 38, WARN, maxw=860), 100, 760, C['p3'] + 0.3))
    return E

def s_req(C, D, dur):
    t = C['q1']; E = [tracker(1)] + stage_title(2, 'Requirements', 'Turn the plan into precise statements.', t) + [ill(t)]
    E.append(El(card(620, 300, ACC, 'Functional', [('What it does', MUTED), ('Show the product list', TXT), ('Place an order', TXT)], 40), 100, 440, C['q2']))
    E.append(El(card(620, 300, VIO, 'Non-functional', [('How well it does it', MUTED), ('Answer within 1 second', TXT), ('Keep passwords safe', TXT)], 40), 790, 440, C['q3']))
    E.append(El(T('Vague requirements make projects drift.', 'b', 38, WARN), 100, 800, C['q3'] + 6.0))
    return E
def s_design(C, D, dur):
    t = C['d1']; E = [tracker(2)] + stage_title(3, 'Design', 'Decide the parts and how they talk.', t) + [ill(t)]
    parts = [(1000, 280, 'Browser', 'browser', ACC, C['d2']), (1000, 560, 'API', 'server', VIO, C['d2'] + 3.5), (1000, 840, 'Data store', 'server', GOOD, C['d2'] + 7.0)]
    for x, y, n, ic, col, tt in parts:
        E.append(El(rrect(460, 150, 18, fill=PANEL, outline=col, width=3), x, y, tt, anim='fade'))
        E.append(El(icon(ic, 100, TXT, col), x + 24, y + 25, tt + 0.1, anim='fade')); E.append(El(T(n, 'b', 44, col), x + 150, y + 48, tt + 0.2, anim='fade'))
    mid = 1000 + 150
    for i, (up, down) in enumerate([('asks', 'answers'), ('reads and writes', 'returns data')]):
        y0 = 280 + 150 + 12 + i * 280; y1 = y0 + 280 - 150 - 24; tt = C['d2'] + 2.0 + i * 3.5
        E.append(A([(mid - 40, y0), (mid - 40, y1)], tt, ACC, 7, 28)); E.append(A([(mid + 40, y1), (mid + 40, y0)], tt + 0.6, GOOD, 7, 28))
        E.append(El(T(up, 'm', 28, ACC), 1000 + 230, y0 + 18, tt + 0.2, anim='fade')); E.append(El(T(down, 'm', 28, GOOD), 1000 + 230, y0 + 58, tt + 0.8, anim='fade'))
    E.append(El(T('Fix problems on paper, while they are cheap.', 'b', 36, WARN, maxw=800), 100, 520, C['d3']))
    return E

SRC = [('public Order place(List<Line> lines) {', TXT), ('  int total = 0;', TXT), ('  for (Line l : lines) {', TXT),
       ('    if (l.quantity() < 1 || l.quantity() > 100) {', WARN), ('      throw new IllegalArgumentException(', WARN), ('        "quantity must be 1 to 100");', WARN), ('    }', TXT),
       ('    Product p = catalog.find(l.productId())...', TXT), ('    total += p.priceCents() * l.quantity();', GOOD), ('  }', TXT), ('  return new Order(total, count);', TXT)]
def s_build(C, D, dur):
    t = C['b1']; E = [tracker(3)] + stage_title(4, 'Build', 'Developers write the code.', t)
    E.append(real(t, 'REAL FILE  ·  OrderService.java (abridged)', 100, 400))
    E.append(El(term_frame(1000, 560, 'OrderService.java'), 880, 250, t + 0.5, anim='fade'))
    ts = [C['b2'] + i * 1.0 for i in range(len(SRC))]
    E += lines_el([(s, tt, col) for (s, col), tt in zip(SRC, ts)], 910, 320, 25, 42)
    E.append(El(T('Version control tracks every change.', 'b', 38, ACC, maxw=720), 100, 560, C['b3']))
    E.append(El(T('Git, in a later lesson', 'm', 30, MUTED), 100, 620, C['b3'] + 1.5))
    return E
def s_test(C, D, dur):
    t = C['t1']; E = [tracker(4)] + stage_title(5, 'Test', 'Automated checks on every change.', t)
    E.append(real(t, 'REAL CI RUN  ·  GitHub Actions', 100, 400))
    E.append(El(term_frame(1000, 420, 'build job  —  mvn verify'), 880, 250, t + 0.5, anim='fade'))
    L = [('[INFO] Tests run: 7, Failures: 0, Errors: 0, Skipped: 0', 'ApiTest', TXT), ('[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0', 'OrderServiceTest', TXT),
         ('[INFO] Tests run: 11, Failures: 0, Errors: 0, Skipped: 0', '', GOOD), ('[INFO] BUILD SUCCESS', '', GOOD)]
    ts = [C['t2'] + 0.5, C['t2'] + 2.0, C['t2'] + 3.5, C['t2'] + 5.0]
    E += lines_el([(l[0].replace('Tests run: ', 'Tests run: '), tt, l[2]) for l, tt in zip(L, ts)], 910, 330, 24, 56)
    E.append(El(T('One failure would stop the change here.', 'b', 38, WARN, maxw=720), 100, 560, C['t3']))
    return E
def s_deploy(C, D, dur):
    t = C['y1']; E = [tracker(5)] + stage_title(6, 'Release and deploy', 'Put the tested package on a server and start it.', t)
    E.append(real(t, 'REAL CI RUN  ·  deploy job, Tomcat 10.1.34', 100, 470))
    E.append(El(term_frame(1000, 460, 'deploy job  —  runtime checks'), 880, 250, t + 0.5, anim='fade'))
    L = [('$ curl localhost:8080/cloudcart/health', C['y2'] + 0.0, OUT), ('{"version":"0.1.0","status":"UP"}', C['y2'] + 1.2, GOOD),
         ('$ curl -X POST -d \'{"items":[{"productId":2,"quantity":2}]}\' ...', C['y2'] + 3.2, OUT), ('{"totalCents":7000,"itemCount":2}', C['y2'] + 4.8, GOOD), ('RUNTIME CHECKS PASSED', C['y2'] + 6.5, GOOD)]
    E += lines_el(L, 910, 330, 23, 62)
    E.append(El(T('Tests passed  ≠  deployment works', 'x', 44, WARN, maxw=760), 100, 600, C['y3']))
    E.append(El(T('Check both.', 'b', 44, GOOD), 100, 680, C['y3'] + 2.0))
    return E
def s_operate(C, D, dur):
    t = C['o1']; E = [tracker(6)] + stage_title(7, 'Operate and learn', 'Watch it, listen to customers, improve.', t) + [ill(t)]
    cx, cy, R = 1380, 590, 235; bw, bh = 210, 92
    nodes = [(-90, 'Plan', ACC), (0, 'Build', VIO), (90, 'Deploy', GOOD), (180, 'Operate', WARN)]
    boxes = []
    for a, n, col in nodes:
        x = cx + R * math.cos(math.radians(a)); y = cy + R * math.sin(math.radians(a)); boxes.append((x - bw / 2, y - bh / 2, x + bw / 2, y + bh / 2))
    for i, ((a, n, col), b) in enumerate(zip(nodes, boxes)):
        E.append(El(card(bw, bh, col, n, [], 36), b[0], b[1], t + 2.0 + i * 1.2, anim='fade'))
    for i, (a, n, col) in enumerate(nodes):
        a0 = a; a1 = a + 90
        s0 = next(x for x in range(0, 60) if outside(arc_pts(cx, cy, R, a0 + x, a0 + x, 1)[0], boxes)); s1 = next(x for x in range(0, 60) if outside(arc_pts(cx, cy, R, a1 - x, a1 - x, 1)[0], boxes))
        E.append(A(arc_pts(cx, cy, R, a0 + s0, a1 - s1, 28), t + 3.4 + i * 1.2, ACC, 7, 30, d=0.7))
    E.append(El(T('keep learning', 'm', 30, MUTED, align='center'), cx - 110, cy - 20, t + 8.0, anim='fade'))
    E.append(El(T('DevOps = a faster, safer loop', 'x', 46, GOOD, maxw=700), 100, 520, C['o2']))
    for i, n in enumerate(['Git', 'Maven', 'Jenkins', 'Docker', 'Kubernetes']):
        E.append(El(badge(n, F('b', 30), (12, 18, 28), [ACC, VIO, GOOD, WARN, PINK][i], padx=20, pady=10), 100 + i * 190, 700, C['o2'] + 3.0 + i * 1.2, anim='fade'))
    return E

def s_recap(C, D, dur):
    t = C['z1']; E = [El(T('Quick check', 'x', 72), 100, 130, t)]
    qs = ['Which stage decides what the system must do?', 'Which stage catches a bad change before customers do?', 'Which two checks prove an app really works?']
    for i, q in enumerate(qs): E.append(El(card(1720, 110, [ACC, VIO, GOOD][i], f'{i + 1}', [], 36), 100, 290 + i * 140, t + 2.5 + i * 3.0, anim='fade')); E.append(El(T(q, 'm', 38, maxw=1500), 190, 316 + i * 140, t + 2.6 + i * 3.0, anim='fade'))
    E.append(El(badge('PAUSE  ·  answer out loud', F('b', 30), (12, 18, 28), PINK, padx=22, pady=12), 100, 760, C['z2']))
    E.append(El(T('Next: Requirements, in depth', 'x', 52, ACC), 100, 880, C['z3']))
    E.append(El(badge('SUBSCRIBE', F('b', 30), (12, 18, 28), GOOD, padx=22, pady=12), 1500, 890, C['z3'] + 1.5))
    return E
FN = dict(hook=s_hook, roadmap=s_roadmap, plan=s_plan, req=s_req, design=s_design, build=s_build, test=s_test, deploy=s_deploy, operate=s_operate, recap=s_recap)
