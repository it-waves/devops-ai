import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 25  ·  DEVOPS BOOTCAMP'
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
       'startweb': 'start web', 'localhost': 'local host', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "Every masterclass ends the same way. With proof."),
  c('h2', "Not a quiz. A broken network, and four checks that say pass or fail."),
  c('h3', "When the checks pass, anyone can see that you fixed it. That is mastery evidence."),
  c('h4', "Today you build the scenario, fix the first fault live with me, and learn how to document it."),
 ]),
 ('mission', [
  c('s1', "Here is the scenario. A small shop service, called cart, runs on a server."),
  c('s2', "A client has to reach it, through one router."),
  c('s3', "Two addresses must work. Plain H T T P on port eighty eighty, and secure H T T P S on port eighty four forty three."),
  c('s4', "Four things are broken. I will not say which. The checker will."),
  c('s5', "You need a Linux machine, the lab scripts from the course repository, and an hour without rushing."),
 ]),
 ('setup', [
  c('u1', "I already built the lab. It makes a client, a router and a server, and breaks four things. It takes ten seconds, and you will run it yourself in a moment."),
  c('u2', "Now ask the checker. Type: lab check. Lab is my short name for the lab script.", "Now ask the checker. Type: lab check. Lab is my short name for the lab script."),
  c('u3', "Four checks, four fails. That is your starting point. Every fix must turn a fail into a pass."),
 ]),
 ('rules', [
  c('d1', "Before you touch anything, a rule. For every fault, you keep four notes."),
  c('d2', "One: the exact message, before the fix."),
  c('d3', "Two: the cause, and the command that proves it."),
  c('d4', "Three: the one change you made."),
  c('d5', "Four: the proof, after the fix."),
  c('d6', "Those four notes are your report. They take a minute each, and they turn luck into evidence."),
 ]),
 ('fix1', [
  c('a1', "Fault one, live. Check two failed: ping. Start with evidence. Type: cl ping -c 1 -W 1 10.0.2.2. C L runs a command inside the client.",
    "Fault one, live. Check two failed: ping. Start with evidence. Type: C L, ping, dash c, one, dash big W, one, ten dot zero dot two dot two. C L runs a command inside the client."),
  c('a2', "No reply, and no error message. Silence. The client has a route, so something on the way is not passing packets on."),
  c('a3', "Where does the path stop? Type: cl traceroute -n -w 1 -q 1 -m 3 10.0.2.2",
    "Where does the path stop? Type: C L, trace route, dash n, dash w one, dash q one, dash m three, ten dot zero dot two dot two."),
  c('a4', "Stars from the very first hop. The gateway is not forwarding traffic."),
  c('a5', "Ask the router. Type: rt sysctl net.ipv4.ip_forward", "Ask the router. Type: R T, sys control, net dot I P v four dot I P underscore forward."),
  c('a6', "Zero. Forwarding is switched off. That is the cause."),
  c('a7', "One change only. Type: rt sysctl -w net.ipv4.ip_forward=1", "One change only. Type: R T, sys control, dash w, net dot I P v four dot I P underscore forward, equals one."),
  c('a8', "Now the proof. Type: cl ping -c 1 -W 1 10.0.2.2", "Now the proof. Type: C L, ping, dash c, one, dash big W, one, ten dot zero dot two dot two."),
  c('a9', "A reply. The server is reachable. Save this output in your report."),
  c('a10', "Run the checker again. Type: lab check", "Run the checker again. Type: lab check."),
  c('a11', "Check two is a pass. Three still fail. Notice that the name check is still failing, and it needed the router first. Fix the lower layer first."),
 ]),
 ('report', [
  c('r1', "Now the report. There is a template in the repository, with one section per fault."),
  c('r2', "Symptom: the exact message you saw."),
  c('r3', "Cause: what was wrong, in one sentence."),
  c('r4', "Fix: the single command or edit you made."),
  c('r5', "Proof: the output after the fix."),
  c('r6', "At the end, paste the full checker output, with all four lines passing."),
  c('r7', "Fill it in as you go, not at the end from memory."),
 ]),
 ('remain', [
  c('q1', "Your turn begins where I stopped. Three checks still fail."),
  c('q2', "The name. The plain web page. The secure web page."),
  c('q3', "Each has its own clue, just like last lesson. Open the clue table, and read the exact words of every message."),
  c('q4', "Fix one at a time, and run the checker after each fix."),
  c('q5', "The lab script has three helpers: client, router and server. Each one runs a command inside that machine."),
  c('q6', "If you are stuck, ask which layer fails first: the name, the route, the port, or the trust."),
 ]),
 ('cleanup', [
  c('k1', "When you are done, clean up. A good engineer leaves nothing behind. Type: lab down", "When you are done, clean up. A good engineer leaves nothing behind. Type: lab down."),
  c('k2', "Lab removed. Now prove it. Type: ip netns list | wc -l", "Lab removed. Now prove it. Type: I P, net N S, list, pipe, W C, dash l."),
  c('k3', "Zero network namespaces left."),
  c('k4', "And no servers running. Type: pgrep -fc web25.py", "And no servers running. Type: P grep, dash f c, web twenty five dot P Y."),
  c('k5', "Zero. Put that proof at the end of your report."),
 ]),
 ('rubric', [
  c('b1', "Here is how your scenario is judged. Pass or fail, no opinions."),
  c('b2', "One: the checker shows four passes."),
  c('b3', "Two: your report has symptom, cause, fix and proof for every fault."),
  c('b4', "Three: you changed one thing at a time, and the report shows the order."),
  c('b5', "Four: the cleanup proof shows no namespaces and no servers left."),
  c('b6', "Miss one, and you are not done yet. Go back and fix it."),
  c('b7', "Also write down where you got stuck. That is not failure. It is the most useful part of the report."),
 ]),
 ('yourturn', [
  c('z1', "Your turn. Do this in your own virtual machine."),
  c('z2', "One: copy the three lab files from the course repository into user local bin. The link is in the description."),
  c('z3', "Two: run the lab script with sudo, and the word up. Wait ten seconds."),
  c('z4', "Three: run check, and save the four fail lines."),
  c('z5', "Four: fix all four faults, one at a time, with your notes."),
  c('z6', "Five: run check again, and save the four passes."),
  c('z7', "Six: clean up with lab down, and save that proof too."),
  c('z8', "Pause the video, and start now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "How many checks must pass?"), c('f13', "Which four notes do you keep for each fault?"),
  c('f14', "What does the cleanup prove?"), c('f15', "Why did we fix the router before the name?"),
  c('f16', "Mastery evidence for masterclass three is complete.", "Mastery evidence for masterclass three is complete."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next masterclass: M C zero four, Linux administration."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'u2': 5.0, 'a10': 2.5, 'h4': 0.5, 's5': 0.5, 'u3': 0.5, 'd6': 0.5, 'a9': 0.5, 'a11': 0.5, 'r7': 0.5, 'q6': 0.5, 'k5': 0.5, 'b7': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'mission': 'The scenario', 'setup': 'Start the lab', 'rules': 'Four notes per fault', 'fix1': 'Fault 1 live: the route', 'report': 'The report', 'remain': 'Your three faults',
        'cleanup': 'Cleanup', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Networking  ·  Lesson 25', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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

RB = 'REAL RECORDING  ·  lab network on this computer'
def s_hook(C, D, dur):
    E = [El(T('Mastery evidence.', 'x', 64), 100, 130, C['h1'])]
    E.append(Pop(card(900, 150, BAD, 'Not a quiz', [('A broken network, four checks.', TXT)], 44, 34), 100, 280, C['h2']))
    E.append(Pop(card(900, 150, GOOD, 'Pass or fail', [('Anyone can re-run the checker.', TXT)], 44, 34), 100, 460, C['h3']))
    for i, (n, col) in enumerate([('build', PINK), ('fix', ACC), ('document', WARN), ('clean up', GOOD)]):
        E.append(Pop(chip(n, col, 34, 24, 12), 1100 + (i % 2) * 400, 280 + (i // 2) * 130, C['h4'] + i * 0.7))
    E.append(takeaway('Fix it. Prove it. Clean up.', 850, C['h4'] + 3.0, GOOD, 1600)); return E
def s_mission(C, D, dur):
    E = head('The scenario', 'A broken network with four checks.', C['s1'])
    nodes = [('client', ACC, 's2'), ('router', WARN, 's2'), ('server  ·  cart', GOOD, 's1')]
    for i, (n, col, cid) in enumerate(nodes): E.append(Pop(card(440, 150, col, n, [('', TXT)], 40, 28, True), 100 + i * 560, 350, C[cid]))
    for i in range(2): E.append(El(T('→', 'x', 60, MUTED), 560 + i * 560, 400, C['s2'] + 0.3, anim='fade'))
    E.append(Pop(chip('http://cart.lab.test:8080', ACC, 34, 24, 12), 100, 580, C['s3'])); E.append(Pop(chip('https://cart.lab.test:8443', VIO, 34, 24, 12), 100, 670, C['s3'] + 0.5))
    for i, (n, col) in enumerate([('1  name', PINK), ('2  ping', ACC), ('3  http', WARN), ('4  https', VIO)]): E.append(Pop(chip(n, col, 30, 22, 10), 1100 + (i % 2) * 380, 580 + (i // 2) * 100, C['s4'] + i * 0.4))
    E.append(takeaway('Four things are broken.', 880, C['s4'] + 1.2, BAD, 1500)); return E
s_setup = _lab('Start the lab', 'Four things are wrong.', 'u1', RB, [('u1', 'lab up', 'Build and break it', ACC), ('u2', 'lab check', 'Ask the checker', VIO), ('u3', 'FAIL  ×4', 'Your starting point', BAD)])
def s_rules(C, D, dur):
    E = head('Four notes per fault', 'This becomes your report.', C['d1'])
    it = [('1  Message', 'The exact words, before', BAD, 'd2'), ('2  Cause', 'And the proving command', VIO, 'd3'), ('3  Change', 'One change only', WARN, 'd4'), ('4  Proof', 'The output, after', GOOD, 'd5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 44, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Notes turn luck into evidence.', 860, C['d6'], GOOD, 1500)); return E
s_fix1 = _lab('Fault 1 live: the route', 'Silence, then evidence.', 'a1', RB, [('a1', 'cl ping 10.0.2.2', 'Evidence first', ACC), ('a2', 'No reply · silence', 'No error message', BAD), ('a4', 'traceroute: stars', 'Stuck at the gateway', VIO), ('a6', 'ip_forward = 0', 'Forwarding is off', WARN), ('a7', 'rt sysctl -w …=1', 'One change', PINK), ('a10', 'lab check', 'Check 2 passes', GOOD)])
def s_report(C, D, dur):
    E = head('The report', 'One section per fault.', C['r1'])
    E.append(Pop(card(900, 560, ACC, '', [], 4), 100, 340, C['r1']))
    for i, (n, col, cid) in enumerate([('Symptom', BAD, 'r2'), ('Cause', VIO, 'r3'), ('Fix', WARN, 'r4'), ('Proof', GOOD, 'r5')]): E.append(Pop(chip(n, col, 34, 28, 12), 140, 375 + i * 105, C[cid]))
    for i, (s, cid) in enumerate([('the exact message', 'r2'), ('one sentence', 'r3'), ('the single command', 'r4'), ('the output after', 'r5')]): E.append(El(T(s, 'm', 32, TXT, maxw=560), 440, 390 + i * 105, C[cid] + 0.2, anim='fade'))
    E.append(Pop(card(560, 240, GOOD, 'Final checker output', [('4 lines, all PASS', TXT)], 38, 32), 1100, 340, C['r6']))
    E.append(Pop(card(560, 240, WARN, 'Fill it in as you go', [('Not from memory', TXT)], 38, 32), 1100, 620, C['r7'])); return E
def s_remain(C, D, dur):
    E = head('Your three faults', 'Pick up where I stopped.', C['q1'])
    it = [('2  ping', 'Passes now', GOOD, 'q1'), ('1  name', 'Still failing', BAD, 'q2'), ('3  http', 'Still failing', BAD, 'q2'), ('4  https', 'Still failing', BAD, 'q2')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 150, col, a, [(b, TXT)], 40, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 180, C[cid]))
    for i, (n, col) in enumerate([('client', ACC), ('router', WARN), ('server', GOOD)]): E.append(Pop(chip(f'lab {n} CMD', col, 28, 22, 10), 100 + i * 560, 730, C['q5'] + i * 0.4))
    E.append(takeaway('One fix. Then run the checker.', 880, C['q4'], GOOD, 1500)); return E
s_cleanup = _lab('Cleanup', 'Leave nothing behind.', 'k1', RB, [('k1', 'lab down', 'Remove the lab', ACC), ('k2', 'ip netns list | wc -l', 'Count what is left', VIO), ('k3', '0', 'No namespaces', GOOD), ('k4', 'pgrep -fc web25.py', 'Any server running?', WARN), ('k5', '0', 'Proof for the report', GOOD)])
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Four points. All four to pass.', C['b1'])
    items = [('Checker: four passes', 'b2'), ('Report: all four notes', 'b3'), ('One change at a time', 'b4'), ('Cleanup proof', 'b5')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all four', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 720, C['b6']))
    E.append(Pop(card(1200, 110, WARN, 'Write down where you got stuck', [], 36), 100, 850, C['b7'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine.', C['z1'])
    it = [('1  Install', 'Copy the lab files', PINK, 'z2'), ('2  Up', 'sudo lab25.sh up', BAD, 'z3'), ('3  Check', 'Save the four fails', ACC, 'z4'), ('4  Fix', 'One at a time, with notes', WARN, 'z5'), ('5  Check', 'Save the four passes', VIO, 'z6'), ('6  Clean up', 'lab down, save proof', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  start before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('How many checks must pass?', 'f12'), ('Which four notes per fault?', 'f13'), ('What does the cleanup prove?', 'f14'), ('Why the router before the name?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Mastery evidence: networking', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next masterclass: Linux administration', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, mission=s_mission, setup=s_setup, rules=s_rules, fix1=s_fix1, report=s_report, remain=s_remain, cleanup=s_cleanup, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(mission=('eye', GOOD), setup=('eye', GOOD), rules=('steps', VIO), fix1=('eye', GOOD), report=('steps', ACC), remain=('question', BAD), cleanup=('eye', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'setup': [('u3', 1, 4, 4, 620, '')],
 'fix1': [('a2', 4, 1, 340, 765, ''), ('a4', 2, 3, 4, 100, ''), ('a6', 1, 1, 4, 352, ''), ('a9', 2, 1, 4, 832, ''), ('a11', 2, 1, 4, 475, '')],
 'cleanup': [('k3', 1, 1, 4, 30, ''), ('k5', 1, 1, 4, 30, '')],
}
