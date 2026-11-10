import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 23  ·  DEVOPS BOOTCAMP'
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
       'ESTABLISHED': 'established', 'TIME-WAIT': 'time wait', 'UNCONN': 'unconnected', 'nc': 'n c', 'ss': 's s', 'curl': 'curl', 'localhost': 'local host', 'ICMP': 'I C M P', 'RTT': 'R T T', 'traceroute': 'trace route', 'nslookup': 'n s lookup', 'ping': 'ping', 'ip': 'I P', 'c0': 'c zero', 'lo': 'loopback', 'sport': 's port', 'MC03-O07': 'number seven', 'NAT': 'nat', 'iptables': 'I P tables', 'nginx': 'engine X', 'sysctl': 'sis control', 'rt': 'R T', 'MASQUERADE': 'masquerade', 'DROP': 'drop', 'REJECT': 'reject', 'FORWARD': 'forward', 'LAN': 'L A N', 'DMZ': 'D M Z', 'HAProxy': 'H A proxy', 'ACCEPT': 'accept', 'ctr': 'C T R', 'hnat': 'H nat', 'hst': 'H S T', 'veth': 'veeth', 'docker0': 'docker zero', 'eth0': 'E T H zero', 'br0': 'B R zero', 'VPC': 'V P C', 'IGW': 'I G W', 'EC2': 'E C two', 'AWS': 'A W S', 'DNAT': 'D nat', 'whoami': 'who am I', 'CIDR': 'cider', 't3.micro': 'T three micro', '8080': 'eighty eighty', '8000': 'eight thousand', 'Docker': 'Docker', 'iptables': 'I P tables'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)


