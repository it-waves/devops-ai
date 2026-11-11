import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 35  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps

_ON = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_TN = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def _w99(n): return _ON[n] if n < 20 else _TN[n // 10] + ('' if n % 10 == 0 else '-' + _ON[n % 10])
def _wip(n):
    if n < 100: return _w99(n)
    h, r = divmod(n, 100)
    return _ON[h] + (' hundred' if r == 0 else ' oh ' + _ON[r] if r < 10 else ' ' + _w99(r))
_SP = { 'ufw': 'U F W', 'sshd': 'S S H D', 'ed25519': 'E D two five five one nine', 'eth0': 'eth zero', 'MC04-O10': 'M C zero four, objective ten', 'MC04-O09': 'M C zero four, objective nine', 'chmod': 'C H mod', 'sed': 'sed', 'nc': 'N C', 'diff': 'diff', 'tmp': 'temp', 'http': 'H T T P', 'systemd-analyze': 'system D analyze', 'tcp': 'T C P', 'du': 'D U', 'df': 'D F', 'loopback': 'loop back', 'ping': 'ping', 'ss': 'S S', 'lsblk': 'L S B L K', 'du': 'D U', 'mkfs': 'M K F S', 'ext4': 'E X T four', 'blkid': 'block I D', 'fallocate': 'F allocate', 'truncate': 'truncate', 'resize2fs': 'resize two F S', 'e2fsck': 'E two F S C K', 'fstab': 'F S tab', 'UUID': 'U U I D', 'umount': 'U mount', 'MC04-O08': 'M C zero four, objective eight', 'sda': 'S D A', 'nvme': 'N V M E', 'xfs': 'X F S', 'nofail': 'no fail', 'findmnt': 'find mount', 'mnt': 'M N T','TCP': 'T C P', 'UDP': 'U D P', 'DNS': 'D N S', 'TLS': 'T L S', 'HTTP': 'H T T P', 'HTTPS': 'H T T P S', 'IP': 'I P', 'CA': 'C A', 'openssl': 'open S S L', 'ICMP': 'I C M P',
       'ss': 's s', 'sv': 'S V', 'rt': 'R T', 'nc': 'n c', 'curl': 'curl', 'dig': 'dig', 'iptables': 'I P tables', 'sysctl': 'sys control', 'traceroute': 'trace route', 'ip': 'I P',
       'startweb': 'start web', 'localhost': 'local host', 'pwd': 'P W D', 'ls': 'L S', 'cd': 'C D', 'man': 'man', 'apropos': 'apropos', 'whatis': 'what is', 'etc': 'E T C', 'var': 'var', 'usr': 'U S R', 'proc': 'proc', 'tmp': 'temp', 'bin': 'bin', 'sbin': 'S bin', 'MC04-O02': 'M C zero four, objective two', 'MC04-O05': 'M C zero four, objective five', 'ps': 'P S', 'pid': 'P I D', 'PID': 'P I D', 'pgrep': 'P grep', 'pkill': 'P kill', 'uptime': 'up time', 'nproc': 'N proc', 'SIGTERM': 'sig term', 'SIGKILL': 'sig kill', 'SIGINT': 'sig int', 'SIGHUP': 'sig hup', 'CPU': 'C P U', 'RAM': 'ram', 'df': 'D F', 'sshd': 'S S H D', 'systemctl': 'system control', 'systemd': 'system D', 'pcpu': 'P C P U', 'mkdir': 'make dir', 'cat': 'cat', 'wc': 'W C', 'cp': 'C P', 'mv': 'M V', 'rm': 'R M', 'rmdir': 'R M dir', 'vim': 'vim', 'tail': 'tail', 'touch': 'touch', 'cl': 'C L', 'wc': 'W C', 'pgrep': 'P grep', 'ip_forward': 'I P underscore forward', 'MC04-O06': 'M C zero four, objective six', 'journalctl': 'journal control', 'crontab': 'cron tab', 'systemd-analyze': 'system D analyze', 'journald': 'journal D', 'cron': 'cron', 'ssh': 'S S H', 'sudo': 'sue do', 'daemon-reload': 'daemon reload', 'MC04-O07': 'M C zero four, objective seven', 'apt': 'apt', 'dpkg': 'D P K G', 'apt-get': 'apt get', 'apt-cache': 'apt cache', 'PPA': 'P P A', 'URI': 'U R I', 'URIs': 'U R Is', 'MC03': 'M C zero three', 'MC04': 'M C zero four', 'PEM': 'P E M', 'RTT': 'R T T', 'ping': 'ping', 'cert': 'cert', 'SAN': 'S A N'}
def _say(cap):
    s = re.sub(r'\b(\d{1,3}(?:\.\d{1,3}){3})(?:/(\d{1,2}))?\b', lambda m: ' dot '.join(_wip(int(x)) for x in m.group(1).split('.')) + (' slash ' + _w99(int(m.group(2))) if m.group(2) else ''), cap)
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in sorted(_SP, key=len, reverse=True)) + r')(?![\w-])', lambda m: _SP[m.group(1)], s)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

