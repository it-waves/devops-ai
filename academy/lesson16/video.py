import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 16  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps
_SP = {'DNS': 'D N S', 'TCP': 'T C P', 'HTTP': 'H T T P', 'IP': 'I P', 'GET': 'G E T', 'POST': 'P O S T', 'JSON': 'jason', 'URL': 'U R L', 'nginx': 'engine X', 'curl': 'curl', 'getent': 'get ent', 'localhost': 'local host'}
def _say(cap):
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in _SP) + r')(?![\w-])', lambda m: _SP[m.group(1)], cap)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "Every time you open a website, a request travels across the internet and back."),
  c('h2', "It takes less than a second, but it happens in several clear steps."),
  c('h3', "Today you trace one request, step by step, and watch the steps happen live."),
  c('h4', "Then, when a page will not load, you will know exactly where to look."),
 ]),
 ('journey', [
  c('j1', "Here is the whole journey."), c('j2', "One: you type a name, like shop dot example dot com."),
  c('j3', "Two: DNS turns that name into an IP address."), c('j4', "Three: your browser opens a TCP connection to that address, on a port."),
  c('j5', "Four: it sends an HTTP request."), c('j6', "Five: the server builds a response, often by asking an application."),
  c('j7', "Six: the response travels back, and the page appears."), c('j8', "Each step can fail, and each failure looks different."),
 ]),
 ('dns', [
  c('d1', "Step two: from a name to a number."), c('d2', "Computers connect by IP address, not by name."),
  c('d3', "DNS is the phone book. It turns a name into an address."), c('d4', "If DNS fails, you see: could not resolve host."),
  c('d5', "The first check: can the name be resolved?"),
 ]),
 ('dnsdemo', [
  c('n1', "Let us try a name that this computer has never heard of."),
  c('n2', "Type: curl web:5000/health", "Type: curl, web, colon, five thousand, slash health."),
  c('n3', "Could not resolve host. The name has no address, so the request never even starts."),
  c('n4', "Now we hand curl the address ourselves. Type: curl --resolve web:5000:127.0.0.1 web:5000/health",
    "Now we hand curl the address ourselves. Type: curl, dash dash resolve, web, colon, five thousand, colon, one twenty-seven dot zero dot zero dot one, then web, colon, five thousand, slash health."),
  c('n5', "That option says: when you look for web, use this address."),
  c('n6', "A reply, ok! Once the name had an address, the request reached our application."),
  c('n7', "Your computer already knows one name by itself. Type: getent hosts localhost", "Your computer already knows one name by itself. Type: get ent, hosts, local host."),
  c('n8', "Localhost always means this computer. Its address is one twenty-seven dot zero dot zero dot one."),
 ]),
 ('anatomy', [
  c('a1', "Step four: the HTTP request."), c('a2', "A request has a method, a path, and headers."),
  c('a3', "The method says what to do. GET reads something. POST sends data."), c('a4', "The path says which thing you want."),
  c('a5', "Headers add details, such as which host you mean."), c('a6', "The response comes back with a status code, headers, and a body."),
 ]),
 ('reqdemo', [
  c('r1', "Let us catch a real request. We ask for the health page, and show only the lines we send."),
  c('r2', "Type: curl -sv localhost:5000/health 2>&1 | grep '^>'", "Type: curl, dash s v, local host, colon, five thousand, slash health, then a pipe to grep, for lines starting with a greater-than sign."),
  c('r3', "The first line is the request: method GET, path slash health, protocol HTTP."), c('r4', "Next, the host header: which server we mean."),
  c('r5', "Now the lines that came back. Type: curl -sv localhost:5000/health 2>&1 | grep '^<'", "Now the lines that came back. The same command, but grep for lines starting with a less-than sign."),
  c('r6', "The first line is the status: two hundred, O K."), c('r7', "The content type header says what kind of data follows."),
  c('r8', "And the body itself. Type: curl -s localhost:5000/health", "And the body itself. Type: curl, dash s, local host, colon, five thousand, slash health."),
  c('r9', "A small piece of data that says the status is ok. That is one complete request and response."),
 ]),
 ('status', [
  c('s1', "Step five: the status code."), c('s2', "Read the first digit. It tells you who has the problem."),
  c('s3', "Two hundred range: success."), c('s4', "Three hundred range: go somewhere else."),
  c('s5', "Four hundred range: the request is wrong, such as a page that does not exist."), c('s6', "Five hundred range: the server failed."),
 ]),
 ('statusdemo', [
  c('t1', "Let us ask our application three questions. First: is it healthy? Type: curl -si localhost:5000/health | head -1", "Let us ask our application three questions. First: is it healthy? Type: curl, dash s i, local host, colon, five thousand, slash health, pipe, head, dash one."),
  c('t2', "Two hundred, O K."),
  c('t3', "Now a page that does not exist. Type: curl -si localhost:5000/nope | head -1", "Now a page that does not exist. The same command, with slash nope."),
  c('t4', "Four oh four. The request was wrong."),
  c('t5', "Now a request that makes the application itself fail. Type: curl -si localhost:5000/crash | head -1", "Now a request that makes the application itself fail. The same command, with slash crash."),
  c('t6', "Five hundred. The server failed. Different first digit, different owner of the problem."),
 ]),
 ('appsrv', [
  c('p1', "Who builds the response?"), c('p2', "A web server, like nginx, hands out files and passes other requests along."),
  c('p3', "An application server runs your code. It looks up data and builds the page."),
  c('p4', "Often they sit in a chain: browser, web server, application server, database."),
  c('p5', "A five oh two or five oh three often means the chain is broken in the middle."),
 ]),
 ('tracedemo', [
  c('x1', "We can measure each step of the journey. A small file tells curl what to report. Type: cat timing.txt", "We can measure each step of the journey. A small file tells curl what to report. Type: cat, timing dot t x t."),
  c('x2', "Name lookup, connect, first byte, and total. The backslash n just means a new line."),
  c('x3', "Now run the request with that report. Type: curl -so /dev/null -w @timing.txt localhost:5000/health", "Now run the request with that report. Type: curl, dash s o, dev null, dash w, at timing dot t x t, local host, colon, five thousand, slash health."),
  c('x4', "Every step took a tiny fraction of a second. This is a healthy request."),
  c('x5', "Now a page that is slow. Type: curl -so /dev/null -w @timing.txt localhost:5000/slow", "Now a page that is slow. The same command, with slash slow."),
  c('x6', "Look at first byte. Two seconds! But connect was still tiny."),
  c('x7', "So the network was fine. The delay is inside the application. The timing tells you where to look."),
 ]),
 ('method', [
  c('m1', "Use the trace as a checklist, from the start."), c('m2', "Name not found? That is a DNS problem."),
  c('m3', "Connection refused? Nothing is listening on that port."), c('m4', "A four hundred range code? Fix the request."),
  c('m5', "A five hundred range code? Look at the application and its logs."), c('m6', "Slow? Compare connect with first byte, to find which side is slow."),
 ]),
 ('errors', [
  c('e1', "Match the symptom to the step."), c('e2', "Could not resolve host: DNS."),
  c('e3', "Connection refused: no service on that port."), c('e4', "Four oh four: wrong path."),
  c('e5', "Five hundred: the application failed."), c('e6', "Five oh two or five oh three: the web server cannot reach the application."),
 ]),
 ('myths', [
  c('k1', "Watch out for four common myths."), c('k2', "Myth one: four oh four means the site is down. It means the server answered."),
  c('k3', "Myth two: five hundred errors are the browser's fault. They come from the server."),
  c('k4', "Myth three: slow always means a slow network. The timing may show a slow application."), c('k5', "Myth four: one error code means one cause. Always confirm in the logs."), c('k6', "Trace first, then conclude."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "List the six steps of a request, in order."),
  c('b3', "Explain what DNS does, and show a resolve failure."), c('b4', "Read a request line and a response line with curl dash v."),
  c('b5', "Say who is at fault from the first digit of a status code."), c('b6', "Use the timing report to find a slow step."), c('b7', "Name the first check for each kind of failure."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('y1', "Your turn, in the virtual machine you built."), c('y2', "One: start the Python web server from last time, and fetch it with curl dash v."),
  c('y3', "Two: find the request line and the status line in the output."), c('y4', "Three: ask for a page that does not exist, and read the four oh four."),
  c('y5', "Four: try curl on a made-up name, and read the DNS error."), c('y6', "Five: use the timing report, and write down each number."),
  c('y7', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f1', "Quick check."), c('f2', "Name the six steps of a web request."), c('f3', "What does DNS do?"),
  c('f4', "What does the first digit of a status code tell you?"), c('f8', "How can timing show whether the network or the application is slow?"),
  c('f9', "Objective covered: MC02-O08.", "Objective covered: number eight, in the I T fundamentals masterclass."),
  c('f5', "Pause the video, and answer out loud."), c('f6', "Next: a new masterclass, computer networking."), c('f7', "Subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'x5': 1.5, 'h4': 0.5, 'j8': 0.5, 'd5': 0.5, 'n8': 0.5, 'a6': 0.5, 'r9': 0.5, 's6': 0.5, 't6': 0.5, 'p5': 0.5, 'x7': 0.5, 'm6': 0.5, 'e6': 0.5, 'k6': 0.5, 'b8': 0.5, 'y7': 14.0, 'f5': 10.0}
CHAP = {'journey': 'The whole journey', 'dns': 'DNS: names to numbers', 'dnsdemo': 'Live: DNS', 'anatomy': 'Request and response', 'reqdemo': 'Live: catch a request', 'status': 'Status codes', 'statusdemo': 'Live: 200, 404, 500',
        'appsrv': 'Web and application servers', 'tracedemo': 'Live: time each step', 'method': 'The checklist', 'errors': 'Symptoms and causes', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Fundamentals  ·  Lesson 16', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def trio(E, C, items, ids, y=520, h=230, w=540):
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def photo(path, w, h, col):
    im = Image.open(path).convert('RGB'); im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.5))
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=tuple(col)[:3] + (255,))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=20, fill=255)
    out.paste(im, (6, 6), m); return out
PHOTO = '/home/claude/academy/lesson16/assets/photo_l16_network.jpg'
PHOTO_CREDIT = 'Ethernet cable  ·  Yuri Samoilov  ·  CC BY 2.0  ·  via Wikimedia Commons'
def mono(s, col, size=28):
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', size)
    im = Image.new('RGBA', (int(f.getlength(s)) + 10, size + 16), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), s, font=f, fill=tuple(col)[:3] + (255,)); return im
def chip(s, col, size=40, padx=22, pady=10):
    return badge(s, ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', size), INK, col, padx=padx, pady=pady, r=18)


def _lab(title, sub, first, badge_, steps, mono_steps=True):
    def f(C, D, dur):
        E = head(title, sub, C[first]); E.append(real(C[first] + 0.2, badge_, 1260, 286))
        E.append(Pop(card(1100, 640, ACC, '', [], 4), 100, 330, C[first]))
        n = len(steps); gap = min(120, (1035 - 345) // n); fs_t, fs_s = (30, 25) if n <= 6 else (27, 23)
        for i, (cid, t, sb, col) in enumerate(steps): E.append(Pop(card(560, gap - 12, col, t, [(sb, TXT)], fs_t, fs_s), 1260, 345 + i * gap, C[cid] + 0.2))
        return E
    return f

def trio3(E, C, items, ids, y=330, h=230, w=540): 
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def slide(title, sub, first, items, ids, chips, chip_id, take, take_id, gl):
    def f(C, D, dur):
        E = head(title, sub, C[first]); trio3(E, C, items, ids)
        x = 100
        for i, (s, col) in enumerate(chips):
            ch = chip(s, col, 36, 24, 12); E.append(Pop(ch, x, 640, C[chip_id] + i * 0.4)); x += ch.width + 22
        E.append(takeaway(take, 820, C[take_id], GOOD, 1700)); return E
    return f
def s_hook(C, D, dur):
    E = [El(T('Servers fail in patterns', 'x', 64), 100, 130, C['h1'])]
    if os.path.exists(PHOTO):
        E.append(Pop(photo(PHOTO, 740, 500, ACC), 1080, 250, C['h1']))
        E.append(El(T(PHOTO_CREDIT, 'm', 24, MUTED, maxw=740), 1080, 770, C['h1'] + 0.5, anim='fade'))
    E.append(Pop(card(900, 150, ACC, 'A server', [('A computer others depend on.', TXT)], 46, 36), 100, 250, C['h1']))
    E.append(Pop(card(900, 150, WARN, 'A few parts, clear symptoms', [('Learn the pairs, fix faster.', TXT)], 46, 36), 100, 430, C['h3']))
    bs = [badge(n, F('b', 34), INK, col, padx=26, pady=14, r=26) for n, col in [('CPU', ACC), ('Memory', VIO), ('Disk', GOOD), ('Services', WARN), ('Logs', PINK)]]
    E.append(El(T('Today, live', 'b', 32, MUTED), 100, 640, C['h4'], anim='fade'))
    bx = 100
    for i, b in enumerate(bs): E.append(Pop(b, bx, 700, C['h4'] + 0.3 + i * 0.5)); bx += b.width + 24
    E.append(takeaway('Real commands, real failures, in a safe setup.', 840, C['h4'] + 2.5, GOOD, 1600)); return E
def s_parts(C, D, dur):
    E = head('The main parts', 'What every server is made of.', C['p1'])
    it = [('CPU', 'Does the work', ACC, 'p2'), ('Memory', 'Fast workspace', VIO, 'p3'), ('Disk', 'Long-term storage', GOOD, 'p4'), ('Network', 'Connects to others', WARN, 'p5'), ('Services', 'Wait for requests', PINK, 'p6'), ('Logs', 'The diary', ACC, 'p7')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(takeaway('Each part fails in its own way.', 860, C['p8'], GOOD, 1500)); return E
s_cpu = slide('The CPU', 'It does the work.', 'q1', [('What it does', 'Runs instructions, shared by cores', ACC), ('Symptom', 'Slow, laggy, high load', WARN), ('First check', 'Who is the busiest process?', GOOD)], ['q2', 'q5', 'q6'],
              [('nproc', ACC), ('ps', VIO), ('top', GOOD)], 'q6', 'A hogging process slows everything.', 'q4', 0)
s_mem = slide('Memory', 'The fast workspace.', 's1', [('What it does', 'Holds running programs', VIO), ('Symptom', 'Swapping, slowness, killed programs', WARN), ('First check', 'free -h', GOOD)], ['s2', 's5', 's6'],
              [('free -h', VIO), ('available', GOOD), ('out of memory', BAD)], 's4', 'Out of memory: the kernel kills a program.', 's4', 0)
s_disk = slide('The disk', 'Long-term storage.', 'u1', [('What it does', 'Keeps files, databases, logs', GOOD), ('Symptom', 'No space left on device', BAD), ('First check', 'df, then du', ACC)], ['u2', 'u5', 'u6'],
               [('df -h', GOOD), ('du -sh', ACC)], 'u6', 'A full disk can stop everything.', 'u4', 0)
s_svc = slide('Services and ports', 'Programs that wait for requests.', 'w1', [('Running?', 'The program must be started', ACC), ('Listening?', 'On the right numbered port', VIO), ('Codes', '200 ok · 404 missing · 5xx failed', WARN)], ['w2', 'w3', 'w4'],
              [('ps', ACC), ('ss -ltn', VIO), ('curl -sI', GOOD)], 'w5', 'Running, listening, answering: check all three.', 'w5', 0)
s_logs = slide('Logs', 'The diary of what happened.', 'y1', [('What they hold', 'Requests, errors, starts, stops', PINK), ('Symptom', 'The screen shows nothing', WARN), ('First check', 'tail and grep', GOOD)], ['y3', 'y2', 'y4'],
               [('tail -n', PINK), ('grep', GOOD)], 'y4', 'Do not guess. Read the log first.', 'y5', 0)

def trio3(E, C, items, ids, y=330, h=230, w=540): 
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def slide(title, sub, first, items, ids, chips, chip_id, take, take_id, gl):
    def f(C, D, dur):
        E = head(title, sub, C[first]); trio3(E, C, items, ids)
        x = 100
        for i, (s, col) in enumerate(chips):
            ch = chip(s, col, 36, 24, 12); E.append(Pop(ch, x, 640, C[chip_id] + i * 0.4)); x += ch.width + 22
        E.append(takeaway(take, 820, C[take_id], GOOD, 1700)); return E
    return f

RB = 'REAL RECORDING  ·  Ubuntu 24.04 terminal'
def s_hook(C, D, dur):
    E = [El(T('Follow one request', 'x', 64), 100, 130, C['h1'])]
    if os.path.exists(PHOTO):
        E.append(Pop(photo(PHOTO, 740, 500, ACC), 1080, 250, C['h1']))
        E.append(El(T(PHOTO_CREDIT, 'm', 24, MUTED, maxw=740), 1080, 770, C['h1'] + 0.5, anim='fade'))
    E.append(Pop(card(900, 150, ACC, 'One click', [('Six steps, under a second.', TXT)], 46, 36), 100, 250, C['h2']))
    E.append(Pop(card(900, 150, WARN, 'Each step can fail', [('Each failure looks different.', TXT)], 46, 36), 100, 430, C['h3']))
    bs = [badge(n, F('b', 34), INK, col, padx=26, pady=14, r=26) for n, col in [('DNS', ACC), ('TCP', VIO), ('HTTP', GOOD), ('Status', WARN), ('Timing', PINK)]]
    E.append(El(T('Today, live', 'b', 32, MUTED), 100, 640, C['h4'], anim='fade'))
    bx = 100
    for i, b in enumerate(bs): E.append(Pop(b, bx, 700, C['h4'] + 0.3 + i * 0.5)); bx += b.width + 24
    E.append(takeaway('Trace it, then you know where to look.', 840, C['h4'] + 2.5, GOOD, 1600)); return E
def s_journey(C, D, dur):
    E = head('The whole journey', 'One request, six steps.', C['j1'])
    it = [('1  Name', 'You type shop.example.com', ACC, 'j2'), ('2  DNS', 'Name becomes an IP address', VIO, 'j3'), ('3  TCP', 'Connect to address and port', GOOD, 'j4'),
          ('4  HTTP request', 'Method, path, headers', WARN, 'j5'), ('5  Server', 'Builds the response', PINK, 'j6'), ('6  Response', 'Travels back, page appears', ACC, 'j7')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(takeaway('Each step can fail in its own way.', 860, C['j8'], WARN, 1500)); return E
s_dns = slide('DNS', 'From a name to a number.', 'd1', [('What it does', 'Turns a name into an IP address', ACC), ('Symptom', 'Could not resolve host', BAD), ('First check', 'Can the name be resolved?', GOOD)], ['d2', 'd4', 'd5'],
              [('curl --resolve', ACC), ('getent hosts', VIO)], 'd5', 'DNS is the phone book of the internet.', 'd3', 0)
def s_anatomy(C, D, dur):
    E = head('Request and response', 'The two halves of every exchange.', C['a1'])
    E.append(Pop(card(840, 330, ACC, 'Request', [('GET /health HTTP/1.1', ACC), ('Host: localhost:5000', TXT), ('Method · path · headers', MUTED)], 52, 34), 100, 330, C['a2']))
    E.append(Pop(card(840, 330, GOOD, 'Response', [('HTTP/1.0 200 OK', GOOD), ('Content-Type: application/json', TXT), ('Status · headers · body', MUTED)], 52, 34), 980, 330, C['a6']))
    for i, (n, col, cid) in enumerate([('GET: read', ACC, 'a3'), ('POST: send data', VIO, 'a3'), ('Path: which thing', GOOD, 'a4'), ('Header: details', WARN, 'a5')]):
        E.append(Pop(chip(n, col, 32, 22, 12), 100 + i * 430, 720, C[cid] + (0.6 if i == 1 else 0)))
    E.append(takeaway('Same shape every time.', 860, C['a6'] + 1.0, GOOD, 1500)); return E
def s_status(C, D, dur):
    E = head('Status codes', 'Read the first digit.', C['s1'])
    it = [('2xx', 'Success', GOOD, 's3'), ('3xx', 'Go somewhere else', ACC, 's4'), ('4xx', 'The request is wrong', WARN, 's5'), ('5xx', 'The server failed', BAD, 's6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(410, 260, col, n, [(s, TXT)], 72, 30, True), 100 + i * 437, 340, C[cid]))
    E.append(takeaway('The first digit tells you who owns the problem.', 700, C['s6'] + 0.5, GOOD, 1700)); return E
def s_appsrv(C, D, dur):
    E = head('Web and application servers', 'Who builds the response?', C['p1'])
    it = [('Browser', 'Asks', ACC), ('Web server', 'nginx: files, passes on', VIO), ('App server', 'Runs your code', GOOD), ('Database', 'Stores the data', WARN)]
    for i, (n, s, col) in enumerate(it):
        x = 100 + i * 437; E.append(Pop(card(360, 220, col, n, [(s, TXT)], 40, 28, True), x, 360, C['p2'] if i < 2 else C['p3'] if i == 2 else C['p4']))
        if i < 3: E.append(El(T('→', 'x', 56, MUTED), x + 372, 440, C['p4'], anim='fade'))
    E.append(Pop(card(1720, 150, BAD, '502 · 503', [('The chain is broken in the middle.', TXT)], 46, 36), 100, 640, C['p5']))
    E.append(takeaway('Know which link answered.', 860, C['p5'] + 1.0, GOOD, 1500)); return E
s_dnsdemo = _lab('DNS, live', 'A name needs an address.', 'n1', RB, [('n2', 'curl web:5000/health', 'The name is unknown', ACC), ('n3', 'Could not resolve', 'No address, no request', BAD), ('n4', 'curl --resolve', 'Give the address by hand', WARN), ('n6', '{"status": "ok"}', 'The request got through', GOOD), ('n7', 'getent hosts localhost', 'A name this PC knows', VIO), ('n8', '127.0.0.1', 'Always this computer', PINK)])
s_reqdemo = _lab('Catch a request', 'See the lines on the wire.', 'r1', RB, [('r2', "grep '^>'", 'Lines we send', ACC), ('r3', 'GET /health HTTP/1.1', 'The request line', VIO), ('r5', "grep '^<'", 'Lines that came back', WARN), ('r6', 'HTTP/1.0 200 OK', 'The status line', GOOD), ('r7', 'Content-Type', 'What the body is', PINK), ('r8', 'the body', 'The data itself', ACC)])
s_statusdemo = _lab('200, 404, 500', 'Same app, three answers.', 't1', RB, [('t1', '/health', 'Is it healthy?', ACC), ('t2', '200 OK', 'Success', GOOD), ('t3', '/nope', 'A missing page', VIO), ('t4', '404', 'The request is wrong', WARN), ('t5', '/crash', 'The app fails', PINK), ('t6', '500', 'The server failed', BAD)])
s_tracedemo = _lab('Time each step', 'Find the slow part.', 'x1', RB, [('x1', 'cat timing.txt', 'What to report', ACC), ('x3', 'curl -w @timing.txt', 'Run with the report', VIO), ('x4', 'tiny numbers', 'A healthy request', GOOD), ('x5', '/slow', 'A slow page', WARN), ('x6', 'first byte: 2 s', 'The wait is here', BAD), ('x7', 'connect is tiny', 'App slow, not the network', PINK)])
def s_method(C, D, dur):
    E = head('The checklist', 'Follow the trace from the start.', C['m1'])
    it = [('Name not found', 'DNS problem', ACC, 'm2'), ('Connection refused', 'Nothing listens on that port', VIO, 'm3'), ('4xx', 'Fix the request', WARN, 'm4'), ('5xx', 'App and its logs', BAD, 'm5'), ('Slow', 'Compare connect and first byte', GOOD, 'm6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(takeaway('Work from the start of the journey.', 860, C['m6'] + 1.0, GOOD, 1500)); return E
def s_errors(C, D, dur):
    E = head('Symptoms and causes', 'Match the symptom to the step.', C['e1'])
    it = [('Could not resolve host', 'Step 2: DNS', 'e2', ACC), ('Connection refused', 'Step 3: no service on the port', 'e3', VIO), ('404 Not Found', 'Step 4: wrong path', 'e4', WARN), ('500 Server Error', 'Step 5: the app failed', 'e5', BAD), ('502 / 503', 'Web server cannot reach the app', 'e6', PINK)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 130
        E.append(Pop(card(900, 112, col, '', [(a, TXT)], 4, 34), 100, y, C[cid])); E.append(El(T('→', 'x', 50, MUTED), 1020, y + 25, C[cid] + 0.3, anim='fade')); E.append(Pop(card(700, 112, col, '', [(b, TXT)], 4, 30), 1100, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['k1'])
    it = [('Myth: 404 means site down', 'Reality: the server answered.', WARN, 'k2'), ('Myth: 500 is the browser', 'Reality: it comes from the server.', BAD, 'k3'),
          ('Myth: slow = slow network', 'Reality: timing may show the app.', VIO, 'k4'), ('Myth: one code, one cause', 'Reality: confirm in the logs.', GOOD, 'k5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Trace first, then conclude.', 860, C['k6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['b1'])
    items = [('Lists the six steps in order', 'b2'), ('Explains DNS, shows a failure', 'b3'), ('Reads request and status lines', 'b4'), ('Status digit = who is at fault', 'b5'), ('Finds a slow step with timing', 'b6'), ('First check for each failure', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid]))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['y1'])
    it = [('1  curl -v', 'Fetch your own server', ACC, 'y2'), ('2  Read it', 'Request line, status line', VIO, 'y3'), ('3  404', 'Ask for a missing page', WARN, 'y4'), ('4  DNS', 'Try a made-up name', GOOD, 'y5'), ('5  Timing', 'Write down each number', PINK, 'y6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['y7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f1'])]
    qs = [('Name the six steps of a web request.', 'f2'), ('What does DNS do?', 'f3'), ('What does the first digit of a status code tell you?', 'f4'), ('How can timing show network versus application?', 'f8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f9'] + 0.2))
    E.append(El(T('Objective covered: MC02-O08  ·  trace an HTTP request', 'b', 28, TXT, maxw=960), 220, 748, C['f9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f5']))
    E.append(El(T('Next: a new masterclass, computer networking', 'x', 46, ACC, maxw=1600), 100, 960, C['f6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f7']))
    return E
FN = dict(hook=s_hook, journey=s_journey, dns=s_dns, dnsdemo=s_dnsdemo, anatomy=s_anatomy, reqdemo=s_reqdemo, status=s_status, statusdemo=s_statusdemo, appsrv=s_appsrv, tracedemo=s_tracedemo,
          method=s_method, errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(journey=('steps', ACC), dns=('question', VIO), dnsdemo=('eye', GOOD), anatomy=('doc', ACC), reqdemo=('eye', GOOD), status=('test', GOOD), statusdemo=('eye', GOOD), appsrv=('server', WARN), tracedemo=('eye', GOOD),
           method=('steps', ACC), errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'dnsdemo': [('n3', 1, 1, 4, 560, ''), ('n6', 1, 1, 4, 250, 'it works'), ('n8', 1, 1, 4, 330, '')],
 'reqdemo': [('r3', 1, 1, 4, 330, 'request line'), ('r4', 2, 1, 4, 330, ''), ('r6', 1, 1, 4, 290, 'status'), ('r7', 4, 1, 4, 510, ''), ('r9', 1, 1, 4, 260, '')],
 'statusdemo': [('t2', 1, 1, 4, 275, '2xx success'), ('t4', 1, 1, 4, 350, '4xx: request wrong'), ('t6', 1, 1, 4, 525, '5xx: server failed')],
 'tracedemo': [('x2', 1, 4, 4, 520, ''), ('x4', 1, 4, 4, 335, ''), ('x6', 2, 1, 4, 260, 'tiny'), ('x6', 3, 1, 4, 335, '2 seconds here')],
}
