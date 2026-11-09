import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 2  ·  DEVOPS BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "Imagine your boss says,"), c('h2', "build me a fast online shop."), c('h3', "Sounds simple."), c('h4', "But what does fast mean?"),
  c('h5', "One developer hears: pages load in a blink."), c('h6', "Another hears: orders ship the same day."),
  c('h7', "Both build something."), c('h8', "And neither is what the owner wanted."),
  c('h9', "This is why requirements exist."), c('h10', "In this lesson, you will write requirements that everyone reads the same way."),
 ]),
 ('who', [
  c('w1', "First, ask who needs the system."), c('w2', "These people are called stakeholders."),
  c('w3', "The owner wants sales."), c('w4', "Shoppers want it quick, and easy."), c('w5', "Support staff want clear order records."), c('w6', "The operations team wants something they can run, and fix."),
  c('w7', "Each group cares about different things."), c('w8', "So a good requirement starts with a conversation, not a guess."),
 ]),
 ('story', [
  c('s1', "Teams often write requirements as user stories."), c('s2', "A user story has three parts:"), c('s3', "who,"), c('s4', "what,"), c('s5', "and why."),
  c('s6', "As a shopper,"), c('s7', "I want to search for a product,"), c('s8', "so that I can find it fast."),
  c('s9', "The why matters."), c('s10', "It tells developers what the feature is really for."),
 ]),
 ('accept', [
  c('a1', "A story says what is wanted."), c('a2', "Acceptance criteria say how we know it is done."), c('a3', "A popular way to write them is: given, when, then."),
  c('a4', "Given a shopper on the product page,"), c('a5', "when they search for the word mug,"), c('a6', "then they see only products named mug."),
  c('a7', "Now anyone can check it, and a test can automate it."), c('a8', "If you cannot check it, it is not a requirement yet."),
 ]),
 ('nfr', [
  c('n1', "Now, the how well."), c('n2', "Words like fast, easy, and secure are traps."), c('n3', "They sound clear, but they mean different things to different people."),
  c('n4', "So make them measurable."), c('n5', "Fast becomes: the product list loads in under one second."), c('n6', "Secure becomes: passwords are never stored as plain text."),
  c('n7', "Now there is a number to check, and a rule to test."),
 ]),
 ('types', [
  c('k1', "Non-functional requirements deserve a closer look."), c('k2', "Here are five kinds you will meet again and again."),
  c('k3', "Performance: how fast it responds."), c('k4', "Security: who can do what, and how data is protected."), c('k5', "Reliability: how often it works, and how it recovers."),
  c('k6', "Usability: how easy it is to use."), c('k7', "Maintainability: how easy it is to change, safely."), c('k8', "Each one needs a measurable target, agreed with the owner."),
 ]),
 ('rank', [
  c('m1', "You cannot build everything at once."), c('m2', "So we rank requirements."), c('m3', "A simple method is called MoSCoW.", "A simple method is called moss cow."),
  c('m4', "Must have,"), c('m5', "should have,"), c('m6', "could have,"), c('m7', "and will not have, for now."),
  c('m8', "For CloudCart, placing an order is a must."), c('m9', "A wish list is only a could."), c('m10', "Ranking keeps the first release small, and shippable."),
 ]),
 ('example', [
  c('x1', "Let us follow one requirement, from vague to ready."), c('x2', "Step one. It starts vague: customers should check out quickly."),
  c('x3', "Step two. Turn it into a story: as a shopper, I want to pay in one step, so that I finish my order."),
  c('x4', "Step three. Add criteria: given items in my cart, when I pay with a valid card, then I get an order number."),
  c('x5', "Step four. Add a target: the confirmation appears within two seconds."), c('x6', "Step five. Rank it. This one is a must."),
  c('x7', "Now the team can design it, build it, and test it."),
 ]),
 ('link', [
  c('l1', "Good requirements connect to the rest of the cycle."), c('l2', "Remember this rule from the CloudCart code?"), c('l3', "Quantity must be one to a hundred."),
  c('l4', "A rule like this should start as a written requirement."), c('l5', "Design plans for it, code enforces it, and tests check it."), c('l6', "When a requirement changes, you know what else must change."),
 ]),
 ('devops', [
  c('v1', "DevOps cares about requirements too."), c('v2', "Some requirements are about running the system, not only using it."),
  c('v3', "Can we deploy it without taking the shop offline?"), c('v4', "Can we see it when something breaks?"), c('v5', "Can we roll back a bad release?"), c('v6', "Can we recover if a server is lost?"),
  c('v7', "Ask the operations team early, and these become requirements, not surprises."),
 ]),
 ('mistakes', [
  c('e1', "Watch for four common mistakes."), c('e2', "One: vague words."), c('e3', "Two: no owner, to make the decision."),
  c('e4', "Three: listing features, but forgetting how well they must work."), c('e5', "Four: changing requirements silently."), c('e6', "Write changes down, and tell everyone."),
 ]),
 ('review', [
  c('f1', "Before you accept a requirement, run a quick check."), c('f2', "Is it clear? Would two people read it the same way?"), c('f3', "Is it testable? Can you prove it is met?"),
  c('f4', "Is it one thing, not three requirements in one sentence?"), c('f5', "Does it have an owner who agreed to it?"), c('f6', "Is it written down where everyone can find it?"),
  c('f7', "If any answer is no, fix it before building."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "What three parts make a user story?"), c('z3', "What do given, when, and then describe?"), c('z4', "How do you turn the word fast into something you can test?"), c('z8', "Name two kinds of non-functional requirement."),
  c('z5', "Pause the video, and answer out loud."), c('z6', "Next lesson: Waterfall, Agile, and Kanban."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'k8': 0.5, 'x7': 0.5, 'v7': 0.5, 'f7': 0.5, 'z5': 6.0, 'h8': 0.5, 'w8': 0.5, 's10': 0.5, 'a8': 0.5, 'n7': 0.5, 'm10': 0.5, 'l6': 0.5, 'e6': 0.5}
CHAP = {'types': 'Kinds of non-functional', 'example': 'A worked example', 'devops': 'Requirements and DevOps', 'review': 'The quick check', 'who': 'Stakeholders', 'story': 'User stories', 'accept': 'Acceptance criteria', 'nfr': 'Measurable requirements', 'rank': 'Ranking', 'link': 'Connect to the cycle', 'mistakes': 'Common mistakes', 'recap': 'Quick check'}
def head2(title, sub, t):
    return [El(T('Requirements  ·  Lesson 2', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)

def s_hook(C, D, dur):
    E = [El(T('A vague request', 'x', 64), 100, 130, C['h1'])]
    E.append(Pop(card(780, 150, WARN, 'The boss', [('"Build me a fast online shop."', TXT)], 34), 100, 260, C['h1']))
    E.append(Pop(badge('fast = ?', F('x', 80), INK, WARN, padx=40, pady=18, r=36), 1000, 270, C['h4']))
    E.append(A([(250, 420), (250, 520)], C['h5'] - 0.2, ACC, 6, 24)); E.append(A([(650, 420), (650, 460), (1360, 460), (1360, 520)], C['h6'] - 0.2, VIO, 6, 24))
    E.append(Pop(card(820, 170, ACC, 'Developer A', [('"Fast" means pages load in a blink.', TXT)], 34), 100, 540, C['h5']))
    E.append(Pop(card(820, 170, VIO, 'Developer B', [('"Fast" means orders ship the same day.', TXT)], 34), 1000, 540, C['h6']))
    E.append(Pop(badge('Both built something', F('b', 40), INK, GOOD, padx=30, pady=14, r=26), 100, 770, C['h7']))
    E.append(Pop(badge("Neither is what the owner wanted", F('b', 40), INK, BAD, padx=30, pady=14, r=26), 700, 770, C['h8']))
    E.append(Pop(badge('REQUIREMENTS', F('x', 80), INK, ACC, padx=44, pady=18, r=36), 100, 885, C['h9']))
    E.append(El(T('Everyone reads them the same way.', 'x', 44), 960, 910, C['h10'], anim='fade'))
    E.append(ill(C['h1'], 1400, 130))
    return E
def s_who(C, D, dur):
    E = head2('Who needs the system?', 'Stakeholders: the people who care about the result.', C['w1'])
    E.append(Pop(card(480, 150, GOOD, 'CloudCart', [('our example shop', MUTED)], 44, 28), 720, 540, C['w1']))
    E.append(Pop(badge('Stakeholders', F('b', 34), INK, ACC, padx=24, pady=12, r=22), 740, 700, C['w2']))
    pos = [(100, 360, WARN, 'Owner', 'wants sales', 'w3'), (1220, 360, ACC, 'Shoppers', 'want it quick and easy', 'w4'),
           (100, 700, VIO, 'Support staff', 'want clear order records', 'w5'), (1220, 700, GOOD, 'Operations team', 'want something they can run and fix', 'w6')]
    for x, y, col, who, what, cid in pos:
        E.append(Pop(card(600, 170, col, who, [(what, TXT)], 38, 30), x, y, C[cid]))
    E.append(A([(700, 470), (730, 520)], C['w3'] + 0.5, WARN, 5, 20)) if False else None
    E.append(takeaway('Start with a conversation, not a guess.', 940, C['w8'], WARN, 1500))
    return E
def s_story(C, D, dur):
    E = head2('The user story', 'One sentence with three parts.', C['s1'])
    parts = [('Who', 'As a shopper,', ACC, 's3', 's6'), ('What', 'I want to search for a product,', VIO, 's4', 's7'), ('Why', 'so that I can find it fast.', GOOD, 's5', 's8')]
    for i, (n, ex, col, c1, c2) in enumerate(parts):
        y = 360 + i * 170
        E.append(Pop(badge(f'{i + 1}  {n}', F('x', 46), INK, col, padx=34, pady=18, r=30), 100, y, C[c1]))
        E.append(Pop(card(1180, 120, col, '', [(ex, TXT)], 4, 40), 520, y - 6, C[c2]))
    E.append(takeaway('The why tells developers what the feature is really for.', 900, C['s10'], WARN, 1600))
    return E
def s_accept(C, D, dur):
    E = head2('Acceptance criteria', 'How we know the story is done.', C['a1'])
    rows = [('Given', 'a shopper on the product page', ACC, 'a4'), ('When', 'they search for the word "mug"', VIO, 'a5'), ('Then', 'they see only products named mug', GOOD, 'a6')]
    for i, (k, v, col, cid) in enumerate(rows):
        y = 360 + i * 150
        E.append(Pop(badge(k, F('x', 50), INK, col, padx=36, pady=18, r=30), 100, y, C[cid]))
        E.append(Pop(card(1250, 110, col, '', [(v, TXT)], 4, 40), 440, y - 4, C[cid] + 0.2))
    E.append(Pop(icon('check', 90, TXT, GOOD), 1780, 700, C['a7'])) if False else None
    E.append(Pop(badge('Anyone can check it', F('b', 36), INK, GOOD, padx=26, pady=14, r=24), 100, 830, C['a7']))
    E.append(Pop(badge('A test can automate it', F('b', 36), INK, ACC, padx=26, pady=14, r=24), 600, 830, C['a7'] + 1.0))
    E.append(takeaway("Can't check it? It's not a requirement yet.", 930, C['a8'], WARN, 1600))
    return E
def s_nfr(C, D, dur):
    E = head2('Make "how well" measurable', 'Non-functional requirements need numbers and rules.', C['n1'])
    E.append(ill(C['n6'], 1400, 130))
    vague = ['fast', 'easy', 'secure']
    for i, w in enumerate(vague):
        E.append(Pop(badge(w, F('x', 56), INK, WARN, padx=34, pady=16, r=28), 100 + i * 250, 360, C['n2'] + i * 0.35))
    E.append(El(T('Different meanings for different people', 'm', 32, MUTED, maxw=900), 100, 470, C['n3'], anim='fade'))
    E.append(Pop(badge('Make them measurable', F('x', 54), INK, ACC, padx=34, pady=16, r=28), 100, 560, C['n4']))
    E.append(A([(250, 676), (250, 730)], C['n5'] - 0.3, ACC, 6, 24))
    E.append(Pop(card(840, 150, ACC, 'Fast', [('The product list loads in under 1 second.', TXT)], 34), 100, 745, C['n5']))
    E.append(Pop(card(840, 150, VIO, 'Secure', [('Passwords are never stored as plain text.', TXT)], 34), 980, 745, C['n6']))
    E.append(takeaway('A number to check. A rule to test.', 940, C['n7'], GOOD, 1500))
    return E
def s_rank(C, D, dur):
    E = head2('Rank what you build first', 'MoSCoW: Must, Should, Could, Won\'t (for now).', C['m1'])
    E.append(ill(C['m4'], 1400, 130))
    cols = [('Must', 'Browse products', 'Place an order', GOOD, 'm4'), ('Should', 'Search products', '', ACC, 'm5'), ('Could', 'Wish list', '', VIO, 'm6'), ("Won't (now)", 'Gift cards', '', WARN, 'm7')]
    for i, (n, a, b, col, cid) in enumerate(cols):
        x = 100 + i * 440
        E.append(Pop(card(400, 240, col, n, [(a, TXT)] + ([(b, TXT)] if b else []), 42, 32), x, 360, C[cid]))
    E.append(Pop(badge('Place an order = MUST', F('b', 34), INK, GOOD, padx=26, pady=12, r=22), 100, 640, C['m8']))
    E.append(Pop(badge('Wish list = COULD', F('b', 34), INK, VIO, padx=26, pady=12, r=22), 620, 640, C['m9']))
    E.append(takeaway('A small first release that ships.', 780, C['m10'], WARN, 1500))
    return E
SRC = [('  if (l.quantity() < 1 || l.quantity() > 100) {', WARN), ('    throw new IllegalArgumentException(', WARN), ('      "quantity must be 1 to 100");', WARN), ('  }', TXT)]
def s_link(C, D, dur):
    E = head2('Requirements connect everything', 'One written rule, followed through the cycle.', C['l1'])
    E.append(real(C['l2'], 'REAL FILE  ·  OrderService.java (abridged, from Lesson 1)', 100, 340))
    CX, CY, LH, FS = 100, 400, 50, 30
    E.append(El(term_frame(1100, 280, 'OrderService.java'), CX - 20, CY - 10, C['l2'], anim='fade'))
    for i, (s, col) in enumerate(SRC): E.append(El(T(s, 'mono', FS, col), CX + 10, CY + 50 + i * LH, C['l2'] + 0.3 + i * 0.12, anim='fade', d=0.2))
    E.append(bar(CX - 2, CY + 46, 1050, 3 * LH + 6, C['l3'], C['l3.e'] + 0.2, WARN))
    E.append(Pop(badge('Requirement: quantity must be 1 to 100', F('b', 34), INK, ACC, padx=26, pady=12, r=22), 100, 760, C['l4']))
    steps = [('Design', VIO), ('Code', GOOD), ('Test', WARN)]
    x = 1360
    for i, (n, col) in enumerate(steps):
        E.append(Pop(badge(n, F('b', 36), INK, col, padx=28, pady=14, r=24), x, 450 + i * 130, C['l5'] + i * 0.7))
    E.append(A([(1450, 535), (1450, 575)], C['l5'] + 0.9, MUTED, 5, 18)); E.append(A([(1450, 665), (1450, 705)], C['l5'] + 1.6, MUTED, 5, 18))
    E.append(takeaway('Change the rule, and you know what else changes.', 910, C['l6'], WARN, 1600))
    return E
def s_mistakes(C, D, dur):
    E = head2('Four common mistakes', 'Spot them early.', C['e1'])
    items = [('1', 'Vague words', 'fast, easy, secure', WARN, 'e2'), ('2', 'No owner', 'nobody can decide', ACC, 'e3'), ('3', 'Features only', 'forgetting how well', VIO, 'e4'), ('4', 'Silent changes', 'nobody was told', BAD, 'e5')]
    for i, (n, t, s, col, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 360 + (i // 2) * 210
        E.append(Pop(card(840, 180, col, f'{n}   {t}', [(s, TXT)], 40, 32), x, y, C[cid]))
    E.append(takeaway('Write changes down, and tell everyone.', 840, C['e6'], GOOD, 1500))
    return E

def s_types(C, D, dur):
    E = head2('Five kinds of "how well"', 'Each needs a target you can measure.', C['k1'])
    E.append(ill(C['k3'], 1400, 130))
    it = [('Performance', 'List loads in under 1 second', ACC, 'k3'), ('Security', 'Passwords never stored as plain text', VIO, 'k4'), ('Reliability', 'Checkout works 99.9% of the month', GOOD, 'k5'),
          ('Usability', 'A shopper can order in 3 steps', WARN, 'k6'), ('Maintainability', 'Every change runs automated tests', PINK, 'k7')]
    for i, (n, ex, col, cid) in enumerate(it):
        x = 100 + (i % 3) * 590; y = 360 + (i // 3) * 250
        E.append(Pop(card(560, 220, col, n, [(ex, TXT)], 40, 32), x, y, C[cid]))
    E.append(Pop(badge('Example targets for CloudCart', F('b', 30), INK, EN.WARN, padx=22, pady=10, r=20), 1190 - 0, 640, C['k8'] - 1.0)) if False else None
    E.append(takeaway('Agree a measurable target with the owner.', 880, C['k8'], GOOD, 1500))
    return E
def s_example(C, D, dur):
    E = head2('One requirement, start to finish', 'From vague to ready to build.', C['x1'])
    E.append(ill(C['x2'], 1400, 130))
    rows = [('1  Vague', 'Customers should check out quickly.', WARN, 'x2'), ('2  Story', 'As a shopper, I want to pay in one step, so that I finish my order.', ACC, 'x3'),
            ('3  Criteria', 'Given items in my cart, when I pay with a valid card, then I get an order number.', VIO, 'x4'), ('4  Target', 'The confirmation appears within 2 seconds.', GOOD, 'x5'),
            ('5  Rank', 'MUST have', PINK, 'x6')]
    for i, (n, t_, col, cid) in enumerate(rows):
        y = 320 + i * 125
        E.append(Pop(badge(n, F('x', 38), INK, col, padx=26, pady=12, r=24), 100, y + 6, C[cid]))
        E.append(Pop(card(1330, 100, col, '', [(t_, TXT)], 4, 32), 470, y, C[cid] + 0.2))
    E.append(takeaway('Now the team can design it, build it, and test it.', 960, C['x7'], WARN, 1600))
    return E
def s_devops(C, D, dur):
    E = head2('Requirements and DevOps', 'Some requirements are about running the system.', C['v1'])
    E.append(Pop(badge('OPERATIONAL REQUIREMENTS', F('x', 44), INK, ACC, padx=30, pady=14, r=26), 100, 340, C['v2']))
    it = [('Deploy', 'without taking the shop offline?', ACC, 'v3'), ('Monitor', 'can we see it when something breaks?', VIO, 'v4'), ('Roll back', 'can we undo a bad release?', WARN, 'v5'), ('Recover', 'can we recover if a server is lost?', GOOD, 'v6')]
    for i, (n, q, col, cid) in enumerate(it):
        x = 100 + (i % 2) * 880; y = 470 + (i // 2) * 210
        E.append(Pop(card(840, 180, col, n, [(q, TXT)], 42, 32), x, y, C[cid]))
    E.append(takeaway('Ask operations early. No surprises.', 920, C['v7'], GOOD, 1500))
    return E
def s_review(C, D, dur):
    E = head2('The quick check', 'Run it on every requirement.', C['f1'])
    qs = [('Clear', 'Would two people read it the same way?', ACC, 'f2'), ('Testable', 'Can you prove it is met?', VIO, 'f3'), ('One thing', 'Not three requirements in one sentence', GOOD, 'f4'),
          ('Owned', 'Someone agreed to it', WARN, 'f5'), ('Written down', 'Where everyone can find it', PINK, 'f6')]
    for i, (n, q, col, cid) in enumerate(qs):
        y = 330 + i * 115
        E.append(Pop(card(1720, 95, col, '', [], 4), 100, y, C[cid]))
        E.append(Pop(icon('check', 52, TXT, col), 130, y + 20, C[cid] + 0.15)); E.append(El(T(n, 'x', 38, col), 220, y + 24, C[cid] + 0.1, anim='fade')); E.append(El(T(q, 'm', 34, TXT), 620, y + 26, C[cid] + 0.2, anim='fade'))
    E.append(takeaway('Any answer is no? Fix it before building.', 930, C['f7'], WARN, 1500))
    return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    for i, (q, cid) in enumerate([('What three parts make a user story?', 'z2'), ('What do given, when, and then describe?', 'z3'), ('How do you turn "fast" into something you can test?', 'z4'), ('Name two kinds of non-functional requirement.', 'z8')]):
        E.append(Pop(card(1720, 100, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 270 + i * 125, C[cid])); E.append(El(T(q, 'm', 38, maxw=1500), 190, 292 + i * 125, C[cid] + 0.1, anim='fade'))
    E.append(Pop(badge('PAUSE  ·  answer out loud', F('b', 34), INK, PINK, padx=26, pady=14), 100, 800, C['z5']))
    E.append(El(T('Next: Waterfall, Agile, Kanban', 'x', 56, ACC), 100, 910, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 1450, 920, C['z7']))
    return E
FN = dict(types=s_types, example=s_example, devops=s_devops, review=s_review, hook=s_hook, who=s_who, story=s_story, accept=s_accept, nfr=s_nfr, rank=s_rank, link=s_link, mistakes=s_mistakes, recap=s_recap)
