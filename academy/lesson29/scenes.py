def s_hook(C, D, dur):
    E = [El(T('Every file has an owner.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Users', 'who you are', ACC), ('Permissions', 'what you may do', VIO), ('Keys', 'how you prove it', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('Who. What. Proof.', 850, C['h3'], GOOD, 1600)); return E
s_ids = _lab('Who am I', 'Users, groups and the passwd file.', 'i1', RB, [('i1', 'whoami', 'Your user name', ACC), ('i2', 'id', 'Numbers and groups', VIO), ('i3', '/etc/passwd', 'One line per user', WARN)])
s_perms = _lab('Read and change permissions', 'r, w, x for owner, group, others.', 'p1', RB, [('p1', 'ls -l', 'See permissions', ACC), ('p3', 'rwx', 'Read, write, execute', VIO), ('p4', 'chmod 600', 'Owner read and write', WARN), ('p7', './run.sh', 'Denied: not executable', BAD), ('p8', 'chmod +x', 'Make it executable', GOOD)])
s_sudo = _lab('sudo, users and owners', 'Borrow root power, one command at a time.', 's1', RB, [('s1', '/etc/shadow', 'Denied: root only', BAD), ('s3', 'sudo', 'Borrow root', ACC), ('s4', 'useradd -m', 'New user', VIO), ('s5', 'groupadd', 'New group', WARN), ('s6', 'usermod -aG', 'Add to group', PINK), ('s8', 'chown', 'New owner', GOOD)])
s_ssh = _lab('SSH keys', 'A private half and a public half.', 'k1', RB, [('k1', 'ssh-keygen', 'Make the pair', ACC), ('k3', '.pub', 'Public: share', GOOD), ('k5', '~/.ssh', 'Server key folder', VIO), ('k6', '>>', 'Append the key', WARN), ('k7', 'chmod 700', 'Folder: owner only', PINK), ('k8', 'chmod 600', 'File: owner only', BAD)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: chmod 777 fixes it', 'It hides the problem.', 'my2'), ('Myth: sudo for everything', 'Least power wins.', 'my3'), ('Myth: share the private key', 'Public key only.', 'my4'), ('Myth: root equals sudo', 'Sudo borrows root power.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Least power. Public key only.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('whoami and id', 'b2'), ('Read ls -l permissions', 'b3'), ('chmod: numbers and +x', 'b4'), ('User, group, chown', 'b5'), ('Make an SSH key pair', 'b6'), ('SSH folder and file modes', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine. Practice folder only.', C['z1'])
    it = [('1  Who', 'whoami, id', PINK, 'z2'), ('2  Read', 'ls -l a file', ACC, 'z3'), ('3  Lock', 'chmod, check', WARN, 'z4'), ('4  Run', 'denied, then +x', VIO, 'z5'), ('5  Admin', 'user, group, chown', GOOD, 'z6'), ('6  Keys', 'pair, 700, 600', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does chmod 600 give the owner?', 'f12'), ('Which command borrows root power?', 'f13'), ('Which key file is safe to share?', 'f14'), ('What mode should ~/.ssh have?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: processes and signals', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ids=s_ids, perms=s_perms, sudo=s_sudo, ssh=s_ssh, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ids=('eye', GOOD), perms=('eye', GOOD), sudo=('question', WARN), ssh=('eye', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'ids': [('i4', 1, 1, 4, 520, '')],
 'perms': [('p2', 2, 3, 4, 150, ''), ('p6', 1, 1, 4, 150, '')],
}
