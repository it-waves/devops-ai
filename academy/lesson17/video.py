import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 17  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

# ---- speech helpers: IPs and slash numbers are spoken the way people say them ----
_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = {'DNS': 'D N S', 'IP': 'I P', 'IPv4': 'I P v four', 'CIDR': 'cider', 'DHCP': 'D H C P', 'TCP': 'T C P', 'UDP': 'U D P', 'ipwhat': 'I P what', 'enp0s3': 'e n p zero s three',
       'nameserver': 'name server', 'curl': 'curl', 'localhost': 'local host'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w.])/(\d{1,2})\b', lambda m: 'slash ' + _w99(int(m.group(1))), s)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in _SP) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "Every device on a network needs an address, just like every house needs one."),
  c('h2', "Today you learn to read that address: what the four numbers mean, what slash twenty-four means, and where the gateway fits in."),
  c('h3', "You will check them live, in a real terminal, and work out the maths yourself."),
  c('h4', "After this, a network address will never look like a secret code again."),
 ]),
 ('address', [
  c('a1', "First, the I P address."), c('a2', "An I P address identifies one device on a network."),
  c('a3', "I P version four uses four numbers, each from zero to two hundred fifty-five, separated by dots. Like this: 192.168.1.25.",
    "I P version four uses four numbers, each from zero to two hundred fifty-five, separated by dots. Like this: one ninety-two dot one sixty-eight dot one dot twenty-five."),
  c('a4', "Part of the address names the network. The rest names the device on that network."),
  c('a5', "Think of a street and a house number. The street is the network. The house is the device."),
  c('a6', "Two devices on the same street can talk to each other directly."),
 ]),
 ('ipdemo', [
  c('i1', "Let us look at the address of this computer's network card. It is called enp0s3, the usual name in a VirtualBox machine like yours. Type: ip -br addr show enp0s3",
    "Let us look at the address of this computer's network card. It is called e n p zero s three, the usual name in a VirtualBox machine like yours. Type: i p, dash b r, addr, show, e n p zero s three."),
  c('i2', "The state says U P, so the card is working."),
  c('i3', "And here is the address: 192.168.1.25, then slash twenty-four.", "And here is the address: one ninety-two dot one sixty-eight dot one dot twenty-five, then slash twenty-four."),
  c('i4', "That slash twenty-four says how much of the address names the network. We decode it soon."),
  c('i5', "Now the routes. Type: ip route show dev enp0s3", "Now the routes. Type: i p, route, show, dev, e n p zero s three."),
  c('i6', "The second line says: the network 192.168.1.0/24 is directly reachable from this card.", "The second line says: the network one ninety-two dot one sixty-eight dot one dot zero, slash twenty-four, is directly reachable from this card."),
  c('i7', "The first line says: for everything else, go via 192.168.1.1. That is the gateway.", "The first line says: for everything else, go via one ninety-two dot one sixty-eight dot one dot one. That is the gateway."),
  c('i8', "Your numbers will differ, but the shape is the same: an address, a network, and a gateway."),
 ]),
 ('private', [
  c('p1', "Not every address works everywhere."), c('p2', "Some ranges are private: reserved for use inside homes, offices and cloud networks."),
  c('p3', "There are three. Ten dot anything. One seventy-two dot sixteen up to one seventy-two dot thirty-one. And one ninety-two dot one sixty-eight dot anything."),
  c('p4', "Anyone can use them inside their own network, so the same private address exists in millions of places."),
  c('p5', "Everything else is public. A public address is unique, and reachable from the internet."),
  c('p6', "Your home router has one public address, and shares it with every private device behind it. We cover how, in a later lesson."),
  c('p7', "Careful: one seventy-two dot thirty-two is public. The private range stops at thirty-one."),
 ]),
 ('privdemo', [
  c('v1', "Let us ask the computer. We wrote a small helper called ipwhat, with Python's standard address library. Type: ipwhat 192.168.1.25",
    "Let us ask the computer. We wrote a small helper called I P what, with Python's standard address library. Type: I P what, one ninety-two dot one sixty-eight dot one dot twenty-five."),
  c('v2', "Private. A home-style address."),
  c('v3', "Next. Type: ipwhat 172.20.5.9", "Next. Type: I P what, one seventy-two dot twenty dot five dot nine."),
  c('v4', "Also private, because twenty sits between sixteen and thirty-one."),
  c('v5', "Now a famous one. Type: ipwhat 8.8.8.8", "Now a famous one. Type: I P what, eight dot eight dot eight dot eight."),
  c('v6', "Public. A real address on the internet."),
 ]),
 ('cidr', [
  c('c1', "Now the slash. This is called CIDR notation, said like cider."),
  c('c2', "An address is thirty-two bits. Here is ours in binary, in four groups of eight."),
  c('c3', "The number after the slash says how many bits, counted from the left, name the network. Slash twenty-four: the first twenty-four bits."),
  c('c4', "The last eight bits are left for devices. Eight bits give two hundred fifty-six addresses."),
  c('c5', "Two are reserved: the first names the network itself, and the last is the broadcast address."),
  c('c6', "A bigger slash number means a smaller network. Slash twenty-six leaves six bits, so sixty-four addresses. Slash sixteen leaves sixteen bits, so sixty-five thousand five hundred thirty-six."),
  c('c7', "A subnet is just one of these slices."),
  c('c8', "The subnet mask says the same thing in another way: 255.255.255.0 means slash twenty-four.", "The subnet mask says the same thing in another way: two fifty-five dot two fifty-five dot two fifty-five dot zero means slash twenty-four."),
 ]),
 ('cidrdemo', [
  c('u1', "Let us do the maths with the computer. A second helper, called subnet, lays it out. Type: subnet 192.168.1.0/24",
    "Let us do the maths with the computer. A second helper, called subnet, lays it out. Type: subnet, one ninety-two dot one sixty-eight dot one dot zero, slash twenty-four."),
  c('u2', "The network, and the mask: 255.255.255.0.", "The network, and the mask: two fifty-five dot two fifty-five dot two fifty-five dot zero."),
  c('u3', "Devices live from dot one to dot two fifty-four. Dot two fifty-five is the broadcast. That makes two hundred fifty-four hosts."),
  c('u4', "Now cut it smaller. Type: subnet 192.168.1.0/26", "Now cut it smaller. The same command, with slash twenty-six."),
  c('u5', "The mask now ends in one ninety-two, and only sixty-two hosts fit, dot one to dot sixty-two."),
  c('u6', "And a big one. Type: subnet 10.0.0.0/16", "And a big one. Type: subnet, ten dot zero dot zero dot zero, slash sixteen."),
  c('u7', "The mask is 255.255.0.0, and sixty-five thousand five hundred thirty-four hosts fit.", "The mask is two fifty-five dot two fifty-five dot zero dot zero, and sixty-five thousand five hundred thirty-four hosts fit."),
  c('u8', "Same method every time. A smaller slash number means a bigger network."),
 ]),
 ('gateway', [
  c('g1', "Now the gateway."), c('g2', "When your computer sends a packet, it asks one question: is the destination on my own subnet?"),
  c('g3', "If yes, it sends the packet directly to that device."),
  c('g4', "If no, it hands the packet to the gateway. That is the router, and it forwards the packet onward."),
  c('g5', "The gateway must sit on your own subnet, because it is the one door you can reach directly."),
  c('g6', "Your computer decides using your address and your slash number."),
 ]),
 ('gwdemo', [
  c('w1', "Let us ask the same question. A third helper, called inside, checks a destination against a subnet. Type: inside 192.168.1.0/24 192.168.1.200",
    "Let us ask the same question. A third helper, called inside, checks a destination against a subnet. Type: inside, one ninety-two dot one sixty-eight dot one dot zero, slash twenty-four, one ninety-two dot one sixty-eight dot one dot two hundred."),
  c('w2', "Inside. So it is sent directly."),
  c('w3', "Now an internet address. Type: inside 192.168.1.0/24 8.8.8.8", "Now an internet address. The same command, with eight dot eight dot eight dot eight."),
  c('w4', "Outside. So it goes to the gateway."),
  c('w5', "One more thing: names. Type: grep nameserver /etc/resolv.conf", "One more thing: names. Type: grep, name server, slash e t c, slash resolve dot conf."),
  c('w6', "These are the D N S servers this computer asks. They are I P addresses too. Public ones, in this case."),
 ]),
 ('four', [
  c('q1', "Every working network connection needs four settings."), c('q2', "One: an I P address, which says who you are."),
  c('q3', "Two: a subnet mask, or slash number, which says who is local."), c('q4', "Three: a gateway, which is the way out."),
  c('q5', "Four: a D N S server, which turns names into addresses."), c('q6', "Check these four, in this order, and most basic network problems become simple."),
 ]),
 ('errors', [
  c('e1', "Match the symptom to the setting."),
  c('e2', "An address starting 169.254 means that D H C P, the service that hands out addresses, did not answer.", "An address starting one sixty-nine dot two fifty-four means that D H C P, the service that hands out addresses, did not answer."),
  c('e3', "Network is unreachable: there is no route, often a missing gateway."),
  c('e4', "Local devices work but the internet does not: check the gateway."),
  c('e5', "An address works but a name fails: check the D N S server."), c('e6', "Random drops: two devices may share one address."),
 ]),
 ('myths', [
  c('k1', "Watch out for four common myths."), c('k2', "Myth one: private addresses are secure. They are only not routed on the internet. That is not a security feature."),
  c('k3', "Myth two: every network is slash twenty-four. Any size from slash zero to slash thirty-two is possible."),
  c('k4', "Myth three: all two hundred fifty-six addresses are usable. Two are reserved, so two hundred fifty-four are."),
  c('k5', "Myth four: the gateway can be any device. It must be a router on your own subnet."), c('k6', "Know the real size, then count."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Explain the network part and the host part of an I P address."),
  c('b3', "Say whether an address is private or public."), c('b4', "Read slash notation and name the mask."),
  c('b5', "Work out how many hosts fit in a subnet."), c('b6', "Say when traffic goes to the gateway."), c('b7', "Name the four settings a working network needs."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('y1', "Your turn, in the virtual machine you built."), c('y2', "One: run ip -br addr, and find your own address and slash number.", "One: run i p, dash b r, addr, and find your own address and slash number."),
  c('y3', "Two: run ip route, and find your gateway. With the default VirtualBox network you will probably see 10.0.2.15 and a gateway of 10.0.2.2.",
    "Two: run i p route, and find your gateway. With the default VirtualBox network you will probably see ten dot zero dot two dot fifteen, and a gateway of ten dot zero dot two dot two."),
  c('y4', "Three: decide whether your address is private or public, using the three ranges."), c('y5', "Four: work out how many hosts your slash number allows."),
  c('y6', "Five: read your D N S server with grep nameserver. On Ubuntu it may show a local address, and that is fine.", "Five: read your D N S server with grep name server. On Ubuntu it may show a local address, and that is fine."),
  c('y7', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f1', "Quick check."), c('f2', "What do the network part and the host part of an address mean?"), c('f3', "Which three ranges are private?"),
  c('f4', "What does slash twenty-six mean, and how many hosts fit?"), c('f8', "When does a computer use the gateway?"),
  c('f9', "Objective covered: MC03-O01.", "Objective covered: number one, in the computer networking masterclass."),
  c('f5', "Pause the video, and answer out loud."), c('f6', "Next: T C P, U D P, and ports."), c('f7', "Subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h4': 0.5, 'a6': 0.5, 'i8': 0.5, 'p7': 0.5, 'v6': 0.5, 'c8': 0.5, 'u8': 0.5, 'g6': 0.5, 'w6': 0.5, 'q6': 0.5, 'e6': 0.5, 'k6': 0.5, 'b8': 0.5, 'y7': 14.0, 'f5': 10.0}
CHAP = {'address': 'The IP address', 'ipdemo': 'Live: your address and gateway', 'private': 'Private and public', 'privdemo': 'Live: private or public', 'cidr': 'CIDR: the slash', 'cidrdemo': 'Live: subnet maths',
        'gateway': 'The gateway', 'gwdemo': 'Live: direct or gateway', 'four': 'The four settings', 'errors': 'Symptoms and causes', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Networking  ·  Lesson 17', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def photo(path, w, h, col):
    im = Image.open(path).convert('RGB'); im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.5))
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=tuple(col)[:3] + (255,))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=20, fill=255)
    out.paste(im, (6, 6), m); return out
PHOTO = '/home/claude/academy/lesson17/assets/photo_l17_router.jpg'
PHOTO_CREDIT = open('/home/claude/academy/lesson17/assets/credit.txt').read().strip() if os.path.exists('/home/claude/academy/lesson17/assets/credit.txt') else 'Photo via Wikimedia Commons'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
def router_art(w=740, h=500):
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out); col = tuple(ACC)[:3]
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=col + (255,)); d.rounded_rectangle([6, 6, w + 5, h + 5], radius=20, fill=(12, 30, 34, 255))
    cx = (w + 12) // 2
    for dx in (-190, 190):                                   # antennas
        d.rounded_rectangle([cx + dx - 14, 70, cx + dx + 14, 250], radius=12, fill=(70, 90, 96, 255))
    d.rounded_rectangle([cx - 300, 230, cx + 300, 400], radius=30, fill=(226, 234, 236, 255))
    d.rounded_rectangle([cx - 300, 360, cx + 300, 400], radius=20, fill=(190, 202, 206, 255))
    for i, c2 in enumerate([tuple(GOOD)[:3], tuple(GOOD)[:3], tuple(WARN)[:3], (150, 165, 170)]):
        d.ellipse([cx - 230 + i * 56, 288, cx - 206 + i * 56, 312], fill=c2 + (255,))
    for i in range(4):                                         # LAN ports
        d.rounded_rectangle([cx + 20 + i * 62, 282, cx + 66 + i * 62, 322], radius=6, fill=(40, 52, 58, 255))
    f = ImageFont.truetype(MONO, 26); d.text((cx - 300, 430), '192.168.1.1', font=f, fill=col + (255,)); d.text((cx + 40, 430), 'the gateway', font=f, fill=(190, 202, 206, 255))
    return out
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
def trio3(E, C, items, ids, y=330, h=230, w=540):
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def grid6(E, C, it, y0=330):
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, y0 + (i // 3) * 245, C[cid]))

RB = 'REAL RECORDING  ·  Ubuntu 24.04 terminal'
def s_hook(C, D, dur):
    E = [El(T('Every device needs an address', 'x', 64), 100, 130, C['h1'])]
    if os.path.exists(PHOTO):
        E.append(Pop(photo(PHOTO, 740, 500, ACC), 1080, 250, C['h1']))
        E.append(El(T(PHOTO_CREDIT, 'm', 22, MUTED, maxw=740), 1080, 770, C['h1'] + 0.5, anim='fade'))
    else:
        E.append(Pop(router_art(), 1080, 250, C['h1']))
        E.append(El(T('ILLUSTRATION  ·  not a photo', 'm', 24, MUTED, maxw=740), 1080, 770, C['h1'] + 0.5, anim='fade'))
    E.append(Pop(card(900, 150, ACC, 'An address', [('Who is this device?', TXT)], 46, 36), 100, 250, C['h2']))
    E.append(Pop(card(900, 150, WARN, 'A subnet and a gateway', [('Where does the traffic go?', TXT)], 46, 36), 100, 430, C['h2'] + 2.5))
    bs = [badge(n, F('b', 34), INK, col, padx=26, pady=14, r=26) for n, col in [('IP', ACC), ('Private', VIO), ('CIDR', GOOD), ('Gateway', WARN), ('DNS', PINK)]]
    E.append(El(T('Today, live', 'b', 32, MUTED), 100, 640, C['h3'], anim='fade'))
    bx = 100
    for i, b in enumerate(bs): E.append(Pop(b, bx, 700, C['h3'] + 0.3 + i * 0.5)); bx += b.width + 24
    E.append(takeaway('Read any network address with confidence.', 840, C['h4'], GOOD, 1600)); return E
def s_address(C, D, dur):
    E = head('The IP address', 'One number for one device.', C['a1'])
    a = mono('192.168.1.', ACC, 120); b = mono('25', WARN, 120); x0 = 100
    E.append(Pop(a, x0, 330, C['a3'])); E.append(Pop(b, x0 + a.width - 6, 330, C['a3'] + 0.6))
    E.append(Pop(chip('network part', ACC, 34, 24, 12), x0 + 120, 500, C['a4'])); E.append(Pop(chip('host part', WARN, 34, 24, 12), x0 + a.width + 20, 500, C['a4'] + 0.8))
    for i, (s, col) in enumerate([('4 numbers', VIO), ('each 0 to 255', GOOD), ('32 bits', PINK)]): E.append(Pop(chip(s, col, 32, 22, 12), 1180 + (i % 2) * 330 if False else 1330, 330 + i * 90, C['a3'] + 1.0 + i * 0.5))
    E.append(Pop(card(840, 170, ACC, 'The street', [('The network', TXT)], 46, 34), 100, 620, C['a5']))
    E.append(Pop(card(840, 170, WARN, 'The house', [('The device', TXT)], 46, 34), 980, 620, C['a5'] + 1.8))
    E.append(takeaway('Same street: talk directly.', 860, C['a6'], GOOD, 1500)); return E
s_ipdemo = _lab('Your address, live', 'Address, network, gateway.', 'i1', RB, [('i1', 'ip -br addr', 'Show the address', ACC), ('i2', 'UP', 'The card works', GOOD), ('i3', '192.168.1.25/24', 'Address and slash', VIO), ('i5', 'ip route', 'Show the routes', WARN), ('i6', '192.168.1.0/24', 'The local network', PINK), ('i7', 'default via .1', 'The gateway', BAD)])
def s_private(C, D, dur):
    E = head('Private and public', 'Three private ranges.', C['p1'])
    it = [('10.0.0.0/8', 'Big networks, clouds', ACC, 'p3'), ('172.16.0.0/12', '172.16 to 172.31', VIO, 'p3'), ('192.168.0.0/16', 'Homes, small offices', WARN, 'p3')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 230, col, n, [(s, TXT)], 40, 32), 100 + i * 590, 330, C[cid] + i * 1.2))
    E.append(Pop(card(1720, 150, GOOD, 'Everything else is public', [('Unique, and reachable from the internet.', TXT)], 46, 34), 100, 600, C['p5']))
    E.append(takeaway('Private stays inside. Public is on the internet.', 800, C['p6'], GOOD, 1700)); return E
