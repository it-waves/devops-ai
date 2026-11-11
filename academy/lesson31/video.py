import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 31  ·  DEVOPS BOOTCAMP'
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
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 31', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "When you log out, the server keeps working. Something has to start it, watch it, and restart it."),
  c('h2', "On Ubuntu that something is system D. It runs services, keeps their logs, and starts jobs on a schedule."),
  c('h3', "Today you read a service file, check it, read its logs, and schedule a job."),
 ]),
 ('unit', [
  c('u1', "A service is described by a unit file. Read the one for S S H. Type: head -n 14 /usr/lib/systemd/system/ssh.service.", "A service is described by a unit file. Read the one for S S H. Type: head, dash n, fourteen, slash U S R, slash lib, slash system D, slash system, slash S S H dot service."),
  c('u2', "The Unit section describes the service and when it starts. The Service section says how to run it."),
  c('u3', "Exec start is the command that system D runs. The service is that program."),
  c('u4', "Restart equals on-failure means: if it crashes, system D starts it again. That is why services come back by themselves.", "Restart equals on dash failure means: if it crashes, system D starts it again. That is why services come back by themselves."),
 ]),
 ('mine', [
  c('m1', "Now write a unit file of your own. Here is one. Type: cat web.service.", "Now a unit file of your own. Here is one. Type: cat, web dot service."),
  c('m2', "A small web server. The install section says wanted by multi-user target, which means start at normal boot.", "A small web server. The install section says wanted by multi dash user dot target, which means start at normal boot."),
  c('m3', "Check it before you use it. Type: systemd-analyze verify web.service. Grep hides one harmless warning about I P version six from this recording computer.", "Check it before you use it. Type: system D analyze, verify, web dot service. Then grep, dash v, Bind. It hides one harmless warning about I P version six from this recording computer."),
  c('m4', "No output means no problems found."),
  c('m5', "Now a file with mistakes. Type: cat bad.service.", "Now a file with mistakes. Type: cat, bad dot service."),
  c('m6', "Can you spot them? Check it the same way.", "Can you spot them? Check it the same way. Type: system D analyze, verify, bad dot service."),
  c('m7', "Two problems. An unknown key name, because Restart is misspelled. And a command that does not exist. Fix both, and verify again."),
 ]),
 ('control', [
  c('c1', "Now control a service. This needs a running system D machine, such as your virtual machine, so these screens are an illustration."),
  c('c2', "Check status first. Type: systemctl status web. Read two lines.", "Check status first. Type: system control, status, web. Read two lines."),
  c('c3', "Loaded says the file was found, and enabled means it starts at boot."),
  c('c4', "Active says running now. If it says failed, read the log lines under it."),
  c('c5', "Start, stop, restart and reload change the service right now. Use sue do."),
  c('c6', "Enable and disable control boot. Enable does not start it now. Add dash dash now to do both."),
  c('c7', "After you edit a unit file, run: systemctl daemon-reload. Then restart the service.", "After you edit a unit file, run: system control, daemon reload. Then restart the service."),
  c('c8', "Then check status again. Always confirm the change."),
 ]),
 ('journal', [
  c('j1', "When a service fails, read its log. System D keeps logs in the journal, and you read them with journal control."),
  c('j2', "Logs for one service: journalctl -u web. Add dash n to limit the lines.", "Logs for one service: journal control, dash u, web. Add dash n to limit the lines."),
  c('j3', "Read the end first. The last lines usually say why it failed."),
  c('j4', "Add dash f to follow new lines live. Control C stops it."),
  c('j5', "Filter by time with dash dash since, and by severity with dash p err."),
  c('j6', "And dash b shows only the current boot."),
 ]),
 ('boot', [
  c('b1', "How does a server start? It is a chain. Firmware starts the boot loader. The boot loader starts the kernel. The kernel starts system D, process number one."),
  c('b2', "System D then reaches a target, a group of services. A server normally reaches multi-user dot target.", "System D then reaches a target, a group of services. A server normally reaches multi dash user dot target."),
  c('b3', "To see which services slowed the boot, run: systemd-analyze blame. For the boot logs, use journal control dash b.", "To see which services slowed the boot, run: system D analyze blame. For the boot logs, use journal control dash b."),
 ]),
 ('timers', [
  c('t1', "System D can also start jobs on a schedule, with timers. First, check a schedule before you trust it. Type: systemd-analyze calendar.", "System D can also start jobs on a schedule, with timers. First, check a schedule before you trust it. Type: system D analyze, calendar, then the time in quotes."),
  c('t2', "It shows the normal form, and when it will next run. Your date and time zone will differ. Two a m, every day."),
  c('t3', "Weekday mornings. Same command, new schedule.", "Weekday mornings. Same command, new schedule. Monday to Friday at nine."),
  c('t4', "Monday to Friday, at nine. Always read the next run time before you rely on a schedule."),
 ]),
 ('cron', [
  c('k1', "The older tool is cron. One line has five time fields, then the command."),
  c('k2', "Minute thirty, hour two, any day of the month, any month, Monday to Friday. That is two thirty a m on weekdays."),
  c('k3', "Edit your table with: crontab -e. List it with: crontab -l.", "Edit your table with: cron tab, dash e. List it with: cron tab, dash l."),
  c('k4', "Cron runs with a small environment, so use full paths, and test the command by hand first."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: enable starts the service. No. Enable is for boot. Start is for now."),
  c('my3', "Myth two: edit the unit file and it applies. No. Reload system D, then restart."),
  c('my4', "Myth three: restart is the first fix. No. Read the log first, or you lose the clue."),
  c('my5', "Myth four: cron has your normal shell. No. Use full paths."),
  c('my6', "Read first. Then change."),
 ]),
 ('rubric', [
  c('r1', "Here is how you check your own understanding."), c('r2', "Read a unit file, and find the command and the restart rule."),
  c('r3', "Check a unit file with system D analyze verify.", "Check a unit file with system D analyze verify."), c('r4', "Read status, Loaded and Active."),
  c('r5', "Explain start, enable, and daemon reload."), c('r6', "Read a service log with journal control."),
  c('r7', "Write a schedule as a cron line, and check a timer schedule."), c('r8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. Nothing here installs or changes a service."),
  c('z2', "One: read the S S H unit file with head, and find exec start and restart."),
  c('z3', "Two: write your own web dot service in your home folder, and verify it. Then break it on purpose, and verify again.", "Two: write your own web dot service in your home folder, and verify it. Then break it on purpose, and verify again."),
  c('z4', "Three: run system control status S S H, and read Loaded and Active.", "Three: run system control status S S H, and read Loaded and Active."),
  c('z5', "Four: read the last ten lines of its log, with journal control dash u S S H dash n ten.", "Four: read the last ten lines of its log, with journal control, dash u, S S H, dash n, ten."),
  c('z6', "Five: check a timer schedule with system D analyze calendar.", "Five: check a timer schedule with system D analyze calendar."),
  c('z7', "Six: write, on paper, a cron line for two thirty a m on weekdays. Do not install it."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which line in a unit file is the command to run?"), c('f13', "Which command makes system D re-read edited unit files?"),
  c('f14', "Which tool reads service logs?"), c('f15', "Does enable start a service now?"),
  c('f16', "Objective covered: MC04-O06.", "Objective covered: M C zero four, objective six, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: installing and updating packages.", "Next lesson: installing and updating packages."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'u2': 0.4, 'u4': 0.5, 'm2': 0.4, 'm4': 0.6, 'm7': 0.5, 'c1': 0.4, 'c3': 0.5, 'c4': 0.5, 'c6': 0.4, 'c8': 0.5, 'j3': 0.5, 'j6': 0.5, 'b3': 0.6, 't2': 0.5, 't4': 0.5, 'k2': 0.5, 'k4': 0.5, 'my6': 0.5, 'r8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'unit': 'Read a unit file', 'mine': 'Write and check a unit', 'control': 'Control a service', 'journal': 'Read the journal', 'boot': 'How a server boots', 'timers': 'Timers', 'cron': 'Cron', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))

def s_hook(C, D, dur):
    E = [El(T('Services run without you.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Service', 'a program that runs in the background', ACC), ('Journal', 'the log of what it said', VIO), ('Schedule', 'a job that starts by the clock', WARN)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('Run. Read. Schedule.', 850, C['h3'], GOOD, 1600)); return E
s_unit = _lab('Read a unit file', 'The recipe that system D follows.', 'u1', RB, [('u1', 'ssh.service', 'A real unit file', ACC), ('u3', 'ExecStart=', 'The command to run', VIO), ('u4', 'Restart=', 'Come back after a crash', GOOD)])
s_mine = _lab('Write and check a unit', 'Verify before you use it.', 'm1', RB, [('m1', 'web.service', 'Your own unit file', ACC), ('m3', 'analyze verify', 'Silence means pass', GOOD), ('m6', 'bad.service', 'Find the mistakes', BAD), ('m7', 'fix, verify again', 'Until it is silent', WARN)])
s_timers = _lab('Timers', 'Check a schedule before you trust it.', 't1', RB, [('t1', 'analyze calendar', 'Check a schedule', ACC), ('t2', 'Next elapse', 'When it will run', WARN), ('t3', 'Mon..Fri 09:00', 'Weekday mornings', VIO)])
def s_control(C, D, dur):
    E = head('Control a service', 'Status, start, stop and enable.', C['c1']); E.append(ill(C['c1'] + 0.2, 1260, 286))
    rows = [('$ systemctl status web', GOOD), ('● web.service - Demo web server', TXT), ('     Loaded: loaded (/etc/systemd/system/web.service; enabled)', TXT), ('     Active: active (running) since Wed 09:00:01 EST; 2h ago', TXT), ('   Main PID: 1234 (python3)', TXT), ('      Tasks: 1', TXT)]
    mono_panel(E, 100, 345, 1060, rows, C['c2'])
    hbar(E, 112, 345 + 24 + 2 * 40 - 4, 1030, 38, C['c3'], C['c3'] + dur['c3'] + 0.5, GOOD)
    hbar(E, 112, 345 + 24 + 3 * 40 - 4, 1030, 38, C['c4'], C['c4'] + dur['c4'] + 0.5, WARN)
    E.append(Pop(card(560, 150, ACC, 'Right now', [('start  stop  restart  reload', TXT)], 36, 30), 1260, 345, C['c5']))
    E.append(Pop(card(560, 150, VIO, 'At boot', [('enable  disable  (--now: both)', TXT)], 36, 30), 1260, 525, C['c6']))
    E.append(Pop(card(560, 150, GOOD, 'After editing a unit', [('daemon-reload, then restart', TXT)], 36, 30), 1260, 705, C['c7']))
    E.append(takeaway('Change. Then check status.', 920, C['c8'], GOOD, 1400)); return E
def s_journal(C, D, dur):
    E = head('Read the journal', 'journalctl keeps the log of every service.', C['j1']); E.append(ill(C['j1'] + 0.2, 1260, 286))
    rows = [('$ journalctl -u web -n 5', GOOD), ('Nov 11 09:14:20 lab systemd[1]: Started web.service.', TXT), ('Nov 11 09:14:21 lab python3[1234]: OSError: Address in use', TXT), ('Nov 11 09:14:21 lab systemd[1]: web.service: Failed.', TXT), ('Nov 11 09:14:26 lab systemd[1]: web.service: Scheduled restart.', TXT), ('Nov 11 09:14:26 lab systemd[1]: Started web.service.', TXT)]
    mono_panel(E, 100, 345, 1060, rows, C['j2'])
    hbar(E, 112, 345 + 24 + 2 * 40 - 4, 1030, 38, C['j3'], C['j3'] + dur['j3'] + 0.5, WARN)
    E.append(Pop(card(560, 120, ACC, '-u web  -n 20', [('One service, last lines', TXT)], 34, 28), 1260, 345, C['j2']))
    E.append(Pop(card(560, 120, VIO, '-f', [('Follow live. Ctrl+C stops', TXT)], 34, 28), 1260, 490, C['j4']))
    E.append(Pop(card(560, 120, WARN, '--since   -p err', [('Time and severity', TXT)], 34, 28), 1260, 635, C['j5']))
    E.append(Pop(card(560, 120, GOOD, '-b', [('Current boot only', TXT)], 34, 28), 1260, 780, C['j6']))
    E.append(takeaway('Read the end first.', 920, C['j3'] + 1.0, GOOD, 1000)); return E
def s_boot(C, D, dur):
    E = head('How a server boots', 'A chain, ending in system D.', C['b1'])
    it = [('Firmware', 'UEFI', MUTED), ('Boot loader', 'GRUB', VIO), ('Kernel', 'Linux', ACC), ('systemd', 'PID 1', WARN), ('Target', 'multi-user', GOOD)]
    for i, (a, b, col) in enumerate(it):
        x = 100 + i * 360
        E.append(Pop(card(300, 190, col, a, [(b, TXT)], 38, 32), x, 360, C['b1'] + 0.2 + i * 1.5 if i < 4 else C['b2']))
        if i < 4: E.append(El(T('›', 'x', 70, TXT), x + 318, 410, C['b1'] + 0.7 + i * 1.5 if i < 3 else C['b2'] - 0.3, anim='fade'))
    E.append(Pop(card(820, 150, ACC, 'systemd-analyze blame', [('Which services slowed the boot', TXT)], 38, 30), 100, 650, C['b3']))
    E.append(Pop(card(820, 150, VIO, 'journalctl -b', [('Logs of this boot only', TXT)], 38, 30), 980, 650, C['b3'] + 3.5))
    return E
def s_cron(C, D, dur):
    E = head('Cron', 'The older scheduler: five fields, then the command.', C['k1']); E.append(ill(C['k1'] + 0.2, 1260, 286))
    it = [('30', 'minute', ACC), ('2', 'hour', VIO), ('*', 'day of month', GOOD), ('*', 'month', WARN), ('1-5', 'day of week', PINK)]
    for i, (v, n, col) in enumerate(it): E.append(Pop(card(310, 180, col, v, [(n, TXT)], 64, 30), 100 + i * 340, 340, C['k1'] + 0.6 + i * 0.4 if i else C['k1'] + 0.6))
    E.append(Pop(card(1640, 110, TXT if False else ACC, '', [('/home/student/backup.sh', TXT)], 4, 40), 100, 560, C['k1'] + 3.0))
    E.append(Pop(badge('30 2 * * 1-5   =   02:30, Monday to Friday', F('b', 40), INK, GOOD, padx=30, pady=16), 100, 720, C['k2'] + 1.5))
    E.append(Pop(card(520, 110, VIO, 'crontab -e', [('Edit your table', TXT)], 34, 28), 100, 850, C['k3']))
    E.append(Pop(card(520, 110, VIO, 'crontab -l', [('List your table', TXT)], 34, 28), 660, 850, C['k3'] + 2.5))
    E.append(Pop(card(520, 110, WARN, 'Full paths', [('Small environment', TXT)], 34, 28), 1220, 850, C['k4'])); return E
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: enable starts it now', 'Enable is for boot.', 'my2'), ('Myth: edits apply at once', 'Reload, then restart.', 'my3'), ('Myth: restart first', 'Read the log first.', 'my4'), ('Myth: cron = my shell', 'Use full paths.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Read first. Then change.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['r1'])
    items = [('Read ExecStart and Restart', 'r2'), ('Verify a unit file', 'r3'), ('Read Loaded and Active', 'r4'), ('Start, enable, reload', 'r5'), ('Read a service log', 'r6'), ('Cron line, timer check', 'r7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['r8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine. Nothing is installed.', C['z1'])
    it = [('1  Read', 'head the ssh unit', PINK, 'z2'), ('2  Write', 'web.service, verify', ACC, 'z3'), ('3  Status', 'systemctl status ssh', WARN, 'z4'), ('4  Journal', 'journalctl -u ssh -n 10', VIO, 'z5'), ('5  Timer', 'analyze calendar', GOOD, 'z6'), ('6  Cron', 'write a line on paper', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which line is the command to run?', 'f12'), ('Which command re-reads edited units?', 'f13'), ('Which tool reads service logs?', 'f14'), ('Does enable start it now?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O06', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: install and update packages', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, unit=s_unit, mine=s_mine, control=s_control, journal=s_journal, boot=s_boot, timers=s_timers, cron=s_cron, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(unit=('eye', GOOD), mine=('eye', GOOD), timers=('eye', GOOD), control=('gear', ACC), journal=('eye', VIO), boot=('gear', WARN), cron=('gear', VIO), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'unit': [('u3', 10, 1, 4, 574, ''), ('u4', 14, 1, 4, 274, '')],
 'mine': [('m2', 9, 1, 4, 379, ''), ('m7', 1, 2, 4, 1068, ''), ('m7', 3, 2, 4, 1068, '')],
 'timers': [('t2', 3, 1, 4, 664, ''), ('t4', 3, 1, 4, 664, '')],
}
