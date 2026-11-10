import sys, re; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 13  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps
MONO = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 28)
_SP = {'VM': 'V M', 'VMs': 'V Ms', 'SSH': 'S S H', 'ISO': 'I S O', 'CPU': 'C P U', 'LTS': 'L T S', 'AWS': 'A W S', 'WSL': 'W S L', 'OS': 'O S'}
def _say(cap):
    s = re.sub(r'\b(' + '|'.join(_SP) + r')\b', lambda m: _SP[m.group(1)], cap)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "You want to learn Linux, but you do not want to break your own computer."),
  c('h2', "The answer is a disposable Linux virtual machine."),
  c('h3', "Break it, delete it, and start fresh in minutes."),
  c('h4', "Today: why, your options, the install, and how to log in."),
 ]),
 ('why', [
  c('w1', "First, why disposable?"),
  c('w2', "A virtual machine is separate from your real computer, so a mistake stays inside it."),
  c('w3', "It is the same for everyone, so your steps match the lesson."),
  c('w4', "And if it breaks, you delete it, and rebuild."),
  c('w5', "Treat it like a sandbox, not a home."),
 ]),
 ('options', [
  c('o1', "Where does the virtual machine come from?"),
  c('o2', "On your own computer, VirtualBox gives you a window, and a normal installer."),
  c('o3', "Multipass starts an Ubuntu machine with one command."),
  c('o4', "On Windows, WSL 2 gives you a light Linux environment.", "On Windows, W S L two gives you a light Linux environment."),
  c('o5', "Or rent one in the cloud, from a provider such as AWS, Azure, or Google Cloud."),
  c('o6', "Cloud machines can cost money, so delete them when you are done."),
  c('o7', "Any of them works. Pick one, and stay with it."),
 ]),
 ('size', [
  c('s1', "Next: how big should it be?"),
  c('s2', "For practice, two processors, two gigabytes of memory, and twenty gigabytes of disk are a comfortable start."),
  c('s3', "Never give it more than your computer can spare."),
  c('s4', "Choose a long term support release of Ubuntu Server, because it is widely documented.", "Choose an L T S, long term support, release of Ubuntu Server, because it is widely documented."),
  c('s5', "Server means no desktop, just the command line, which is exactly what we want."),
 ]),
 ('dlvbox', [
  c('d1', "Before the wizard, you need two downloads. First, VirtualBox itself."),
  c('d2', "Open virtualbox.org, and go to Downloads. On Windows, choose Windows hosts. On a Mac or Linux, choose yours.", "Open virtualbox dot org, and go to Downloads. On Windows, choose Windows hosts. On a Mac or Linux, choose yours."),
  c('d3', "Run the file you download. You do not need the Extension Pack for this lab."),
  c('d4', "Your version number will be newer than mine, and that is fine."),
 ]),
 ('dlubuntu', [
  c('u1', "Second, the Ubuntu Server image."),
  c('u2', "Open ubuntu.com slash download slash server, and press Download. Choose the Intel or AMD 64 bit one.", "Open ubuntu dot com slash download slash server, and press Download. Choose the Intel or AMD sixty four bit one."),
  c('u3', "It is about three gigabytes, so start it on a good connection."),
  c('u4', "The file ends in ISO. That is a disk image the installer boots from. Remember where you saved it."),
  c('u5', "At recording time, the latest long term support release was Ubuntu 26.04.1.", "At recording time, the latest long term support release was Ubuntu twenty six oh four point one."),
  c('u6', "Yours may be newer. Choose the current long term support release."),
 ]),
 ('install', [
  c('i1', "Now the install, in two ways."),
  c('i2', "With VirtualBox on Windows: run the installer you downloaded, and accept the defaults. It may briefly interrupt your network, and ask to install drivers. Allow them."),
  c('i3', "Then open VirtualBox, and create the machine. We do that next."),
  c('i4', "Later, inside the Ubuntu installer, choose a throwaway user and password, and tick the OpenSSH server option.", "Later, inside the Ubuntu installer, choose a throwaway user and password, and tick the open S S H server option."),
  c('i5', "With Multipass, one command does all of it."),
  c('i6', "Launch creates the machine, shell opens a terminal inside it, and list shows what is running."),
 ]),
 ('vbox', [
  c('b1', "Let us walk through the VirtualBox wizard."),
  c('b2', "These are real screenshots, captured from VirtualBox running in the sandbox."),
  c('b3', "Step one: name the machine, choose Linux, and the Ubuntu version. This is also where you pick your ISO file."),
  c('b4', "Step two: memory and processors. Two gigabytes, and two processors."),
  c('b5', "Step three: the virtual disk. Twenty gigabytes. It grows as you use it, so it does not take all of that at once."),
  c('b6', "Step four: the summary. Check it, then press Finish."),
  c('b7', "The machine now appears in the list, powered off. Press Start, and the installer boots from the ISO."),
  c('b8', "Here, we stop, because the sandbox cannot start virtual machines."),
  c('b9', "On Windows, you first run the VirtualBox installer. I have not captured that part, but the wizard you just saw is very similar."),
 ]),
 ('access', [
  c('a1', "Now: how do you get in?"),
  c('a2', "The console is the machine's own screen. It always works, but it is awkward."),
  c('a3', "SSH lets you log in from your own terminal, over the network."),
  c('a4', "SSH needs three things: an address, a user name, and a way to prove who you are."),
  c('a5', "The best proof is a key pair: a private key that stays secret, and a public key that you place on the machine."),
  c('a6', "Never share the private key."),
 ]),
 ('demo', [
  c('e1', "Now let us do the SSH part for real, in a disposable Linux sandbox."),
  c('e2', "These outputs are real captures. Here, the sandbox plays your virtual machine, and SSH connects back to itself."),
  c('e3', "First, we create a key pair. The command stays quiet when it works."),
  c('e4', "The fingerprint identifies the key, and it is safe to share. The private file is not."),
  c('e5', "Now we log in with the key, and run three commands: the host name, the user name, and the kernel version."),
  c('e6', "The answers come from the machine we logged in to: its name, its user, and its kernel."),
  c('e7', "If we try the wrong port, nothing answers: connection refused."),
  c('e8', "In your own machine, you use its address, and the port is usually twenty-two."),
 ]),
 ('errors', [
  c('x1', "Three messages you will meet."),
  c('x2', "Connection refused: the machine answered, but nothing is listening on that port. Is SSH installed and running, and is the port right?"),
  c('x3', "Permission denied: the server is there, but it rejected your key or your user name. Check both."),
  c('x4', "Connection timed out: no answer at all. Check that the machine is running, and that the address is right."),
  c('x5', "Read the message, then check one thing at a time."),
 ]),
 ('reset', [
  c('t1', "Now the disposable part."),
  c('t2', "Before a risky experiment, take a snapshot. VirtualBox can save the machine's state, and restore it later."),
  c('t3', "With Multipass, delete the machine, purge it, and launch it again."),
  c('t4', "Keep anything valuable outside the virtual machine, such as scripts in Git."),
  c('t5', "If you can rebuild it in minutes, you can experiment without fear."),
 ]),
 ('myths', [
  c('w6', "Watch out for four common myths."),
  c('m2', "Myth one: a virtual machine puts my computer at risk. In fact, it is the safer place to experiment."),
  c('m3', "Myth two: I need a powerful computer. In fact, a small Ubuntu Server runs on modest resources."),
  c('m4', "Myth three: a password is just as good as a key. In fact, keys are much harder to guess."),
  c('m5', "Myth four: a disposable machine can hold my real work. In fact, if you might need it, keep it elsewhere."),
  c('m6', "Disposable means replaceable."),
 ]),
 ('rubric', [
  c('r1', "Here is how you check your own work."),
  c('r2', "Imagine a teammate asks you to set up a practice machine."),
  c('r3', "Explain why it is disposable."), c('r4', "Choose a platform, and say why."), c('r5', "Create it with sensible sizes."),
  c('r6', "Log in over SSH, with a key."), c('r7', "Verify it with three commands."), c('r8', "Delete it, and rebuild it."), c('r9', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('y1', "Your turn."),
  c('y2', "This lab is unverified until you run it yourself, because I cannot install a machine on your computer."),
  c('y3', "One: create a machine with two processors, two gigabytes of memory, and twenty gigabytes of disk."),
  c('y4', "Two: log in over SSH, with a key."),
  c('y5', "Three: run the host name, user name, and kernel version commands, and write down the answers."),
  c('y6', "Four: break something inside it on purpose, then delete the machine, and rebuild it."),
  c('y7', "Mark yourself on the rubric."), c('y8', "Pause the video, and do it now."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "Why use a disposable machine?"), c('z3', "Name two ways to get one."),
  c('z4', "What does a key pair do?"), c('z10', "What does connection refused mean?"),
  c('z9', "Objective covered: MC02-O05.", "Objective covered: number five, in the I T fundamentals masterclass."),
  c('z5', "Pause the video, and answer out loud."), c('z6', "Next lesson: files, text, encodings, and paths."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'b3': 4.0, 'b4': 2.0, 'b5': 2.5, 'b6': 2.5, 'b7': 1.5, 'd4': 0.5, 'u6': 0.5, 'b9': 0.5, 'h4': 0.5, 'w5': 0.5, 'o7': 0.5, 's5': 0.5, 'i6': 0.5, 'a6': 0.5, 'e8': 0.5, 'x5': 0.5, 't5': 0.5, 'm6': 0.5, 'r9': 0.5, 'y8': 12.0, 'z5': 10.0}
CHAP = {'why': 'Why disposable', 'options': 'Your options', 'size': 'Size and release', 'dlvbox': 'Download VirtualBox', 'dlubuntu': 'Download Ubuntu Server', 'install': 'The install', 'vbox': 'VirtualBox wizard', 'access': 'Console and SSH', 'demo': 'Real demo', 'errors': 'Common errors',
        'reset': 'Snapshot and rebuild', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Fundamentals  ·  Lesson 13', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def trio(E, C, items, ids, y=520, h=230, w=540):
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def photo(path, w, h, col):
    im = Image.open(path).convert('RGB'); im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.5))
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=tuple(col)[:3] + (255,))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=20, fill=255)
    out.paste(im, (6, 6), m); return out
