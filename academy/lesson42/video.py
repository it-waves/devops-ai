import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 42  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'MC05-O06': 'M C zero five, objective six', 'trap': 'trap', 'EXIT': 'exit', 'grep': 'grep', 'awk': 'awk', 'uniq': 'unique', 'bash': 'bash', 'shebang': 'shebang', 'stdout': 'standard out', 'ufw': 'U F W', 'sshd': 'S S H D', 'ed25519': 'E D two five five one nine', 'eth0': 'eth zero', 'MC04-O10': 'M C zero four, objective ten', 'MC04-O09': 'M C zero four, objective nine', 'chmod': 'C H mod', 'sed': 'sed', 'nc': 'N C', 'diff': 'diff', 'tmp': 'temp', 'http': 'H T T P', 'systemd-analyze': 'system D analyze', 'tcp': 'T C P', 'du': 'D U', 'df': 'D F', 'loopback': 'loop back', 'ping': 'ping', 'ss': 'S S', 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Bash scripting  ·  Lesson 42', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "Scripts fail. A disk fills up, a file is missing, a server does not answer. The question is whether your script notices, stops safely, cleans up and tells you what happened."),
  c('h2', "Today you learn four things. Exit codes. Strict mode, to stop on the first failure. Traps, to clean up. And logging, to leave a clear record."),
  c('h3', "Every demo is a real recording on Ubuntu."),
 ]),
 ('exitcodes', [
  k('e1', "First, exit codes. Every command ends with a number. Zero means success, and anything else means failure. Run a command that works. Type: L S, slash E T C slash hostname."),
  k('e2', "It printed the file name. Now ask for its exit code, with dollar question mark. Type: echo, dollar question mark."),
  k('e3', "Zero, success. Now a command that fails. Type: L S, slash nope."),
  k('e4', "An error message. Ask for the exit code again. Type: echo, dollar question mark."),
  k('e5', "Two. Not zero, so the command failed. Your own scripts can return a code too, with the exit command. Here is a small check script. Type: cat check dot S H."),
  k('e6', "If the log contains the word ERROR, the script prints a message and exits with one. Otherwise it prints clean, and exits with zero. Run it. Type: bash check dot S H."),
  k('e7', "It found errors. Check the code. Type: echo, dollar question mark."),
  c('e8', "One. Other tools, like pipelines and schedulers, read this number, to decide what to do next."),
 ]),
 ('strict', [
  k('s1', "Next, strict mode. By default, bash carries on after an error, and that can be dangerous. Here is a loose script. Type: cat loose dot S H."),
  k('s2', "It tries to change into a folder that does not exist, and then carries on. Run it. Type: bash loose dot S H."),
  k('s3', "The cd failed, but the script went on. It reported a folder that is not the one it wanted, and used a variable that was never set. Now a strict version. Type: cat strict dot S H."),
  k('s4', "The set line has three options. Dash E stops at the first failing command. Dash U treats an unset variable as an error. And pipe fail makes a pipeline fail if any stage fails. Run it. Type: bash strict dot S H."),
  k('s5', "It stopped at the failed cd, and nothing after it ran. Check the exit code. Type: echo, dollar question mark."),
  k('s6', "One. Now see what dash U does. Here is a script that uses a variable that was never set. Type: cat unset dot S H."),
  k('s7', "Run it. Type: bash unset dot S H."),
  c('s8', "Unbound variable. Without dash U, the script would have printed an empty name, and gone on."),
 ]),
 ('trap', [
  k('t1', "Stopping early is good, but a script that stops can leave a mess. A trap runs a command when something happens. Here is a script with a trap on the word EXIT. Type: cat trap dot S H."),
  k('t2', "It makes a temporary file, and sets a trap that removes the file and prints a message. Then a command fails. Run it. Type: bash trap dot S H."),
  k('t3', "The script stopped at the failure, and the trap still ran. Check the exit code. Type: echo, dollar question mark."),
  k('t4', "One, still a failure. Now check that nothing was left behind in slash temp. Type: L S, slash temp."),
  c('t5', "Empty. The trap on EXIT runs however the script ends: success, failure or an interrupt. That is how you clean up safely."),
 ]),
 ('logging', [
  k('l1', "Next, logging. A good script says what it is doing, and when. Here is a small log function. Type: cat log dot S H."),
  k('l2', "The function prints the time, a level and a message, to standard error, with the redirect, greater than ampersand two. Run it. Type: bash log dot S H."),
  k('l3', "Messages with times, on the screen. Because they went to standard error, you can capture them without touching the normal output. Type: bash log dot S H, space, two greater than, run dot log."),
  k('l4', "Silent, because the log went into the file. Look inside. Type: cat run dot log."),
  c('l5', "A timestamped record. Results on standard out, and logs on standard error, so each can go to its own place."),
 ]),
 ('build', [
  k('w1', "Now put it all together, in one safe script. Strict mode, a temporary file, a trap, and an exit code. Type: cat safe dot S H."),
  k('w2', "Notice or true after grep. When grep finds no match, it exits with one, and strict mode would stop the script. Or true says: that is allowed. Run it. Type: bash safe dot S H."),
  k('w3', "Two errors. The script then exits with one, to tell the caller. Check it. Type: echo, dollar question mark."),
  c('w4', "Strict, clean, and honest about the result. That is a script you can run from a scheduler, and trust."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: exit code zero means failure. No. Zero means success. Anything else is a failure."),
  c('my3', "Myth two: set dash E catches every error. No. Commands inside an if test, or before or or, are exempt."),
  c('my4', "Myth three: a trap only runs on control C. No. A trap on EXIT runs however the script ends."),
  c('my5', "Myth four: logs belong on standard out. No. Put results on standard out, and logs on standard error."),
  c('my6', "Exit codes. Strict mode. Traps. Logs."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Read an exit code with dollar question mark, and know that zero means success."),
  c('b3', "Return your own exit code with the exit command."),
  c('b4', "Use set dash E U O pipe fail, and explain each option."),
  c('b5', "Clean up with a trap on EXIT."),
  c('b6', "Write timestamped log lines to standard error."),
  c('b7', "Allow an expected failure with or true."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Type every command yourself."),
  c('z2', "One: run a command that works and one that fails, and print each exit code."),
  c('z3', "Two: write a script that exits with one when a file contains a word, and zero when it does not."),
  c('z4', "Three: add set dash E U O pipe fail, and prove that it stops at the first failure."),
  c('z5', "Four: add a trap on EXIT that removes a temporary file, and check that none is left."),
  c('z6', "Five: add a log function that writes timestamps to standard error, and save them to a file."),
  c('z7', "Six: run grep on a file with no match, and make the script survive with or true."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which exit code means success?"), c('f13', "What does set dash U do?"),
  c('f14', "When does a trap on EXIT run?"), c('f15', "Where should log messages go?"),
  c('f16', "Objective covered: MC05-O06.", "Objective covered: M C zero five, objective six, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: secrets, permissions, input validation and injection risks."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'e8': 0.5, 's8': 0.5, 't5': 0.5, 'l5': 0.5, 'w4': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'exitcodes': 'Exit codes', 'strict': 'Strict mode', 'trap': 'Clean up with trap', 'logging': 'Logging', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Fail safely, leave a record', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Exit codes', '0 is success', ACC), ('Strict mode', 'set -euo pipefail', VIO), ('Traps', 'clean up on EXIT', WARN), ('Logging', 'timestamps on stderr', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Stop. Clean up. Tell the truth.', 880, C['h3'], GOOD, 1700)); return E
s_exitcodes = _lab('Exit codes', 'Zero is success, anything else fails.', 'e1', RB, [('e1', 'ls /etc/hostname', 'A command that works', ACC), ('e2', 'echo $?', 'Exit code: 0', GOOD), ('e3', 'ls /nope', 'A command that fails', BAD), ('e4', 'echo $?', 'Exit code: 2', WARN), ('e5', 'cat check.sh', 'exit 1 if ERROR found', VIO), ('e6', 'bash check.sh', 'Run the script', PINK), ('e7', 'echo $?', 'Exit code: 1', WARN)])
s_strict = _lab('Strict mode', 'Stop at the first failure.', 's1', RB, [('s1', 'cat loose.sh', 'No safety net', ACC), ('s2', 'bash loose.sh', 'Carries on after an error', BAD), ('s3', 'cat strict.sh', 'set -euo pipefail', GOOD), ('s4', 'bash strict.sh', 'Stops at the cd', VIO), ('s5', 'echo $?', 'Exit code: 1', WARN), ('s6', 'cat unset.sh', 'set -u', PINK), ('s7', 'bash unset.sh', 'Unbound variable', BAD)])
s_trap = _lab('Clean up with trap', 'Runs however the script ends.', 't1', RB, [('t1', 'cat trap.sh', 'trap ... EXIT', ACC), ('t2', 'bash trap.sh', 'Fails, then cleans up', GOOD), ('t3', 'echo $?', 'Still a failure: 1', WARN), ('t4', 'ls /tmp', 'Nothing left behind', VIO)])
s_logging = _lab('Logging', 'Timestamps on standard error.', 'l1', RB, [('l1', 'cat log.sh', 'A log function', ACC), ('l2', 'bash log.sh', 'Time, level, message', GOOD), ('l3', '2> run.log', 'Logs to a file', VIO), ('l4', 'cat run.log', 'The record', WARN)])
s_build = _lab('Put it together', 'One safe script.', 'w1', RB, [('w1', 'cat safe.sh', 'Strict, trap, exit code', ACC), ('w2', 'bash safe.sh', '|| true allows no match', GOOD), ('w3', 'echo $?', 'Exit code: 1', WARN)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: exit 0 means failure', 'Zero means success.', 'my2'), ('Myth: set -e catches all', 'Not in if tests or after ||.', 'my3'), ('Myth: trap is for Ctrl-C', 'EXIT runs on every exit.', 'my4'), ('Myth: logs go to stdout', 'Logs go to stderr.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Exit codes. Strict mode. Traps. Logs.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Read $?', 'b2'), ('exit N', 'b3'), ('set -euo pipefail', 'b4'), ('trap ... EXIT', 'b5'), ('Timestamped logs', 'b6'), ('|| true', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  $?', 'works and fails', PINK, 'z2'), ('2  exit', '0 or 1 by a test', ACC, 'z3'), ('3  set -euo', 'prove it stops', WARN, 'z4'), ('4  trap', 'no temp left', VIO, 'z5'), ('5  log', 'timestamps to a file', BAD, 'z6'), ('6  || true', 'survive no match', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which exit code means success?', 'f12'), ('What does set -u do?', 'f13'), ('When does a trap on EXIT run?', 'f14'), ('Where do log messages go?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O06', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: secrets and safe input', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'exitcodes': s_exitcodes, 'strict': s_strict, 'trap': s_trap, 'logging': s_logging, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'exitcodes': ('question', ACC), 'strict': ('test', VIO), 'trap': ('gear', WARN), 'logging': ('board', GOOD), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'exitcodes': [('e2', 1, 1, 4, 205, ''), ('e3', 1, 1, 4, 22, ''), ('e4', 1, 1, 4, 790, ''), ('e5', 1, 1, 4, 22, ''), ('e6', 4, 1, 4, 125, ''), ('e7', 1, 1, 4, 190, ''), ('e8', 1, 1, 4, 22, '')],
 'strict': [('s3', 1, 1, 4, 900, ''), ('s3', 3, 1, 4, 240, ''), ('s4', 2, 1, 4, 260, ''), ('s5', 1, 1, 4, 840, ''), ('s6', 1, 1, 4, 22, ''), ('s7', 2, 1, 4, 100, ''), ('s8', 1, 1, 4, 610, '')],
 'trap': [('t2', 4, 1, 4, 630, ''), ('t3', 2, 1, 4, 160, ''), ('t4', 1, 1, 4, 22, '')],
 'logging': [('l2', 2, 1, 4, 655, ''), ('l3', 1, 2, 4, 400, ''), ('l5', 1, 2, 4, 400, '')],
 'build': [('w2', 5, 1, 4, 535, ''), ('w3', 1, 1, 4, 145, ''), ('w4', 1, 1, 4, 22, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson42/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
