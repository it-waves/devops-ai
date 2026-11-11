import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 36  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'ufw': 'U F W', 'sshd': 'S S H D', 'ed25519': 'E D two five five one nine', 'eth0': 'eth zero', 'MC04-O10': 'M C zero four, objective ten', 'lab36': 'lab thirty-six', 'github': 'git hub', 'MC05': 'M C zero five', 'MC04-O09': 'M C zero four, objective nine', 'chmod': 'C H mod', 'sed': 'sed', 'nc': 'N C', 'diff': 'diff', 'tmp': 'temp', 'http': 'H T T P', 'systemd-analyze': 'system D analyze', 'tcp': 'T C P', 'du': 'D U', 'df': 'D F', 'loopback': 'loop back', 'ping': 'ping', 'ss': 'S S', 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 36', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "Mastery evidence. You have learned the Linux administration toolkit. Now you prove it."),
  c('h2', "Mastery means someone else could check your work. So this lesson gives you a lab, a checker that says pass or fail, and a report that shows how you thought."),
  c('h3', "I will build the lab, fix the first fault live, and leave the other three to you."),
 ]),
 ('scenario', [
  c('sc1', "Meet the tidy shop server. It has a report script, a data disk, a web service, and a firewall."),
  c('sc2', "Four things are broken, on purpose. A checker prints pass or fail for four checks."),
  c('sc3', "One: the report script runs."),
  c('sc4', "Two: the data disk accepts a write."),
  c('sc5', "Three: the service file verifies clean."),
  c('sc6', "Four: the shop page answers on port 8080.", "Four: the shop page answers on port eighty eighty."),
  c('sc7', "Your mission: four pass lines, with proof for every fix."),
 ]),
 ('getlab', [
  c('g1', "Before we start, here is where everything lives. It is also in the description."),
  c('g2', "The repository is github dot com, slash it dash waves, slash devops dash A I.", "The repository is git hub dot com, slash it dash waves, slash dev ops dash A I."),
  c('g3', "The lab is one file: lab36.sh, in the academy slash lab folder. Your report template and install notes are in academy slash lesson36.", "The lab is one file: lab thirty-six dot S H, in the academy slash lab folder. Your report template and install notes are in academy slash lesson thirty-six."),
  c('g4', "Install it in three steps. Clone the repository. Go to the lab folder. Install the script into slash usr slash local slash sbin.", "Install it in three steps. Clone the repository. Go to the lab folder. Install the script into slash U S R slash local slash S bin."),
  c('g5', "Three commands run everything. Lab up builds the problems. Lab check prints pass or fail for each. Lab down removes it all.", "Three commands run everything. Lab up builds the problems. Lab check prints pass or fail for each. Lab down removes it all."),
  c('g6', "Lab is a short name. Source the shortcuts file, and it runs sudo lab36.sh for you.", "Lab is a short name. Source the shortcuts file, and it runs sue do, lab thirty-six dot S H, for you."),
  c('g7', "You need an Ubuntu virtual machine with root, python three, iptables, curl, and system D analyze. Run it only in your own machine.", "You need an Ubuntu virtual machine with root, python three, I P tables, curl, and system D analyze. Run it only in your own machine."),
 ]),
 ('start', [
  c('st1', "Now for real. I have cloned the repository, and the lab files are in a folder called lab. Type: cd lab.", "Now for real. I have cloned the repository, and the lab files are in a folder called lab. Type: C D, lab."),
  c('st2', "List what is here. Type: ls.", "List what is here. Type: L S."),
  c('st3', "The lab script and the shortcuts file. Install the script. Type: sudo install -m 755 lab36.sh /usr/local/sbin/. Dash m seven five five makes it executable.", "The lab script and the shortcuts file. Install the script. Type: sue do, install, dash m, seven five five, lab thirty-six dot S H, slash U S R, slash local, slash S bin, slash. Dash m seven five five makes it executable."),
  c('st4', "Load the short names. Type: source shortcuts36.sh.", "Load the short names. Type: source, shortcuts thirty-six dot S H."),
  c('st5', "Build the lab. Type: lab up. It takes a few seconds, because it builds a small disk.", None),
  c('st6', "Now ask the checker. Type: lab check.", None),
  c('st7', "Four FAIL lines. That is your starting point. Copy them into your report."),
 ]),
 ('notes', [
  c('n1', "Keep four notes for every fault."),
  c('n2', "One: the symptom, in the exact words of the error."),
  c('n3', "Two: the cause, and the command that proved it."),
  c('n4', "Three: the fix. One change only."),
  c('n5', "Four: the proof, the output after the fix."),
  c('n6', "Notes turn a lucky fix into evidence."),
 ]),
 ('fix1', [
  c('f1', "Fault one, live. The checker says the report script does not run. Run it the way the checker does. Type the full path: /opt/lab36/bin/report.sh.", "Fault one, live. The checker says the report script does not run. Run it the way the checker does. Type the full path: slash opt, slash lab thirty-six, slash bin, slash report dot S H."),
  c('f2', "Note one, the symptom: permission denied. Now check, do not guess. Type: ls -l /opt/lab36/bin.", "Note one, the symptom: permission denied. Now check, do not guess. Type: L S, dash l, slash opt, slash lab thirty-six, slash bin."),
  c('f3', "Note two, the cause. The mode has no x anywhere, so nobody may execute the file. This listing is the proof."),
  c('f4', "Note three, one change. Type: chmod u+x and the same path.", "Note three, one change. Type: C H mod, u plus x, and the same path."),
  c('f5', "Note four, the proof. Run the script again.", None),
  c('f6', "It runs. Now ask the checker. Type: lab check.", None),
  c('f7', "One PASS, three FAIL. One fault down, one change, with proof. Now it is your turn for the other three."),
 ]),
 ('report', [
  c('r1', "Your report has five parts. The template is in the lesson folder."),
  c('r2', "Setup: the checker output at the start."),
  c('r3', "Each fault, with its four notes."),
  c('r4', "The final checker output, all four lines saying pass."),
  c('r5', "Where you got stuck, and what unstuck you. Honest notes are worth more than a perfect story."),
  c('r6', "And the cleanup proof, which we do next."),
 ]),
 ('hints', [
  c('y1', "Your three faults. No spoilers, only directions."),
  c('y2', "Check two says the data disk will not accept a write. Read the exact error. Then recall how you measure space, and what is using it."),
  c('y3', "Check three says the service file does not verify. System D analyze will tell you in plain words what is wrong."),
  c('y4', "Check four says the page does not answer. Is anything listening on 8080? If yes, ask what stands in the way. Look at the firewall rules."),
  c('y5', "Same method every time. Symptom, check, fix one thing, verify."),
 ]),
 ('cleanup', [
  c('c1', "When you finish, clean up, and prove it. Type: lab down.", None),
  c('c2', "Proof one: is any lab disk still mounted? Type: mount, pipe, grep dash c lab36, to count the matches.", "Proof one: is any lab disk still mounted? Type: mount, pipe, grep dash c lab thirty-six, to count the matches."),
  c('c3', "Zero. Proof two: is the web server gone? Type: pgrep -fc and the pattern, in quotes.", "Zero. Proof two: is the web server gone? Type: P grep, dash f c, and the pattern, in quotes."),
  c('c4', "Zero. Proof three: is the firewall rule gone? Type: sudo iptables -S, pipe, grep dash c 8080.", "Zero. Proof three: is the firewall rule gone? Type: sue do, I P tables, dash capital S, pipe, grep dash c, eighty eighty."),
  c('c5', "Zero. Proof four: is the folder gone? Type: ls /opt/lab36.", "Zero. Proof four: is the folder gone? Type: L S, slash opt, slash lab thirty-six."),
  c('c6', "No such file or directory. Everything is removed. Paste these four proofs into your report."),
 ]),
 ('rubric', [
  c('b1', "Here is how your work is judged. Six points, and you need all six."),
  c('b2', "The checker shows four pass lines."), c('b3', "Every fault has a symptom, a cause, a fix, and a proof."),
  c('b4', "You changed one thing at a time."), c('b5', "The report is complete, including where you got stuck."),
  c('b6', "The cleanup proof shows nothing left behind."), c('b7', "You ran it only in your own virtual machine."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Take your time. Mastery is slow and exact."),
  c('z2', "One: clone the repository and install the lab."),
  c('z3', "Two: run lab up, and save the checker output."),
  c('z4', "Three: fix the three remaining faults, with four notes each."),
  c('z5', "Four: write the report from the template."),
  c('z6', "Five: run the checker. All four lines must say pass."),
  c('z7', "Six: clean up, and paste the proof."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which command counts what is still mounted?"), c('f13', "What are the four notes for a fault?"),
  c('f14', "How many changes do you make before you verify?"), c('f15', "What proves your cleanup worked?"),
  c('f16', "Mastery evidence covered: M C zero four, building on objectives one to ten.", "Mastery evidence covered: M C zero four, building on objectives one to ten, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next masterclass: Bash scripting."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'sc7': 0.5, 'g7': 0.8, 'st5': 4.0, 'st6': 1.0, 'st7': 0.5, 'n6': 0.5, 'f3': 0.4, 'f7': 0.5, 'r6': 0.4, 'y5': 0.5, 'c1': 2.0, 'c6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'scenario': 'The scenario', 'getlab': 'Get the lab', 'start': 'Start the lab', 'notes': 'Four notes per fault', 'fix1': 'Fault 1 live', 'report': 'The report', 'hints': 'Your three faults', 'cleanup': 'Cleanup with proof', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))


def s_hook(C, D, dur):
    E = [El(T('Mastery evidence', 'x', 72), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('A lab', 'four faults, injected for you', ACC), ('A checker', 'PASS or FAIL for each', GOOD), ('A report', 'proof of how you thought', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 3.0))
    E.append(takeaway('Prove it. Someone else can check it.', 850, C['h3'], GOOD, 1700)); return E
def s_scenario(C, D, dur):
    E = head('The scenario', 'The tidy shop server. Four things are broken.', C['sc1']); E.append(ill(C['sc1'] + 0.2, 1400, 170))
    it = [('1  report script runs', 'sc3', ACC), ('2  data disk accepts a write', 'sc4', VIO), ('3  service file verifies clean', 'sc5', WARN), ('4  shop page answers on 8080', 'sc6', PINK)]
    for i, (n, cid, col) in enumerate(it):
        E.append(Pop(card(1100, 120, col, '', [], 4), 100, 330 + i * 140, C[cid])); E.append(El(T('FAIL', 'mono', 34, BAD, align='left'), 140, 372 + i * 140, C[cid] + 0.2, anim='fade')); E.append(El(T(n, 'b', 36, TXT, maxw=900), 280, 370 + i * 140, C[cid] + 0.3, anim='fade'))
    E.append(takeaway('Goal: four PASS lines, with proof.', 920, C['sc7'], GOOD, 1500)); return E
def s_getlab(C, D, dur):
    E = head('Get the lab', 'Everything you need, in one place.', C['g1']); E.append(ill(C['g1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 'g2', ACC), ('Lab file', 'academy/lab/lab36.sh', 'g3', VIO), ('Lesson files', 'academy/lesson36: INSTALL.txt, report_template.md', 'g3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 'g4'), ('cd devops-ai/academy/lab', 'g4'), ('sudo install -m 755 lab36.sh /usr/local/sbin/', 'g4'), ('source shortcuts36.sh', 'g6'), ('lab up  |  lab check  |  lab down', 'g5')]
    E.append(Pop(glass(1700, 5 * 46 + 48, WARN), 100, 700, C['g4']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, root, python3, iptables, curl, systemd-analyze. Your own machine only.', 'm', 26, MUTED, maxw=1700), 100, 990, C['g7'], anim='fade')); return E
s_start = _lab('Start the lab', 'Install it, build it, check it.', 'st1', RB, [('st1', 'cd lab', 'The lab folder', ACC), ('st3', 'sudo install', 'Install the script', VIO), ('st4', 'source', 'Short name: lab', WARN), ('st5', 'lab up', 'Build the faults', BAD), ('st6', 'lab check', 'Four FAIL lines', GOOD)])
def s_notes(C, D, dur):
    E = head('Four notes per fault', 'Evidence, not luck.', C['n1'])
    it = [('1  Symptom', 'the exact words', BAD, 'n2'), ('2  Cause', 'and the proving command', ACC, 'n3'), ('3  Fix', 'one change only', WARN, 'n4'), ('4  Proof', 'output after the fix', GOOD, 'n5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s_, TXT)], 44, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Notes turn a lucky fix into evidence.', 800, C['n6'], GOOD, 1700)); return E
s_fix1 = _lab('Fault 1 live', 'Permission denied, fixed with proof.', 'f1', RB, [('f1', 'run the script', 'Symptom: denied', BAD), ('f2', 'ls -l', 'Check the mode', ACC), ('f4', 'chmod u+x', 'One change', WARN), ('f5', 'run again', 'Proof', GOOD), ('f6', 'lab check', 'One PASS', VIO)])
def s_report(C, D, dur):
    E = head('The report', 'Five parts. Template in academy/lesson36.', C['r1']); E.append(ill(C['r1'] + 0.2, 1400, 170))
    it = [('Setup', 'checker output at the start', ACC, 'r2'), ('Each fault', 'its four notes', VIO, 'r3'), ('Final check', 'four PASS lines', GOOD, 'r4'), ('Where I got stuck', 'and what unstuck me', WARN, 'r5'), ('Cleanup proof', 'four proofs', PINK, 'r6')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s_, TXT)], 40, 30, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    return E
def s_hints(C, D, dur):
    E = head('Your three faults', 'Directions only. No spoilers.', C['y1'])
    it = [('Check 2', 'read the exact error. df? du?', VIO, 'y2'), ('Check 3', 'systemd-analyze verify says it in words', WARN, 'y3'), ('Check 4', 'listening? then what is in the way?', PINK, 'y4')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1500, 150, col, n, [(s_, TXT)], 44, 32), 100, 330 + i * 175, C[cid]))
    E.append(takeaway('Symptom. Check. Fix one thing. Verify.', 900, C['y5'], GOOD, 1700)); return E
s_cleanup = _lab('Cleanup with proof', 'Nothing left behind.', 'c1', RB, [('c1', 'lab down', 'Remove the lab', ACC), ('c2', 'mount | grep -c', 'No lab disk', VIO), ('c3', 'pgrep -fc', 'No server', WARN), ('c4', 'iptables -S', 'No rule', PINK), ('c5', 'ls /opt/lab36', 'No folder', GOOD)])
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Four PASS lines', 'b2'), ('Four notes per fault', 'b3'), ('One change at a time', 'b4'), ('Complete report', 'b5'), ('Cleanup proof', 'b6'), ('Own VM only', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'clone and install the lab', PINK, 'z2'), ('2  Start', 'lab up, save the output', ACC, 'z3'), ('3  Fix', 'three faults, four notes', WARN, 'z4'), ('4  Report', 'from the template', VIO, 'z5'), ('5  Check', 'four PASS lines', BAD, 'z6'), ('6  Clean up', 'and paste the proof', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What counts what is still mounted?', 'f12'), ('What are the four notes per fault?', 'f13'), ('Changes before you verify?', 'f14'), ('What proves cleanup worked?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Mastery evidence: MC04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next masterclass: Bash scripting', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, scenario=s_scenario, getlab=s_getlab, start=s_start, notes=s_notes, fix1=s_fix1, report=s_report, hints=s_hints, cleanup=s_cleanup, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(scenario=('board', ACC), getlab=('gear', VIO), start=('gear', ACC), notes=('board', WARN), fix1=('test', GOOD), report=('board', VIO), hints=('question', WARN), cleanup=('eye', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'start': [('st7', 1, 4, 4, 78, '')],
 'fix1': [('f2', 1, 1, 450, 720, ''), ('f3', 2, 1, 4, 160, ''), ('f6', 1, 1, 4, 250, ''), ('f7', 1, 1, 4, 72, '')],
 'cleanup': [('c2', 1, 1, 4, 190, ''), ('c3', 1, 1, 4, 30, ''), ('c4', 1, 1, 4, 30, ''), ('c5', 1, 1, 4, 30, ''), ('c6', 1, 1, 480, 885, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson36/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