def head(title, sub, t): return [El(T('Linux administration  ·  Lesson 35', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
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
  c('h1', "Things break. What separates a beginner from an administrator is not never breaking anything. It is finding the cause, and fixing it calmly."),
  c('h2', "Today you learn a four step method. Then you use it on four faults: a script that will not run, a disk that is full, a service nobody is listening to, and a broken service file."),
  c('h3', "Every fault is a real recording on Ubuntu, broken on purpose, so you can watch the method work."),
 ]),
 ('method', [
  c('m1', "Here is the method. It has four steps."),
  c('m2', "One: read the symptom. What exactly failed, and what did the error say? Copy the words. Do not guess."),
  c('m3', "Two: check. Ask the system what is true, with a command, before you change anything."),
  c('m4', "Three: fix one thing. Make the smallest change, and keep a backup of any file you edit."),
  c('m5', "Four: verify. Run the original action again. If it works, you are done. If not, you have a new error, so go back to step one."),
  c('m6', "Slow is smooth. Change five things at once, and you never learn which one worked."),
 ]),
 ('perms', [
  c('p1', "Fault one. A script will not run. Type: ./backup.sh.", "Fault one. A script will not run. Type: dot slash backup dot S H."),
  c('p2', "Read the symptom: permission denied. The file is there, but the system will not let us run it. So check the permissions. Type: ls -l backup.sh.", "Read the symptom: permission denied. The file is there, but the system will not let us run it. So check the permissions. Type: L S, dash l, backup dot S H."),
  c('p3', "The mode is dash r w, dash r, dash dash, r, dash dash. Nobody has an x, so nobody may execute it. We own the file, so we can change it."),
  c('p4', "Fix one thing. Add the execute bit for the owner. Type: chmod u+x backup.sh. U is the user, and plus x adds execute.", "Fix one thing. Add the execute bit for the owner. Type: C H mod, u plus x, backup dot S H. U is the user, and plus x adds execute."),
  c('p5', "Verify. Run the original command again. Type: ./backup.sh.", "Verify. Run the original command again. Type: dot slash backup dot S H."),
  c('p6', "It runs. Fixed with one change. Not chmod seven seven seven, which would give everyone everything."),
 ]),
 ('disk', [
  c('d1', "Fault two. You try to save a file, and it fails. Type: echo hello > mnt/new.txt.", "Fault two. You try to save a file, and it fails. Type: echo hello, greater than sign, mnt slash new dot text."),
  c('d2', "No space left on device. Check, do not guess. Type: df -h mnt. D F shows how full a filesystem is.", "No space left on device. Check, do not guess. Type: D F, dash h, mnt. D F shows how full a filesystem is."),
  c('d3', "Use is one hundred percent. Next question: what is using it? Type: du -ah mnt, then a pipe to sort -rh, then head -n 3. That lists the three biggest items.", "Use is one hundred percent. Next question: what is using it? Type: D U, dash a h, mnt, then a pipe to sort, dash r h, then head, dash n, three. That lists the three biggest items."),
  c('d4', "Two lines show eighty-eight megabytes: the folder total, and old dump dot log. The file is the culprit. Check it is safe to remove. Then delete only that file. Type: rm mnt/old-dump.log.", "Two lines show eighty-eight megabytes: the folder total, and old dump dot log. The file is the culprit. Check it is safe to remove. Then delete only that file. Type: R M, mnt slash old dash dump dot log."),
  c('d5', "Verify. Try the original action again. Type: echo hello > mnt/new.txt, and, and, echo saved.", "Verify. Try the original action again. Type: echo hello, greater than sign, mnt slash new dot text, and, and, echo saved."),
  c('d6', "Saved. Confirm with D F. Type: df -h mnt.", "Saved. Confirm with D F. Type: D F, dash h, mnt."),
  c('d7', "The space is back. D F says how full. D U says what is using it. Use both."),
 ]),
 ('net', [
  c('t1', "Fault three. A web server on port 8080 is not answering. Test the port. Type: nc -zv 127.0.0.1 8080. Z means just test, and v means tell me.", "Fault three. A web server on port eighty eighty is not answering. Test the port. Type: N C, dash z v, one twenty-seven dot zero dot zero dot one, eighty eighty. Z means just test, and v means tell me."),
  c('t2', "Connection refused. That is a precise clue: the machine answered, but no program is listening on that port. A silent hang would point at a firewall instead. Double check. Type: ss -tln | grep 8080.", "Connection refused. That is a precise clue: the machine answered, but no program is listening on that port. A silent hang would point at a firewall instead. Double check. Type: S S, dash t l n, pipe, grep, eighty eighty."),
  c('t3', "Nothing printed. Nothing is listening on port 8080. So the fault is the service, not the network."),
  c('t4', "Fix one thing: start the service. For this demo it is Python's built in web server. Type: python3 -m http.server 8080 &>/dev/null &. The last ampersand runs it in the background.", "Fix one thing: start the service. For this demo it is Python's built in web server. Type: python three, dash m, H T T P dot server, eighty eighty, and then send the output to dev null, with an ampersand at the end. The ampersand runs it in the background."),
  c('t5', "The number in brackets is the job. The second number is the process I D. Verify. Type: nc -zv 127.0.0.1 8080.", "The number in brackets is the job. The second number is the process I D. Verify. Type: N C, dash z v, one twenty-seven dot zero dot zero dot one, eighty eighty."),
  c('t6', "Succeeded. Now the port answers. See who is listening. Type: ss -tln | grep 8080.", "Succeeded. Now the port answers. See who is listening. Type: S S, dash t l n, pipe, grep, eighty eighty."),
  c('t7', "A listener on port 8080. Refused means nothing listens. Timed out means something blocks the way. Read the difference, and you know where to look."),
 ]),
 ('svc', [
  c('s1', "Fault four. A service will not start. On a live system you would run systemctl status and read the journal. Here we check the unit file itself. Type: cat web.service.", "Fault four. A service will not start. On a live system you would run system control status and read the journal. Here we check the unit file itself. Type: cat web dot service."),
  c('s2', "A unit file has sections. The Service section says what to run. Now ask system D to verify the file. Type: systemd-analyze verify web.service, and keep only the lines about our file with grep web.", "A unit file has sections. The Service section says what to run. Now ask system D to verify the file. Type: system D analyze, verify, web dot service, and keep only the lines about our file with grep web."),
  c('s3', "There is the cause, in plain words. The command is not executable: no such file. Look closely at the path. Pythn three. A missing letter o."),
  c('s4', "Check the real path before you edit. Type: ls /usr/bin/python3.", "Check the real path before you edit. Type: L S, slash U S R, slash bin, slash python three."),
  c('s5', "It exists. Fix one thing, with a backup. Type: sed -i.bak and the substitution, then web.service. Dash i dot bak keeps the original as web dot service dot bak.", "It exists. Fix one thing, with a backup. Type: sed, dash i dot bak, the substitution that changes pythn three to python three, then web dot service. Dash i dot bak keeps the original as web dot service dot bak."),
  c('s6', "Verify. Run the same check again. Type: systemd-analyze verify web.service.", "Verify. Run the same check again. Type: system D analyze, verify, web dot service."),
  c('s7', "Silence. No errors. With this tool, silence is success. Last, see exactly what you changed. Type: diff web.service.bak web.service.", "Silence. No errors. With this tool, silence is success. Last, see exactly what you changed. Type: diff, web dot service dot bak, web dot service."),
  c('s8', "One word changed, and you can prove it. That is how careful administrators work."),
 ]),
 ('tools', [
  c('o1', "On a live system, with system D running, you add a few more tools to the same method."),
  c('o2', "Systemctl status shows whether a service is running, and its last log lines.", "System control status shows whether a service is running, and its last log lines."),
  c('o3', "Journalctl dash u, then the service name, shows that service's own log.", "Journal control, dash u, then the service name, shows that service's own log."),
  c('o4', "After you edit a unit file, run systemctl daemon dash reload, so system D reads it again.", "After you edit a unit file, run system control daemon reload, so system D reads it again."),
  c('o5', "Then restart the service, and run status again to verify.", "Then restart the service, and run system control status again to verify."),
  c('o6', "Same method. Symptom, check, fix, verify. These screens are an illustration, not a recording."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: a reboot fixes everything. No. It hides the cause, wipes the evidence, and the fault comes back."),
  c('my3', "Myth two: chmod seven seven seven fixes permissions. It does, by removing all protection. Add only the bit that is missing."),
  c('my4', "Myth three: disk full, so delete something big. Check first. The biggest file may be the one that matters."),
  c('my5', "Myth four: keep restarting until it works. A restart without a fix just fails again. Read the error."),
  c('my6', "Read it. Check it. Fix one thing. Verify."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Name the four steps of the method."),
  c('b3', "Read a file mode with ls dash l, and fix it with chmod."), c('b4', "Find a full disk with df, and what fills it with du."),
  c('b5', "Tell connection refused from timed out, and check listeners with ss."), c('b6', "Verify a unit file with systemd-analyze, and name the status and journal commands."),
  c('b7', "Verify after every fix, and back up before you edit."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own virtual machine. Break things only on a machine you own, and keep notes as you go."),
  c('z2', "One: make a script, take away its execute bit, watch it fail, then fix it with chmod."),
  c('z3', "Two: fill a small loop disk image, find the culprit with D U, and free the space."),
  c('z4', "Three: start a web server, stop it, read connection refused, and bring it back."),
  c('z5', "Four: put a typo in a unit file, and catch it with systemd dash analyze verify."),
  c('z6', "Five: on a machine running system D, make a real service fail on purpose. Read status and the journal."),
  c('z7', "Six: for each fault, write four lines in a notes file: symptom, check, fix, verify."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which command shows what is using disk space?"), c('f13', "What does connection refused tell you?"),
  c('f14', "Which tool checks a unit file for mistakes?"), c('f15', "What do you do after every fix?"),
  c('f16', "Objective covered: MC04-O10.", "Objective covered: M C zero four, objective ten, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: the Linux administration mastery scenario."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'm6': 0.5, 'p3': 0.4, 'p6': 0.5, 'd3': 0.4, 'd4': 0.4, 'd7': 0.5, 't2': 0.3, 't3': 0.4, 't4': 0.4, 't6': 0.4, 't7': 0.5, 's3': 0.4, 's7': 0.3, 's8': 0.5, 'o6': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'method': 'The four step method', 'perms': 'Fault 1: permission denied', 'disk': 'Fault 2: disk full', 'net': 'Fault 3: connection refused', 'svc': 'Fault 4: broken service file', 'tools': 'Live system tools', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))


def s_hook(C, D, dur):
    E = [El(T('Find the cause. Fix it calmly.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Permissions', 'a script that will not run', ACC), ('Storage', 'a disk that is full', VIO), ('Connectivity', 'a service nobody listens to', WARN), ('Services', 'a broken unit file', PINK)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 2.2))
    E.append(takeaway('Symptom. Check. Fix. Verify.', 880, C['h3'], GOOD, 1600)); return E
def s_method(C, D, dur):
    E = head('The four step method', 'Use it on every fault.', C['m1']); E.append(ill(C['m1'] + 0.2, 1400, 170))
    it = [('1  Symptom', 'read the exact error', BAD, 'm2'), ('2  Check', 'ask the system, then act', ACC, 'm3'), ('3  Fix one thing', 'small change, keep a backup', WARN, 'm4'), ('4  Verify', 'repeat the original action', GOOD, 'm5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s_, TXT)], 44, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Slow is smooth.', 800, C['m6'], GOOD, 1500)); return E
s_perms = _lab('Fault 1: permission denied', 'The file is there. The system says no.', 'p1', RB, [('p1', './backup.sh', 'Symptom: denied', BAD), ('p2', 'ls -l', 'Check the mode', ACC), ('p4', 'chmod u+x', 'Fix one thing', WARN), ('p5', './backup.sh', 'Verify', GOOD)])
s_disk = _lab('Fault 2: disk full', 'No space left on device.', 'd1', RB, [('d1', 'save a file', 'Symptom: no space', BAD), ('d2', 'df -h', 'How full?', ACC), ('d3', 'du -ah | sort', 'What fills it?', VIO), ('d4', 'rm one file', 'Fix one thing', WARN), ('d5', 'save again', 'Verify', GOOD)])
s_net = _lab('Fault 3: connection refused', 'Reachable, but nobody is listening.', 't1', RB, [('t1', 'nc -zv', 'Symptom: refused', BAD), ('t2', 'ss -tln', 'Who is listening?', ACC), ('t4', 'start it', 'Fix one thing', WARN), ('t5', 'nc -zv', 'Verify', GOOD), ('t6', 'ss -tln', 'Listener found', VIO)])
s_svc = _lab('Fault 4: broken service file', 'Read the unit before you restart it.', 's1', RB, [('s1', 'cat web.service', 'What runs?', ACC), ('s2', 'systemd-analyze', 'Verify the file', BAD), ('s5', 'sed -i.bak', 'Fix, keep a backup', WARN), ('s6', 'verify again', 'Silence is success', GOOD), ('s7', 'diff', 'Prove the change', VIO)])
def s_tools(C, D, dur):
    E = head('Live system tools', 'Same method, more commands.', C['o1']); E.append(ill(C['o1'] + 0.2, 1400, 170))
    it = [('systemctl status web', 'Running? Last log lines', ACC, 'o2'), ('journalctl -u web', 'The service log', VIO, 'o3'), ('systemctl daemon-reload', 'After editing a unit', WARN, 'o4'), ('systemctl restart web', 'Then verify with status', GOOD, 'o5')]
    for i, (n, s_, col, cid) in enumerate(it):
        E.append(Pop(card(1100, 130, col, '', [], 4), 100, 330 + i * 160, C[cid]))
        E.append(El(T(n, 'mono', 34, TXT, align='left'), 140, 352 + i * 160, C[cid] + 0.2, anim='fade')); E.append(El(T(s_, 'm', 28, MUTED, maxw=1000), 140, 400 + i * 160, C[cid] + 0.3, anim='fade'))
    E.append(takeaway('Symptom, check, fix, verify.', 980, C['o6'], GOOD, 1500)); return E
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: reboot fixes it', 'Hides the cause.', 'my2'), ('Myth: chmod 777', 'Add only the missing bit.', 'my3'), ('Myth: delete the big file', 'Check what it is first.', 'my4'), ('Myth: restart until it works', 'Read the error.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Read it. Check it. Fix one thing. Verify.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('The four steps', 'b2'), ('ls -l and chmod', 'b3'), ('df and du', 'b4'), ('Refused vs timeout, ss', 'b5'), ('Verify a unit file', 'b6'), ('Verify and back up', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Keep notes.', C['z1'])
    it = [('1  Perms', 'break and fix a script', PINK, 'z2'), ('2  Disk', 'fill it, find it, free it', ACC, 'z3'), ('3  Port', 'stop, refuse, restore', WARN, 'z4'), ('4  Unit', 'typo, systemd-analyze', VIO, 'z5'), ('5  Real service', 'status and journal', BAD, 'z6'), ('6  Notes', 'symptom, check, fix, verify', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command shows what uses disk space?', 'f12'), ('What does connection refused tell you?', 'f13'), ('Which tool checks a unit file?', 'f14'), ('What do you do after every fix?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O10', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: the mastery scenario', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, method=s_method, perms=s_perms, disk=s_disk, net=s_net, svc=s_svc, tools=s_tools, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(method=('board', ACC), perms=('gear', ACC), disk=('eye', WARN), net=('eye', GOOD), svc=('gear', VIO), tools=('gear', VIO), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'perms': [('p2', 1, 1, 285, 565, ''), ('p3', 1, 1, 4, 160, ''), ('p6', 1, 1, 4, 245, '')],
 'disk': [('d2', 1, 1, 375, 735, ''), ('d3', 2, 1, 440, 575, ''), ('d4', 1, 2, 4, 380, ''), ('d6', 1, 1, 4, 90, ''), ('d7', 2, 1, 410, 575, '')],
 'net': [('t2', 1, 1, 730, 1018, ''), ('t5', 1, 1, 4, 135, ''), ('t6', 1, 1, 730, 892, ''), ('t7', 1, 1, 408, 598, '')],
 'svc': [('s2', 5, 1, 4, 690, ''), ('s3', 1, 1, 320, 560, ''), ('s5', 1, 1, 4, 250, ''), ('s8', 2, 3, 4, 745, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson35/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
