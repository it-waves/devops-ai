import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 7  ·  DEVOPS BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
V143 = "version one point four point three"
SCENES = [
 ('hook', [
  c('h1', "CloudCart has a new version, ready to ship.", "CloudCart has a new version, ready to ship."),
  c('h2', "Would you send it straight to every customer?"),
  c('h3', "Of course not. It travels through safe stages first."),
  c('h4', "Today you learn those stages, who approves each move, and how to undo a mistake."),
  c('h5', "That is environments, approvals, release risk, rollback, and maintenance."),
 ]),
 ('envs', [
  c('n1', "First, what is an environment?"),
  c('n2', "An environment is a separate place where the application runs."),
  c('n3', "Each one has its own servers."), c('n4', "Its own data."), c('n5', "Its own settings."), c('n6', "And its own list of who may access it."),
  c('n7', "Separation means a mistake in one place cannot hurt another."),
 ]),
 ('dev', [
  c('d1', "The first environment is development."),
  c('d2', "Developers run and try the code here, often on their own machines."),
  c('d3', "Breaking things is normal, and nobody is harmed."), c('d4', "The data is fake, or a small sample."),
  c('d5', "Development answers one question: does my change work at all?"),
 ]),
 ('test', [
  c('t1', "Next comes the test environment, often called staging."),
  c('t2', "It is built to look as much like production as possible."),
  c('t3', "Automated tests and Q A check the release here.", "Automated tests and Q A check the release here."),
  c('t4', "The data is test data, never real customer data."),
  c('t5', "Test answers a different question: will it work when it is live?"),
 ]),
 ('prod', [
  c('p1', "Then there is production."), c('p2', "Production is the live shop, with real customers, real orders, and real money."),
  c('p3', "Access is limited to a few trusted people."), c('p4', "Every change here is approved, recorded, and watched."),
  c('p5', "A mistake here costs customers, and trust."),
 ]),
 ('same', [
  c('s1', "Here is a rule that prevents many surprises."), c('s2', "Build once, then move the same build through every environment."),
  c('s3', "If you rebuild for each stage, you are no longer testing what you ship."), c('s4', "What changes between environments is the settings, such as the database address."),
  c('s5', "Secrets, like passwords, are supplied to each environment, never written into the code."),
 ]),
 ('approvals', [
  c('a1', "Now, approvals."), c('a2', "An approval is a recorded decision that a change may move forward."),
  c('a3', "Code review comes first: a teammate approves the change."), c('a4', "Q A signs off that it behaves as the acceptance criteria say.", "Q A signs off that it behaves as the acceptance criteria say."),
  c('a5', "Risky changes also get a security check."), c('a6', "Production needs a final release approval, from product or a release owner."),
  c('a7', "Some gates are automatic, like tests. Others need human judgment."), c('a8', "The amount of approval should match the amount of risk."),
 ]),
 ('risk', [
  c('k1', "Release risk is the chance a release causes harm, times how much harm."), c('k2', "Ask four questions before you ship."),
  c('k3', "How big is the change?"), c('k4', "Who is affected if it fails?"), c('k5', "Can we undo it quickly?"), c('k6', "How well was it tested?"),
  c('k7', "Fixing a typo is low risk. Changing how payments work is high risk."), c('k8', "Higher risk means more checks, more care, and a better plan."),
 ]),
 ('reduce', [
  c('u1', "Good teams do not just fear risk. They shrink it."), c('u2', "Small changes are easier to understand, and easier to undo."),
  c('u3', "Automated tests catch known problems before customers do."), c('u4', "A gradual rollout starts with a few customers, then grows if all looks healthy."),
  c('u5', "Choose quiet times, when the team is present and traffic is low."), c('u6', "Each of these makes a failure smaller, and recovery faster."),
 ]),
 ('rollback', [
  c('r1', "Even so, things go wrong. That is why rollback exists."), c('r2', "A rollback returns production to the last known good version."),
  c('r3', "Here, version one point four point three misbehaves, so we return to one point four point two.", "Here, version one point four point three misbehaves, so we return to one point four point two."),
  c('r4', "Rollback only works if you prepared for it."), c('r5', "Keep the previous version available."), c('r6', "Make deployment repeatable, so going back is as easy as going forward."),
  c('r7', "And be careful with data: some database changes cannot simply be reversed."), c('r8', "Rollback is a plan you prepare, not a hope."),
 ]),
 ('story', [
  c('y1', "Let us walk through a rollback, step by step."), c('y2', "At ten o'clock, the team deploys the new version.", "At ten o'clock, the team deploys the new version."),
  c('y3', "Six minutes later, monitoring shows errors rising."), c('y4', "The agreed rule says: if errors stay high, roll back."),
  c('y5', "At ten fourteen, the old version is serving customers again.", "At ten fourteen, the old version is serving customers again."), c('y6', "Only now does the team investigate, in a test environment, without pressure."),
  c('y7', "Sometimes a fast fix is safer than a rollback. The team decides using the risk."), c('y8', "Notice the deployment record: it says exactly what happened, and when."),
 ]),
 ('maint', [
  c('m1', "A release is not the end. Software needs care for as long as it runs."), c('m2', "That care is called maintenance."),
  c('m3', "Corrective maintenance fixes bugs that customers find."), c('m4', "Adaptive maintenance keeps up with change, such as new browsers or new rules."),
  c('m5', "Perfective maintenance improves speed, and usability."), c('m6', "Preventive maintenance tidies code, and applies security patches before they are needed."),
  c('m7', "Ignored maintenance turns into technical debt, which slows every future change."), c('m8', "Planned maintenance is cheaper than emergency repair."),
 ]),
 ('myths', [
  c('w1', "Watch out for four common myths."), c('w2', "Myth one: if it passed in test, it is safe. In fact, test lowers risk, but differences remain."),
  c('w3', "Myth two: you can always roll back. In fact, data changes can make that hard."), c('w4', "Myth three: approvals only slow us down. In fact, the right ones prevent expensive mistakes."),
  c('w5', "Myth four: maintenance is leftover work. In fact, it is where software spends most of its life."), c('w6', "Plan for all four."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "Name the three environments, and what each is for."), c('z3', "Why build once, and move the same build?"),
  c('z4', "What four questions measure release risk?"), c('z8', "What must be ready before a rollback can work?"),
  c('z9', "Objective covered: MC01-O07.", "Objective covered: number seven, in the S D L C masterclass."),
  c('z5', "Pause the video, and plan the environments, approvals and rollback for a change of your own."), c('z6', "Next lesson: the CloudCart workflow."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h5': 0.5, 'n7': 0.5, 'd5': 0.5, 't5': 0.5, 'p5': 0.5, 's5': 0.5, 'a8': 0.5, 'k8': 0.5, 'u6': 0.5, 'r8': 0.5, 'y8': 0.5, 'm8': 0.5, 'w6': 0.5, 'z5': 10.0}
CHAP = {'envs': 'What is an environment', 'dev': 'Development', 'test': 'Test and staging', 'prod': 'Production', 'same': 'Build once', 'approvals': 'Approvals', 'risk': 'Release risk',
        'reduce': 'Reducing risk', 'rollback': 'Rollback', 'story': 'A rollback, step by step', 'maint': 'Maintenance', 'myths': 'Common myths', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Release  ·  Lesson 7', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
VIOC = VIO

def s_hook(C, D, dur):
    E = [El(T('Ready to ship?', 'x', 64), 100, 130, C['h1']), ill(C['h1'], 1400, 130)]
    E.append(Pop(card(1720, 120, WARN, 'CloudCart  ·  version 1.4.3', [], 46), 100, 260, C['h1']))
    names = [('Development', 'Try it', ACC), ('Test', 'Check it', GOOD), ('Production', 'Customers', WARN)]
    for i, (n, s, col) in enumerate(names):
        E.append(Pop(card(480, 220, col, n, [(s, TXT)], 46, 36), 100 + i * 620, 440, C['h3'] + i * 0.5))
        if i: E.append(A([(100 + i * 620 - 140, 550), (100 + i * 620 - 20, 550)], C['h3'] + i * 0.5, MUTED, 6, 24))
    bs = [badge(n, F('b', 36), INK, col, padx=28, pady=14, r=26) for n, col in [('Approvals', VIO), ('Rollback', BAD), ('Maintenance', PINK)]]
    gap = 60; bx = 100 + (1720 - (sum(b.width for b in bs) + gap * 2)) / 2
    E.append(El(T('Today, around that path', 'b', 32, MUTED), bx, 730, C['h4'], anim='fade'))
    for i, b in enumerate(bs):
        E.append(Pop(b, bx, 790, C['h4'] + 0.3 + i * 0.5 if i < 2 else C['h5'])); bx += b.width + gap
    E.append(takeaway('Safe delivery is a path, not a leap.', 920, C['h5'] + 0.4, GOOD, 1600))
    return E
def s_envs(C, D, dur):
    E = head('What is an environment?', 'A separate place where the application runs.', C['n1'])
    E.append(Pop(card(1720, 130, ACC, 'Definition', [('One copy of the application, with its own resources.', TXT)], 36, 38), 100, 330, C['n2']))
    it = [('Servers', 'Its own machines', ACC, 'n3', 'server'), ('Data', 'Its own database', GOOD, 'n4', 'db'), ('Settings', 'Its own configuration', WARN, 'n5', 'gear'), ('Access', 'Its own list of people', VIO, 'n6', 'people')]
    for i, (n, s, col, cid, g) in enumerate(it):
        E.append(Pop(card(400, 250, col, n, [(s, TXT)], 44, 30, True), 100 + i * 440, 520, C[cid]))
        E.append(Pop(glyph(g, 70, col, True), 100 + i * 440 + 165, 660, C[cid] + 0.2))
    E.append(takeaway('A mistake in one place cannot hurt another.', 860, C['n7'], GOOD, 1600))
    return E
def _env(title, sub, ids, items, art, tk, tkid, col, aid, logo_=None):
    E = head(title, sub, ids[0])
    return E
def s_dev(C, D, dur):
    E = head('Development', 'Where developers build and try.', C['d1'])
    it = [('Build and try', 'Often on a developer machine'), ('Breaking is fine', 'Nobody is harmed'), ('Fake data', 'Or a small sample')]
    ids = ['d2', 'd3', 'd4']
    for i, (n, s) in enumerate(it): E.append(Pop(card(540, 220, ACC, n, [(s, TXT)], 44, 34), 100 + i * 590, 360, C[ids[i]]))
    E.append(Pop(card(1720, 200, ACC, 'The question it answers', [('Does my change work at all?', TXT)], 44, 44), 100, 640, C['d5']))
    E.append(Pop(badge('Risk to customers: none', F('b', 36), INK, GOOD, padx=26, pady=14, r=24), 100, 880, C['d3'] + 0.5))
    return E
def s_test(C, D, dur):
    E = head('Test and staging', 'Where the release is proven.', C['t1'])
    it = [('Like production', 'Built to match the live shop'), ('Tests and Q A', 'Automated, then human'), ('Test data', 'Never real customer data')]
    ids = ['t2', 't3', 't4']
    for i, (n, s) in enumerate(it): E.append(Pop(card(540, 220, GOOD, n, [(s, TXT)], 44, 32), 100 + i * 590, 360, C[ids[i]]))
    E.append(Pop(card(1720, 200, GOOD, 'The question it answers', [('Will it work when it is live?', TXT)], 44, 44), 100, 640, C['t5']))
    E.append(Pop(badge('Risk to customers: very low', F('b', 36), INK, GOOD, padx=26, pady=14, r=24), 100, 880, C['t4'] + 0.5))
    return E
def s_prod(C, D, dur):
    E = head('Production', 'The live shop.', C['p1'])
    it = [('Real customers', 'Real orders, real money'), ('Limited access', 'A few trusted people'), ('Controlled', 'Approved, recorded, watched')]
    ids = ['p2', 'p3', 'p4']
    for i, (n, s) in enumerate(it): E.append(Pop(card(540, 220, WARN, n, [(s, TXT)], 44, 34), 100 + i * 590, 360, C[ids[i]]))
    E.append(Pop(card(1720, 200, BAD, 'What is at stake', [('Customers, revenue, and trust.', TXT)], 44, 44), 100, 640, C['p5']))
    E.append(Pop(badge('Risk to customers: real', F('b', 36), INK, BAD, padx=26, pady=14, r=24), 100, 880, C['p4'] + 0.5))
    return E
def s_same(C, D, dur):
    E = head('Build once', 'The same build, every environment.', C['s1'])
    E.append(ill(C['s2'], 1400, 130))
    stages = [('Build #318', ACC), ('Development', ACC), ('Test', GOOD), ('Production', WARN)]
    for i, (n, col) in enumerate(stages):
        x = 100 + i * 446
        E.append(Pop(card(380, 150, col, n, [], 42), x, 340, C['s2'] + i * 0.5))
        if i: E.append(A([(x - 58, 415), (x - 8, 415)], C['s2'] + i * 0.5, MUTED, 6, 22))
    E.append(Pop(card(840, 210, GOOD, 'Stays the same', [('The build you tested is the build you ship.', TXT)], 40, 32), 100, 560, C['s3']))
    E.append(Pop(card(840, 210, WARN, 'Changes per environment', [('Settings, like the database address.', TXT)], 40, 32), 980, 560, C['s4']))
    E.append(Pop(badge('Secrets are supplied, never written in code', F('b', 36), INK, BAD, padx=28, pady=14, r=26), 100, 830, C['s5']))
    return E
def s_approvals(C, D, dur):
    E = head('Approvals', 'A recorded decision to move forward.', C['a1'])
    E.append(Pop(card(1720, 100, VIO, '', [('Who decides, and where, depends on the risk.', TXT)], 4, 36), 100, 320, C['a2']))
    it = [('Code review', 'A teammate approves', ACC, 'a3'), ('Q A sign-off', 'Meets acceptance criteria', GOOD, 'a4'), ('Security check', 'For risky changes', BAD, 'a5'), ('Release approval', 'Product or release owner', WARN, 'a6')]
    for i, (n, s, col, cid) in enumerate(it):
        E.append(Pop(card(400, 220, col, n, [(s, TXT)], 40, 28), 100 + i * 440, 470, C[cid]))
        if i: E.append(A([(100 + i * 440 - 38, 580), (100 + i * 440 - 4, 580)], C[cid] - 0.1, MUTED, 5, 16))
    b1 = badge('Automatic gates: tests, scans', F('b', 34), INK, ACC, padx=26, pady=12, r=24); b2 = badge('Human gates: judgment', F('b', 34), INK, PINK, padx=26, pady=12, r=24)
    E.append(Pop(b1, 100, 740, C['a7'])); E.append(Pop(b2, 100 + b1.width + 40, 740, C['a7'] + 0.7))
    E.append(takeaway('The amount of approval should match the risk.', 900, C['a8'], GOOD, 1600))
    return E
def s_risk(C, D, dur):
    E = head('Release risk', 'Ask four questions before you ship.', C['k1'])
    it = [('How big is the change?', 'More code, more places to fail', ACC, 'k3'), ('Who is affected?', 'A few customers, or all of them', VIO, 'k4'),
          ('Can we undo it?', 'Quick to reverse, or not', WARN, 'k5'), ('How well is it tested?', 'Automated and manual checks', GOOD, 'k6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 170, col, n, [(s, TXT)], 40, 30), 100 + (i % 2) * 880, 330 + (i // 2) * 200, C[cid]))
    E.append(El(T('Low risk', 'b', 30, MUTED), 100, 750, C['k7'], anim='fade')); E.append(Pop(badge('Fix a typo', F('x', 40), INK, GOOD, padx=28, pady=14, r=26), 100, 800, C['k7'] + 0.2))
    E.append(El(T('High risk', 'b', 30, MUTED), 760, 750, C['k7'] + 1.2, anim='fade')); E.append(Pop(badge('Change how payments work', F('x', 40), INK, BAD, padx=28, pady=14, r=26), 760, 800, C['k7'] + 1.4))
    E.append(takeaway('More risk: more checks, more care, a better plan.', 940, C['k8'], WARN, 1600, 36))
    return E
def s_reduce(C, D, dur):
    E = head('Reducing risk', 'Make failures small, and recovery fast.', C['u1'])
    it = [('Small changes', 'Easier to understand and undo', ACC, 'u2'), ('Automated tests', 'Catch known problems early', GOOD, 'u3'),
          ('Gradual rollout', 'A few customers first', VIO, 'u4'), ('Quiet times', 'Team present, traffic low', WARN, 'u5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 170, col, n, [(s, TXT)], 40, 30), 100 + (i % 2) * 880, 330 + (i // 2) * 200, C[cid]))
    E.append(El(T('A gradual rollout', 'b', 30, MUTED), 100, 750, C['u4'] + 1.0, anim='fade'))
    bx = 100
    for i, (n, col) in enumerate([('5% of customers', GOOD), ('50%', ACC), ('100%', WARN)]):
        b = badge(n, F('x', 38), INK, col, padx=26, pady=14, r=26)
        if i: E.append(A([(bx + 8, 830), (bx + 62, 830)], C['u4'] + 1.2 + i * 0.7, MUTED, 5, 16)); bx += 70
        E.append(Pop(b, bx, 800, C['u4'] + 1.2 + i * 0.7)); bx += b.width + 16 if i < 2 else 0
    E.append(takeaway('Smaller failures are cheaper failures.', 940, C['u6'], GOOD, 1600, 36))
    return E
def s_rollback(C, D, dur):
    E = head('Rollback', 'Return to the last known good version.', C['r1'])
    E.append(ill(C['r3'], 1400, 130))
    E.append(Pop(card(640, 190, GOOD, 'v1.4.2', [('Last known good', TXT)], 52, 34), 100, 340, C['r3']))
    E.append(Pop(card(640, 190, BAD, 'v1.4.3', [('Misbehaving in production', TXT)], 52, 32), 1180, 340, C['r3'] - 0.2))
    E.append(A([(1160, 440), (770, 440)], C['r3'] + 0.6, WARN, 7, 28)); E.append(El(T('Roll back', 'b', 32, WARN), 880, 385, C['r3'] + 0.6, anim='fade'))
    it = [('Old version kept', 'Ready to run again', ACC, 'r5'), ('Repeatable deploys', 'Back is as easy as forward', VIO, 'r6'), ('Compatible data', 'Some database changes cannot be reversed', BAD, 'r7')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 220, col, n, [(s, TXT)], 40, 30), 100 + i * 590, 590, C[cid]))
    E.append(takeaway('A rollback is a plan you prepare, not a hope.', 880, C['r8'], GOOD, 1600))
    return E
def s_story(C, D, dur):
    E = head('A rollback, step by step', 'One bad release, handled calmly.', C['y1']); E.append(ill(C['y1'], 1400, 130))
    it = [('10:00', 'Deploy v1.4.3', WARN, 'y2'), ('10:06', 'Errors rise', BAD, 'y3'), ('10:10', 'Rule met: roll back', VIO, 'y4'), ('10:14', 'v1.4.2 restored', GOOD, 'y5'), ('Then', 'Investigate in test', ACC, 'y6')]
    for i, (n, t_, col, cid) in enumerate(it):
        E.append(Pop(card(290, 230, col, n, [(t_, TXT)], 44, 30), 100 + i * 350, 400, C[cid]))
        if i: E.append(A([(100 + i * 350 - 54, 515), (100 + i * 350 - 8, 515)], C[cid] - 0.1, MUTED, 5, 18))
    E.append(Pop(card(840, 170, WARN, 'Alternative', [('A quick fix can be safer than a rollback.', TXT)], 38, 32), 100, 690, C['y7']))
    E.append(Pop(card(840, 170, ACC, 'The record', [('Deployment record: what, when, by whom.', TXT)], 38, 32), 980, 690, C['y8']))
    return E
def s_maint(C, D, dur):
    E = head('Maintenance', 'Software needs care as long as it runs.', C['m1'])
    it = [('Corrective', 'Fix bugs that customers find', BAD, 'm3', 'test'), ('Adaptive', 'Keep up with new browsers and rules', ACC, 'm4', 'swap'),
          ('Perfective', 'Improve speed and usability', GOOD, 'm5', 'rocket'), ('Preventive', 'Tidy code, apply security patches', VIO, 'm6', 'gear')]
    for i, (n, s, col, cid, g) in enumerate(it):
        E.append(Pop(card(840, 170, col, n, [(s, TXT)], 40, 30), 100 + (i % 2) * 880, 330 + (i // 2) * 200, C[cid]))
    E.append(Pop(card(1720, 150, WARN, 'Ignored maintenance becomes technical debt', [('It slows every future change.', TXT)], 38, 34), 100, 760, C['m7']))
    E.append(takeaway('Planned care is cheaper than emergency repair.', 940, C['m8'], GOOD, 1600, 36))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Spot them early.', C['w1'])
    it = [('Myth: passed in test, so it is safe', 'Reality: test lowers risk, differences remain.', WARN, 'w2'), ('Myth: we can always roll back', 'Reality: data changes can make it hard.', BAD, 'w3'),
          ('Myth: approvals only slow us down', 'Reality: the right ones prevent costly mistakes.', VIO, 'w4'), ('Myth: maintenance is leftover work', 'Reality: it is most of a system\'s life.', GOOD, 'w5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 36, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Plan for all four.', 860, C['w6'], GOOD, 1500))
    return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    qs = [('Name the three environments, and what each is for.', 'z2'), ('Why build once, and move the same build?', 'z3'), ('What four questions measure release risk?', 'z4'), ('What must be ready before a rollback can work?', 'z8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 32, maxw=930), 190, 280 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['z9']))
    E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC01-O07  ·  Releases', 'b', 30, TXT, maxw=900), 220, 748, C['z9'] + 0.3, anim='wipe', d=1.6))
    E.append(Pop(badge('PAUSE  ·  plan one change\'s path', F('b', 34), INK, PINK, padx=26, pady=14), 100, 860, C['z5']))
    E.append(El(T('Next: The CloudCart workflow', 'x', 50, ACC), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 960, 960, C['z7']))
    return E
FN = dict(hook=s_hook, envs=s_envs, dev=s_dev, test=s_test, prod=s_prod, same=s_same, approvals=s_approvals, risk=s_risk, reduce=s_reduce, rollback=s_rollback, story=s_story, maint=s_maint, myths=s_myths, recap=s_recap)

_GL7 = dict(envs=('grid', ACC), dev=('code', ACC), test=('test', GOOD), prod=('rocket', WARN), same=('tag', PINK), approvals=('check', VIO), risk=('question', WARN), reduce=('eye', GOOD),
            rollback=('swap', BAD), story=('loop', VIO), maint=('gear', PINK), myths=('question', VIO))
def _wrap7(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL7[name]
        if g == 'check': E.append(Pop(icon('check', 90, TXT, col), 1255, 130, C[first] + 0.3))
        else: E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3))
        return E
    return w
for _n in _GL7: FN[_n] = _wrap7(_n, FN[_n])
