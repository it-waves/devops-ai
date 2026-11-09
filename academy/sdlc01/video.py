import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
LABEL = 'DEVOPS ENGINEERING BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "You tap the Buy button."), c('h2', "Seconds later, an order exists,"), c('h3', "and a package is on its way."),
  c('h4', "But before that button worked,"), c('h5', "somebody had to plan it,"), c('h6', "design it,"), c('h7', "build it,"), c('h8', "test it,"), c('h9', "and put it online."),
  c('h10', "That journey has a name: the software development life cycle, or S D L C.", "That journey has a name: the software development life cycle, or S D L C."),
  c('h11', "In this lesson, you will walk through all seven stages."),
 ]),
 ('roadmap', [
  c('r1', "We will follow one small online shop, called CloudCart,"), c('r2', "from first idea to real customer."),
  c('r3', "Seven stages."), c('r4', "Plan,"), c('r5', "requirements,"), c('r6', "design,"), c('r7', "build,"), c('r8', "test,"), c('r9', "deploy,"), c('r10', "and operate."),
  c('r11', "Then the loop starts again, with everything we learned."),
  c('r12', "By the end, you can name every stage, say what happens in it, and see where DevOps fits."),
 ]),
 ('plan', [
  c('p1', "Stage one: plan."), c('p2', "Before anyone writes code,"), c('p3', "the team agrees on the problem."),
  c('p4', "The owner wants to sell online."), c('p5', "Customers want to find things fast."), c('p6', "Developers need a clear goal."),
  c('p7', "For CloudCart, the goal is simple:"), c('p8', "customers browse products, and place an order."),
  c('p9', "Teams often track this work in a tool like GitHub."), c('p10', "A written plan stops you building the wrong thing."),
 ]),
 ('req', [
  c('q1', "Stage two: requirements."), c('q2', "Now the plan becomes a list of precise statements."),
  c('q3', "Functional requirements say what the system does:"), c('q4', "show the product list,"), c('q5', "place an order."),
  c('q6', "Non-functional requirements say how well it does it:"), c('q7', "answer within one second,"), c('q8', "keep passwords safe."),
  c('q9', "Vague requirements are why projects drift."),
 ]),
 ('design', [
  c('d1', "Stage three: design."), c('d2', "Here the team decides the parts of the system,"), c('d3', "and how they talk to each other."),
  c('d4', "CloudCart has a browser,"), c('d5', "an A P I,", "an A P I,"), c('d6', "and a data store."),
  c('d7', "The browser asks,"), c('d8', "the A P I answers,", "the A P I answers,"), c('d9', "and the data store remembers."),
  c('d10', "In our first version, the A P I is Java, running on Tomcat, and the data lives in memory.", "In our first version, the A P I is Java, running on Tomcat, and the data lives in memory."),
  c('d11', "A real database, Postgres, comes in a later lesson.", "A real database, Postgres sequel, comes in a later lesson."),
  c('d12', "Drawing this first lets people spot problems while they are still cheap to fix."),
 ]),
 ('build', [
  c('b1', "Stage four: build."), c('b2', "Developers turn the design into code."), c('b3', "This is real CloudCart source,"), c('b4', "the function that calculates an order total."),
  c('b5', "It checks the quantity,"), c('b6', "finds the product,"), c('b7', "and adds up the price."),
  c('b8', "Code lives in version control, called Git,"), c('b9', "so every change is tracked, and can be undone."), c('b10', "Then a build tool, Maven, packages it."),
 ]),
 ('test', [
  c('t1', "Stage five: test."), c('t2', "Automated tests check the code every time it changes."),
  c('t3', "Ours are written with J Unit,", "Ours are written with J Unit,"), c('t4', "and run on GitHub Actions."), c('t5', "This is a real run from our pipeline."),
  c('t6', "Seven A P I tests pass,", "Seven A P I tests pass,"), c('t7', "four order tests pass,"), c('t8', "eleven in total, zero failures,"), c('t9', "and the build succeeds."),
  c('t10', "If even one test failed, the change would stop here,"), c('t11', "before any customer sees it."),
 ]),
 ('deploy', [
  c('y1', "Stage six: release and deploy."), c('y2', "The tested package goes onto a server, and starts."), c('y3', "Our pipeline starts it on Tomcat,"), c('y4', "then checks it again while it is running."),
  c('y5', "The health check answers: up."), c('y6', "An order for two items totals seven thousand cents."), c('y7', "Runtime checks passed."),
  c('y8', "Passing tests,"), c('y9', "and a working deployment,"), c('y10', "are two different checks."), c('y11', "You need both."),
  c('y12', "Later, Docker and Kubernetes will do this job at scale."),
 ]),
 ('operate', [
  c('o1', "Stage seven: operate and learn."), c('o2', "We watch the system,"), c('o3', "listen to customers,"), c('o4', "and plan the next improvement."), c('o5', "Then the cycle starts again."),
  c('o6', "Tools like Prometheus and Grafana help us watch a running system."), c('o7', "DevOps is about making this loop fast, and safe."),
  c('o8', "Along the way, you will learn"), c('o9', "Git,"), c('o10', "Maven,"), c('o11', "Jenkins,"), c('o12', "Docker,"), c('o13', "Kubernetes,"), c('o14', "Terraform,", "terra form,"), c('o15', "and much more."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "Which stage decides what the system must do?"), c('z3', "Which stage catches a bad change before customers do?"), c('z4', "Which two checks prove an app really works?"),
  c('z5', "Pause the video, and answer out loud."), c('z6', "Next lesson: requirements, in depth."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'z5': 6.0, 'o5': 1.0, 'r11': 0.6, 'y11': 0.5, 'p10': 0.5, 'q9': 0.5, 'd12': 0.5, 'b9': 0.4}
CHAP = {'roadmap': 'Overview', 'plan': 'Plan', 'req': 'Requirements', 'design': 'Design', 'build': 'Build', 'test': 'Test', 'deploy': 'Deploy', 'operate': 'Operate', 'recap': 'Quick check'}
STAGES = ['Plan', 'Requirements', 'Design', 'Build', 'Test', 'Deploy', 'Operate']
SC = [ACC, VIO, GOOD, WARN, PINK, ACC, VIO]
def tracker(active, t):
    im = canvas(1720, 54); d = ImageDraw.Draw(im); f = F('s', 22); x = 0
    for i, n in enumerate(STAGES):
        lab = f'{i + 1}  {n}'; w = int(f.getlength(lab)) + 36
        if i == active: fill, fg, ol = ACC, INK, ACC
        elif i < active: fill, fg, ol = tint(GOOD, 50), GOOD, GOOD
        else: fill, fg, ol = PANEL, EN.DIM, EN.EDGE
        d.rounded_rectangle([x, 4, x + w, 46], radius=21, fill=fill, outline=ol, width=2); d.text((x + 18, 13), lab, font=f, fill=fg); x += w + 14
    return El(im, 100, 96, t, anim='fade', d=0.2)
def head(n, title, sub, t):
    return [El(T(f'Stage {n}', 'b', 30, ACC), 100, 175, t), El(T(title, 'x', 64), 100, 215, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=740), 100, 300, t + 0.4)]
def takeaway(s, y, t, col=None, w=800, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)

def s_hook(C, D, dur):
    E = []; fade = C['h4'] - 0.1
    ph = Pop(phone(), 260, 190, C['h1'] - 0.3); ph.t1 = fade; E.append(ph)
    btn = badge('   Buy   ', F('x', 76), INK, GOOD, padx=56, pady=30, r=30); bx, by = 260 + (430 - btn.width) // 2, 560
    e = Pop(btn, bx, by, C['h1'] - 0.1); e.t1 = fade; E.append(e); E.append(Ripple(bx + btn.width // 2, by + btn.height // 2, C['h1'] + 0.55, GOOD, 150))
    e = El(T('Your phone', 'b', 30, MUTED), 330, 880, C['h1'], anim='fade'); e.t1 = fade; E.append(e)
    hs = Pop(house(300), 1380, 380, C['h2']); hs.t1 = fade; E.append(hs); e = El(T('Customer', 'b', 36, GOOD), 1450, 690, C['h2'] + 0.3, anim='fade'); e.t1 = fade; E.append(e)
    E.append(Move(parcel(170), [(C['h2'], bx + btn.width // 2, by + 40), (C['h2'] + 0.9, 900, 330), (C['h3'] + 2.0, 1530, 520)], fade + 0.3, 6))
    e = El(T('Order placed', 'x', 46, GOOD), 760, 640, C['h2'] + 0.5, anim='fade'); e.t1 = fade; E.append(e)
    e = El(T('On its way', 'x', 46, ACC), 760, 720, C['h3'], anim='fade'); e.t1 = fade; E.append(e)
    e = ill(C['h1'], 1400, 130); e.t1 = fade; E.append(e)
    E.append(El(T('Before that button worked…', 'x', 70), 100, 190, C['h4']))
    items = [('Plan it', ACC, 'h5'), ('Design it', VIO, 'h6'), ('Build it', GOOD, 'h7'), ('Test it', PINK, 'h8'), ('Put it online', WARN, 'h9')]
    x = 100
    for n, col, cid in items:
        p = pill(n, x, 380, C[cid] - 0.05, col, INK, 54, 36, 20); E.append(p); x += p.img.width + 30
    E.append(Pop(badge('SDLC', F('x', 190), INK, ACC, padx=90, pady=34, r=56), 100, 600, C['h10'] + 0.9)); E.append(Ripple(330, 700, C['h10'] + 1.2, ACC, 220, 1.1))
    E.append(El(T('Software Development', 'x', 54), 860, 620, C['h10'] + 0.3)); E.append(El(T('Life Cycle', 'x', 54), 860, 690, C['h10'] + 0.5))
    E.append(El(T('7 stages', 'x', 64, GOOD), 860, 800, C['h11']))
    return E
def s_roadmap(C, D, dur):
    E = [El(T('One shop. Seven stages.', 'x', 60), 100, 130, C['r3']), ill(C['r3'], 1400, 140)]
    E.append(Pop(card(900, 120, GOOD, 'CloudCart', [], 44), 100, 250, C['r1']))
    E.append(El(T('our example online shop', 'm', 32, MUTED), 400, 288, C['r1'] + 0.5, anim='fade'))
    cw, gap, y = 205, 47, 480; ids = ['r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10']
    E.append(El(rrect(1720, 10, 5, fill=EN.EDGE, outline=EN.EDGE), 100, y - 60, C['r3'], anim='wipe', d=1.0))
    E.append(Pop(bulb(110), 85, 345, C['r2']))
    way = [(C['r2'], 140, 410)]
    for i, cid in enumerate(ids):
        x = 100 + i * (cw + gap); E.append(Pop(card(cw, 230, SC[i], f'{i + 1}', [(STAGES[i], TXT)], 80, 23), x, y, C[cid] - 0.05))
        way.append((C[cid] + 0.1, x + cw // 2, 410))
    E.append(Move(parcel(110), way, None, 4))
    E.append(Move(bulb(110), [(C['r2'], 140, 400), (C['r4'] - 0.1, 140, 400)], C['r4'] + 0.1))
    E.append(El(T('Then the loop starts again.', 'b', 40, MUTED), 640, 800, C['r11']))
    E.append(A([(1700, 740), (1700, 780), (180, 780), (180, 730)], C['r11'] + 0.3, MUTED, 5, 18, 0.9))
    for i, s in enumerate(['Name each stage', 'Say what happens in it', 'See where DevOps fits']):
        E.append(pill(s, 100 + i * 560, 920, C['r12'] + 0.3 + i * 1.5, [ACC, VIO, GOOD][i], INK, 34, 26, 14))
    return E
def s_plan(C, D, dur):
    E = [tracker(0, C['p1'])] + head(1, 'Plan', 'Agree on the problem before writing code.', C['p1']) + [ill(C['p1'])]
    notes = [('Owner', '"I want to sell online."', WARN, 'p4'), ('Customer', '"I want to find things fast."', ACC, 'p5'), ('Developer', '"I need a clear goal."', VIO, 'p6')]
    for i, (who, say, col, cid) in enumerate(notes):
        x = 100 + i * 590; E.append(Pop(card(540, 150, col, who, [(say, TXT)], 34), x, 400, C[cid])); E.append(A([(x + 270, 565), (x + 270, 625)], C[cid] + 0.8, col, 6, 24))
    E.append(Pop(card(1720, 160, GOOD, 'The goal', [('Customers browse products and place an order.', TXT)], 38), 100, 640, C['p7']))
    E.append(logo('github', 1670, 655, C['p9'], 110)); E.append(El(T('Teams track plans with issues and boards, for example in GitHub', 'm', 30, MUTED, maxw=1300), 100, 830, C['p9'] + 0.5, anim='fade'))
    E.append(takeaway('A written plan stops you building the wrong thing.', 910, C['p10'], WARN, 1500))
    return E
def s_req(C, D, dur):
    E = [tracker(1, C['q1'])] + head(2, 'Requirements', 'Turn the plan into precise statements.', C['q1']) + [ill(C['q1'])]
    cols = [(100, ACC, 'Functional', 'What it does', ['Show the product list', 'Place an order'], ['q3', 'q4', 'q5']), (990, VIO, 'Non-functional', 'How well it does it', ['Answer within 1 second', 'Keep passwords safe'], ['q6', 'q7', 'q8'])]
    for x, col, title, sub, rows, cids in cols:
        E.append(Pop(card(830, 440, col, title, [(sub, MUTED)], 46, 30), x, 400, C[cids[0]]))
        for i, r in enumerate(rows):
            y = 540 + i * 110; tt = C[cids[1 + i]]
            E.append(El(rrect(770, 90, 14, fill=(26, 58, 66), outline=EN.EDGE, width=2), x + 30, y, tt, anim='fade'))
            E.append(Pop(icon('check', 52, TXT, col), x + 52, y + 19, tt + 0.15)); E.append(El(T(r, 'b', 36), x + 130, y + 21, tt + 0.1, anim='fade'))
    E.append(takeaway('Vague requirements are why projects drift.', 900, C['q9'], WARN, 1500))
    return E
def s_design(C, D, dur):
    E = [tracker(2, C['d1'])] + head(3, 'Design', 'Decide the parts and how they talk.', C['d1']) + [ill(C['d1'])]
    X, Wd, Ht = 1000, 440, 130; ys = [270, 520, 770]; names = [('Browser', 'browser', ACC, 'd4'), ('API', 'server', VIO, 'd5'), ('Data store', 'server', GOOD, 'd6')]
    for (n, ic, col, cid), y in zip(names, ys):
        E.append(Pop(rrect(Wd, Ht, 18, fill=PANEL, outline=col, width=3), X, y, C[cid] - 0.05)); E.append(Pop(icon(ic, 84, TXT, col), X + 24, y + 23, C[cid])); E.append(El(T(n, 'b', 42, col), X + 140, y + 40, C[cid] + 0.15, anim='fade'))
    mid = X + Wd // 2
    for i, cid in enumerate(['d5', 'd6']):
        y0 = ys[i] + Ht + 8; y1 = ys[i + 1] - 8
        E.append(A([(mid - 40, y0), (mid - 40, y1)], C[cid] + 0.3, ACC, 7, 26)); E.append(A([(mid + 40, y1), (mid + 40, y0)], C[cid] + 0.5, GOOD, 7, 26))
    pk = lambda s, col: badge(s, F('b', 24), INK, col, padx=14, pady=6, r=14)
    E.append(Move(pk('GET /api/products', ACC), [(C['d7'], mid - 40, ys[0] + Ht + 20), (C['d7'] + 0.8, mid - 40, ys[1] - 20)], C['d7'] + 1.5))
    E.append(Move(pk('products (JSON)', GOOD), [(C['d8'], mid + 40, ys[1] - 20), (C['d8'] + 0.8, mid + 40, ys[0] + Ht + 20)], C['d8'] + 1.6))
    E.append(Move(pk('look up', ACC), [(C['d9'], mid - 40, ys[1] + Ht + 20), (C['d9'] + 0.7, mid - 40, ys[2] - 20)], C['d9'] + 1.2))
    E.append(El(T('asks', 'm', 28, ACC), X - 230, ys[0] + Ht + 36, C['d7'] + 0.2, anim='fade')); E.append(El(T('answers', 'm', 28, GOOD), X - 230, ys[0] + Ht + 76, C['d8'] + 0.2, anim='fade'))
    E.append(El(T('remembers', 'm', 28, GOOD), X - 230, ys[1] + Ht + 56, C['d9'] + 0.2, anim='fade'))
    E.append(logo('java', 1520, 440, C['d10'], 100, 'Java')); E.append(logo('tomcat', 1650, 440, C['d10'] + 1.0, 100, 'Tomcat'))
    E.append(El(T('v0: data in memory', 'm', 24, MUTED), 1520, 590, C['d10'] + 2.0, anim='fade'))
    E.append(logo('postgresql', 1520, 780, C['d11'], 100, 'Postgres')); E.append(pill('LATER', 1650, 800, C['d11'] + 0.8, EN.WARN, INK, 26, 18, 8))
    E.append(takeaway('Fix problems on paper, while they are cheap.', 520, C['d12'], WARN, 800))
    return E
SRC = [('public Order place(List<Line> lines) {', TXT), ('  int total = 0;', TXT), ('  for (Line l : lines) {', TXT),
       ('    if (l.quantity() < 1 || l.quantity() > 100) {', WARN), ('      throw new IllegalArgumentException(', WARN), ('        "quantity must be 1 to 100");', WARN), ('    }', TXT),
       ('    Product p = catalog.find(l.productId())...', ACC), ('    total += p.priceCents() * l.quantity();', GOOD), ('  }', TXT), ('  return new Order(total, count);', TXT)]
def s_build(C, D, dur):
    E = [tracker(3, C['b1'])] + head(4, 'Build', 'Developers write the code.', C['b1'])
    E.append(real(C['b3'], 'REAL FILE  ·  OrderService.java (abridged)', 100, 420))
    CX, CY, LH, FS = 910, 270, 46, 26
    E.append(El(term_frame(980, 600, 'OrderService.java'), CX - 30, CY - 20, C['b3'], anim='fade'))
    for i, (s, col) in enumerate(SRC): E.append(El(T(s, 'mono', FS, col), CX, CY + 50 + i * LH, C['b4'] + i * 0.12, anim='fade', d=0.2))
    def hl(i0, i1, cid, col): return bar(CX - 12, CY + 50 + i0 * LH - 4, 940, (i1 - i0 + 1) * LH, C[cid], C[cid + '.e'] + 0.2, col)
    E += [hl(3, 5, 'b5', WARN), hl(7, 7, 'b6', ACC), hl(8, 8, 'b7', GOOD)]
    E.append(logo('git', 100, 560, C['b8'], 120, 'Git')); E.append(El(T('tracks every change', 'm', 26, MUTED, maxw=190), 100, 735, C['b9'], anim='fade'))
    E.append(logo('maven', 330, 560, C['b10'], 120, 'Maven')); E.append(logo('java', 480, 560, C['b10'] + 0.4, 120, 'Java'))
    E.append(El(T('packages it into a WAR', 'm', 26, MUTED, maxw=400), 330, 735, C['b10'] + 0.9, anim='fade'))
    return E
def s_test(C, D, dur):
    E = [tracker(4, C['t1'])] + head(5, 'Test', 'Automated checks on every change.', C['t1'])
    E.append(logo('junit', 100, 430, C['t3'], 120, 'JUnit')); E.append(logo('actions', 270, 430, C['t4'], 120, 'GitHub Actions'))
    E.append(real(C['t5'], 'REAL CI RUN  ·  GitHub Actions', 100, 640))
    E.append(El(term_frame(1000, 470, 'build job  —  mvn verify'), 870, 250, C['t5'], anim='fade'))
    L = [('[INFO] Tests run: 7, Failures: 0, Errors: 0', 't6', TXT), ('[INFO] Tests run: 4, Failures: 0, Errors: 0', 't7', TXT), ('[INFO] Tests run: 11, Failures: 0, Errors: 0', 't8', GOOD), ('[INFO] BUILD SUCCESS', 't9', GOOD)]
    for i, (s, cid, col) in enumerate(L):
        y = 340 + i * 75; E.append(El(T(s, 'mono', 25, col), 910, y, C[cid], anim='fade', d=0.2))
        if i < 3: E.append(Pop(icon('check', 40, TXT, GOOD), 1800, y - 4, C[cid] + 0.3))
    E.append(Pop(badge('  PASS  ', F('x', 56), INK, GOOD, padx=36, pady=14, r=26), 1500, 545, C['t9'] + 0.4)); E.append(Ripple(1590, 570, C['t9'] + 0.6, GOOD, 120))
    E.append(El(T('Sample of the real log', 'm', 24, MUTED), 910, 645, C['t9'] + 0.2, anim='fade'))
    E.append(Pop(badge('ONE FAILURE  →  CHANGE STOPPED', F('x', 40), INK, EN.BAD, padx=30, pady=16, r=22), 100, 800, C['t10'] + 0.5)); E.append(ill(C['t10'], 100, 890))
    E.append(El(T('before any customer sees it', 'b', 38, WARN), 100, 940, C['t11']))
    return E
def s_deploy(C, D, dur):
    E = [tracker(5, C['y1'])] + head(6, 'Release and deploy', 'Put the tested package on a server and start it.', C['y1'])
    E.append(logo('tomcat', 100, 470, C['y3'], 120, 'Tomcat 10.1.34'))
    E.append(real(C['y4'], 'REAL CI RUN  ·  deploy job', 100, 700))
    E.append(El(term_frame(1000, 470, 'deploy job  —  runtime checks'), 870, 250, C['y4'], anim='fade'))
    L = [('$ curl localhost:8080/cloudcart/health', 'y5', EN.OUT, 0), ('{"version":"0.1.0","status":"UP"}', 'y5', GOOD, 1.1), ("$ curl -X POST -d '{\"items\":[...]}' /api/orders", 'y6', EN.OUT, 0),
         ('{"totalCents":7000,"itemCount":2}', 'y6', GOOD, 1.6), ('RUNTIME CHECKS PASSED', 'y7', GOOD, 0)]
    for i, (s, cid, col, o) in enumerate(L): E.append(El(T(s, 'mono', 24, col), 910, 340 + i * 70, C[cid] + o, anim='fade', d=0.2))
    E.append(Pop(icon('check', 44, TXT, GOOD), 1790, 340 + 4 * 70 - 4, C['y7'] + 0.3))
    a = pill('Tests passed', 100, 800, C['y8'], GOOD, INK, 38, 28, 14); b = pill('Deployment works', 780, 800, C['y9'], ACC, INK, 38, 28, 14)
    E += [a, b, El(T('≠', 'x', 72, WARN), 560, 770, C['y10'], anim='fade'), El(T('Two different checks. You need both.', 'b', 38, WARN), 100, 900, C['y11'])]
    E.append(logo('docker', 1230, 780, C['y12'], 100, 'Docker')); E.append(logo('kubernetes', 1360, 780, C['y12'] + 0.7, 100, 'Kubernetes')); E.append(pill('LATER', 1500, 800, C['y12'] + 1.3, EN.WARN, INK, 26, 18, 8))
    return E
def s_operate(C, D, dur):
    E = [tracker(6, C['o1'])] + head(7, 'Operate and learn', 'Watch it, listen to customers, improve.', C['o1']) + [ill(C['o1'])]
    cx, cy, R = 1380, 520, 215; bw, bh = 210, 90
    nodes = [(-90, 'Plan', ACC, 'o4'), (0, 'Build', VIO, 'o4'), (90, 'Deploy', GOOD, 'o3'), (180, 'Operate', WARN, 'o2')]
    boxes = [(cx + R * math.cos(math.radians(a)) - bw / 2, cy + R * math.sin(math.radians(a)) - bh / 2, cx + R * math.cos(math.radians(a)) + bw / 2, cy + R * math.sin(math.radians(a)) + bh / 2) for a, _, _, _ in nodes]
    order = [3, 2, 0, 1]
    for k, i in enumerate(order):
        a, n, col, cid = nodes[i]; b = boxes[i]; E.append(Pop(card(bw, bh, col, n, [], 36), b[0], b[1], C[['o2', 'o3', 'o4', 'o4'][k]] + (0.6 if k == 3 else 0)))
    for i, (a, n, col, _) in enumerate(nodes):
        s0 = next(x for x in range(0, 60) if outside(arc_pts(cx, cy, R, a + x, a + x, 1)[0], boxes)); s1 = next(x for x in range(0, 60) if outside(arc_pts(cx, cy, R, a + 90 - x, a + 90 - x, 1)[0], boxes))
        E.append(A(arc_pts(cx, cy, R, a + s0, a + 90 - s1, 28), C['o5'] + i * 0.35, ACC, 7, 28, 0.6))
    E.append(El(T('keep learning', 'm', 28, MUTED, align='center'), cx - 90, cy - 18, C['o5'] + 1.2, anim='fade'))
    E.append(logo('prometheus', 100, 470, C['o6'], 110, 'Prometheus')); E.append(logo('grafana', 270, 470, C['o6'] + 1.5, 110, 'Grafana')); E.append(pill('LATER', 420, 490, C['o6'] + 2.4, EN.WARN, INK, 26, 18, 8))
    E.append(takeaway('DevOps = a faster, safer loop', 680, C['o7'], GOOD, 800, 46))
    E.append(El(T('Tools you will learn:', 'b', 30, MUTED), 100, 790, C['o8']))
    for i, (n, cid) in enumerate([('git', 'o9'), ('maven', 'o10'), ('jenkins', 'o11'), ('docker', 'o12'), ('kubernetes', 'o13'), ('terraform', 'o14')]): E.append(logo(n, 100 + i * 150, 840, C[cid], 112))
    E.append(El(T('+ more', 'x', 40, ACC), 1010, 880, C['o15'], anim='fade'))
    return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    for i, (q, cid) in enumerate([('Which stage decides what the system must do?', 'z2'), ('Which stage catches a bad change before customers do?', 'z3'), ('Which two checks prove an app really works?', 'z4')]):
        E.append(Pop(card(1720, 110, [ACC, VIO, GOOD][i], f'{i + 1}', [], 36), 100, 290 + i * 140, C[cid])); E.append(El(T(q, 'm', 38, maxw=1500), 190, 316 + i * 140, C[cid] + 0.1, anim='fade'))
    E.append(Pop(badge('PAUSE  ·  answer out loud', F('b', 34), INK, PINK, padx=26, pady=14), 100, 760, C['z5']))
    E.append(El(T('Next: Requirements, in depth', 'x', 56, ACC), 100, 880, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 1450, 890, C['z7']))
    return E
FN = dict(hook=s_hook, roadmap=s_roadmap, plan=s_plan, req=s_req, design=s_design, build=s_build, test=s_test, deploy=s_deploy, operate=s_operate, recap=s_recap)
