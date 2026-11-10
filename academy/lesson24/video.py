import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 24  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = {'TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'MC03-O08': 'number eight', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "Five outages. Five different error messages."),
  c('h2', "Today you break a small network five ways, and fix every one of them."),
  c('h3', "A name, a port, a firewall, a certificate, and a route. Each one leaves its own clue."),
  c('h4', "Learn to read the clue, and you can find the fault in minutes, not hours."),
 ]),
 ('method', [
  c('m1', "Here is the method. Every failure arrives as a message. Read the exact words."),
  c('m2', "Could not resolve host. That is the name. D N S has no answer."),
  c('m3', "Connection refused. The machine answered, but nothing is listening on that port."),
  c('m4', "Timed out. Nobody answered at all. Often a firewall is dropping the packets."),
  c('m5', "Certificate problem. The connection worked, but T L S does not trust the server."),
  c('m6', "Network is unreachable. Your own machine has no route to get there."),
  c('m7', "We meet each one live. I broke the lab in advance with a script, so you see the fault, the clue, and the fix."),
 ]),
 ('dns', [
  c('n1', "Fault one: the name. A page will not open. Type: curl -sS -m 3 http://shop.lab.test:8080",
    "Fault one: the name. A page will not open. Type: curl, dash s big S, dash m three, H T T P colon slash slash shop dot lab dot test, colon, eighty eighty."),
  c('n2', "Could not resolve host. The request never left this machine, because the name has no address."),
  c('n3', "Ask D N S directly. Type: dig +short shop.lab.test", "Ask D N S directly. Type: dig, plus short, shop dot lab dot test."),
  c('n4', "Nothing comes back. The name is not in the zone: a typo, or a missing record."),
  c('n5', "Compare with a name that exists. Type: dig +short web.lab.test", "Compare with a name that exists. Type: dig, plus short, web dot lab dot test."),
  c('n6', "That one returns ten dot zero dot two dot two. So D N S works, and the record for shop is missing."),
  c('n7', "The fix is a record, or the right name. Check the name first, because every other test depends on it."),
 ]),
 ('port', [
  c('p1', "Fault two: the port. The name works now. Type: curl -sS -m 3 http://web.lab.test:8080",
    "Fault two: the port. The name works now. Type: curl, dash s big S, dash m three, H T T P colon slash slash web dot lab dot test, colon, eighty eighty."),
  c('p2', "Failed to connect, after two milliseconds. That speed is the clue. Something answered at once, and said no."),
  c('p3', "Go to the server, and ask who is listening. Type: sv ss -ltn", "Go to the server, and ask who is listening. Type: S V, s s, dash l t n."),
  c('p4', "Port eighty eighty is missing. Only eighty four forty three is listening. The web server is not running."),
  c('p5', "Start it again. Type: sv startweb", "Start it again. Type: S V, start web."),
  c('p6', "Try the page once more. Type: curl -s http://web.lab.test:8080", "Try the page once more. Type: curl, dash s, H T T P colon slash slash web dot lab dot test, colon, eighty eighty."),
  c('p7', "Hello from the lab. Refused means the machine is fine, and the service is not."),
 ]),
 ('fw', [
  c('f1', "Fault three: the firewall. Same page, same port. Type: curl -sS -m 3 http://web.lab.test:8080",
    "Fault three: the firewall. Same page, same port. Type: curl, dash s big S, dash m three, H T T P colon slash slash web dot lab dot test, colon, eighty eighty."),
  c('f2', "Watch the difference. It was not refused. It waited three seconds, and gave up. Timed out."),
  c('f3', "Nobody said no. The packets just vanished. That is what a firewall drop looks like."),
  c('f4', "Is the server alive? Type: ping -c 1 10.0.2.2", "Is the server alive? Type: ping, dash c, one, ten dot zero dot two dot two."),
  c('f5', "It replies, so the machine is up, and the path is fine. Only this one port is blocked."),
  c('f6', "On the server, list the firewall rules. Type: sv iptables -S INPUT", "On the server, list the firewall rules. Type: S V, I P tables, dash big S, input."),
  c('f7', "There it is. A rule for T C P, destination port eighty eighty, with the action drop."),
  c('f8', "Delete rule number one. Type: sv iptables -D INPUT 1", "Delete rule number one. Type: S V, I P tables, dash big D, input, one."),
  c('f9', "Try the page again. Type: curl -s http://web.lab.test:8080", "Try the page again. Type: curl, dash s, H T T P colon slash slash web dot lab dot test, colon, eighty eighty."),
  c('f10', "Refused is instant. A timeout is slow. Remember that pair, and you can tell a stopped service from a firewall."),
 ]),
 ('tls', [
  c('t1', "Fault four: T L S. Now the secure page, on port eighty four forty three. Type: get https://web.lab.test:8443. Get is my short name for curl, keeping only the first line, because T L S errors are long.",
    "Fault four: T L S. Now the secure page, on port eighty four forty three. Type: get, H T T P S colon slash slash web dot lab dot test, colon, eighty four forty three. Get is my short name for curl, keeping only the first line, because T L S errors are long."),
  c('t2', "Certificate problem: unable to get local issuer certificate. The name worked, and the port worked. The trust failed."),
  c('t3', "Read the certificate itself. Type: cert web.lab.test:8443. That is a short name I made for a longer open S S L command.",
    "Read the certificate itself. Type: cert, web dot lab dot test, colon, eighty four forty three. That is a short name I made for a longer open S S L command."),
  c('t4', "The subject is web dot lab dot test, so the name matches. The issuer is Lab Root C A, a private authority this computer does not know. The dates cover a full year, so it is not expired."),
  c('t5', "Tell curl to trust that authority. Type: get --cacert ca.pem https://web.lab.test:8443",
    "Tell curl to trust that authority. Type: get, dash dash c a cert, C A dot P E M, H T T P S colon slash slash web dot lab dot test, colon, eighty four forty three."),
  c('t6', "Hello from the lab. Trusted, and encrypted."),
  c('t7', "A second mistake: the right certificate, but the wrong name. Use the address instead. Type: get --cacert ca.pem https://10.0.2.2:8443",
    "A second mistake: the right certificate, but the wrong name. Use the address instead. Type: get, dash dash c a cert, C A dot P E M, H T T P S colon slash slash ten dot zero dot two dot two, colon, eighty four forty three."),
  c('t8', "No alternative certificate subject name matches. A certificate is issued for a name, not for an address. Use the name on the certificate."),
  c('t9', "You will see advice to add dash k. It skips the check. It hides the very problem you are trying to find, so never use it in production."),
 ]),
 ('route', [
  c('r1', "Fault five: the route. Now even ping fails. Type: ping -c 1 -W 1 10.0.2.2",
    "Fault five: the route. Now even ping fails. Type: ping, dash c, one, dash big W, one, ten dot zero dot two dot two."),
  c('r2', "Network is unreachable. Not a timeout. This machine already knows it has no way out."),
  c('r3', "Look at the routing table. Type: ip route", "Look at the routing table. Type: I P, route."),
  c('r4', "One line only: my own network. There is no default route, so nothing outside has a path."),
  c('r5', "Add the default route, through the gateway. Type: sudo ip route add default via 10.0.1.1",
    "Add the default route, through the gateway. Type: sudo, I P, route, add default via, ten dot zero dot one dot one."),
  c('r6', "Ping again. Type: ping -c 1 -W 1 10.0.2.2", "Ping again. Type: ping, dash c, one, dash big W, one, ten dot zero dot two dot two."),
  c('r7', "No reply, and this time it is a timeout, not unreachable. The first fault is fixed. There is a second one."),
  c('r8', "Where does the path stop? Type: traceroute -n -w 1 -q 1 -m 3 10.0.2.2",
    "Where does the path stop? Type: trace route, dash n, dash w one, dash q one, dash m three, ten dot zero dot two dot two."),
  c('r9', "Stars from the very first hop. Even the gateway is not passing traffic on."),
  c('r10', "Ask the router. Type: rt sysctl net.ipv4.ip_forward", "Ask the router. Type: R T, sys control, net dot I P v four dot I P underscore forward."),
  c('r11', "Zero. Forwarding is switched off. Switch it on. Type: rt sysctl -w net.ipv4.ip_forward=1",
    "Zero. Forwarding is switched off. Switch it on. Type: R T, sys control, dash w, net dot I P v four dot I P underscore forward, equals one."),
  c('r12', "Ping one last time. Type: ping -c 1 -W 1 10.0.2.2", "Ping one last time. Type: ping, dash c, one, dash big W, one, ten dot zero dot two dot two."),
  c('r13', "Two faults, found one at a time, just by reading each message."),
 ]),
 ('table', [
  c('x1', "Keep this table. It is the whole lesson in six rows."),
  c('x2', "Could not resolve host: name. Check with dig."),
  c('x3', "Connection refused: no listener. Check with s s."),
  c('x4', "Timed out: a firewall drop. Check the rules."),
  c('x5', "Certificate problem: trust, name, or dates. Check with open S S L."),
  c('x6', "Network is unreachable: no route. Check I P route."),
  c('x7', "Stars from hop one: a router not forwarding. Check with trace route."),
 ]),
 ('myths', [
  c('y1', "Watch out for four myths."),
  c('y2', "Myth one: add dash k and move on. That switches the certificate check off. It hides the fault instead of fixing it."),
  c('y3', "Myth two: refused and timed out mean the same thing. Refused is an instant no. A timeout is silence."),
  c('y4', "Myth three: if the name resolves, the page will load. An address is only the start. The port and the firewall can still fail."),
  c('y5', "Myth four: change several things at once. Change one thing, test, and only then change the next."),
  c('y6', "One fault at a time."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Tell refused from timed out, and say what each means."),
  c('b3', "Check a name with dig, and a listener with s s."), c('b4', "Read a certificate: the name, the issuer, and the dates."),
  c('b5', "Read I P route, and spot a missing default route."), c('b6', "Use trace route to see where a path stops."),
  c('b7', "Fix a fault, changing one thing at a time, and test after each."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in the virtual machine you built. Only break things in your own virtual machine."),
  c('z2', "One: run curl against a made-up name, like shop dot example dot invalid. Read the message."),
  c('z3', "Two: run curl against local host, port nine thousand nine. Nothing listens there. Is it instant?"),
  c('z4', "Three: start a server with python three dash m h t t p dot server eight thousand eighty, and curl it from a second terminal."),
  c('z5', "Four: block that port with sudo I P tables, watch curl time out, then delete the rule."),
  c('z6', "Five: read a real certificate, with open S S L s client, against example dot com."),
  c('z7', "Six: write down your gateway from I P route, remove the default route, see network unreachable, and add it back."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which message means a firewall may be dropping packets?"), c('f13', "What does connection refused tell you?"),
  c('f14', "Which command checks that a name resolves?"), c('f15', "Why is dash k a bad fix?"),
  c('f16', "Objective covered: MC03-O08.", "Objective covered: number eight, in the computer networking masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: your mastery scenario, where you fix a broken network on your own."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h4': 0.5, 'm7': 0.5, 'n7': 0.5, 'p7': 0.5, 'f1': 1.0, 'f10': 0.5, 't9': 0.5, 'r13': 0.5, 'x7': 0.5, 'y6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'method': 'The method', 'dns': 'Fault 1: the name (DNS)', 'port': 'Fault 2: the port', 'fw': 'Fault 3: the firewall', 'tls': 'Fault 4: the certificate (TLS)', 'route': 'Fault 5: the route',
        'table': 'Clue to cause table', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Networking  ·  Lesson 24', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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


RB = 'REAL RECORDING  ·  lab network on this computer'
def s_hook(C, D, dur):
    E = [El(T('Five outages.', 'x', 64), 100, 130, C['h1'])]
    E.append(Pop(card(900, 150, BAD, 'Five error messages', [('Each one means something different.', TXT)], 44, 34), 100, 280, C['h2']))
    E.append(Pop(card(900, 150, GOOD, 'Read the clue', [('Then fix one thing at a time.', TXT)], 44, 34), 100, 460, C['h4']))
    for i, (n, col) in enumerate([('name', PINK), ('port', ACC), ('firewall', WARN), ('certificate', VIO), ('route', GOOD)]):
        E.append(Pop(chip(n, col, 34, 24, 12), 1100 + (i % 2) * 400, 280 + (i // 2) * 130, C['h3'] + i * 0.5))
    E.append(takeaway('Break it. Read it. Fix it.', 850, C['h4'] + 1.0, GOOD, 1600)); return E
def s_method(C, D, dur):
    E = head('The method', 'Read the exact words of the error.', C['m1'])
    it = [('Could not resolve host', 'The name: D N S has no answer', 'm2', PINK), ('Connection refused', 'The port: nothing listening', 'm3', BAD), ('Timed out', 'A firewall quietly dropping', 'm4', WARN),
          ('Certificate problem', 'T L S: trust, name or dates', 'm5', VIO), ('Network is unreachable', 'The route: no way out', 'm6', GOOD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 108
        E.append(Pop(card(760, 94, col, '', [(a, TXT)], 4, 32), 100, y, C[cid])); E.append(El(T('→', 'x', 46, MUTED), 890, y + 20, C[cid] + 0.3, anim='fade')); E.append(Pop(card(820, 94, col, '', [(b, TXT)], 4, 28), 980, y, C[cid] + 0.4))
    E.append(takeaway('Five faults. Live. Broken in advance.', 880, C['m7'], GOOD, 1700)); return E
s_dns = _lab('Fault 1: the name', 'DNS has no answer.', 'n1', RB, [('n1', 'curl …shop.lab.test', 'The page will not open', ACC), ('n2', 'Could not resolve host', 'Never left this machine', BAD), ('n3', 'dig +short shop…', 'Ask D N S directly', VIO), ('n4', 'Empty answer', 'Name not in the zone', WARN), ('n5', 'dig +short web…', 'A name that exists', PINK), ('n6', '10.0.2.2', 'D N S itself works', GOOD)])
s_port = _lab('Fault 2: the port', 'Refused: nothing listening.', 'p1', RB, [('p1', 'curl …:8080', 'The name works now', ACC), ('p2', 'Failed to connect · 2 ms', 'An instant no', BAD), ('p3', 'sv ss -ltn', 'Ask the server', VIO), ('p4', 'No :8080 line', 'Only :8443 listens', WARN), ('p5', 'sv startweb', 'Start the service', PINK), ('p6', 'hello from the lab', 'Fixed', GOOD)])
s_fw = _lab('Fault 3: the firewall', 'Timed out: silence.', 'f1', RB, [('f1', 'curl …:8080', 'Same page, same port', ACC), ('f2', 'Timed out · 3 s', 'Not refused: silence', BAD), ('f4', 'ping -c 1 10.0.2.2', 'The server is alive', VIO), ('f6', 'sv iptables -S INPUT', 'Rule: --dport 8080 -j DROP', WARN), ('f8', 'sv iptables -D INPUT 1', 'Delete the rule', PINK), ('f9', 'hello from the lab', 'Fixed', GOOD)])
s_tls = _lab('Fault 4: the certificate', 'Connection fine, trust failed.', 't1', RB, [('t1', 'get https://web…:8443', 'The secure page', ACC), ('t2', 'unable to get local issuer', 'Trust failed', BAD), ('t3', 'cert web.lab.test:8443', 'Issuer: Lab Root CA', VIO), ('t5', 'get --cacert ca.pem', 'Trust that authority', GOOD), ('t7', 'get https://10.0.2.2', 'Right cert, wrong name', WARN), ('t8', 'no alternative name matches', 'Use the name on it', PINK)])
s_route = _lab('Fault 5: the route', 'Two faults, one at a time.', 'r1', RB, [('r2', 'Network is unreachable', 'Even ping fails', BAD), ('r3', 'ip route', 'No default route', VIO), ('r5', 'sudo ip route add default', 'Add the gateway', GOOD), ('r7', 'No reply · timeout', 'A second fault', WARN), ('r9', 'traceroute: stars at hop 1', 'The router is stuck', PINK), ('r11', 'rt sysctl -w …=1', 'Switch forwarding on', ACC)])
def s_table(C, D, dur):
    E = head('Clue to cause table', 'Keep this one.', C['x1'])
    it = [('Could not resolve host', 'name', 'dig', 'x2', PINK), ('Connection refused', 'no listener', 'ss -ltn', 'x3', BAD), ('Timed out', 'firewall drop', 'iptables -L', 'x4', WARN),
          ('Certificate problem', 'trust · name · dates', 'openssl', 'x5', VIO), ('Network unreachable', 'no route', 'ip route', 'x6', GOOD), ('Stars from hop 1', 'router not forwarding', 'traceroute', 'x7', ACC)]
    for i, (a, b, t, cid, col) in enumerate(it):
        y = 335 + i * 100
        E.append(Pop(card(640, 88, col, '', [(a, TXT)], 4, 30), 100, y, C[cid])); E.append(El(T('→', 'x', 40, MUTED), 760, y + 20, C[cid] + 0.3, anim='fade'))
        E.append(Pop(card(500, 88, col, '', [(b, TXT)], 4, 28), 830, y, C[cid] + 0.3)); E.append(Pop(chip(t, col, 26, 18, 10), 1370, y + 14, C[cid] + 0.6))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['y1'])
    it = [('Myth: add -k and move on', 'Reality: it hides the fault.', BAD, 'y2'), ('Myth: refused = timed out', 'Reality: instant no vs silence.', WARN, 'y3'),
          ('Myth: name resolves = page loads', 'Reality: the port can still fail.', VIO, 'y4'), ('Myth: change many things', 'Reality: one change, then test.', GOOD, 'y5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('One fault at a time.', 860, C['y6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['b1'])
    items = [('Refused vs timed out', 'b2'), ('Check a name and a listener', 'b3'), ('Read a certificate', 'b4'), ('Spot a missing route', 'b5'), ('Read a traceroute', 'b6'), ('Fix one change at a time', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine.', C['z1'])
    it = [('1  Name', 'curl a made-up name', PINK, 'z2'), ('2  Port', 'curl localhost:9090', BAD, 'z3'), ('3  Serve', 'python3 -m http.server', ACC, 'z4'), ('4  Firewall', 'iptables drop, then delete', WARN, 'z5'), ('5  Certificate', 'openssl s_client', VIO, 'z6'), ('6  Route', 'remove, then restore', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which message hints at a firewall?', 'f12'), ('What does connection refused tell you?', 'f13'), ('Which command checks a name?', 'f14'), ('Why is -k a bad fix?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC03-O08', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: your networking mastery scenario', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, method=s_method, dns=s_dns, port=s_port, fw=s_fw, tls=s_tls, route=s_route, table=s_table, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(method=('steps', VIO), dns=('eye', GOOD), port=('eye', GOOD), fw=('eye', GOOD), tls=('eye', GOOD), route=('eye', GOOD), table=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'dns': [('n2', 1, 1, 154, 712, ''), ('n4', 0, 1, 397, 592, ''), ('n6', 1, 1, 4, 130, '')],
 'port': [('p2', 1, 2, 4, 1072, ''), ('p4', 2, 1, 442, 640, ''), ('p7', 1, 1, 4, 282, '')],
 'fw': [('f2', 1, 1, 4, 830, ''), ('f5', 2, 1, 4, 830, ''), ('f5', 5, 1, 525, 745, ''), ('f7', 2, 1, 4, 655, ''), ('f10', 1, 1, 4, 282, '')],
 'tls': [('t2', 1, 1, 4, 1028, ''), ('t4', 1, 1, 200, 382, ''), ('t4', 2, 1, 186, 352, ''), ('t4', 3, 2, 4, 520, ''), ('t6', 1, 1, 4, 282, ''), ('t8', 1, 2, 4, 1072, '')],
 'route': [('r2', 1, 1, 4, 562, ''), ('r4', 1, 1, 4, 832, ''), ('r7', 4, 1, 334, 925, ''), ('r9', 2, 3, 4, 100, ''), ('r11', 1, 1, 4, 352, ''), ('r13', 2, 1, 4, 830, ''), ('r13', 5, 1, 525, 745, '')],
}
