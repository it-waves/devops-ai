def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))

def s_hook(C, D, dur):
    E = [El(T('Software arrives in packages.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Package', 'a program plus what it needs', ACC), ('Repository', 'where packages are kept', VIO), ('apt and dpkg', 'find them, install them', WARN)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 2.6))
    E.append(takeaway('Preview. Then change.', 850, C['h3'], GOOD, 1600)); return E
s_repo = _lab('Repositories and versions', 'Where packages come from.', 'q1', RB, [('q1', 'sources file', 'The repository list', ACC), ('q3', 'Suites', 'Release channels', VIO), ('q5', 'apt-cache policy', 'Installed vs candidate', GOOD)])
s_installed = _lab('Inspect installed packages', 'Ask the package database.', 'd1', RB, [('d1', 'dpkg -s', 'What is installed', ACC), ('d3', 'dpkg -S', 'Who owns a file', VIO), ('d5', 'dpkg -L', 'Files it installed', WARN)])
s_plan = _lab('Preview before you change', 'Simulate with -s. Nothing changes.', 'n1', RB, [('n1', 'install -s', 'Preview an install', GOOD), ('n3', 'Inst lines', 'The plan', ACC), ('n4', 'remove -s', 'Preview a removal', BAD), ('n6', 'upgrade -s', 'Updates waiting', WARN)])
def s_manage(C, D, dur):
    E = head('Install, update, remove', 'The routine, with sudo.', C['a1']); E.append(ill(C['a1'] + 0.2, 1260, 286))
    rows = [('$ sudo apt update', GOOD), ('Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease', TXT), ('Get:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease', TXT), ('Get:3 http://security.ubuntu.com/ubuntu noble-security InRelease', TXT), ('Fetched 252 kB in 1s', TXT), ('Reading package lists... Done', TXT), ('22 packages can be upgraded.', TXT)]
    mono_panel(E, 100, 345, 1060, rows, C['a2'], fs=22, lh=38)
    hbar(E, 112, 345 + 24 + 6 * 38 - 4, 1030, 36, C['a4'], C['a4'] + dur['a4'] + 0.5, WARN)
    it = [('sudo apt update', 'Refresh the lists', ACC, 'a2'), ('sudo apt install pkg', 'Shows the plan, asks', VIO, 'a3'), ('sudo apt upgrade', 'Update, then upgrade', GOOD, 'a4'), ('remove  /  purge', 'Purge deletes config too', WARN, 'a5'), ('sudo apt autoremove', 'Unneeded dependencies', PINK, 'a6')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(560, 105, col, a, [(b, TXT)], 32, 26), 1260, 345 + i * 118, C[cid]))
    E.append(takeaway('Read the plan. Then answer yes.', 920, C['a7'], GOOD, 1100)); return E
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: update installs', 'Update = refresh the list.', 'my2'), ('Myth: remove deletes all', 'Purge deletes config.', 'my3'), ('Myth: it installs, so safe', 'Use trusted repositories.', 'my4'), ('Myth: yes to every prompt', 'Read the plan first.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Update. Read. Upgrade.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Repositories and sources', 'b2'), ('Installed vs candidate', 'b3'), ('Which package owns a file', 'b4'), ('Simulate and read the plan', 'b5'), ('Update, upgrade, purge', 'b6'), ('Add software safely', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Read and simulate only. Nothing is installed.', C['z1'])
    it = [('1  Sources', 'read the list, suites', PINK, 'z2'), ('2  Policy', 'installed vs candidate', ACC, 'z3'), ('3  Inspect', 'dpkg -s and dpkg -S', WARN, 'z4'), ('4  Preview', 'apt-get -s install', VIO, 'z5'), ('5  Update', 'apt update, upgradable', GOOD, 'z6'), ('6  Remove', 'simulate, purge', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command refreshes the lists?', 'f12'), ('Which flag simulates an install?', 'f13'), ('Which option finds a file owner?', 'f14'), ('Does remove delete config files?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: disks, filesystems, mounts', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, repo=s_repo, installed=s_installed, plan=s_plan, manage=s_manage, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(repo=('eye', GOOD), installed=('eye', GOOD), plan=('eye', GOOD), manage=('gear', ACC), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'repo': [('q2', 1, 2, 4, 592, ''), ('q4', 1, 2, 4, 652, ''), ('q6', 2, 2, 4, 450, '')],
 'installed': [('d2', 2, 1, 4, 424, ''), ('d4', 1, 1, 4, 290, ''), ('d6', 1, 2, 4, 216, '')],
 'plan': [('n2', 1, 2, 4, 948, ''), ('n3', 3, 2, 4, 1062, ''), ('n5', 1, 2, 4, 700, ''), ('n5', 4, 1, 4, 454, ''), ('n7', 1, 1, 4, 948, '')],
}