PHOTO = '/home/claude/academy/lesson13/assets/photo_l13_nersc.jpg'
def mono(s, col):
    im = Image.new('RGBA', (int(MONO.getlength(s)) + 10, 44), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), s, font=MONO, fill=tuple(col)[:3] + (255,)); return im

def s_hook(C, D, dur):
    E = [El(T('A safe place to practice', 'x', 64), 100, 130, C['h1'])]
    E.append(Pop(photo(PHOTO, 740, 500, ACC), 1080, 250, C['h1']))
    E.append(El(T('Photo: Derrick Coetzee  ·  CC0  ·  via Wikimedia Commons', 'm', 24, MUTED, maxw=740), 1080, 770, C['h1'] + 0.5, anim='fade'))
    E.append(Pop(card(900, 190, WARN, 'Your real computer', [('Keep it safe.', TXT)], 50, 36), 100, 250, C['h1']))
    E.append(Pop(card(900, 190, GOOD, 'A disposable VM', [('Break it, delete it, rebuild it.', TXT)], 50, 36), 100, 480, C['h2']))
    bs = [badge(n, F('b', 34), INK, col, padx=26, pady=14, r=26) for n, col in [('Why', WARN), ('Options', ACC), ('Install', VIO), ('Log in', GOOD)]]
    E.append(El(T('Today', 'b', 32, MUTED), 100, 740, C['h4'], anim='fade'))
    bx = 100
    for i, b in enumerate(bs): E.append(Pop(b, bx, 800, C['h4'] + 0.3 + i * 0.5)); bx += b.width + 30
    E.append(takeaway('Start fresh in minutes.', 930, C['h4'] + 1.2, GOOD, 1600)); return E
