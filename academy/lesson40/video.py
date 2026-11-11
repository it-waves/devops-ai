import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 40  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'MC05-O04': 'M C zero five, objective four', 'grep': 'grep', 'awk': 'awk', 'uniq': 'unique', 'bash': 'bash', 'shebang': 'shebang', 'stdout': 'standard out', 'ufw': 'U F W', 'sshd': 'S S H D', 'ed25519': 'E D two five five one nine', 'eth0': 'eth zero', 'MC04-O10': 'M C zero four, objective ten', 'MC04-O09': 'M C zero four, objective nine', 'chmod': 'C H mod', 'sed': 'sed', 'nc': 'N C', 'diff': 'diff', 'tmp': 'temp', 'http': 'H T T P', 'systemd-analyze': 'system D analyze', 'tcp': 'T C P', 'du': 'D U', 'df': 'D F', 'loopback': 'loop back', 'ping': 'ping', 'ss': 'S S', 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Bash scripting  ·  Lesson 40', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "Real servers produce text: logs, lists and configuration files. Searching and reshaping that text is one of the most useful skills in operations."),
  c('h2', "Today you learn six tools. grep, to search. Cut and sort, to pick columns and put lines in order. sed, to replace text. awk, to calculate. And find, to locate files."),
  c('h3', "Every demo is a real recording on Ubuntu."),
 ]),
 ('grep', [
  c('r1', "First, grep. It prints the lines of a file that match a pattern. Here is a small application log. Type: cat app dot log.", "First, grep. It prints the lines of a file that match a pattern. Here is a small application log. Type: cat app dot log."),
  c('r2', "Six lines, with three levels: info, warn and error. Find the errors. Type: grep, ERROR, app dot log.", "Six lines, with three levels: info, warn and error. Find the errors. Type: grep, ERROR, app dot log."),
  c('r3', "Only the two error lines. Now count the info lines instead, with dash c. Type: grep, dash c, INFO, app dot log.", "Only the two error lines. Now count the info lines instead, with dash c. Type: grep, dash c, INFO, app dot log."),
  c('r4', "Three info lines. Now invert the match, with dash v, to see every line that is not info. Type: grep, dash v, INFO, app dot log.", "Three info lines. Now invert the match, with dash v, to see every line that is not info. Type: grep, dash v, INFO, app dot log."),
  c('r5', "Those are the lines that need attention. Next, add line numbers, with dash n. Type: grep, dash n, timeout, app dot log.", "Those are the lines that need attention. Next, add line numbers, with dash n. Type: grep, dash n, timeout, app dot log."),
  c('r6', "Line five. Last, extended patterns, with dash capital E. A bar means or. Type: grep, dash capital E, double quote, WARN, bar, ERROR, double quote, app dot log.", "Line five. Last, extended patterns, with dash capital E. A bar means or. Type: grep, dash capital E, double quote, WARN, bar, ERROR, double quote, app dot log."),
  c('r7', "Warnings and errors together: three lines. One tool, four flags, and you can read any log."),
 ]),
 ('cutsort', [
  c('p1', "Next, cut and sort. Here is a small table of people, with the columns separated by commas. Type: cat users dot C S V.", "Next, cut and sort. Here is a small table of people, with the columns separated by commas. Type: cat users dot C S V."),
  c('p2', "Three columns: name, team and age. The cut command pulls out columns. Dash d sets the separator, and dash f picks the field. Type: cut, dash d, comma, dash f, one, users dot C S V.", "Three columns: name, team and age. The cut command pulls out columns. Dash d sets the separator, and dash f picks the field. Type: cut, dash d, comma, dash f, one, users dot C S V."),
  c('p3', "Just the names. Now sort the whole table by age. Dash t sets the separator, dash k three picks the third column, and dash n sorts as numbers. Type: sort, dash t, comma, dash k, three, dash n, users dot C S V.", "Just the names. Now sort the whole table by age. Dash t sets the separator, dash k three picks the third column, and dash n sorts as numbers. Type: sort, dash t, comma, dash k, three, dash n, users dot C S V."),
  c('p4', "Youngest first, and the header stayed on top, because text counts as zero. Next, count people per team. Cut the team column, sort it, then count the repeats with unique dash c. Type: cut, dash d, comma, dash f, two, users dot C S V, pipe, sort, pipe, unique dash c.", "Youngest first, and the header stayed on top, because text counts as zero. Next, count people per team. Cut the team column, sort it, then count the repeats with unique dash c. Type: cut, dash d, comma, dash f, two, users dot C S V, pipe, sort, pipe, unique dash c."),
  c('p5', "Two in dev, three in ops, and the header counted once. Unique only collapses neighbouring lines, which is why you sort first."),
 ]),
 ('sed', [
  c('s1', "Now sed, the stream editor. Its most common job is search and replace. Here is a small configuration file. Type: cat config dot text.", "Now sed, the stream editor. Its most common job is search and replace. Here is a small configuration file. Type: cat config dot text."),
  c('s2', "Three settings. Change the mode from dev to prod. The s command means substitute: s, slash, old, slash, new, slash. Type: sed, single quote, s slash dev slash prod slash, single quote, config dot text.", "Three settings. Change the mode from dev to prod. The s command means substitute: s, slash, old, slash, new, slash. Type: sed, single quote, s slash dev slash prod slash, single quote, config dot text."),
  c('s3', "The mode shows prod. But did the file change? Check it. Type: cat config dot text.", "The mode shows prod. But did the file change? Check it. Type: cat config dot text."),
  c('s4', "Still dev. The sed command only printed the change, and the file is untouched. To edit the file itself, use dash i. Change the port. Type: sed, dash i, single quote, s slash eight zero eight zero slash nine zero nine zero slash, single quote, config dot text.", "Still dev. The sed command only printed the change, and the file is untouched. To edit the file itself, use dash i. Change the port. Type: sed, dash i, single quote, s slash eight zero eight zero slash nine zero nine zero slash, single quote, config dot text."),
  c('s5', "Silent, and the file has changed. Check it. Type: cat config dot text.", "Silent, and the file has changed. Check it. Type: cat config dot text."),
  c('s6', "The port is now nine zero nine zero. Dash i changes a file for good, so keep a backup first. One more trick: delete matching lines. Type: sed, single quote, slash mode slash d, single quote, config dot text.", "The port is now nine zero nine zero. Dash i changes a file for good, so keep a backup first. One more trick: delete matching lines. Type: sed, single quote, slash mode slash d, single quote, config dot text."),
  c('s7', "The mode line is gone from the output. Again, the file itself is unchanged, because there was no dash i."),
 ]),
 ('awk', [
  c('a1', "Now awk, a small language for columns of text. First, look at the table again. Type: cat users dot C S V.", "Now awk, a small language for columns of text. First, look at the table again. Type: cat users dot C S V."),
  c('a2', "Awk reads each line and splits it into fields. Dollar one is the first field, and dash capital F sets the separator. Type: awk, dash capital F, comma, single quote, open brace, print dollar one, close brace, single quote, users dot C S V.", "Awk reads each line and splits it into fields. Dollar one is the first field, and dash capital F sets the separator. Type: awk, dash capital F, comma, single quote, open brace, print dollar one, close brace, single quote, users dot C S V."),
  c('a3', "The names again, like cut. But awk can also test conditions. Print the people older than thirty. N R is the line number, and N R greater than one skips the header. Type: awk, dash capital F, comma, single quote, N R greater than one, double ampersand, dollar three greater than thirty, open brace, print dollar one, comma, dollar three, close brace, single quote, users dot C S V.", "The names again, like cut. But awk can also test conditions. Print the people older than thirty. N R is the line number, and N R greater than one skips the header. Type: awk, dash capital F, comma, single quote, N R greater than one, double ampersand, dollar three greater than thirty, open brace, print dollar one, comma, dollar three, close brace, single quote, users dot C S V."),
  c('a4', "Three people. Last, a calculation. Add every age to a total, and after the last line, print the average. Type: awk, dash capital F, comma, single quote, N R greater than one, open brace, sum plus equals dollar three, close brace, END, open brace, print sum slash, open round bracket, N R minus one, close round bracket, close brace, single quote, users dot C S V.", "Three people. Last, a calculation. Add every age to a total, and after the last line, print the average. Type: awk, dash capital F, comma, single quote, N R greater than one, open brace, sum plus equals dollar three, close brace, END, open brace, print sum slash, open round bracket, N R minus one, close round bracket, close brace, single quote, users dot C S V."),
  c('a5', "The average age is thirty-three point six. Awk did the maths, with no spreadsheet."),
 ]),
 ('find', [
  c('n1', "Last tool: find. It searches folders for files. Here is a small folder with two subfolders. Type: L S, dash capital R.", "Last tool: find. It searches folders for files. Here is a small folder with two subfolders. Type: L S, dash capital R."),
  c('n2', "Logs in two places. Find every log file below here. The dot means start in the current folder. Type: find, dot, dash name, double quote, star dot log, double quote.", "Logs in two places. Find every log file below here. The dot means start in the current folder. Type: find, dot, dash name, double quote, star dot log, double quote."),
  c('n3', "Three log files. The quotes matter: they stop the shell from expanding the star too early. Now find old files. Dash M time plus seven means modified more than seven days ago. Type: find, dot, dash name, double quote, star dot log, double quote, dash M time, plus seven.", "Three log files. The quotes matter: they stop the shell from expanding the star too early. Now find old files. Dash M time plus seven means modified more than seven days ago. Type: find, dot, dash name, double quote, star dot log, double quote, dash M time, plus seven."),
  c('n4', "Only the old log. Last, run a command on every match, with dash exec. The curly braces stand for each file found. Type: find, dot, dash name, double quote, star dot log, double quote, dash exec, W C, dash l, open brace, close brace, plus.", "Only the old log. Last, run a command on every match, with dash exec. The curly braces stand for each file found. Type: find, dot, dash name, double quote, star dot log, double quote, dash exec, W C, dash l, open brace, close brace, plus."),
  c('n5', "A line count for every log, and a total. Find with dash exec can run any command on thousands of files."),
 ]),
 ('build', [
  c('w1', "Now combine the tools in a small log report. Here is the log again. Type: cat app dot log.", "Now combine the tools in a small log report. Here is the log again. Type: cat app dot log."),
  c('w2', "Which levels appear most? Pull the third field with awk. Sort the words, and count the repeats with unique dash c. Type: awk, single quote, open brace, print dollar three, close brace, single quote, app dot log, pipe, sort, pipe, unique dash c.", "Which levels appear most? Pull the third field with awk. Sort the words, and count the repeats with unique dash c. Type: awk, single quote, open brace, print dollar three, close brace, single quote, app dot log, pipe, sort, pipe, unique dash c."),
  c('w3', "Three info lines, two errors and one warning. Now the details of each error: the time, and the cause. Type: grep, ERROR, app dot log, pipe, awk, single quote, open brace, print dollar two, comma, dollar four, close brace, single quote.", "Three info lines, two errors and one warning. Now the details of each error: the time, and the cause. Type: grep, ERROR, app dot log, pipe, awk, single quote, open brace, print dollar two, comma, dollar four, close brace, single quote."),
  c('w4', "A report with one line per error. Small tools, joined by pipes, do real work."),
  c('w5', "Search. Cut. Replace. Calculate. Find."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: sed changes the file. No. It prints the change. Only dash i edits the file itself."),
  c('my3', "Myth two: grep only searches files. No. It also filters the output of other commands, through a pipe."),
  c('my4', "Myth three: unique removes all duplicates. No. It collapses neighbouring lines only, so sort first."),
  c('my5', "Myth four: find needs a file name. No. It can also filter by type, size and age."),
  c('my6', "Search. Cut. Replace. Calculate. Find."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Search a file with grep, using dash c, dash v and dash n."),
  c('b3', "Cut a column, and sort lines as text and as numbers."),
  c('b4', "Replace text with sed, and know when dash i changes the file."),
  c('b5', "Print fields and calculate a total or an average with awk."),
  c('b6', "Find files by name and by age, and run a command on them."),
  c('b7', "Join the tools with pipes to build a small report."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Type every command yourself."),
  c('z2', "One: write a small log file, and use grep to count, invert and number lines."),
  c('z3', "Two: write a comma separated table, then cut a column and sort it by a number."),
  c('z4', "Three: use sed to replace a word. Then use dash i, but only on a copy of the file."),
  c('z5', "Four: use awk to add up one column, and print the average."),
  c('z6', "Five: find files by name, then by age, and run word count on them."),
  c('z7', "Six: build a pipeline that counts how many times each level appears in your log."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which grep flag inverts the match?"), c('f13', "Why do you sort before unique?"),
  c('f14', "How do you make sed edit the file itself?"), c('f15', "What does N R hold in awk?"),
  c('f16', "Objective covered: MC05-O04.", "Objective covered: M C zero five, objective four, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: pipes, file descriptors, redirection and safe temporary files."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'r7': 0.5, 'p5': 0.5, 's7': 0.5, 'a5': 0.5, 'n5': 0.5, 'w5': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'grep': 'Search with grep', 'cutsort': 'Cut and sort', 'sed': 'Replace with sed', 'awk': 'Calculate with awk', 'find': 'Find files', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Search, reshape, find', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('grep', 'search lines', ACC), ('cut / sort', 'columns and order', VIO), ('sed / awk', 'replace and calculate', WARN), ('find', 'locate files', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Small tools. Big jobs.', 880, C['h3'], GOOD, 1700)); return E
s_grep = _lab('Search with grep', 'Print the lines that match.', 'r1', RB, [('r1', 'cat app.log', 'The log', ACC), ('r2', 'grep ERROR app.log', 'Matching lines', GOOD), ('r3', 'grep -c INFO', 'Count: -c', VIO), ('r4', 'grep -v INFO', 'Invert: -v', WARN), ('r5', 'grep -n timeout', 'Line number: -n', PINK), ('r6', 'grep -E "WARN|ERROR"', 'Either word: -E', BAD)])
s_cutsort = _lab('Cut and sort', 'Pick columns, put lines in order.', 'p1', RB, [('p1', 'cat users.csv', 'name, team, age', ACC), ('p2', 'cut -d, -f1', 'Pick a column', GOOD), ('p3', 'sort -t, -k3 -n', 'Sort by number', VIO), ('p4', '... | sort | uniq -c', 'Count repeats', WARN)])
s_sed = _lab('Replace with sed', 'Search and replace in a stream.', 's1', RB, [('s1', 'cat config.txt', 'Three settings', ACC), ('s2', "sed 's/dev/prod/'", 'Prints the change', GOOD), ('s3', 'cat config.txt', 'File unchanged', VIO), ('s4', "sed -i 's/8080/9090/'", '-i edits the file', WARN), ('s5', 'cat config.txt', 'Now changed', PINK), ('s6', "sed '/mode/d'", 'Delete matching lines', BAD)])
s_awk = _lab('Calculate with awk', 'Fields, conditions, totals.', 'a1', RB, [('a1', 'cat users.csv', 'The table', ACC), ('a2', "awk -F, '{print $1}'", 'Print field one', GOOD), ('a3', 'NR > 1 && $3 > 30', 'Test a condition', VIO), ('a4', 'sum += $3 ... END', 'Average age', WARN)])
s_find = _lab('Find files', 'Search folders by name and age.', 'n1', RB, [('n1', 'ls -R', 'Two subfolders', ACC), ('n2', 'find . -name "*.log"', 'By name', GOOD), ('n3', '-mtime +7', 'Older than 7 days', VIO), ('n4', '-exec wc -l {} +', 'Run on each match', WARN)])
s_build = _lab('Put it together', 'A small log report.', 'w1', RB, [('w1', 'cat app.log', 'The log', ACC), ('w2', 'awk | sort | uniq -c', 'Count the levels', GOOD), ('w3', 'grep ERROR | awk', 'Time and cause', VIO)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: sed edits the file', 'Only -i edits it.', 'my2'), ('Myth: grep reads files only', 'It filters pipes too.', 'my3'), ('Myth: uniq removes all', 'Only neighbours: sort first.', 'my4'), ('Myth: find needs a name', 'Type, size and age work too.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Search. Cut. Replace. Calculate. Find.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('grep: -c -v -n', 'b2'), ('cut and sort', 'b3'), ('sed and -i', 'b4'), ('awk totals', 'b5'), ('find and -exec', 'b6'), ('Join with pipes', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  grep', 'count, invert, number', PINK, 'z2'), ('2  cut, sort', 'column, by number', ACC, 'z3'), ('3  sed', 'replace, then -i on a copy', WARN, 'z4'), ('4  awk', 'sum and average', VIO, 'z5'), ('5  find', 'name, age, wc -l', BAD, 'z6'), ('6  Pipeline', 'count the levels', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which grep flag inverts?', 'f12'), ('Why sort before uniq?', 'f13'), ('How does sed edit a file?', 'f14'), ('What does NR hold in awk?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: pipes and redirection', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'grep': s_grep, 'cutsort': s_cutsort, 'sed': s_sed, 'awk': s_awk, 'find': s_find, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'grep': ('question', ACC), 'cutsort': ('board', VIO), 'sed': ('gear', WARN), 'awk': ('gear', GOOD), 'find': ('question', ACC), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'grep': [('r2', 2, 1, 308, 386, ''), ('r2', 5, 1, 308, 386, ''), ('r3', 1, 2, 4, 690, ''), ('r4', 1, 1, 4, 22, ''), ('r5', 1, 3, 4, 690, ''), ('r6', 1, 1, 4, 40, ''), ('r7', 1, 3, 4, 690, '')],
 'cutsort': [('p2', 1, 6, 4, 65, ''), ('p3', 1, 6, 4, 70, ''), ('p4', 2, 2, 4, 190, ''), ('p5', 1, 3, 4, 150, '')],
 'sed': [('s2', 3, 1, 4, 126, ''), ('s3', 3, 1, 4, 142, ''), ('s4', 3, 1, 4, 126, ''), ('s6', 2, 1, 4, 142, ''), ('s7', 1, 2, 4, 220, '')],
 'awk': [('a2', 1, 1, 4, 200, ''), ('a3', 1, 6, 4, 70, ''), ('a4', 1, 3, 4, 110, ''), ('a5', 2, 1, 4, 60, '')],
 'find': [('n2', 5, 1, 4, 175, ''), ('n2', 8, 1, 4, 80, ''), ('n3', 1, 3, 4, 170, ''), ('n4', 1, 1, 4, 172, ''), ('n5', 1, 4, 4, 210, '')],
 'build': [('w2', 1, 6, 308, 386, ''), ('w3', 1, 3, 4, 205, ''), ('w4', 1, 2, 4, 250, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson40/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
