import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 39  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'MC05-O03': 'M C zero five, objective three', 'bash': 'bash', 'shebang': 'shebang', 'stdout': 'standard out', 'ufw': 'U F W', 'sshd': 'S S H D', 'ed25519': 'E D two five five one nine', 'eth0': 'eth zero', 'MC04-O10': 'M C zero four, objective ten', 'MC04-O09': 'M C zero four, objective nine', 'chmod': 'C H mod', 'sed': 'sed', 'nc': 'N C', 'diff': 'diff', 'tmp': 'temp', 'http': 'H T T P', 'systemd-analyze': 'system D analyze', 'tcp': 'T C P', 'du': 'D U', 'df': 'D F', 'loopback': 'loop back', 'ping': 'ping', 'ss': 'S S', 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Bash scripting  ·  Lesson 39', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "A script that cannot decide is just a list of commands. Real scripts check a condition, choose a path, repeat work, and reuse code."),
  c('h2', "Today you learn four tools. If and test, to make decisions. Case, to pick one of many answers. For and while loops, to repeat work. And functions, to reuse a block of commands."),
  c('h3', "Every demo is a real recording on Ubuntu."),
 ]),
 ('if', [
  c('d1', "Scripts make decisions with if. Here is one. Type: cat age.sh.", "Scripts make decisions with if. Here is one. Type: cat age dot S H."),
  c('d2', "If the test in square brackets is true, the first branch runs. Otherwise the else branch runs. Dash G E means greater than or equal. Run it with the number twenty. Type: dot slash age dot S H, twenty.", "If the test in square brackets is true, the first branch runs. Otherwise the else branch runs. Dash G E means greater than or equal. Run it with the number twenty. Type: dot slash age dot S H, twenty."),
  c('d3', "Adult. Now ten. Type: dot slash age dot S H, ten.", "Adult. Now ten. Type: dot slash age dot S H, ten."),
  c('d4', "Minor. The square brackets are really a command, named test. It reports true or false with an exit status. Type: open square bracket, five, dash G T, three, close square bracket, semicolon, echo dollar question mark.", "Minor. The square brackets are really a command, named test. It reports true or false with an exit status. Type: open square bracket, five, dash G T, three, close square bracket, semicolon, echo, dollar, question mark."),
  c('d5', "Zero. In the shell, zero means true. Now a test that is false. Type: open square bracket, five, dash G T, nine, close square bracket, semicolon, echo dollar question mark.", "Zero. In the shell, zero means true. Now a test that is false. Type: open square bracket, five, dash G T, nine, close square bracket, semicolon, echo, dollar, question mark."),
  c('d6', "One. Anything other than zero means false. The if statement simply reads that exit status, and picks a branch."),
 ]),
 ('tests', [
  c('q1', "Tests come in three kinds: files, strings and numbers. Files first. Does notes dot text exist? Dash F tests for a regular file. Type: open square bracket, dash F, notes dot text, close square bracket, double ampersand, echo, double quote, file exists, double quote.", "Tests come in three kinds: files, strings and numbers. Files first. Does notes dot text exist? Dash F tests for a regular file. Type: open square bracket, dash F, notes dot text, close square bracket, double ampersand, echo, double quote, file exists, double quote."),
  c('q2', "File exists. The double ampersand means: run the next part only if the test was true. Dash D tests for a directory. Type: open square bracket, dash D, docs, close square bracket, double ampersand, echo, double quote, directory exists, double quote.", "File exists. The double ampersand means: run the next part only if the test was true. Dash D tests for a directory. Type: open square bracket, dash D, docs, close square bracket, double ampersand, echo, double quote, directory exists, double quote."),
  c('q3', "Directory exists. The double pipe means the opposite: run the next part only if the test failed. Type: open square bracket, dash D, no dir, close square bracket, double pipe, echo, double quote, no such directory, double quote.", "Directory exists. The double pipe means the opposite: run the next part only if the test failed. Type: open square bracket, dash D, no dir, close square bracket, double pipe, echo, double quote, no such directory, double quote."),
  c('q4', "No such directory. Next, strings. First store a name. Type: name equals Sam.", "No such directory. Next, strings. First store a name. Type: name equals Sam."),
  c('q5', "Strings use a single equals sign, with a space on each side. Type: open square bracket, double quote, dollar name, double quote, equals, Sam, close square bracket, double ampersand, echo, double quote, same name, double quote.", "Strings use a single equals sign, with a space on each side. Type: open square bracket, double quote, dollar name, double quote, equals, Sam, close square bracket, double ampersand, echo, double quote, same name, double quote."),
  c('q6', "Same name. Numbers use letters, not symbols: dash L T for less than, dash G T for greater than, dash E Q for equal. Type: open square bracket, seven, dash L T, ten, close square bracket, double ampersand, echo, double quote, seven is less, double quote.", "Same name. Numbers use letters, not symbols: dash L T for less than, dash G T for greater than, dash E Q for equal. Type: open square bracket, seven, dash L T, ten, close square bracket, double ampersand, echo, double quote, seven is less, double quote."),
  c('q7', "Seven is less. Now the classic trap: an empty variable, with no quotes. Type: open square bracket, dollar empty, equals, x, close square bracket.", "Seven is less. Now the classic trap: an empty variable, with no quotes. Type: open square bracket, dollar empty, equals, x, close square bracket."),
  c('q8', "An error. The shell removed the empty variable, and the test lost its left side. Quote the variable, and the test stays valid. Type: open square bracket, double quote, dollar empty, double quote, equals, x, close square bracket, double pipe, echo, double quote, quoted is safe, double quote.", "An error. The shell removed the empty variable, and the test lost its left side. Quote the variable, and the test stays valid. Type: open square bracket, double quote, dollar empty, double quote, equals, x, close square bracket, double pipe, echo, double quote, quoted is safe, double quote."),
  c('q9', "Quoted is safe. Always quote a variable inside a test."),
 ]),
 ('case', [
  c('m1', "When one value has many possible answers, use case. Here is a small menu script. Type: cat menu.sh.", "When one value has many possible answers, use case. Here is a small menu script. Type: cat menu dot S H."),
  c('m2', "Each pattern ends with a close parenthesis, and each branch ends with a double semicolon. The star pattern matches anything else. Run it with start. Type: dot slash menu dot S H, start.", "Each pattern ends with a close parenthesis, and each branch ends with a double semicolon. The star pattern matches anything else. Run it with start. Type: dot slash menu dot S H, start."),
  c('m3', "Starting. Now stop. Type: dot slash menu dot S H, stop.", "Starting. Now stop. Type: dot slash menu dot S H, stop."),
  c('m4', "Stopping. And now a word that no pattern matches. Type: dot slash menu dot S H, jump.", "Stopping. And now a word that no pattern matches. Type: dot slash menu dot S H, jump."),
  c('m5', "The star branch caught it, and printed a usage message. Notice dollar zero, the name of the script itself."),
  c('m6', "Case is cleaner than a long chain of if statements, and the star branch gives you a safe default."),
 ]),
 ('loops', [
  c('l1', "Loops repeat work. The for loop walks through a list. Type: cat for dot S H.", "Loops repeat work. The for loop walks through a list. Type: cat for dot S H."),
  c('l2', "For each word in the list, the body runs once, with name set to that word. Run it. Type: dot slash for dot S H.", "For each word in the list, the body runs once, with name set to that word. Run it. Type: dot slash for dot S H."),
  c('l3', "Three words, three rounds. The list can also be files that match a pattern. Type: for f in star dot log, semicolon, do, echo, double quote, found dollar f, double quote, semicolon, done.", "Three words, three rounds. The list can also be files that match a pattern. Type: for f in star dot log, semicolon, do, echo, double quote, found dollar f, double quote, semicolon, done."),
  c('l4', "One round per matching file. Now the while loop. It repeats as long as its test is true. Type: cat count dot S H.", "One round per matching file. Now the while loop. It repeats as long as its test is true. Type: cat count dot S H."),
  c('l5', "The test is dash L E, less than or equal. The line with double round brackets does arithmetic: it adds one each round. Without it, the loop would never end. Run it. Type: dot slash count dot S H.", "The test is dash L E, less than or equal. The line with double round brackets does arithmetic: it adds one each round. Without it, the loop would never end. Run it. Type: dot slash count dot S H."),
  c('l6', "Round one, two, three. Then the test turned false, and the loop ended."),
  c('l7', "A loop that never ends is an infinite loop. If you ever start one, press control C to stop it."),
 ]),
 ('func', [
  c('u1', "A function is a named block of commands that you can reuse. Type: cat func dot S H.", "A function is a named block of commands that you can reuse. Type: cat func dot S H."),
  c('u2', "You define a function once, with a name, round brackets and braces. Then you call it like any command, and the words you pass become dollar one inside it. Run the script. Type: dot slash func dot S H.", "You define a function once, with a name, round brackets and braces. Then you call it like any command, and the words you pass become dollar one inside it. Run the script. Type: dot slash func dot S H."),
  c('u3', "Hello, Sam. The check function then ran twice, with two different file names, and printed a different result each time."),
  c('u4', "Functions keep a long script readable, and a fix in one place applies everywhere. A function can also end with a status, using the return keyword, and an if statement can test it."),
  c('u5', "One rule: define a function before you call it."),
 ]),
 ('build', [
  c('w1', "Now combine everything, in a small health check. Type: cat health dot S H.", "Now combine everything, in a small health check. Type: cat health dot S H."),
  c('w2', "A function, a test, a loop and arithmetic. The loop walks over every argument, quoted, and the function counts the failures. Run it with two files that exist. Type: dot slash health dot S H, notes dot text, app dot log.", "A function, a test, a loop and arithmetic. The loop walks over every argument, quoted, and the function counts the failures. Run it with two files that exist. Type: dot slash health dot S H, notes dot text, app dot log."),
  c('w3', "All good. Now give it a file that does not exist. Type: dot slash health dot S H, notes dot text, gone dot text.", "All good. Now give it a file that does not exist. Type: dot slash health dot S H, notes dot text, gone dot text."),
  c('w4', "One file failed, and the script gave a clear count. A script like this can run on a schedule, and tell you what broke."),
  c('w5', "Decide. Choose. Repeat. Reuse."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: square brackets are special syntax. No. They are a command named test, so the spaces inside them are required."),
  c('my3', "Myth two: dash E Q and equals are the same. No. Dash E Q compares numbers. Equals compares text."),
  c('my4', "Myth three: a while loop stops by itself. No. It stops only when its test turns false, so change something inside the loop."),
  c('my5', "Myth four: a function returns text. No. It prints text, and returns a status. Capture the text with command substitution."),
  c('my6', "Test it. Choose it. Repeat it. Reuse it."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Write an if statement with an else branch, using a test in square brackets."),
  c('b3', "Use file, string and number tests correctly, and quote your variables."),
  c('b4', "Write a case statement with a star branch as the default."),
  c('b5', "Write a for loop, and a while loop that ends."),
  c('b6', "Define a function, and call it with arguments."),
  c('b7', "Combine them in one small script, and explain its exit status."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Type every command yourself."),
  c('z2', "One: write an if and else script that tells you whether a number is at least eighteen."),
  c('z3', "Two: test a file, a directory, a string and a number. Then try the empty variable trap, with and without quotes."),
  c('z4', "Three: write a case script for start and stop, with a star branch for anything else."),
  c('z5', "Four: write a for loop over a list, and a for loop over star dot log. Then a while loop that counts to five."),
  c('z6', "Five: write a function, and call it twice with different arguments."),
  c('z7', "Six: write a health check script, and run it with one file that exists and one that does not."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What are the square brackets, really?"), c('f13', "Which case pattern catches everything else?"),
  c('f14', "What stops a while loop from running forever?"), c('f15', "How do you pass values into a function?"),
  c('f16', "Objective covered: MC05-O03.", "Objective covered: M C zero five, objective three, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: text processing, with grep, sed, awk, cut, sort and find."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'd6': 0.5, 'q9': 0.5, 'm6': 0.5, 'l7': 0.5, 'u5': 0.5, 'w5': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'if': 'If and else', 'tests': 'Tests', 'case': 'The case statement', 'loops': 'For and while loops', 'func': 'Functions', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Decide, repeat, reuse', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('if / test', 'make a decision', ACC), ('case', 'pick one of many', VIO), ('for / while', 'repeat work', WARN), ('function', 'reuse a block', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Scripts that think.', 880, C['h3'], GOOD, 1700)); return E
s_if = _lab('If and else', 'A test picks a branch.', 'd1', RB, [('d1', 'cat age.sh', 'if / else', ACC), ('d2', './age.sh 20', 'Test true: adult', GOOD), ('d3', './age.sh 10', 'Test false: minor', VIO), ('d4', '[ 5 -gt 3 ]; echo $?', '0 means true', WARN), ('d5', '[ 5 -gt 9 ]; echo $?', '1 means false', BAD)])
s_tests = _lab('Tests', 'Files, strings and numbers.', 'q1', RB, [('q1', '[ -f notes.txt ]', 'File exists', ACC), ('q2', '[ -d docs ]', 'Directory exists', GOOD), ('q3', '|| echo ...', 'Runs if test fails', VIO), ('q5', '[ "$name" = Sam ]', 'Strings: =', WARN), ('q6', '[ 7 -lt 10 ]', 'Numbers: -lt -gt -eq', PINK), ('q7', '[ $empty = x ]', 'Unquoted: error', BAD)])
s_case = _lab('The case statement', 'One value, many answers.', 'm1', RB, [('m1', 'cat menu.sh', 'case ... esac', ACC), ('m2', './menu.sh start', 'Pattern: start)', GOOD), ('m3', './menu.sh stop', 'Pattern: stop)', VIO), ('m4', './menu.sh jump', 'Pattern: *)  default', WARN)])
s_loops = _lab('For and while loops', 'Repeat work, then stop.', 'l1', RB, [('l1', 'cat for.sh', 'for name in list', ACC), ('l2', './for.sh', 'One round per word', GOOD), ('l3', 'for f in *.log', 'One round per file', VIO), ('l4', 'cat count.sh', 'while test', WARN), ('l5', './count.sh', 'Stops when false', PINK)])
s_func = _lab('Functions', 'A named block you can reuse.', 'u1', RB, [('u1', 'cat func.sh', 'name() { ... }', ACC), ('u2', './func.sh', 'Call with arguments', GOOD)])
s_build = _lab('Put it together', 'Function, test, loop, count.', 'w1', RB, [('w1', 'cat health.sh', 'Read the script', ACC), ('w2', './health.sh notes.txt app.log', 'All present', GOOD), ('w3', './health.sh notes.txt gone.txt', 'One missing', BAD)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: [ ] is syntax', 'It is a command: spaces required.', 'my2'), ('Myth: -eq is =', '-eq compares numbers, = compares text.', 'my3'), ('Myth: while stops alone', 'Only when its test turns false.', 'my4'), ('Myth: functions return text', 'They print text, and return a status.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Test it. Choose it. Repeat it. Reuse it.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('if and else', 'b2'), ('Three kinds of test', 'b3'), ('case with *', 'b4'), ('for and while', 'b5'), ('Functions', 'b6'), ('Combine them', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  if / else', 'age check', PINK, 'z2'), ('2  Tests', 'file, dir, text, number', ACC, 'z3'), ('3  case', 'start, stop, default', WARN, 'z4'), ('4  Loops', 'for, for *.log, while', VIO, 'z5'), ('5  Function', 'call it twice', BAD, 'z6'), ('6  Health check', 'found and missing', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What are [ ] really?', 'f12'), ('Which case pattern is the default?', 'f13'), ('What ends a while loop?', 'f14'), ('How do you pass values to a function?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O03', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: text processing', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'if': s_if, 'tests': s_tests, 'case': s_case, 'loops': s_loops, 'func': s_func, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'if': ('test', ACC), 'tests': ('question', WARN), 'case': ('board', VIO), 'loops': ('gear', GOOD), 'func': ('gear', ACC), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'if': [('d2', 3, 1, 4, 372, ''), ('d3', 1, 1, 4, 84, ''), ('d4', 1, 1, 4, 84, ''), ('d5', 1, 1, 4, 22, ''), ('d6', 1, 1, 4, 22, '')],
 'tests': [('q2', 1, 1, 4, 172, ''), ('q3', 1, 1, 4, 247, ''), ('q4', 1, 1, 4, 262, ''), ('q6', 1, 1, 4, 141, ''), ('q7', 1, 1, 4, 202, ''), ('q8', 1, 1, 4, 552, ''), ('q9', 1, 1, 4, 217, '')],
 'case': [('m2', 3, 3, 4, 600, ''), ('m3', 1, 1, 4, 126, ''), ('m4', 1, 1, 4, 126, ''), ('m5', 1, 1, 4, 416, '')],
 'loops': [('l2', 2, 2, 4, 432, ''), ('l3', 1, 3, 4, 220, ''), ('l4', 1, 2, 4, 205, ''), ('l5', 3, 1, 4, 388, ''), ('l5', 5, 1, 4, 190, ''), ('l6', 1, 3, 4, 112, '')],
 'func': [('u2', 2, 3, 4, 300, ''), ('u3', 1, 3, 4, 250, '')],
 'build': [('w2', 11, 3, 4, 285, ''), ('w3', 1, 3, 4, 220, ''), ('w4', 1, 3, 4, 220, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson39/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