def s_why(C, D, dur):
    E = head('Why disposable?', 'A mistake stays inside the box.', C['w1'])
    trio(E, C, [('Safe', 'Apart from your computer', GOOD), ('Repeatable', 'Same for everyone', ACC), ('Replaceable', 'Break it? Delete and rebuild', WARN)], ['w2', 'w3', 'w4'], y=380, h=260)
    E.append(Pop(badge('A sandbox, not a home', F('x', 52), INK, GOOD, padx=34, pady=18, r=32), 100, 740, C['w5']))
    E.append(takeaway('Keep nothing in it you cannot lose.', 900, C['w5'] + 0.6, GOOD, 1600)); return E
def s_options(C, D, dur):
    E = head('Your options', 'Four ways to get a Linux machine.', C['o1'])
    E.append(Pop(card(840, 210, ACC, 'VirtualBox', [('A window and a normal installer', TXT)], 46, 34), 100, 330, C['o2']))
    E.append(Pop(card(840, 210, VIO, 'Multipass', [('An Ubuntu machine, one command', TXT)], 46, 34), 980, 330, C['o3']))
    E.append(Pop(card(840, 210, GOOD, 'WSL 2 on Windows', [('A light Linux environment', TXT)], 46, 34), 100, 570, C['o4']))
    E.append(Pop(card(840, 210, WARN, 'Cloud machine', [('Can cost money. Delete after use.', TXT)], 46, 34), 980, 570, C['o5']))
    for i, n in enumerate(['aws', 'azure', 'gcp']): E.append(logo(n, 1560 + i * 90, 600, C['o5'] + 0.3 + i * 0.2, 76))
    E.append(takeaway('Pick one, and stay with it.', 840, C['o7'], GOOD, 1500)); return E
