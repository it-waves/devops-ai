import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 15  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps
_SP = {'CPU': 'C P U', 'RAM': 'R A M', 'OOM': 'O O M', 'nproc': 'n proc', 'df': 'd f', 'du': 'd u', 'dd': 'd d', 'ps': 'p s', 'ss': 's s', 'HTTP': 'H T T P', 'curl': 'curl', 'tmpfs': 't m p f s', 'ulimit': 'u limit', 'kill': 'kill', 'rm': 'r m', 'tail': 'tail', 'grep': 'grep'}
def _say(cap):
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in _SP) + r')(?![\w-])', lambda m: _SP[m.group(1)], cap)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "A server is just a computer that other computers depend on."), c('h2', "When it breaks, people notice quickly."),
  c('h3', "The good news: a handful of parts cause most failures, and each one fails in a recognisable way."),
  c('h4', "Today you meet those parts, and watch each one fail, live, in a safe practice setup."),
 ]),
 ('parts', [
  c('p1', "Every server has the same main parts."), c('p2', "The CPU does the work."), c('p3', "Memory, or RAM, is the fast workspace for whatever is running right now."),
  c('p4', "The disk stores data for the long term."), c('p5', "The network connects the server to everyone else."),
  c('p6', "Services are the programs that wait for requests."), c('p7', "And logs are the diary where those programs write down what happened."),
  c('p8', "Learn which part fails in which way, and troubleshooting gets much easier."),
 ]),
 ('cpu', [
  c('q1', "First, the CPU."), c('q2', "It runs instructions, billions of times every second."),
  c('q3', "Each core does one thing at a time, so a busy server shares its cores out."),
  c('q4', "When one program hogs the CPU, everything else slows down."), c('q5', "The symptom: slow responses, lag, and a high load."),
  c('q6', "The first check: which process is using the most CPU?"),
 ]),
 ('cpudemo', [
  c('r1', "Let us watch a CPU problem happen."), c('r2', "First, how many cores? Type: nproc", "First, how many cores? Type: n proc."), c('r3', "Two cores. That is our budget."),
  c('r4', "Now start a program that never rests. Type: yes > /dev/null &", "Now start a program that never rests. Type: yes, redirect into dev null, and an ampersand."),
  c('r5', "The ampersand runs it in the background, and the shell gives it a job number."),
  c('r6', "Now ask who is busiest. Type: ps -u student -o pid,pcpu,comm --sort=-pcpu", "Now ask who is busiest. Type: p s, dash u student, dash o, pid, comma, p c p u, comma, comm, dash dash sort equals dash p c p u."),
  c('r7', "There it is: yes, using about ninety-nine percent of one core."), c('r8', "That is a runaway process. Stop it. Type: kill %1", "That is a runaway process. Stop it. Type: kill, percent one."),
  c('r9', "Now ask again. Press the up arrow twice, then Enter."), c('r10', "Gone. The CPU is free again. The pattern: find the busiest process, then decide whether to stop it."),
 ]),
 ('mem', [
  c('s1', "Next, memory."), c('s2', "Memory holds the data of every running program, and it is much faster than the disk."),
  c('s3', "But it is limited. When it runs out, the system starts swapping to disk, which is very slow."),
  c('s4', "If it runs out completely, the system kills a program to survive. That event is called out of memory."),
  c('s5', "The symptom: sudden slowness, or a program that vanishes without warning."), c('s6', "The first check: free dash h."),
 ]),
 ('memdemo', [
  c('t1', "Let us look at memory. Type: free -h", "Let us look at memory. Type: free, dash h."),
  c('t2', "Total is what exists. Available is what a new program can really use."),
  c('t3', "Now a greedy program. Look at it first. Type: cat hog.py", "Now a greedy program. Look at it first. Type: cat, hog dot p y."),
  c('t4', "It asks for five hundred megabytes in one go."),
  c('t5', "To copy a small server, we cap this run at two hundred megabytes. Type: (ulimit -v 200000; python3 hog.py) 2>&1 | tail -1",
    "To copy a small server, we cap this run at two hundred megabytes. Type: open bracket, u limit, dash v, two hundred thousand, semicolon, python three, hog dot p y, close bracket, two, greater than, ampersand one, pipe, tail, dash one."),
  c('t6', "Memory error. The program asked for more than it was allowed."),
  c('t7', "On a real server with no cap, the kernel would kill it instead, and the log would say out of memory."),
 ]),
 ('disk', [
  c('u1', "Now the disk."), c('u2', "The disk keeps your files, databases, and logs."),
  c('u3', "A full disk is one of the most common outages, and one of the easiest to miss."),
  c('u4', "When there is no room, databases stop writing, logs stop, and programs crash."),
  c('u5', "The symptom: no space left on device."), c('u6', "The first checks: d f to see which disk is full, then d u to see what is filling it."),
 ]),
 ('diskdemo', [
  c('v1', "Let us fill a disk, safely. We use a small practice disk of only ten megabytes."),
  c('v2', "Type: df -h data", "Type: d f, dash h, data."), c('v3', "Size ten megabytes, almost nothing used."),
  c('v4', "Now write twenty megabytes into it. Type: dd if=/dev/zero of=data/big.bin bs=1M count=20",
    "Now write twenty megabytes into it. Type: d d, i f equals slash dev slash zero, o f equals data slash big dot bin, b s equals one M, count equals twenty."),
  c('v5', "No space left on device. The disk is full."), c('v6', "Check again. Type: df -h data", "Check again. Type: d f, dash h, data."), c('v7', "One hundred percent used."),
  c('v8', "Who is using it? Type: du -sh data/*", "Who is using it? Type: d u, dash s h, data slash star."), c('v9', "One file, big dot bin, ten megabytes. Found the culprit."),
  c('v10', "Remove it. Type: rm data/big.bin", "Remove it. Type: r m, data slash big dot bin."), c('v11', "One last check. Type: df -h data", "One last check. Type: d f, dash h, data."),
  c('v12', "Back to zero. Check disk space early, before a full disk stops your service."),
 ]),
 ('svc', [
  c('w1', "Now services: the programs that answer requests, like a web server."),
  c('w2', "A service must be running, and it must be listening on a port."), c('w3', "A port is a numbered door on the server. Only one program can hold each door."),
  c('w4', "Clients get codes back. Two hundred means success. Four hundred four means that page is missing. Five hundred range means the server itself failed."),
  c('w5', "The symptom: connection refused, or an error code. The first check: is it running, and is it listening?"),
 ]),
 ('svcdemo', [
  c('x1', "Let us run a tiny web server that comes with Python."),
  c('x2', "Type: python3 -m http.server 8080 >server.log 2>&1 &",
    "Type: python three, dash m, h t t p dot server, eight zero eight zero, then redirect everything into server dot log, and run it in the background."),
  c('x3', "Is it reachable? Ask for its headline. Type: curl -sI localhost:8080 | head -1", "Is it reachable? Ask for its headline. Type: curl, dash s capital I, localhost, colon eight zero eight zero, pipe, head, dash one."),
  c('x4', "Two hundred, O K. The service is up."),
  c('x5', "Now ask for a page that does not exist. Type: curl -sI localhost:8080/nope | head -1", "Now ask for a page that does not exist. Type: curl, dash s capital I, localhost colon eight zero eight zero, slash nope, pipe, head, dash one."),
  c('x6', "Four hundred four. The server is fine; that page is missing. A different problem."),
  c('x7', "Now start a second copy on the same port. Type: python3 -m http.server 8080 2>&1 | tail -1", "Now start a second copy on the same port. Type: python three, dash m, h t t p dot server, eight zero eight zero, two, greater than, ampersand one, pipe, tail, dash one."),
  c('x8', "Address already in use. Only one program can hold a port."),
  c('x9', "Who is listening? Type: ss -ltn sport = :8080", "Who is listening? Type: s s, dash l t n, s port, equals, colon eight zero eight zero."),
  c('x10', "The state is listen, on port eight zero eight zero. Now stop the server. Type: kill %1", "The state is listen, on port eight zero eight zero. Now stop the server. Type: kill, percent one."),
  c('x11', "Ask again. Type: curl -sS localhost:8080", "Ask again. Type: curl, dash s capital S, localhost, colon eight zero eight zero."),
  c('x12', "Failed to connect. Nothing is listening, so the service is down. That is what connection refused looks like."),
 ]),
 ('logs', [
  c('y1', "Last, the logs."), c('y2', "When a service fails, the screen often shows nothing. The reason is in its log."),
  c('y3', "Logs record each request, each error, each start and stop, with a time."),
  c('y4', "Two tools do most of the work: tail shows the end of a file, and grep finds matching lines."),
  c('y5', "Rule: do not guess. Read the log first."),
 ]),
 ('logdemo', [
  c('z1', "This log came from a real run of the same web server. Let us read it."),
  c('z2', "Show the last lines. Type: tail -n 4 server.log", "Show the last lines. Type: tail, dash n four, server dot log."),
  c('z3', "Each line has the client, the time, the request, and the result code."),
  c('z4', "Now find only the problems. Type: grep 404 server.log", "Now find only the problems. Type: grep, four oh four, server dot log."),
  c('z5', "These are the failed requests, with the reason: file not found."),
  c('z6', "Count them. Type: grep -c 404 server.log", "Count them. Type: grep, dash c, four oh four, server dot log."),
  c('z7', "Two lines: the request, and the reason it failed. That is how a log turns a vague complaint into a fact."),
 ]),
 ('method', [
  c('m1', "Put it together as one routine, in order."), c('m2', "One: is the service running?"), c('m3', "Two: is it reachable, on the right port?"),
  c('m4', "Three: are the CPU, memory, and disk exhausted?"), c('m5', "Four: what do the logs say?"), c('m6', "Work in that order, and write down what you find."),
 ]),
 ('errors', [
  c('e1', "Match the symptom to the part."), c('e2', "Everything is slow: CPU or memory. Check with p s and free."),
  c('e3', "A program vanished: out of memory. Check the logs."), c('e4', "No space left on device: disk. Check with d f and d u."),
  c('e5', "Connection refused: the service is down or not listening. Check with s s and curl."), c('e6', "Four oh four: the service is fine. The page or path is wrong."),
 ]),
 ('myths', [
  c('k1', "Watch out for four common myths."), c('k2', "Myth one: slow means the network. Often it is the CPU, memory, or disk."),
  c('k3', "Myth two: a full disk only means no new files. It can stop a database completely."),
  c('k4', "Myth three: four oh four means the server is down. It means the server answered."),
  c('k5', "Myth four: restart first, look later. A restart can erase the evidence."), c('k6', "Check, then act."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Name the six parts: CPU, memory, disk, network, services, logs."),
  c('b3', "Find the busiest process, and stop a runaway one."), c('b4', "Read memory with free, and explain available."), c('b5', "Find a full disk, and what fills it."),
  c('b6', "Tell down from missing: connection refused versus four oh four."), c('b7', "Find a failed request in a log with grep."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('j1', "Your turn, in the virtual machine you built."), c('j2', "One: run nproc and free dash h, and write down your numbers."),
  c('j3', "Two: start a yes process, find it with p s, and kill it."), c('j4', "Three: run d f on your system, and find your biggest folder with d u."),
  c('j5', "Four: start the Python web server, get a two hundred and a four oh four, then stop it and see the refusal."),
  c('j6', "Five: grep your own server log for four oh four."), c('j7', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f1', "Quick check."), c('f2', "Name the six parts of a server."), c('f3', "Which command finds the busiest process?"),
  c('f4', "What does no space left on device point to?"), c('f8', "What is the difference between connection refused and four oh four?"),
  c('f9', "Objective covered: MC02-O07.", "Objective covered: number seven, in the I T fundamentals masterclass."),
  c('f5', "Pause the video, and answer out loud."), c('f6', "Next lesson: tracing one web request."), c('f7', "Subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h4': 0.5, 'p8': 0.5, 'q6': 0.5, 'r10': 0.5, 't7': 0.5, 's6': 0.5, 'u6': 0.5, 'v12': 0.5, 'w5': 0.5, 'x12': 0.5, 'y5': 0.5, 'z7': 0.5, 'm6': 0.5, 'e6': 0.5, 'k6': 0.5, 'b8': 0.5,
         'j7': 14.0, 'f5': 10.0, 'r9': 3.0, 't5': 0.0}
CHAP = {'parts': 'The main parts', 'cpu': 'CPU', 'cpudemo': 'Live: a busy CPU', 'mem': 'Memory', 'memdemo': 'Live: memory limits', 'disk': 'Disk', 'diskdemo': 'Live: a full disk', 'svc': 'Services and ports',
        'svcdemo': 'Live: a service down', 'logs': 'Logs', 'logdemo': 'Live: read a log', 'method': 'The routine', 'errors': 'Symptoms and causes', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Fundamentals  ·  Lesson 15', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def trio(E, C, items, ids, y=520, h=230, w=540):
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def photo(path, w, h, col):
    im = Image.open(path).convert('RGB'); im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.5))
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=tuple(col)[:3] + (255,))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=20, fill=255)
    out.paste(im, (6, 6), m); return out
PHOTO = '/home/claude/academy/lesson15/assets/photo_l15_server.jpg'
PHOTO_CREDIT = 'Server farm  ·  NASA  ·  Public domain  ·  via Wikimedia Commons'
def mono(s, col, size=28):
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', size)
    im = Image.new('RGBA', (int(f.getlength(s)) + 10, size + 16), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), s, font=f, fill=tuple(col)[:3] + (255,)); return im
def chip(s, col, size=40, padx=22, pady=10):
    return badge(s, ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', size), INK, col, padx=padx, pady=pady, r=18)


def _lab(title, sub, first, badge_, steps, mono_steps=True):
    def f(C, D, dur):
        E = head(title, sub, C[first]); E.append(real(C[first] + 0.2, badge_, 1260, 286))
        E.append(Pop(card(1100, 640, ACC, '', [], 4), 100, 330, C[first]))
        n = len(steps); gap = min(120, (1035 - 345) // n); fs_t, fs_s = (30, 25) if n <= 6 else (27, 23)
        for i, (cid, t, sb, col) in enumerate(steps): E.append(Pop(card(560, gap - 12, col, t, [(sb, TXT)], fs_t, fs_s), 1260, 345 + i * gap, C[cid] + 0.2))
        return E
    return f

def trio3(E, C, items, ids, y=330, h=230, w=540): 
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def slide(title, sub, first, items, ids, chips, chip_id, take, take_id, gl):
    def f(C, D, dur):
        E = head(title, sub, C[first]); trio3(E, C, items, ids)
        x = 100
        for i, (s, col) in enumerate(chips):
            ch = chip(s, col, 36, 24, 12); E.append(Pop(ch, x, 640, C[chip_id] + i * 0.4)); x += ch.width + 22
        E.append(takeaway(take, 820, C[take_id], GOOD, 1700)); return E
    return f
def s_hook(C, D, dur):
    E = [El(T('Servers fail in patterns', 'x', 64), 100, 130, C['h1'])]
    if os.path.exists(PHOTO):
        E.append(Pop(photo(PHOTO, 740, 500, ACC), 1080, 250, C['h1']))
        E.append(El(T(PHOTO_CREDIT, 'm', 24, MUTED, maxw=740), 1080, 770, C['h1'] + 0.5, anim='fade'))
    E.append(Pop(card(900, 150, ACC, 'A server', [('A computer others depend on.', TXT)], 46, 36), 100, 250, C['h1']))
    E.append(Pop(card(900, 150, WARN, 'A few parts, clear symptoms', [('Learn the pairs, fix faster.', TXT)], 46, 36), 100, 430, C['h3']))
    bs = [badge(n, F('b', 34), INK, col, padx=26, pady=14, r=26) for n, col in [('CPU', ACC), ('Memory', VIO), ('Disk', GOOD), ('Services', WARN), ('Logs', PINK)]]
    E.append(El(T('Today, live', 'b', 32, MUTED), 100, 640, C['h4'], anim='fade'))
    bx = 100
    for i, b in enumerate(bs): E.append(Pop(b, bx, 700, C['h4'] + 0.3 + i * 0.5)); bx += b.width + 24
    E.append(takeaway('Real commands, real failures, in a safe setup.', 840, C['h4'] + 2.5, GOOD, 1600)); return E
def s_parts(C, D, dur):
    E = head('The main parts', 'What every server is made of.', C['p1'])
    it = [('CPU', 'Does the work', ACC, 'p2'), ('Memory', 'Fast workspace', VIO, 'p3'), ('Disk', 'Long-term storage', GOOD, 'p4'), ('Network', 'Connects to others', WARN, 'p5'), ('Services', 'Wait for requests', PINK, 'p6'), ('Logs', 'The diary', ACC, 'p7')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(takeaway('Each part fails in its own way.', 860, C['p8'], GOOD, 1500)); return E
s_cpu = slide('The CPU', 'It does the work.', 'q1', [('What it does', 'Runs instructions, shared by cores', ACC), ('Symptom', 'Slow, laggy, high load', WARN), ('First check', 'Who is the busiest process?', GOOD)], ['q2', 'q5', 'q6'],
              [('nproc', ACC), ('ps', VIO), ('top', GOOD)], 'q6', 'A hogging process slows everything.', 'q4', 0)
s_mem = slide('Memory', 'The fast workspace.', 's1', [('What it does', 'Holds running programs', VIO), ('Symptom', 'Swapping, slowness, killed programs', WARN), ('First check', 'free -h', GOOD)], ['s2', 's5', 's6'],
              [('free -h', VIO), ('available', GOOD), ('out of memory', BAD)], 's4', 'Out of memory: the kernel kills a program.', 's4', 0)
s_disk = slide('The disk', 'Long-term storage.', 'u1', [('What it does', 'Keeps files, databases, logs', GOOD), ('Symptom', 'No space left on device', BAD), ('First check', 'df, then du', ACC)], ['u2', 'u5', 'u6'],
               [('df -h', GOOD), ('du -sh', ACC)], 'u6', 'A full disk can stop everything.', 'u4', 0)
s_svc = slide('Services and ports', 'Programs that wait for requests.', 'w1', [('Running?', 'The program must be started', ACC), ('Listening?', 'On the right numbered port', VIO), ('Codes', '200 ok · 404 missing · 5xx failed', WARN)], ['w2', 'w3', 'w4'],
              [('ps', ACC), ('ss -ltn', VIO), ('curl -sI', GOOD)], 'w5', 'Running, listening, answering: check all three.', 'w5', 0)
s_logs = slide('Logs', 'The diary of what happened.', 'y1', [('What they hold', 'Requests, errors, starts, stops', PINK), ('Symptom', 'The screen shows nothing', WARN), ('First check', 'tail and grep', GOOD)], ['y3', 'y2', 'y4'],
               [('tail -n', PINK), ('grep', GOOD)], 'y4', 'Do not guess. Read the log first.', 'y5', 0)
RB = 'REAL RECORDING  ·  Ubuntu 24.04 terminal'
s_cpudemo = _lab('A busy CPU', 'Find the runaway, stop it.', 'r1', RB, [('r2', 'nproc', 'How many cores', ACC), ('r4', 'yes > /dev/null &', 'A program that never rests', VIO), ('r6', 'ps ... --sort=-pcpu', 'Busiest process first', GOOD), ('r7', 'yes  99%', 'One core fully used', BAD), ('r8', 'kill %1', 'Stop the runaway', WARN), ('r9', 'ps again', 'CPU is free again', GOOD)])
s_memdemo = _lab('Memory limits', 'A small cap mimics a small server.', 't1', 'REAL RECORDING  ·  memory capped with ulimit', [('t1', 'free -h', 'Total and available', ACC), ('t3', 'cat hog.py', 'Asks for 500 MB', VIO), ('t5', 'ulimit -v 200000', 'Cap this run at 200 MB', WARN), ('t6', 'MemoryError', 'Asked for more than allowed', BAD), ('t7', 'Real server', 'The kernel would kill it', PINK)])
s_diskdemo = _lab('A full disk', 'Fill, find, free.', 'v1', 'REAL RECORDING  ·  10 MB practice disk', [('v2', 'df -h data', 'Size and use', ACC), ('v4', 'dd ... count=20', 'Write 20 MB into 10 MB', VIO), ('v5', 'No space left', 'The disk is full', BAD), ('v8', 'du -sh data/*', 'Find the culprit', WARN), ('v10', 'rm data/big.bin', 'Free the space', GOOD), ('v11', 'df -h data', 'Back to 0%', GOOD)])
s_svcdemo = _lab('A service goes down', 'Running, listening, answering.', 'x1', RB, [('x2', 'http.server 8080 &', 'Start a tiny web server', ACC), ('x3', 'curl -sI', '200 OK: it is up', GOOD), ('x5', 'curl .../nope', '404: page missing', WARN), ('x7', 'second server', 'Address already in use', BAD), ('x9', 'ss -ltn sport', 'Who holds the port', VIO), ('x11', 'after kill', 'Failed to connect', BAD)])
s_logdemo = _lab('Read a log', 'tail and grep.', 'z1', 'REAL RECORDING  ·  log from a real run', [('z2', 'tail -n 4', 'The last lines', ACC), ('z3', 'client · time · request', 'Each line, decoded', VIO), ('z4', 'grep 404', 'Only the failures', WARN), ('z5', 'File not found', 'The reason is written down', GOOD), ('z6', 'grep -c 404', 'Count them', ACC)])
def s_method(C, D, dur):
    E = head('The routine', 'Four questions, in order.', C['m1'])
    it = [('1  Running?', 'Is the service started?', ACC, 'm2'), ('2  Reachable?', 'Right port, answering?', VIO, 'm3'), ('3  Resources?', 'CPU, memory, disk', WARN, 'm4'), ('4  Logs?', 'What do they say?', GOOD, 'm5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(410, 215, col, n, [(s, TXT)], 40, 30, True), 100 + i * 437, 340, C[cid]))
    E.append(takeaway('Same order every time. Write down what you find.', 700, C['m6'], GOOD, 1700)); return E
def s_errors(C, D, dur):
    E = head('Symptoms and causes', 'Match the symptom to the part.', C['e1'])
    it = [('Everything is slow', 'CPU or memory: ps, free', 'e2', ACC), ('A program vanished', 'Out of memory: logs', 'e3', VIO), ('No space left on device', 'Disk: df, du', 'e4', BAD), ('Connection refused', 'Service down: ss, curl', 'e5', WARN), ('404 Not Found', 'Server fine, wrong path', 'e6', GOOD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 130
        E.append(Pop(card(900, 112, col, '', [(a, TXT)], 4, 34), 100, y, C[cid])); E.append(El(T('→', 'x', 50, MUTED), 1020, y + 25, C[cid] + 0.3, anim='fade')); E.append(Pop(card(700, 112, col, '', [(b, TXT)], 4, 32), 1100, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['k1'])
    it = [('Myth: slow means the network', 'Reality: often CPU, memory, disk.', WARN, 'k2'), ('Myth: full disk = no new files', 'Reality: databases can stop.', BAD, 'k3'),
          ('Myth: 404 means server down', 'Reality: it answered.', VIO, 'k4'), ('Myth: restart first', 'Reality: it can erase evidence.', GOOD, 'k5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Check, then act.', 860, C['k6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['b1'])
    items = [('Names the six parts', 'b2'), ('Finds and stops a runaway', 'b3'), ('Reads free, explains available', 'b4'), ('Finds a full disk and its cause', 'b5'), ('Refused versus 404', 'b6'), ('Finds a failure with grep', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid]))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['j1'])
    it = [('1  nproc, free', 'Write down your numbers', ACC, 'j2'), ('2  yes', 'Find it with ps, kill it', VIO, 'j3'), ('3  df, du', 'Biggest folder', WARN, 'j4'), ('4  http.server', '200, 404, stop, refused', GOOD, 'j5'), ('5  grep', 'Find 404 in your log', PINK, 'j6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['j7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f1'])]
    qs = [('Name the six parts of a server.', 'f2'), ('Which command finds the busiest process?', 'f3'), ('What does no space left on device point to?', 'f4'), ('Connection refused versus 404?', 'f8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f9'] + 0.2))
    E.append(El(T('Objective covered: MC02-O07  ·  server parts and failure symptoms', 'b', 28, TXT, maxw=960), 220, 748, C['f9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f5']))
    E.append(El(T('Next: tracing one web request', 'x', 46, ACC, maxw=1600), 100, 960, C['f6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f7']))
    return E
FN = dict(hook=s_hook, parts=s_parts, cpu=s_cpu, cpudemo=s_cpudemo, mem=s_mem, memdemo=s_memdemo, disk=s_disk, diskdemo=s_diskdemo, svc=s_svc, svcdemo=s_svcdemo, logs=s_logs, logdemo=s_logdemo,
          method=s_method, errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(parts=('server', ACC), cpu=('gear', ACC), cpudemo=('eye', GOOD), mem=('grid', VIO), memdemo=('eye', GOOD), disk=('db', GOOD), diskdemo=('eye', GOOD), svc=('link', WARN), svcdemo=('eye', GOOD),
           logs=('doc', PINK), logdemo=('eye', GOOD), method=('steps', ACC), errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])

HL = {
 'cpudemo': [('r3', 1, 1, 4, 34, '2 cores'), ('r7', 2, 1, 4, 250, '99% of one CPU'), ('r10', 1, 3, 4, 270, 'yes is gone')],
 'memdemo': [('t2', 2, 1, 4, 150, ''), ('t2', 4, 1, 60, 150, 'usable memory'), ('t4', 1, 1, 4, 540, '500 MB'), ('t6', 1, 1, 4, 180, 'too big for the cap')],
 'diskdemo': [('v3', 2, 1, 4, 850, ''), ('v5', 1, 1, 4, 875, ''), ('v7', 2, 1, 497, 568, 'full'), ('v9', 1, 1, 4, 380, '10M file'), ('v12', 2, 1, 528, 562, '0% used')],
 'svcdemo': [('x4', 1, 1, 4, 235, 'service is up'), ('x6', 1, 1, 4, 415, 'page missing'), ('x8', 1, 1, 4, 650, ''), ('x10', 2, 1, 4, 890, ''), ('x12', 1, 2, 4, 1070, '')],
 'logdemo': [('z3', 1, 1, 4, 1040, ''), ('z5', 2, 1, 4, 1040, ''), ('z7', 1, 1, 4, 22, 'only 2')],
}
