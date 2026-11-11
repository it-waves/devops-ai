def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))


def s_hook(C, D, dur):
    E = [El(T('The network is the front door.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Read it', 'addresses, routes, listeners', ACC), ('Lock it', 'SSH keys, no passwords', VIO), ('Filter it', 'a firewall with UFW', WARN)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100 + 0, 280 + i * 160, C['h2'] + i * 2.6))
    E.append(takeaway('Know it. Lock it. Filter it.', 850, C['h3'], GOOD, 1600)); return E
s_net = _lab('Your network, in four commands', 'Address, route, reach, listen.', 'n1', RB, [('n1', 'ip -br addr', 'Your addresses', ACC), ('n3', 'ip route', 'Where traffic goes', VIO), ('n5', 'ping -c 2', 'Can we reach it?', GOOD), ('n7', 'ss -tlnp', 'What is listening', WARN)])
s_ssh = _lab('Log in with a key', 'Private key stays. Public key goes.', 'k1', RB, [('k1', 'ssh-keygen', 'Make a key pair', ACC), ('k3', 'id_ed25519.pub', 'Public: safe to share', GOOD), ('k4', 'authorized_keys', 'Who may log in', VIO), ('k5', 'chmod 600', 'Lock the file down', WARN), ('k6', 'ssh localhost', 'Log in, no password', PINK)])
s_harden = _lab('Lock the SSH door', 'No passwords. No root login.', 'r1', RB, [('r1', 'sshd_config.d', 'The settings', ACC), ('r3', 'sshd -T', 'What is really used', VIO), ('r5', 'ssh, no key', 'Test the lock', BAD), ('r7', 'sshd -t', 'Test before reload', GOOD)])
s_fw = _lab('A firewall in minutes', 'Allow what you need. Deny the rest.', 'w1', RB, [('w1', 'ufw status', 'Inactive at first', ACC), ('w3', 'allow 22/tcp', 'SSH first!', WARN), ('w5', 'ufw enable', 'Switch it on', GOOD), ('w7', 'status numbered', 'List the rules', VIO), ('w9', 'delete allow', 'Remove a rule', PINK)])
def s_habits(C, D, dur):
    E = head('Security habits', 'Small habits stop most attacks.', C['e1'])
    it = [('1  Keys', 'not passwords', ACC, 'e2'), ('2  No root', 'login, use sudo', VIO, 'e3'), ('3  Few ports', 'know what listens', WARN, 'e4'), ('4  Updates', 'apt, every week', GOOD, 'e5'), ('5  Least', 'privilege for all', PINK, 'e6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    return E
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: firewall = secure', 'It is one layer only.', 'my2'), ('Myth: long passwords', 'Keys cannot be guessed.', 'my3'), ('Myth: new SSH port', 'Hides noise, not a lock.', 'my4'), ('Myth: listening = needed', 'Check it. Stop unused.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Read it. Lock it. Filter it.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Addresses and routes', 'b2'), ('What is listening', 'b3'), ('Key login', 'b4'), ('Harden SSH, test it', 'b5'), ('Firewall, SSH first', 'b6'), ('Three security habits', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Keep a second session open.', C['z1'])
    it = [('1  Look', 'ip, route, ss', PINK, 'z2'), ('2  Keys', 'with a passphrase', ACC, 'z3'), ('3  Login', 'authorized_keys', WARN, 'z4'), ('4  Harden', 'no passwords, sshd -t', VIO, 'z5'), ('5  Firewall', 'allow SSH, enable', BAD, 'z6'), ('6  Verify', 'second session first', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command shows your addresses?', 'f12'), ('Which file lists allowed keys?', 'f13'), ('Which command tests the SSH config?', 'f14'), ('What do you allow before enabling?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O09', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: diagnose and recover', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, net=s_net, ssh=s_ssh, harden=s_harden, fw=s_fw, habits=s_habits, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(net=('eye', GOOD), ssh=('gear', ACC), harden=('test', GOOD), fw=('eye', GOOD), habits=('board', WARN), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'net': [('n2', 2, 1, 4, 700, ''), ('n4', 1, 1, 4, 440, ''), ('n6', 6, 1, 4, 780, ''), ('n8', 2, 2, 4, 1060, '')],
 'ssh': [('k3', 1, 1, 4, 400, ''), ('k7', 2, 2, 4, 1065, ''), ('k8', 9, 1, 4, 70, '')],
 'harden': [('r2', 2, 2, 4, 480, ''), ('r4', 1, 2, 4, 420, ''), ('r6', 1, 1, 4, 760, ''), ('r8', 1, 1, 4, 150, '')],
 'fw': [('w2', 1, 1, 4, 260, ''), ('w6', 1, 1, 4, 740, ''), ('w8', 5, 2, 4, 600, ''), ('w10', 1, 1, 4, 160, '')],
}