def s_size(C, D, dur):
    E = head('Size and release', 'A comfortable start, not a rule.', C['s1'])
    trio(E, C, [('2 processors', 'Enough for practice', ACC), ('2 GB memory', 'Spare it from your computer', VIO), ('20 GB disk', 'Plenty for a lab', GOOD)], ['s2', 's2', 's2'], y=330, h=210)
    E.append(Pop(card(1720, 150, WARN, 'Ubuntu Server  ·  a long term support release', [('No desktop. Just the command line.', TXT)], 44, 34), 100, 600, C['s4']))
    E.append(logo('ubuntu', 1680, 622, C['s4'] + 0.3, 100))
    E.append(takeaway('Never give it more than you can spare.', 840, C['s3'] + 0.0, GOOD, 1600)); return E
def s_install(C, D, dur):
    E = head('The install', 'Two ways in.', C['i1']); E.append(ill(C['i1'] + 0.5, 1400, 130))
    st = [('1  Run the installer you downloaded', 'i2', 0), ('2  Accept the defaults, press Next', 'i2', 0.8), ('3  Allow the driver prompt', 'i2', 1.6), ('4  Finish, then open VirtualBox', 'i3', 0), ('5  Ubuntu installer: throwaway user, password', 'i4', 0), ('6  Tick the OpenSSH server option', 'i4', 1.2)]
    E.append(Pop(card(900, 520, ACC, 'VirtualBox on Windows', [], 40), 100, 330, C['i2']))
    for i, (s_, cid, off) in enumerate(st): E.append(El(T(s_, 'm', 28, TXT, maxw=840), 140, 420 + i * 70, C[cid] + off, anim='fade'))
    E.append(Pop(card(780, 520, VIO, 'Multipass', [], 40), 1040, 330, C['i5']))
    cmds = [('$ multipass launch --name lab', ACC), ('$ multipass shell lab', ACC), ('$ multipass list', ACC)]
    for j, (s_, col) in enumerate(cmds): E.append(El(mono(s_, col), 1070, 430 + j * 64, C['i5'] + 0.6 + (j * 1.0 if j else 0), anim='fade'))
    E.append(El(T('Launch creates it, shell opens it, list shows it.', 'm', 28, MUTED, maxw=700), 1070, 660, C['i6'], anim='fade'))
    E.append(takeaway('Either way: a Linux machine you can throw away.', 900, C['i6'] + 0.8, GOOD, 1700)); return E
