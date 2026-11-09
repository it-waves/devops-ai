import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 3  ·  DEVOPS BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "Two teams must build the same shop, CloudCart."), c('h2', "Team A plans everything first, then builds, then ships."),
  c('h3', "Team B builds a small version, shows it, and improves it."), c('h4', "Both teams follow the software development life cycle."),
  c('h5', "But they arrange the stages in time very differently."), c('h6', "Those arrangements have names, and knowing them is today's goal."),
  c('h7', "By the end, you will tell Waterfall, Agile, Scrum, Kanban, and DevOps apart."),
 ]),
 ('layers', [
  c('y1', "Start with one distinction."), c('y2', "The life cycle lists the stages: plan, design, build, test, release, deploy, and operate."),
  c('y3', "Waterfall and Agile describe how those stages are arranged over time."), c('y4', "Scrum and Kanban are ways of organizing the daily work."),
  c('y5', "And DevOps extends the cycle, so delivery and operations are part of the team's job."), c('y6', "Each level answers a different question."),
 ]),
 ('waterfall', [
  c('wf1', "Waterfall is the oldest, and simplest, arrangement."), c('wf2', "The stages run in order, and each one finishes before the next begins."),
  c('wf3', "Requirements, then design, then build, then test, then release, then operate."),
  c('wf4', "It works well when requirements are clear, stable, and well understood."), c('wf5', "For example, a fixed contract, or strict rules."),
  c('wf6', "The weakness is late feedback."), c('wf7', "Users may not see working software until the end."), c('wf8', "And a change late in the project is expensive."),
 ]),
 ('agile', [
  c('ag1', "Agile arranges the same stages in small, repeated cycles."), c('ag2', "Each cycle delivers a small piece of working software."),
  c('ag3', "Cycle one: browse products. Cycle two: search. Cycle three: place an order."), c('ag4', "After every cycle, the team shows the result, and listens."),
  c('ag5', "Agile began as a set of values, written in 2001, called the Agile Manifesto.", "Agile began as a set of values, written in two thousand one, called the Agile Manifesto."),
  c('ag6', "It prefers collaboration, working software, and a readiness to respond to change."),
  c('ag7', "Agile is a way of thinking, not one fixed method."), c('ag8', "Scrum and Kanban are two popular ways to practice it."),
 ]),
 ('scrum', [
  c('sc1', "Scrum is a framework for doing Agile work."), c('sc2', "Work happens in sprints: fixed time boxes of one month or less."),
  c('sc3', "A Scrum team has three roles."), c('sc4', "The product owner decides what is most valuable."), c('sc5', "The developers build and test the increment."),
  c('sc6', "The Scrum master helps the team follow Scrum, and removes blockers."),
  c('sc7', "Each sprint has four events: planning, a 15-minute daily scrum, a review, and a retrospective.", "Each sprint has four events: planning, a fifteen minute daily scrum, a review, and a retrospective."),
  c('sc8', "The result is a usable increment, at the end of every sprint."),
 ]),
 ('kanban', [
  c('kb1', "Kanban is a different way to organize the work."), c('kb2', "Work is shown on a board, with a column for each step."), c('kb3', "To do, doing, and done."),
  c('kb4', "The key rule is a limit on work in progress."), c('kb5', "If doing is full, the team finishes something before starting anything new."),
  c('kb6', "That keeps work flowing, and shows bottlenecks early."), c('kb7', "Kanban has no fixed sprints, so work can arrive and finish at any time."),
  c('kb8', "It suits support and operations work well."),
 ]),
 ('devops', [
  c('dv1', "DevOps goes one step further."), c('dv2', "Agile gets code written in small steps."),
  c('dv3', "DevOps carries that code all the way to a running system, and keeps it healthy."), c('dv4', "Three ideas stand out."),
  c('dv5', "Shared ownership: developers and operations work as one team."), c('dv6', "Automation: building, testing, and deploying are done by pipelines."),
  c('dv7', "Fast feedback: monitoring shows what users really experience."),
  c('dv8', "DevOps is not a tool, and not a job title. It is a way of working, supported by tools."), c('dv9', "You will learn those tools later in this bootcamp."),
 ]),
 ('compare', [
  c('cp1', "Let us compare them side by side."), c('cp2', "Waterfall: stages in strict order. Best when requirements are clear and stable."),
  c('cp3', "Agile: small cycles with steady feedback. Best when needs are still changing."), c('cp4', "Scrum: sprints, roles, and events. Best when one team builds one product."),
  c('cp5', "Kanban: a board with work limits. Best for a steady flow of requests."),
  c('cp6', "DevOps: development and operations as one team, with automation. Best for keeping software running, and improving it."),
  c('cp7', "Notice they are not rivals. Many teams combine them."),
 ]),
 ('cloudcart', [
  c('cc1', "Here is CloudCart, built both ways."), c('cc2', "With Waterfall, the team spends months on requirements, design, build, and test."),
  c('cc3', "Customers see the shop for the first time at the end."), c('cc4', "With Agile, a small piece is ready every month, or even sooner."),
  c('cc5', "Browse first, then search, then ordering."), c('cc6', "Customers can react early, and the team can change direction."),
  c('cc7', "Same stages, same goal, different rhythm."),
 ]),
 ('choose', [
  c('ch1', "Now match situations to methods."), c('ch2', "Fixed, well understood requirements, and strict sign-off? Waterfall-style planning fits."),
  c('ch3', "A new product where needs are unclear? Agile, often with Scrum."), c('ch4', "A team handling a steady stream of support requests? Kanban."),
  c('ch5', "Keeping a live shop healthy, with frequent, safe releases? DevOps practices."), c('ch6', "Real teams mix these, and adjust as they learn."),
 ]),
 ('myths', [
  c('my1', "Watch out for four common myths."), c('my2', "Myth one: Agile means no planning. In fact, Agile plans all the time, in smaller steps."),
  c('my3', "Myth two: Scrum and Agile are the same. Scrum is one way to practice Agile."), c('my4', "Myth three: DevOps is a tool, or a job title. It is a way of working."),
  c('my5', "Myth four: Waterfall is always wrong. It can still fit work with fixed, well understood requirements."), c('my6', "Choose by the situation, not by fashion."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "How is Waterfall different from Agile?"), c('z3', "What are the three roles in a Scrum team?"), c('z4', "What is the key rule in Kanban?"), c('z8', "Is DevOps a tool? Explain."),
  c('z9', "Objective covered: MC01-O03.", "Objective covered: number three, in the S D L C masterclass."),
  c('z5', "Pause the video, and answer out loud."), c('z6', "Next lesson: the parts of an application."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h7': 0.5, 'y6': 0.5, 'wf8': 0.5, 'ag8': 0.5, 'sc8': 0.5, 'kb8': 0.5, 'dv9': 0.5, 'cp7': 0.5, 'cc7': 0.5, 'ch6': 0.5, 'my6': 0.5, 'z5': 6.0}
CHAP = {'layers': 'The cycle and its methods', 'waterfall': 'Waterfall', 'agile': 'Agile', 'scrum': 'Scrum', 'kanban': 'Kanban', 'devops': 'DevOps', 'compare': 'Side by side',
        'cloudcart': 'CloudCart both ways', 'choose': 'Match the method', 'myths': 'Common myths', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Methods  ·  Lesson 3', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)

def s_hook(C, D, dur):
    E = [El(T('Same shop. Two plans.', 'x', 64), 100, 130, C['h1']), ill(C['h1'], 1400, 130)]
    E.append(Pop(card(840, 200, ACC, 'Team A', [('Plan everything first, then build, then ship.', TXT)], 44, 34), 100, 300, C['h2']))
    E.append(Pop(card(840, 200, VIO, 'Team B', [('Build a small version, show it, improve it.', TXT)], 44, 34), 980, 300, C['h3']))
    E.append(Pop(badge('Both follow the life cycle', F('x', 50), INK, GOOD, padx=34, pady=16, r=30), 100, 640, C['h4']))
    E.append(Pop(badge('One big release', F('b', 36), INK, ACC, padx=26, pady=12, r=22), 100, 540, C['h5']))
    E.append(Pop(badge('Many small releases', F('b', 36), INK, VIO, padx=26, pady=12, r=22), 980, 540, C['h5'] + 0.8))
    E.append(takeaway('Learn to tell the arrangements apart.', 860, C['h7'], WARN, 1500))
    return E
def s_layers(C, D, dur):
    E = head('The cycle, and how to run it', 'Four levels, four different questions.', C['y1'])
    rows = [('SDLC', 'What stages exist: plan to operate', ACC, 'y2'), ('Waterfall · Agile', 'How the stages are arranged over time', VIO, 'y3'),
            ('Scrum · Kanban', 'How the daily work is organized', GOOD, 'y4'), ('DevOps', 'Extends the cycle to delivery and operations', WARN, 'y5')]
    for i, (n, t_, col, cid) in enumerate(rows):
        y = 340 + i * 140
        E.append(Pop(badge(n, F('x', 44), INK, col, padx=30, pady=14, r=28), 100, y + 8, C[cid]))
        E.append(Pop(card(1160, 100, col, '', [(t_, TXT)], 4, 34), 660, y, C[cid] + 0.2))
    E.append(takeaway('Each level answers a different question.', 930, C['y6'], WARN, 1500))
    return E
def s_waterfall(C, D, dur):
    E = head('Waterfall', 'Each stage finishes before the next begins.', C['wf1'])
    names = ['Requirements', 'Design', 'Build', 'Test', 'Release', 'Operate']; cols = [ACC, VIO, GOOD, WARN, PINK, ACC]
    for i, n in enumerate(names):
        E.append(Pop(badge(n, F('x', 36), INK, cols[i], padx=24, pady=12, r=24), 100 + i * 295, 340 + i * 68, C['wf3'] + i * 0.55))
    E.append(Pop(card(840, 170, GOOD, 'Works well when', [('Requirements are clear and stable: a fixed contract, or strict rules.', TXT)], 38, 30), 100, 800, C['wf4']))
    E.append(Pop(card(840, 170, WARN, 'Watch out for', [('Late feedback, and expensive changes late in the project.', TXT)], 38, 30), 980, 800, C['wf6']))
    return E
def s_agile(C, D, dur):
    E = head('Agile', 'The same stages, in small repeated cycles.', C['ag1'])
    cyc = [('Cycle 1', 'Browse products'), ('Cycle 2', 'Search'), ('Cycle 3', 'Place an order')]
    for i, (n, t_) in enumerate(cyc):
        E.append(Pop(card(540, 130, ACC, n, [(t_, TXT)], 38, 32), 100 + i * 590, 340, C['ag3'] + i * 1.2))
    E.append(Pop(badge('The Agile Manifesto  ·  2001', F('b', 32), INK, WARN, padx=24, pady=10, r=22), 100, 500, C['ag5']))
    vals = [('Collaboration', 'Customers and team work together', VIO), ('Working software', 'Shown early, and often', GOOD), ('Responding to change', 'More than following a fixed plan', PINK)]
    for i, (n, t_, col) in enumerate(vals):
        E.append(Pop(card(540, 170, col, n, [(t_, TXT)], 38, 30), 100 + i * 590, 580, C['ag6'] + i * 0.9))
    E.append(takeaway('A way of thinking, not one fixed method.', 800, C['ag7'], WARN, 1500))
    E.append(Pop(badge('Scrum', F('x', 44), INK, ACC, padx=30, pady=14, r=28), 100, 900, C['ag8']))
    E.append(Pop(badge('Kanban', F('x', 44), INK, VIO, padx=30, pady=14, r=28), 360, 900, C['ag8'] + 0.6))
    return E
def s_scrum(C, D, dur):
    E = head('Scrum', 'A framework for doing Agile work.', C['sc1'])
    E.append(Pop(badge('Sprint: a fixed time box of one month or less', F('b', 34), INK, ACC, padx=26, pady=12, r=22), 100, 335, C['sc2']))
    E.append(El(T('Three roles', 'b', 32, MUTED), 100, 415, C['sc3'], anim='fade'))
    roles = [('Product owner', 'Decides what is most valuable', WARN, 'sc4'), ('Developers', 'Build and test the increment', GOOD, 'sc5'), ('Scrum master', 'Helps the team, removes blockers', VIO, 'sc6')]
    for i, (n, t_, col, cid) in enumerate(roles):
        E.append(Pop(card(540, 150, col, n, [(t_, TXT)], 38, 30), 100 + i * 590, 460, C[cid]))
    E.append(El(T('Four events in every sprint', 'b', 32, MUTED), 100, 640, C['sc7'], anim='fade'))
    ev = ['Sprint planning', 'Daily scrum · 15 min', 'Sprint review', 'Retrospective']
    for i, n in enumerate(ev):
        E.append(Pop(badge(n, F('b', 32), INK, ACC if i % 2 == 0 else VIO, padx=22, pady=14, r=22), 100 + i * 440, 700, C['sc7'] + 0.5 + i * 0.9))
    E.append(takeaway('Every sprint ends with a usable increment.', 880, C['sc8'], GOOD, 1500))
    return E
def s_kanban(C, D, dur):
    E = head('Kanban', 'Show the work, and limit work in progress.', C['kb1'])
    cols = [('To do', ['Wish list', 'Gift cards'], VIO, 'kb3', 0), ('Doing', ['Search', 'Fix cart bug'], WARN, 'kb3', 0.7), ('Done', ['Browse products'], GOOD, 'kb3', 1.4)]
    for k, (n, items, col, cid, dl) in enumerate(cols):
        x = 100 + k * 570
        E.append(Pop(card(540, 420, col, n, [], 42), x, 340, C[cid] + dl))
        for i, it in enumerate(items):
            E.append(Pop(card(480, 90, col, '', [(it, TXT)], 4, 32), x + 30, 455 + i * 110, C[cid] + dl + 0.4))
    E.append(Pop(badge('Limit: 2', F('b', 32), INK, BAD, padx=20, pady=10, r=20), 940, 352, C['kb4']))
    E.append(Pop(badge('Doing is full: finish something first', F('b', 32), INK, WARN, padx=24, pady=12, r=22), 670, 800, C['kb5']))
    E.append(takeaway('Work keeps flowing, and bottlenecks show early.', 930, C['kb6'], GOOD, 1600))
    return E
def s_devops(C, D, dur):
    E = head('DevOps', 'Carry the code to a running, healthy system.', C['dv1'])
    st = ['Plan', 'Code', 'Build', 'Test', 'Release', 'Deploy', 'Operate', 'Monitor']; cl = [ACC, VIO, GOOD, WARN, PINK, ACC, VIO, GOOD]
    bs = [badge(n, F('b', 30), INK, cl[i], padx=20, pady=10, r=20) for i, n in enumerate(st)]; gap = (1720 - sum(b.width for b in bs)) / (len(bs) - 1); bx = 100
    for i, b in enumerate(bs):
        E.append(Pop(b, int(bx), 340, C['dv3'] + i * 0.4)); bx += b.width + gap
    ideas = [('Shared ownership', 'Developers and operations as one team', ACC, 'dv5'), ('Automation', 'Pipelines build, test, and deploy', VIO, 'dv6'), ('Fast feedback', 'Monitoring shows what users experience', GOOD, 'dv7')]
    for i, (n, t_, col, cid) in enumerate(ideas):
        E.append(Pop(card(540, 190, col, n, [(t_, TXT)], 40, 30), 100 + i * 590, 460, C[cid]))
    E.append(takeaway('A way of working, supported by tools.', 700, C['dv8'], WARN, 1500))
    for i, (nm, lb) in enumerate([('git', 'Git'), ('actions', 'GitHub Actions'), ('docker', 'Docker'), ('kubernetes', 'Kubernetes'), ('prometheus', 'Prometheus')]):
        E.append(logo_c(nm, 160 + i * 215, 790, C['dv9'] + i * 0.3, 100, lb))
    E.append(pill('LATER IN THE BOOTCAMP', 1240, 830, C['dv9'] + 1.6, WARN, INK, 28, 18, 10))
    return E
def s_compare(C, D, dur):
    E = head('Side by side', 'Five ideas, five different jobs.', C['cp1'])
    it = [('Waterfall', 'Stages in strict order', 'Best when: requirements are clear and stable', ACC, 'cp2'),
          ('Agile', 'Small cycles, steady feedback', 'Best when: needs are still changing', VIO, 'cp3'),
          ('Scrum', 'Sprints, roles, and events', 'Best when: one team builds one product', GOOD, 'cp4'),
          ('Kanban', 'A board with work limits', 'Best when: a steady flow of requests', WARN, 'cp5'),
          ('DevOps', 'Dev and ops as one team, with automation', 'Best when: software must keep running and improving', PINK, 'cp6')]
    for i, (n, a, b, col, cid) in enumerate(it):
        E.append(Pop(card(335, 340, col, n, [(a, TXT), (b, MUTED)], 40, 28), 100 + i * 350, 340, C[cid]))
    E.append(takeaway('Not rivals: many teams combine them.', 780, C['cp7'], GOOD, 1500))
    return E
def s_cloudcart(C, D, dur):
    E = head('CloudCart, built both ways', 'Same stages, same goal, different rhythm.', C['cc1'])
    E.append(ill(C['cc1'], 1400, 130))
    for i in range(6): E.append(El(T(f'Month {i + 1}', 'm', 24, MUTED), 330 + i * 240 + 60, 330, C['cc1'] + 0.3, anim='fade'))
    E.append(El(T('Waterfall', 'x', 38, ACC), 100, 430, C['cc2'], anim='fade'))
    segs = [('Requirements', 232, 0, ACC), ('Design', 232, 240, VIO), ('Build', 472, 480, GOOD), ('Test', 232, 960, WARN), ('Release', 232, 1200, PINK)]
    for i, (n, w, dx, col) in enumerate(segs):
        E.append(Pop(card(w, 90, col, '', [(n, TXT)], 4, 28), 330 + dx, 410, C['cc2'] + i * 0.6))
    E.append(Pop(badge('Customers see it: month 6', F('b', 34), INK, WARN, padx=24, pady=12, r=22), 1010, 520, C['cc3']))
    E.append(El(T('Agile', 'x', 38, VIO), 100, 650, C['cc4'], anim='fade'))
    for i, n in enumerate(['Browse', 'Search', 'Order', 'Pay', 'Reviews', 'Wish list']):
        E.append(Pop(card(232, 90, VIO if i % 2 else ACC, '', [(n, TXT)], 4, 28), 330 + i * 240, 630, C['cc4'] + 0.4 + i * 0.5))
    E.append(Pop(badge('Customers see it: month 1', F('b', 34), INK, GOOD, padx=24, pady=12, r=22), 330, 740, C['cc6']))
    E.append(takeaway('Same stages, same goal, different rhythm.', 880, C['cc7'], WARN, 1500))
    return E
def s_choose(C, D, dur):
    E = head('Match the method', 'Which arrangement fits the situation?', C['ch1'])
    E.append(ill(C['ch1'], 1400, 130))
    rows = [('Fixed requirements, strict sign-off', 'Waterfall-style planning', ACC, 'ch2'), ('New product, unclear needs', 'Agile, often Scrum', VIO, 'ch3'),
            ('Steady stream of support requests', 'Kanban', WARN, 'ch4'), ('Keeping the live shop healthy', 'DevOps practices', GOOD, 'ch5')]
    for i, (s, f, col, cid) in enumerate(rows):
        y = 340 + i * 135
        E.append(Pop(card(1000, 100, col, '', [(s, TXT)], 4, 34), 100, y, C[cid]))
        E.append(Pop(badge(f, F('b', 38), INK, col, padx=28, pady=14, r=26), 1180, y + 14, C[cid] + 1.0))
    E.append(takeaway('Real teams mix them, and adjust as they learn.', 920, C['ch6'], WARN, 1600))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Spot them early.', C['my1'])
    it = [('Myth: Agile means no planning', 'Reality: Agile plans all the time, in smaller steps.', WARN, 'my2'), ('Myth: Scrum and Agile are the same', 'Reality: Scrum is one way to practice Agile.', VIO, 'my3'),
          ('Myth: DevOps is a tool or a job title', 'Reality: it is a way of working.', ACC, 'my4'), ('Myth: Waterfall is always wrong', 'Reality: it can fit fixed, well understood requirements.', GOOD, 'my5')]
    for i, (a, b, col, cid) in enumerate(it):
        E.append(Pop(card(840, 210, col, a, [(b, TXT)], 36, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Choose by the situation, not by fashion.', 860, C['my6'], GOOD, 1500))
    return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    for i, (q, cid) in enumerate([('How is Waterfall different from Agile?', 'z2'), ('What are the three roles in a Scrum team?', 'z3'), ('What is the key rule in Kanban?', 'z4'), ('Is DevOps a tool? Explain.', 'z8')]):
        E.append(Pop(card(1720, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 38, maxw=1500), 190, 268 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1720, 100, GOOD, '', [], 4), 100, 710, C['z9']))
    E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC01-O03  ·  SDLC vs Waterfall, Agile, Scrum, Kanban, DevOps', 'b', 32, TXT, maxw=1560), 220, 746, C['z9'] + 0.3, anim='wipe', d=1.6))
    E.append(Pop(badge('PAUSE  ·  answer out loud', F('b', 34), INK, PINK, padx=26, pady=14), 100, 860, C['z5']))
    E.append(El(T('Next: The parts of an application', 'x', 50, ACC), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 1500, 960, C['z7']))
    return E
FN = dict(hook=s_hook, layers=s_layers, waterfall=s_waterfall, agile=s_agile, scrum=s_scrum, kanban=s_kanban, devops=s_devops, compare=s_compare, cloudcart=s_cloudcart, choose=s_choose, myths=s_myths, recap=s_recap)

_GL3 = dict(layers=('grid', ACC), waterfall=('steps', WARN), agile=('loop', ACC), scrum=('people', VIO), kanban=('board', GOOD), devops=('gear', PINK), compare=('swap', ACC), cloudcart=('rocket', WARN), choose=('question', VIO), myths=('eye', GOOD))
def _wrap3(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL3[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL3: FN[_n] = _wrap3(_n, FN[_n])
