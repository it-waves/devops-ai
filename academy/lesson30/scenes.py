def s_hook(C, D, dur):
    E = [El(T('A server is never idle.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Process', 'a running program', ACC), ('Signal', 'a message to it', VIO), ('Load', 'how busy it is', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('List. Signal. Measure.', 850, C['h3'], GOOD, 1600)); return E
s_ps = _lab('List processes', 'Every running program has a PID.', 'p1', RB, [('p1', 'ps', 'Your own shell', ACC), ('p3', 'ps -eo', 'Choose the columns', VIO), ('p5', 'pcpu  pmem', 'CPU and memory', WARN)])
s_signals = _lab('Background jobs and signals', 'Start, find and stop a process.', 's1', RB, [('s1', 'cmd &', 'Run in background', ACC), ('s2', 'jobs', 'List your jobs', VIO), ('s3', 'kill %1', 'TERM: ask politely', GOOD), ('s5', 'yes > /dev/null &', 'A runaway process', BAD), ('s6', '--sort=-pcpu', 'Find the hog', WARN), ('s7', 'kill -9', 'KILL: last resort', PINK)])
s_resources = _lab('Load and memory', 'Is the machine busy?', 'r1', RB, [('r1', 'uptime', 'Load average', ACC), ('r3', 'nproc', 'Count the cores', VIO), ('r4', 'free -h', 'Read: available', WARN)])
s_running = _lab('Is it running?', 'pgrep and the exit status.', 'u1', RB, [('u2', 'pgrep -a', 'Find by name', ACC), ('u3', 'pkill', 'Stop by name', VIO), ('u5', 'echo $?', 'Exit status', WARN), ('u6', '0 found  1 none', 'What it means', GOOD)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: kill -9 is normal', 'Try TERM first.', 'my2'), ('Myth: high memory is bad', 'Read available.', 'my3'), ('Myth: only load matters', 'Compare with cores.', 'my4'), ('Myth: kill only kills', 'It sends signals.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('TERM first. KILL last.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('List PID, user, command', 'b2'), ('Run a job in background', 'b3'), ('TERM first, KILL last', 'b4'), ('Find the CPU hog', 'b5'), ('Load vs CPU cores', 'b6'), ('pgrep and exit status', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine. Practice folder only.', C['z1'])
    it = [('1  List', 'ps -eo, find PID 1', PINK, 'z2'), ('2  Start', 'sleep 300 &, jobs', ACC, 'z3'), ('3  Stop', 'kill, confirm', WARN, 'z4'), ('4  Hog', 'yes, find, stop', VIO, 'z5'), ('5  Load', 'uptime, nproc', GOOD, 'z6'), ('6  Memory', 'free -h, available', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which character runs a command in the background?', 'f12'), ('Which signal does a plain kill send?', 'f13'), ('Which memory column should you read?', 'f14'), ('Which exit status means found?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O05', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: systemd, logs and cron', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, ps=s_ps, signals=s_signals, resources=s_resources, running=s_running, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(ps=('eye', GOOD), signals=('eye', GOOD), resources=('eye', GOOD), running=('eye', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'signals': [('s7', 2, 1, 4, 200, '')],
}
