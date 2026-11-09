import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 9  ·  DEVOPS BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "You open CloudCart in your browser, and a page appears."),
  c('h2', "It feels instant. But five different things just worked together."),
  c('h3', "A client asked. A network carried the question. A server received it."),
  c('h4', "An application did the work, on top of an operating system."),
  c('h5', "Today you learn to tell these five apart, because every outage lives in one of them."),
 ]),
 ('client', [
  c('c1', "First, the client."), c('c2', "A client is whoever asks for something."),
  c('c3', "Your browser is a client."), c('c4', "A phone app is a client."), c('c5', "A script that checks prices is a client."),
  c('c6', "Notice: a client is not a person. It is software making a request."),
  c('c7', "Being a client is a role, not a type of machine."),
 ]),
 ('server', [
  c('s1', "Next, the server."), c('s2', "A server is whoever answers requests."),
  c('s3', "The word has two meanings, and people mix them up."),
  c('s4', "It can mean a program that waits for requests."), c('s5', "It can also mean the machine that runs such a program."),
  c('s6', "Any computer can act as a server, even a laptop."), c('s7', "What makes it a server is the job it does, not how big it is."),
 ]),
 ('app', [
  c('a1', "Now, the application."), c('a2', "An application is a program that does a useful job for people."),
  c('a3', "CloudCart's shop code is an application: it lists products, and takes orders."),
  c('a4', "A database program is an application too, because it stores and finds data."),
  c('a5', "Applications decide what happens. But they cannot run on their own."), c('a6', "They need something underneath."),
 ]),
 ('os', [
  c('o1', "That something is the operating system."), c('o2', "The operating system manages the machine, so applications do not have to."),
  c('o3', "It starts and stops programs."), c('o4', "It shares memory and processor time between them."),
  c('o5', "It stores files, and controls who may open them."), c('o6', "And it handles the connection to the network."),
  c('o7', "Linux, Windows, and macOS are operating systems."), c('o8', "Most servers you will manage run Linux."),
 ]),
 ('stack', [
  c('k1', "Put it together, and one machine is a stack of layers."), c('k2', "At the bottom is hardware: processor, memory, and disks."),
  c('k3', "Above it, the operating system."), c('k4', "Above that, the applications."),
  c('k5', "Your laptop has this stack, and so does the server."), c('k6', "Between the two machines sits the network."),
  c('k7', "The network is simply the connection that lets computers talk."),
 ]),
 ('roles', [
  c('r1', "Here is the idea that confuses beginners: roles change."), c('r2', "Your browser asks the shop for a page. The browser is the client."),
  c('r3', "The shop then asks the database for your order. Now the shop is the client."),
  c('r4', "The database answers. The database is the server."),
  c('r5', "So the shop application is a server to the browser, and a client of the database."),
  c('r6', "Always ask: in this conversation, who asks, and who answers?"),
 ]),
 ('trace', [
  c('t1', "Let us follow one request through all five parts."), c('t2', "One: the browser, the client, sends the request."),
  c('t3', "Two: the network carries it to the server."), c('t4', "Three: the operating system on the server receives it, and hands it to the right program."),
  c('t5', "Four: the shop application builds the page, asking the database when it needs data."),
  c('t6', "Five: the database finds the data, and answers."), c('t7', "Then the reply travels back the same way, and your page appears."),
 ]),
 ('demo', [
  c('e1', "Now let us see this for real, in a disposable Linux sandbox."), c('e2', "These outputs are real captures, not an illustration."),
  c('e3', "First command: the operating system reports that it is Linux."),
  c('e4', "Second: a program is listening on port eight zero eight zero. That is a server, waiting."),
  c('e5', "Third: a client, called curl, asks it for a page. The answer says two hundred, okay."),
  c('e6', "Fourth: we ask a port where nothing is listening."), c('e7', "No answer, and exit code seven: the connection failed."),
  c('e8', "Same client, same network. The difference is whether a server is there to answer."),
 ]),
 ('symptoms', [
  c('m1', "Why does this matter for DevOps?"), c('m2', "Because a symptom points to a layer."),
  c('m3', "Cannot connect at all? Suspect the network, or that nothing is listening."),
  c('m4', "The page loads, but shows an error? Suspect the application."),
  c('m5', "Everything is slow? Suspect the operating system or the hardware running short of resources."),
  c('m6', "The server will not start? Look at the operating system, and the machine."),
  c('m7', "Name the layer first, then investigate it."),
 ]),
 ('myths', [
  c('w1', "Watch out for four common myths."),
  c('w2', "Myth one: a server is a special, big computer. In fact, it is any computer doing the serving job."),
  c('w3', "Myth two: the operating system and the application are the same. In fact, one runs on the other."),
  c('w4', "Myth three: the network is the internet. In fact, your home Wi-Fi, and an office network, are networks too."),
  c('w5', "Myth four: a client is a person. In fact, it is software that asks."), c('w6', "Clear these up, and later topics get easier."),
 ]),
 ('rubric', [
  c('u1', "Here is how you can check your own understanding."), c('u2', "Pick any website you use, and describe one visit."),
  c('u3', "Name the client, and the server."), c('u4', "Name the application, and the operating system."),
  c('u5', "Show the network between them."), c('u6', "Then pick one symptom, and name the layer you would check first."),
  c('u7', "Check yourself on six points."), c('u8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('y1', "Your turn."), c('y2', "Choose a site or an app you use every day."),
  c('y3', "One: draw the five parts for it."), c('y4', "Two: invent one failure, and name the layer it belongs to."),
  c('y5', "Three: mark yourself on the rubric."), c('y6', "Pause the video, and do it now."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "What is the difference between a client and a server?"), c('z3', "What does an operating system do?"),
  c('z4', "Which layers sit inside one machine?"), c('z8', "Name the five parts of a web request."),
  c('z9', "Objective covered: MC02-O01.", "Objective covered: number one, in the I T fundamentals masterclass."),
  c('z5', "Pause the video, and describe one site visit with all five parts."), c('z6', "Next lesson: C P U, memory, storage, and processes."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h5': 0.5, 'c7': 0.5, 's7': 0.5, 'a6': 0.5, 'o8': 0.5, 'k7': 0.5, 'r6': 0.5, 't7': 0.5, 'e8': 0.5, 'm7': 0.5, 'w6': 0.5, 'u8': 0.5, 'y6': 12.0, 'z5': 10.0}
CHAP = {'client': 'The client', 'server': 'The server', 'app': 'The application', 'os': 'The operating system', 'stack': 'The layers', 'roles': 'Roles change', 'trace': 'One request',
        'demo': 'Real demo', 'symptoms': 'Symptoms and layers', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Fundamentals  ·  Lesson 9', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def row3(E, C, items, ids, y=360, h=220, tsize=44, lsize=32):
    for i, (n, s, col) in enumerate(items): E.append(Pop(card(540, h, col, n, [(s, TXT)], tsize, lsize), 100 + i * 590, y, C[ids[i]]))

def s_hook(C, D, dur):
    E = [El(T('What just happened?', 'x', 64), 100, 130, C['h1']), ill(C['h1'], 1400, 130)]
    E.append(Pop(card(1720, 120, WARN, 'You open CloudCart in a browser', [], 46), 100, 260, C['h1']))
    it = [('Client', 'Asks', ACC), ('Network', 'Carries', GOOD), ('Server', 'Answers', WARN)]
    for i, (n, s, col) in enumerate(it):
        E.append(Pop(card(480, 220, col, n, [(s, TXT)], 46, 36), 100 + i * 620, 440, C['h3'] + i * 0.6))
        if i: E.append(A([(100 + i * 620 - 140, 550), (100 + i * 620 - 20, 550)], C['h3'] + i * 0.6, MUTED, 6, 24))
    bs = [badge(n, F('b', 36), INK, col, padx=28, pady=14, r=26) for n, col in [('Application', VIO), ('Operating system', PINK)]]
    gap = 60; bx = 100 + (1720 - (sum(b.width for b in bs) + gap)) / 2
    E.append(El(T('Inside the server', 'b', 32, MUTED), bx, 730, C['h4'], anim='fade'))
    for i, b in enumerate(bs): E.append(Pop(b, bx, 790, C['h4'] + 0.3 + i * 0.6)); bx += b.width + gap
    E.append(takeaway('Five parts. Every outage lives in one of them.', 920, C['h5'] + 0.4, GOOD, 1600))
    return E
def s_client(C, D, dur):
    E = head('The client', 'Whoever asks for something.', C['c1'])
    E.append(Pop(card(1720, 130, ACC, 'Definition', [('Software that sends a request, and waits for an answer.', TXT)], 36, 38), 100, 330, C['c2']))
    it = [('A browser', 'Asks for web pages', 'c3', 'screen'), ('A phone app', 'Asks for your orders', 'c4', 'link'), ('A script', 'Asks for prices, every hour', 'c5', 'code')]
    for i, (n, s, cid, g) in enumerate(it):
        E.append(Pop(card(540, 230, ACC, n, [(s, TXT)], 44, 32, True), 100 + i * 590, 520, C[cid]))
        E.append(Pop(glyph(g, 70, ACC, True), 100 + i * 590 + 235, 660, C[cid] + 0.2))
    E.append(takeaway('A client is a role, played by software.', 860, C['c7'], GOOD, 1600))
    return E
def s_server(C, D, dur):
    E = head('The server', 'Whoever answers requests.', C['s1'])
    E.append(Pop(card(1720, 130, WARN, 'Definition', [('Software that waits for requests, and answers them.', TXT)], 36, 38), 100, 330, C['s2']))
    it = [('Meaning one', 'A program that waits for requests', 's4', 'gear'), ('Meaning two', 'The machine that runs it', 's5', 'server')]
    for i, (n, s, cid, g) in enumerate(it):
        E.append(Pop(card(840, 230, WARN, n, [(s, TXT)], 44, 34), 100 + i * 880, 520, C[cid]))
        E.append(Pop(glyph(g, 70, WARN, True), 100 + i * 880 + 730, 540, C[cid] + 0.2))
    E.append(takeaway('Any computer can serve. The job makes it a server.', 860, C['s7'], GOOD, 1600))
    return E
def s_app(C, D, dur):
    E = head('The application', 'A program that does a useful job.', C['a1'])
    it = [('Shop code', 'Lists products, takes orders', 'a3'), ('Database', 'Stores and finds data', 'a4'), ('Needs a base', 'It cannot run alone', 'a6')]
    cols = [VIO, VIO, BAD]
    for i, (n, s, cid) in enumerate(it): E.append(Pop(card(540, 230, cols[i], n, [(s, TXT)], 44, 32), 100 + i * 590, 400, C[cid]))
    E.append(Pop(card(1720, 150, VIO, 'The application decides what happens', [('The operating system makes it possible.', TXT)], 40, 36), 100, 700, C['a5']))
    E.append(takeaway('Applications need something underneath.', 920, C['a6'] + 0.4, GOOD, 1600))
    return E
def s_os(C, D, dur):
    E = head('The operating system', 'It manages the machine for everyone above it.', C['o1'])
    it = [('Programs', 'Starts and stops them', ACC, 'o3'), ('Resources', 'Shares memory and processor', VIO, 'o4'), ('Files', 'Stores them, controls access', GOOD, 'o5'), ('Network', 'Handles the connection', WARN, 'o6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 170, col, n, [(s, TXT)], 40, 30), 100 + (i % 2) * 880, 330 + (i // 2) * 200, C[cid]))
    E.append(El(T('Examples', 'b', 30, MUTED), 100, 750, C['o7'], anim='fade'))
    bx = 100
    for i, (n, col) in enumerate([('Linux', GOOD), ('Windows', ACC), ('macOS', PINK)]):
        b = badge(n, F('x', 40), INK, col, padx=28, pady=14, r=26); E.append(Pop(b, bx, 800, C['o7'] + 0.2 + i * 0.5)); bx += b.width + 30
    E.append(takeaway('Most servers you manage will run Linux.', 940, C['o8'], GOOD, 1600, 36))
    return E
def s_stack(C, D, dur):
    E = head('The layers', 'One machine is a stack.', C['k1'])
    E.append(El(T('Your laptop  ·  client', 'b', 32, ACC), 100, 330, C['k5'], anim='fade')); E.append(El(T('CloudCart  ·  server', 'b', 32, WARN), 1180, 330, C['k5'], anim='fade'))
    layers = [('Application', VIO, 'k4'), ('Operating system', PINK, 'k3'), ('Hardware', GOOD, 'k2')]
    for i, (n, col, cid) in enumerate(layers):
        t = C[cid] if i else C[cid]
        E.append(Pop(card(640, 120, col, '', [(n, TXT)], 4, 40), 100, 385 + i * 140, t)); E.append(Pop(card(640, 120, col, '', [(n, TXT)], 4, 40), 1180, 385 + i * 140, C['k5'] + 0.3 + i * 0.2))
    E.append(Pop(card(320, 140, ACC, '', [('Network', TXT)], 4, 44), 800, 515, C['k6']))
    E.append(A([(745, 585), (795, 585)], C['k6'] + 0.2, MUTED, 6, 20)); E.append(A([(1125, 585), (1175, 585)], C['k6'] + 0.4, MUTED, 6, 20))
    E.append(takeaway('Same layers on both sides, joined by the network.', 860, C['k7'], GOOD, 1600))
    return E
def s_roles(C, D, dur):
    E = head('Roles change', 'Ask: who asks, and who answers?', C['r1'])
    it = [('Browser', 'Asks the shop', ACC, 'r2'), ('Shop application', 'Asks the database', VIO, 'r3'), ('Database', 'Answers the shop', WARN, 'r4')]
    for i, (n, s, col, cid) in enumerate(it):
        x = 100 + i * 620; E.append(Pop(card(480, 220, col, n, [(s, TXT)], 42, 34), x, 380, C[cid]))
        if i: E.append(A([(x - 140, 490), (x - 20, 490)], C[cid] - 0.1, MUTED, 6, 22))
    E.append(Pop(card(840, 170, ACC, 'To the browser', [('The shop is a server.', TXT)], 40, 36), 100, 680, C['r5']))
    E.append(Pop(card(840, 170, VIO, 'To the database', [('The same shop is a client.', TXT)], 40, 36), 980, 680, C['r5'] + 0.8))
    E.append(takeaway('Roles belong to a conversation, not to a machine.', 920, C['r6'], GOOD, 1600, 36))
    return E
def s_trace(C, D, dur):
    E = head('One request, five parts', 'From click to page.', C['t1']); E.append(ill(C['t1'], 1400, 130))
    it = [('1  Browser', 'Client sends it', ACC, 't2'), ('2  Network', 'Carries it', GOOD, 't3'), ('3  OS', 'The operating system hands it on', PINK, 't4'), ('4  Application', 'Builds the page', VIO, 't5'), ('5  Database', 'Finds the data', WARN, 't6')]
    for i, (n, s, col, cid) in enumerate(it):
        x = 100 + i * 350; E.append(Pop(card(290, 260, col, n, [(s, TXT)], 36, 30, True), x, 420, C[cid]))
        if i: E.append(A([(x - 54, 550), (x - 8, 550)], C[cid] - 0.1, MUTED, 5, 18))
    E.append(Pop(card(1720, 170, GOOD, 'The reply', [('Travels back the same way, and your page appears.', TXT)], 44, 40), 100, 740, C['t7']))
    return E
def term_lines(x, y, rows, t0, t1s):
    pass
def s_demo(C, D, dur):
    E = head('Real demo', 'Five parts, seen in a Linux sandbox.', C['e1']); E.append(real(C['e2'], 'REAL OUTPUT  ·  captured in a Linux sandbox', 1260, 296))
    E.append(Pop(card(1100, 600, ACC, '', [], 4), 100, 330, C['e1'] + 0.3))
    blocks = [('e3', [('$ uname -sr', ACC), ('Linux 6.18.44-fc-v310', TXT)]),
              ('e4', [('$ ss -ltn | grep 8080', ACC), ('LISTEN 127.0.0.1:8080', TXT)]),
              ('e5', [('$ curl -i http://127.0.0.1:8080/ | head -n 4', ACC), ('HTTP/1.0 200 OK', GOOD), ('Server: SimpleHTTP/0.6 Python/3.13.18', TXT), ('Date: Mon, 09 Nov 2026 23:18:11 GMT', TXT), ('Content-type: text/html', TXT)]),
              ('e6', [('$ curl http://127.0.0.1:9090/', ACC), ('(no output)   exit code 7', BAD)])]
    ys = [375, 480, 585, 810]
    for (cid, lines), y in zip(blocks, ys):
        for j, (s, col) in enumerate(lines): E.append(El(T(s, 'm', 30, col, maxw=1020), 140, y + j * 40, C[cid] + j * 0.5, anim='fade'))
    ann = [('Operating system', 'Linux is running', PINK, 'e3', 375), ('Server', 'A program is listening', WARN, 'e4', 480), ('Client and server', '200 OK: it answered', GOOD, 'e5', 585), ('No server', 'Nothing was listening', BAD, 'e7', 800)]
    for n, s, col, cid, y in ann: E.append(Pop(card(560, 90, col, '', [(n + ': ' + s, TXT)], 4, 26), 1260, y, C[cid]))
    return E
def s_symptoms(C, D, dur):
    E = head('Symptoms point to layers', 'Name the layer, then investigate.', C['m1'])
    it = [('Cannot connect', 'Network, or nothing is listening', ACC, 'm3'), ('Page loads with an error', 'The application', VIO, 'm4'),
          ('Everything is slow', 'Operating system or hardware: short of resources', WARN, 'm5'), ('Server will not start', 'Operating system, or the machine', BAD, 'm6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s, TXT)], 40, 30), 100 + (i % 2) * 880, 330 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Layer first. Then the investigation.', 860, C['m7'], GOOD, 1500))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['w1'])
    it = [('Myth: a server is a special computer', 'Reality: any computer doing the serving job.', WARN, 'w2'), ('Myth: the OS and the app are the same', 'Reality: one runs on the other.', BAD, 'w3'),
          ('Myth: the network is the internet', 'Reality: Wi-Fi and office networks count too.', VIO, 'w4'), ('Myth: a client is a person', 'Reality: it is software that asks.', GOOD, 'w5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Clear these up, and later topics get easier.', 860, C['w6'], GOOD, 1500))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['u1'])
    items = [('Names the client', 'u3'), ('Names the server', 'u3'), ('Names the application', 'u4'), ('Names the operating system and its job', 'u4'), ('Shows the network between them', 'u5'), ('Names the layer for one symptom', 'u6')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid] + (i % 2) * 0.5))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + (i % 2) * 0.5 + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['u8']))
    return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Take apart a site you use every day.', C['y1'])
    E.append(Pop(card(1720, 150, WARN, 'Choose any site or app', [('Email, a video site, a shop, a game.', TXT)], 46, 40), 100, 330, C['y2']))
    it = [('1  Draw it', 'Client, network, server, application, operating system', ACC, 'y3'), ('2  Break it', 'Invent one failure, name the layer', VIO, 'y4'), ('3  Check it', 'Mark yourself on the rubric', GOOD, 'y5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 270, col, n, [(s, TXT)], 44, 32, True), 100 + i * 590, 540, C[cid]))
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['y6']))
    return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    qs = [('What is the difference between a client and a server?', 'z2'), ('What does an operating system do?', 'z3'), ('Which layers sit inside one machine?', 'z4'), ('Name the five parts of a web request.', 'z8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 32, maxw=930), 190, 280 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['z9']))
    E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC02-O01  ·  Client, server, app, OS, network', 'b', 30, TXT, maxw=960), 220, 748, C['z9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  describe one site visit', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['z5']))
    E.append(El(T('Next: CPU, memory, storage, processes', 'x', 46, ACC, maxw=1500), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['z7']))
    return E
FN = dict(hook=s_hook, client=s_client, server=s_server, app=s_app, os=s_os, stack=s_stack, roles=s_roles, trace=s_trace, demo=s_demo, symptoms=s_symptoms, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(client=('screen', ACC), server=('server', WARN), app=('code', VIO), os=('gear', PINK), stack=('grid', GOOD), roles=('swap', ACC), trace=('link', PINK), demo=('eye', GOOD), symptoms=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105 if name != 'demo' else 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