def s_dlvbox(C, D, dur):
    E = head('Download VirtualBox', 'Download one of two.', C['d1']); E.append(real(C['d2'], 'REAL SCREENSHOT  ·  the official website', 1260, 296))
    E.append(Pop(photo('/home/claude/academy/lesson13/assets/dl/ann_vbox.jpg', 1100, 584, ACC), 100, 336, C['d2']))
    it = [('Website', 'virtualbox.org, then Downloads', ACC, 'd2'), ('Click', 'Your computer: Windows hosts', WARN, 'd2'), ('Then', 'Run the file you download', GOOD, 'd3')]
    for i, (n, t_, col, cid) in enumerate(it): E.append(Pop(card(560, 130, col, n, [(t_, TXT)], 36, 28), 1260, 370 + i * 150 + (0.0), C[cid] + 0.4 * i))
    E.append(takeaway('No Extension Pack needed for this lab.', 960, C['d3'] + 0.5, GOOD, 1100, 34)); return E
def s_dlubuntu(C, D, dur):
    E = head('Download Ubuntu Server', 'The disk image for your machine.', C['u1']); E.append(real(C['u2'], 'REAL SCREENSHOT  ·  the official website', 1260, 296))
    E.append(Pop(photo('/home/claude/academy/lesson13/assets/dl/ann_ubuntu.jpg', 1100, 409, ACC), 100, 336, C['u2']))
    it = [('Website', 'ubuntu.com/download/server', ACC, 'u2'), ('Click', 'Download, Intel or AMD 64-bit', WARN, 'u2'), ('Keep', 'The .iso file', GOOD, 'u4')]
    for i, (n, t_, col, cid) in enumerate(it): E.append(Pop(card(560, 130, col, n, [(t_, TXT)], 36, 28), 1260, 370 + i * 150, C[cid] + 0.4 * i))
    trio_i = [('File type', '.iso, a disk image', VIO, 'u4'), ('Size', 'About 3 GB', PINK, 'u3'), ('Version', 'Latest long term support', ACC, 'u6')]
    for i, (n, t_, col, cid) in enumerate(trio_i): E.append(Pop(card(340, 170, col, n, [(t_, TXT)], 36, 28), 100 + i * 380, 790, C[cid]))
    return E
def s_vbox(C, D, dur):
    E = head('VirtualBox wizard', 'Watch it happen, step by step.', C['b1']); E.append(real(C['b2'], 'REAL RECORDING  ·  VirtualBox 7.0', 1260, 296))
    E.append(Pop(card(1100, 600, ACC, '', [], 4), 100, 330, C['b2']))
    steps = [('Step 1  ·  Name and type', ACC, 'b3'), ('Step 2  ·  2 GB, 2 CPUs', VIO, 'b4'), ('Step 3  ·  20 GB disk', GOOD, 'b5'), ('Step 4  ·  Check, Finish', WARN, 'b6'), ('Step 5  ·  Start the VM', PINK, 'b7')]
    for i, (n, col, cid) in enumerate(steps):
        E.append(Pop(card(560, 100, col, '', [(n, TXT)], 4, 32), 1260, 360 + i * 120, C[cid] + 0.2))
    E.append(El(T('Sandbox limit: it cannot start a machine, so we stop after creating it.', 'm', 24, MUTED, maxw=1100), 100, 955, C['b8'], anim='fade'))
    E.append(El(T('Windows: run the VirtualBox installer first. Not captured here.', 'm', 24, MUTED, maxw=1100), 100, 990, C['b9'], anim='fade')); return E
def s_access(C, D, dur):
    E = head('Console and SSH', 'Two ways to get in.', C['a1'])
    E.append(Pop(card(560, 150, MUTED, 'Console', [('Always works, but awkward', TXT)], 40, 28), 100, 330, C['a2']))
    E.append(Pop(card(560, 150, ACC, 'SSH', [('Log in over the network', TXT)], 40, 28), 100, 505, C['a3']))
    E.append(Pop(card(560, 240, WARN, 'SSH needs three things', [('An address', TXT), ('A user name', TXT), ('A way to prove who you are', TXT)], 36, 28), 100, 680, C['a4']))
    E.append(Pop(card(1120, 170, BAD, 'Private key', [('Stays on your computer. Never share it.', TXT)], 44, 34), 700, 330, C['a5']))
    E.append(Pop(card(1120, 170, GOOD, 'Public key', [('Placed on the machine, in its authorized keys.', TXT)], 44, 34), 700, 525, C['a5'] + 1.0))
    E.append(Pop(card(1120, 190, VIO, 'The match', [('The server checks that your key pairs with the public one. If it does, you are in.', TXT)], 44, 32), 700, 720, C['a5'] + 2.2))
    E.append(takeaway('Never share the private key.', 965, C['a6'], BAD, 1600)); return E
