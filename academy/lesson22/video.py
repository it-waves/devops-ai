import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 22  ·  DEVOPS BOOTCAMP'
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
       'ESTABLISHED': 'established', 'TIME-WAIT': 'time wait', 'UNCONN': 'unconnected', 'nc': 'n c', 'ss': 's s', 'curl': 'curl', 'localhost': 'local host', 'ICMP': 'I C M P', 'RTT': 'R T T', 'traceroute': 'trace route', 'nslookup': 'n s lookup', 'ping': 'ping', 'ip': 'I P', 'c0': 'c zero', 'lo': 'loopback', 'sport': 's port', 'MC03-O06': 'number six', 'NAT': 'nat', 'iptables': 'I P tables', 'nginx': 'engine X', 'sysctl': 'sis control', 'rt': 'R T', 'MASQUERADE': 'masquerade', 'DROP': 'drop', 'REJECT': 'reject', 'FORWARD': 'forward', 'LAN': 'L A N', 'DMZ': 'D M Z', 'HAProxy': 'H A proxy', 'ACCEPT': 'accept'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "Your laptop has a private address, yet it reaches the whole internet. How?"),
  c('h2', "Five ideas make that work, and you will meet them in every cloud and every company network."),
  c('h3', "Routing decides where a packet goes next. N A T rewrites addresses on the way out. A firewall decides what is allowed."),
  c('h4', "A load balancer shares the traffic, and a reverse proxy stands in front of your servers."),
  c('h5', "Today you see all five work, live, on a small network built on this computer."),
 ]),
 ('routing', [
  c('r1', "Start with routing. A router joins networks together."),
  c('r2', "When a packet arrives, the router looks at the destination address, and checks its routing table."),
  c('r3', "The table says which network is reachable through which door, and who the next hop is."),
  c('r4', "If nothing matches, the packet goes to the default route, the way out to everything else."),
  c('r5', "No router knows the whole path. Each one only knows the next step."),
 ]),
 ('routedemo', [
  c('t1', "Let us look at a real router. In this lab, the letters R T mean: run the next command on the router. Type: rt ip route",
    "Let us look at a real router. In this lab, the letters R T mean: run the next command on the router. Type: R T, I P, route."),
  c('t2', "The router sits on two networks, ten dot zero dot one, and ten dot zero dot two. That is what makes it a router.",
    "The router sits on two networks, ten dot zero dot one, and ten dot zero dot two. That is what makes it a router."),
  c('t3', "One setting turns it on. Type: rt sysctl net.ipv4.ip_forward",
    "One setting turns it on. Type: R T, sis control, net dot I P v four dot I P underscore forward."),
  c('t4', "A one means forwarding is on: it passes packets between its networks."),
  c('t5', "Now switch it off. Type: rt sysctl -w net.ipv4.ip_forward=0",
    "Now switch it off. Type: R T, sis control, dash w, net dot I P v four dot I P underscore forward, equals zero."),
  c('t6', "Then try to reach the server. Type: ping -c 1 -W 1 10.0.2.2",
    "Then try to reach the server. Type: ping, dash c, one, dash big W, one, ten dot zero dot two dot two."),
  c('t7', "No reply. One hundred percent loss. The router received the packet, but refused to pass it on."),
  c('t8', "Switch forwarding back on. Type: rt sysctl -w net.ipv4.ip_forward=1",
    "Switch forwarding back on. Type: R T, sis control, dash w, net dot I P v four dot I P underscore forward, equals one."),
 ]),
 ('nat', [
  c('a1', "Next, N A T, network address translation."),
  c('a2', "Private addresses, like ten dot something, or one ninety-two dot one sixty-eight, cannot be used on the public internet.",
    "Private addresses, like ten dot something, or one ninety-two dot one sixty-eight, cannot be used on the public internet."),
  c('a3', "So the router swaps your private source address for its own public one, and remembers the swap."),
  c('a4', "When the reply comes back, it swaps the address back, and hands the answer to you."),
  c('a5', "Many machines can share one public address, and the outside world only ever sees the router."),
 ]),
 ('natdemo', [
  c('n1', "A small web server here can tell us who is calling. Type: curl -s http://10.0.2.2:8080/whoami",
    "A small web server here can tell us who is calling. Type: curl, dash s, H T T P colon slash slash ten dot zero dot two dot two, colon, eighty eighty, slash who am I."),
  c('n2', "You are ten dot zero dot one dot two. The server sees my real, private address.", "You are ten dot zero dot one dot two. The server sees my real, private address."),
  c('n3', "Now turn on N A T on the router. Type: rt iptables -t nat -A POSTROUTING -j MASQUERADE",
    "Now turn on nat on the router. Type: R T, I P tables, dash t nat, dash big A, post routing, dash j, masquerade."),
  c('n4', "Same request again. Type: curl -s http://10.0.2.2:8080/whoami",
    "Same request again. Type: curl, dash s, H T T P colon slash slash ten dot zero dot two dot two, colon, eighty eighty, slash who am I."),
  c('n5', "Now the server sees ten dot zero dot two dot one: the router. My private address is hidden.", "Now the server sees ten dot zero dot two dot one: the router. My private address is hidden."),
  c('n6', "Look at the rule. Type: rt iptables -t nat -S POSTROUTING",
    "Look at the rule. Type: R T, I P tables, dash t nat, dash big S, post routing."),
  c('n7', "Masquerade: rewrite the source address to the router's own. That one line is home N A T."),
 ]),
 ('firewall', [
  c('w1', "Now the firewall. A firewall is a list of rules, checked from the top."),
  c('w2', "The first rule that matches wins, and that rule says accept, drop, or reject."),
  c('w3', "Drop throws the packet away in silence. The sender waits, and then times out."),
  c('w4', "Reject throws it away, and tells the sender. The sender fails at once."),
  c('w5', "Remember the last lesson? A time out and a refusal point to different problems."),
 ]),
 ('fwdemo', [
  c('f1', "Let us block the web server's port, with a drop rule. Type: rt iptables -A FORWARD -p tcp --dport 8080 -j DROP",
    "Let us block the web server's port, with a drop rule. Type: R T, I P tables, dash big A, forward, dash p T C P, dash dash d port, eighty eighty, dash j, drop."),
  c('f2', "Now try the page, and give up after two seconds. Type: curl -sS -m 2 http://10.0.2.2:8080",
    "Now try the page, and give up after two seconds. Type: curl, dash s big S, dash m two, H T T P colon slash slash ten dot zero dot two dot two, colon, eighty eighty."),
  c('f3', "Operation timed out. Silence. That is what a drop looks like from outside."),
  c('f4', "Remove the rule. Type: rt iptables -F FORWARD", "Remove the rule. Type: R T, I P tables, dash big F, forward."),
  c('f5', "Now the same block, but with reject. Type: rt iptables -A FORWARD -p tcp --dport 8080 -j REJECT",
    "Now the same block, but with reject. Type: R T, I P tables, dash big A, forward, dash p T C P, dash dash d port, eighty eighty, dash j, reject."),
  c('f6', "And try the page again. Type: curl -sS -m 2 http://10.0.2.2:8080",
    "And try the page again. Type: curl, dash s big S, dash m two, H T T P colon slash slash ten dot zero dot two dot two, colon, eighty eighty."),
  c('f7', "Failed to connect, straight away. The sender is told no. Same block, different symptom."),
  c('f8', "List the rules. Type: rt iptables -S FORWARD", "List the rules. Type: R T, I P tables, dash big S, forward."),
  c('f9', "The first line is the default policy: accept. Then our rule, with the port, and reject."),
 ]),
 ('proxy', [
  c('p1', "Last, the reverse proxy, and the load balancer."),
  c('p2', "A reverse proxy stands in front of your servers. Clients talk to it, and it talks to the servers for them."),
  c('p3', "That hides the servers, and it can add security, caching, and secure connections."),
  c('p4', "A load balancer spreads the requests across several servers, so no single one is overloaded."),
  c('p5', "If a server dies, a good balancer stops sending traffic to it. Often one tool does both jobs, like engine X."),
 ]),
 ('lbdemo', [
  c('l1', "Here the proxy listens on ten dot zero dot one dot one. Behind it are two servers. Type: for i in 1 2 3 4; do curl -s 10.0.1.1; done",
    "Here the proxy listens on ten dot zero dot one dot one. Behind it are two servers. Type: for i in one two three four, do, curl, dash s, ten dot zero dot one dot one, done."),
  c('l2', "Four requests, to one address. Backend A, backend B, A, B. The proxy takes turns."),
  c('l3', "The client never learns the servers' addresses. It only knows the proxy."),
  c('l4', "Where does the proxy live? Type: rt ss -ltn", "Where does the proxy live? Type: R T, s s, dash l t n."),
  c('l5', "Listening on port eighty, on the router's front address. That is the proxy, waiting for clients."),
 ]),
 ('errors', [
  c('x1', "Match the symptom to the cause."),
  c('x2', "Times out, only through the router: forwarding is off, or a route is missing."),
  c('x3', "Times out on one port only: a drop rule."),
  c('x4', "Refused at once: a reject rule, or nothing is listening."),
  c('x5', "Every client shows the router's address in the logs: that is N A T."),
  c('x6', "Bad gateway: the proxy cannot reach the server behind it."),
  c('x7', "One server overloaded, one idle: check the balancing."),
 ]),
 ('myths', [
  c('y1', "Four myths to drop."),
  c('y2', "Myth one: N A T is a firewall. It hides addresses, but it does not decide what is allowed."),
  c('y3', "Myth two: a blocked port is invisible. A reject announces itself, and a drop still shows as a time out."),
  c('y4', "Myth three: a load balancer only does round robin. There are many strategies."),
  c('y5', "Myth four: a reverse proxy is a proxy for users. It serves the servers, not the users."),
  c('y6', "Name the job, then pick the tool."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Explain what a routing table and a default route do."),
  c('b3', "Explain N A T, and what the server sees."), c('b4', "Explain accept, drop, and reject, and how each looks from outside."),
  c('b5', "Explain what a load balancer does."), c('b6', "Explain a reverse proxy, and how it differs from a load balancer."),
  c('b7', "Match a symptom to routing, N A T, firewall, or proxy."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in the virtual machine you built."),
  c('z2', "One: run ip route, and find the default route.", "One: run I P, route, and find the default route."),
  c('z3', "Two: run sysctl net.ipv4.ip_forward. Is your machine a router?", "Two: run sis control, net dot I P v four dot I P underscore forward. Is your machine a router?"),
  c('z4', "Three: run sudo iptables dash S, and read the rules you already have.", "Three: run sudo, I P tables, dash big S, and read the rules you already have."),
  c('z5', "Four: run curl dash s i f config dot me, and compare it with ip dash br addr. That gap is N A T.",
    "Four: run curl, dash s, i f config dot me, and compare it with I P, dash b r, addr. That gap is nat."),
  c('z6', "Five: for each symptom in the table, write the cause in one line."),
  c('z7', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f10', "Quick check."), c('f11', "What does the default route do?"), c('f12', "What does N A T change?"),
  c('f13', "How do drop and reject differ?"), c('f14', "Load balancer or reverse proxy: what is the difference?"),
  c('f15', "Objective covered: MC03-O06.", "Objective covered: number six, in the computer networking masterclass."),
  c('f16', "Pause the video, and answer out loud."), c('f17', "Next: network boundaries, clients, servers, containers and cloud subnets."), c('f18', "Subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h5': 0.5, 'r5': 0.5, 't8': 0.5, 'a5': 0.5, 'n7': 0.5, 'w5': 0.5, 'f9': 0.5, 'p5': 0.5, 'l5': 0.5, 'x7': 0.5, 'y6': 0.5, 'b8': 0.5, 'z7': 14.0, 'f16': 10.0}
CHAP = {'routing': 'Routing', 'routedemo': 'Live: a router', 'nat': 'NAT', 'natdemo': 'Live: NAT', 'firewall': 'Firewalls', 'fwdemo': 'Live: drop vs reject', 'proxy': 'Proxies and load balancers',
        'lbdemo': 'Live: a reverse proxy', 'errors': 'Symptoms and causes', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Networking  ·  Lesson 22', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
    E = [El(T('Private address. Whole internet.', 'x', 60), 100, 130, C['h1'])]
    it = [('Routing', 'Where next?', ACC, 'h3'), ('NAT', 'Swap addresses', VIO, 'h3'), ('Firewall', 'Allowed or not?', BAD, 'h3'), ('Load balancer', 'Share the load', WARN, 'h4'), ('Reverse proxy', 'Front door', GOOD, 'h4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s_, TXT)], 48, 34), 100 + (i % 3) * 590, 280 + (i // 3) * 245, C[cid] + (0.8 if i in (1, 4) else 0) + (1.6 if i == 2 else 0)))
    E.append(takeaway('Five ideas. All live today.', 850, C['h5'], GOOD, 1600)); return E
def s_routing(C, D, dur):
    E = head('Routing', 'The next hop, one router at a time.', C['r1'])
    E.append(Pop(card(540, 215, ACC, 'Routing table', [('destination → next hop', TXT)], 44, 30), 100, 330, C['r2']))
    E.append(Pop(card(540, 215, VIO, 'Two doors', [('one per network', TXT)], 44, 34), 690, 330, C['r3']))
    E.append(Pop(card(540, 215, WARN, 'Default route', [('everything else', TXT)], 44, 34), 1280, 330, C['r4']))
    E.append(Pop(chip('10.0.2.0/24 via r1b   ·   default via 10.0.1.1', GOOD, 30, 26, 12), 100, 640, C['r3'] + 1.0))
    E.append(takeaway('Each router knows only the next step.', 850, C['r5'], GOOD, 1700)); return E
s_routedemo = _lab('A real router', 'Forwarding on, then off.', 't1', RB, [('t1', 'rt ip route', 'The router, two networks', ACC), ('t3', 'ip_forward', 'The router switch', VIO), ('t4', '= 1', 'On: packets pass through', GOOD), ('t5', 'ip_forward = 0', 'Switch it off', WARN), ('t7', '100% packet loss', 'Router will not pass them', BAD), ('t8', 'ip_forward = 1', 'Back on', GOOD)])
def s_nat(C, D, dur):
    E = head('NAT', 'Network address translation.', C['a1'])
    E.append(Pop(card(540, 215, ACC, 'Inside', [('10.0.1.2  private', TXT)], 44, 34), 100, 330, C['a2']))
    E.append(Pop(card(540, 215, WARN, 'Router', [('swaps the address', TXT)], 44, 34), 690, 330, C['a3']))
    E.append(Pop(card(540, 215, GOOD, 'Outside', [('sees the router only', TXT)], 44, 32), 1280, 330, C['a5']))
    E.append(El(T('→', 'x', 60, MUTED), 640, 400, C['a3'], anim='fade')); E.append(El(T('→', 'x', 60, MUTED), 1230, 400, C['a5'], anim='fade'))
    E.append(Pop(chip('Replies are swapped back', VIO, 34, 28, 14), 100, 640, C['a4']))
    E.append(takeaway('Many machines, one public address.', 850, C['a5'] + 0.8, GOOD, 1700)); return E
s_natdemo = _lab('A real NAT', 'Who does the server see?', 'n1', RB, [('n1', 'curl …/whoami', 'Ask who is calling', ACC), ('n2', 'you are 10.0.1.2', 'My private address', VIO), ('n3', 'MASQUERADE', 'Turn on NAT at the router', WARN), ('n5', 'you are 10.0.2.1', 'Now only the router', GOOD), ('n6', 'iptables -t nat -S', 'Read the rule', PINK), ('n7', 'Rewrite the source', 'Home NAT in one line', GOOD)])
def s_firewall(C, D, dur):
    E = head('Firewalls', 'Rules, checked from the top.', C['w1'])
    E.append(Pop(card(1100, 300, ACC, 'Rule list', [('1   allow  tcp 22', GOOD), ('2   drop   tcp 8080', BAD), ('3   allow  everything else', GOOD)], 40, 36), 100, 330, C['w2']))
    E.append(Pop(card(540, 215, WARN, 'DROP', [('silence · time out', TXT)], 52, 32, True), 1260, 330, C['w3']))
    E.append(Pop(card(540, 215, BAD, 'REJECT', [('told no · refused', TXT)], 52, 32, True), 1260, 575, C['w4']))
    E.append(takeaway('Time out and refused point to different causes.', 850, C['w5'], GOOD, 1700)); return E
s_fwdemo = _lab('Drop versus reject', 'Same block, different symptom.', 'f1', RB, [('f1', '… -j DROP', 'Block port 8080 silently', WARN), ('f3', 'Connection timed out', 'Drop: silence', BAD), ('f4', 'iptables -F FORWARD', 'Remove the rule', ACC), ('f5', '… -j REJECT', 'Block it, and say so', PINK), ('f7', 'Failed to connect', 'Reject: told no, at once', BAD), ('f9', 'iptables -S FORWARD', 'Read the rule list', GOOD)])
def s_proxy(C, D, dur):
    E = head('Proxies and load balancers', 'The front door of your servers.', C['p1'])
    E.append(Pop(card(400, 200, ACC, 'Clients', [('know one address', TXT)], 44, 30, True), 100, 340, C['p2']))
    E.append(Pop(card(400, 200, WARN, 'Proxy', [('the front door', TXT)], 44, 32, True), 640, 340, C['p2'] + 0.8))
    E.append(Pop(card(400, 100, VIO, 'Server A', [], 32), 1180, 340, C['p4']))
    E.append(Pop(card(400, 100, GOOD, 'Server B', [], 32), 1180, 450, C['p4'] + 0.6))
    E.append(El(T('→', 'x', 60, MUTED), 540, 400, C['p2'] + 0.4, anim='fade')); E.append(El(T('→', 'x', 60, MUTED), 1090, 400, C['p4'], anim='fade'))
    E.append(Pop(chip('Reverse proxy: hide, secure, cache', GOOD, 30, 26, 12), 100, 640, C['p3'])); E.append(Pop(chip('Load balancer: share, check health', VIO, 30, 26, 12), 100, 730, C['p4'] + 0.5))
    E.append(takeaway('Often one tool, two jobs.', 850, C['p5'], GOOD, 1500)); return E
s_lbdemo = _lab('A real reverse proxy', 'One address, two servers.', 'l1', RB, [('l1', 'curl 10.0.1.1  ×4', 'One address, four requests', ACC), ('l2', 'A · B · A · B', 'The proxy takes turns', GOOD), ('l3', 'Servers stay hidden', 'Clients know the proxy only', VIO), ('l4', 'ss -ltn', 'Where does the proxy live?', WARN), ('l5', '10.0.1.1:80', 'Listening, waiting for clients', PINK)])
def s_errors(C, D, dur):
    E = head('Symptoms and causes', 'Match the symptom to the cause.', C['x1'])
    it = [('Times out, only via the router', 'Forwarding off, or no route', 'x2', ACC), ('Times out on one port', 'A drop rule', 'x3', WARN), ('Refused at once', 'A reject rule, or no listener', 'x4', BAD), ('Router address in every log', 'That is NAT', 'x5', VIO), ('502 Bad Gateway', 'Proxy cannot reach the server', 'x6', PINK), ('One server busy, one idle', 'Check the balancing', 'x7', GOOD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 108
        E.append(Pop(card(760, 94, col, '', [(a, TXT)], 4, 32), 100, y, C[cid])); E.append(El(T('→', 'x', 46, MUTED), 890, y + 20, C[cid] + 0.3, anim='fade')); E.append(Pop(card(820, 94, col, '', [(b, TXT)], 4, 28), 980, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['y1'])
    it = [('Myth: NAT is a firewall', 'Reality: it hides, not decides.', WARN, 'y2'), ('Myth: a blocked port is invisible', 'Reality: it times out or refuses.', VIO, 'y3'),
          ('Myth: balancing = round robin', 'Reality: many strategies.', BAD, 'y4'), ('Myth: a reverse proxy serves users', 'Reality: it serves the servers.', GOOD, 'y5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 32, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Name the job, then pick the tool.', 860, C['y6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['b1'])
    items = [('Routing table, default route', 'b2'), ('NAT: what the server sees', 'b3'), ('Accept, drop, reject', 'b4'), ('What a load balancer does', 'b5'), ('Reverse proxy vs balancer', 'b6'), ('Symptom → cause', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['z1'])
    it = [('1  Route', 'ip route', ACC, 'z2'), ('2  Forwarding', 'sysctl net.ipv4.ip_forward', VIO, 'z3'), ('3  Rules', 'sudo iptables -S', WARN, 'z4'), ('4  NAT gap', 'curl -s ifconfig.me', GOOD, 'z5'), ('5  Table', 'Symptom → cause', PINK, 'z6')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f10'])]
    qs = [('What does the default route do?', 'f11'), ('What does NAT change?', 'f12'), ('How do drop and reject differ?', 'f13'), ('Balancer or reverse proxy?', 'f14')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f15'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f15'] + 0.2))
    E.append(El(T('Objective covered: MC03-O06  ·  routing, NAT, firewalls, proxies', 'b', 28, TXT, maxw=960), 220, 748, C['f15'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f16']))
    E.append(El(T('Next: network boundaries', 'x', 46, ACC, maxw=1600), 100, 960, C['f17'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f18']))
    return E
FN = dict(hook=s_hook, routing=s_routing, routedemo=s_routedemo, nat=s_nat, natdemo=s_natdemo, firewall=s_firewall, fwdemo=s_fwdemo, proxy=s_proxy, lbdemo=s_lbdemo, errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(routing=('swap', ACC), routedemo=('eye', GOOD), nat=('tag', VIO), natdemo=('eye', GOOD), firewall=('gear', BAD), fwdemo=('eye', GOOD), proxy=('branch', GOOD), lbdemo=('eye', GOOD), errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'routedemo': [('t2', 1, 2, 4, 705, ''), ('t4', 1, 1, 296, 356, ''), ('t7', 4, 1, 534, 782, '')],
 'natdemo': [('n2', 1, 1, 4, 252, ''), ('n5', 1, 1, 4, 252, ''), ('n7', 2, 1, 4, 432, '')],
 'fwdemo': [('f3', 1, 1, 170, 484, ''), ('f7', 1, 1, 155, 568, ''), ('f9', 2, 1, 470, 812, '')],
 'lbdemo': [('l2', 1, 4, 4, 150, ''), ('l5', 2, 1, 366, 612, '')],
}
