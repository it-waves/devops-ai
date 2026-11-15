def s_hook(C, D, dur):
    E = [El(T('Installing Tomcat', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(900, 150, BAD, 'the usual way', [('download, unpack, run as root', TXT)], 52, 32), 100, 320, C['h2']))
    E.append(Pop(card(900, 150, WARN, 'the risk', [('one app bug = full control', TXT)], 52, 32), 100, 500, C['h3']))
    E.append(Pop(card(900, 160, ACC, 'today', [('the right way, on real Linux', TXT)], 46, 30), 1000, 410, C['h4']))
    E.append(Pop(card(1100, 140, GOOD, 'verify, user, run, log, browser', [('then tour the web interface', TXT)], 46, 30), 100, 720, C['h5']))
    E.append(takeaway('Install it safely, from day one.', 900, C['h5'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
def s_plan(C, D, dur):
    E = head('The five steps', 'The same on any server.', C['a1'])
    st = [('1  Verify', 'checksum matches', ACC, 'a2'), ('2  User', 'no login shell', VIO, 'a3'), ('3  Unpack', 'strip components', WARN, 'a4'), ('4  Owner', 'chown to tomcat', PINK, 'a5'), ('5  Run', 'as tomcat, not root', GOOD, 'a6')]
    for i, (n, sb, col, cid) in enumerate(st): E.append(Pop(card(320, 330, col, n, [(sb, TXT)], 40, 28), 100 + i * 345, 400, C[cid]))
    E.append(Pop(card(1700, 120, ACC, '', [('verify > user > unpack > owner > run', TXT)], 4, 38), 100, 800, C['a7'])); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab105.sh: a real Tomcat on your VM. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Verify', [('sha512sum -c', TXT), ('checksum.txt', TXT)], 'k2', ACC), ('2  User', [('useradd, no', TXT), ('login shell', TXT)], 'k3', WARN), ('3  Unpack + own', [('tar, then', TXT), ('chown -R', TXT)], 'k4', VIO), ('4  Run as tomcat', [('startup.sh, 200', TXT), ('on :8080', TXT)], 'k5', PINK), ('5  The log', [('Server startup', TXT), ('startup.txt', TXT)], 'k6', GOOD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab105.sh   and   shortcuts105.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab105.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts105.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, curl, 1 GB, internet', PINK, 'i6'), ('6  Check + cleanup', 'lab check builds on your machine. lab down removes all.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('Checksum verified: OK', 'q3x'), ('tomcat user, no login', 'q4x'), ('Files owned by tomcat', 'q5x'), ('200, runs as tomcat', 'q6x'), ('lab down removes all', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the tasks', PINK, 'z2'), ('2  Verify', 'sha512sum -c', ACC, 'z3'), ('3  User + unpack', 'useradd, tar', WARN, 'z4'), ('4  Own + run', 'chown, start as tomcat', VIO, 'z5'), ('5  Log + check', 'startup.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why verify the download?', 'f12'), ('Why a no-login user?', 'f13'), ('What does file ownership control?', 'f14'), ('Where is the proof it started?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC12-O02 Install and run', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: deploy a WAR built with Maven', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: install and run', 'Real Apache Tomcat 10.1.34, real Linux, then a real browser.', 'p0', RB, [('l3', '1  verify', 'sha512sum -c: OK', ACC), ('l5', '2  user', 'no login shell', WARN), ('l8', '3  unpack', 'tar, strip components', VIO), ('l10', '4  owner', 'chown -R tomcat', PINK), ('l12', '5  run as tomcat', 'ps shows tomcat, 200', GOOD), ('u0', '6  browser tour', 'welcome, manager, examples', ACC)])
FN = dict(hook=s_hook, plan=s_plan, live=s_live, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(plan=('board', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': []}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson105/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