s_privdemo = _lab('Private or public?', 'Ask the computer.', 'v1', RB, [('v1', 'ipwhat 192.168.1.25', 'Check an address', ACC), ('v2', 'private', 'Stays inside', VIO), ('v3', 'ipwhat 172.20.5.9', 'Another one', WARN), ('v4', 'private', '172.16 to 172.31', PINK), ('v5', 'ipwhat 8.8.8.8', 'A famous address', ACC), ('v6', 'public', 'On the internet', GOOD)])
def s_cidr(C, D, dur):
    E = head('CIDR: the slash', 'How many bits name the network?', C['c1'])
    grp = [('11000000', 192), ('10101000', 168), ('00000001', 1), ('00011001', 25)]; x = 100; xs = []
    for i, (bits, dec) in enumerate(grp):
        im = mono(bits, ACC if i < 3 else WARN, 62); E.append(Pop(im, x, 330, C['c2'] + i * 0.4)); E.append(El(T(str(dec), 'b', 36, MUTED), x + 6, 408, C['c2'] + 0.4 + i * 0.4, anim='fade')); xs.append((x, im.width)); x += im.width + 70
    E.append(Pop(chip('network: 24 bits  ·  /24', ACC, 32, 24, 12), 100, 490, C['c3'])); E.append(Pop(chip('host: 8 bits', WARN, 32, 24, 12), xs[3][0] - 20, 490, C['c4']))
    E.append(Pop(chip('256 addresses', WARN, 30, 22, 10), xs[3][0] - 20, 560, C['c4'] + 1.5))
    E.append(Pop(chip('first = network', VIO, 30, 22, 10), 100, 560, C['c5'])); E.append(Pop(chip('last = broadcast', PINK, 30, 22, 10), 100 + 400, 560, C['c5'] + 1.0))
    x = 100
    for i, (s_, col) in enumerate([('/24  →  256', ACC), ('/26  →  64', VIO), ('/16  →  65,536', GOOD)]):
        ch = chip(s_, col, 34, 24, 12); E.append(Pop(ch, x, 660, C['c6'] + i * 1.8)); x += ch.width + 30
    E.append(Pop(chip('mask 255.255.255.0  =  /24', WARN, 34, 24, 12), 100, 760, C['c8']))
    E.append(takeaway('Bigger slash number, smaller network.', 880, C['c7'], GOOD, 1700)); return E
