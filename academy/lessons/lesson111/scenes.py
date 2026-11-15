def s_hook(C, D, dur):
    E = [El(T('Bad release?', 'x', 66), 100, 130, C['h1'])]
    E.append(Pop(card(900, 150, GOOD, 'the home page loads', [('CloudCart 2.0, all green', TXT)], 52, 32), 100, 320, C['h1'] + 1.0))
    E.append(Pop(card(900, 150, WARN, 'but health says 503', [('the app is really down', TXT)], 52, 32), 100, 500, C['h2']))
    E.append(Pop(card(900, 160, VIO, 'watch and read', [('a health script and the log', TXT)], 46, 30), 1000, 410, C['h3']))
    E.append(Pop(card(1100, 140, GOOD, 'roll back, then fix', [('users first, cause second', TXT)], 46, 30), 100, 720, C['h4']))
    E.append(takeaway('One health page, one calm recovery.', 900, C['h4'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
def s_plan(C, D, dur):
    E = head('Four moves', 'Watch, read, roll back, fix.', C['a1'])
    st = [('1  Watch', 'health page + script', ACC, 'a2'), ('2  Read', 'the log says why', VIO, 'a3'), ('3  Roll back', 'last good release', WARN, 'a4'), ('4  Fix', 'the cause, ship again', GOOD, 'a5')]
    for i, (n, sb, col, cid) in enumerate(st): E.append(Pop(card(400, 330, col, n, [(sb, TXT)], 40, 26), 100 + i * 430, 400, C[cid]))
    E.append(Pop(card(1700, 120, ACC, '', [('watch > read > roll back > fix', TXT)], 4, 38), 100, 800, C['a6'])); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab111.sh: a real Tomcat release. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Start + watch', [('startup.sh, health.sh', TXT), ('exit 0 on 200', TXT)], 'k2', ACC), ('2  Bad release', [('ship cart-2.0.war,', TXT), ('read the log', TXT)], 'k3', WARN), ('3  Roll back', [('cart-1.0.war', TXT), ('health 200 again', TXT)], 'k4', VIO), ('4  Fix + ship', [('pool.size=10,', TXT), ('ship 2.0 again', TXT)], 'k5', PINK), ('5  lab check', [('all five', TXT), ('must pass', TXT)], 'k6', GOOD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab111.sh   and   shortcuts111.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab111.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts111.sh  then: lab', WARN, 'i5'), ('5  You need', 'JDK, curl, 1 GB, ports 8087 8097', PINK, 'i6'), ('6  Check + cleanup', 'lab check tests it. lab down removes all.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('Tomcat answers on 8087', 'q3x'), ('health.sh exits 0 when healthy', 'q4x'), ('cart.war deployed 4 times', 'q5x'), ('log: pool.size is missing', 'q6x'), ('pool.size set, 2.0 healthy', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own machine only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, startup.sh', PINK, 'z2'), ('2  Watch', 'health.sh, the loop', ACC, 'z3'), ('3  Bad release', 'ship 2.0, read log', WARN, 'z4'), ('4  Roll back', 'cart-1.0.war', VIO, 'z5'), ('5  Fix + check', 'pool.size, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why is a loading page not a health check?', 'f12'), ('Roll back first, or investigate first?', 'f13'), ('Where did you read why it failed?', 'f14'), ('How does Tomcat notice a new war?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC12-O08 Health and recovery', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: the Tomcat mastery scenario', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: ship a bad release, recover', 'A real release, a real failure, a real browser.', 'p0', RB, [('l5', '1  watch', 'health page says UP', ACC), ('l6', '2  script', 'health.sh, exit code', VIO), ('l10', '3  bad release', 'ship 2.0: 503', WARN), ('l13', '4  read why', 'log: pool.size missing', GOOD), ('u0', '5  the browser', 'page vs health page', PINK), ('l15', '6  recover', 'roll back, fix, ship', ACC)])
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
_rs = open('/home/claude/academy/lesson111/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
