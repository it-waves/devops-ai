import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 18  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

# ---- speech helpers ----
_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = {'TCP': 'T C P', 'UDP': 'U D P', 'SSH': 'S S H', 'DNS': 'D N S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'SYN': 'sin', 'SYN-ACK': 'sin ack', 'ACK': 'ack', 'ESTAB': 'E S T A B',
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
  c('h1', "Every conversation on a network needs two things: an address, and a door number."),
  c('h2', "The address finds the computer. The door number finds the program on that computer."),
  c('h3', "Today you learn how those door numbers, called ports, work, and how TCP and UDP carry the conversation."),
  c('h4', "You will watch ports open, connections form, and a port say no, all live."),
 ]),
 ('ports', [
  c('p1', "First, ports."), c('p2', "A computer runs many programs that use the network at the same time."),
  c('p3', "The IP address finds the computer. The port number finds the right program."),
  c('p4', "A port is just a number, from zero to sixty-five thousand five hundred thirty-five."),
  c('p5', "Some are well known. Twenty-two is SSH. Fifty-three is DNS. Eighty is web traffic. Four forty-three is secure web traffic.", gap=0.3),
  c('p6', "Numbers up to one thousand twenty-three are reserved for well-known services."),
  c('p7', "When your browser connects, it picks a random high port for itself, and connects to the server's well-known port."),
 ]),
 ('servicedemo', [
  c('s1', "Your computer keeps a small list of well-known names and numbers. Type: getent services ssh http https",
    "Your computer keeps a small list of well-known names and numbers. Type: get ent, services, S S H, H T T P, H T T P S."),
  c('s2', "Each line shows a name, a port number, and the protocol. All three use TCP."),
  c('s3', "Now let us see a real program listening. We started a small web server beforehand, on port eighty eighty. Type: ss -ltn 'sport = :8080'",
    "Now let us see a real program listening. We started a small web server beforehand, on port eighty eighty. Type: s s, dash l t n, then in quotes: s port equals colon eighty eighty."),
  c('s4', "LISTEN means it is waiting for connections, on this address, at port eighty eighty."),
  c('s5', "Now let us knock on that door. Type: curl -sI localhost:8080 | head -1", "Now let us knock on that door. Type: curl, dash s capital I, local host, colon, eighty eighty, pipe, head, dash one."),
  c('s6', "Two hundred, O K. The door was open, and a program answered."),
  c('s7', "Remember: a port is only open while a program is listening on it."),
 ]),
 ('tcpudp', [
  c('t1', "Now the two ways to carry data: TCP and UDP."),
  c('t2', "TCP is like a phone call. First you connect. Then every piece arrives, in order, or it is sent again."),
  c('t3', "That makes TCP reliable. Web pages, SSH and email use it."),
  c('t4', "UDP is like sending postcards. No connection, no checking, no resending."),
  c('t5', "That makes UDP fast and light. DNS questions, video calls and games use it."),
  c('t6', "Neither is better. The job decides."),
 ]),
 ('handshake', [
  c('z1', "Before TCP sends data, it makes a connection with three short messages."),
  c('z2', "One: the client sends SYN, which means: can we talk?"), c('z3', "Two: the server answers SYN-ACK: yes, and I am ready."),
  c('z4', "Three: the client sends ACK: great, let us begin."), c('z5', "This is the three-way handshake. It takes a tiny fraction of a second."),
  c('z6', "If the first message gets no answer, the connection hangs, and then times out."),
 ]),
 ('states', [
  c('m1', "A TCP connection moves through states, and you can see them."),
  c('m2', "LISTEN: a program is waiting for new connections."),
  c('m3', "ESTABLISHED: the handshake is done, and data can flow. The tool shows it as ESTAB."),
  c('m4', "TIME-WAIT: a connection just closed, and the computer waits a short while before reusing it."),
  c('m5', "TIME-WAIT is normal. A busy server shows many of them."),
  c('m6', "SYN-SENT: a client sent its first message and is waiting. If it stays there, something is blocking the way."),
 ]),
 ('statedemo', [
  c('n1', "Let us see two states at once. A client is already connected to our web server. Type: ss -tn 'sport = :8080'",
    "Let us see two states at once. A client is already connected to our web server. Type: s s, dash t n, then in quotes: s port equals colon eighty eighty."),
  c('n2', "ESTAB. One established connection. The other end is the client, on a random high port."),
  c('n3', "Now we make one short request. Type: curl -s localhost:8080 >/dev/null", "Now we make one short request. Type: curl, dash s, local host, colon, eighty eighty, then send the output to dev null."),
  c('n4', "Now list every state on that port. Type: ss -tan 'sport = :8080'", "Now list every state on that port. Type: s s, dash t a n, then in quotes: s port equals colon eighty eighty."),
  c('n5', "LISTEN: the server, waiting. ESTAB: the client that is still holding its connection."),
  c('n6', "And TIME-WAIT: requests that just finished and closed. All three states, live."),
 ]),
 ('udpdemo', [
  c('u1', "Now UDP. A small UDP listener is waiting on port ninety-nine ninety-nine. Type: ss -lun 'sport = :9999'",
    "Now U D P. A small U D P listener is waiting on port ninety-nine ninety-nine. Type: s s, dash l u n, then in quotes: s port equals colon ninety-nine ninety-nine."),
  c('u2', "UNCONN, short for unconnected. There is no connection state, because UDP has no connection."),
  c('u3', "Now send one message with the tool n c. The dash u means UDP. Type: echo hello | nc -u -w1 127.0.0.1 9999",
    "Now send one message with the tool n c. The dash u means U D P. Type: echo hello, pipe, n c, dash u, dash w one, one twenty-seven dot zero dot zero dot one, ninety-nine ninety-nine."),
  c('u4', "Nothing came back. UDP does not confirm anything."),
  c('u5', "But the listener wrote it down. Type: cat udp.log", "But the listener wrote it down. Type: cat, U D P dot log."),
  c('u6', "Got hello. The message arrived, with no handshake at all."),
 ]),
 ('socket', [
  c('k1', "One more word: socket."), c('k2', "A socket is one end of a connection: an IP address plus a port."),
  c('k3', "A TCP connection is two sockets talking: the client's socket, and the server's socket."),
  c('k4', "The client uses a random high port. The server uses its well-known port, here eighty eighty."),
  c('k5', "That pair of sockets is how the computer keeps many connections apart, even to the same server port."),
 ]),
 ('conflictdemo', [
  c('q1', "Now, two ways a port says no. First: knock on a door nobody answers."),
  c('q2', "Nothing listens on port eighty eighty-one. Type: curl -s localhost:8081; echo \"exit code $?\"",
    "Nothing listens on port eighty eighty-one. Type: curl, dash s, local host, colon, eighty eighty-one, semicolon, echo, in quotes, exit code, dollar, question mark."),
  c('q3', "Exit code seven. For curl, that means: could not connect. The connection was refused, because nothing is listening."),
  c('q4', "Second: two programs cannot share one port. Port eighty eighty is taken, so let us try to start another server on it. Type: python3 -m http.server 8080 2>&1 | tail -1",
    "Second: two programs cannot share one port. Port eighty eighty is taken, so let us try to start another server on it. Type: python three, dash m, H T T P dot server, eighty eighty, then show only the last line."),
  c('q5', "Address already in use. One port, one program."), c('q6', "The fix: stop the old program, or choose another port."),
 ]),
 ('errors', [
  c('e1', "Match the symptom to the cause."), c('e2', "Connection refused: the computer is reachable, but nothing listens on that port."),
  c('e3', "Connection timed out: no answer at all. A firewall may be dropping it, or the host is down."), c('e4', "Address already in use: another program already holds that port."),
  c('e5', "Many TIME-WAIT lines: normal after busy traffic. Not an error."), c('e6', "Works on the server, but not from outside: the program may listen on the local address only."),
 ]),
 ('myths', [
  c('x1', "Watch out for four common myths."), c('x2', "Myth one: ports are physical sockets on the machine. They are only numbers in software."),
  c('x3', "Myth two: UDP is the bad one. It is chosen on purpose, when speed matters more than perfection."),
  c('x4', "Myth three: TIME-WAIT means something is broken. It is a normal, short wait."),
  c('x5', "Myth four: port eighty only works for web traffic. It is a convention, and a program can use any free port."), c('x6', "Check what is really listening."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Explain what a port is, and name three well-known ports."),
  c('b3', "Choose TCP or UDP for a job, and say why."), c('b4', "Describe the three-way handshake."),
  c('b5', "Read LISTEN, ESTAB and TIME-WAIT in the s s output."), c('b6', "Explain refused versus timed out."), c('b7', "Explain why a port can be already in use."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('y1', "Your turn, in the virtual machine you built."),
  c('y2', "One: start a server with python3 -m http.server 8080, and leave it running.", "One: start a server with python three, dash m, H T T P dot server, eighty eighty, and leave it running."),
  c('y3', "Two: in a second terminal, run ss -ltn 'sport = :8080', and find LISTEN.", "Two: in a second terminal, run s s, dash l t n, with s port equals colon eighty eighty, and find LISTEN."),
  c('y4', "Three: fetch it with curl, list all states with ss -tan, and find the TIME-WAIT line.", "Three: fetch it with curl, list all states with s s, dash t a n, and find the time wait line."),
  c('y5', "Four: try to start a second server on the same port, and read the error."), c('y6', "Five: stop the first server with control C, and watch the port disappear."),
  c('y7', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f1', "Quick check."), c('f2', "What does a port do, and which three well-known ports can you name?"), c('f3', "How do TCP and UDP differ?"),
  c('f4', "What are the three steps of the handshake?"), c('f8', "What does connection refused tell you?"),
  c('f9', "Objective covered: MC03-O02.", "Objective covered: number two, in the computer networking masterclass."),
  c('f5', "Pause the video, and answer out loud."), c('f6', "Next: HTTPS and TLS certificates."), c('f7', "Subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h4': 0.5, 'p7': 0.5, 's7': 0.5, 't6': 0.5, 'z6': 0.5, 'm6': 0.5, 'n6': 0.5, 'u6': 0.5, 'k5': 0.5, 'q6': 0.5, 'e6': 0.5, 'x6': 0.5, 'b8': 0.5, 'y7': 14.0, 'f5': 10.0}
CHAP = {'ports': 'Ports', 'servicedemo': 'Live: ports and listening', 'tcpudp': 'TCP and UDP', 'handshake': 'The three-way handshake', 'states': 'Connection states', 'statedemo': 'Live: connection states',
        'udpdemo': 'Live: UDP', 'socket': 'Sockets', 'conflictdemo': 'Live: when a port says no', 'errors': 'Symptoms and causes', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Networking  ·  Lesson 18', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
    E = [El(T('Every conversation needs a door number', 'x', 64), 100, 130, C['h1'])]
    E.append(Pop(door_art(), 1080, 250, C['h1'])); E.append(El(T('ILLUSTRATION  ·  not a photo', 'm', 24, MUTED, maxw=740), 1080, 770, C['h1'] + 0.5, anim='fade'))
    E.append(Pop(card(900, 150, ACC, 'The address', [('Finds the computer.', TXT)], 46, 36), 100, 250, C['h2']))
    E.append(Pop(card(900, 150, WARN, 'The port', [('Finds the program.', TXT)], 46, 36), 100, 430, C['h2'] + 2.5))
    bs = [badge(n, F('b', 34), INK, col, padx=26, pady=14, r=26) for n, col in [('Ports', ACC), ('TCP', VIO), ('UDP', GOOD), ('States', WARN), ('Sockets', PINK)]]
    E.append(El(T('Today, live', 'b', 32, MUTED), 100, 640, C['h3'], anim='fade')); bx = 100
    for i, b in enumerate(bs): E.append(Pop(b, bx, 700, C['h3'] + 0.3 + i * 0.5)); bx += b.width + 24
    E.append(takeaway('Learn to read what is listening, and why.', 840, C['h4'], GOOD, 1600)); return E
def s_ports(C, D, dur):
    E = head('Ports', 'Which program should get this?', C['p1'])
    it = [('22', 'SSH', ACC), ('53', 'DNS', VIO), ('80', 'HTTP', GOOD), ('443', 'HTTPS', WARN)]
    for i, (n, s, col) in enumerate(it): E.append(Pop(card(410, 230, col, n, [(s, TXT)], 80, 40, True), 100 + i * 437, 330, C['p5'] + i * 1.4))
    E.append(Pop(chip('range: 0 to 65535', ACC, 34, 24, 12), 100, 620, C['p4']))
    E.append(Pop(chip('well known: up to 1023', GOOD, 34, 24, 12), 600, 620, C['p6']))
    E.append(Pop(chip('your browser: a random high port', WARN, 34, 24, 12), 100, 710, C['p7']))
    E.append(takeaway('The IP finds the computer. The port finds the program.', 850, C['p3'] + 1.0, GOOD, 1700)); return E
s_servicedemo = _lab('Ports, live', 'Names, numbers, and listeners.', 's1', RB, [('s1', 'getent services', 'Well-known ports', ACC), ('s2', '22/tcp  80/tcp  443/tcp', 'Name, number, protocol', VIO), ('s3', "ss -ltn 'sport = :8080'", 'Who listens on 8080?', WARN), ('s4', 'LISTEN', 'Waiting for connections', GOOD), ('s5', 'curl localhost:8080', 'Knock on the door', PINK), ('s6', '200 OK', 'A program answered', GOOD)])
def s_tcpudp(C, D, dur):
    E = head('TCP and UDP', 'Two ways to carry data.', C['t1'])
    E.append(Pop(card(840, 400, ACC, 'TCP  ·  the phone call', [('Connects first', TXT), ('Every piece arrives, in order', TXT), ('Lost pieces are sent again', TXT)], 46, 34), 100, 330, C['t2']))
    E.append(Pop(card(840, 400, VIO, 'UDP  ·  the postcard', [('No connection', TXT), ('No checking, no resending', TXT), ('Fast and light', TXT)], 46, 34), 980, 330, C['t4']))
    x = 100
    for i, s in enumerate(['web', 'SSH', 'email']): ch = chip(s, ACC, 30, 22, 10); E.append(Pop(ch, x, 760, C['t3'] + i * 0.4)); x += ch.width + 20
    x = 980
    for i, s in enumerate(['DNS', 'video calls', 'games']): ch = chip(s, VIO, 30, 22, 10); E.append(Pop(ch, x, 760, C['t5'] + i * 0.4)); x += ch.width + 20
    E.append(takeaway('Neither is better. The job decides.', 880, C['t6'], GOOD, 1500)); return E
def s_handshake(C, D, dur):
    E = head('The three-way handshake', 'How TCP starts a connection.', C['z1'])
    E.append(Pop(card(420, 130, ACC, 'Client', [], 50), 100, 330, C['z1'])); E.append(Pop(card(420, 130, WARN, 'Server', [], 50), 1400, 330, C['z1']))
    steps = [('SYN', 'can we talk?', ACC, 'z2', True), ('SYN-ACK', 'yes, I am ready', VIO, 'z3', False), ('ACK', 'great, begin', GOOD, 'z4', True)]
    for i, (n, s, col, cid, fwd) in enumerate(steps):
        y = 520 + i * 120
        E.append(Pop(chip(n + '   ' + s, col, 34, 28, 14), 560, y, C[cid])); E.append(El(T('→' if fwd else '←', 'x', 64, col), 1330 if fwd else 450, y - 4, C[cid] + 0.3, anim='fade'))
    E.append(takeaway('Three short messages, then data flows.', 900, C['z5'], GOOD, 1700)); return E
def s_states(C, D, dur):
    E = head('Connection states', 'What the tool shows you.', C['m1'])
    it = [('LISTEN', 'A program is waiting', GOOD, 'm2'), ('ESTAB', 'Connected, data flows', ACC, 'm3'), ('TIME-WAIT', 'Just closed, a short wait', VIO, 'm4'), ('SYN-SENT', 'Knocked, no answer yet', WARN, 'm6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, n, [(s, TXT)], 50, 34, True), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('TIME-WAIT is normal. Stuck in SYN-SENT is not.', 860, C['m5'], GOOD, 1700)); return E
s_statedemo = _lab('States, live', 'LISTEN, ESTAB, TIME-WAIT.', 'n1', RB, [('n1', "ss -tn 'sport = :8080'", 'One connection', ACC), ('n2', 'ESTAB', 'Connected, data can flow', GOOD), ('n3', 'curl … >/dev/null', 'A short request', VIO), ('n4', "ss -tan 'sport = :8080'", 'Every state', WARN), ('n5', 'LISTEN + ESTAB', 'Waiting, and talking', PINK), ('n6', 'TIME-WAIT', 'Just closed', BAD)])
s_udpdemo = _lab('UDP, live', 'No connection at all.', 'u1', RB, [('u1', "ss -lun 'sport = :9999'", 'A UDP listener', ACC), ('u2', 'UNCONN', 'No connection state', VIO), ('u3', 'nc -u 127.0.0.1 9999', 'Send one message', WARN), ('u4', '(nothing back)', 'No confirmation', PINK), ('u5', 'cat udp.log', 'Did it arrive?', ACC), ('u6', 'got: hello', 'It did, no handshake', GOOD)])
def s_socket(C, D, dur):
    E = head('Sockets', 'One end of a connection.', C['k1'])
    E.append(Pop(card(780, 260, ACC, 'Client socket', [('127.0.0.1 : 43414', ACC), ('random high port', MUTED)], 46, 40), 100, 340, C['k3']))
    E.append(Pop(card(780, 260, WARN, 'Server socket', [('127.0.0.1 : 8080', WARN), ('well-known port', MUTED)], 46, 40), 1040, 340, C['k4']))
    E.append(El(T('→', 'x', 80, MUTED), 905, 410, C['k4'] + 0.5, anim='fade'))
    E.append(Pop(chip('socket  =  IP address  +  port', GOOD, 36, 28, 14), 100, 700, C['k2']))
    E.append(takeaway('Two sockets make one connection.', 860, C['k5'], GOOD, 1500)); return E
s_conflictdemo = _lab('When a port says no', 'Refused, and already in use.', 'q1', RB, [('q2', 'curl localhost:8081', 'Nobody listens there', ACC), ('q3', 'exit code 7', 'Could not connect', BAD), ('q4', 'http.server 8080', 'Start a second server', WARN), ('q5', 'Address in use', 'One port, one program', PINK), ('q6', 'the fix', 'Stop it, or change port', GOOD)])
def s_errors(C, D, dur):
    E = head('Symptoms and causes', 'Match the symptom to the cause.', C['e1'])
    it = [('Connection refused', 'Nothing listens on that port', 'e2', ACC), ('Connection timed out', 'No answer: firewall or host down', 'e3', VIO), ('Address already in use', 'Another program holds the port', 'e4', WARN), ('Many TIME-WAIT lines', 'Normal after busy traffic', 'e5', GOOD), ('Works locally, not outside', 'Listening on 127.0.0.1 only', 'e6', BAD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 130
        E.append(Pop(card(900, 112, col, '', [(a, TXT)], 4, 34), 100, y, C[cid])); E.append(El(T('→', 'x', 50, MUTED), 1020, y + 25, C[cid] + 0.3, anim='fade')); E.append(Pop(card(700, 112, col, '', [(b, TXT)], 4, 28), 1100, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['x1'])
    it = [('Myth: ports are physical', 'Reality: only numbers in software.', WARN, 'x2'), ('Myth: UDP is the bad one', 'Reality: chosen when speed matters.', BAD, 'x3'),
          ('Myth: TIME-WAIT is broken', 'Reality: a normal, short wait.', VIO, 'x4'), ('Myth: port 80 is for web only', 'Reality: just a convention.', GOOD, 'x5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Check what is really listening.', 860, C['x6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['b1'])
    items = [('What a port is, three examples', 'b2'), ('Choose TCP or UDP, and why', 'b3'), ('Describe the handshake', 'b4'), ('Read LISTEN, ESTAB, TIME-WAIT', 'b5'), ('Refused versus timed out', 'b6'), ('Why a port is already in use', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['y1'])
    it = [('1  Start', 'http.server 8080', ACC, 'y2'), ('2  Listen', "ss -ltn 'sport = :8080'", VIO, 'y3'), ('3  States', 'curl, then ss -tan', WARN, 'y4'), ('4  Conflict', 'A second server, same port', GOOD, 'y5'), ('5  Stop', 'Control C, check ss', PINK, 'y6')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['y7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f1'])]
    qs = [('What does a port do? Name three.', 'f2'), ('How do TCP and UDP differ?', 'f3'), ('Three steps of the handshake?', 'f4'), ('What does connection refused tell you?', 'f8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f9'] + 0.2))
    E.append(El(T('Objective covered: MC03-O02  ·  TCP, UDP, ports, states', 'b', 28, TXT, maxw=960), 220, 748, C['f9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f5']))
    E.append(El(T('Next: HTTPS and TLS certificates', 'x', 46, ACC, maxw=1600), 100, 960, C['f6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f7']))
    return E
FN = dict(hook=s_hook, ports=s_ports, servicedemo=s_servicedemo, tcpudp=s_tcpudp, handshake=s_handshake, states=s_states, statedemo=s_statedemo, udpdemo=s_udpdemo, socket=s_socket, conflictdemo=s_conflictdemo,
          errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ports=('tag', ACC), servicedemo=('eye', GOOD), tcpudp=('swap', VIO), handshake=('link', WARN), states=('loop', GOOD), statedemo=('eye', GOOD), udpdemo=('eye', GOOD), socket=('link', ACC), conflictdemo=('eye', GOOD),
           errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
# highlights: (cue, first_row, n_rows, x0, x1, label); row 0 is the typed command line
HL = {
 'servicedemo': [('s2', 1, 3, 333, 430, ''), ('s4', 2, 1, 4, 95, ''), ('s6', 1, 1, 140, 230, '')],
 'statedemo': [('n2', 2, 1, 4, 80, ''), ('n5', 2, 2, 4, 95, ''), ('n6', 4, 2, 4, 140, '')],
 'udpdemo': [('u2', 2, 1, 4, 95, ''), ('u6', 1, 1, 4, 150, '')],
 'conflictdemo': [('q3', 1, 1, 4, 180, ''), ('q5', 1, 1, 150, 650, '')],
}