s_cidrdemo = _lab('Subnet maths, live', 'Let the computer count.', 'u1', RB, [('u1', 'subnet 192.168.1.0/24', 'Lay out the subnet', ACC), ('u2', 'mask 255.255.255.0', 'Network and mask', VIO), ('u3', '254 hosts', 'dot 1 to dot 254', GOOD), ('u4', 'subnet 192.168.1.0/26', 'A smaller slice', WARN), ('u5', '62 hosts', 'Mask ends in 192', PINK), ('u6', 'subnet 10.0.0.0/16', 'A big network', BAD)])
def s_gateway(C, D, dur):
    E = head('The gateway', 'Is the destination on my subnet?', C['g1'])
    E.append(Pop(card(460, 200, ACC, 'This PC', [('192.168.1.25/24', TXT)], 44, 34), 100, 330, C['g2']))
    E.append(Pop(card(460, 200, VIO, 'A neighbour', [('192.168.1.200', TXT)], 44, 34), 100, 620, C['g3']))
    E.append(El(T('direct', 'b', 36, GOOD), 130, 560, C['g3'] + 0.6, anim='fade'))
    E.append(El(T('→', 'x', 64, MUTED), 600, 380, C['g4'], anim='fade'))
    E.append(Pop(card(460, 200, WARN, 'Gateway', [('192.168.1.1', TXT)], 44, 34), 730, 330, C['g4']))
    E.append(El(T('→', 'x', 64, MUTED), 1230, 380, C['g4'] + 0.8, anim='fade'))
    E.append(Pop(card(460, 200, GOOD, 'Internet', [('8.8.8.8', TXT)], 44, 34), 1360, 330, C['g4'] + 0.8))
    E.append(El(T('on your own subnet', 'b', 30, WARN, maxw=460), 730, 560, C['g5'], anim='fade'))
    E.append(takeaway('Same subnet: direct. Otherwise: the gateway.', 860, C['g6'], GOOD, 1700)); return E
