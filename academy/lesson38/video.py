import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 38  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'MC05-O02': 'M C zero five, objective two', 'bash': 'bash', 'shebang': 'shebang', 'stdout': 'standard out', 'ufw': 'U F W', 'sshd': 'S S H D', 'ed25519': 'E D two five five one nine', 'eth0': 'eth zero', 'MC04-O10': 'M C zero four, objective ten', 'MC04-O09': 'M C zero four, objective nine', 'chmod': 'C H mod', 'sed': 'sed', 'nc': 'N C', 'diff': 'diff', 'tmp': 'temp', 'http': 'H T T P', 'systemd-analyze': 'system D analyze', 'tcp': 'T C P', 'du': 'D U', 'df': 'D F', 'loopback': 'loop back', 'ping': 'ping', 'ss': 'S S', 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Bash scripting  ·  Lesson 38', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
SCENES = [
 ('hook', [
  c('h1', "A script that does the same thing every time is not very useful. Useful scripts take input: a name, a file, a number. Today you learn four ways to feed a script."),
  c('h2', "Variables, to store values. Positional arguments, to pass values in when you run the script. The read command, to ask the user. And command substitution, to capture the output of another command."),
  c('h3', "Every demo is a real recording on Ubuntu."),
 ]),
 ('vars', [
  c('a1', "Variables first. A variable is a named box for a value. Type: city=Paris. There are no spaces around the equals sign.", "Variables first. A variable is a named box for a value. Type: city equals Paris. There are no spaces around the equals sign."),
  c('a2', "Nothing printed. Read it back with a dollar sign. Type: echo, double quote, I live in dollar city, double quote.", "Nothing printed. Read it back with a dollar sign. Type: echo, double quote, I live in dollar city, double quote."),
  c('a3', "Paris. Now a trap. I want the word Parisland. Type: echo, double quote, dollar cityland, double quote.", "Paris. Now a trap. I want the word Parisland. Type: echo, double quote, dollar cityland, double quote."),
  c('a4', "An empty line. The shell looked for a variable called cityland, which does not exist. Mark where the name ends, with braces. Type: echo, double quote, dollar, open brace, city, close brace, land, double quote.", "An empty line. The shell looked for a variable called cityland, which does not exist. Mark where the name ends, with braces. Type: echo, double quote, dollar, open brace, city, close brace, land, double quote."),
  c('a5', "Parisland. Use braces whenever text touches the name. Next, a default value, for a variable that is not set. Type: echo, double quote, dollar, open brace, name, colon, dash, stranger, close brace, double quote.", "Parisland. Use braces whenever text touches the name. Next, a default value, for a variable that is not set. Type: echo, double quote, dollar, open brace, name, colon, dash, stranger, close brace, double quote."),
  c('a6', "Stranger. The variable name was never set, so the default was used. One last trap: spaces. Type: city, space, equals, space, Paris.", "Stranger. The variable name was never set, so the default was used. One last trap: spaces. Type: city, space, equals, space, Paris."),
  c('a7', "The shell treated city as a command, and failed. An assignment has no spaces. Keep it tight."),
 ]),
 ('args', [
  c('g1', "Next, positional arguments. They are the words you type after the script name. Here is a script that uses them. Type: cat greet.sh.", "Next, positional arguments. They are the words you type after the script name. Here is a script that uses them. Type: cat greet dot S H."),
  c('g2', "Dollar one is the first argument. Dollar hash is how many there are. Dollar at is all of them. Run it with one word. Type: dot slash greet dot S H, Sam.", "Dollar one is the first argument. Dollar hash is how many there are. Dollar at is all of them. Run it with one word. Type: dot slash greet dot S H, Sam."),
  c('g3', "First is Sam, and the count is one. Now three words. Type: dot slash greet dot S H, Sam Lee Kim.", "First is Sam, and the count is one. Now three words. Type: dot slash greet dot S H, Sam Lee Kim."),
  c('g4', "The count is three, and all three are listed. What if one argument has a space? Quote it, and it stays one argument. Type: dot slash greet dot S H, double quote, Sam Lee, double quote, Kim.", "The count is three, and all three are listed. What if one argument has a space? Quote it, and it stays one argument. Type: dot slash greet dot S H, double quote, Sam Lee, double quote, Kim."),
  c('g5', "First is Sam Lee, and the count is two. Quotes group words, just as before. Last case: no arguments at all. Type: dot slash greet dot S H.", "First is Sam Lee, and the count is two. Quotes group words, just as before. Last case: no arguments at all. Type: dot slash greet dot S H."),
  c('g6', "First is empty, and the count is zero. A good script checks the count before it uses an argument. You learn how in the next lesson."),
 ]),
 ('input', [
  c('i1', "Third way: ask the user. The read command waits for a line of input. Here is a short script. Type: cat ask.sh.", "Third way: ask the user. The read command waits for a line of input. Here is a short script. Type: cat ask dot S H."),
  c('i2', "Read dash p prints a prompt, then stores what the user types in a variable. Run it, and then answer the question. Type: dot slash ask dot S H.", "Read, dash p, prints a prompt, then stores what the user types in a variable. Run it, and then answer the question. Type: dot slash ask dot S H.", 6.0),
  c('i3', "Welcome, Maya. The script used my answer. Scripts also run with no person present, so input can come from a pipe. Type: echo Lee, pipe, dot slash ask dot S H.", "Welcome, Maya. The script used my answer. Scripts also run with no person present, so input can come from a pipe. Type: echo Lee, pipe, dot slash ask dot S H."),
  c('i4', "No prompt appeared, because there was no keyboard to ask. But the answer was read from the pipe. The same script works both ways."),
 ]),
 ('subst', [
  c('s1', "Fourth way: command substitution. It captures a command's output, so you can store it. Type: today equals dollar, bracket, date plus percent capital F, bracket. That format is year, month, day.", "Fourth way: command substitution. It captures a command's output, so you can store it. Type: today equals dollar, bracket, date plus percent capital F, bracket. That format is year, month, day."),
  c('s2', "Nothing printed. The output went into the variable. Use it inside a file name. Type: echo, double quote, backup dash dollar today dot tar, double quote.", "Nothing printed. The output went into the variable. Use it inside a file name. Type: echo, double quote, backup dash dollar today dot tar, double quote."),
  c('s3', "A dated file name, built by the shell. Now count things. Type: L S, pipe, W C, dash l. That counts lines.", "A dated file name, built by the shell. Now count things. Type: L S, pipe, W C, dash l. That counts lines."),
  c('s4', "Three files. Store that number. Type: count equals dollar, bracket, L S, pipe, W C, dash l, bracket.", "Three files. Store that number. Type: count equals dollar, bracket, L S, pipe, W C, dash l, bracket."),
  c('s5', "Again nothing printed. Now print a sentence with it. Type: echo, double quote, There are dollar count files, double quote.", "Again nothing printed. Now print a sentence with it. Type: echo, double quote, There are dollar count files, double quote."),
  c('s6', "There are three files. A script can now report facts about the system, not just fixed text. The older style uses backticks. It works, but brackets are easier to read, and they can be nested."),
 ]),
 ('build', [
  c('t1', "Now put it all together in one script. Type: cat backup.sh.", "Now put it all together in one script. Type: cat backup dot S H."),
  c('t2', "A default name with colon dash, a date from command substitution, and a message. Run it with no argument. Type: dot slash backup dot S H.", "A default name with colon dash, a date from command substitution, and a message. Run it with no argument. Type: dot slash backup dot S H."),
  c('t3', "It used the default name, data, and today's date. Now pass a name. Type: dot slash backup dot S H, photos.", "It used the default name, data, and today's date. Now pass a name. Type: dot slash backup dot S H, photos."),
  c('t4', "Photos. Same script, different input. That is why scripts use variables and arguments."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: spaces around the equals sign are fine. No. Spaces make it a command, and it fails."),
  c('my3', "Myth two: dollar one is the script name. No. That is dollar zero. Dollar one is the first argument."),
  c('my4', "Myth three: an unquoted variable is always fine. If the value holds a space, it splits. Quote it."),
  c('my5', "Myth four: read only works with a keyboard. It also reads from pipes and files."),
  c('my6', "Set it. Pass it. Ask for it. Capture it."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Assign and print a variable, with no spaces around the equals sign."),
  c('b3', "Use braces, and a default value with colon dash."),
  c('b4', "Name dollar zero, dollar one, dollar hash, and dollar at."),
  c('b5', "Quote an argument that contains a space."),
  c('b6', "Use read to take input, from a keyboard and from a pipe."),
  c('b7', "Capture a command's output with a dollar sign and brackets."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Type every command yourself."),
  c('z2', "One: set two variables, and print them in one sentence, using braces."),
  c('z3', "Two: write a script that prints its first argument, the count, and all arguments. Run it with zero, one, and three arguments."),
  c('z4', "Three: run it with an argument that contains a space, with quotes and without."),
  c('z5', "Four: write a script that asks your name with read, and greets you. Run it by hand, then from a pipe."),
  c('z6', "Five: store today's date and the number of files in your folder, and print one sentence with both."),
  c('z7', "Six: write a backup name script with a default value, and run it with and without an argument."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does dollar hash hold?"), c('f13', "How do you keep an argument with a space as one argument?"),
  c('f14', "Which command asks the user for input?"), c('f15', "What does a dollar sign with brackets do?"),
  c('f16', "Objective covered: MC05-O02.", "Objective covered: M C zero five, objective two, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: conditions, tests, case statements, loops and functions."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'a7': 0.5, 'g6': 0.5, 'i4': 0.5, 's6': 0.5, 't4': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'vars': 'Variables', 'args': 'Positional arguments', 'input': 'Reading input', 'subst': 'Command substitution', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Feed your script', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Variables', 'named boxes for values', ACC), ('Arguments', 'words after the script name', VIO), ('read', 'ask the user', WARN), ('$( )', 'capture a command output', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.2))
    E.append(takeaway('Same script, different input.', 880, C['h3'], GOOD, 1700)); return E
s_vars = _lab('Variables', 'Named boxes for values.', 'a1', RB, [('a1', 'city=Paris', 'No spaces', ACC), ('a2', 'echo "$city"', 'Read it back', GOOD), ('a4', '${city}land', 'Braces end the name', VIO), ('a5', '${name:-stranger}', 'Default value', WARN), ('a6', 'city = Paris', 'Spaces: fails', BAD)])
s_args = _lab('Positional arguments', 'Words after the script name.', 'g1', RB, [('g1', 'cat greet.sh', '$1  $#  $@', ACC), ('g2', './greet.sh Sam', 'One argument', GOOD), ('g3', './greet.sh Sam Lee Kim', 'Three arguments', VIO), ('g4', '"Sam Lee" Kim', 'Quotes group', WARN), ('g5', './greet.sh', 'None: empty, 0', BAD)])
s_input = _lab('Reading input', 'Ask the user, or read a pipe.', 'i1', RB, [('i1', 'cat ask.sh', 'read -p', ACC), ('i2', './ask.sh', 'Answer by keyboard', GOOD), ('i3', 'echo Lee | ./ask.sh', 'Answer from a pipe', VIO)])
s_subst = _lab('Command substitution', 'Capture a command output.', 's1', RB, [('s1', 'today=$(date +%F)', 'Store the output', ACC), ('s2', 'backup-$today.tar', 'Use it in text', GOOD), ('s3', 'ls | wc -l', 'Count lines', VIO), ('s4', 'count=$(ls | wc -l)', 'Store the count', WARN), ('s5', 'There are $count', 'Use it', PINK)])
s_build = _lab('Put it together', 'One script, three ideas.', 't1', RB, [('t1', 'cat backup.sh', 'Read the script', ACC), ('t2', './backup.sh', 'Default: data', GOOD), ('t3', './backup.sh photos', 'Argument: photos', VIO)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: spaces around =', 'Spaces make it a command.', 'my2'), ('Myth: $1 is the script', '$0 is the script, $1 the first argument.', 'my3'), ('Myth: quotes are optional', 'A space in the value splits it.', 'my4'), ('Myth: read needs a keyboard', 'It reads pipes and files too.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Set it. Pass it. Ask for it. Capture it.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Assign and print', 'b2'), ('Braces and defaults', 'b3'), ('$0 $1 $# $@', 'b4'), ('Quote spaced args', 'b5'), ('read: keyboard, pipe', 'b6'), ('Capture with $( )', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  Variables', 'two, in a sentence', PINK, 'z2'), ('2  Arguments', 'first, count, all', ACC, 'z3'), ('3  Spaces', 'quoted and not', WARN, 'z4'), ('4  Read', 'by hand, then piped', VIO, 'z5'), ('5  Capture', 'date and file count', BAD, 'z6'), ('6  Default', 'with and without', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does $# hold?', 'f12'), ('Keep a spaced argument as one?', 'f13'), ('Which command asks for input?', 'f14'), ('What does $( ) do?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O02', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: conditions and loops', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, vars=s_vars, args=s_args, input=s_input, subst=s_subst, build=s_build, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(vars=('board', ACC), args=('gear', VIO), input=('question', WARN), subst=('gear', GOOD), build=('test', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'vars': [('a3', 1, 1, 4, 240, ''), ('a5', 1, 1, 4, 150, ''), ('a6', 1, 1, 4, 135, ''), ('a7', 1, 1, 4, 450, '')],
 'args': [('g2', 2, 3, 4, 270, ''), ('g3', 1, 2, 4, 170, ''), ('g4', 1, 3, 4, 260, ''), ('g5', 1, 2, 4, 200, ''), ('g6', 1, 3, 4, 150, '')],
 'input': [('i2', 2, 1, 4, 430, ''), ('i3', 1, 2, 4, 260, ''), ('i4', 1, 1, 4, 195, '')],
 'subst': [('s3', 1, 1, 4, 325, ''), ('s4', 1, 1, 4, 30, ''), ('s6', 1, 1, 4, 265, '')],
 'build': [('t2', 2, 2, 4, 270, ''), ('t3', 1, 1, 4, 540, ''), ('t4', 1, 1, 4, 570, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson38/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
