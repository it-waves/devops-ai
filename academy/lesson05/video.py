import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 5  ·  DEVOPS BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "CloudCart wants a new feature: a wish list."), c('h2', "One feature, but six kinds of people will touch it."),
  c('h3', "Each one cares about something different."), c('h4', "Product asks: is this worth building?"), c('h5', "Developers ask: how do we build it?"),
  c('h6', "QA, security, operations, and DevOps each ask their own question."), c('h7', "Today you learn who does what, and why it matters."),
 ]),
 ('why', [
  c('w1', "Why do roles matter?"), c('w2', "Clear roles mean clear ownership."), c('w3', "Without them, important work is done twice, or not at all."),
  c('w4', "In a small team, one person may wear several hats."), c('w5', "But the responsibilities still exist, and someone must own each one."),
 ]),
 ('product', [
  c('p1', "Product decides what to build, and why."), c('p2', "They listen to customers, and set priorities."), c('p3', "They keep a backlog: an ordered list of work."),
  c('p4', "And they describe what done means, using requirements, like the ones from the requirements lesson."), c('p5', "Their question: is this worth building?"),
 ]),
 ('developer', [
  c('dv1', "Developers build the software."), c('dv2', "They write the code, and review each other's changes."), c('dv3', "They fix bugs, and write unit tests for their own code."),
  c('dv4', "In many teams, they also help run what they build."), c('dv5', "Their question: how do we build this well?"),
 ]),
 ('qa', [
  c('q1', "QA, or quality assurance, protects quality.", "Q A, or quality assurance, protects quality."), c('q2', "They plan tests, and run them, by hand and by automation."),
  c('q3', "They find defects before customers do."), c('q4', "Good QA also improves the process, so fewer defects appear."),
  c('q5', "Quality is a team responsibility, not only QA's job.", "Quality is a team responsibility, not only Q A's job."), c('q6', "Their question: does it really work, in every case?"),
 ]),
 ('security', [
  c('s1', "Security protects the system, and the data."), c('s2', "They assess risks, and set rules for access and secrets."),
  c('s3', "They scan code and dependencies for known weaknesses."), c('s4', "The modern goal is to build security in early, not add it at the end."),
  c('s5', "Security is also everyone's job."), c('s6', "Their question: what could go wrong, and who could abuse it?"),
 ]),
 ('operations', [
  c('o1', "Operations runs the live system."), c('o2', "They monitor health, respond to incidents, and manage capacity."),
  c('o3', "They keep backups, and apply updates."), c('o4', "They are often the first to know when something breaks."), c('o5', "Their question: is it healthy, and can it keep running?"),
 ]),
 ('devops', [
  c('v1', "DevOps connects all of this."), c('v2', "A DevOps engineer builds and improves the delivery path."), c('v3', "That means pipelines, automation, and environments."),
  c('v4', "They help developers ship safely, and operations run reliably."), c('v5', "DevOps is also a culture: shared goals, and shared responsibility."), c('v6', "Their question: how do we deliver faster, and safer?"),
 ]),
 ('wall', [
  c('l1', "Look at how many teams used to work."), c('l2', "Developers wrote code, then threw it over a wall to operations."), c('l3', "Developers wanted change. Operations wanted stability."),
  c('l4', "When something broke, each side blamed the other."), c('l5', "DevOps tears down the wall, with shared goals, and shared tools."), c('l6', "Everyone cares about both speed, and stability."),
 ]),
 ('matrix', [
  c('m1', "Here are the six roles, side by side."), c('m2', "Product: what, and why."), c('m3', "Developers: build."), c('m4', "QA: verify."), c('m5', "Security: protect."),
  c('m6', "Operations: run."), c('m7', "DevOps: connect, and automate."),
 ]),
 ('cloudcart', [
  c('c1', "Follow the wish list feature through the team."), c('c2', "Product writes the story: customers can save products to a wish list."),
  c('c3', "Developers build it, and add unit tests."), c('c4', "QA tests it, in every case."), c('c5', "Security checks that one customer cannot see another customer's list."),
  c('c6', "A DevOps pipeline builds and deploys it."), c('c7', "Operations monitors it, and watches for problems."), c('c8', "Every role touched one feature."),
 ]),
 ('choose', [
  c('k1', "Now try it: who owns each problem?"), c('k2', "What should we build next? Product."), c('k3', "Checkout is slow at two in the morning? Operations responds, with the developers."),
  c('k4', "A library has a known vulnerability? Security flags it, and developers upgrade it."), c('k5', "Deploying takes two hours of manual steps? DevOps automates it."),
  c('k6', "Does the discount code work in every case? QA tests it, and developers fix it."), c('k7', "Notice that many problems involve more than one role."),
 ]),
 ('myths', [
  c('y1', "Watch out for four common myths."), c('y2', "Myth one: a DevOps engineer is a renamed system administrator. In fact, the work centers on automation and collaboration."),
  c('y3', "Myth two: only QA owns quality. In fact, the whole team does."), c('y4', "Myth three: security slows teams down. Late security does. Early security saves time."),
  c('y5', "Myth four: developers never need to know operations. Knowing how code runs makes better code."), c('y6', "Roles differ, but the goal is shared."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "Which role decides what to build, and why?"), c('z3', "Who runs the live system?"),
  c('z4', "What problem did the wall between developers and operations cause?"), c('z8', "Name two things a DevOps engineer builds."),
  c('z9', "Objective covered: MC01-O05.", "Objective covered: number five, in the S D L C masterclass."),
  c('z5', "Pause the video, and answer out loud."), c('z6', "Next lesson: tracing one change."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h7': 0.5, 'w5': 0.5, 'p5': 0.5, 'dv5': 0.5, 'q6': 0.5, 's6': 0.5, 'o5': 0.5, 'v6': 0.5, 'l6': 0.5, 'm7': 0.5, 'c8': 0.5, 'k7': 0.5, 'y6': 0.5, 'z5': 6.0}
CHAP = {'why': 'Why roles matter', 'product': 'Product', 'developer': 'Developers', 'qa': 'QA', 'security': 'Security', 'operations': 'Operations', 'devops': 'DevOps',
        'wall': 'The wall', 'matrix': 'Side by side', 'cloudcart': 'CloudCart wish list', 'choose': 'Who owns it?', 'myths': 'Common myths', 'recap': 'Quick check'}
ROLE = {'Product': WARN, 'Developers': ACC, 'QA': GOOD, 'Security': BAD, 'Operations': VIO, 'DevOps': PINK}
def head(title, sub, t): return [El(T('Roles  ·  Lesson 5', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def role(E, name, sub, items, q, col, C, ids, qid, tk=None, tkid=None):
    E += head(name, sub, C[ids[0]])
    for i, (n, t_) in enumerate(items): E.append(Pop(card(540, 250, col, n, [(t_, TXT)], 44, 34), 100 + i * 590, 340, C[ids[i + 1]]))
    E.append(Pop(card(1720, 200, col, 'Their question', [(q, TXT)], 44, 44), 100, 650, C[qid]))
    if tk: E.append(takeaway(tk, 820, C[tkid], GOOD, 1500))
    return E

def s_hook(C, D, dur):
    E = [El(T('One feature. Six roles.', 'x', 64), 100, 130, C['h1']), ill(C['h1'], 1400, 130)]
    E.append(Pop(card(540, 260, ACC, 'Wish list', [('A new CloudCart feature: customers save products for later.', TXT)], 44, 32), 100, 320, C['h1']))
    for i, n in enumerate(['Product', 'Developers', 'QA', 'Security', 'Operations', 'DevOps']):
        E.append(Pop(badge(n, F('x', 38), INK, ROLE[n], padx=26, pady=14, r=26), 760 + (i % 3) * 330, 340 + (i // 3) * 100, C['h2'] + i * 0.4))
    E.append(Pop(card(1720, 100, WARN, 'Product asks', [], 40), 100, 600, C['h4']))
    E.append(El(T('Is this worth building?', 'm', 38), 640, 622, C['h4'] + 0.2, anim='fade'))
    E.append(Pop(card(1720, 100, ACC, 'Developers ask', [], 40), 100, 720, C['h5']))
    E.append(El(T('How do we build it?', 'm', 38), 640, 742, C['h5'] + 0.2, anim='fade'))
    E.append(takeaway('Same feature, different questions.', 880, C['h7'], GOOD, 1500))
    return E
def s_why(C, D, dur):
    E = head('Why roles matter', 'Clear ownership, clear work.', C['w1'])
    it = [('Clear ownership', 'Everyone knows who decides', ACC, 'w2'), ('No gaps, no repeats', 'Work is not done twice, or missed', GOOD, 'w3'), ('Many hats', 'Small teams share roles', VIO, 'w4')]
    for i, (n, t_, col, cid) in enumerate(it): E.append(Pop(card(540, 320, col, n, [(t_, TXT)], 46, 36), 100 + i * 590, 340, C[cid]))
    E.append(takeaway('The responsibilities exist, even when one person covers many.', 740, C['w5'], WARN, 1600))
    return E
def s_product(C, D, dur):
    return role([], 'Product', 'Decides what to build, and why.', [('Customers', 'Listens, and sets priorities'), ('Backlog', 'An ordered list of work'), ('Done means', 'Defines it, from requirements')], 'Is this worth building?', WARN, C, ['p1', 'p2', 'p3', 'p4'], 'p5')
def s_developer(C, D, dur):
    return role([], 'Developers', 'Build the software.', [('Write code', 'And review each other\'s changes'), ('Fix bugs', 'And write unit tests'), ('Help run it', 'In many teams, they support what they build')], 'How do we build this well?', ACC, C, ['dv1', 'dv2', 'dv3', 'dv4'], 'dv5')
def s_qa(C, D, dur):
    E = head('QA', 'Quality assurance protects quality.', C['q1'])
    it = [('Plan and run tests', 'By hand, and by automation', 'q2'), ('Find defects', 'Before customers do', 'q3'), ('Improve the process', 'So fewer defects appear', 'q4')]
    for i, (n, t_, cid) in enumerate(it): E.append(Pop(card(540, 250, GOOD, n, [(t_, TXT)], 44, 34), 100 + i * 590, 340, C[cid]))
    E.append(Pop(card(1720, 200, GOOD, 'Their question', [('Does it really work, in every case?', TXT)], 44, 44), 100, 650, C['q6']))
    E.append(Pop(badge('Quality is a team responsibility', F('b', 36), INK, WARN, padx=30, pady=16, r=26), 100, 920, C['q5']))
    return E
def s_security(C, D, dur):
    E = head('Security', 'Protects the system, and the data.', C['s1'])
    it = [('Assess risks', 'Set rules for access and secrets', 's2'), ('Scan', 'Code and dependencies for known weaknesses', 's3'), ('Build in early', 'Not added at the end', 's4')]
    for i, (n, t_, cid) in enumerate(it): E.append(Pop(card(540, 250, BAD, n, [(t_, TXT)], 44, 34), 100 + i * 590, 340, C[cid]))
    E.append(Pop(card(1720, 200, BAD, 'Their question', [('What could go wrong, and who could abuse it?', TXT)], 44, 44), 100, 650, C['s6']))
    E.append(Pop(badge('Security is everyone\'s job too', F('b', 36), INK, WARN, padx=30, pady=16, r=26), 100, 920, C['s5']))
    return E
def s_operations(C, D, dur):
    return role([], 'Operations', 'Runs the live system.', [('Monitor', 'Health, incidents, capacity'), ('Protect data', 'Backups, and updates'), ('First to know', 'When something breaks')], 'Is it healthy, and can it keep running?', VIO, C, ['o1', 'o2', 'o3', 'o4'], 'o5')
def s_devops(C, D, dur):
    E = head('DevOps', 'Connects building and running.', C['v1'])
    for i, (n, t_, cid) in enumerate([('Pipelines', 'Build, test, and deploy', 'v2'), ('Automation', 'Fewer manual steps', 'v3'), ('Environments', 'Places to test, and to run', 'v3')]):
        E.append(Pop(card(540, 220, PINK, n, [(t_, TXT)], 44, 34), 100 + i * 590, 340, C[cid] + (0.8 * i if cid == 'v3' else 0)))
    E.append(Pop(card(840, 200, PINK, 'A culture too', [('Shared goals, shared responsibility.', TXT)], 44, 36), 100, 620, C['v5']))
    E.append(Pop(card(840, 200, PINK, 'Their question', [('How do we deliver faster, and safer?', TXT)], 44, 36), 980, 620, C['v6']))
    E.append(takeaway('They help developers ship safely, and operations run reliably.', 900, C['v4'], WARN, 1650))
    return E
def s_wall(C, D, dur):
    E = head('The wall', 'How many teams used to work.', C['l1'])
    E.append(ill(C['l1'], 1400, 130))
    E.append(Pop(card(540, 200, ACC, 'Developers', [('Want change', TXT)], 44, 34), 100, 440, C['l1'] + 0.5))
    E.append(Pop(card(540, 200, VIO, 'Operations', [('Want stability', TXT)], 44, 34), 1280, 440, C['l1'] + 1.0))
    E.append(Pop(card(300, 250, BAD, 'WALL', [], 44), 810, 380, C['l2']))
    E.append(A([(370, 420), (370, 350), (1550, 350), (1550, 420)], C['l2'] + 0.8, WARN, 6, 24)); E.append(El(T('code thrown over', 'b', 28, WARN), 780, 300, C['l2'] + 0.8, anim='fade'))
    E.append(Pop(badge('Blame', F('x', 40), INK, BAD, padx=30, pady=14, r=26), 865, 660, C['l4']))
    E.append(Pop(card(1720, 130, GOOD, 'DevOps', [('Shared goals, and shared tools.', TXT)], 38, 34), 100, 770, C['l5']))
    E.append(takeaway('Everyone cares about both speed, and stability.', 950, C['l6'], GOOD, 1500))
    return E
def s_matrix(C, D, dur):
    E = head('Side by side', 'Six roles, six questions.', C['m1'])
    it = [('Product', 'What, and why', 'Is this worth building?', 'm2'), ('Developers', 'Build', 'How do we build it well?', 'm3'), ('QA', 'Verify', 'Does it work in every case?', 'm4'),
          ('Security', 'Protect', 'What could go wrong?', 'm5'), ('Operations', 'Run', 'Is it healthy?', 'm6'), ('DevOps', 'Connect, and automate', 'How do we deliver faster, and safer?', 'm7')]
    for i, (n, a, b, cid) in enumerate(it): E.append(Pop(card(540, 270, ROLE[n], n, [(a, TXT), (b, MUTED)], 42, 32), 100 + (i % 3) * 590, 340 + (i // 3) * 285, C[cid]))
    E.append(takeaway('Different jobs, one shared goal.', 920, C['m7'] + 0.8, GOOD, 1500))
    return E
def s_cloudcart(C, D, dur):
    E = head('CloudCart wish list', 'One feature, through every role.', C['c1'])
    E.append(ill(C['c1'], 1400, 130))
    it = [('1  Product', 'Writes the story', 'Product', 'c2'), ('2  Developers', 'Build it, add unit tests', 'Developers', 'c3'), ('3  QA', 'Tests every case', 'QA', 'c4'),
          ('4  Security', 'Checks lists stay private', 'Security', 'c5'), ('5  DevOps', 'Pipeline builds and deploys', 'DevOps', 'c6'), ('6  Operations', 'Monitors, and watches', 'Operations', 'c7')]
    for i, (n, t_, r, cid) in enumerate(it): E.append(Pop(card(540, 190, ROLE[r], n, [(t_, TXT)], 40, 30), 100 + (i % 3) * 590, 340 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Every role touched one feature.', 840, C['c8'], WARN, 1500))
    return E
def s_choose(C, D, dur):
    E = head('Who owns it?', 'Match each problem to a role.', C['k1'])
    E.append(ill(C['k1'], 1400, 130))
    rows = [('What should we build next?', 'Product', 'k2'), ('Checkout is slow at 2 a.m.', 'Operations + developers', 'k3'), ('A library has a known vulnerability', 'Security + developers', 'k4'),
            ('Deploying takes two hours by hand', 'DevOps', 'k5'), ('Does the discount code always work?', 'QA + developers', 'k6')]
    for i, (s, f, cid) in enumerate(rows):
        r = f.split(' +')[0]; col = ROLE[r]; y = 330 + i * 112
        E.append(Pop(card(1000, 90, col, '', [(s, TXT)], 4, 34), 100, y, C[cid]))
        E.append(Pop(badge(f, F('b', 36), INK, col, padx=26, pady=12, r=24), 1140, y + 12, C[cid] + 1.0))
    E.append(takeaway('Many problems involve more than one role.', 920, C['k7'], WARN, 1500))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Spot them early.', C['y1'])
    it = [('Myth: DevOps is a renamed sysadmin', 'Reality: automation and collaboration.', PINK, 'y2'), ('Myth: only QA owns quality', 'Reality: the whole team does.', GOOD, 'y3'),
          ('Myth: security slows teams down', 'Reality: late security does. Early saves time.', BAD, 'y4'), ('Myth: developers skip operations', 'Reality: knowing how code runs helps.', ACC, 'y5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 36, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Roles differ, but the goal is shared.', 860, C['y6'], GOOD, 1500))
    return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    for i, (q, cid) in enumerate([('Which role decides what to build, and why?', 'z2'), ('Who runs the live system?', 'z3'), ('What did the wall between developers and operations cause?', 'z4'), ('Name two things a DevOps engineer builds.', 'z8')]):
        E.append(Pop(card(1720, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 38, maxw=1500), 190, 268 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1720, 100, GOOD, '', [], 4), 100, 710, C['z9']))
    E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC01-O05  ·  Who does what', 'b', 32, TXT, maxw=1560), 220, 744, C['z9'] + 0.3, anim='wipe', d=1.6))
    E.append(Pop(badge('PAUSE  ·  answer out loud', F('b', 34), INK, PINK, padx=26, pady=14), 100, 860, C['z5']))
    E.append(El(T('Next: Tracing one change', 'x', 50, ACC), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 1500, 960, C['z7']))
    return E
FN = dict(hook=s_hook, why=s_why, product=s_product, developer=s_developer, qa=s_qa, security=s_security, operations=s_operations, devops=s_devops, wall=s_wall, matrix=s_matrix, cloudcart=s_cloudcart, choose=s_choose, myths=s_myths, recap=s_recap)
