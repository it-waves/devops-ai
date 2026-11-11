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