SCENES = [
 ('hook', [
  c('h1', "Your app runs in a container, on a server, inside a cloud network. So who can reach whom?"),
  c('h2', "The answer is always the same: find the boundaries."),
  c('h3', "A boundary is a place where the rules change: the address range, the route, and what is allowed through."),
  c('h4', "Today you cross four of them: client to server, host to container, container to internet, and a cloud subnet."),
  c('h5', "First on a small network built on this computer, then live in a real cloud account."),
 ]),
 ('bound', [
  c('u1', "Start with one question: where does one network end, and another begin?"),
  c('u2', "Inside one network, machines reach each other directly. To leave it, they need a router, the gateway."),
  c('u3', "At every boundary, three things can change: the address range, the route, and the rules about what is allowed."),
  c('u4', "So when something cannot connect, do not guess. Ask: which boundary is it crossing, and what changed there?"),
  c('u5', "Here is the lab. A client, a router, and behind the router, a host that runs two containers, plus a server standing in for the internet."),
 ]),
 ('bdemo', [
  c('d1', "You are the client, ten dot zero dot one dot two. How do I reach the router? Type: ip route get 10.0.1.1"),
  c('d2', "Directly, on dev c zero, with no via. The router sits on my own network."),
  c('d3', "Now the host, on the other side. Type: ip route get 10.0.2.2"),
  c('d4', "This time it says via ten dot zero dot one dot one. The host is on another network, so my packets must go through the gateway. That is a boundary."),
  c('d5', "And the container, one seventy-two dot eighteen dot zero dot two? Type: ping -c 1 -W 1 172.18.0.2",
    "And the container, one seventy-two dot eighteen dot zero dot two? Type: ping, dash c, one, dash big W, one, one seventy-two dot eighteen dot zero dot two."),
  c('d6', "Destination net unreachable, from the router. It has no route to that network. From out here, the container does not exist."),
 ]),
 ('ctrs', [
  c('k1', "Now containers. A container is not a tiny virtual machine. It is an ordinary process, with its own private view of the system."),
  c('k2', "One part of that view is the network. The container gets its own network namespace: its own addresses, and its own routes."),
  c('k3', "A virtual cable, called a veth pair, joins that namespace to a virtual switch on the host, called a bridge."),
  c('k4', "Docker names its bridge docker0. The host acts as the container's router, and the bridge address is its gateway."),
  c('k5', "No Docker is installed here. I built the same pieces by hand, so you can see what Docker does for you."),
 ]),
 ('ctrdemo', [
  c('m1', "In this lab, the letters C T R mean: run the next command inside the container. Type: ctr ip -br addr",
    "In this lab, the letters C T R mean: run the next command inside the container. Type: C T R, I P, dash b r, addr."),
  c('m2', "One interface, E T H zero, address one seventy-two dot eighteen dot zero dot two. A private network, inside the host."),
  c('m3', "Its routes. Type: ctr ip route", "Its routes. Type: C T R, I P, route."),
  c('m4', "The default route points at the bridge, one seventy-two dot eighteen dot zero dot one. That is the container's gateway."),
  c('m5', "Reach the other container. Type: ctr ping -c 1 172.18.0.3",
    "Reach the other container. Type: C T R, ping, dash c, one, one seventy-two dot eighteen dot zero dot three."),
  c('m6', "Same bridge, so it works. Now the outside world. Type: ctr curl -sS -m 2 10.0.3.2:8080/whoami",
    "Same bridge, so it works. Now the outside world. Type: C T R, curl, dash s big S, dash m two, ten dot zero dot three dot two, colon, eighty eighty, slash who am I."),
  c('m7', "Timed out. The request left, but nobody outside knows how to answer a private address."),
  c('m8', "The fix is N A T, on the host. In this lab, H nat means: iptables, in the nat table, on the host. Type: hnat -A POSTROUTING -s 172.18.0.0/24 -j MASQUERADE",
    "The fix is nat, on the host. In this lab, H nat means: I P tables, in the nat table, on the host. Type: H nat, dash big A, post routing, dash s, one seventy-two dot eighteen dot zero dot zero, slash twenty-four, dash j, masquerade."),
  c('m9', "Same request again. Type: ctr curl -sS -m 2 10.0.3.2:8080/whoami",
    "Same request again. Type: C T R, curl, dash s big S, dash m two, ten dot zero dot three dot two, colon, eighty eighty, slash who am I."),
  c('m10', "You are ten dot zero dot two dot two. The server sees the host, not the container. The container hides behind the host, like your laptop behind a home router."),
 ]),
 ('pub', [
  c('p1', "One more direction. Someone outside wants to reach a service inside the container."),
  c('p2', "The container's address is private, so outsiders cannot aim at it. They can only aim at the host."),
  c('p3', "So the host listens on a port, and forwards the traffic to the container. Docker calls this publishing a port."),
  c('p4', "Underneath, it is a destination N A T rule. Masquerade rewrites the source address. This rewrites the destination."),
 ]),
 ('pubdemo', [
  c('q1', "Back on the client. The host is ten dot zero dot two dot two. Is anything on port eighty eighty? Type: curl -sS -m 2 10.0.2.2:8080",
    "Back on the client. The host is ten dot zero dot two dot two. Is anything on port eighty eighty? Type: curl, dash s big S, dash m two, ten dot zero dot two dot two, colon, eighty eighty."),
  c('q2', "Failed to connect. The host is there, but nothing is listening on that port."),
  c('q3', "Now publish it, the way Docker would. In this lab, publish forwards a host port to a container port. Type: publish 8080 8000",
    "Now publish it, the way Docker would. In this lab, publish forwards a host port to a container port. Type: publish, eighty eighty, eight thousand."),
  c('q4', "Ask again. Type: curl -s 10.0.2.2:8080/whoami",
    "Ask again. Type: curl, dash s, ten dot zero dot two dot two, colon, eighty eighty, slash who am I."),
  c('q5', "You are ten dot zero dot one dot two. The container answered, and it sees the real client. Only the destination was rewritten."),
  c('q6', "Look at the rule behind it. Type: hnat -S PREROUTING", "Look at the rule behind it. Type: H nat, dash big S, pre routing."),
  c('q7', "D nat, to one seventy-two dot eighteen dot zero dot two, port eight thousand. That is all a published port is."),
 ]),
 ('cloud', [
  c('v1', "Now the same ideas in the cloud. In Amazon's cloud, your private network is a V P C, a virtual private cloud."),
  c('v2', "You choose its address range, like 10.20.0.0/16, and cut it into subnets."),
  c('v3', "A public subnet has a route to an internet gateway. A private subnet has no such route."),
  c('v4', "That route is the only difference. A subnet is public because of its route table, not because of its name."),
  c('v5', "A security group is the firewall around each server. By default, it lets nothing in."),
  c('v6', "A private server that must reach out needs a N A T gateway. That one costs money, so we will not build it."),
  c('v7', "Now watch it live, in a real account. These are real screen recordings. My account details are blurred."),
 ]),
 ('awsA', [
  c('a1', "The console builds the network: a V P C, two subnets, two route tables, and an internet gateway."),
  c('a2', "Here is the public route table. Ten dot twenty slash sixteen stays local. And zero dot zero dot zero dot zero slash zero goes to the internet gateway.",
    "Here is the public route table. Ten dot twenty, slash sixteen, stays local. And zero dot zero dot zero dot zero, slash zero, goes to the internet gateway."),
  c('a3', "That second line is the whole definition of public: everything else leaves through the gateway."),
  c('a4', "Now the private route table."),
  c('a5', "One route only: local. Nothing leads to the internet. A server here can talk inside the V P C, and nowhere else."),
  c('a6', "The resource map draws it for you. One subnet routes to the internet. The other does not."),
 ]),
 ('awsB', [
  c('e1', "Now two real servers, one in each subnet. Both are T three micro, marked free tier eligible in this account."),
  c('e2', "Look at the security group: no inbound rules at all. Nothing from the internet can connect to either server."),
  c('e3', "Here they are, running."),
  c('e4', "The public server has a public address. The private server has none. Same account, same network, different subnet."),
  c('e5', "The private server's own page shows only a private address: ten dot twenty dot one thirty-three dot one fourteen.",
    "The private server's own page shows only a private address: ten dot twenty dot one thirty-three dot one fourteen."),
  c('e6', "Now the most important step. When you finish a cloud lab, delete what you built. First, terminate both servers."),
  c('e7', "Then delete the V P C. The console lists everything that goes with it."),
  c('e8', "Gone. Only the default network is left. Do this every time, so nothing keeps running, and nothing is billed. Check your own free tier before you try."),
 ]),
 ('errors', [
  c('x1', "Match the symptom to the boundary."),
  c('x2', "A container cannot be reached from another machine: the port is not published, or there is no route."),
  c('x3', "A container cannot reach the internet: no N A T, or no default route."),
  c('x4', "Refused on the published port: nothing is listening inside the container."),
  c('x5', "A cloud server is unreachable from the internet: no internet gateway route, or no public address."),
  c('x6', "A private server cannot download updates: it needs a N A T gateway, or a different design."),
  c('x7', "Times out only in the cloud: check the security group, then the route table."),
 ]),
 ('myths', [
  c('y1', "Four myths to drop."),
  c('y2', "Myth one: a container is its own computer. It shares the host's kernel. Only its view is separate."),
  c('y3', "Myth two: a private subnet is secure by itself. It is only unreachable until someone adds a route or a rule."),
  c('y4', "Myth three: every server in a public subnet is public. It also needs a public address, and a rule that allows the traffic."),
  c('y5', "Myth four: a container's address works outside the host. It is private to the host, unless you publish a port."),
  c('y6', "Find the boundary, then check the address, the route, and the rule."),
 ]),
 ('rubric', [
  c('r1', "Here is how you check your own understanding."), c('r2', "Explain what a network boundary is, and what can change at one."),
  c('r3', "Read the output of ip route get, and say whether the destination is direct or via a gateway."),
  c('r4', "Explain how a container reaches the internet."), c('r5', "Explain what publishing a port does."),
  c('r6', "Explain the difference between a public and a private subnet."), c('r7', "Delete your cloud resources, and explain why."), c('r8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in the virtual machine you built."),
  c('z2', "One: run ip route get 8.8.8.8, and find your gateway.", "One: run I P, route get, eight dot eight dot eight dot eight, and find your gateway."),
  c('z3', "Two: if Docker is installed, run docker network ls, and find the bridge."),
  c('z4', "Three: on paper, draw a V P C with one public subnet, one private subnet, and two route tables."),
  c('z5', "Four: if you build it in a free account, use free resources only, and delete everything when you finish. Servers first, then the V P C."),
  c('z6', "Five: for each symptom in the table, write the boundary and the cause."),
  c('z7', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f10', "Quick check."), c('f11', "What can change at a boundary?"), c('f12', "How does a container reach the internet?"),
  c('f13', "What makes a subnet public?"), c('f14', "What must you do when a cloud lab ends?"),
  c('f15', "Objective covered: MC03-O07.", "Objective covered: number seven, in the computer networking masterclass."),
  c('f16', "Pause the video, and answer out loud."), c('f17', "Next: diagnosing D N S, port, firewall, T L S and routing failures in a lab."),
  c('f18', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h5': 0.5, 'u5': 0.5, 'd6': 0.5, 'k5': 0.5, 'm10': 0.5, 'p4': 0.5, 'q7': 0.5, 'v7': 0.5, 'a6': 0.5, 'e8': 0.8, 'x7': 0.5, 'y6': 0.5, 'r8': 0.5, 'z7': 14.0, 'f16': 10.0}
CHAP = {'bound': 'Network boundaries', 'bdemo': 'Live: client, router, host', 'ctrs': 'Containers', 'ctrdemo': "Live: a container's network", 'pub': 'Publishing a port', 'pubdemo': 'Live: publish a port',
        'cloud': 'Cloud subnets', 'awsA': 'Live in AWS: public vs private', 'awsB': 'Live in AWS: two servers, then clean up', 'errors': 'Symptoms and causes', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Networking  ·  Lesson 23', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
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
def photo(path, w, h, col):
    im = Image.open(path).convert('RGB'); im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.5))
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=tuple(col)[:3] + (255,))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=20, fill=255)
    out.paste(im, (6, 6), m); return out
def hbox(w, h, col=None):
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im); c_ = tuple(col or WARN)[:3]
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=8, fill=c_ + (60,), outline=c_ + (255,), width=4); return im

RB = 'REAL RECORDING  ·  lab network on this computer'
RA = 'REAL RECORDING  ·  AWS console  ·  details blurred'
AS = '/home/claude/academy/lesson23/assets/'
def s_hook(C, D, dur):
    E = [El(T('Where does one network end?', 'x', 60), 100, 130, C['h1'])]
    it = [('Client → server', 'Router, gateway', ACC, 'h4'), ('Host → container', 'Bridge, namespace', VIO, 'h4'), ('Container → internet', 'NAT on the way out', WARN, 'h4'), ('Cloud subnet', 'Public or private', GOOD, 'h4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(420, 215, col, n, [(s_, TXT)], 36, 28), 100 + i * 440, 300, C[cid] + 0.9 * i))
    E.append(Pop(chip('address  ·  route  ·  rules', GOOD, 34, 28, 14), 100, 600, C['h3'] + 0.6))
    E.append(takeaway('Find the boundary first.', 740, C['h5'], GOOD, 1600)); return E
def s_bound(C, D, dur):
    E = head('Network boundaries', 'Where the rules change.', C['u1'])
    E.append(Pop(card(540, 215, ACC, 'Address', [('a different range', TXT)], 44, 34), 100, 330, C['u3']))
    E.append(Pop(card(540, 215, VIO, 'Route', [('through a gateway', TXT)], 44, 34), 690, 330, C['u3'] + 0.7))
    E.append(Pop(card(540, 215, WARN, 'Rules', [('what may pass', TXT)], 44, 34), 1280, 330, C['u3'] + 1.4))
    E.append(ill(C['u5'] - 0.2, 1400, 170))
    names = [('client', '10.0.1.2', ACC), ('router r1', '3 networks', VIO), ('host', '10.0.2.2', WARN), ('c1 · c2', '172.18.0.x', GOOD)]
    for i, (n, s_, col) in enumerate(names):
        E.append(Pop(card(380, 150, col, n, [(s_, TXT)], 36, 28, True), 100 + i * 440, 590, C['u5'] + 0.5 * i))
        if i < 3: E.append(El(T('→', 'x', 50, MUTED), 490 + i * 440, 640, C['u5'] + 0.5 * i + 0.3, anim='fade'))
    E.append(Pop(card(380, 150, BAD, 'server', [('10.0.3.2 · "internet"', TXT)], 36, 26, True), 540, 780, C['u5'] + 2.2))
    E.append(takeaway('Ask: which boundary, and what changed?', 960, C['u4'], GOOD, 1700)); return E
s_bdemo = _lab('Client, router, host', 'Direct, or via a gateway?', 'd1', RB, [('d1', 'ip route get', 'How do I reach it?', ACC), ('d2', 'dev c0  (direct)', 'Router: my own network', GOOD), ('d3', 'ip route get 10.0.2.2', 'The host, one hop away', VIO), ('d4', 'via 10.0.1.1', 'Other network: a boundary', WARN), ('d5', 'ping 172.18.0.2', 'The container, from outside', PINK), ('d6', 'Net Unreachable', 'No route to that network', BAD)])
def s_ctrs(C, D, dur):
    E = head('Containers', 'A private network inside the host.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 215, ACC, 'Namespace', [('own addresses, routes', TXT)], 44, 28), 100, 330, C['k2']))
    E.append(Pop(card(540, 215, VIO, 'veth pair', [('a virtual cable', TXT)], 44, 34), 690, 330, C['k3']))
    E.append(Pop(card(540, 215, WARN, 'Bridge', [('a virtual switch', TXT)], 44, 34), 1280, 330, C['k3'] + 1.0))
    E.append(Pop(chip('docker0  =  the bridge, the gateway', GOOD, 30, 26, 12), 100, 640, C['k4']))
    E.append(takeaway('No Docker here: the same pieces, built by hand.', 850, C['k5'], GOOD, 1700)); return E
s_ctrdemo = _lab("A container's network", 'Inside, and the way out.', 'm1', RB, [('m1', 'ctr ip -br addr', 'Run inside the container', ACC), ('m4', 'default via 172.18.0.1', 'The bridge is the gateway', VIO), ('m5', 'ping c2  works', 'Same bridge, same network', GOOD), ('m7', 'Connection timed out', 'No way back for private', BAD), ('m8', 'MASQUERADE', 'NAT on the host', WARN), ('m10', 'you are 10.0.2.2', 'The server sees the host', GOOD)])
def s_pub(C, D, dur):
    E = head('Publishing a port', 'The way in.', C['p1'])
    E.append(Pop(card(400, 200, ACC, 'Outsider', [('aims at the host', TXT)], 44, 30, True), 100, 340, C['p2']))
    E.append(Pop(card(400, 200, WARN, 'Host :8080', [('forwards the traffic', TXT)], 44, 28, True), 640, 340, C['p3']))
    E.append(Pop(card(400, 200, GOOD, 'Container :8000', [('private address', TXT)], 36, 30, True), 1180, 340, C['p3'] + 0.8))
    E.append(El(T('→', 'x', 60, MUTED), 540, 400, C['p3'], anim='fade')); E.append(El(T('→', 'x', 60, MUTED), 1090, 400, C['p3'] + 0.5, anim='fade'))
    E.append(Pop(chip('docker run -p 8080:8000', VIO, 34, 28, 14), 100, 640, C['p3'] + 0.8))
    E.append(takeaway('Publishing a port is destination NAT.', 850, C['p4'], GOOD, 1700)); return E
s_pubdemo = _lab('Publish a port', 'Refused, then answered.', 'q1', RB, [('q1', 'curl host:8080', 'Anything there?', ACC), ('q2', 'Failed to connect', 'Nothing listening yet', BAD), ('q3', 'publish 8080 8000', 'Forward it to the container', WARN), ('q5', 'you are 10.0.1.2', 'Answered, real client seen', GOOD), ('q6', 'iptables -S PREROUTING', 'Read the rule behind it', PINK), ('q7', '-j DNAT --to 172.18.0.2:8000', 'Destination rewritten', VIO)])
def s_cloud(C, D, dur):
    E = head('Cloud subnets', 'A VPC, cut into public and private.', C['v1']); E.append(ill(C['v1'] + 0.2, 1400, 170))
    E.append(Pop(card(1100, 560, ACC, 'VPC  10.20.0.0/16', [], 36), 100, 330, C['v2']))
    E.append(Pop(card(500, 190, GOOD, 'Public subnet', [('0.0.0.0/0 → internet gateway', TXT)], 36, 24), 140, 410, C['v3']))
    E.append(Pop(card(500, 190, VIO, 'Private subnet', [('local only', TXT)], 36, 28), 140, 640, C['v3'] + 1.0))
    E.append(Pop(card(440, 190, WARN, 'Security group', [('allows nothing in', TXT)], 36, 28), 690, 410, C['v5']))
    E.append(Pop(card(440, 190, BAD, 'NAT gateway', [('costs money · skipped', TXT)], 36, 24), 690, 640, C['v6']))
    E.append(Pop(card(560, 215, ACC, 'Internet gateway', [('the door out', TXT)], 40, 32, True), 1260, 330, C['v3'] + 0.5))
    E.append(Pop(card(560, 215, GOOD, 'Public = a route', [('not a name', TXT)], 40, 32, True), 1260, 575, C['v4']))
    E.append(takeaway('Live next: the real console.', 930, C['v7'], GOOD, 1500)); return E
def _aws(title, sub, first, shots, steps, boxes):
    def f(C, D, dur):
        E = head(title, sub, C[first]); E.append(real(C[first] + 0.2, RA, 1260, 286))
        E.append(Pop(card(1100, 590, ACC, '', [], 4), 100, 330, C[first]))
        ev = [(C[cid], 0, ('p', name)) for cid, name in shots] + [(C[cid] + 0.2, 1, ('b', rect, col)) for cid, rect, col in boxes]
        for _t, _k, d_ in sorted(ev, key=lambda e: (e[0], e[1])):
            if d_[0] == 'p': E.append(Pop(photo(AS + d_[1] + '.jpg', 1076, 534, ACC), 100, 345, _t))
            else: E.append(Pop(hbox(d_[1][2], d_[1][3], d_[2]), d_[1][0], d_[1][1], _t))
        n = len(steps); gap = min(120, (1035 - 345) // n)
        for i, (cid, t, sb, col) in enumerate(steps): E.append(Pop(card(560, gap - 12, col, t, [(sb, TXT)], 30, 25), 1260, 345 + i * gap, C[cid] + 0.2))
        return E
    return f
s_awsA = _aws('Public versus private', 'The route table decides.', 'a1',
  [('a1', 'create_workflow'), ('a2', 'public_rt'), ('a4', 'private_rt'), ('a6', 'map_details')],
  [('a1', 'VPC + 2 subnets', 'Built by the console', ACC), ('a2', '0.0.0.0/0 → igw', 'Public route table', GOOD), ('a3', 'That route = public', 'Everything else leaves', WARN), ('a4', 'Private route table', 'Main table', VIO), ('a5', '10.20.0.0/16  local', 'Nothing leads out', BAD), ('a6', 'Resource map', 'One subnet routes out', PINK)],
  [('a3', (266, 716, 902, 30), WARN), ('a5', (266, 716, 902, 30), BAD), ('a6', (1030, 748, 146, 40), WARN)])
s_awsB = _aws('Two servers, then clean up', 'Public address, or none.', 'e1',
  [('e1', 'inst_net_settings'), ('e3', 'inst_both_list'), ('e5', 'inst_private_detail'), ('e6', 'inst_terminate_dialog'), ('e7', 'vpc_delete_dialog2'), ('e8', 'vpc_deleted2')],
  [('e1', 't3.micro  ×2', 'One per subnet', ACC), ('e2', 'No inbound rules', 'Nothing may connect in', WARN), ('e4', 'Public IP vs none', 'Different subnet', GOOD), ('e5', '10.20.133.114', 'Private address only', VIO), ('e6', 'Terminate both', 'Servers first', BAD), ('e8', 'Delete the VPC', 'Nothing left running', GOOD)],
  [('e2', (146, 682, 460, 28), WARN), ('e4', (1012, 494, 90, 22), BAD), ('e4', (1012, 516, 90, 22), GOOD), ('e5', (566, 472, 176, 42), BAD), ('e5', (858, 472, 150, 42), GOOD), ('e8', (280, 458, 364, 28), GOOD)])
def s_errors(C, D, dur):
    E = head('Symptoms and causes', 'Match the symptom to the boundary.', C['x1'])
    it = [('Container not reachable', 'Port not published, or no route', 'x2', ACC), ('Container has no internet', 'No NAT, or no default route', 'x3', WARN), ('Refused on published port', 'Nothing listening inside', 'x4', BAD), ('Cloud server unreachable', 'No gateway route, or no public IP', 'x5', VIO), ('Private server cannot update', 'Needs a NAT gateway', 'x6', PINK), ('Times out, only in the cloud', 'Security group, then routes', 'x7', GOOD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 108
        E.append(Pop(card(760, 94, col, '', [(a, TXT)], 4, 32), 100, y, C[cid])); E.append(El(T('→', 'x', 46, MUTED), 890, y + 20, C[cid] + 0.3, anim='fade')); E.append(Pop(card(820, 94, col, '', [(b, TXT)], 4, 28), 980, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['y1'])
    it = [('Myth: a container is its own computer', 'Reality: it shares the kernel.', WARN, 'y2'), ('Myth: private subnet = secure', 'Reality: just no route yet.', VIO, 'y3'),
          ('Myth: public subnet = public server', 'Reality: needs an address and a rule.', BAD, 'y4'), ('Myth: container IP works outside', 'Reality: publish a port.', GOOD, 'y5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 30, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Boundary, then address, route, rule.', 860, C['y6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['r1'])
    items = [('What a boundary changes', 'r2'), ('Direct or via a gateway', 'r3'), ('How a container gets out', 'r4'), ('What publishing a port does', 'r5'), ('Public vs private subnet', 'r6'), ('Delete cloud resources, and why', 'r7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['r8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['z1'])
    it = [('1  Gateway', 'ip route get 8.8.8.8', ACC, 'z2'), ('2  Bridge', 'docker network ls', VIO, 'z3'), ('3  Draw', 'VPC · 2 subnets · 2 tables', WARN, 'z4'), ('4  Clean up', 'Servers first, then VPC', BAD, 'z5'), ('5  Table', 'Symptom → boundary', PINK, 'z6')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f10'])]
    qs = [('What can change at a boundary?', 'f11'), ('How does a container reach the internet?', 'f12'), ('What makes a subnet public?', 'f13'), ('What must you do when a cloud lab ends?', 'f14')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f15'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f15'] + 0.2))
    E.append(El(T('Objective covered: MC03-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f15'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f16']))
    E.append(El(T('Next: diagnose DNS, port, firewall, TLS and routing failures', 'x', 40, ACC, maxw=1700), 100, 960, C['f17'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f18']))
    return E
FN = dict(hook=s_hook, bound=s_bound, bdemo=s_bdemo, ctrs=s_ctrs, ctrdemo=s_ctrdemo, pub=s_pub, pubdemo=s_pubdemo, cloud=s_cloud, awsA=s_awsA, awsB=s_awsB, errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(bound=('swap', ACC), bdemo=('eye', GOOD), ctrs=('gear', VIO), ctrdemo=('eye', GOOD), pub=('link', WARN), pubdemo=('eye', GOOD), cloud=('branch', GOOD), awsA=('eye', GOOD), awsB=('eye', GOOD), errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'bdemo': [('d2', 1, 1, 136, 236, ''), ('d4', 1, 1, 136, 328, ''), ('d6', 2, 1, 378, 796, '')],
 'ctrdemo': [('m2', 2, 1, 482, 686, ''), ('m4', 1, 1, 4, 342, ''), ('m7', 1, 1, 166, 474, ''), ('m10', 1, 1, 4, 252, '')],
 'pubdemo': [('q2', 1, 1, 150, 418, ''), ('q5', 1, 1, 4, 252, ''), ('q7', 2, 1, 618, 1072, ''), ('q7', 3, 1, 4, 160, '')],
}
