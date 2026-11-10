import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 21  ·  DEVOPS BOOTCAMP'
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
       'ESTABLISHED': 'established', 'TIME-WAIT': 'time wait', 'UNCONN': 'unconnected', 'nc': 'n c', 'ss': 's s', 'curl': 'curl', 'localhost': 'local host', 'ICMP': 'I C M P', 'RTT': 'R T T', 'traceroute': 'trace route', 'nslookup': 'n s lookup', 'ping': 'ping', 'ip': 'I P', 'c0': 'c zero', 'lo': 'loopback', 'sport': 's port', 'MC03-O05': 'number five'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "The page will not load. Where do you even start?"),
  c('h2', "Most people refresh, restart, and hope. A good engineer does something different."),
  c('h3', "You test one layer at a time, and the first test that fails tells you where the problem is."),
  c('h4', "Today you learn six tools for that, and you use them live, on a small network built on this computer."),
 ]),
 ('ladder', [
  c('l1', "Here is the diagnosis ladder. One question per rung."),
  c('l2', "Rung one: is this machine set up? The ip command shows your address, and your way out."),
  c('l3', "Rung two: does the name work? Dig asks D N S. N s lookup is an older tool for the same job."),
  c('l4', "Rung three: can I reach the machine? Ping sends a message, and waits for the reply."),
  c('l5', "Rung four: where does the path stop? Trace route lists every router on the way."),
  c('l6', "Rung five: is anything listening on the port? S s shows the listeners, and curl tries the connection."),
  c('l7', "The first rung that fails is your suspect. You do not need to guess."),
 ]),
 ('ipdemo', [
  c('i1', "First, know your own setup. Type: ip -br addr", "First, know your own setup. Type: I P, dash b r, addr."),
  c('i2', "Each line is an interface. This one, c zero, is up, with the address ten dot zero dot one dot two, slash twenty-four.",
    "Each line is an interface. This one, c zero, is up, with the address ten dot zero dot one dot two, slash twenty-four."),
  c('i3', "Now the way out. Type: ip route", "Now the way out. Type: I P, route."),
  c('i4', "The first line is the default route. Anything not on my own network goes via ten dot zero dot one dot one. That is the gateway.",
    "The first line is the default route. Anything not on my own network goes via ten dot zero dot one dot one. That is the gateway."),
  c('i5', "No address, or no default route? Stop here. Nothing above this rung will work."),
 ]),
 ('pingdemo', [
  c('p1', "Now reach out. Ping sends a small message, and waits for a reply. First, the gateway. Type: ping -c 3 10.0.1.1",
    "Now reach out. Ping sends a small message, and waits for a reply. First, the gateway. Type: ping, dash c, three, ten dot zero dot one dot one."),
  c('p2', "Three sent, three replies. The time is the round trip, in milliseconds. It is tiny here, because everything runs on one machine."),
  c('p3', "Now the server. Type: ping -c 3 10.0.2.2", "Now the server. Type: ping, dash c, three, ten dot zero dot two dot two."),
  c('p4', "Zero percent packet loss. Loss is the number to watch. Any loss means a flaky link."),
  c('p5', "Now an address with no route. Type: ping -c 2 -W 1 10.0.3.9",
    "Now an address with no route. Type: ping, dash c, two, dash big W, one, ten dot zero dot three dot nine."),
  c('p6', "Destination net unreachable, reported by the gateway. The router is saying: I do not know how to get there."),
 ]),
 ('tracedemo', [
  c('t1', "Ping tells you if you can reach it. Trace route shows how. Type: traceroute -n 10.0.2.2",
    "Ping tells you if you can reach it. Trace route shows how. Type: trace route, dash n, ten dot zero dot two dot two."),
  c('t2', "Each line is one hop, one router on the path. The dash n option skips name lookups, so the output stays clean."),
  c('t3', "Hop one is the gateway, ten dot zero dot one dot one. Hop two is the server itself. Two hops, and we arrived.",
    "Hop one is the gateway, ten dot zero dot one dot one. Hop two is the server itself. Two hops, and we arrived."),
  c('t4', "On a long path, a hop where the time jumps, or where the stars begin, shows where the trouble starts."),
  c('t5', "It works by sending packets with a tiny time to live, so each router in turn reports back."),
 ]),
 ('ssdemo', [
  c('s1', "Now the server side. This terminal is on the server. Is anything listening? Type: ss -ltn",
    "Now the server side. This terminal is on the server. Is anything listening? Type: s s, dash l t n."),
  c('s2', "L is listening, T is T C P, and N shows numbers. One listener: port eighty eighty, on ten dot zero dot two dot two.",
    "L is listening, T is T C P, and N shows numbers. One listener: port eighty eighty, on ten dot zero dot two dot two."),
  c('s3', "What about port 9090? Type: ss -ltn sport = :9090",
    "What about port ninety ninety? Type: s s, dash l t n, s port, equals, colon, ninety ninety."),
  c('s4', "Only the header comes back. Nothing is listening on that port, so a client that tries it will be refused."),
 ]),
 ('diagdemo', [
  c('d1', "Now a real incident. A page will not load, so we climb the ladder. First, a typo in the name. Type: ping -c 1 wbe.lab.test",
    "Now a real incident. A page will not load, so we climb the ladder. First, a typo in the name. Type: ping, dash c, one, w b e, dot lab dot test."),
  c('d2', "Name or service not known. The name rung failed, so stop there, and fix the spelling."),
  c('d3', "With the right name, ask D N S. Type: dig +short web.lab.test", "With the right name, ask D N S. Type: dig, plus short, web dot lab dot test."),
  c('d4', "An address comes back: ten dot zero dot two dot two. The name rung is fine."),
  c('d5', "Can we reach it? Type: ping -c 1 10.0.2.2", "Can we reach it? Type: ping, dash c, one, ten dot zero dot two dot two."),
  c('d6', "One reply. The address and the path are fine."),
  c('d7', "Now the page, on port 9090. Type: curl -sS -m 3 http://web.lab.test:9090",
    "Now the page, on port ninety ninety. Type: curl, dash s big S, dash m three, H T T P colon slash slash web dot lab dot test, colon, ninety ninety."),
  c('d8', "Failed to connect. Everything below worked, so the problem is the port. Nothing is listening, just as the server showed."),
  c('d9', "Try the right port. Type: curl -s http://web.lab.test:8080",
    "Try the right port. Type: curl, dash s, H T T P colon slash slash web dot lab dot test, colon, eighty eighty."),
  c('d10', "Hello from the lab. Fixed in five commands, with no guessing."),
 ]),
 ('errors', [
  c('x1', "Match the message to the rung."),
  c('x2', "Name or service not known: D N S. Check the spelling, and the resolver."),
  c('x3', "Network is unreachable: I P. Check your address, and your gateway."),
  c('x4', "Destination net unreachable: a router has no route. Trace route shows which one."),
  c('x5', "No answer at all, or only stars: a firewall, or a machine that is down."),
  c('x6', "Connection refused: the machine answers, but nothing listens on that port."),
  c('x7', "Connection timed out: often a firewall quietly dropping the packets."),
 ]),
 ('myths', [
  c('y1', "Watch out for four myths."),
  c('y2', "Myth one: if ping fails, the server is down. Many servers block ping on purpose."),
  c('y3', "Myth two: if ping works, the website works. Ping only proves the machine answers, not that the web server is running."),
  c('y4', "Myth three: stars in trace route mean a broken router. Many routers just do not reply to those probes."),
  c('y5', "Myth four: restart first, investigate later. Restarting can erase the evidence."),
  c('y6', "Test one layer at a time."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Explain the ladder, and what each rung checks."),
  c('b3', "Read ip addr and ip route: address, network, and gateway."), c('b4', "Run and read a ping: replies, time, and packet loss."),
  c('b5', "Run and read a trace route: the hops, and where it stops."), c('b6', "Use dig, curl, and s s to check a name, a port, and a listener."),
  c('b7', "Match an error message to its rung."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in the virtual machine you built."),
  c('z2', "One: run ip -br addr, and find your address.", "One: run I P, dash b r, addr, and find your address."),
  c('z3', "Two: run ip route, and find your default gateway.", "Two: run I P, route, and find your default gateway."),
  c('z4', "Three: ping your gateway, then ping a public site, and compare the times."),
  c('z5', "Four: run trace route to a public site, and count the hops. If it is missing, install it with apt."),
  c('z6', "Five: run s s dash l t n, and list what is listening on your machine.", "Five: run s s, dash l t n, and list what is listening on your machine."),
  c('z7', "Six: break something on purpose. Ping a made-up name, and say which rung failed."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f1', "Quick check."), c('f2', "Which tool lists every hop on the path?"), c('f3', "What does connection refused tell you?"),
  c('f4', "What does packet loss mean?"), c('f8', "Which command shows what is listening?"),
  c('f9', "Objective covered: MC03-O05.", "Objective covered: number five, in the computer networking masterclass."),
  c('f5', "Pause the video, and answer out loud."), c('f6', "Next: routing, N A T, and firewalls."), c('f7', "Subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h4': 0.5, 'l7': 0.5, 'i5': 0.5, 't5': 0.5, 's4': 0.5, 'd10': 0.5, 'x7': 0.5, 'y6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f5': 10.0}
CHAP = {'ladder': 'The diagnosis ladder', 'ipdemo': 'Live: ip', 'pingdemo': 'Live: ping', 'tracedemo': 'Live: traceroute', 'ssdemo': 'Live: ss on the server', 'diagdemo': 'Live: a real incident',
        'errors': 'Messages and rungs', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Networking  ·  Lesson 21', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
def mono(s, col, size=28):
    f = ImageFont.truetype(MONO, size)
    im = Image.new('RGBA', (int(f.getlength(s)) + 10, size + 16), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), s, font=f, fill=tuple(col)[:3] + (255,)); return im
def chip(s, col, size=40, padx=22, pady=10):
    return badge(s, ImageFont.truetype(MONO, size), INK, col, padx=padx, pady=pady, r=18)
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
RB = 'REAL RECORDING  ·  lab network on this computer'
def s_hook(C, D, dur):
    E = [El(T('The page will not load.', 'x', 64), 100, 130, C['h1'])]
    E.append(Pop(card(900, 150, BAD, 'Refresh. Restart. Hope.', [('Guessing.', TXT)], 44, 36), 100, 280, C['h2']))
    E.append(Pop(card(900, 150, GOOD, 'One layer at a time', [('The first failure is the clue.', TXT)], 44, 34), 100, 460, C['h3']))
    for i, (n, col) in enumerate([('ip', ACC), ('ping', VIO), ('traceroute', WARN), ('dig', PINK), ('ss', GOOD), ('curl', ACC)]):
        E.append(Pop(chip(n, col, 34, 24, 12), 1100 + (i % 2) * 330, 280 + (i // 2) * 130, C['h4'] + i * 0.35))
    E.append(takeaway('Six tools. One ladder. Live.', 850, C['h4'] + 2.2, GOOD, 1600)); return E
def s_ladder(C, D, dur):
    E = head('The diagnosis ladder', 'One question per rung.', C['l1'])
    it = [('1  Setup', 'ip addr · ip route', ACC, 'l2'), ('2  Name', 'dig · nslookup', PINK, 'l3'), ('3  Reach', 'ping', VIO, 'l4'), ('4  Path', 'traceroute', WARN, 'l5'), ('5  Port', 'ss · curl', GOOD, 'l6')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s_, TXT)], 48, 36), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(takeaway('The first rung that fails is your suspect.', 850, C['l7'], GOOD, 1700)); return E
s_ipdemo = _lab('ip: your own setup', 'Address, network, gateway.', 'i1', RB, [('i1', 'ip -br addr', 'Interfaces and addresses', ACC), ('i2', '10.0.1.2/24', 'This machine on its network', VIO), ('i3', 'ip route', 'The way out', WARN), ('i4', 'default via 10.0.1.1', 'The gateway', GOOD), ('i5', 'No address? No route?', 'Stop. Fix this first', BAD)])
s_pingdemo = _lab('ping: can I reach it?', 'Replies, time, packet loss.', 'p1', RB, [('p1', 'ping -c 3 10.0.1.1', 'The gateway', ACC), ('p2', 'time = round trip', 'In milliseconds', VIO), ('p3', 'ping -c 3 10.0.2.2', 'The server', WARN), ('p4', '0% packet loss', 'The number to watch', GOOD), ('p5', 'ping 10.0.3.9', 'No route to it', PINK), ('p6', 'Net Unreachable', 'A router says: no route', BAD)])
s_tracedemo = _lab('traceroute: the path', 'Every router on the way.', 't1', RB, [('t1', 'traceroute -n 10.0.2.2', 'Show the path', ACC), ('t2', 'One line per hop', 'A hop is one router', VIO), ('t3', '10.0.1.1 → 10.0.2.2', 'Gateway, then server', GOOD), ('t4', 'Stars or a time jump', 'Where trouble starts', WARN), ('t5', 'Tiny time to live', 'Each router replies in turn', PINK)])
s_ssdemo = _lab('ss: what is listening?', 'Run on the server.', 's1', 'REAL RECORDING  ·  on the server', [('s1', 'ss -ltn', 'L listening · T tcp · N numbers', ACC), ('s2', '10.0.2.2:8080', 'One listener', GOOD), ('s3', 'ss -ltn sport = :9090', 'Ask about one port', WARN), ('s4', 'Header only', 'Nothing listening: refused', BAD)])
s_diagdemo = _lab('A real incident', 'Climb the ladder.', 'd1', RB, [('d1', 'ping wbe.lab.test', 'Typo: name not known', BAD), ('d3', 'dig +short web.lab.test', 'The right name works', VIO), ('d5', 'ping -c 1 10.0.2.2', 'Reachable', WARN), ('d7', 'curl … :9090', 'The page, wrong port', PINK), ('d8', 'Failed to connect', 'Nothing is listening', BAD), ('d9', 'curl … :8080', 'Right port: it works', GOOD)])
def s_errors(C, D, dur):
    E = head('Messages and rungs', 'Match the message to the rung.', C['x1'])
    it = [('Name or service not known', 'Name: check spelling, resolver', 'x2', PINK), ('Network is unreachable', 'Setup: address and gateway', 'x3', ACC), ('Destination net unreachable', 'A router has no route', 'x4', WARN), ('No answer, only stars', 'Firewall, or machine down', 'x5', VIO), ('Connection refused', 'Port: nothing listening', 'x6', BAD), ('Connection timed out', 'Often a firewall dropping', 'x7', GOOD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 108
        E.append(Pop(card(760, 94, col, '', [(a, TXT)], 4, 32), 100, y, C[cid])); E.append(El(T('→', 'x', 46, MUTED), 890, y + 20, C[cid] + 0.3, anim='fade')); E.append(Pop(card(820, 94, col, '', [(b, TXT)], 4, 28), 980, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['y1'])
    it = [('Myth: ping fails = down', 'Reality: ping is often blocked.', WARN, 'y2'), ('Myth: ping works = site works', 'Reality: the web server may be off.', VIO, 'y3'),
          ('Myth: stars = broken router', 'Reality: many do not reply.', BAD, 'y4'), ('Myth: restart first', 'Reality: it erases the evidence.', GOOD, 'y5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Test one layer at a time.', 860, C['y6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['b1'])
    items = [('Explain the ladder', 'b2'), ('Read ip addr and ip route', 'b3'), ('Read a ping result', 'b4'), ('Read a traceroute', 'b5'), ('Check name, port, listener', 'b6'), ('Match message to rung', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['z1'])
    it = [('1  Setup', 'ip -br addr', ACC, 'z2'), ('2  Gateway', 'ip route', VIO, 'z3'), ('3  Reach', 'ping gateway, ping a site', WARN, 'z4'), ('4  Path', 'traceroute a site', GOOD, 'z5'), ('5  Listen', 'ss -ltn', PINK, 'z6'), ('6  Break it', 'ping a made-up name', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f1'])]
    qs = [('Which tool lists every hop?', 'f2'), ('What does connection refused mean?', 'f3'), ('What does packet loss mean?', 'f4'), ('Which command shows listeners?', 'f8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f9'] + 0.2))
    E.append(El(T('Objective covered: MC03-O05  ·  diagnosis tools', 'b', 28, TXT, maxw=960), 220, 748, C['f9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f5']))
    E.append(El(T('Next: routing, NAT, and firewalls', 'x', 46, ACC, maxw=1600), 100, 960, C['f6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f7']))
    return E
FN = dict(hook=s_hook, ladder=s_ladder, ipdemo=s_ipdemo, pingdemo=s_pingdemo, tracedemo=s_tracedemo, ssdemo=s_ssdemo, diagdemo=s_diagdemo, errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ladder=('steps', VIO), ipdemo=('eye', GOOD), pingdemo=('eye', GOOD), tracedemo=('eye', GOOD), ssdemo=('eye', GOOD), diagdemo=('eye', GOOD), errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'ipdemo': [('i2', 2, 1, 4, 671, ''), ('i4', 1, 1, 4, 415, '')],
 'pingdemo': [('p2', 2, 3, 640, 840, ''), ('p4', 7, 1, 534, 750, ''), ('p6', 2, 2, 383, 792, '')],
 'tracedemo': [('t2', 2, 2, 4, 560, ''), ('t3', 2, 2, 56, 210, '')],
 'ssdemo': [('s2', 2, 1, 443, 640, ''), ('s4', 1, 1, 4, 1070, '')],
 'diagdemo': [('d2', 1, 1, 307, 692, ''), ('d4', 1, 1, 4, 130, ''), ('d6', 2, 1, 4, 837, ''), ('d8', 1, 2, 4, 1070, ''), ('d10', 1, 1, 4, 282, '')],
}