s_gwdemo = _lab('Direct or gateway?', 'The question your computer asks.', 'w1', RB, [('w1', 'inside … .200', 'Same subnet?', ACC), ('w2', 'inside', 'Send directly', GOOD), ('w3', 'inside … 8.8.8.8', 'An internet address', WARN), ('w4', 'outside', 'Send to the gateway', PINK), ('w5', 'grep nameserver', 'Which DNS servers?', VIO), ('w6', '8.8.8.8  8.8.4.4', 'Addresses too', ACC)])
def s_four(C, D, dur):
    E = head('The four settings', 'Check them in this order.', C['q1'])
    it = [('1  IP address', 'Who you are', ACC, 'q2'), ('2  Subnet mask', 'Who is local: the slash', VIO, 'q3'), ('3  Gateway', 'The way out', WARN, 'q4'), ('4  DNS server', 'Names to addresses', GOOD, 'q5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, n, [(s, TXT)], 46, 34, True), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Four settings, four checks.', 860, C['q6'], GOOD, 1500)); return E
def s_errors(C, D, dur):
    E = head('Symptoms and causes', 'Match the symptom to the setting.', C['e1'])
    it = [('Address starts 169.254', 'No DHCP answer', 'e2', ACC), ('Network is unreachable', 'No route: gateway missing', 'e3', VIO), ('Local works, internet not', 'Check the gateway', 'e4', WARN), ('Address works, name fails', 'Check the DNS server', 'e5', GOOD), ('Random drops', 'Two devices, one address', 'e6', BAD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 130
        E.append(Pop(card(900, 112, col, '', [(a, TXT)], 4, 34), 100, y, C[cid])); E.append(El(T('→', 'x', 50, MUTED), 1020, y + 25, C[cid] + 0.3, anim='fade')); E.append(Pop(card(700, 112, col, '', [(b, TXT)], 4, 30), 1100, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['k1'])
    it = [('Myth: private = secure', 'Reality: just not routed online.', WARN, 'k2'), ('Myth: all networks are /24', 'Reality: /0 up to /32.', BAD, 'k3'),
          ('Myth: 256 usable hosts', 'Reality: 254. Two are reserved.', VIO, 'k4'), ('Myth: any device is a gateway', 'Reality: a router on your subnet.', GOOD, 'k5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Know the real size, then count.', 860, C['k6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['b1'])
    items = [('Network part and host part', 'b2'), ('Private or public', 'b3'), ('Read slash, name the mask', 'b4'), ('Count hosts in a subnet', 'b5'), ('Gateway or direct', 'b6'), ('The four settings', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid]))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['y1'])
    it = [('1  ip -br addr', 'Find address and slash', ACC, 'y2'), ('2  ip route', 'Find your gateway', VIO, 'y3'), ('3  Classify', 'Private or public?', WARN, 'y4'), ('4  Count', 'Hosts for your slash', GOOD, 'y5'), ('5  DNS', 'grep nameserver', PINK, 'y6')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['y7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f1'])]
    qs = [('Network part and host part: what are they?', 'f2'), ('Which three ranges are private?', 'f3'), ('What does /26 mean, and how many hosts?', 'f4'), ('When is the gateway used?', 'f8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f9'] + 0.2))
    E.append(El(T('Objective covered: MC03-O01  ·  IP, CIDR, gateway', 'b', 28, TXT, maxw=960), 220, 748, C['f9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f5']))
    E.append(El(T('Next: TCP, UDP, and ports', 'x', 46, ACC, maxw=1600), 100, 960, C['f6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f7']))
    return E
FN = dict(hook=s_hook, address=s_address, ipdemo=s_ipdemo, private=s_private, privdemo=s_privdemo, cidr=s_cidr, cidrdemo=s_cidrdemo, gateway=s_gateway, gwdemo=s_gwdemo, four=s_four,
          errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(address=('tag', ACC), ipdemo=('eye', GOOD), private=('grid', VIO), privdemo=('eye', GOOD), cidr=('grid', ACC), cidrdemo=('eye', GOOD), gateway=('swap', WARN), gwdemo=('eye', GOOD),
           four=('steps', ACC), errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
# highlights: (cue, first_row, n_rows, x0, x1, label); row 0 is the typed command line
HL = {
 'ipdemo': [('i2', 1, 1, 255, 295, ''), ('i3', 1, 1, 486, 722, ''), ('i4', 1, 1, 668, 722, '/24'), ('i6', 2, 1, 4, 220, ''), ('i7', 1, 1, 180, 356, '')],
 'privdemo': [('v2', 1, 1, 227, 333, ''), ('v4', 1, 1, 227, 333, ''), ('v6', 1, 1, 227, 318, '')],
 'cidrdemo': [('u2', 1, 2, 4, 400, ''), ('u3', 3, 2, 166, 400, ''), ('u3', 6, 1, 4, 260, ''), ('u5', 2, 1, 166, 400, ''), ('u5', 6, 1, 4, 260, ''), ('u7', 2, 1, 166, 350, ''), ('u7', 6, 1, 4, 260, '')],
 'gwdemo': [('w2', 1, 1, 4, 820, ''), ('w4', 1, 1, 4, 850, ''), ('w6', 1, 2, 165, 284, 'DNS servers')],
}
