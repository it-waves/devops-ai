import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 19  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

# ---- speech helpers ----
_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = {'TCP': 'T C P', 'UDP': 'U D P', 'SSH': 'S S H', 'DNS': 'D N S', 'TLS': 'T L S', 'URL': 'U R L', 'CA': 'C A', 'openssl': 'open S S L',  'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'SYN': 'sin', 'SYN-ACK': 'sin ack', 'ACK': 'ack', 'ESTAB': 'E S T A B',
       'ESTABLISHED': 'established', 'TIME-WAIT': 'time wait', 'UNCONN': 'unconnected', 'nc': 'n c', 'ss': 's s', 'curl': 'curl', 'localhost': 'local host'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "Every time you open a web page, your browser asks a question, and a server gives an answer."),
  c('h2', "That conversation has strict rules. A request goes out. A response comes back, with a number that says how it went."),
  c('h3', "Today you learn those rules: methods, status codes, headers, and how HTTPS keeps the conversation private."),
  c('h4', "You will send real requests, read real answers, and inspect a real certificate."),
 ]),
 ('request', [
  c('r1', "First, the shape of a web conversation."), c('r2', "The client sends a request. It has a method, a path, and headers."),
  c('r3', "The server sends a response. It has a status code, headers, and a body."),
  c('r4', "The body is the page, or the data, that you asked for."),
  c('r5', "Everything in web work, from browsers to A P I calls, is this same exchange."),
 ]),
 ('methods', [
  c('m1', "The method says what you want to do."),
  c('m2', "GET: read something. It should never change anything."),
  c('m3', "POST: send new data, like submitting a form."),
  c('m4', "PUT: replace something that already exists."),
  c('m5', "DELETE: remove something."),
  c('m6', "Safe reading is GET. Anything that changes data uses another method."),
 ]),
 ('methoddemo', [
  c('d1', "Let us send a real request to a small web server on this computer. Type: curl -i localhost:8080",
    "Let us send a real request to a small web server on this computer. Type: curl, dash i, local host, colon, eighty eighty."),
  c('d2', "The first line is the status line. H T T P one point one, status two hundred, O K."),
  c('d3', "Then the headers: the server name, the date, and the type and size of the body."),
  c('d4', "And below, a blank line, then the body: hello from the lab."),
  c('d5', "Now a POST that sends data. Type: curl -s -X POST -d name=ana localhost:8080/form",
    "Now a POST that sends data. Type: curl, dash s, dash capital X, post, dash d, name equals ana, local host, colon, eighty eighty, slash form."),
  c('d6', "The server answers: created name equals ana. The data went in the body of the request."),
 ]),
 ('status', [
  c('s1', "The status code tells you how it went. It is a three-digit number, and the first digit is the family."),
  c('s2', "Two hundred family: success. Two hundred is O K."),
  c('s3', "Three hundred family: go somewhere else. Three oh one means moved permanently."),
  c('s4', "Four hundred family: your request was wrong. Four oh four, not found. Four oh three, forbidden."),
  c('s5', "Five hundred family: the server failed. Five hundred is a server error."),
  c('s6', "Remember: four is you, five is them."),
 ]),
 ('statusdemo', [
  c('t1', "Let us ask for a page that does not exist. Type: curl -sI localhost:8080/missing | head -1",
    "Let us ask for a page that does not exist. Type: curl, dash s capital I, local host, colon, eighty eighty, slash missing, pipe, head, dash one."),
  c('t2', "Four oh four, not found. The server is fine. The request was wrong."),
  c('t3', "Now a page that has moved. Type: curl -sI localhost:8080/old | grep -i \"^HTTP\\|^loc\"",
    "Now a page that has moved. Type: curl, dash s capital I, local host, colon, eighty eighty, slash old, pipe, grep, dash i, then the pattern for the status line and the location line."),
  c('t4', "Three oh one, with a Location header. It tells the browser where to go next."),
  c('t5', "And a server that fails. Type: curl -sI localhost:8080/boom | head -1",
    "And a server that fails. Type: curl, dash s capital I, local host, colon, eighty eighty, slash boom, pipe, head, dash one."),
  c('t6', "Five hundred. This time the problem is on the server side."),
 ]),
 ('headers', [
  c('a1', "Headers are small labelled notes that travel with every request and response."),
  c('a2', "Content-Type says what the body is: text, a web page, or data."),
  c('a3', "Content-Length says how big the body is."),
  c('a4', "Location says where to go next, after a redirect."),
  c('a5', "Authorization carries your proof of identity, and Cookie carries your session."),
  c('a6', "When something fails, the headers often tell you why."),
 ]),
 ('https', [
  c('x1', "Plain H T T P has a problem."), c('x2', "Anyone on the path between you and the server can read it, or change it."),
  c('x3', "H T T P S adds a lock. It runs the same conversation inside T L S."),
  c('x4', "T L S does two jobs. It encrypts the traffic, and it proves who the server is."),
  c('x5', "The padlock in your browser means the connection is encrypted and the server was verified. It does not mean the site is honest."),
 ]),
 ('certs', [
  c('c1', "How does the server prove who it is? With a certificate."),
  c('c2', "A certificate says: this public key belongs to this name."),
  c('c3', "It is signed by a certificate authority that your computer already trusts."),
  c('c4', "Your computer checks three things. The name matches. The signature is trusted. And it has not expired."),
  c('c5', "If any check fails, the connection is refused. That is a good thing."),
 ]),
 ('tlsdemo', [
  c('l1', "Now a secure server on this computer, with a certificate we made ourselves. Type: curl -sSI https://localhost:8443 2>&1 | head -1",
    "Now a secure server on this computer, with a certificate we made ourselves. Type: curl, dash s, capital S, capital I, H T T P S, local host, colon, eighty four forty-three, then show only the first line."),
  c('l2', "Certificate problem: self-signed. No trusted authority signed it, so curl refuses. Exit code sixty."),
  c('l3', "To look at the page anyway, we can switch the check off with dash k. Only do that in a lab. Type: curl -skI https://localhost:8443 | head -1",
    "To look at the page anyway, we can switch the check off with dash k. Only do that in a lab. Type: curl, dash s, k, capital I, H T T P S, local host, colon, eighty four forty-three, pipe, head, dash one."),
  c('l4', "Two hundred, O K. The connection works, but we skipped the safety check."),
  c('l5', "Now read the certificate itself. Type: openssl x509 -in tls/cert.pem -noout -subject -dates",
    "Now read the certificate itself. Type: open S S L, x five oh nine, dash in, T L S slash cert dot pem, dash noout, dash subject, dash dates."),
  c('l6', "The subject is the name it vouches for. And two dates: not before, and not after. That is its lifetime."),
 ]),
 ('errors', [
  c('e1', "Match the symptom to the cause."), c('e2', "Four oh four: wrong path. Check the address you typed."),
  c('e3', "Five hundred: the server broke. Read the server logs."), c('e4', "Certificate problem: the name, the date, or the signer is wrong."),
  c('e5', "Too many redirects: two rules send you back and forth."), c('e6', "Connection refused or timed out: that is not H T T P at all. Go back to ports and firewalls."),
 ]),
 ('myths', [
  c('y1', "Watch out for four myths."), c('y2', "Myth one: the padlock means the site is safe. It means the connection is private."),
  c('y3', "Myth two: a four hundred error is the server's fault. Four hundred is the request's fault."),
  c('y4', "Myth three: dash k fixes certificate errors. It only hides them."),
  c('y5', "Myth four: GET and POST are just two names for the same thing. They have different rules."), c('y6', "Read the status code first."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Name the parts of a request and a response."),
  c('b3', "Choose the right method for a job."), c('b4', "Say what each status family means."),
  c('b5', "Read a status line and a header with curl."), c('b6', "Explain what H T T P S and a certificate add."), c('b7', "Explain why a certificate can fail."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in the virtual machine you built."),
  c('z2', "One: pick any public site, and run curl -I on its address. Read the status line.", "One: pick any public site, and run curl, dash capital I, on its address. Read the status line."),
  c('z3', "Two: add a path that does not exist, and find the four oh four."),
  c('z4', "Three: run curl -v on an H T T P S address, and find the line about the certificate.", "Three: run curl, dash v, on an H T T P S address, and find the line about the certificate."),
  c('z5', "Four: use curl with dash L, to follow a redirect, and see where it ends."), c('z6', "Five: find the expiry date with openssl s client, or in your browser's padlock."),
  c('z7', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f1', "Quick check."), c('f2', "What are the parts of a request and a response?"), c('f3', "What does each status family mean?"),
  c('f4', "What two jobs does T L S do?"), c('f8', "Why would a certificate be refused?"),
  c('f9', "Objective covered: MC03-O03.", "Objective covered: number three, in the computer networking masterclass."),
  c('f5', "Pause the video, and answer out loud."), c('f6', "Next: names, D N S, and a request from start to finish."), c('f7', "Subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h4': 0.5, 'r5': 0.5, 'm6': 0.5, 'd6': 0.5, 's6': 0.5, 't6': 0.5, 'a6': 0.5, 'x5': 0.5, 'c5': 0.5, 'l6': 0.5, 'e6': 0.5, 'y6': 0.5, 'b8': 0.5, 'z7': 14.0, 'f5': 10.0}
CHAP = {'request': 'Requests and responses', 'methods': 'Methods', 'methoddemo': 'Live: GET and POST', 'status': 'Status codes', 'statusdemo': 'Live: 404, 301, 500', 'headers': 'Headers', 'https': 'HTTPS and TLS',
        'certs': 'Certificates', 'tlsdemo': 'Live: a certificate', 'errors': 'Symptoms and causes', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Networking  ·  Lesson 19', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
def mono(s, col, size=28):
    f = ImageFont.truetype(MONO, size)
    im = Image.new('RGBA', (int(f.getlength(s)) + 10, size + 16), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), s, font=f, fill=tuple(col)[:3] + (255,)); return im
def chip(s, col, size=40, padx=22, pady=10):
    return badge(s, ImageFont.truetype(MONO, size), INK, col, padx=padx, pady=pady, r=18)
def door_art(w=740, h=500):
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out); col = tuple(ACC)[:3]
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=col + (255,)); d.rounded_rectangle([6, 6, w + 5, h + 5], radius=20, fill=(12, 30, 34, 255))
    d.rounded_rectangle([60, 110, w - 50, h - 30], radius=14, fill=(226, 234, 236, 255))
    d.rounded_rectangle([60, 60, w - 50, 130], radius=14, fill=(70, 90, 96, 255))
    f = ImageFont.truetype(MONO, 34); d.text((90, 76), '192.168.1.25', font=f, fill=col + (255,))
    nums = ['22', '53', '80', '443']; cols = [tuple(ACC)[:3], tuple(VIO)[:3], tuple(GOOD)[:3], tuple(WARN)[:3]]; fn = ImageFont.truetype(MONO, 40)
    for i, n in enumerate(nums):
        x = 100 + i * 140
        d.rounded_rectangle([x, 220, x + 100, h - 30], radius=10, fill=cols[i] + (255,)); d.ellipse([x + 74, 330, x + 88, 344], fill=(30, 40, 44, 255))
        d.text((x + 50 - fn.getlength(n) / 2, 160), n, font=fn, fill=(20, 30, 34, 255))
    return out
def _lab(title, sub, first, badge_, steps):
    def f(C, D, dur):
        E = head(title, sub, C[first]); E.append(real(C[first] + 0.2, badge_, 1260, 286))
        E.append(Pop(card(1100, 640, ACC, '', [], 4), 100, 330, C[first]))
        n = len(steps); gap = min(120, (1035 - 345) // n); fs_t, fs_s = (30, 25) if n <= 6 else (27, 23)
        for i, (cid, t, sb, col) in enumerate(steps): E.append(Pop(card(560, gap - 12, col, t, [(sb, TXT)], fs_t, fs_s), 1260, 345 + i * gap, C[cid] + 0.2))
        return E
    return f
def grid6(E, C, it, y0=330):
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, y0 + (i // 3) * 245, C[cid]))

RB = 'REAL RECORDING  ·  Ubuntu 24.04 terminal'
def s_hook(C, D, dur):
    E = [El(T('Every web page is a question and an answer', 'x', 60), 100, 130, C['h1'])]
    E.append(Pop(card(740, 200, ACC, 'Request', [('GET /  →', TXT)], 46, 40), 1080, 260, C['h2'])); E.append(Pop(card(740, 200, GOOD, 'Response', [('←  200 OK', TXT)], 46, 40), 1080, 500, C['h2'] + 2.0))
    E.append(Pop(card(900, 150, ACC, 'Methods and status codes', [('What was asked, how it went.', TXT)], 42, 34), 100, 250, C['h3']))
    E.append(Pop(card(900, 150, WARN, 'HTTPS and certificates', [('Private, and verified.', TXT)], 42, 34), 100, 430, C['h3'] + 1.5))
    E.append(takeaway('Read any web error with confidence.', 840, C['h4'], GOOD, 1600)); return E
def s_request(C, D, dur):
    E = head('Requests and responses', 'One exchange, over and over.', C['r1'])
    E.append(Pop(card(840, 420, ACC, 'Request  →', [('Method  GET', TXT), ('Path  /index', TXT), ('Headers', TXT)], 46, 38), 100, 330, C['r2']))
    E.append(Pop(card(840, 420, GOOD, '←  Response', [('Status  200 OK', TXT), ('Headers', TXT), ('Body  the page or data', TXT)], 46, 38), 980, 330, C['r3']))
    E.append(takeaway('Browsers and APIs use the same exchange.', 840, C['r5'], GOOD, 1700)); return E
def s_methods(C, D, dur):
    E = head('Methods', 'What do you want to do?', C['m1'])
    it = [('GET', 'Read', GOOD, 'm2'), ('POST', 'Create / send', ACC, 'm3'), ('PUT', 'Replace', VIO, 'm4'), ('DELETE', 'Remove', BAD, 'm5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(410, 260, col, n, [(s, TXT)], 56, 38, True), 100 + i * 437, 330, C[cid]))
    E.append(takeaway('GET only reads. The others change things.', 700, C['m6'], GOOD, 1700)); return E
s_methoddemo = _lab('GET and POST, live', 'Real requests, real answers.', 'd1', RB, [('d1', 'curl -i localhost:8080', 'A GET request', ACC), ('d2', 'HTTP/1.1 200 OK', 'The status line', GOOD), ('d3', 'Headers', 'Server, date, type, size', VIO), ('d4', 'The body', 'hello from the lab', WARN), ('d5', 'curl -X POST -d …', 'A POST with data', PINK), ('d6', 'created name=ana', 'The server got it', GOOD)])
def s_status(C, D, dur):
    E = head('Status codes', 'How did it go?', C['s1'])
    it = [('2xx', 'Success', GOOD, 's2'), ('3xx', 'Go elsewhere', ACC, 's3'), ('4xx', 'Your request', WARN, 's4'), ('5xx', 'Their server', BAD, 's5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(410, 260, col, n, [(s, TXT)], 72, 38, True), 100 + i * 437, 330, C[cid]))
    for i, (s, cid) in enumerate([('200  OK', 's2'), ('301  Moved', 's3'), ('404  Not found', 's4'), ('500  Server error', 's5')]): E.append(Pop(chip(s, [GOOD, ACC, WARN, BAD][i], 28, 18, 10), 100 + i * 437, 640, C[cid] + 0.6))
    E.append(takeaway('Four is you. Five is them.', 790, C['s6'], GOOD, 1500)); return E
s_statusdemo = _lab('Status codes, live', '404, 301 and 500.', 't1', RB, [('t1', 'curl …/missing', 'A page that is not there', ACC), ('t2', '404 Not Found', 'The request was wrong', WARN), ('t3', 'curl …/old', 'A page that moved', VIO), ('t4', '301 + Location', 'Go here instead', GOOD), ('t5', 'curl …/boom', 'A failing server', PINK), ('t6', '500', 'Their side', BAD)])
def s_headers(C, D, dur):
    E = head('Headers', 'Small labelled notes.', C['a1'])
    it = [('Content-Type', 'What the body is', ACC, 'a2'), ('Content-Length', 'How big it is', VIO, 'a3'), ('Location', 'Where to go next', GOOD, 'a4'), ('Authorization / Cookie', 'Who you are', WARN, 'a5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, n, [(s, TXT)], 40, 34), 100 + (i % 2) * 880, 330 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Headers often tell you why it failed.', 840, C['a6'], GOOD, 1700)); return E
def s_https(C, D, dur):
    E = head('HTTPS and TLS', 'The same conversation, with a lock.', C['x1'])
    E.append(Pop(card(840, 330, BAD, 'HTTP', [('Readable by anyone on the path', TXT), ('Can be changed on the way', TXT)], 52, 34), 100, 330, C['x2']))
    E.append(Pop(card(840, 330, GOOD, 'HTTPS  =  HTTP inside TLS', [('Encrypts the traffic', TXT), ('Proves who the server is', TXT)], 44, 34), 980, 330, C['x3']))
    E.append(takeaway('The padlock means private, not honest.', 760, C['x5'], WARN, 1700)); return E
def s_certs(C, D, dur):
    E = head('Certificates', 'How a server proves who it is.', C['c1'])
    E.append(Pop(card(540, 300, ACC, 'The certificate', [('This key belongs', TXT), ('to this name', TXT)], 44, 36), 100, 330, C['c2']))
    E.append(Pop(card(540, 300, VIO, 'Signed by a CA', [('Your computer', TXT), ('already trusts it', TXT)], 44, 36), 670, 330, C['c3']))
    E.append(Pop(card(540, 300, GOOD, 'Three checks', [('Name matches', TXT), ('Signature trusted', TXT), ('Not expired', TXT)], 44, 34), 1240, 330, C['c4']))
    E.append(takeaway('If a check fails, the connection is refused.', 740, C['c5'], GOOD, 1700)); return E
s_tlsdemo = _lab('A certificate, live', 'Refused, bypassed, and inspected.', 'l1', RB, [('l1', 'curl https://…', 'A self-signed server', ACC), ('l2', 'certificate problem', 'Not trusted, exit 60', BAD), ('l3', 'curl -k https://…', '-k skips the check', WARN), ('l4', '200 OK', 'Works, but unchecked', PINK), ('l5', 'openssl x509 …', 'Read the certificate', VIO), ('l6', 'subject + dates', 'Name and lifetime', GOOD)])
def s_errors(C, D, dur):
    E = head('Symptoms and causes', 'Match the symptom to the cause.', C['e1'])
    it = [('404 Not Found', 'Wrong path or address', 'e2', WARN), ('500 Server error', 'The server broke: read its logs', 'e3', BAD), ('Certificate problem', 'Name, date, or signer is wrong', 'e4', VIO), ('Too many redirects', 'Two rules loop back and forth', 'e5', ACC), ('Refused / timed out', 'Not HTTP: ports or firewall', 'e6', GOOD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 130
        E.append(Pop(card(700, 112, col, '', [(a, TXT)], 4, 34), 100, y, C[cid])); E.append(El(T('→', 'x', 50, MUTED), 830, y + 25, C[cid] + 0.3, anim='fade')); E.append(Pop(card(880, 112, col, '', [(b, TXT)], 4, 28), 920, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['y1'])
    it = [('Myth: padlock = safe site', 'Reality: the link is private.', WARN, 'y2'), ('Myth: 4xx is the server’s fault', 'Reality: the request was wrong.', BAD, 'y3'),
          ('Myth: -k fixes certificates', 'Reality: it only hides the error.', VIO, 'y4'), ('Myth: GET equals POST', 'Reality: different rules.', GOOD, 'y5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Read the status code first.', 860, C['y6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['b1'])
    items = [('Parts of a request and response', 'b2'), ('Pick the right method', 'b3'), ('What each status family means', 'b4'), ('Read a status line and header', 'b5'), ('What HTTPS and a certificate add', 'b6'), ('Why a certificate can fail', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['z1'])
    it = [('1  Status', 'curl -I a public site', ACC, 'z2'), ('2  Not found', 'Add a path that is missing', VIO, 'z3'), ('3  Certificate', 'curl -v on an https address', WARN, 'z4'), ('4  Redirect', 'curl -L follows it', GOOD, 'z5'), ('5  Expiry', 'openssl or the padlock', PINK, 'z6')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f1'])]
    qs = [('Parts of a request and a response?', 'f2'), ('What does each status family mean?', 'f3'), ('What two jobs does TLS do?', 'f4'), ('Why is a certificate refused?', 'f8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f9'] + 0.2))
    E.append(El(T('Objective covered: MC03-O03  ·  HTTP, status codes, HTTPS, TLS', 'b', 28, TXT, maxw=960), 220, 748, C['f9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f5']))
    E.append(El(T('Next: names, DNS, and a request end to end', 'x', 46, ACC, maxw=1600), 100, 960, C['f6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f7']))
    return E
FN = dict(hook=s_hook, request=s_request, methods=s_methods, methoddemo=s_methoddemo, status=s_status, statusdemo=s_statusdemo, headers=s_headers, https=s_https, certs=s_certs, tlsdemo=s_tlsdemo,
          errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(request=('swap', ACC), methods=('steps', VIO), methoddemo=('eye', GOOD), status=('tag', WARN), statusdemo=('eye', GOOD), headers=('doc', ACC), https=('test', GOOD), certs=('doc', VIO), tlsdemo=('eye', GOOD),
           errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'methoddemo': [('d2', 1, 1, 4, 235, ''), ('d3', 2, 4, 4, 540, ''), ('d4', 7, 1, 4, 280, ''), ('d6', 1, 1, 4, 250, '')],
 'statusdemo': [('t2', 1, 1, 4, 340, ''), ('t4', 1, 2, 4, 462, ''), ('t6', 1, 1, 4, 522, '')],
 'tlsdemo': [('l2', 1, 1, 4, 900, ''), ('l4', 1, 1, 4, 235, ''), ('l6', 1, 3, 4, 552, '')],
}
