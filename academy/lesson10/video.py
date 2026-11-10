import sys; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 10  ·  DEVOPS BOOTCAMP'
def _say(cap):
    s = cap.replace('CPU', 'C P U').replace('PID', 'P I D').replace('RAM', 'ram')
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
from PIL import ImageFont
MONO = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 28)

SCENES = [
 ('hook', [
  c('h1', "Your server is slow."), c('h2', "Is it the processor, the memory, or the disk?"), c('h3', "Guessing wastes hours."),
  c('h4', "Today you learn what each part does, and how programs share them."),
  c('h5', "That is processors, memory, storage, processes, threads, and resource contention."),
 ]),
 ('cpu', [
  c('c1', "First, the CPU."), c('c2', "The CPU runs instructions, one tiny step at a time."),
  c('c3', "Modern ones have several cores, and each core works on one thing at a time."),
  c('c4', "More cores means more work at the same moment."), c('c5', "A busy CPU means work is waiting for its turn."),
 ]),
 ('memory', [
  c('m1', "Next, memory, also called RAM."), c('m2', "Memory holds what programs are using right now."),
  c('m3', "It is very fast, but it is temporary."), c('m4', "Switch off the machine, and memory is emptied."),
  c('m5', "When memory runs out, the system slows down badly, or stops programs to survive."),
 ]),
 ('storage', [
  c('s1', "Then storage, the disk."), c('s2', "Storage keeps data permanently: files, programs, and databases."),
  c('s3', "It is much larger than memory, and much slower."), c('s4', "Switch off the machine, and the data is still there."),
  c('s5', "When storage fills up, programs cannot save, and logs cannot be written."),
  c('s6', "Remember the trade: memory is fast and temporary, storage is slower and lasting."),
 ]),
 ('process', [
  c('p1', "Now, processes."), c('p2', "A program is a file, waiting on disk. A process is that program, running."),
  c('p3', "Open the same program twice, and you get two processes."), c('p4', "Each process has its own identity number, called a PID."),
  c('p5', "Each has its own memory, kept separate from the others."), c('p6', "The operating system decides which process gets the CPU, and for how long."),
 ]),
 ('threads', [
  c('t1', "Inside a process, there can be threads."), c('t2', "A thread is one line of work, inside a process."),
  c('t3', "All the threads of a process share its memory."), c('t4', "That lets one program do many things at once, like serving many customers."),
  c('t5', "But shared memory means the program must manage its threads carefully."),
 ]),
 ('contention', [
  c('r1', "Now the key idea: resource contention."), c('r2', "Contention is when several processes want the same resource, at the same time."),
  c('r3', "Two cores, and four busy programs: each gets about half of a core."), c('r4', "Nothing is broken. Everything is just slower."),
  c('r5', "The system switches between them so quickly that they seem to run together."), c('r6', "Memory has contention too. So does the disk."),
 ]),
 ('demo', [
  c('e1', "Now let us see this for real, in a disposable Linux sandbox."), c('e2', "These outputs are real captures, not an illustration."),
  c('e3', "First: this machine has two processors, and about eight gigabytes of memory."),
  c('e4', "Next, we start four programs that do nothing but calculate."), c('e5', "Look at the CPU column. Four processes share two cores, so each gets about fifty percent."),
  c('e6', "That is contention, measured."), c('e7', "Last: one Python process, with five threads. That is the main thread, plus four more."),
  c('e8', "One process, many threads, all sharing its memory."),
 ]),
 ('symptoms', [
  c('k1', "Why does this matter for DevOps?"), c('k2', "Because slow has three common causes."),
  c('k3', "CPU contention: processes wait for processor time."), c('k4', "Memory shortage: the system slows down, or stops programs."),
  c('k5', "Full storage: writes fail, and logs stop."), c('k6', "Measure first, then fix."),
 ]),
 ('myths', [
  c('w1', "Watch out for four common myths."),
  c('w2', "Myth one: more memory makes everything faster. In fact, it helps only when memory was the shortage."),
  c('w3', "Myth two: memory and storage are the same. In fact, one is fast and temporary, the other slower and lasting."),
  c('w4', "Myth three: a program and a process are the same. In fact, a process is a program that is running."),
  c('w5', "Myth four: a busy CPU is always a problem. In fact, work waiting for the CPU is the problem."), c('w6', "Measure, then decide."),
 ]),
 ('rubric', [
  c('u1', "Here is how you check your own understanding."), c('u2', "Imagine a friend says: my server is slow."),
  c('u3', "Explain what the CPU, memory, and storage each do."), c('u4', "Explain a process, and a thread."),
  c('u5', "Explain contention, with an example and numbers."), c('u6', "Say which resource you would measure first, and why."),
  c('u7', "Check yourself on six points."), c('u8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('y1', "Your turn."), c('y2', "Take any computer you can reach, and find three things."),
  c('y3', "One: how many processors it has, and how much memory."), c('y4', "Two: which process is using the most CPU right now."),
  c('y5', "On Windows, Task Manager shows both. On Linux, the commands from the demo do."),
  c('y6', "Three: mark yourself on the rubric."), c('y7', "Pause the video, and do it now."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "What is the difference between memory and storage?"), c('z3', "What is the difference between a process and a thread?"),
  c('z4', "What is resource contention?"), c('z8', "Name three common causes of a slow server."),
  c('z9', "Objective covered: MC02-O02.", "Objective covered: number two, in the I T fundamentals masterclass."),
  c('z5', "Pause the video, and explain contention with your own example."), c('z6', "Next lesson: the command line and the filesystem."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h5': 0.5, 'c5': 0.5, 'm5': 0.5, 's6': 0.5, 'p6': 0.5, 't5': 0.5, 'r6': 0.5, 'e8': 0.5, 'k6': 0.5, 'w6': 0.5, 'u8': 0.5, 'y7': 12.0, 'z5': 10.0}
CHAP = {'cpu': 'The CPU', 'memory': 'Memory', 'storage': 'Storage', 'process': 'Processes', 'threads': 'Threads', 'contention': 'Resource contention', 'demo': 'Real demo',
        'symptoms': 'Causes of slow', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Fundamentals  ·  Lesson 10', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def defn(E, t, col, text, y=330): E.append(Pop(card(1720, 130, col, 'Definition', [(text, TXT)], 36, 38), 100, y, t))
def trio(E, C, items, ids, col=None, y=520, h=230, w=540):
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))

def s_hook(C, D, dur):
    E = [El(T('Why is it slow?', 'x', 64), 100, 130, C['h1']), ill(C['h1'], 1400, 130)]
    E.append(Pop(card(1720, 120, WARN, 'Your server is slow', [], 46), 100, 260, C['h1']))
    for i, (n, s, col) in enumerate([('CPU', 'Calculates', ACC), ('Memory', 'Holds work right now', GOOD), ('Storage', 'Keeps data', WARN)]):
        E.append(Pop(card(480, 220, col, n, [(s, TXT)], 46, 34), 100 + i * 620, 440, C['h2'] + i * 0.5))
    bs = [badge(n, F('b', 36), INK, col, padx=28, pady=14, r=26) for n, col in [('Processes', VIO), ('Threads', PINK), ('Contention', BAD)]]
    gap = 50; bx = 100 + (1720 - (sum(b.width for b in bs) + gap * 2)) / 2
    E.append(El(T('And how programs share them', 'b', 32, MUTED), bx, 730, C['h4'], anim='fade'))
    for i, b in enumerate(bs): E.append(Pop(b, bx, 790, C['h4'] + 0.3 + i * 0.6)); bx += b.width + gap
    E.append(takeaway('Measure first. Then fix.', 920, C['h5'] + 0.4, GOOD, 1600))
    return E
def s_cpu(C, D, dur):
    E = head('The CPU', 'It does the calculating.', C['c1']); defn(E, C['c2'], ACC, 'Runs instructions, one tiny step at a time.')
    trio(E, C, [('One core', 'Works on one thing at a time', ACC), ('Several cores', 'Several things at once', GOOD), ('A busy CPU', 'Work is waiting its turn', WARN)], ['c3', 'c4', 'c5'])
    E.append(takeaway('More cores, more work at the same moment.', 860, C['c5'] + 0.4, GOOD, 1600)); return E
def s_memory(C, D, dur):
    E = head('Memory (RAM)', 'What programs use right now.', C['m1']); defn(E, C['m2'], GOOD, 'Holds the data of running programs.')
    trio(E, C, [('Very fast', 'Programs can use it instantly', GOOD), ('Temporary', 'Emptied when power goes off', WARN), ('Limited', 'When it runs out, trouble starts', BAD)], ['m3', 'm4', 'm5'])
    E.append(takeaway('Fast, temporary, and never enough.', 860, C['m5'] + 0.4, GOOD, 1600)); return E
def s_storage(C, D, dur):
    E = head('Storage', 'Where data stays.', C['s1']); defn(E, C['s2'], WARN, 'Keeps files, programs and databases permanently.')
    trio(E, C, [('Large', 'Far bigger than memory', ACC), ('Slower', 'Much slower than memory', WARN), ('Lasting', 'Data survives power off', GOOD)], ['s3', 's3', 's4'])
    E.append(Pop(badge('When it fills: saves and logs fail', F('b', 36), INK, BAD, padx=28, pady=14, r=26), 100, 800, C['s5']))
    E.append(takeaway('Memory: fast and temporary. Storage: slower and lasting.', 930, C['s6'], GOOD, 1700, 36)); return E
def s_process(C, D, dur):
    E = head('Processes', 'A program, running.', C['p1'])
    for i, (n, s, col, cid) in enumerate([('Program', 'A file waiting on disk', ACC, 'p2'), ('Process', 'That program, running', VIO, 'p2'), ('Its own identity', 'A number called the PID', WARN, 'p4')]):
        E.append(Pop(card(480, 220, col, n, [(s, TXT)], 44, 34), 100 + i * 620, 370, C[cid] + (0.8 if i == 1 else 0)))
        if i == 1: E.append(A([(100 + 620 - 140, 480), (100 + 620 - 20, 480)], C['p2'] + 0.8, MUTED, 6, 22))
        if i == 2: E.append(A([(100 + 1240 - 140, 480), (100 + 1240 - 20, 480)], C['p4'], MUTED, 6, 22))
    E.append(Pop(card(840, 170, GOOD, 'Its own memory', [('Kept separate from other processes.', TXT)], 40, 32), 100, 650, C['p5']))
    E.append(Pop(card(840, 170, PINK, 'The operating system schedules', [('It decides who gets the CPU, and for how long.', TXT)], 38, 30), 980, 650, C['p6']))
    E.append(takeaway('Two copies of a program are two processes.', 900, C['p6'] + 0.4, GOOD, 1600, 36)); return E
def s_threads(C, D, dur):
    E = head('Threads', 'Lines of work inside a process.', C['t1'])
    E.append(Pop(card(1720, 130, VIO, 'One process', [('One PID, one block of memory.', TXT)], 40, 34), 100, 330, C['t2']))
    for i in range(4): E.append(Pop(card(400, 190, PINK, f'Thread {i + 1}', [('One line of work', TXT)], 40, 30), 100 + i * 440, 520, C['t3'] + i * 0.3))
    E.append(Pop(badge('All threads share the process memory', F('b', 36), INK, GOOD, padx=28, pady=14, r=26), 100, 770, C['t3'] + 1.4))
    E.append(takeaway('Powerful, and risky if managed badly.', 900, C['t5'], WARN, 1600)); return E
def s_contention(C, D, dur):
    E = head('Resource contention', 'Many wanting one resource.', C['r1']); E.append(ill(C['r3'], 1400, 130))
    E.append(Pop(card(840, 190, ACC, 'Two cores', [('The resource.', TXT)], 44, 36), 100, 330, C['r3']))
    E.append(Pop(card(840, 190, WARN, 'Four busy programs', [('All want it now.', TXT)], 44, 36), 980, 330, C['r3'] + 0.5))
    E.append(Pop(card(1720, 170, GOOD, 'Each gets about half a core', [('Nothing is broken. Everything is slower.', TXT)], 46, 38), 100, 590, C['r4']))
    for i, (n, col) in enumerate([('CPU', ACC), ('Memory', GOOD), ('Disk', WARN)]):
        pass
    E.append(El(T('It applies to', 'b', 30, MUTED), 100, 810, C['r6'], anim='fade'))
    bx = 100
    for i, (n, col) in enumerate([('CPU', ACC), ('Memory', GOOD), ('Disk', WARN)]):
        b = badge(n, F('x', 40), INK, col, padx=28, pady=14, r=26); E.append(Pop(b, bx, 860, C['r6'] + 0.3 + i * 0.5)); bx += b.width + 30
    return E
def mono(s, col):
    im = Image.new('RGBA', (int(MONO.getlength(s)) + 10, 44), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), s, font=MONO, fill=tuple(col)[:3] + (255,)); return im
def s_demo(C, D, dur):
    E = head('Real demo', 'CPU, memory, processes, threads.', C['e1']); E.append(real(C['e2'], 'REAL OUTPUT  ·  captured in a Linux sandbox', 1260, 296))
    E.append(Pop(card(1100, 640, ACC, '', [], 4), 100, 330, C['e1'] + 0.3))
    blocks = [('e3', [('$ nproc', ACC), ('2', TXT), ('$ free -m | head -n 2', ACC), ('              total   used   free', TXT), ('Mem:           8022    361   7671', TXT)]),
              ('e5', [('$ ps -eo pid,pcpu,nlwp,comm --sort=-pcpu | head -n 5', ACC), ('  PID %CPU NLWP COMMAND', TXT), ('  151 50.1    1 python3', GOOD), ('  153 49.6    1 python3', GOOD), ('  158 48.3    1 python3', GOOD), ('  159 48.1    1 python3', GOOD)]),
              ('e7', [('$ ps -o pid,nlwp,comm -C python3', ACC), ('  PID NLWP COMMAND', TXT), ('  189    5 python3', WARN)])]
    y = 365; ys = []
    for cid, lines in blocks:
        ys.append(y)
        for j, (s, col) in enumerate(lines): E.append(El(mono(s, col), 130, y + j * 36, C[cid] + j * 0.4, anim='fade'))
        y += len(lines) * 36 + 24
    ann = [('Resources', '2 cores, about 8 GB memory', ACC, 'e3', ys[0]), ('Contention', 'four processes, two cores: about 50% each', GOOD, 'e5', ys[1]), ('Threads', 'one process (PID), five threads', WARN, 'e7', ys[2])]
    for n, s, col, cid, yy in ann: E.append(Pop(card(560, 110, col, '', [(n + ': ' + s, TXT)], 4, 26), 1260, yy, C[cid]))
    return E
def s_symptoms(C, D, dur):
    E = head('Causes of slow', 'Three suspects, one method.', C['k1'])
    it = [('CPU contention', 'Processes wait for processor time', ACC, 'k3'), ('Memory shortage', 'The system slows, or stops programs', GOOD, 'k4'), ('Full storage', 'Writes fail, and logs stop', WARN, 'k5'), ('The method', 'Measure first, then fix', PINK, 'k6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(840, 190, col, n, [(s, TXT)], 40, 30), 100 + (i % 2) * 880, 330 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Do not guess. Look at the numbers.', 860, C['k6'] + 0.4, GOOD, 1500)); return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['w1'])
    it = [('Myth: more memory is always faster', 'Reality: only if memory was short.', WARN, 'w2'), ('Myth: memory and storage are the same', 'Reality: fast and temporary, or slower and lasting.', BAD, 'w3'),
          ('Myth: a program is a process', 'Reality: a process is a program running.', VIO, 'w4'), ('Myth: a busy CPU is always bad', 'Reality: work waiting for the CPU is bad.', GOOD, 'w5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Measure, then decide.', 860, C['w6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['u1'])
    items = [('Explains what the CPU does', 'u3'), ('Separates memory from storage', 'u3'), ('Explains a process', 'u4'), ('Explains a thread', 'u4'), ('Explains contention with numbers', 'u5'), ('Names the first resource, and why', 'u6')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid] + (i % 2) * 0.5))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + (i % 2) * 0.5 + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['u8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Measure a real computer.', C['y1'])
    E.append(Pop(card(1720, 150, WARN, 'Any computer you can reach', [('Windows: Task Manager.  Linux: the demo commands.', TXT)], 46, 36), 100, 330, C['y2']))
    it = [('1  Count', 'Processors, and memory', ACC, 'y3'), ('2  Find', 'The process using most CPU', VIO, 'y4'), ('3  Check', 'Mark yourself on the rubric', GOOD, 'y6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 270, col, n, [(s, TXT)], 44, 32, True), 100 + i * 590, 540, C[cid]))
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['y7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    qs = [('What is the difference between memory and storage?', 'z2'), ('What is the difference between a process and a thread?', 'z3'), ('What is resource contention?', 'z4'), ('Name three common causes of a slow server.', 'z8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 32, maxw=930), 190, 280 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['z9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC02-O02  ·  CPU, memory, processes', 'b', 30, TXT, maxw=960), 220, 748, C['z9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  explain contention', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['z5']))
    E.append(El(T('Next: the command line and the filesystem', 'x', 46, ACC, maxw=1500), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['z7']))
    return E
FN = dict(hook=s_hook, cpu=s_cpu, memory=s_memory, storage=s_storage, process=s_process, threads=s_threads, contention=s_contention, demo=s_demo, symptoms=s_symptoms, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(cpu=('gear', ACC), memory=('grid', GOOD), storage=('db', WARN), process=('steps', VIO), threads=('branch', PINK), contention=('swap', BAD), demo=('eye', GOOD), symptoms=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
