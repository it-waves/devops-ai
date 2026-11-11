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
