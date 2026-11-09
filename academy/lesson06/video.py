import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 6  ·  DEVOPS BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "One small change. Many steps."), c('h2', "CloudCart wants free shipping on orders over fifty dollars.", "CloudCart wants free shipping on orders over fifty dollars."),
  c('h3', "It sounds simple. But a change passes through many hands before customers see it."), c('h4', "Tracing it shows how the whole life cycle connects."),
  c('h5', "Today you follow one change, from idea to feedback."),
 ]),
 ('journey', [
  c('j1', "Here is the journey, in seven steps."), c('j2', "First, a requirement says what is needed."), c('j3', "Then code makes it happen."), c('j4', "Reviewers check the code."),
  c('j5', "Tests prove it works."), c('j6', "A release packages the approved version, and deployment puts it live."), c('j7', "Feedback shows how it went."),
  c('j8', "Then the loop starts again."),
 ]),
 ('requirement', [
  c('r1', "Step one: the requirement."), c('r2', "Product writes a ticket: C A R T, one forty-two.", "Product writes a ticket: C A R T, one forty-two."),
  c('r3', "It includes acceptance criteria."), c('r4', "Given a cart of fifty dollars or more, shipping shows zero dollars.", "Given a cart of fifty dollars or more, shipping shows zero dollars."),
  c('r5', "Acceptance criteria turn an idea into something testable."),
 ]),
 ('code', [
  c('c1', "Step two: the code."), c('c2', "A developer creates a branch, a separate copy of the main code."), c('c3', "They change the shipping rule, and write a unit test."),
  c('c4', "Each saved change is a commit, with its own identifier."), c('c5', "In this example, the commit links back to the ticket."),
 ]),
 ('review', [
  c('v1', "Step three: review."), c('v2', "The developer opens a pull request."), c('v3', "A teammate reads the change, and asks questions."),
  c('v4', "Review catches mistakes, and shares knowledge."), c('v5', "Only after approval does the change merge into the main code."),
 ]),
 ('test', [
  c('t1', "Step four: test."), c('t2', "When the change merges, a pipeline starts automatically."), c('t3', "It builds the application, and runs the automated tests."),
  c('t4', "In this example, build three eighteen passes."), c('t5', "QA also checks the change in a test environment."), c('t6', "If a test fails, the change goes back to the developer."),
 ]),
 ('release', [
  c('e1', "Step five: release."), c('e2', "The approved build gets a version number: one point four point three.", "The approved build gets a version number: one point four point three."),
  c('e3', "Release notes explain what changed."), c('e4', "The version number lets everyone say exactly which code is running."),
 ]),
 ('deploy', [
  c('d1', "Step six: deployment."), c('d2', "The release goes to a test environment first, then to production."), c('d3', "The deployment is recorded: what, when, and by whom."),
  c('d4', "A safe deployment can be repeated, and reversed if needed."), c('d5', "Environments and rollback get their own lesson next."),
 ]),
 ('feedback', [
  c('f1', "Step seven: feedback."), c('f2', "Monitoring shows errors, speed, and traffic."), c('f3', "Customers react: orders, comments, and support tickets."),
  c('f4', "Did free shipping increase orders? Did anything break?"), c('f5', "Feedback becomes the next requirement, and the loop continues."),
 ]),
 ('trail', [
  c('a1', "Notice that every step left a trail."), c('a2', "The ticket, the commit, the pull request, the build, the release, and the deployment record."),
  c('a3', "This is called traceability."), c('a4', "If something breaks, you can follow the trail backwards to the cause."), c('a5', "Good teams make every step leave evidence."),
 ]),
 ('broken', [
  c('b1', "Now suppose customers report a wrong shipping price."), c('b2', "Start from the symptom, and ask: which version is running?"),
  c('b3', "That points to the release, and the build behind it."), c('b4', "Then to the pull request, and its review."), c('b5', "And finally to the ticket, to see what was asked."),
  c('b6', "Tracing backwards turns a mystery into a short search."),
 ]),
 ('where', [
  c('w1', "Where does the problem start? Match each symptom to a step."), c('w2', "Nobody agrees what free shipping means? The requirement was unclear."),
  c('w3', "The change broke another page? The tests missed it."), c('w4', "A bug went unnoticed for a week? Monitoring and feedback were weak."),
  c('w5', "Nobody knows which version is live? The release and deployment records are missing."), c('w6', "Problems often show up late, but they usually start early."),
 ]),
 ('myths', [
  c('y1', "Watch out for four common myths."), c('y2', "Myth one: a change is finished when the code is written. In fact, it is finished when it works for customers."),
  c('y3', "Myth two: testing is one step at the end. In fact, testing happens throughout."), c('y4', "Myth three: feedback is optional. Without it, the team is guessing."),
  c('y5', "Myth four: small changes do not need the full path. Small changes break things too."), c('y6', "Follow the whole path, every time."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "Name the seven steps, in order."), c('z3', "What are acceptance criteria for?"), c('z4', "What is traceability?"), c('z8', "Why is feedback the last step, and also the first of the next change?"),
  c('z9', "Objective covered: MC01-O06.", "Objective covered: number six, in the S D L C masterclass."),
  c('z5', "Pause the video, and write the seven steps for a change of your own."), c('z6', "Next lesson: environments and releases."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h5': 0.5, 'j8': 0.5, 'r5': 0.5, 'c5': 0.5, 'v5': 0.5, 't6': 0.5, 'e4': 0.5, 'd5': 0.5, 'f5': 0.5, 'a5': 0.5, 'b6': 0.5, 'w6': 0.5, 'y6': 0.5, 'z5': 12.0}
CHAP = {'journey': 'The seven steps', 'requirement': 'Requirement', 'code': 'Code', 'review': 'Review', 'test': 'Test', 'release': 'Release', 'deploy': 'Deployment', 'feedback': 'Feedback',
        'trail': 'The trail', 'broken': 'Tracing a problem', 'where': 'Where did it start?', 'myths': 'Common myths', 'recap': 'Quick check'}
STEPS = ['Requirement', 'Code', 'Review', 'Test', 'Release', 'Deploy', 'Feedback']
SC = [WARN, ACC, VIO, GOOD, PINK, WARN, VIO]
def head(title, sub, t): return [El(T('Trace  ·  Lesson 6', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
GL = ['doc', 'code', 'eye', 'test', 'tag', 'rocket', 'loop']
LOGO = [None, 'git', 'github', 'jenkins', 'docker', 'kubernetes', 'prometheus']
def tracker(E, active, t):
    for i, n in enumerate(STEPS):
        on = i == active
        E.append(Pop(card(215, 64, SC[i] if on else MUTED, '', [(n, TXT if on else MUTED)], 4, 26), 100 + i * 250, 300, t + 0.05 * i))
def step(E, idx, title, sub, cards, art, q, C, ids, aid, tk, tkid, tkcol=GOOD):
    E += head(title, sub, C[ids[0]]); tracker(E, idx, C[ids[0]] + 0.3)
    for i, (n, t_) in enumerate(cards): E.append(Pop(card(540, 220, SC[idx], n, [(t_, TXT)], 44, 34), 100 + i * 590, 400, C[ids[i + 1]]))
    E.append(Pop(card(1720, 200, SC[idx], art[0], [(art[1], TXT)], 44, 40), 100, 660, C[aid]))
    E.append(ill(C[ids[0]], 1400, 130))
    E.append(Pop(glyph(GL[idx], 120, SC[idx], True), 1230, 105, C[ids[0]] + 0.2))
    if LOGO[idx]: E.append(logo(LOGO[idx], 1680, 705, C[aid] + 0.4, 90))
    else: E.append(Pop(glyph('doc', 90, SC[idx], True), 1680, 715, C[aid] + 0.4))
    E.append(takeaway(tk, 920, C[tkid], tkcol, 1600))
    return E

def s_hook(C, D, dur):
    E = [El(T('One change. Many steps.', 'x', 64), 100, 130, C['h1']), ill(C['h1'], 1400, 130)]
    E.append(Pop(card(1720, 220, WARN, 'Ticket CART-142', [('Free shipping on orders over $50', TXT)], 48, 46), 100, 320, C['h2']))
    E.append(El(T('Touched by', 'b', 32, MUTED), 100, 600, C['h3'], anim='fade'))
    bx = 100
    for i, n in enumerate(['Product', 'Developers', 'QA', 'Security', 'DevOps', 'Operations']):
        b = badge(n, F('x', 36), INK, [WARN, ACC, GOOD, BAD, PINK, VIO][i], padx=26, pady=14, r=26)
        E.append(Pop(b, bx, 650, C['h3'] + 0.3 + i * 0.35)); bx += b.width + 40
    E.append(takeaway('Follow one change, and the whole life cycle appears.', 880, C['h4'], GOOD, 1600))
    return E
def s_journey(C, D, dur):
    E = head('The seven steps', 'One change, from idea to feedback.', C['j1'])
    ids = ['j2', 'j3', 'j4', 'j5', 'j5', 'j6', 'j7']
    for i, n in enumerate(STEPS):
        E.append(Pop(card(215, 170, SC[i], f'{i + 1}', [(n, TXT)], 48, 26), 100 + i * 250, 380, C[ids[i]] + (0.8 if i == 5 else 0)))
        E.append(Pop(glyph(GL[i], 54, SC[i]), 100 + i * 250 + 140, 392, C[ids[i]] + (0.8 if i == 5 else 0) + 0.2))
        if i: E.append(El(T('›', 'x', 56, MUTED), 100 + i * 250 - 26, 420, C[ids[i]] + (0.8 if i == 5 else 0), anim='fade'))
    E.append(Pop(card(1720, 150, ACC, 'The loop', [('Feedback becomes the next requirement.', TXT)], 44, 40), 100, 640, C['j8']))
    E.append(takeaway('Every change follows this path, large or small.', 880, C['j8'] + 0.6, WARN, 1600))
    return E
def s_requirement(C, D, dur):
    return step([], 0, 'Requirement', 'What is needed, and how we will know.', [('The ticket', 'CART-142 from Product'), ('Acceptance criteria', 'Clear, testable rules'), ('Shared meaning', 'Everyone agrees what free means')],
                ('Acceptance criterion', 'Given a cart of $50 or more, shipping shows $0.'), None, C, ['r1', 'r2', 'r3', 'r3'], 'r4', 'Acceptance criteria turn an idea into something testable.', 'r5')
def s_code(C, D, dur):
    return step([], 1, 'Code', 'A developer builds the change.', [('Branch', 'A separate copy to work in'), ('Change and test', 'Shipping rule, plus a unit test'), ('Commit', 'Each saved change has an identifier')],
                ('Commit a1b2c3d', 'Message: CART-142 free shipping over $50'), None, C, ['c1', 'c2', 'c3', 'c4'], 'c5', 'The commit links back to the ticket.', 'c5')
def s_review(C, D, dur):
    return step([], 2, 'Review', 'A teammate checks before it merges.', [('Pull request', 'The developer asks to merge'), ('Read and ask', 'A teammate reviews the change'), ('Catch and share', 'Mistakes found, knowledge spread')],
                ('Pull request #57', 'Approved by a teammate, then merged to main'), None, C, ['v1', 'v2', 'v3', 'v4'], 'v5', 'Approval first, then merge.', 'v5')
def s_test(C, D, dur):
    return step([], 3, 'Test', 'Prove it works, automatically.', [('Pipeline starts', 'Triggered by the merge'), ('Build and test', 'Automated checks run'), ('QA checks', 'In a test environment')],
                ('Build #318', 'Passed: build succeeded, all tests green'), None, C, ['t1', 't2', 't3', 't5'], 't4', 'A failed test sends the change back to the developer.', 't6')
def s_release(C, D, dur):
    return step([], 4, 'Release', 'The approved version gets a name.', [('Version number', 'One identity for this code'), ('Release notes', 'What changed, in plain words'), ('Exact meaning', 'Everyone knows what is running')],
                ('Release v1.4.3', 'Includes CART-142: free shipping over $50'), None, C, ['e1', 'e2', 'e3', 'e4'], 'e2', 'The version number says exactly which code is running.', 'e4')
def s_deploy(C, D, dur):
    return step([], 5, 'Deployment', 'Put the release where customers use it.', [('Test first', 'A test environment'), ('Then production', 'The live shop'), ('Recorded', 'What, when, and by whom')],
                ('Deployment record', 'v1.4.3 to production, with time and owner'), None, C, ['d1', 'd2', 'd2', 'd3'], 'd3', 'Safe deployments can be repeated, and reversed.', 'd4')
def s_feedback(C, D, dur):
    return step([], 6, 'Feedback', 'Learn what really happened.', [('Monitoring', 'Errors, speed, and traffic'), ('Customers', 'Orders, comments, tickets'), ('Questions', 'More orders? Anything broken?')],
                ('The next requirement', 'What we learn becomes the next ticket'), None, C, ['f1', 'f2', 'f3', 'f4'], 'f5', 'Feedback closes the loop.', 'f5')
def s_trail(C, D, dur):
    E = head('The trail', 'Every step leaves evidence.', C['a1']); E.append(ill(C['a2'], 1400, 130))
    it = [('Ticket', 'CART-142', WARN), ('Commit', 'a1b2c3d', ACC), ('Pull request', '#57', VIO), ('Build', '#318', GOOD), ('Release', 'v1.4.3', PINK), ('Deployment', 'Recorded: what, when, by whom', WARN)]
    for i, (n, t_, col) in enumerate(it): E.append(Pop(card(540, 190, col, n, [(t_, TXT)], 44, 36), 100 + (i % 3) * 590, 340 + (i // 3) * 230, C['a2'] + i * 0.6))
    E.append(Pop(badge('Traceability', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 805, C['a3']))
    E.append(Pop(glyph('link', 84, GOOD, True), 480, 797, C['a3'] + 0.3))
    E.append(takeaway('Follow the trail backwards to find a cause.', 950, C['a4'], WARN, 1600))
    return E
def s_broken(C, D, dur):
    E = head('Tracing a problem', 'From the symptom back to the ticket.', C['b1']); E.append(ill(C['b1'], 1400, 130))
    it = [('Symptom', 'Wrong shipping price', BAD, 'b1'), ('Release', 'v1.4.3 is live', PINK, 'b2'), ('Build', '#318 and its commit', GOOD, 'b3'), ('Pull request', '#57 and its review', VIO, 'b4'), ('Ticket', 'CART-142: what was asked', WARN, 'b5')]
    for i, (n, t_, col, cid) in enumerate(it):
        E.append(Pop(card(290, 230, col, n, [(t_, TXT)], 40, 30), 100 + i * 350, 420, C[cid] + (0.6 if i == 0 else 0)))
        if i: E.append(A([(100 + i * 350 - 54, 535), (100 + i * 350 - 8, 535)], C[cid] - 0.1, MUTED, 5, 18))
    E.append(El(T('Trace backwards', 'b', 32, MUTED), 100, 350, C['b2'], anim='fade'))
    E.append(takeaway('A mystery becomes a short search.', 760, C['b6'], GOOD, 1500))
    return E
def s_where(C, D, dur):
    E = head('Where did it start?', 'Match each symptom to a step.', C['w1']); E.append(ill(C['w1'], 1400, 130))
    rows = [('Nobody agrees what "free" means', 'Requirement', 0, 'w2'), ('The change broke another page', 'Test', 3, 'w3'), ('A bug went unnoticed for a week', 'Feedback', 6, 'w4'), ('Nobody knows which version is live', 'Release and deployment', 4, 'w5')]
    for i, (s_, f, k, cid) in enumerate(rows):
        y = 340 + i * 125
        E.append(Pop(card(1000, 90, SC[k], '', [(s_, TXT)], 4, 34), 100, y, C[cid]))
        E.append(Pop(badge(f, F('b', 36), INK, SC[k], padx=26, pady=12, r=24), 1140, y + 14, C[cid] + 1.0))
    E.append(takeaway('Problems often show up late, but start early.', 880, C['w6'], WARN, 1600))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Spot them early.', C['y1'])
    it = [('Myth: done when the code is written', 'Reality: done when it works for customers.', WARN, 'y2'), ('Myth: testing is one step at the end', 'Reality: testing happens throughout.', GOOD, 'y3'),
          ('Myth: feedback is optional', 'Reality: without it, the team is guessing.', VIO, 'y4'), ('Myth: small changes skip the path', 'Reality: small changes break things too.', ACC, 'y5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 36, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Follow the whole path, every time.', 860, C['y6'], GOOD, 1500))
    return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    for i, (q, cid) in enumerate([('Name the seven steps, in order.', 'z2'), ('What are acceptance criteria for?', 'z3'), ('What is traceability?', 'z4'), ('Why is feedback last, yet also first for the next change?', 'z8')]):
        E.append(Pop(card(1720, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 38, maxw=1500), 190, 278 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1720, 100, GOOD, '', [], 4), 100, 710, C['z9']))
    E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC01-O06  ·  Tracing one change', 'b', 32, TXT, maxw=1560), 220, 744, C['z9'] + 0.3, anim='wipe', d=1.6))
    E.append(Pop(badge('PAUSE  ·  write the seven steps for a change of your own', F('b', 34), INK, PINK, padx=26, pady=14), 100, 860, C['z5']))
    E.append(El(T('Next: Environments and releases', 'x', 50, ACC), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 1500, 960, C['z7']))
    return E
FN = dict(hook=s_hook, journey=s_journey, requirement=s_requirement, code=s_code, review=s_review, test=s_test, release=s_release, deploy=s_deploy, feedback=s_feedback, trail=s_trail, broken=s_broken, where=s_where, myths=s_myths, recap=s_recap)
