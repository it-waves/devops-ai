import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 26  ·  DEVOPS BOOTCAMP'
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
       'startweb': 'start web', 'localhost': 'local host', 'ps': 'P S', 'du': 'D U', 'pid': 'P I D', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "A few lessons ago you learned how a computer really works. Today you prove it."),
  c('h2', "A shop server is misbehaving. Four things are wrong, and a checker says pass or fail."),
  c('h3', "Fix them, document them, and clean up. That is your mastery evidence for computer fundamentals."),
  c('h4', "You fix the first fault live with me. Then it is your turn."),
 ]),
 ('mission', [
  c('s1', "Here is the scenario. A small shop server runs on your own Linux virtual machine."),
  c('s2', "It must answer one address: local host, port eighty ninety, slash products. A good answer is a two hundred."),
  c('s3', "Four things are wrong. I will not say which. The checker will."),
  c('s4', "Each one uses a skill you already learned: processes, files, settings, and how a request is answered."),
  c('s5', "You need the virtual machine from lesson thirteen, python three, and curl. No sudo, and nothing outside one temporary folder."),
 ]),
 ('setup', [
  c('u1', "I already built the lab. One script does it, and you will run it yourself in a moment."),
  c('u2', "Ask the checker. Type: ./lab26.sh check", "Ask the checker. Type: dot slash, lab twenty six, dot S H, space, check."),
  c('u3', "Four checks, four fails. That is your starting point. Every fix must turn a fail into a pass."),
 ]),
 ('rules', [
  c('d1', "The same rule as the last mastery lesson. For every fault, you keep four notes."),
  c('d2', "One: the exact message, before the fix."),
  c('d3', "Two: the cause, and the command that proves it."),
  c('d4', "Three: the one change you made."),
  c('d5', "Four: the proof, after the fix."),
  c('d6', "Those four notes are your report. They turn luck into evidence."),
 ]),
 ('fix1', [
  c('a1', "Fault one, live. Check one failed: a runaway process. Something is using the processor. Start with evidence. Type: ps -u $USER -o pid,pcpu,comm --sort=-pcpu | head -4. P S lists processes, busiest first, for my user only.",
    "Fault one, live. Check one failed: a runaway process. Something is using the processor. Start with evidence. Type: P S, dash u, dollar user, dash o, pid, comma, p c p u, comma, comm, dash dash sort equals dash p c p u, pipe, head, dash four. P S lists processes, busiest first, for my user only."),
  c('a2', "Python three is using almost all of one processor. Everything else is nearly idle. The first number is its process I D."),
  c('a3', "Which program is it? The name alone is vague. Ask for the full command. Type: ps -o pid,etime,args -p, and that process I D.",
    "Which program is it? The name alone is vague. Ask for the full command. Type: P S, dash o, pid, comma, E time, comma, args, dash p, and that process I D."),
  c('a4', "A nightly report script, stuck in a busy loop. Nothing in this lab needs it, so we stop it."),
  c('a5', "Ask it to stop. Type: kill, and the process I D.", "Ask it to stop. Type: kill, and the process I D."),
  c('a6', "No output means it worked. Prove it. Run the list again.", "No output means it worked. Prove it. Run the list again."),
  c('a7', "The busy process is gone, and everything is idle. Save this output in your report."),
  c('a8', "Now the checker. Type: ./lab26.sh check", "Now the checker. Type: dot slash, lab twenty six, dot S H, space, check."),
  c('a9', "Check one is a pass. Three still fail. One fault: found with evidence, fixed with one change, proved with output."),
 ]),
 ('belt', [
  c('t1', "Here is your tool belt, one skill from this masterclass for each kind of fault."),
  c('t2', "P S and top show processes, and who is using the processor."),
  c('t3', "ls and D U show files, and how big a folder has grown."),
  c('t4', "env shows settings. export sets one for the programs you start next."),
  c('t5', "file tells you what kind of text a file holds, even when you cannot see the problem."),
  c('t6', "curl dash i shows the whole answer: the status line first, then the body."),
  c('t7', "Nothing here is new. You have met every one of these."),
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
  c('q2', "The logs. The shop. The request."),
  c('q3', "Read each message exactly. When a program stops, it usually tells you why, in its own words."),
  c('q4', "Fix one at a time, and run the checker after each fix."),
  c('q5', "Two reminders. Get the shop running before you test the request. And a request can still fail after the shop starts, so read the status line."),
  c('q6', "If you are stuck, ask: is it a process, a file, a setting, or the data?"),
 ]),
 ('cleanup', [
  c('k1', "When you are done, clean up. Leave nothing behind. Type: ./lab26.sh down", "When you are done, clean up. Leave nothing behind. Type: dot slash, lab twenty six, dot S H, space, down."),
  c('k2', "Lab removed. Now prove it. Type: ls /tmp/lab26", "Lab removed. Now prove it. Type: l s, space, slash temp, slash, lab twenty six."),
  c('k3', "No such file or directory. The folder is gone."),
  c('k4', "And nothing is still running. Type: pgrep -fc /tmp/lab26", "And nothing is still running. Type: P grep, dash f c, slash temp, slash, lab twenty six."),
  c('k5', "Zero. Put that proof at the end of your report."),
 ]),
 ('getlab', [
  c('g1', "Here is where to find the lab. Everything is in the course repository on Git Hub. The link is in the description."),
  c('g2', "The repository is it dash waves, slash devops dash A I."),
  c('g3', "Open the folder called academy, then lab. The file you need is lab twenty six dot S H."),
  c('g4', "Download it into your virtual machine, and make it runnable with: chmod plus x, lab twenty six dot S H."),
  c('g5', "Start it with dot slash, lab twenty six dot S H, up. Check it with check. Remove it with down."),
  c('g6', "No sudo, and no shortcut names. Everything lives in one temporary folder, and down removes it all."),
 ]),
 ('rubric', [
  c('b1', "Here is how your scenario is judged. Pass or fail, no opinions."),
  c('b2', "One: the checker shows four passes."),
  c('b3', "Two: your report has symptom, cause, fix and proof for every fault."),
  c('b4', "Three: you changed one thing at a time, and the report shows the order."),
  c('b5', "Four: the cleanup proof shows the folder gone and nothing running."),
  c('b6', "Miss one, and you are not done yet. Go back and fix it."),
  c('b7', "Also write down where you got stuck. That is not failure. It is the most useful part of the report."),
 ]),
 ('yourturn', [
  c('z1', "Your turn. Do this in your own Linux virtual machine."),
  c('z2', "One: download the lab file, and make it runnable."),
  c('z3', "Two: run up, then check, and save the four fail lines."),
  c('z4', "Three: fix all four faults, one at a time, with your notes."),
  c('z5', "Four: run check again, and save the four passes."),
  c('z6', "Five: run down, and save the cleanup proof."),
  c('z7', "Six: finish your report from the template."),
  c('z8', "Pause the video, and start now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "How many checks must pass?"), c('f13', "Name two commands from the tool belt, and what each shows."),
  c('f14', "What does the cleanup prove?"), c('f15', "Why do you save the output after every fix?"),
  c('f16', "Mastery evidence for computer fundamentals is complete.", "Mastery evidence for computer fundamentals is complete."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next masterclass: M C zero four, Linux administration."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'u2': 2.0, 'a9': 0.5, 'h4': 0.5, 's5': 0.5, 'u3': 0.5, 'd6': 0.5, 't7': 0.5, 'r7': 0.5, 'q6': 0.5, 'k5': 0.5, 'g6': 0.5, 'b7': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'mission': 'The scenario', 'setup': 'Start the lab', 'rules': 'Four notes per fault', 'fix1': 'Fault 1 live: the runaway process', 'belt': 'Your tool belt', 'report': 'The report',
        'remain': 'Your three faults', 'cleanup': 'Cleanup', 'getlab': 'Where to find the lab', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Computer fundamentals  ·  Lesson 26', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
    E.append(Pop(card(900, 150, BAD, 'Four things are wrong', [('A shop server is misbehaving.', TXT)], 44, 34), 100, 280, C['h2']))
    E.append(Pop(card(900, 150, GOOD, 'Pass or fail', [('Anyone can re-run the checker.', TXT)], 44, 34), 100, 460, C['h3']))
    for i, (n, col) in enumerate([('fix', PINK), ('document', ACC), ('clean up', WARN), ('prove', GOOD)]):
        E.append(Pop(chip(n, col, 34, 24, 12), 1100 + (i % 2) * 400, 280 + (i // 2) * 130, C['h4'] + i * 0.7))
    E.append(takeaway('Fix it. Prove it. Clean up.', 850, C['h4'] + 3.0, GOOD, 1600)); return E
def s_mission(C, D, dur):
    E = head('The scenario', 'A shop server on your virtual machine.', C['s1'])
    E.append(Pop(card(560, 150, ACC, 'your Linux VM', [('python3 shop server', TXT)], 38, 28, True), 100, 350, C['s1']))
    E.append(El(T('→', 'x', 60, MUTED), 700, 395, C['s2'], anim='fade'))
    E.append(Pop(chip('localhost:8090/products', ACC, 34, 24, 12), 780, 380, C['s2'])); E.append(Pop(chip('200 OK', GOOD, 34, 24, 12), 780, 480, C['s2'] + 0.6))
    for i, (n, col) in enumerate([('process', PINK), ('files', ACC), ('settings', WARN), ('request', VIO)]): E.append(Pop(chip(n, col, 30, 22, 10), 100 + (i % 2) * 330, 600 + (i // 2) * 100, C['s4'] + i * 0.5))
    E.append(Pop(card(640, 220, BAD, 'Four checks', [('1 process   2 logs', TXT), ('3 shop      4 request', TXT)], 38, 30), 1100, 580, C['s3']))
    E.append(takeaway('Four things are broken.', 880, C['s3'] + 1.0, BAD, 1500)); return E
s_setup = _lab('Start the lab', 'Four things are wrong.', 'u1', RB, [('u1', './lab26.sh up', 'Build and break it', ACC), ('u2', './lab26.sh check', 'Ask the checker', VIO), ('u3', 'FAIL  ×4', 'Your starting point', BAD)])
def s_rules(C, D, dur):
    E = head('Four notes per fault', 'This becomes your report.', C['d1'])
    it = [('1  Message', 'The exact words, before', BAD, 'd2'), ('2  Cause', 'And the proving command', VIO, 'd3'), ('3  Change', 'One change only', WARN, 'd4'), ('4  Proof', 'The output, after', GOOD, 'd5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 44, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Notes turn luck into evidence.', 860, C['d6'], GOOD, 1500)); return E
s_fix1 = _lab('Fault 1 live: a runaway process', 'Evidence first.', 'a1', RB, [('a1', 'ps … --sort=-pcpu', 'Busiest first', ACC), ('a2', 'python3 · ~96% CPU', 'Almost one full core', BAD), ('a4', 'nightly-report.py', 'A stuck busy loop', VIO), ('a5', 'kill PID', 'One change', PINK), ('a7', 'idle again', 'Proof for the report', GOOD), ('a9', './lab26.sh check', 'Check 1 passes', WARN)])
def s_belt(C, D, dur):
    E = head('Your tool belt', 'One skill for each kind of fault.', C['t1'])
    it = [('Processes', 'ps · top', PINK, 't2'), ('Files', 'ls · du -sh', ACC, 't3'), ('Settings', 'env · export', WARN, 't4'), ('Text', 'file', VIO, 't5'), ('Requests', 'curl -i', GOOD, 't6')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, a, [(b, TXT)], 44, 36, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(Pop(card(540, 215, MUTED, 'Nothing new', [('You have met all of these', TXT)], 40, 30, True), 100 + 2 * 590, 330 + 245, C['t7']))
    return E
def s_report(C, D, dur):
    E = head('The report', 'One section per fault.', C['r1'])
    E.append(Pop(card(900, 560, ACC, '', [], 4), 100, 340, C['r1']))
    for i, (n, col, cid) in enumerate([('Symptom', BAD, 'r2'), ('Cause', VIO, 'r3'), ('Fix', WARN, 'r4'), ('Proof', GOOD, 'r5')]): E.append(Pop(chip(n, col, 34, 28, 12), 140, 375 + i * 105, C[cid]))
    for i, (s, cid) in enumerate([('the exact message', 'r2'), ('one sentence', 'r3'), ('the single command', 'r4'), ('the output after', 'r5')]): E.append(El(T(s, 'm', 32, TXT, maxw=560), 440, 390 + i * 105, C[cid] + 0.2, anim='fade'))
    E.append(Pop(card(560, 240, GOOD, 'Final checker output', [('4 lines, all PASS', TXT)], 38, 32), 1100, 340, C['r6']))
    E.append(Pop(card(560, 240, WARN, 'Fill it in as you go', [('Not from memory', TXT)], 38, 32), 1100, 620, C['r7'])); return E
def s_remain(C, D, dur):
    E = head('Your three faults', 'Pick up where I stopped.', C['q1'])
    it = [('1  process', 'Fixed live', GOOD, 'q1'), ('2  logs', 'Still failing', BAD, 'q2'), ('3  shop', 'Still failing', BAD, 'q2'), ('4  request', 'Still failing', BAD, 'q2')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 150, col, a, [(b, TXT)], 40, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 180, C[cid]))
    for i, (n, col) in enumerate([('process', PINK), ('file', ACC), ('setting', WARN), ('data', VIO)]): E.append(Pop(chip(n, col, 28, 22, 10), 100 + i * 360, 730, C['q6'] + i * 0.4))
    E.append(takeaway('One fix. Then run the checker.', 880, C['q4'], GOOD, 1500)); return E
s_cleanup = _lab('Cleanup', 'Leave nothing behind.', 'k1', RB, [('k1', './lab26.sh down', 'Remove the lab', ACC), ('k2', 'ls /tmp/lab26', 'Is the folder gone?', VIO), ('k3', 'No such file', 'Gone', GOOD), ('k4', 'pgrep -fc /tmp/lab26', 'Anything running?', WARN), ('k5', '0', 'Proof for the report', GOOD)])
def s_getlab(C, D, dur):
    E = head('Where to find the lab', 'Everything is in the course repository.', C['g1'])
    rows = [('Repository', 'github.com/it-waves/devops-ai', ACC, 'g2'), ('Folder', 'academy / lab / lab26.sh', VIO, 'g3'), ('Install', 'chmod +x lab26.sh', WARN, 'g4'), ('Run', './lab26.sh up | check | down', GOOD, 'g5')]
    for i, (a, b, col, cid) in enumerate(rows):
        y = 340 + i * 150; E.append(Pop(card(1500, 130, col, '', [], 4), 100, y, C[cid])); E.append(Pop(chip(a, col, 30, 26, 10), 130, y + 36, C[cid] + 0.2)); E.append(El(T(b, 'm', 36, TXT, maxw=1000), 560, y + 40, C[cid] + 0.4, anim='fade'))
    E.append(takeaway('No sudo. One temporary folder.', 960, C['g6'], GOOD, 1600)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Four points. All four to pass.', C['b1'])
    items = [('Checker: four passes', 'b2'), ('Report: all four notes', 'b3'), ('One change at a time', 'b4'), ('Cleanup proof', 'b5')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all four', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 720, C['b6']))
    E.append(Pop(card(1200, 110, WARN, 'Write down where you got stuck', [], 36), 100, 850, C['b7'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own Linux virtual machine.', C['z1'])
    it = [('1  Download', 'Get lab26.sh, make runnable', PINK, 'z2'), ('2  Up + check', 'Save the four fails', BAD, 'z3'), ('3  Fix', 'One at a time, with notes', WARN, 'z4'), ('4  Check', 'Save the four passes', VIO, 'z5'), ('5  Down', 'Save the cleanup proof', GOOD, 'z6'), ('6  Report', 'Finish the template', ACC, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  start before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('How many checks must pass?', 'f12'), ('Name two tool belt commands', 'f13'), ('What does the cleanup prove?', 'f14'), ('Why save output after each fix?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Mastery evidence: computer fundamentals', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next masterclass: Linux administration', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, mission=s_mission, setup=s_setup, rules=s_rules, fix1=s_fix1, belt=s_belt, report=s_report, remain=s_remain, cleanup=s_cleanup, getlab=s_getlab, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(mission=('eye', GOOD), setup=('eye', GOOD), rules=('steps', VIO), fix1=('eye', GOOD), belt=('steps', ACC), report=('steps', ACC), remain=('question', BAD), cleanup=('eye', GOOD), getlab=('board', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
