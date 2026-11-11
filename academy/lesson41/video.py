import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 41  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'MC05-O05': 'M C zero five, objective five', 'grep': 'grep', 'awk': 'awk', 'uniq': 'unique', 'bash': 'bash', 'shebang': 'shebang', 'stdout': 'standard out', 'ufw': 'U F W', 'sshd': 'S S H D', 'ed25519': 'E D two five five one nine', 'eth0': 'eth zero', 'MC04-O10': 'M C zero four, objective ten', 'MC04-O09': 'M C zero four, objective nine', 'chmod': 'C H mod', 'sed': 'sed', 'nc': 'N C', 'diff': 'diff', 'tmp': 'temp', 'http': 'H T T P', 'systemd-analyze': 'system D analyze', 'tcp': 'T C P', 'du': 'D U', 'df': 'D F', 'loopback': 'loop back', 'ping': 'ping', 'ss': 'S S', 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Bash scripting  ·  Lesson 41', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "A command has three channels: one for input, one for normal output and one for errors. Once you control them, you can save output, hide noise and join commands together."),
  c('h2', "Today you learn four things. The three standard streams. Redirection, to send them to files. Pipes, to join commands. And safe temporary files."),
  c('h3', "Every demo is a real recording on Ubuntu."),
 ]),
 ('streams', [
  k('f1', "First, the three streams. Every command has standard in, numbered zero. Standard out, numbered one, for normal output. And standard error, numbered two, for errors. Watch both. List one file that exists, and one that does not. Type: L S, slash E T C slash hostname, space, slash nope."),
  k('f2', "Two lines on the screen. The error, and the file name. They look the same, but they travel on different streams. Now send standard out to a file with a greater than sign. Type: L S, slash E T C slash hostname, space, slash nope, greater than, out dot text."),
  k('f3', "Only the error is left on the screen. The normal output went into the file. Look inside it. Type: cat out dot text."),
  k('f4', "The file name, and no error. Now do the opposite. Two, greater than, sends the errors to a file. Type: L S, slash E T C slash hostname, space, slash nope, space, two greater than, err dot text."),
  k('f5', "Now the file name shows, and the error is gone. Check where it went. Type: cat err dot text."),
  c('f6', "The error message, saved. Stream one holds results. Stream two holds problems. Keep them apart, and each is easier to use."),
 ]),
 ('redir', [
  k('d1', "Next, more redirection. A single greater than creates the file, or replaces it. Type: echo first, greater than, log dot text."),
  k('d2', "Silent, because the output went into the file. Now two greater than signs append, and keep what is already there. Type: echo second, double greater than, log dot text."),
  k('d3', "Look at the file. Type: cat log dot text."),
  k('d4', "Both lines. A single greater than would have erased the first one, so be careful with it. A less than sign does the reverse: it feeds a file into a command as input. Count the lines. Type: W C, dash l, less than, log dot text."),
  k('d5', "Two lines. Now, a special file named slash dev slash null throws away everything written to it. Hide the error. Type: L S, slash nope, space, two greater than, slash dev slash null."),
  k('d6', "Nothing at all. But did the command succeed? Every command leaves an exit status, in the variable dollar question mark. Zero means success. Type: echo, dollar question mark."),
  c('d7', "Two, so it failed. Hiding the message did not hide the failure."),
 ]),
 ('pipes', [
  k('q1', "Now pipes. A pipe sends the standard out of one command into the standard in of the next. Here is the log again. Type: cat app dot log."),
  k('q2', "Six lines. Send them through grep, to keep only the errors. Type: cat app dot log, space, pipe, space, grep ERROR."),
  k('q3', "Two lines. Add another stage, to count them. Type: grep ERROR app dot log, space, pipe, space, W C, dash l."),
  k('q4', "Two errors. Now suppose you want to see the data and also save it. The tee command writes a copy to a file, and passes the data on. Type: grep ERROR app dot log, pipe, tee errors dot text, pipe, W C, dash l."),
  k('q5', "The count came out, and the file was written on the way. Check it. Type: cat errors dot text."),
  c('q6', "The two error lines, saved. Remember, a pipe carries standard out only. Errors still go to the screen, unless you redirect them."),
 ]),
 ('tmp', [
  k('t1', "Last, temporary files. A script often needs a scratch file. Never invent a fixed name, because it is predictable, and other users can plant a link there. Ask for a safe one with M K temp. Type: f equals dollar, open round bracket, M K temp, close round bracket."),
  k('t2', "Silent, because the name went into the variable f. Look at it. Type: echo, double quote, dollar f, double quote."),
  k('t3', "A new file in slash temp, with a random name that nobody can guess, created with private permissions. Write the errors into it. Type: grep ERROR app dot log, greater than, double quote, dollar f, double quote."),
  k('t4', "Count its lines. Type: W C, dash l, less than, double quote, dollar f, double quote."),
  k('t5', "Two lines. When you are finished, always clean up. Type: R M, double quote, dollar f, double quote."),
  k('t6', "Check that it is gone. Type: L S, double quote, dollar f, double quote."),
  c('t7', "No such file. Make, use, remove. In the next lessons, a trap will do that cleanup even when a script fails."),
 ]),
 ('build', [
  k('w1', "Now a small job that uses everything. Count the log levels, save the report, and keep the problems apart. Here is the log. Type: cat app dot log."),
  k('w2', "Count the levels, and send the report to a file. Type: awk, single quote, open brace, print dollar three, close brace, single quote, app dot log, pipe, sort, pipe, unique dash c, greater than, out dot text."),
  k('w3', "No output, because it went to the file. Look at the report. Type: cat out dot text."),
  k('w4', "Two errors, three info lines and one warning. Now run grep on a good file and a missing one, and keep the errors in their own file. Type: grep, dash c, ERROR, app dot log, missing dot log, two greater than, problems dot text."),
  k('w5', "The count for the good file. The complaint about the missing file went elsewhere. Look. Type: cat problems dot text."),
  c('w6', "Results on the screen, problems in a file. That is a script you can trust."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: greater than adds to a file. No. It replaces the file. To add, use two greater than signs."),
  c('my3', "Myth two: a pipe carries errors too. No. It carries standard out only. Errors need two greater than."),
  c('my4', "Myth three: slash dev slash null stores output. No. It throws everything away."),
  c('my5', "Myth four: a fixed name in slash temp is fine. No. It is predictable. Use M K temp."),
  c('my6', "Streams. Redirects. Pipes. Safe temp files."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Name the three standard streams, and their numbers: zero, one and two."),
  c('b3', "Redirect output with greater than and double greater than, and input with less than."),
  c('b4', "Send errors to a file with two greater than, or discard them with slash dev slash null."),
  c('b5', "Join commands with a pipe, and save a copy with tee."),
  c('b6', "Create a temporary file with M K temp, and remove it when done."),
  c('b7', "Read the exit status, with dollar question mark."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Type every command yourself."),
  c('z2', "One: list one file that exists and one that does not, and see both streams on the screen."),
  c('z3', "Two: write a line to a file with greater than, add one with double greater than, and count with less than."),
  c('z4', "Three: send errors to a file with two greater than, then discard them with slash dev slash null, and print the exit status."),
  c('z5', "Four: build a pipeline with tee, and check the saved copy."),
  c('z6', "Five: make a temporary file with M K temp, write to it, read it back and remove it."),
  c('z7', "Six: save a report to one file, and the errors to another."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which number is standard error?"), c('f13', "What is the difference between greater than, and double greater than?"),
  c('f14', "Does a pipe carry errors?"), c('f15', "Which command makes a safe temporary file?"),
  c('f16', "Objective covered: MC05-O05.", "Objective covered: M C zero five, objective five, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: error handling, traps, logging and exit codes."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'f6': 0.5, 'd7': 0.5, 'q6': 0.5, 't7': 0.5, 'w6': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'streams': 'The three streams', 'redir': 'Redirection', 'pipes': 'Pipes and tee', 'tmp': 'Safe temporary files', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Streams, redirects, pipes', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Three streams', 'in, out and error', ACC), ('Redirection', '> >> < 2>', VIO), ('Pipes', 'join commands', WARN), ('Temp files', 'safe and clean', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Control where data goes.', 880, C['h3'], GOOD, 1700)); return E
s_streams = _lab('The three streams', 'Standard in, out and error.', 'f1', RB, [('f1', 'ls /etc/hostname /nope', 'Two streams, one screen', ACC), ('f2', '> out.txt', 'Out to a file', GOOD), ('f3', 'cat out.txt', 'The saved output', VIO), ('f4', '2> err.txt', 'Errors to a file', WARN), ('f5', 'cat err.txt', 'The saved error', PINK)])
s_redir = _lab('Redirection', 'Send data to and from files.', 'd1', RB, [('d1', 'echo first > log.txt', '> replaces', ACC), ('d2', 'echo second >> log.txt', '>> appends', GOOD), ('d3', 'cat log.txt', 'Both lines', VIO), ('d4', 'wc -l < log.txt', '< feeds input', WARN), ('d5', '2> /dev/null', 'Throw errors away', PINK), ('d6', 'echo $?', 'Exit status', BAD)])
s_pipes = _lab('Pipes and tee', 'One command feeds the next.', 'q1', RB, [('q1', 'cat app.log', 'The log', ACC), ('q2', '| grep ERROR', 'Filter', GOOD), ('q3', '| wc -l', 'Count', VIO), ('q4', '| tee errors.txt |', 'Save a copy', WARN), ('q5', 'cat errors.txt', 'The copy', PINK)])
s_tmp = _lab('Safe temporary files', 'Random name, private, removed.', 't1', RB, [('t1', 'f=$(mktemp)', 'Ask for a safe name', ACC), ('t2', 'echo "$f"', 'Random name', GOOD), ('t3', 'grep ERROR app.log > "$f"', 'Use it', VIO), ('t4', 'wc -l < "$f"', 'Read it', WARN), ('t5', 'rm "$f"', 'Clean up', PINK), ('t6', 'ls "$f"', 'Gone', BAD)])
s_build = _lab('Put it together', 'Report to a file, errors apart.', 'w1', RB, [('w1', 'cat app.log', 'The log', ACC), ('w2', '... | uniq -c > out.txt', 'Save the report', GOOD), ('w3', 'cat out.txt', 'The report', VIO), ('w4', '2> problems.txt', 'Errors apart', WARN), ('w5', 'cat problems.txt', 'The problems', PINK)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: > adds to a file', 'It replaces. Use >> to add.', 'my2'), ('Myth: pipes carry errors', 'Standard out only. Use 2>.', 'my3'), ('Myth: /dev/null stores it', 'It discards everything.', 'my4'), ('Myth: fixed /tmp names', 'Predictable. Use mktemp.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Streams. Redirects. Pipes. Safe temp files.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Streams 0, 1, 2', 'b2'), ('> >> and <', 'b3'), ('2> and /dev/null', 'b4'), ('Pipe and tee', 'b5'), ('mktemp and rm', 'b6'), ('Exit status $?', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  Streams', 'both on screen', PINK, 'z2'), ('2  > >> <', 'write, append, count', ACC, 'z3'), ('3  2>', 'file, null, status', WARN, 'z4'), ('4  Pipe + tee', 'save a copy', VIO, 'z5'), ('5  mktemp', 'use, read, remove', BAD, 'z6'), ('6  Report', 'results and errors apart', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which number is standard error?', 'f12'), ('> versus >> ?', 'f13'), ('Does a pipe carry errors?', 'f14'), ('Which command makes a safe temp file?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O05', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: errors, traps and exit codes', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'streams': s_streams, 'redir': s_redir, 'pipes': s_pipes, 'tmp': s_tmp, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'streams': ('question', ACC), 'redir': ('board', VIO), 'pipes': ('gear', WARN), 'tmp': ('gear', GOOD), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'streams': [('f2', 1, 1, 4, 790, ''), ('f2', 2, 1, 4, 205, ''), ('f3', 1, 1, 4, 790, ''), ('f4', 1, 1, 4, 205, ''), ('f5', 1, 1, 4, 205, ''), ('f6', 1, 1, 4, 790, '')],
 'redir': [('d4', 1, 2, 4, 95, ''), ('d5', 1, 1, 4, 22, ''), ('d7', 1, 1, 4, 22, '')],
 'pipes': [('q3', 1, 2, 4, 640, ''), ('q4', 1, 1, 4, 22, ''), ('q5', 1, 1, 4, 22, ''), ('q6', 1, 2, 4, 640, '')],
 'tmp': [('t3', 1, 1, 4, 325, ''), ('t5', 1, 1, 4, 22, ''), ('t7', 1, 1, 4, 1000, '')],
 'build': [('w4', 1, 3, 4, 200, ''), ('w5', 1, 1, 4, 145, ''), ('w6', 1, 1, 4, 840, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson41/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
