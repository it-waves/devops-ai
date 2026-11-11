import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 30  ·  DEVOPS BOOTCAMP'
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
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 30', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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

RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
SCENES = [
 ('hook', [
  c('h1', "A server is never idle. Something is always running."),
  c('h2', "A process is a running program. When one misbehaves, you need to find it, read it, and stop it."),
  c('h3', "Today you list processes, send signals, and check how busy the machine is."),
 ]),
 ('ps', [
  c('p1', "Start with the simplest list. Type: ps.", "Start with the simplest list. Type: P S."),
  c('p2', "Only your own shell, and P S itself. Every process has a number, the P I D, and a name."),
  c('p3', "Now every process on the system, with the columns you choose. Type: ps -eo pid,user,comm.", "Now every process on the system, with the columns you choose. Type: P S, dash e o, pid, comma, user, comma, comm."),
  c('p4', "Three columns: the P I D, the owner, and the command. Process number one is the parent of everything else."),
  c('p5', "Add C P U and memory. Type: ps -eo pid,pcpu,pmem,comm.", "Add C P U and memory. Type: P S, dash e o, pid, comma, P C P U, comma, P mem, comma, comm."),
  c('p6', "Percent of one C P U, and percent of memory. Those two columns find a hungry process fast."),
 ]),
 ('signals', [
  c('s1', "Start a program in the background. Type: sleep 300 &. The ampersand returns your prompt at once.", "Start a program in the background. Type: sleep, three hundred, ampersand. The ampersand returns your prompt at once."),
  c('s2', "Bracket one is the job number. The next number is its P I D. Check with: jobs.", "Bracket one is the job number. The next number is its P I D. Check with: jobs."),
  c('s3', "Stop it politely. Type: kill %1. That sends the term signal, number fifteen. The program may clean up, then exit.", "Stop it politely. Type: kill, percent one. That sends the term signal, number fifteen. The program may clean up, then exit."),
  c('s4', "Check again with: jobs. Terminated.", "Check again with: jobs. Terminated."),
  c('s5', "Now a runaway program. Type: yes > /dev/null &. It burns a whole C P U doing nothing.", "Now a runaway program. Type: yes, greater than, slash dev slash null, ampersand. It burns a whole C P U doing nothing."),
  c('s6', "Find it. Sort by C P U, and show the top three. Type: ps -eo pid,pcpu,comm --sort=-pcpu | head -n 4.", "Find it. Sort by C P U, and show the top three. Type: P S, dash e o, pid, comma, P C P U, comma, comm, dash dash sort equals dash P C P U, pipe, head, dash n, four."),
  c('s7', "Yes is at the top, near one hundred percent. Stop it with: kill -9 %1. Signal nine cannot be ignored. Use it last.", "Yes is at the top, near one hundred percent. Stop it with: kill, dash nine, percent one. Signal nine cannot be ignored. Use it last."),
  c('s8', "Order of force: term first, kill only if term fails. Control C sends the int signal from your keyboard."),
 ]),
 ('resources', [
  c('r1', "How busy is the machine? Type: uptime.", "How busy is the machine? Type: up time."),
  c('r2', "The three numbers are the load average, over one, five and fifteen minutes. Compare them with the number of C P U cores."),
  c('r3', "Count the cores. Type: nproc.", "Count the cores. Type: N proc."),
  c('r4', "A load above the core count means work is waiting. Now memory. Type: free -h | column -t. Column tidies the table.", "A load above the core count means work is waiting. Now memory. Type: free, dash h, pipe, column, dash t. Column tidies the table."),
  c('r5', "Look at the available column, not free. Linux uses spare memory as cache, and gives it back when needed."),
 ]),
 ('running', [
  c('u1', "Is a program running? Start one. Type: sleep 300 &.", "Is a program running? Start one. Type: sleep, three hundred, ampersand."),
  c('u2', "Now ask by name. Type: pgrep -a sleep. It prints the P I D and the command.", "Now ask by name. Type: P grep, dash a, sleep. It prints the P I D and the command."),
  c('u3', "Stop everything with that name. Type: pkill sleep.", "Stop everything with that name. Type: P kill, sleep."),
  c('u4', "Ask again. Type: pgrep sleep. No output.", "Ask again. Type: P grep, sleep. No output."),
  c('u5', "Read the exit status. Type: echo $?.", "Read the exit status. Type: echo, dollar, question mark."),
  c('u6', "One means nothing matched. Zero means found. Scripts and monitoring tools use this exit status to test whether a service is up."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: kill dash nine is the normal way to stop a program. No. Term first, so it can clean up."),
  c('my3', "Myth two: high memory use means a problem. Not always. Linux caches. Read available."),
  c('my4', "Myth three: a process with a high load is the only suspect. Check the load against the core count."),
  c('my5', "Myth four: kill only kills. It sends signals, and most signals ask politely."),
  c('my6', "Term first. Kill last."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "List processes with P I D, user and command.", "List processes with P I D, user and command."),
  c('b3', "Start a job in the background, and find it."), c('b4', "Stop it with term, and say when kill dash nine is needed.", "Stop it with term, and say when kill dash nine is needed."),
  c('b5', "Find the process using the most C P U."), c('b6', "Read the load average against the core count."),
  c('b7', "Check if a program runs with P grep, and read its exit status.", "Check if a program runs with P grep, and read its exit status."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. These commands are safe, but only stop programs you started."),
  c('z2', "One: list processes with P I D, user and command, and find process number one."),
  c('z3', "Two: start a sleep in the background, and find it with jobs and with P grep."),
  c('z4', "Three: stop it with a normal kill, and confirm it is gone."),
  c('z5', "Four: start yes, sent to dev null, find it at the top by C P U, then stop it."),
  c('z6', "Five: read uptime and nproc, and say in one sentence if your machine is busy."),
  c('z7', "Six: check free dash h, and explain the difference between free and available.", "Six: check free, dash h, and explain the difference between free and available."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which character starts a command in the background?"), c('f13', "Which signal does a plain kill send?"),
  c('f14', "Which memory column should you read?"), c('f15', "What exit status means a process was found?"),
  c('f16', "Objective covered: MC04-O05.", "Objective covered: M C zero four, objective five, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: system D services, logs and scheduled jobs.", "Next lesson: system D services, logs and scheduled jobs."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'p2': 0.4, 'p4': 0.4, 'p6': 0.5, 's4': 0.5, 's7': 0.5, 's8': 0.5, 'r2': 0.5, 'r5': 0.5, 'u6': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'ps': 'List processes', 'signals': 'Background jobs and signals', 'resources': 'Load and memory', 'running': 'Is it running?', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def s_hook(C, D, dur):
    E = [El(T('A server is never idle.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Process', 'a running program', ACC), ('Signal', 'a message to it', VIO), ('Load', 'how busy it is', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('List. Signal. Measure.', 850, C['h3'], GOOD, 1600)); return E
s_ps = _lab('List processes', 'Every running program has a PID.', 'p1', RB, [('p1', 'ps', 'Your own shell', ACC), ('p3', 'ps -eo', 'Choose the columns', VIO), ('p5', 'pcpu  pmem', 'CPU and memory', WARN)])
s_signals = _lab('Background jobs and signals', 'Start, find and stop a process.', 's1', RB, [('s1', 'cmd &', 'Run in background', ACC), ('s2', 'jobs', 'List your jobs', VIO), ('s3', 'kill %1', 'TERM: ask politely', GOOD), ('s5', 'yes > /dev/null &', 'A runaway process', BAD), ('s6', '--sort=-pcpu', 'Find the hog', WARN), ('s7', 'kill -9', 'KILL: last resort', PINK)])
s_resources = _lab('Load and memory', 'Is the machine busy?', 'r1', RB, [('r1', 'uptime', 'Load average', ACC), ('r3', 'nproc', 'Count the cores', VIO), ('r4', 'free -h', 'Read: available', WARN)])
s_running = _lab('Is it running?', 'pgrep and the exit status.', 'u1', RB, [('u2', 'pgrep -a', 'Find by name', ACC), ('u3', 'pkill', 'Stop by name', VIO), ('u5', 'echo $?', 'Exit status', WARN), ('u6', '0 found  1 none', 'What it means', GOOD)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: kill -9 is normal', 'Try TERM first.', 'my2'), ('Myth: high memory is bad', 'Read available.', 'my3'), ('Myth: only load matters', 'Compare with cores.', 'my4'), ('Myth: kill only kills', 'It sends signals.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('TERM first. KILL last.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('List PID, user, command', 'b2'), ('Run a job in background', 'b3'), ('TERM first, KILL last', 'b4'), ('Find the CPU hog', 'b5'), ('Load vs CPU cores', 'b6'), ('pgrep and exit status', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine. Practice folder only.', C['z1'])
    it = [('1  List', 'ps -eo, find PID 1', PINK, 'z2'), ('2  Start', 'sleep 300 &, jobs', ACC, 'z3'), ('3  Stop', 'kill, confirm', WARN, 'z4'), ('4  Hog', 'yes, find, stop', VIO, 'z5'), ('5  Load', 'uptime, nproc', GOOD, 'z6'), ('6  Memory', 'free -h, available', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which character runs a command in the background?', 'f12'), ('Which signal does a plain kill send?', 'f13'), ('Which memory column should you read?', 'f14'), ('Which exit status means found?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O05', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: systemd, logs and cron', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ps=s_ps, signals=s_signals, resources=s_resources, running=s_running, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ps=('eye', GOOD), signals=('eye', GOOD), resources=('eye', GOOD), running=('eye', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'signals': [('s7', 2, 1, 4, 200, '')],
}
