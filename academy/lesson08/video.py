import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 8  ·  DEVOPS BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "This is the last lesson of the first masterclass."), c('h2', "So today, you stop watching, and start designing."),
  c('h3', "CloudCart wants a new feature: save for later."), c('h4', "Your job is to plan how it travels from idea to customers."),
  c('h5', "You will use everything from lessons one to seven."),
 ]),
 ('brief', [
  c('b1', "Here is the scenario."), c('b2', "Customers want to move an item out of the cart, and save it for later."),
  c('b3', "The ticket is C A R T, two ten.", "The ticket is C A R T, two ten."), c('b4', "You must produce one page, a workflow table."),
  c('b5', "It shows each stage, who owns it, what it produces, and who receives it."), c('b6', "It also shows the approvals, and the rollback plan."),
 ]),
 ('template', [
  c('t1', "Start with the table itself."), c('t2', "The first column is the stage."), c('t3', "The second is the owner, one named role, never everyone."),
  c('t4', "The third is the artifact, the thing that stage produces."), c('t5', "The fourth is the handoff, which says who receives it next."),
  c('t6', "If any cell is empty, the workflow has a gap."),
 ]),
 ('rows1', [
  c('w1', "Now fill it in for save for later."), c('w2', "Requirement. Product owns it, and produces the ticket with acceptance criteria. It goes to a developer."),
  c('w3', "Code. A developer owns it, and produces a branch, commits, and unit tests. It goes to a reviewer."),
  c('w4', "Review. A teammate owns it, and produces an approved pull request. It goes to the pipeline."),
  c('w5', "Test. The pipeline and Q A own it, and produce a build and a test report. It goes to the release owner.", "Test. The pipeline and Q A own it, and produce a build and a test report. It goes to the release owner."),
  c('w6', "Notice that every row ends by naming the next receiver."),
 ]),
 ('rows2', [
  c('x1', "Three stages remain."), c('x2', "Release. The release owner produces version one point five point zero, with release notes. It goes to operations.", "Release. The release owner produces version one point five point zero, with release notes. It goes to operations."),
  c('x3', "Deployment. DevOps produces the deployment record, and hands over to monitoring."),
  c('x4', "Feedback. Product and operations read the metrics, and produce new tickets."), c('x5', "Those tickets go back to Product, and the loop continues."),
 ]),
 ('handoff', [
  c('f1', "Handoffs are where work gets lost."), c('f2', "A good handoff has four parts."), c('f3', "First, a clear input: what exactly is being passed on."),
  c('f4', "Second, a done rule: what must be true before it moves."), c('f5', "Third, evidence, such as a test report, or an approval."),
  c('f6', "Fourth, a named receiver, who knows it is now theirs."), c('f7', "Miss one, and work waits, or gets repeated."),
 ]),
 ('gates', [
  c('g1', "Now add what you learned in lesson seven."), c('g2', "Which environments does this change pass through? Development, then test, then production."),
  c('g3', "Which approvals sit in between? Code review, Q A sign-off, and a release approval."),
  c('g4', "Rate the risk. Saving an item is low to medium, because it touches the cart, but not payments."),
  c('g5', "Write the rollback plan: the trigger, the previous version, and who decides."),
  c('g6', "For example: if errors stay high for five minutes, return to version one point four point three.", "For example: if errors stay high for five minutes, return to version one point four point three."),
 ]),
 ('trace', [
  c('r1', "A good workflow can be traced."), c('r2', "Start at the ticket: C A R T, two ten.", "Start at the ticket: C A R T, two ten."),
  c('r3', "It links to a pull request, and its review."), c('r4', "Then to the build, and the version."), c('r5', "Then to the deployment record."),
  c('r6', "If customers report a problem, you can follow this chain backwards."), c('r7', "No chain, no trace, and no quick answers."),
 ]),
 ('rubric', [
  c('u1', "How do you know your workflow is good? Use this pass or fail rubric."), c('u2', "One: every stage has one named owner."),
  c('u3', "Two: every stage produces a named artifact."), c('u4', "Three: every handoff names who receives it."),
  c('u5', "Four: each move toward production has an approval that matches the risk."), c('u6', "Five: the rollback plan names a trigger, and a previous version."),
  c('u7', "Six: feedback returns as a new ticket."), c('u8', "You pass only when all six are true."),
 ]),
 ('mistakes', [
  c('m1', "Watch for four common mistakes."), c('m2', "No owner. If everyone owns it, nobody does."),
  c('m3', "A vague artifact, like the code, instead of pull request sixty-one."), c('m4', "No rollback plan, so the first failure becomes a crisis."),
  c('m5', "No feedback loop, so the team never learns."), c('m6', "Check your own table for all four."),
 ]),
 ('yourturn', [
  c('y1', "Now it is your turn."), c('y2', "The new feature is order tracking: customers see where their parcel is."),
  c('y3', "Create your own workflow table for it, with all seven stages."), c('y4', "Add the environments, approvals, risk rating, and rollback plan."),
  c('y5', "Then mark yourself against the six-point rubric."), c('y6', "Pause the video now, and do it before you continue."),
 ]),
 ('review', [
  c('v1', "Before we close, look at the whole masterclass."), c('v2', "You met requirements, and user stories."), c('v3', "You compared the phases with Waterfall, Agile, Scrum, Kanban, and DevOps."),
  c('v4', "You learned the parts of an application, and who does what."), c('v5', "You traced a change, and learned environments, approvals, and rollback."),
  c('v6', "And today, you designed a complete workflow."), c('v7', "Passing the rubric on your own is how you show you have mastered it."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "What four columns does a workflow table need?"), c('z3', "What are the four parts of a good handoff?"),
  c('z4', "What does a rollback plan name?"), c('z8', "Which six things does the rubric check?"),
  c('z9', "Objective covered: MC01-O08.", "Objective covered: number eight, in the S D L C masterclass."),
  c('z5', "Pause the video, and check your table against the rubric."), c('z6', "Next masterclass: I T and computer fundamentals.", "Next masterclass: I T and computer fundamentals."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h5': 0.5, 'b6': 0.5, 't6': 0.5, 'w6': 0.5, 'x5': 0.5, 'f7': 0.5, 'g6': 0.5, 'r7': 0.5, 'u8': 0.5, 'm6': 0.5, 'y6': 15.0, 'v7': 0.5, 'z5': 10.0}
CHAP = {'brief': 'The scenario', 'template': 'The workflow table', 'rows1': 'Filling it in, part 1', 'rows2': 'Filling it in, part 2', 'handoff': 'Good handoffs', 'gates': 'Environments, approvals, rollback',
        'trace': 'Traceability', 'rubric': 'Pass or fail rubric', 'mistakes': 'Common mistakes', 'yourturn': 'Your turn', 'review': 'The whole masterclass', 'recap': 'Quick check'}
STEPS = ['Requirement', 'Code', 'Review', 'Test', 'Release', 'Deploy', 'Feedback']
SC = [WARN, ACC, VIO, GOOD, PINK, WARN, VIO]
def head(title, sub, t): return [El(T('Mastery  ·  Lesson 8', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)

COLX = [100, 430, 790, 1360]; COLW = [300, 330, 540, 460]
ROWS = [('Requirement', 'Product owner', 'Ticket CART-210 and criteria', 'Developer'), ('Code', 'Developer', 'Branch, commits, unit tests', 'Reviewer'),
        ('Review', 'Teammate', 'Approved pull request #61', 'Pipeline'), ('Test', 'Pipeline and Q A', 'Build #402, test report', 'Release owner'),
        ('Release', 'Release owner', 'Version 1.5.0, release notes', 'Operations'), ('Deploy', 'DevOps', 'Deployment record', 'Monitoring'),
        ('Feedback', 'Product and operations', 'Metrics, new tickets', 'Product owner')]
def header_row(t, y=330, cols=('Stage', 'Owner', 'Artifact', 'Handoff to')):
    return [El(T(n, 'b', 28, MUTED), COLX[i] + 18, y, t + 0.2 * i, anim='fade') for i, n in enumerate(cols)]
def table_row(i, y, t, tt=0.15):
    E = [Pop(card(COLW[0], 100, SC[i], '', [(f'{i + 1}  {ROWS[i][0]}', SC[i])], 4, 32), COLX[0], y, t)]
    for k in range(1, 4): E.append(Pop(card(COLW[k], 100, SC[i], '', [(ROWS[i][k], TXT)], 4, 28), COLX[k], y, t + tt * k))
    return E

def s_hook(C, D, dur):
    E = [El(T('Your turn to design', 'x', 64), 100, 130, C['h1']), ill(C['h1'], 1400, 130)]
    E.append(Pop(card(1720, 140, WARN, 'CloudCart feature', [('Save for later: move an item out of the cart, and keep it.', TXT)], 46, 40), 100, 300, C['h3']))
    E.append(Pop(card(1720, 150, ACC, 'Your job', [('Plan how it travels from idea to customers.', TXT)], 42, 38), 100, 500, C['h4']))
    bs = [badge(n, F('b', 34), INK, col, padx=24, pady=12, r=24) for n, col in [('Lessons 1 to 7', GOOD), ('Workflow table', ACC), ('Pass or fail rubric', VIO)]]
    gap = 50; bx = 100 + (1720 - (sum(b.width for b in bs) + gap * 2)) / 2
    for i, b in enumerate(bs): E.append(Pop(b, bx, 720, C['h5'] + i * 0.4)); bx += b.width + gap
    E.append(takeaway('Plan it like a professional.', 880, C['h5'] + 0.8, GOOD, 1600))
    return E
def s_brief(C, D, dur):
    E = head('The scenario', 'A small feature, a full workflow.', C['b1']); E.append(ill(C['b2'], 1400, 130))
    E.append(Pop(card(1720, 150, WARN, 'Ticket CART-210', [('Customers can save a cart item for later.', TXT)], 46, 40), 100, 330, C['b2']))
    it = [('Stages and owners', 'Who does what', ACC, 'b5'), ('Artifacts and handoffs', 'What passes on, and to whom', VIO, 'b5'), ('Approvals and rollback', 'How it ships safely', GOOD, 'b6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 200, col, n, [(s, TXT)], 40, 32), 100 + i * 590, 540, C[cid] + (0.7 if i == 1 else 0)))
    E.append(Pop(badge('Deliverable: one page', F('x', 44), INK, WARN, padx=30, pady=14, r=28), 100, 800, C['b4']))
    return E
def s_template(C, D, dur):
    E = head('The workflow table', 'Four columns. No empty cells.', C['t1'])
    it = [('Stage', 'Where the change is', ACC, 't2'), ('Owner', 'One named role', VIO, 't3'), ('Artifact', 'What the stage produces', GOOD, 't4'), ('Handoff to', 'Who receives it next', WARN, 't5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(400, 250, col, n, [(s, TXT)], 46, 32, True), 100 + i * 440, 360, C[cid]))
    E.append(Pop(card(1720, 140, BAD, 'An empty cell', [('means a gap, where work gets lost.', TXT)], 40, 38), 100, 680, C['t6']))
    return E
def s_rows1(C, D, dur):
    E = head('Filling it in, part 1', 'Save for later, stages one to four.', C['w1']); E.append(ill(C['w2'], 1400, 130))
    E += header_row(C['w1'] + 0.5)
    for k, cid in enumerate(['w2', 'w3', 'w4', 'w5']): E += table_row(k, 380 + k * 120, C[cid])
    E.append(takeaway('Every row names the next receiver.', 900, C['w6'], GOOD, 1600))
    return E
def s_rows2(C, D, dur):
    E = head('Filling it in, part 2', 'Stages five to seven.', C['x1']); E.append(ill(C['x2'], 1400, 130))
    E += header_row(C['x1'] + 0.5)
    for k, cid in enumerate(['x2', 'x3', 'x4']): E += table_row(4 + k, 380 + k * 120, C[cid])
    E.append(Pop(card(1720, 130, GOOD, 'The loop', [('Feedback produces new tickets, and the cycle continues.', TXT)], 38, 34), 100, 770, C['x5']))
    return E
def s_handoff(C, D, dur):
    E = head('Good handoffs', 'Where work most often gets lost.', C['f1'])
    it = [('Clear input', 'Exactly what is passed on', ACC, 'f3'), ('Done rule', 'What must be true first', VIO, 'f4'), ('Evidence', 'Test report, approval', GOOD, 'f5'), ('Named receiver', 'Who now owns it', WARN, 'f6')]
    for i, (n, s, col, cid) in enumerate(it):
        E.append(Pop(card(400, 230, col, f'{i + 1}  {n}', [(s, TXT)], 38, 30, True), 100 + i * 440, 360, C[cid]))
    E.append(Pop(card(1720, 150, BAD, 'Miss one part', [('and the work waits, or gets repeated.', TXT)], 40, 38), 100, 680, C['f7']))
    return E
def s_gates(C, D, dur):
    E = head('Environments, approvals, rollback', 'What lesson seven adds to the table.', C['g1']); E.append(ill(C['g2'], 1400, 130))
    envs = [('Development', ACC), ('Test', GOOD), ('Production', WARN)]
    for i, (n, col) in enumerate(envs):
        E.append(Pop(card(480, 110, col, n, [], 42), 100 + i * 620, 330, C['g2'] + i * 0.6))
        if i: E.append(A([(100 + i * 620 - 140, 385), (100 + i * 620 - 12, 385)], C['g2'] + i * 0.6, MUTED, 6, 22))
    ap = [badge(n, F('b', 32), INK, col, padx=24, pady=12, r=24) for n, col in [('Code review', ACC), ('Q A sign-off', GOOD), ('Release approval', WARN)]]
    E.append(El(T('Approvals on the way', 'b', 30, MUTED), 100, 470, C['g3'], anim='fade'))
    bx = 100
    for i, b in enumerate(ap): E.append(Pop(b, bx, 515, C['g3'] + 0.3 + i * 0.5)); bx += b.width + 40
    E.append(Pop(card(840, 190, VIO, 'Risk rating', [('Low to medium: touches the cart, not payments.', TXT)], 40, 32), 100, 600, C['g4']))
    E.append(Pop(card(840, 190, BAD, 'Rollback plan', [('Trigger, previous version, who decides.', TXT)], 40, 32), 980, 600, C['g5']))
    E.append(Pop(card(1720, 110, BAD, '', [('If errors stay high for 5 minutes, return to v1.4.3.', TXT)], 4, 36), 100, 830, C['g6']))
    return E
def s_trace(C, D, dur):
    E = head('Traceability', 'One chain from ticket to deployment.', C['r1']); E.append(ill(C['r2'], 1400, 130))
    it = [('Ticket', 'CART-210', WARN, 'r2'), ('Pull request', '#61 and review', VIO, 'r3'), ('Build', '#402', GOOD, 'r4'), ('Release', 'v1.5.0', PINK, 'r4'), ('Deployment', 'Recorded', WARN, 'r5')]
    for i, (n, t_, col, cid) in enumerate(it):
        E.append(Pop(card(290, 230, col, n, [(t_, TXT)], 38, 30), 100 + i * 350, 400, C[cid] + (0.7 if i == 3 else 0)))
        if i: E.append(A([(100 + i * 350 - 54, 515), (100 + i * 350 - 8, 515)], C[cid] + (0.6 if i == 3 else 0) - 0.1, MUTED, 5, 18))
    E.append(Pop(card(1720, 130, GOOD, 'A customer reports a problem', [('Follow the chain backwards to the cause.', TXT)], 38, 34), 100, 700, C['r6']))
    E.append(takeaway('No chain, no trace, no quick answers.', 900, C['r7'], WARN, 1600))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'All six must be true.', C['u1'])
    it = ['Every stage has one named owner', 'Every stage produces a named artifact', 'Every handoff names its receiver', 'Approvals match the risk', 'Rollback names a trigger and a version', 'Feedback returns as a new ticket']
    ids = ['u2', 'u3', 'u4', 'u5', 'u6', 'u7']
    for i, (n, cid) in enumerate(zip(it, ids)):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid]))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['u8']))
    return E
def s_mistakes(C, D, dur):
    E = head('Four common mistakes', 'Check your own table.', C['m1'])
    it = [('No owner', 'If everyone owns it, nobody does.', WARN, 'm2'), ('A vague artifact', '"The code", instead of pull request #61.', VIO, 'm3'),
          ('No rollback plan', 'The first failure becomes a crisis.', BAD, 'm4'), ('No feedback loop', 'The team never learns.', GOOD, 'm5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Find them before a reviewer does.', 860, C['m6'], GOOD, 1500))
    return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Design the workflow for a new feature.', C['y1'])
    E.append(Pop(card(1720, 150, WARN, 'New feature: order tracking', [('Customers see where their parcel is.', TXT)], 46, 40), 100, 330, C['y2']))
    it = [('1  The table', 'All seven stages', ACC, 'y3'), ('2  The safeguards', 'Environments, approvals, risk, rollback', VIO, 'y4'), ('3  The check', 'Mark yourself on the rubric', GOOD, 'y5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 200, col, n, [(s, TXT)], 40, 30, True), 100 + i * 590, 540, C[cid]))
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 820, C['y6']))
    return E
def s_review(C, D, dur):
    E = head('The whole masterclass', 'Eight objectives, one skill set.', C['v1'])
    it = [('O01', 'Business to software', 'v2'), ('O02', 'Stories and criteria', 'v2'), ('O03', 'Phases and methods', 'v3'), ('O04', 'Parts of an app', 'v4'),
          ('O05', 'Who does what', 'v4'), ('O06', 'Tracing a change', 'v5'), ('O07', 'Environments and releases', 'v5'), ('O08', 'The CloudCart workflow', 'v6')]
    for i, (n, t_, cid) in enumerate(it):
        x = 100 + (i % 4) * 440; y = 340 + (i // 4) * 250; col = [WARN, ACC, VIO, GOOD, PINK, WARN, ACC, VIO][i]
        E.append(Pop(card(400, 210, col, n, [(t_, TXT)], 46, 30, True), x, y, C[cid] + (i % 2) * 0.5))
        E.append(Pop(icon('check', 44, TXT, GOOD), x + 336, y + 22, C[cid] + (i % 2) * 0.5 + 0.3))
    E.append(takeaway('Passing the rubric on your own shows mastery.', 880, C['v7'], GOOD, 1600))
    return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    qs = [('What four columns does a workflow table need?', 'z2'), ('What are the four parts of a good handoff?', 'z3'), ('What does a rollback plan name?', 'z4'), ('Which six things does the rubric check?', 'z8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 32, maxw=930), 190, 280 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['z9']))
    E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC01-O08  ·  The CloudCart workflow', 'b', 30, TXT, maxw=900), 220, 748, C['z9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  check your table', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['z5']))
    E.append(El(T('Next masterclass: MC02  IT and computer fundamentals', 'x', 42, ACC, maxw=1500), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['z7']))
    return E
FN = dict(hook=s_hook, brief=s_brief, template=s_template, rows1=s_rows1, rows2=s_rows2, handoff=s_handoff, gates=s_gates, trace=s_trace, rubric=s_rubric, mistakes=s_mistakes, yourturn=s_yourturn, review=s_review, recap=s_recap)
_GL8 = dict(brief=('doc', WARN), template=('grid', ACC), rows1=('steps', VIO), rows2=('steps', PINK), handoff=('swap', ACC), gates=('rocket', WARN), trace=('link', PINK), rubric=('test', GOOD), mistakes=('question', BAD), yourturn=('board', VIO), review=('tag', GOOD))
def _wrap8(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL8[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL8: FN[_n] = _wrap8(_n, FN[_n])
