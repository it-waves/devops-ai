def s_hook(C, D, dur):
    E = [El(T('Run Tomcat as a service', 'x', 66), 100, 130, C['h1'])]
    E.append(Pop(card(900, 150, WARN, 'by hand', [('gone at the next reboot', TXT)], 52, 32), 100, 320, C['h1'] + 1.0))
    E.append(Pop(card(900, 150, ACC, 'as a service', [('starts at boot, as its own user', TXT)], 52, 32), 100, 500, C['h2']))
    E.append(Pop(card(900, 160, VIO, 'comes back alone', [('after a crash', TXT)], 46, 30), 1000, 410, C['h3']))
    E.append(Pop(card(1100, 140, GOOD, 'crash it on purpose', [('and watch systemd recover', TXT)], 46, 30), 100, 720, C['h4']))
    E.append(takeaway('A service that survives reboots and crashes.', 900, C['h4'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
def s_plan(C, D, dur):
    E = head('Four ideas', 'Setting, file, unit, service.', C['a1'])
    st = [('1  Port', 'a property, 8080 default', ACC, 'a2'), ('2  Environment', 'setenv.sh holds options', VIO, 'a3'), ('3  Unit file', 'user, restart, boot', WARN, 'a4'), ('4  systemctl', 'reload, enable, start', GOOD, 'a5')]
    for i, (n, sb, col, cid) in enumerate(st): E.append(Pop(card(400, 330, col, n, [(sb, TXT)], 40, 26), 100 + i * 430, 400, C[cid]))
    E.append(Pop(card(1700, 120, ACC, '', [('setting > file > unit > service', TXT)], 4, 38), 100, 800, C['a6'])); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab107.sh: a real Tomcat on your VM. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  setenv.sh', [('java, pid file,', TXT), ('port, env name', TXT)], 'k2', ACC), ('2  Unit file', [('forking, tomcat,', TXT), ('Restart=on-failure', TXT)], 'k3', WARN), ('3  Start', [('reload, enable,', TXT), ('--now, :8081', TXT)], 'k4', VIO), ('4  Crash it', [('kill -9,', TXT), ('systemd restarts', TXT)], 'k5', PINK), ('5  lab check', [('all five', TXT), ('must pass', TXT)], 'k6', GOOD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab107.sh   and   shortcuts106.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab107.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts106.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'real systemd, JDK, curl, 1 GB', PINK, 'i6'), ('6  Check + cleanup', 'lab check builds on your machine. lab down removes all.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('setenv.sh: port + options', 'q3x'), ('unit runs as tomcat', 'q4x'), ('active, enabled, 200', 'q5x'), ('restarts after kill -9', 'q6x'), ('lab down removes all', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the tasks', PINK, 'z2'), ('2  setenv.sh', 'java, pid, port, env', ACC, 'z3'), ('3  Unit file', 'forking, user, restart', WARN, 'z4'), ('4  Run it', 'reload, enable --now', VIO, 'z5'), ('5  Crash it', 'kill -9, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Port from the environment?', 'f12'), ('What is Type=forking?', 'f13'), ('What brings it back?', 'f14'), ('What starts it at boot?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC12-O04 Service', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: logs and diagnosing failures', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: port, environment, service', 'Real systemd, a real unit file, a real crash.', 'p0', RB, [('l2', '1  the port property', 'http.port, 8080 default', ACC), ('l3', '2  setenv.sh', 'java, pid, options', VIO), ('l5', '3  the unit file', 'forking, tomcat, restart', WARN), ('l7', '4  enable --now', 'start now and at boot', GOOD), ('l13', '5  kill -9', 'systemd restarts it', PINK), ('l16', '6  the journal', 'why it restarted', ACC)])
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
_rs = open('/home/claude/academy/lesson107/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
