import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 20  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

# ---- speech helpers ----
_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = {'TCP': 'T C P', 'UDP': 'U D P', 'SSH': 'S S H', 'DNS': 'D N S', 'CNAME': 'C name', 'AAAA': 'quad A', 'MX': 'M X', 'TTL': 'T T L', 'NXDOMAIN': 'N X domain', 'TXT': 'T X T', 'NS': 'N S', 'dig': 'dig', 'TLS': 'T L S', 'URL': 'U R L', 'CA': 'C A', 'openssl': 'open S S L',  'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'SYN': 'sin', 'SYN-ACK': 'sin ack', 'ACK': 'ack', 'ESTAB': 'E S T A B',
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
  c('h1', "You type a name, and a web page appears. But computers do not understand names."),
  c('h2', "Computers talk to numbers, the I P addresses you met earlier. Something has to turn the name into a number."),
  c('h3', "That something is D N S, and it is the first step of almost every connection on the internet."),
  c('h4', "Today you trace one request from the name you type, all the way to the page that comes back, live."),
 ]),
 ('names', [
  c('n1', "Why do we need names at all?"), c('n2', "People remember names. Computers need numbers."),
  c('n3', "D N S is the phone book of the internet. You look up a name, and you get back an address."),
  c('n4', "And because it is a separate step, a name can move to a new address, and nobody has to change what they type."),
 ]),
 ('hierarchy', [
  c('r1', "Names are organised in a tree, and you read them from right to left."),
  c('r2', "At the top is the root. Below it, the top-level names, like com and org."),
  c('r3', "Below that, a company's name. And below that, the names inside it, like www."),
  c('r4', "Each level is looked after by a different server. No single computer knows everything."),
 ]),
 ('records', [
  c('t1', "A D N S answer is called a record, and there are a few types worth knowing."),
  c('t2', "A record: a name points to an I P version four address."),
  c('t3', "Quad A: the same, for an I P version six address."),
  c('t4', "C name: this name is an alias for another name."),
  c('t5', "M X: where the mail for this domain goes."),
  c('t6', "T X T: a note, often used to prove who owns the domain."),
 ]),
 ('resolver', [
  c('s1', "Who actually does the looking up?"),
  c('s2', "Your computer asks a resolver, usually run by your network or your provider."),
  c('s3', "The resolver does the hard work, asking the root, then the top level, then the company's own server."),
  c('s4', "Then it remembers the answer for a while. That time is called the T T L, in seconds."),
  c('s5', "So the second lookup is fast. And when you change a record, the old answer can linger until the T T L runs out."),
 ]),
 ('digdemo', [
  c('g1', "Let us look at a real lookup. First, who does this computer ask? Type: cat /etc/resolv.conf",
    "Let us look at a real lookup. First, who does this computer ask? Type: cat, slash, e t c, slash, resolve dot conf."),
  c('g2', "The nameserver line is the resolver. Here it is a small D N S server we started on this computer."),
  c('g3', "Now ask it a question. Type: dig www.lab.test +noall +answer",
    "Now ask it a question. Type: dig, w w w dot lab dot test, plus no all, plus answer."),
  c('g4', "Each line is a record: the name, the time to live, the class, the type, and the value."),
  c('g5', "Here www is an alias, a C name, for web. And web points to an address."),
  c('g6', "Now a different type. Type: dig lab.test MX +noall +answer",
    "Now a different type. Type: dig, lab dot test, M X, plus no all, plus answer."),
  c('g7', "The M X record: a priority number, ten, and the mail server's name."),
  c('g8', "Last, a name that does not exist. Type: dig nope.lab.test | grep status",
    "Last, a name that does not exist. Type: dig, nope dot lab dot test, pipe, grep, status."),
  c('g9', "N X domain. It means: no such name. A typo in a name gives exactly this."),
 ]),
 ('journey', [
  c('j1', "Now put it all together. Here is what happens when you open a page."),
  c('j2', "One: the name is looked up, and you get an address."),
  c('j3', "Two: your computer opens a T C P connection to that address, on a port."),
  c('j4', "Three: for H T T P S, the two sides run the T L S handshake, and check the certificate."),
  c('j5', "Four: the browser sends an H T T P request."),
  c('j6', "Five: the server sends a response, with a status code and a body."),
  c('j7', "Six steps, and every lesson so far is one of them."),
 ]),
 ('e2edemo', [
  c('e1', "Let us trace one request, end to end. First the name. Type: getent hosts www.lab.test",
    "Let us trace one request, end to end. First the name. Type: get ent, hosts, w w w dot lab dot test."),
  c('e2', "This is the answer your computer's own resolver gets: the address, and the names it belongs to."),
  c('e3', "Now the request itself. Type: curl -s http://www.lab.test:8080",
    "Now the request itself. Type: curl, dash s, H T T P colon slash slash w w w dot lab dot test, colon, eighty eighty."),
  c('e4', "The page comes back: hello from the lab. The name worked all the way through."),
  c('e5', "One more look inside. Type: curl -sv www.lab.test:8080 2>&1 | grep -i connected",
    "One more look inside. Type: curl, dash s v, w w w dot lab dot test, colon, eighty eighty, then keep only the line with connected."),
  c('e6', "Connected to the name, with the address it resolved to, and the port. Name first, then connection."),
 ]),
 ('tools', [
  c('o1', "When something fails, pick the tool for the layer."),
  c('o2', "Name problems: dig, or get ent hosts."), c('o3', "Address and route problems: I P, and ping."),
  c('o4', "Port and connection problems: s s, and curl."), c('o5', "Web and certificate problems: curl dash v."),
  c('o6', "Work from the name down, one layer at a time."),
 ]),
 ('errors', [
  c('x1', "Match the symptom to the layer."), c('x2', "Could not resolve host: the name lookup failed. Check the name, and the resolver."),
  c('x3', "N X domain: that name does not exist. Check the spelling."), c('x4', "Works by address, fails by name: D N S is the problem."),
  c('x5', "Old address after a change: the T T L has not expired yet."), c('x6', "Name resolves, connection refused: the problem is the port, not D N S."),
 ]),
 ('myths', [
  c('y1', "Watch out for four myths."), c('y2', "Myth one: D N S is the internet. It is only the phone book."),
  c('y3', "Myth two: a name has one address. It can have several, and it can change."),
  c('y4', "Myth three: changing a record is instant. It waits for the T T L."),
  c('y5', "Myth four: if the page will not load, D N S is to blame. Check each layer first."), c('y6', "Trace it, do not guess."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Explain what D N S does, and why names exist."),
  c('b3', "Name four record types and what each one is for."), c('b4', "Describe the job of a resolver, and what the T T L does."),
  c('b5', "Read a dig answer: name, T T L, type, value."), c('b6', "List the steps from typing a name to seeing a page."), c('b7', "Pick a tool for a name, a port, or a web problem."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in the virtual machine you built."),
  c('z2', "One: run cat /etc/resolv.conf, and find your resolver.", "One: run cat, slash, e t c, slash, resolve dot conf, and find your resolver."),
  c('z3', "Two: run dig on any public site, and read the answer line.", "Two: run dig on any public site, and read the answer line."),
  c('z4', "Three: ask for its M X and its N S records, and compare.", "Three: ask for its M X and its N S records, and compare."),
  c('z5', "Four: run curl dash v on the same site, and find the connected line."), c('z6', "Five: write the six steps of the journey in your own words."),
  c('z7', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f1', "Quick check."), c('f2', "What does D N S do, and what is a resolver?"), c('f3', "Name three record types."),
  c('f4', "What does the T T L control?"), c('f8', "What are the steps from name to page?"),
  c('f9', "Objective covered: MC03-O04.", "Objective covered: number four, in the computer networking masterclass."),
  c('f5', "Pause the video, and answer out loud."), c('f6', "Next: ping, trace route, and diagnosing the network."), c('f7', "Subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h4': 0.5, 'n4': 0.5, 'r4': 0.5, 't6': 0.5, 's5': 0.5, 'g9': 0.5, 'j7': 0.5, 'e6': 0.5, 'o6': 0.5, 'x6': 0.5, 'y6': 0.5, 'b8': 0.5, 'z7': 14.0, 'f5': 10.0}
CHAP = {'names': 'Why names', 'hierarchy': 'The name tree', 'records': 'Record types', 'resolver': 'Resolvers and TTL', 'digdemo': 'Live: dig', 'journey': 'Name to page: the journey',
        'e2edemo': 'Live: one request, end to end', 'tools': 'Which tool for which layer', 'errors': 'Symptoms and causes', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Networking  ·  Lesson 20', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
    E = [El(T('Names are for people. Numbers are for computers.', 'x', 56), 100, 130, C['h1'])]
    E.append(Pop(card(740, 200, ACC, 'You type', [('www.lab.test', ACC)], 46, 44), 1080, 260, C['h2']))
    E.append(El(T('↓', 'x', 80, MUTED), 1400, 470, C['h3'], anim='fade'))
    E.append(Pop(card(740, 200, GOOD, 'Computer needs', [('127.0.0.1', GOOD)], 46, 44), 1080, 580, C['h3'] + 0.5))
    E.append(Pop(card(900, 150, ACC, 'DNS', [('The phone book of the internet.', TXT)], 52, 34), 100, 250, C['h3']))
    E.append(Pop(card(900, 150, WARN, 'The journey', [('Name, connection, request, page.', TXT)], 42, 34), 100, 430, C['h4']))
    E.append(takeaway('Trace a request from the first step.', 840, C['h4'] + 1.0, GOOD, 1600)); return E
def s_names(C, D, dur):
    E = head('Why names', 'People remember names.', C['n1'])
    E.append(Pop(card(840, 330, ACC, 'People', [('remember names', TXT), ('www.lab.test', ACC)], 52, 40), 100, 330, C['n2']))
    E.append(Pop(card(840, 330, GOOD, 'Computers', [('need numbers', TXT), ('127.0.0.1', GOOD)], 52, 40), 980, 330, C['n2'] + 1.2))
    E.append(Pop(chip('DNS  =  the phone book', WARN, 36, 28, 14), 100, 720, C['n3']))
    E.append(takeaway('A name can move. Nobody retypes anything.', 850, C['n4'], GOOD, 1700)); return E
def s_hierarchy(C, D, dur):
    E = head('The name tree', 'Read it from right to left.', C['r1'])
    lv = [('. (root)', VIO, 'r2'), ('com', ACC, 'r2'), ('example', WARN, 'r3'), ('www', GOOD, 'r3')]
    for i, (n, col, cid) in enumerate(lv): E.append(Pop(card(370, 150, col, n, [], 52, 40, True), 100 + i * 440, 340, C[cid] + (0.8 if i % 2 else 0)))
    E.append(El(T('www . example . com . ', 'm', 56, TXT), 100, 590, C['r3'] + 1.5, anim='fade'))
    E.append(takeaway('Each level has its own servers. Nobody knows everything.', 800, C['r4'], GOOD, 1700)); return E
def s_records(C, D, dur):
    E = head('Record types', 'The answers DNS gives.', C['t1'])
    it = [('A', 'Name → IPv4', ACC, 't2'), ('AAAA', 'Name → IPv6', VIO, 't3'), ('CNAME', 'Alias of a name', WARN, 't4'), ('MX', 'Where mail goes', GOOD, 't5'), ('TXT', 'A note, proof of owner', PINK, 't6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 60, 34, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    return E
def s_resolver(C, D, dur):
    E = head('Resolvers and TTL', 'Who does the looking up?', C['s1'])
    E.append(Pop(card(420, 200, ACC, 'Your computer', [('asks', TXT)], 38, 32, True), 100, 340, C['s2']))
    E.append(Pop(card(420, 200, WARN, 'Resolver', [('does the work', TXT)], 40, 32, True), 740, 340, C['s2'] + 0.8))
    E.append(Pop(card(420, 200, VIO, 'DNS servers', [('root, com, company', TXT)], 38, 28, True), 1380, 340, C['s3']))
    E.append(El(T('→', 'x', 60, MUTED), 560, 400, C['s2'] + 1.0, anim='fade')); E.append(El(T('→', 'x', 60, MUTED), 1200, 400, C['s3'], anim='fade'))
    E.append(Pop(chip('TTL 300  =  remember for 300 seconds', GOOD, 34, 28, 14), 100, 640, C['s4']))
    E.append(takeaway('Fast the second time. Slow to change.', 800, C['s5'], WARN, 1700)); return E
s_digdemo = _lab('DNS, live', 'Ask a question, read the answer.', 'g1', RB, [('g1', 'cat /etc/resolv.conf', 'Who do we ask?', ACC), ('g3', 'dig www.lab.test', 'A name lookup', VIO), ('g4', 'name · TTL · type · value', 'Read each answer line', GOOD), ('g6', 'dig lab.test MX', 'A different type', WARN), ('g7', '10 mail.lab.test', 'Priority and server', PINK), ('g8', 'NXDOMAIN', 'No such name', BAD)])
def s_journey(C, D, dur):
    E = head('Name to page', 'The journey of one request.', C['j1'])
    it = [('1  Name', 'DNS lookup', ACC, 'j2'), ('2  Connect', 'TCP to the address', VIO, 'j3'), ('3  Secure', 'TLS and certificate', GOOD, 'j4'), ('4  Request', 'HTTP method and path', WARN, 'j5'), ('5  Response', 'Status, headers, body', PINK, 'j6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 48, 32), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(takeaway('Every lesson so far is one of these steps.', 850, C['j7'], GOOD, 1700)); return E
s_e2edemo = _lab('One request, end to end', 'Name, connection, page.', 'e1', RB, [('e1', 'getent hosts www.lab.test', 'The name lookup', ACC), ('e2', '127.0.0.1', 'Address for the name', VIO), ('e3', 'curl www.lab.test:8080', 'The request', WARN), ('e4', 'hello from the lab', 'The page came back', GOOD), ('e5', 'curl -v … | grep connected', 'Look inside', PINK), ('e6', 'Connected to www.lab.test', 'Name first, then connect', GOOD)])
def s_tools(C, D, dur):
    E = head('Which tool for which layer', 'Work from the name down.', C['o1'])
    it = [('Name', 'dig  ·  getent hosts', ACC, 'o2'), ('Address', 'ip  ·  ping', VIO, 'o3'), ('Port', 'ss  ·  curl', WARN, 'o4'), ('Web', 'curl -v', GOOD, 'o5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, n, [(s, TXT)], 48, 38), 100 + (i % 2) * 880, 330 + (i // 2) * 240, C[cid]))
    E.append(takeaway('One layer at a time.', 850, C['o6'], GOOD, 1500)); return E
def s_errors(C, D, dur):
    E = head('Symptoms and causes', 'Match the symptom to the layer.', C['x1'])
    it = [('Could not resolve host', 'Name lookup failed: name or resolver', 'x2', ACC), ('NXDOMAIN', 'No such name: check spelling', 'x3', WARN), ('Address works, name fails', 'DNS is the problem', 'x4', VIO), ('Old address after a change', 'The TTL has not expired', 'x5', GOOD), ('Resolves, then refused', 'Not DNS: the port', 'x6', BAD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 130
        E.append(Pop(card(760, 112, col, '', [(a, TXT)], 4, 34), 100, y, C[cid])); E.append(El(T('→', 'x', 50, MUTED), 890, y + 25, C[cid] + 0.3, anim='fade')); E.append(Pop(card(820, 112, col, '', [(b, TXT)], 4, 28), 980, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['y1'])
    it = [('Myth: DNS is the internet', 'Reality: just the phone book.', WARN, 'y2'), ('Myth: one name, one address', 'Reality: several, and they change.', VIO, 'y3'),
          ('Myth: changes are instant', 'Reality: they wait for the TTL.', BAD, 'y4'), ('Myth: no page means DNS', 'Reality: check every layer.', GOOD, 'y5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Trace it, do not guess.', 860, C['y6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['b1'])
    items = [('What DNS does, and why', 'b2'), ('Four record types', 'b3'), ('Resolver and TTL', 'b4'), ('Read a dig answer', 'b5'), ('Six steps, name to page', 'b6'), ('Pick a tool for each layer', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['z1'])
    it = [('1  Resolver', 'cat /etc/resolv.conf', ACC, 'z2'), ('2  Lookup', 'dig a public site', VIO, 'z3'), ('3  Records', 'Ask for MX and NS', WARN, 'z4'), ('4  Connect', 'curl -v, find Connected', GOOD, 'z5'), ('5  Journey', 'Write the six steps', PINK, 'z6')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f1'])]
    qs = [('What does DNS do? What is a resolver?', 'f2'), ('Name three record types.', 'f3'), ('What does the TTL control?', 'f4'), ('Steps from name to page?', 'f8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f9'] + 0.2))
    E.append(El(T('Objective covered: MC03-O04  ·  DNS, name to page', 'b', 28, TXT, maxw=960), 220, 748, C['f9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f5']))
    E.append(El(T('Next: ping, traceroute, and diagnosis', 'x', 46, ACC, maxw=1600), 100, 960, C['f6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f7']))
    return E
FN = dict(hook=s_hook, names=s_names, hierarchy=s_hierarchy, records=s_records, resolver=s_resolver, digdemo=s_digdemo, journey=s_journey, e2edemo=s_e2edemo, tools=s_tools,
          errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(names=('tag', ACC), hierarchy=('branch', VIO), records=('doc', WARN), resolver=('swap', ACC), digdemo=('eye', GOOD), journey=('steps', VIO), e2edemo=('eye', GOOD), tools=('gear', WARN),
           errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'digdemo': [('g2', 1, 1, 4, 312, ''), ('g4', 1, 2, 4, 928, ''), ('g5', 1, 1, 600, 928, ''), ('g7', 1, 1, 722, 990, ''), ('g9', 1, 1, 585, 718, '')],
 'e2edemo': [('e2', 1, 1, 4, 628, ''), ('e4', 1, 1, 4, 282, ''), ('e6', 1, 1, 4, 748, '')],
}
