import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 4  ·  DEVOPS BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "You tap Add to cart in CloudCart."), c('h2', "In under a second, many parts work together."),
  c('h3', "Some parts run when a customer uses the shop."), c('h4', "Others carry the code from a developer's laptop to that running shop."),
  c('h5', "Today you learn all nine parts, and how they fit."), c('h6', "By the end, you will explain each one in plain words."),
 ]),
 ('groups', [
  c('g1', "Split the nine parts into two groups."), c('g2', "The first four run when customers use the shop: frontend, backend, A P I, and database.", "The first four run when customers use the shop: frontend, backend, A P I, and database."),
  c('g3', "The other five move the code to that running shop: source control, build, release, deployment, and operations."),
  c('g4', "DevOps work lives mostly in the second group, but you must understand the first."), c('g5', "We start with the first group."),
 ]),
 ('frontend', [
  c('f1', "The frontend is what the user sees and touches."), c('f2', "It runs in the browser, or in a mobile app."),
  c('f3', "In CloudCart: the product pages, the cart, and the checkout form."), c('f4', "Web frontends are built with HTML, CSS, and JavaScript.", "Web frontends are built with H T M L, C S S, and JavaScript."),
  c('f5', "The frontend shows information, and sends the user's actions onward."), c('f6', "Never trust it to hide secrets, because users can inspect it."),
 ]),
 ('backend', [
  c('b1', "The backend is the code that runs on a server."), c('b2', "It applies the rules of the business."),
  c('b3', "For example: is the item in stock, and is the price correct?"), c('b4', "It also decides who is allowed to do what."),
  c('b5', "It talks to the database, and to other services."), c('b6', "Backends are written in languages like Java, Python, or JavaScript on Node."),
  c('b7', "Users never see it directly, but every action depends on it."),
 ]),
 ('api', [
  c('a1', "How do the frontend and the backend talk? Through an A P I.", "How do the frontend and the backend talk? Through an A P I."),
  c('a2', "A P I means application programming interface: a defined way for one program to ask another for something.", "A P I means application programming interface: a defined way for one program to ask another for something."),
  c('a3', "Most web A P Is use H T T P requests, and return data, often as JSON.", "Most web A P Is use H T T P requests, and return data, often as jay son."),
  c('a4', "For example, a request to get the cart, and the reply."), c('a5', "A good A P I is a contract: both sides agree on the requests and the responses.", "A good A P I is a contract: both sides agree on the requests and the responses."),
  c('a6', "If the contract changes carelessly, the frontend breaks."),
 ]),
 ('database', [
  c('d1', "A database stores data that must last."), c('d2', "Servers can restart, but orders and accounts must remain."),
  c('d3', "In CloudCart: products, customers, carts, and orders."), c('d4', "A relational database keeps data in tables, such as PostgreSQL.", "A relational database keeps data in tables, such as post gress Q L."),
  c('d5', "The backend reads and writes the database. The frontend should never touch it directly."), c('d6', "Data needs backups, because losing it is the costliest failure."),
 ]),
 ('trace', [
  c('t1', "Now trace one click."), c('t2', "The customer taps Add to cart in the frontend."), c('t3', "The frontend sends an A P I request to the backend.", "The frontend sends an A P I request to the backend."),
  c('t4', "The backend checks stock and price, then writes to the database."), c('t5', "The database confirms, the backend replies, and the frontend updates the cart."),
  c('t6', "Four parts, one click, well under a second."),
 ]),
 ('source', [
  c('s1', "Now the second group: how code reaches the shop."), c('s2', "Source control stores every version of the code, and who changed it."),
  c('s3', "Git is the standard tool, and GitHub and GitLab host the code online."), c('s4', "It lets teams work in parallel, review changes, and go back if something breaks."),
  c('s5', "It is the single source of truth for the code."),
 ]),
 ('build', [
  c('u1', "A build turns source code into something that can run."), c('u2', "It compiles code, downloads dependencies, and runs automated tests."),
  c('u3', "The result is called an artifact, such as a package or a container image."), c('u4', "A build should be repeatable: the same code gives the same result."),
  c('u5', "Tools include Maven, for Java, and Docker, for container images."),
 ]),
 ('release', [
  c('r1', "A release is a specific, versioned build, approved to go live."), c('r2', "For example, CloudCart version one point four point two.", "For example, CloudCart version one point four point two."),
  c('r3', "Deployment is the act of putting that version onto a running environment."), c('r4', "A deployment can go to a test environment, or to production, which a later lesson covers."),
  c('r5', "Release and deployment are related, but teams use the words a little differently."), c('r6', "So always ask what a team means."),
 ]),
 ('ops', [
  c('o1', "Operations keeps the running system healthy."), c('o2', "It watches performance, errors, and availability."),
  c('o3', "It responds when something fails, and applies updates and fixes."), c('o4', "Monitoring shows problems, often before customers report them."),
  c('o5', "In DevOps, developers and operations share this responsibility."),
 ]),
 ('map', [
  c('m1', "Here is every part, mapped to CloudCart."), c('m2', "Frontend: the product and cart pages."), c('m3', "Backend: the stock, price, and order rules."),
  c('m4', "A P I: the requests between them.", "A P I: the requests between them."), c('m5', "Database: the products and the orders."), c('m6', "Source control: the code, in Git."),
  c('m7', "Build: package the code into an image."), c('m8', "Release: version one point four point two.", "Release: version one point four point two."),
  c('m9', "Deployment: put it on the servers."), c('m10', "Operations: watch it, and keep it healthy."),
 ]),
 ('myths', [
  c('my1', "Watch out for four common myths."), c('my2', "Myth one: the database is the backend. In fact, the backend is code, and the database stores data."),
  c('my3', "Myth two: an A P I is only for outside developers. Your own frontend uses one too.", "Myth two: an A P I is only for outside developers. Your own frontend uses one too."),
  c('my4', "Myth three: release and deployment are always the same thing. They are related, but not identical."), c('my5', "Myth four: operations begins after the project ends. It begins when the first version runs."),
  c('my6', "Knowing the right words prevents expensive misunderstandings."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "What is the difference between frontend and backend?"), c('z3', "What does an A P I do?", "What does an A P I do?"),
  c('z4', "Name the five delivery parts, in order."), c('z8', "What is the difference between a release and a deployment?"),
  c('z9', "Objective covered: MC01-O04.", "Objective covered: number four, in the S D L C masterclass."),
  c('z5', "Pause the video, and answer out loud."), c('z6', "Next lesson: who does what."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h6': 0.5, 'g5': 0.5, 'f6': 0.5, 'b7': 0.5, 'a6': 0.5, 'd6': 0.5, 't6': 0.5, 's5': 0.5, 'u5': 0.5, 'r6': 0.5, 'o5': 0.5, 'm10': 0.5, 'my6': 0.5, 'z5': 6.0}
CHAP = {'groups': 'Two groups of parts', 'frontend': 'Frontend', 'backend': 'Backend', 'api': 'API', 'database': 'Database', 'trace': 'One click, traced', 'source': 'Source control',
        'build': 'Build', 'release': 'Release and deployment', 'ops': 'Operations', 'map': 'CloudCart map', 'myths': 'Common myths', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Parts  ·  Lesson 4', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)

def s_hook(C, D, dur):
    E = [El(T('One tap. Many parts.', 'x', 64), 100, 130, C['h1']), ill(C['h1'], 1400, 130)]
    E.append(Pop(card(540, 260, ACC, 'Add to cart', [('The customer taps one button in CloudCart.', TXT)], 44, 34), 100, 320, C['h1']))
    for i, n in enumerate(['Frontend', 'Backend', 'A P I'.replace(' ', ''), 'Database']):
        E.append(Pop(badge(n, F('x', 40), INK, [ACC, VIO, GOOD, WARN][i], padx=26, pady=14, r=26), 760 + (i % 2) * 380, 330 + (i // 2) * 100, C['h2'] + i * 0.35))
    E.append(Pop(badge('Run the shop', F('b', 34), INK, GOOD, padx=24, pady=12, r=22), 760, 560, C['h3']))
    E.append(Pop(badge('Deliver the code', F('b', 34), INK, VIO, padx=24, pady=12, r=22), 1140, 560, C['h4']))
    E.append(Pop(badge('Nine parts in total', F('x', 54), INK, WARN, padx=34, pady=16, r=30), 100, 760, C['h5']))
    E.append(takeaway('Learn what each part is, and does.', 920, C['h6'], GOOD, 1500))
    return E
def s_groups(C, D, dur):
    E = head('Two groups of parts', 'Run the shop, and deliver the code.', C['g1'])
    E.append(Pop(card(840, 470, ACC, 'Runs when customers use the shop', [], 40), 100, 340, C['g2']))
    for i, n in enumerate(['Frontend', 'Backend', 'API', 'Database']): E.append(Pop(badge(n, F('x', 40), INK, [ACC, VIO, GOOD, WARN][i], padx=30, pady=14, r=26), 140, 430 + i * 82, C['g2'] + 0.8 + i * 0.5))
    E.append(Pop(card(840, 470, VIO, 'Carries code to the shop', [], 40), 980, 340, C['g3']))
    for i, n in enumerate(['Source control', 'Build', 'Release', 'Deployment', 'Operations']): E.append(Pop(badge(n, F('x', 36), INK, [ACC, VIO, GOOD, WARN, PINK][i], padx=28, pady=10, r=24), 1020, 420 + i * 70, C['g3'] + 0.8 + i * 0.5))
    E.append(takeaway('DevOps lives mostly on the right, so know the left.', 900, C['g4'], WARN, 1600))
    return E
def s_frontend(C, D, dur):
    E = head('Frontend', 'What the user sees and touches.', C['f1'])
    E.append(Pop(card(840, 400, ACC, 'CloudCart in the browser', [], 40), 100, 340, C['f2']))
    for i, n in enumerate(['Product pages', 'The cart', 'Checkout form']): E.append(Pop(card(760, 92, ACC, '', [(n, TXT)], 4, 34), 140, 420 + i * 108, C['f3'] + i * 0.7))
    for i, n in enumerate(['HTML', 'CSS', 'JavaScript']): E.append(Pop(badge(n, F('x', 40), INK, [WARN, VIO, GOOD][i], padx=28, pady=14, r=26), 1040 + i * 250 - (40 if i == 2 else 0), 380, C['f4'] + i * 0.5))
    E.append(Pop(card(780, 220, WARN, 'Remember', [('Users can inspect the frontend, so it must never hide secrets.', TXT)], 38, 32), 1040, 500, C['f6']))
    E.append(takeaway('Shows information, and sends actions onward.', 800, C['f5'], GOOD, 1500))
    return E
def s_backend(C, D, dur):
    E = head('Backend', 'Code on a server that applies the rules.', C['b1'])
    rules = [('In stock?', 'Checks the item can be sold', GOOD, 'b3'), ('Right price?', 'Applies the price and discounts', ACC, 'b3'), ('Allowed?', 'Decides who may do what', VIO, 'b4')]
    for i, (n, t_, col, cid) in enumerate(rules): E.append(Pop(card(540, 170, col, n, [(t_, TXT)], 40, 30), 100 + i * 590, 340, C[cid] + (0.8 if i == 1 else 0)))
    E.append(El(T('It also talks to', 'b', 32, MUTED), 100, 560, C['b5'], anim='fade'))
    for i, n in enumerate(['The database', 'Other services']): E.append(Pop(badge(n, F('x', 38), INK, [WARN, PINK][i], padx=28, pady=14, r=26), 100 + i * 360, 610, C['b5'] + 0.3 + i * 0.6))
    E.append(El(T('Written in', 'b', 32, MUTED), 100, 730, C['b6'], anim='fade'))
    for i, (nm, lb) in enumerate([('java', 'Java'), ('python', 'Python')]): E.append(logo(nm, 340 + i * 190, 700, C['b6'] + 0.3 + i * 0.4, 90, lb))
    E.append(takeaway('Users never see it, but every action depends on it.', 930, C['b7'], WARN, 1600))
    return E
def s_api(C, D, dur):
    E = head('API', 'A defined way for programs to ask each other.', C['a1'])
    E.append(ill(C['a4'], 1400, 130))
    E.append(Pop(card(540, 120, ACC, 'Frontend', [], 40), 100, 340, C['a1']))
    E.append(Pop(card(540, 120, VIO, 'Backend', [], 40), 1280, 340, C['a1'] + 0.4))
    E.append(A([(660, 380), (1260, 380)], C['a3'], WARN, 6, 24)); E.append(A([(1260, 430), (660, 430)], C['a4'] + 1.2, GOOD, 6, 24))
    E.append(Pop(card(840, 150, WARN, 'Request', [('GET  /api/cart', TXT)], 36, 38), 100, 520, C['a4']))
    E.append(Pop(card(840, 190, GOOD, 'Response  ·  JSON data', [('{ "items": 2, "total": 59.98 }', TXT)], 36, 34), 980, 520, C['a4'] + 1.2))
    E.append(Pop(card(1720, 130, ACC, 'The contract', [('Both sides agree on the requests and the responses.', TXT)], 38, 32), 100, 760, C['a5']))
    E.append(takeaway('Change it carelessly, and the frontend breaks.', 930, C['a6'], WARN, 1500))
    return E
def s_database(C, D, dur):
    E = head('Database', 'Stores the data that must last.', C['d1'])
    items = [('Products', GOOD), ('Customers', ACC), ('Carts', VIO), ('Orders', WARN)]
    for i, (n, col) in enumerate(items): E.append(Pop(card(400, 130, col, n, [], 42), 100 + i * 430, 340, C['d3'] + i * 0.5))
    E.append(Pop(card(840, 200, WARN, 'Servers restart. Data stays.', [('Orders and accounts must survive.', TXT)], 40, 32), 100, 540, C['d2']))
    E.append(logo('postgresql', 1100, 540, C['d4'], 120, 'PostgreSQL'))
    E.append(Pop(card(840, 170, VIO, 'Who touches it?', [('The backend reads and writes. The frontend never does.', TXT)], 38, 30), 100, 780, C['d5']))
    E.append(Pop(badge('Back it up', F('b', 36), INK, BAD, padx=26, pady=14, r=24), 1100, 800, C['d6']))
    return E
def s_trace(C, D, dur):
    E = head('One click, traced', 'Add to cart, from the button to the data.', C['t1'])
    E.append(ill(C['t1'], 1400, 130))
    names = [('Frontend', 'Add to cart', ACC), ('Backend', 'Check stock and price', VIO), ('Database', 'Save the cart row', WARN)]
    xs = [100, 740, 1380]
    for i, (n, s, col) in enumerate(names): E.append(Pop(card(440, 220, col, n, [(s, TXT)], 44, 30), xs[i], 400, C['t2'] + (0 if i == 0 else (C['t4'] - C['t2'] if i == 2 else C['t3'] - C['t2']))))
    E.append(A([(560, 470), (720, 470)], C['t3'] + 0.2, ACC, 6, 24)); E.append(El(T('API request', 'b', 26, ACC), 566, 425, C['t3'] + 0.2, anim='fade'))
    E.append(A([(1180, 470), (1360, 470)], C['t4'] + 0.2, VIO, 6, 24))
    E.append(A([(1360, 560), (1180, 560)], C['t5'], GOOD, 6, 24)); E.append(A([(720, 560), (540, 560)], C['t5'] + 0.8, GOOD, 6, 24))
    E.append(Pop(badge('Cart updated on screen', F('b', 36), INK, GOOD, padx=26, pady=14, r=24), 100, 700, C['t5'] + 1.4))
    E.append(takeaway('Four parts, one click, well under a second.', 900, C['t6'], WARN, 1500))
    return E
def s_source(C, D, dur):
    E = head('Source control', 'Every version of the code, and who changed it.', C['s1'])
    for i, (nm, lb) in enumerate([('git', 'Git'), ('github', 'GitHub'), ('gitlab', 'GitLab')]): E.append(logo(nm, 100 + i * 300, 340, C['s3'] + i * 0.5, 120, lb))
    ben = [('Work in parallel', 'Many people, one codebase', ACC), ('Review changes', 'Check before it merges', VIO), ('Go back', 'Restore a working version', GOOD)]
    for i, (n, t_, col) in enumerate(ben): E.append(Pop(card(540, 170, col, n, [(t_, TXT)], 40, 30), 100 + i * 590, 600, C['s4'] + i * 0.8))
    E.append(takeaway('The single source of truth for the code.', 860, C['s5'], GOOD, 1500))
    return E
def s_build(C, D, dur):
    E = head('Build', 'Turn source code into something that runs.', C['u1'])
    steps = ['Compile', 'Get dependencies', 'Run tests']
    for i, n in enumerate(steps): E.append(Pop(badge(n, F('x', 38), INK, [ACC, VIO, GOOD][i], padx=28, pady=14, r=26), 100 + i * 480, 340, C['u2'] + i * 0.7))
    E.append(Pop(card(840, 150, WARN, 'Artifact', [('A package or a container image, ready to deploy.', TXT)], 42, 32), 100, 480, C['u3']))
    E.append(Pop(card(840, 150, ACC, 'Repeatable', [('The same code gives the same result.', TXT)], 42, 32), 980, 480, C['u4']))
    for i, (nm, lb) in enumerate([('maven', 'Maven'), ('docker', 'Docker')]): E.append(logo(nm, 100 + i * 300, 700, C['u5'] + i * 0.5, 120, lb))
    E.append(takeaway('The artifact is what moves to the next stage.', 920, C['u5'] + 1.6, GOOD, 1500))
    return E
def s_release(C, D, dur):
    E = head('Release and deployment', 'A version approved, then put in place.', C['r1'])
    E.append(Pop(card(840, 220, VIO, 'Release', [('A versioned build, approved to go live.', TXT), ('Example: CloudCart 1.4.2', MUTED)], 44, 32), 100, 340, C['r1']))
    E.append(Pop(card(840, 220, GOOD, 'Deployment', [('Putting that version onto a running environment.', TXT)], 44, 32), 980, 340, C['r3']))
    E.append(A([(950, 450), (970, 450)], C['r3'], WARN, 5, 18)) if False else None
    for i, n in enumerate(['Test environment', 'Production']): E.append(Pop(badge(n, F('b', 34), INK, [ACC, WARN][i], padx=26, pady=12, r=22), 980 + i * 400, 600, C['r4'] + i * 0.6))
    E.append(Pop(card(1720, 130, WARN, 'Careful', [('Teams use these words a little differently, so ask what they mean.', TXT)], 40, 32), 100, 700, C['r5']))
    E.append(takeaway('Related, but not identical.', 900, C['r6'], WARN, 1500))
    return E
def s_ops(C, D, dur):
    E = head('Operations', 'Keep the running system healthy.', C['o1'])
    w = [('Watch', 'Performance, errors, availability', ACC, 'o2'), ('Respond', 'Fix failures, apply updates', VIO, 'o3'), ('Monitor', 'Find problems before customers do', GOOD, 'o4')]
    for i, (n, t_, col, cid) in enumerate(w): E.append(Pop(card(540, 170, col, n, [(t_, TXT)], 40, 30), 100 + i * 590, 340, C[cid]))
    for i, (nm, lb) in enumerate([('prometheus', 'Prometheus'), ('grafana', 'Grafana')]): E.append(logo(nm, 100 + i * 300, 600, C['o4'] + 0.5 + i * 0.5, 120, lb))
    E.append(pill('LATER IN THE BOOTCAMP', 760, 650, C['o4'] + 1.5, WARN, INK, 28, 18, 10))
    E.append(takeaway('In DevOps, developers and operations share it.', 880, C['o5'], WARN, 1500))
    return E
def s_map(C, D, dur):
    E = head('CloudCart map', 'All nine parts, in one view.', C['m1'])
    it = [('Frontend', 'Product and cart pages', ACC), ('Backend', 'Stock, price, order rules', VIO), ('API', 'Requests between them', GOOD),
          ('Database', 'Products and orders', WARN), ('Source control', 'The code, in Git', PINK), ('Build', 'Package into an image', ACC),
          ('Release', 'Version 1.4.2', VIO), ('Deployment', 'Put it on the servers', GOOD), ('Operations', 'Watch and keep healthy', WARN)]
    for i, (n, t_, col) in enumerate(it): E.append(Pop(card(540, 150, col, n, [(t_, TXT)], 38, 28), 100 + (i % 3) * 590, 320 + (i // 3) * 180, C['m%d' % (i + 2)]))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Spot them early.', C['my1'])
    it = [('Myth: the database is the backend', 'Reality: the backend is code. The database stores data.', WARN, 'my2'), ('Myth: an API is only for outsiders', 'Reality: your own frontend uses one too.', VIO, 'my3'),
          ('Myth: release and deployment are the same', 'Reality: related, but not identical.', ACC, 'my4'), ('Myth: operations starts after the project', 'Reality: it begins when the first version runs.', GOOD, 'my5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 36, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('The right words prevent expensive misunderstandings.', 860, C['my6'], GOOD, 1600))
    return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    for i, (q, cid) in enumerate([('What is the difference between frontend and backend?', 'z2'), ('What does an API do?', 'z3'), ('Name the five delivery parts, in order.', 'z4'), ('Release versus deployment: what is the difference?', 'z8')]):
        E.append(Pop(card(1720, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 38, maxw=1500), 190, 268 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1720, 100, GOOD, '', [], 4), 100, 710, C['z9']))
    E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC01-O04  ·  The parts of an application', 'b', 32, TXT, maxw=1560), 220, 744, C['z9'] + 0.3, anim='wipe', d=1.6))
    E.append(Pop(badge('PAUSE  ·  answer out loud', F('b', 34), INK, PINK, padx=26, pady=14), 100, 860, C['z5']))
    E.append(El(T('Next: Who does what', 'x', 50, ACC), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 1500, 960, C['z7']))
    return E
FN = dict(hook=s_hook, groups=s_groups, frontend=s_frontend, backend=s_backend, api=s_api, database=s_database, trace=s_trace, source=s_source, build=s_build, release=s_release, ops=s_ops, map=s_map, myths=s_myths, recap=s_recap)