def s_demo(C, D, dur):
    E = head('Real demo', 'A key pair, a login, and a refusal.', C['e1']); E.append(real(C['e2'], 'REAL OUTPUT  ·  captured in a Linux sandbox', 1260, 296))
    E.append(Pop(card(1100, 520, ACC, '', [], 4), 100, 330, C['e1'] + 0.3))
    blocks = [('e3', [('$ ssh-keygen -q -t ed25519 -N "" -f lab_key', ACC)], 20),
              ('e4', [("$ ssh-keygen -lf lab_key.pub | cut -d' ' -f1,2", ACC), ('256 SHA256:V01Ak2O/39wAYWZbqoAur+7HU2YkkXEvCNJ0IsusMjk', TXT)], 20),
              ('e5', [('$ ssh -i lab_key -p 2222 root@127.0.0.1 \\', ACC), ("    'hostname; whoami; uname -r'", ACC)], 0),
              ('e6', [('vm', GOOD), ('root', GOOD), ('6.18.44-fc-v338', GOOD)], 20),
              ('e7', [('$ ssh -p 2223 root@127.0.0.1 hostname', ACC), ('ssh: connect to host 127.0.0.1 port 2223: Connection refused', WARN)], 0)]
    y = 365; ys = []
    for cid, lines, gap in blocks:
        ys.append(y)
        for j, (s, col) in enumerate(lines): E.append(El(mono(s, col), 130, y + j * 36, C[cid] + j * 0.4, anim='fade'))
        y += len(lines) * 36 + gap
    ann = [('Step 1', 'make a key pair', ACC, 'e3', ys[0]), ('Fingerprint', 'safe to share', VIO, 'e4', ys[1]), ('Logged in', 'name, user, kernel', GOOD, 'e6', ys[3]), ('Wrong port', 'nothing answers', WARN, 'e7', ys[4])]
    prev = -999
    for n, s, col, cid, yy in ann:
        yy = max(yy, prev + 125); prev = yy; E.append(Pop(card(560, 100, col, '', [(n + ': ' + s, TXT)], 4, 26), 1260, yy, C[cid]))
    E.append(El(T('The sandbox stands in for your VM, so ssh connects to itself. Host-key options omitted for space.', 'm', 24, MUTED, maxw=1700), 100, 868, C['e2'] + 0.8, anim='fade'))
    E.append(takeaway('In your own VM: its address, usually port 22.', 930, C['e8'], GOOD, 1700)); return E
def s_errors(C, D, dur):
    E = head('Common errors', 'Read the message first.', C['x1'])
    rows = [('ssh: connect to host 127.0.0.1 port 2223: Connection refused', 'The machine answered, but nothing listens on that port. Is SSH running? Is the port right?', WARN, 'x2', True),
            ('root@127.0.0.1: Permission denied (publickey,keyboard-interactive).', 'The server rejected your key or user name. Check the key file and the user.', BAD, 'x3', True),
            ('Connection timed out', 'No answer at all. Is the machine running? Is the address right?', VIO, 'x4', False)]
    for i, (a, b, col, cid, r) in enumerate(rows):
        y = 330 + i * 190
        E.append(Pop(card(1720, 170, col, a, [(b, TXT)], 34, 30), 100, y, C[cid]))
        if r: E.append(real(C[cid] + 0.5, 'REAL OUTPUT', 1590, y + 16))
        else: E.append(El(badge('Typical message  ·  not captured', F('b', 24), INK, WARN, padx=16, pady=8), 1330, y + 16, C[cid] + 0.5, anim='fade'))
    E.append(takeaway('One check at a time.', 920, C['x5'], GOOD, 1500)); return E
