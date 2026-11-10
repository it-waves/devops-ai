import sys, re; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 12  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps
MONO = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 28)
_SP = {'VM': 'V M', 'VMs': 'V Ms', 'KVM': 'K V M', 'OS': 'O S', 'CPU': 'C P U', 'unshare': 'un share'}
def _say(cap):
    s = re.sub(r'\b(' + '|'.join(_SP) + r')\b', lambda m: _SP[m.group(1)], cap)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)


SCENES = [
 ('hook', [
  c('h1', "One physical server, and ten applications."), c('h2', "If they all share everything, one crash can take them all down."),
  c('h3', "Virtualization and containers keep them apart."),
  c('h4', "Today: the problem, virtual machines, containers, and how they differ."),
 ]),
 ('problem', [
  c('a1', "First, the problem."), c('a2', "A physical server is expensive, and it often sits mostly idle."),
  c('a3', "Put every application on it, and they fight over the same libraries and settings."),
  c('a4', "So we need isolation: separate spaces on shared hardware."),
 ]),
 ('vm', [
  c('v1', "Solution one: the virtual machine."), c('v2', "A hypervisor is software that splits one physical machine into several virtual ones."),
  c('v3', "Each virtual machine gets its own virtual processor, memory, and disk."),
  c('v4', "And its own complete operating system, with its own kernel."),
  c('v5', "Strong isolation, but each one is heavy, and slower to start."),
 ]),
 ('kernel', [
  c('k1', "One word matters here: the kernel."), c('k2', "The kernel is the core of the operating system, and it talks to the hardware."),
  c('k3', "A virtual machine has its own kernel."), c('k4', "Remember this, because it is the key difference."),
 ]),
 ('container', [
  c('c1', "Solution two: the container."), c('c2', "A container is an isolated process, with its own view of files, processes, and network."),
  c('c3', "Containers share the host's kernel."), c('c4', "So there is no extra operating system to boot."),
  c('c5', "They are light, and often start in seconds, but the isolation is thinner than a virtual machine."),
 ]),
 ('compare', [
  c('m1', "Let us compare them."), c('m2', "A virtual machine has its own kernel. A container shares the host's."),
  c('m3', "Virtual machines are heavier, and slower to start."), c('m4', "Containers are lighter, and faster."),
  c('m5', "Virtual machines isolate more strongly. Containers isolate less."), c('m6', "Neither is better. They solve different problems."),
 ]),
 ('demo', [
  c('e1', "Now let us see isolation for real, in a disposable Linux sandbox."), c('e2', "These outputs are real captures, not an illustration."),
  c('e3', "First: this machine is called vm, and runs one kernel, version six point eighteen."),
  c('e4', "We count its running processes: sixty-seven lines."),
  c('e5', "Now the unshare command starts a new, isolated space, and renames the host to box."),
  c('e6', "Inside: the host name is box, only four lines of processes are visible, and the kernel is the same one."),
  c('e7', "Back outside, the host name is still vm."), c('e8', "Isolation, without a second kernel. That is the idea behind containers."),
 ]),
 ('tools', [
  c('t1', "These ideas are real tools."), c('t2', "Virtual machines run on a hypervisor, such as KVM or VirtualBox."),
  c('t3', "Containers are run by a container runtime, and Docker made them popular."), c('t4', "Later in the bootcamp, we build and run containers ourselves."),
 ]),
 ('choose', [
  c('o1', "So when do you use which?"), c('o2', "Need a different operating system, or strong isolation? Use a virtual machine."),
  c('o3', "Need many small, fast, identical services? Use containers."), c('o4', "In the cloud, containers often run inside virtual machines."),
  c('o5', "Choose by the problem."),
 ]),
 ('myths', [
  c('w1', "Watch out for four common myths."),
  c('w2', "Myth one: a container is a small virtual machine. In fact, it is an isolated process, sharing the host kernel."),
  c('w3', "Myth two: containers are always more secure. In fact, they isolate less than virtual machines."),
  c('w4', "Myth three: virtual machines are obsolete. In fact, they are everywhere, and containers often run on them."),
  c('w5', "Myth four: Docker and a container are the same. In fact, Docker is one tool that runs containers."), c('w6', "Know the difference, then choose."),
 ]),
 ('rubric', [
  c('r1', "Here is how you check your own understanding."), c('r2', "Imagine a colleague asks: virtual machine or container?"),
  c('r3', "Explain why we need isolation."), c('r4', "Explain a hypervisor, and a virtual machine."), c('r5', "Explain the kernel."),
  c('r6', "Explain a container."), c('r7', "Compare the two on four points."), c('r8', "Choose one for a scenario, and say why."), c('r9', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('y1', "Your turn."), c('y2', "On paper, draw a table with four rows: kernel, size, start time, and isolation."),
  c('y3', "One: fill it in for virtual machines and for containers, from memory."),
  c('y4', "Two: imagine hosting a website made of twenty small services."), c('y5', "Three: choose one approach, and defend it in two sentences."),
  c('y6', "Mark yourself on the rubric."), c('y7', "Pause the video, and do it now."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "What does a hypervisor do?"), c('z3', "What is the kernel?"),
  c('z4', "Why are containers lighter than virtual machines?"), c('z8', "When would you choose a virtual machine?"),
  c('z9', "Objective covered: MC02-O04.", "Objective covered: number four, in the I T fundamentals masterclass."),
  c('z5', "Pause the video, and compare them out loud."), c('z6', "Next lesson: your own Linux virtual machine."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'h4': 0.5, 'a4': 0.5, 'v5': 0.5, 'k4': 0.5, 'c5': 0.5, 'm6': 0.5, 'e8': 0.5, 't4': 0.5, 'o5': 0.5, 'w6': 0.5, 'r9': 0.5, 'y7': 12.0, 'z5': 10.0}
CHAP = {'problem': 'The problem', 'vm': 'Virtual machines', 'kernel': 'The kernel', 'container': 'Containers', 'compare': 'VM vs container', 'demo': 'Real demo', 'tools': 'Real tools',
        'choose': 'Which to use', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Fundamentals  ·  Lesson 12', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def defn(E, t, col, text, y=330): E.append(Pop(card(1720, 130, col, 'Definition', [(text, TXT)], 36, 38), 100, y, t))
def trio(E, C, items, ids, y=520, h=230, w=540):
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def photo(path, w, h, col):
    im = Image.open(path).convert('RGB'); im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.5))
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=tuple(col)[:3] + (255,))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=20, fill=255)
    out.paste(im, (6, 6), m); return out
PHOTO = '/home/claude/academy/lesson12/assets/photo_l12_containers.jpg'

def s_hook(C, D, dur):
    E = [El(T('One server, ten apps', 'x', 64), 100, 130, C['h1'])]
    E.append(Pop(photo(PHOTO, 740, 500, ACC), 1080, 250, C['h1']))
    E.append(El(T('Photo: Igor Ovsyannykov  ·  CC0  ·  via Wikimedia Commons', 'm', 24, MUTED, maxw=740), 1080, 770, C['h1'] + 0.5, anim='fade'))
    E.append(Pop(card(900, 190, WARN, 'One physical server', [('Ten applications on it.', TXT)], 50, 36), 100, 250, C['h1']))
    E.append(Pop(card(900, 190, BAD, 'One crash', [('Can take them all down.', TXT)], 50, 36), 100, 480, C['h2']))
    bs = [badge(n, F('b', 34), INK, col, padx=26, pady=14, r=26) for n, col in [('Problem', WARN), ('Virtual machines', ACC), ('Containers', GOOD)]]
    E.append(El(T('Today', 'b', 32, MUTED), 100, 740, C['h4'], anim='fade'))
    bx = 100
    for i, b in enumerate(bs): E.append(Pop(b, bx, 800, C['h4'] + 0.3 + i * 0.6)); bx += b.width + 30
    E.append(takeaway('Keep them apart.', 930, C['h4'] + 1.2, GOOD, 1600)); return E
def s_problem(C, D, dur):
    E = head('The problem', 'Shared hardware, shared trouble.', C['a1'])
    trio(E, C, [('One server', 'Expensive, often idle', ACC), ('Many apps', 'All on the same machine', WARN), ('Conflicts', 'Same libraries, same settings', BAD)], ['a2', 'a3', 'a3'], y=380, h=260)
    E.append(Pop(badge('We need isolation', F('x', 52), INK, GOOD, padx=34, pady=18, r=32), 100, 740, C['a4']))
    E.append(takeaway('Separate spaces on shared hardware.', 900, C['a4'] + 0.6, GOOD, 1600)); return E
def s_vm(C, D, dur):
    E = head('Virtual machines', 'A whole computer, in software.', C['v1'])
    for i in range(3):
        E.append(Pop(card(560, 300, ACC, f'Virtual machine {i + 1}', [('Its own virtual CPU, memory, disk', TXT), ('Its own OS and kernel', GOOD)], 38, 30), 100 + i * 580, 330, C['v3'] + i * 0.3))
    E.append(Pop(card(1720, 100, VIO, 'Hypervisor', [], 44), 100, 660, C['v2']))
    E.append(Pop(card(1720, 100, WARN, 'Physical hardware', [], 44), 100, 780, C['v2'] - 0.01))
    E.append(takeaway('Strong isolation, but heavy.', 930, C['v5'], WARN, 1600)); return E
def s_kernel(C, D, dur):
    E = head('The kernel', 'The core of the operating system.', C['k1']); defn(E, C['k2'], WARN, 'Manages the hardware: processor, memory, disks.')
    trio(E, C, [('Kernel', 'Talks to the hardware', WARN), ('Virtual machine', 'Has its own kernel', ACC), ('Remember', 'This is the key difference', GOOD)], ['k2', 'k3', 'k4'])
    E.append(takeaway('Own kernel, or shared kernel.', 860, C['k4'] + 0.4, GOOD, 1600)); return E
def s_container(C, D, dur):
    E = head('Containers', 'Isolated processes, one shared kernel.', C['c1'])
    for i in range(3):
        E.append(Pop(card(560, 200, GOOD, f'Container {i + 1}', [('App and its files', TXT)], 38, 30), 100 + i * 580, 330, C['c2'] + i * 0.3))
    E.append(Pop(card(1720, 90, VIO, 'Container runtime', [], 40), 100, 560, C['c2'] + 1.0))
    E.append(Pop(card(1720, 110, WARN, 'One shared host kernel', [], 44), 100, 670, C['c3']))
    E.append(Pop(card(1720, 90, MUTED, 'Physical hardware', [], 40), 100, 800, C['c4']))
    E.append(takeaway('Light, but isolated less.', 930, C['c5'], GOOD, 1600)); return E
def s_compare(C, D, dur):
    E = head('VM vs container', 'Same goal, different trade.', C['m1'])
    bv = badge('Virtual machine', F('b', 34), INK, ACC, padx=28, pady=12, r=26); bc = badge('Container', F('b', 34), INK, GOOD, padx=28, pady=12, r=26)
    E.append(Pop(bv, 520 + (640 - bv.width) // 2, 300, C['m1'] + 0.5)); E.append(Pop(bc, 1180 + (640 - bc.width) // 2, 300, C['m1'] + 0.8))
    rows = [('Kernel', 'Its own', 'Shares the host kernel', WARN, 'm2'), ('Size', 'Heavy', 'Light', VIO, 'm3'), ('Start', 'Slower', 'Faster', PINK, 'm4'), ('Isolation', 'Stronger', 'Thinner', BAD, 'm5')]
    for i, (a, b, c2, col, cid) in enumerate(rows):
        y = 405 + i * 125
        E.append(Pop(card(400, 105, col, a, [], 44), 100, y, C[cid])); E.append(Pop(card(640, 105, ACC, '', [(b, TXT)], 4, 38), 520, y, C[cid] + 0.3)); E.append(Pop(card(640, 105, GOOD, '', [(c2, TXT)], 4, 38), 1180, y, C[cid] + 0.6))
    E.append(takeaway('Neither is better. Different problems.', 930, C['m6'], GOOD, 1600)); return E
def mono(s, col):
    im = Image.new('RGBA', (int(MONO.getlength(s)) + 10, 44), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), s, font=MONO, fill=tuple(col)[:3] + (255,)); return im
def s_demo(C, D, dur):
    E = head('Real demo', 'Isolation without a second kernel.', C['e1']); E.append(real(C['e2'], 'REAL OUTPUT  ·  captured in a Linux sandbox', 1260, 296))
    E.append(Pop(card(1100, 640, ACC, '', [], 4), 100, 330, C['e1'] + 0.3))
    blocks = [('e3', [('$ hostname', ACC), ('vm', TXT), ('$ uname -r', ACC), ('6.18.44-fc-v338', TXT)], 20),
              ('e4', [('$ ps -e | wc -l', ACC), ('67', TXT)], 20),
              ('e5', [('$ unshare --uts --pid --fork --mount-proc \\', ACC), ('    sh -c "hostname box; hostname; ps -e | wc -l; uname -r"', ACC)], 0),
              ('e6', [('box', GOOD), ('4', GOOD), ('6.18.44-fc-v338', GOOD)], 20),
              ('e7', [('$ hostname', ACC), ('vm', TXT)], 20)]
    y = 365; ys = []
    for cid, lines, gap in blocks:
        ys.append(y)
        for j, (s, col) in enumerate(lines): E.append(El(mono(s, col), 130, y + j * 36, C[cid] + j * 0.4, anim='fade'))
        y += len(lines) * 36 + gap
    ann = [('Outside', 'host vm, one kernel', ACC, 'e3', ys[0]), ('Outside', '67 process lines', VIO, 'e4', ys[1]), ('Inside', 'host box, 4 lines, same kernel', GOOD, 'e6', ys[3]), ('Outside again', 'host is still vm', WARN, 'e7', ys[4])]
    for n, s, col, cid, yy in ann: E.append(Pop(card(560, 100, col, '', [(n + ': ' + s, TXT)], 4, 26), 1260, yy, C[cid]))
    return E
def s_tools(C, D, dur):
    E = head('Real tools', 'Names you will meet.', C['t1'])
    E.append(Pop(card(840, 300, ACC, 'Virtual machines', [('Run on a hypervisor: KVM, VirtualBox', TXT)], 46, 34), 100, 340, C['t2']))
    E.append(Pop(card(840, 300, GOOD, 'Containers', [('Run by a container runtime', TXT), ('Docker made them popular', TXT)], 46, 34), 980, 340, C['t3']))
    E.append(logo('linux', 820, 365, C['t2'] + 0.4, 90)); E.append(logo('docker', 1700, 365, C['t3'] + 0.4, 90))
    E.append(takeaway('Later: we build and run containers ourselves.', 800, C['t4'], GOOD, 1700)); return E
def s_choose(C, D, dur):
    E = head('Which to use', 'Choose by the problem.', C['o1'])
    E.append(Pop(card(840, 230, ACC, 'Virtual machine', [('Another OS, or strong isolation', TXT)], 46, 34), 100, 330, C['o2']))
    E.append(Pop(card(840, 230, GOOD, 'Container', [('Many small, fast, identical services', TXT)], 46, 34), 980, 330, C['o3']))
    E.append(Pop(card(1720, 150, VIO, 'In the cloud', [('Containers often run inside virtual machines.', TXT)], 46, 36), 100, 600, C['o4']))
    E.append(takeaway('Choose by the problem.', 860, C['o5'], GOOD, 1500)); return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['w1'])
    it = [('Myth: a container is a small VM', 'Reality: an isolated process, shared kernel.', WARN, 'w2'), ('Myth: containers are always safer', 'Reality: they isolate less than VMs.', BAD, 'w3'),
          ('Myth: virtual machines are obsolete', 'Reality: everywhere, and under containers.', VIO, 'w4'), ('Myth: Docker is a container', 'Reality: one tool that runs them.', GOOD, 'w5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Know the difference, then choose.', 860, C['w6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['r1'])
    items = [('Explains why isolation is needed', 'r3'), ('Explains hypervisor and VM', 'r4'), ('Explains the kernel', 'r5'), ('Explains a container', 'r6'), ('Compares them on four points', 'r7'), ('Chooses one, and says why', 'r8')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid] + (i % 2) * 0.5))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + (i % 2) * 0.5 + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['r9'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Compare them from memory.', C['y1'])
    E.append(Pop(card(1720, 150, WARN, 'On paper: four rows', [('Kernel, size, start time, isolation.', TXT)], 46, 36), 100, 330, C['y2']))
    it = [('1  Fill', 'The table, VM and container', ACC, 'y3'), ('2  Imagine', 'A site of twenty small services', VIO, 'y4'), ('3  Choose', 'Defend it in two sentences', GOOD, 'y5')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 270, col, n, [(s, TXT)], 44, 32, True), 100 + i * 590, 540, C[cid]))
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['y7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    qs = [('What does a hypervisor do?', 'z2'), ('What is the kernel?', 'z3'), ('Why are containers lighter than virtual machines?', 'z4'), ('When would you choose a virtual machine?', 'z8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['z9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC02-O04  ·  virtualization, containers', 'b', 30, TXT, maxw=960), 220, 748, C['z9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  compare them aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['z5']))
    E.append(El(T('Next: your own Linux virtual machine', 'x', 46, ACC, maxw=1500), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['z7']))
    return E
FN = dict(hook=s_hook, problem=s_problem, vm=s_vm, kernel=s_kernel, container=s_container, compare=s_compare, demo=s_demo, tools=s_tools, choose=s_choose, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(problem=('server', BAD), vm=('screen', ACC), kernel=('gear', WARN), container=('grid', GOOD), compare=('swap', VIO), demo=('eye', GOOD), tools=('link', ACC), choose=('steps', VIO), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
