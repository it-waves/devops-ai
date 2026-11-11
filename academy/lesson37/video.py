import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 37  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'MC05-O01': 'M C zero five, objective one', 'bash': 'bash', 'shebang': 'shebang', 'stdout': 'standard out', 'ufw': 'U F W', 'sshd': 'S S H D', 'ed25519': 'E D two five five one nine', 'eth0': 'eth zero', 'MC04-O10': 'M C zero four, objective ten', 'MC04-O09': 'M C zero four, objective nine', 'chmod': 'C H mod', 'sed': 'sed', 'nc': 'N C', 'diff': 'diff', 'tmp': 'temp', 'http': 'H T T P', 'systemd-analyze': 'system D analyze', 'tcp': 'T C P', 'du': 'D U', 'df': 'D F', 'loopback': 'loop back', 'ping': 'ping', 'ss': 'S S', 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Bash scripting  ·  Lesson 37', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "A script is just commands in a file. But before you write one, you must understand how the shell reads a line, because most script bugs start right there."),
  c('h2', "Today, four ideas. How a script runs. How quoting protects your text. How expansion changes your line before a command ever sees it. And how every command reports success or failure with an exit status."),
  c('h3', "Every demo is a real recording on Ubuntu, so you can follow along."),
 ]),
 ('order', [
  c('o1', "First, the big picture. When you press Enter, the shell does not simply run your text."),
  c('o2', "Step one: it splits the line into words."),
  c('o3', "Step two: it expands. Variables, command substitutions, wildcards, and the tilde are all replaced."),
  c('o4', "Step three: it runs the command, with the expanded words."),
  c('o5', "Step four: the command finishes, and leaves an exit status. A number. Zero means success."),
  c('o6', "Keep this order in mind. Almost every strange result comes from step one or step two."),
 ]),
 ('run', [
  c('r1', "First: how a script runs. A script is a text file of commands. Here is one, called hi dot S H. Type: cat hi.sh.", "First: how a script runs. A script is a text file of commands. Here is one, called hi dot S H. Type: cat hi dot S H."),
  c('r2', "The first line, hash, bang, slash bin slash bash, is called the shebang. It names the program that reads the file. Run the script by naming that program yourself. Type: bash hi.sh.", "The first line, hash, bang, slash bin slash bash, is called the shebang. It names the program that reads the file. Run the script by naming that program yourself. Type: bash, hi dot S H."),
  c('r3', "It works. Dollar zero holds the name the script was run as. Now run it directly, the way a real tool runs. Type: dot slash hi dot S H.", "It works. Dollar zero holds the name the script was run as. Now run it directly, the way a real tool runs. Type: dot slash hi dot S H."),
  c('r4', "Permission denied. A file is not a program until it has the execute bit. You know this fix. Type: chmod u+x hi.sh.", "Permission denied. A file is not a program until it has the execute bit. You know this fix. Type: C H mod, u plus x, hi dot S H."),
  c('r5', "Now run it again. Type: dot slash hi dot S H.", "Now run it again. Type: dot slash hi dot S H."),
  c('r6', "It runs, and dollar zero now says dot slash hi dot S H. The shebang told the system to hand the file to bash. Two ways to run it, one result, as long as the file is executable."),
 ]),
 ('quote', [
  c('q1', "Next: quoting. Quotes tell the shell which characters are plain text. First, store a name in a variable. Type: name=Sam. There are no spaces around the equals sign.", "Next: quoting. Quotes tell the shell which characters are plain text. First, store a name in a variable. Type: name equals Sam. There are no spaces around the equals sign."),
  c('q2', "Nothing printed, and that is normal. Now use the variable inside double quotes. Type: echo, double quote, Hi dollar name, double quote.", "Nothing printed, and that is normal. Now use the variable inside double quotes. Type: echo, double quote, Hi dollar name, double quote."),
  c('q3', "Double quotes let the variable expand. Hi Sam. Now single quotes. Type: echo, single quote, Hi dollar name, single quote.", "Double quotes let the variable expand. Hi Sam. Now single quotes. Type: echo, single quote, Hi dollar name, single quote."),
  c('q4', "Single quotes keep every character literal, so the dollar sign stays. Rule: double quotes expand, single quotes do not. Now a classic trap. List this folder. Type: ls.", "Single quotes keep every character literal, so the dollar sign stays. Rule: double quotes expand, single quotes do not. Now a classic trap. List this folder. Type: L S."),
  c('q5', "One file, with a space in its name. Try to remove it without quotes. Type: rm my notes.txt.", "One file, with a space in its name. Try to remove it without quotes. Type: R M, my, notes dot text."),
  c('q6', "Two errors. Without quotes, the shell split the name into two words, and rm looked for two files that do not exist. Quote the name. Type: rm, double quote, my notes dot text, double quote, and and, echo removed.", "Two errors. Without quotes, the shell split the name into two words, and R M looked for two files that do not exist. Quote the name. Type: R M, double quote, my notes dot text, double quote, and and, echo removed."),
  c('q7', "Removed. Quote your variables and your file names, every time."),
 ]),
 ('expand', [
  c('e1', "Now expansion. The shell rewrites parts of your line before the command runs. Start with the tilde. Type: echo ~.", "Now expansion. The shell rewrites parts of your line before the command runs. Start with the tilde. Type: echo, tilde."),
  c('e2', "The tilde became your home folder. Echo never saw a tilde. Next, command substitution: a dollar sign and brackets around a command. The output replaces it. Type: echo, double quote, today is, dollar, bracket, date plus percent A, bracket, double quote.", "The tilde became your home folder. Echo never saw a tilde. Next, command substitution: a dollar sign and brackets around a command. The output replaces it. Type: echo, double quote, today is, dollar, bracket, date plus percent A, bracket, double quote."),
  c('e3', "The date command ran first, and its output was pasted into the line. Now wildcards. Type: echo star dot text.", "The date command ran first, and its output was pasted into the line. Now wildcards. Type: echo, star, dot text."),
  c('e4', "The shell expanded the star into the matching file names. Echo just printed what it was given. Now braces, which build a list. Type: echo file dash, brace a, b, c, brace, dot log.", "The shell expanded the star into the matching file names. Echo just printed what it was given. Now braces, which build a list. Type: echo file dash, open brace, a comma b comma c, close brace, dot log."),
  c('e5', "Braces made three words. One more: arithmetic, with a dollar and double brackets. Type: echo, dollar, double bracket, six times seven.", "Braces made three words. One more: arithmetic, with a dollar and double brackets. Type: echo, dollar, double bracket, six times seven."),
  c('e6', "Forty two. Remember, expansion happens first, and then the command runs. If you want text kept exactly as typed, quote it."),
 ]),
 ('env', [
  c('v1', "Next, the environment. Every program carries a set of named values. A plain shell variable belongs only to this shell. Type: GREETING=hello.", "Next, the environment. Every program carries a set of named values. A plain shell variable belongs only to this shell. Type: GREETING equals hello."),
  c('v2', "Now start a child shell, and ask it to print the variable. Type: bash dash c, then the command in single quotes.", "Now start a child shell, and ask it to print the variable. Type: bash, dash c, then the command in single quotes."),
  c('v3', "Empty. The child cannot see it. To share a variable with child programs, export it. Type: export GREETING.", "Empty. The child cannot see it. To share a variable with child programs, export it. Type: export GREETING."),
  c('v4', "Now run the same test again. Type: bash dash c, and the same command.", "Now run the same test again. Type: bash, dash c, and the same command."),
  c('v5', "Now the child sees hello. Exported variables are the environment, passed down to every child. One famous example is path. Type: echo dollar PATH.", "Now the child sees hello. Exported variables are the environment, passed down to every child. One famous example is path. Type: echo, dollar, path."),
  c('v6', "These folders, separated by colons, are where the shell looks for commands, in order. That is why a command can be found, or not found."),
 ]),
 ('exit', [
  c('x1', "Last idea: exit status. Every command ends with a number. First, a command that works. Type: ls /etc/hostname.", "Last idea: exit status. Every command ends with a number. First, a command that works. Type: L S, slash E T C, slash hostname."),
  c('x2', "It printed the file name. Did it succeed? The shell keeps the answer in dollar question mark. Type: echo dollar question mark.", "It printed the file name. Did it succeed? The shell keeps the answer in dollar question mark. Type: echo, dollar, question mark."),
  c('x3', "Zero. Zero means success. Now a command that fails. Type: ls /nope.", "Zero. Zero means success. Now a command that fails. Type: L S, slash nope."),
  c('x4', "An error message. But the number is the real signal. Type: echo dollar question mark.", "An error message. But the number is the real signal. Type: echo, dollar, question mark."),
  c('x5', "Two. Anything but zero means failure, and the number can say why. Scripts use this with and and, and or or. Type: grep dash q root slash E T C slash passwd, and and, echo found.", "Two. Anything but zero means failure, and the number can say why. Scripts use this with and and, and or or. Type: grep, dash q, root, slash E T C slash passwd, and and, echo found."),
  c('x6', "Found. And and runs the next command only if the first one succeeded. Now the reverse. Type: grep dash q, zzzz, the same file, then or or, echo missing.", "Found. And and runs the next command only if the first one succeeded. Now the reverse. Type: grep, dash q, zzzz, the same file, then or or, echo missing."),
  c('x7', "Missing. Or or runs the next command only if the first one failed. Zero is success, anything else is failure. Scripts decide what to do from this one number."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: a script must end in dot S H. No. The name does not matter. The shebang and the execute bit do."),
  c('my3', "Myth two: single and double quotes are the same. No. Double quotes expand variables. Single quotes keep everything literal."),
  c('my4', "Myth three: zero means false. In the shell it is the opposite. Zero means success."),
  c('my5', "Myth four: quotes are optional if it works today. A file name with a space will break it tomorrow. Quote your variables."),
  c('my6', "Quote it. Expand it. Check the exit status."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Run a script two ways, with bash and directly, and say what the shebang does."),
  c('b3', "Say when to use single quotes, and when to use double."),
  c('b4', "Name four expansions: tilde, variables, command substitution, and wildcards."),
  c('b5', "Explain why a child does not see an unexported variable, and fix it with export."),
  c('b6', "Read an exit status with dollar question mark, and use and and, or or."),
  c('b7', "Quote a file name that has a space, and explain why."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Take your time, and type every command yourself."),
  c('z2', "One: write a three line script with a shebang. Run it with bash, then make it executable and run it directly."),
  c('z3', "Two: create a file with a space in its name. Try to remove it without quotes, read the error, then remove it with quotes."),
  c('z4', "Three: print a message with single quotes, and again with double quotes, using a variable. Compare the output."),
  c('z5', "Four: use command substitution to print today's date, and a brace list to print three file names."),
  c('z6', "Five: set a variable, test it in a child shell, export it, and test again."),
  c('z7', "Six: run one command that succeeds, and one that fails, and print the exit status of each."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does the shebang line do?"), c('f13', "Which quotes expand a variable, single or double?"),
  c('f14', "What does an exit status of zero mean?"), c('f15', "Why must you export a variable?"),
  c('f16', "Objective covered: MC05-O01.", "Objective covered: M C zero five, objective one, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: variables, arguments, input and command substitution."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'o6': 0.5, 'r6': 0.5, 'q7': 0.4, 'e6': 0.5, 'v6': 0.5, 'x7': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'order': 'How the shell reads a line', 'run': 'How a script runs', 'quote': 'Quoting', 'expand': 'Expansion', 'env': 'Environment variables', 'exit': 'Exit status', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))



def s_hook(C, D, dur):
    E = [El(T('How the shell reads a line', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Running', 'shebang and execute bit', ACC), ('Quoting', 'single, double, none', VIO), ('Expansion', 'changed before the command runs', WARN), ('Exit status', 'zero means success', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.2))
    E.append(takeaway('Understand the line, then write the script.', 880, C['h3'], GOOD, 1700)); return E
def s_order(C, D, dur):
    E = head('How the shell reads a line', 'Four steps, always in this order.', C['o1']); E.append(ill(C['o1'] + 0.2, 1400, 170))
    it = [('1  Split', 'the line into words', ACC, 'o2'), ('2  Expand', 'variables, $( ), *, ~', WARN, 'o3'), ('3  Run', 'the command with those words', VIO, 'o4'), ('4  Exit status', 'a number: 0 means success', GOOD, 'o5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s_, TXT)], 44, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Strange results start at step 1 or 2.', 800, C['o6'], GOOD, 1700)); return E
s_run = _lab('How a script runs', 'A text file, a shebang, an execute bit.', 'r1', RB, [('r1', 'cat hi.sh', 'Read the script', ACC), ('r2', 'bash hi.sh', 'Name the program', VIO), ('r3', './hi.sh', 'Symptom: denied', BAD), ('r4', 'chmod u+x', 'Add execute', WARN), ('r5', './hi.sh', 'Runs directly', GOOD)])
s_quote = _lab('Quoting', 'Which characters are plain text?', 'q1', RB, [('q1', 'name=Sam', 'A variable', ACC), ('q2', 'echo "Hi $name"', 'Double: expands', GOOD), ('q3', "echo 'Hi $name'", 'Single: literal', WARN), ('q5', 'rm my notes.txt', 'No quotes: split', BAD), ('q6', 'rm "my notes.txt"', 'Quoted: works', VIO)])
s_expand = _lab('Expansion', 'Rewritten before the command runs.', 'e1', RB, [('e1', 'echo ~', 'Tilde: home', ACC), ('e2', 'echo "$(date +%A)"', 'Command output', VIO), ('e3', 'echo *.txt', 'Wildcard', WARN), ('e4', 'echo file-{a,b,c}.log', 'Brace list', PINK), ('e5', 'echo $((6 * 7))', 'Arithmetic', GOOD)])
s_env = _lab('Environment variables', 'What a child program can see.', 'v1', RB, [('v1', 'GREETING=hello', 'Shell only', ACC), ('v2', 'bash -c ...', 'Child: empty', BAD), ('v3', 'export GREETING', 'Share it', WARN), ('v4', 'bash -c ...', 'Child: hello', GOOD), ('v5', 'echo $PATH', 'Command search', VIO)])
s_exit = _lab('Exit status', 'Zero is success. Anything else is not.', 'x1', RB, [('x1', 'ls /etc/hostname', 'A command that works', ACC), ('x2', 'echo $?', 'Status: 0', GOOD), ('x3', 'ls /nope', 'A command that fails', BAD), ('x4', 'echo $?', 'Status: 2', WARN), ('x5', '&&   ||', 'Decide by status', VIO)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: scripts end in .sh', 'The shebang and execute bit matter.', 'my2'), ("Myth: ' and \" are the same", 'Double expands, single is literal.', 'my3'), ('Myth: zero means false', 'In the shell, zero is success.', 'my4'), ('Myth: quotes are optional', 'A space in a name will break it.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Quote it. Expand it. Check the exit status.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Run two ways, shebang', 'b2'), ('Single vs double quotes', 'b3'), ('Four expansions', 'b4'), ('export and children', 'b5'), ('$? with && and ||', 'b6'), ('Quote a spaced name', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  Script', 'bash it, then chmod and run', PINK, 'z2'), ('2  Spaces', 'break rm, then quote it', ACC, 'z3'), ('3  Quotes', "single vs double", WARN, 'z4'), ('4  Expand', 'date and a brace list', VIO, 'z5'), ('5  Export', 'child shell, before and after', BAD, 'z6'), ('6  Status', 'one success, one failure', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does the shebang line do?', 'f12'), ('Which quotes expand a variable?', 'f13'), ('What does exit status zero mean?', 'f14'), ('Why must you export a variable?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O01', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: variables and arguments', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, order=s_order, run=s_run, quote=s_quote, expand=s_expand, env=s_env, exit=s_exit, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(order=('board', ACC), run=('gear', ACC), quote=('question', WARN), expand=('gear', VIO), env=('eye', GOOD), exit=('test', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'run': [('r3', 1, 1, 4, 262, ''), ('r4', 1, 1, 4, 490, ''), ('r6', 1, 1, 4, 285, '')],
 'quote': [('q3', 1, 1, 4, 100, ''), ('q4', 1, 1, 4, 135, ''), ('q5', 1, 1, 4, 225, ''), ('q6', 1, 2, 4, 870, ''), ('q7', 1, 1, 4, 120, '')],
 'expand': [('e2', 1, 1, 4, 210, ''), ('e3', 1, 1, 4, 290, ''), ('e4', 1, 1, 4, 185, ''), ('e5', 1, 1, 4, 500, ''), ('e6', 1, 1, 4, 40, '')],
 'env': [('v3', 1, 1, 4, 180, ''), ('v5', 1, 1, 4, 270, ''), ('v6', 1, 1, 4, 940, '')],
 'exit': [('x2', 1, 1, 4, 215, ''), ('x3', 1, 1, 4, 30, ''), ('x4', 1, 1, 4, 805, ''), ('x5', 1, 1, 4, 30, ''), ('x6', 1, 1, 4, 85, ''), ('x7', 1, 1, 4, 110, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson37/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