def s_reset(C, D, dur):
    E = head('Snapshot and rebuild', 'The disposable part.', C['t1']); E.append(ill(C['t3'], 1400, 130))
    trio(E, C, [('1  Snapshot', "Save the machine's state first", ACC), ('2  Break it', 'Experiment freely inside', WARN), ('3  Restore or rebuild', 'Go back, or rebuild it', GOOD)], ['t2', 't2', 't3'], y=330, h=230)
    E.append(Pop(card(1100, 240, VIO, '', [], 4), 100, 600, C['t3'] + 0.3))
    for j, s in enumerate(['$ multipass delete lab', '$ multipass purge', '$ multipass launch --name lab']): E.append(El(mono(s, ACC), 130, 640 + j * 56, C['t3'] + 0.5 + j * 0.8, anim='fade'))
    E.append(Pop(card(560, 240, GOOD, 'Keep it outside', [('Scripts in Git, not only in the VM', TXT)], 38, 30), 1260, 600, C['t4']))
    E.append(takeaway('Rebuild in minutes, experiment without fear.', 900, C['t5'], GOOD, 1700)); return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['w6'])
    it = [('Myth: a VM puts my computer at risk', 'Reality: it is the safer place to experiment.', WARN, 'm2'), ('Myth: I need a powerful computer', 'Reality: a small Ubuntu Server runs on modest resources.', BAD, 'm3'),
          ('Myth: a password is as good as a key', 'Reality: keys are much harder to guess.', VIO, 'm4'), ('Myth: it can hold my real work', 'Reality: keep anything you need elsewhere.', GOOD, 'm5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Disposable means replaceable.', 860, C['m6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['r1'])
    items = [('Explains why it is disposable', 'r3'), ('Chooses a platform, and says why', 'r4'), ('Creates it with sensible sizes', 'r5'), ('Logs in over SSH with a key', 'r6'), ('Verifies with three commands', 'r7'), ('Deletes it, and rebuilds it', 'r8')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid] + (i % 2) * 0.5))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + (i % 2) * 0.5 + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['r9'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Build one, log in, and rebuild it.', C['y1'])
    E.append(Pop(card(1720, 130, WARN, 'Lab status: UNVERIFIED', [('I have not run this on your computer. Run it, and mark the rubric.', TXT)], 44, 32), 100, 330, C['y2']))
    it = [('1  Create', ['2 CPUs, 2 GB, 20 GB', 'Any platform you chose'], ACC, 'y3'), ('2  Log in', ['Over SSH', 'With a key, not a password'], VIO, 'y4'), ('3  Check', ['Host name, user, kernel', 'Write the answers down'], GOOD, 'y5'), ('4  Rebuild', ['Break it on purpose', 'Delete it, then rebuild'], PINK, 'y6')]
    for i, (n, ls, col, cid) in enumerate(it): E.append(Pop(card(410, 250, col, n, [(l, TXT) for l in ls], 40, 28, True), 100 + i * 437, 500, C[cid]))
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 820, C['y8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    qs = [('Why use a disposable machine?', 'z2'), ('Name two ways to get one.', 'z3'), ('What does a key pair do?', 'z4'), ('What does connection refused mean?', 'z10')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['z9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC02-O05  ·  a disposable Linux VM', 'b', 30, TXT, maxw=960), 220, 748, C['z9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['z5']))
    E.append(El(T('Next: files, text, encodings, and paths', 'x', 46, ACC, maxw=1500), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['z7']))
    return E
FN = dict(hook=s_hook, why=s_why, options=s_options, size=s_size, install=s_install, dlvbox=s_dlvbox, dlubuntu=s_dlubuntu, vbox=s_vbox, access=s_access, demo=s_demo, errors=s_errors, reset=s_reset, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('eye', GOOD), options=('swap', VIO), size=('gear', WARN), install=('steps', ACC), vbox=('screen', ACC), dlvbox=('link', ACC), dlubuntu=('link', GOOD), access=('link', ACC), demo=('eye', GOOD), errors=('question', WARN), reset=('loop', GOOD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
