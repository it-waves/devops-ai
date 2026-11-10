import sys, re, os; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
BAD = EN.BAD
LABEL = 'LESSON 14  ·  DEVOPS BOOTCAMP'
from PIL import ImageFont, ImageOps
MONO = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 28)
_SP = {'ASCII': 'ask ee', 'UTF-8': 'U T F eight', 'xxd': 'x x d', 'CRLF': 'C R L F', 'LF': 'L F', 'CR': 'C R', 'ELF': 'E L F', 'iconv': 'I conv', 'VM': 'V M',
       'sed': 's e d', 'printf': 'print f', 'wc': 'w c', 'pwd': 'p w d', 'mkdir': 'make dir', 'chmod': 'change mod', 'ls': 'l s', 'cd': 'c d', 'PATH': 'path', 'HOME': 'home', 'USER': 'user', 'SHELL': 'shell'}
def _say(cap):
    s = re.sub(r'(?<![\w-])(' + '|'.join(re.escape(k) for k in _SP) + r')(?![\w-])', lambda m: _SP[m.group(1)], cap)
    return s if s != cap else None
def c(cid, cap, say=None, gap=None):
    say = say or _say(cap)
    return (cid, cap, say, gap) if gap is not None else (cid, cap, say)

SCENES = [
 ('hook', [
  c('h1', "Every file on a computer is just numbers."), c('h2', "Text, pictures, programs: all of it is bytes."),
  c('h3', "And many server bugs come from mixing those bytes up."),
  c('h4', "Today we look at real bytes, encodings, paths, and environment variables, live in a terminal."),
 ]),
 ('bits', [
  c('b1', "First, the smallest piece: the bit."), c('b2', "A bit is one switch, either zero or one."), c('b3', "Eight bits make one byte."),
  c('b4', "One byte holds two hundred fifty-six different values, from zero to two hundred fifty-five."),
  c('b5', "Files, memory, and network traffic are all counted in bytes."),
 ]),
 ('xxd', [
  c('x1', "Let us look at a real byte."), c('x2', "The tool xxd shows raw bytes."),
  c('x3', "Type: echo -n A | xxd -b", "Type: echo, dash n, A, pipe, x x d, dash b."),
  c('x4', "Eight bits: zero one zero zero zero zero zero one."), c('x5', "That pattern is the number sixty-five, and sixty-five is the letter A."),
  c('x6', "Now the same, without dash b: echo -n A | xxd", "Now the same, without dash b. Type: echo, dash n, A, pipe, x x d."),
  c('x7', "Forty-one. That is sixty-five written in hexadecimal."), c('x8', "Hexadecimal, or hex, writes one byte with just two characters. Developers use it everywhere."),
  c('x9', "One more, with two letters. Type: echo -n Hi | xxd", "One more, with two letters. Type: echo, dash n, H i, pipe, x x d."),
  c('x10', "Hex forty-eight is H, and hex sixty-nine is i. Two letters, two bytes."), c('x11', "That is all a text file is: bytes, in a row."),
 ]),
 ('text', [
  c('t1', "But a byte is only a number. How does a number become a letter?"), c('t2', "By agreement. A table says which number means which character."),
  c('t3', "The oldest common table is ASCII, with one hundred twenty-eight characters."),
  c('t4', "In it, sixty-five is capital A, sixty-six is capital B, and ninety-seven is lowercase a."),
  c('t5', "So a text file is simply bytes, plus a table to read them with."), c('t6', "Without the right table, the bytes are just numbers."),
 ]),
 ('kinds', [
  c('k1', "Is a file text, or a program? The file command tells you."),
  c('k2', 'First, make a small text file. Type: echo "hello" > hello.txt', "First, make a small text file. Type: echo hello, then a greater-than sign, then hello dot t x t."),
  c('k3', "Now type: file hello.txt", "Now type: file, hello dot t x t."), c('k4', "ASCII text. Just bytes that follow the ASCII table."),
  c('k5', "Now a real program. Type: file -b /bin/ls | cut -d, -f1-2", "Now a real program. Type: file, dash b, slash bin slash l s, pipe, cut, dash d, comma, dash f, one to two. Dash b hides the file name, and cut keeps the first two parts."),
  c('k6', "An ELF executable. That is the standard Linux program format."),
  c('k7', "Last, look inside it. Type: head -c 16 /bin/ls | xxd", "Last, look inside it. Type: head, dash c, sixteen, slash bin slash l s, pipe, x x d."),
  c('k8', "The first bytes are seven f, then E, L, F. Every Linux program starts with that signature."), c('k9', "A program and a text file are both bytes. Only the meaning differs."),
 ]),
 ('enc', [
  c('e1', "A table of one hundred twenty-eight characters cannot hold the world's languages."),
  c('e2', "So Unicode gives every character its own number: letters, accents, symbols, even emoji."),
  c('e3', "UTF-8 is the way those numbers are stored as bytes."),
  c('e4', "English letters take one byte. An accented letter like e acute takes two. Others take three or four."),
  c('e5', "UTF-8 is the default on almost every modern Linux server."),
  c('e6', "Keep two words apart: a character is what you see, and a byte is what is stored."),
 ]),
 ('encdemo', [
  c('n1', "Let us prove it. First, the plain word cafe, with no accent."),
  c('n2', "Type: printf 'cafe' | xxd", "Type: print f, cafe, pipe, x x d."), c('n3', "Four letters, four bytes."),
  c('n4', "Now with the accent. Type: printf 'café' | xxd", "Now with the accent. Type: print f, cafe with an acute accent, pipe, x x d."),
  c('n5', "Five bytes! The e acute became two bytes: c three, a nine."),
  c('n6', "Count the bytes. Type: printf 'café' | wc -c", "Count the bytes. Type: print f, cafe, pipe, w c, dash c."), c('n7', "Five bytes. Now count characters. Type: printf 'café' | wc -m", "Five bytes. Now count characters. Same command, but with dash m."),
  c('n8', "Four characters, five bytes. They are different things."),
  c('n9', "Now the classic bug: read these bytes with the wrong table. Type: echo café | iconv -f latin1 -t utf8", "Now the classic bug: read these bytes with the wrong table. Type: echo, cafe, pipe, I conv, dash f, latin one, dash t, U T F eight."),
  c('n10', "Garbled! Instead of e acute, we see A tilde and a copyright sign."),
  c('n11', "That is the broken text you may have seen on websites. The bytes were fine. The table was wrong."),
  c('n12', "The fix is to use the matching encoding. In practice, use UTF-8 everywhere."),
 ]),
 ('eol', [
  c('l1', "Next: how a text file marks the end of a line."), c('l2', "Linux uses one byte, called L F."), c('l3', "Windows uses two bytes: C R, then L F."),
  c('l4', "A file made on Windows can carry hidden C R bytes onto your Linux server."), c('l5', "The result: scripts that refuse to run, with confusing errors."),
 ]),
 ('eoldemo', [
  c('o1', "Let us create a Windows-style file, and see for ourselves."),
  c('o2', "Type: printf 'one\\r\\ntwo\\r\\n' > win.txt", "Type: print f, one, backslash r, backslash n, two, backslash r, backslash n, redirect into win dot t x t."),
  c('o3', "Now type: file win.txt", "Now type: file, win dot t x t."), c('o4', "The file command spots them: C R L F line terminators."),
  c('o5', "Type: cat -A win.txt", "Type: cat, dash capital A, win dot t x t."), c('o6', "Dash A shows hidden characters. Caret M is the hidden C R, and the dollar sign marks each line end."),
  c('o7', "Now a script with the same problem. First, make it."), 
  c('o8', "Type: printf '#!/bin/bash\\r\\necho hi\\r\\n' > run.sh", "Type: print f, then the script text, with a C R at the end of each line, redirect into run dot s h."),
  c('o9', "Make it executable. Type: chmod +x run.sh", "Make it executable. Type: change mod, plus x, run dot s h."), c('o10', "Now run it. Type: ./run.sh", "Now run it. Type: dot slash run dot s h."),
  c('o11', "Required file not found. But the file is right there!"),
  c('o12', "The system looks for an interpreter named bash plus a hidden C R, and that does not exist."),
  c('o13', "The fix: s e d removes the C R at the end of every line. Type: sed -i 's/\\r$//' run.sh", "The fix: s e d removes the C R at the end of every line. Type: sed, dash i, then the pattern, then run dot s h."),
  c('o14', "Run it again."), c('o15', "It prints hi. Remember this one: it is a very common real-world error."),
 ]),
 ('paths', [
  c('p1', "Now paths: how you tell Linux where a file is."), c('p2', "An absolute path starts with a slash, and works from anywhere."),
  c('p3', "A relative path does not start with a slash. It starts from where you are now."),
  c('p4', "Four shortcuts matter. Slash is the top. Dot is here. Dot dot is one folder up. Tilde is your home folder."),
  c('p5', "Rule of thumb: in scripts and on servers, absolute paths are safer."),
 ]),
 ('pathdemo', [
  c('a1', "Let us walk a path. First, make two folders at once. Type: mkdir -p project/docs", "Let us walk a path. First, make two folders at once. Type: make dir, dash p, project slash docs."),
  c('a2', "Move in, using a relative path. Type: cd project/docs", "Move in, using a relative path. Type: c d, project slash docs."),
  c('a3', "Where are we? Type: pwd", "Where are we? Type: p w d."), c('a3b', "It prints the full, absolute path."),
  c('a4', "Now dot dot, one folder up. Type: cd ..", "Now dot dot, one folder up. Type: c d, dot dot."), c('a5', "Check again. Type: pwd", "Check again. Type: p w d."),
  c('a6', "Now tilde, which takes us home from anywhere. Type: cd ~", "Now tilde, which takes us home from anywhere. Type: c d, tilde."),
  c('a7', "List with a relative path. Type: ls project", "List with a relative path. Type: l s, project."),
  c('a8', "And with an absolute path. Type: ls /home/student/project", "And with an absolute path. Type: l s, slash home slash student slash project."),
  c('a9', "Same folder, same answer. Choose by where the command will run."),
 ]),
 ('envvars', [
  c('v1', "Now environment variables: named values that programs can read."),
  c('v2', "Your shell has variables. When you export one, it becomes an environment variable."),
  c('v3', "Child programs, such as scripts you start, inherit only the exported ones."),
  c('v4', "Common ones are HOME, USER, SHELL, and PATH."),
  c('v5', "Servers use them for settings, such as which database to talk to."),
 ]),
 ('envdemo', [
  c('m1', "Let us watch this happen."), c('m2', "Type: echo $HOME. The dollar sign means: give me the value.", "Type: echo, dollar home. The dollar sign means: give me the value."),
  c('m3', "Now make our own variable. Type: GREETING=hello. No spaces around the equals sign.", "Now make our own variable. Type: greeting, equals, hello. No spaces around the equals sign."),
  c('m4', "Read it back. Type: echo $GREETING", "Read it back. Type: echo, dollar greeting."),
  c('m5', "Now start a child shell, and ask it to print the variable.", "Now start a child shell, and ask it to print the variable. Type: bash, dash c, echo, child sees, colon, dollar greeting."),
  c('m6', "Empty! The child cannot see it, because we have not exported it."),
  c('m7', "So export it. Type: export GREETING", "So export it. Type: export greeting."),
  c('m8', "Press the up arrow twice, to repeat the child shell command, then Enter.", ),
  c('m9', "Now the child sees hello. Exported variables flow down to child programs."),
 ]),
 ('pathvar', [
  c('pv1', "One environment variable deserves special attention: PATH."), c('pv2', "PATH is a list of folders, separated by colons."),
  c('pv3', "When you type a command name, the shell searches those folders, from left to right."),
  c('pv4', "If the program is in none of them, you get: command not found."),
  c('pv5', "The fix: put the program in a folder on the path, or add its folder to the path."),
 ]),
 ('pathrun', [
  c('u1', "Let us see our own path. Type: echo $PATH", "Let us see our own path. Type: echo, dollar path."), c('u2', "Each folder is separated by a colon."),
  c('u3', "Which command was found where? Type: which ls", "Which command was found where? Type: which, l s."), c('u3b', "The which command prints the file that would run."),
  c('u4', "Now our own script. First, a folder for it. Type: mkdir -p ~/bin", "Now our own script. First, a folder for it. Type: make dir, dash p, tilde slash bin."),
  c('u5', "Create a one-line script. Type: printf '#!/bin/bash\\necho \"Hello!\"\\n' > ~/bin/hello", "Create a small script. Type: print f, the script text, redirect into tilde slash bin slash hello."),
  c('u6', "Make it executable. Type: chmod +x ~/bin/hello", "Make it executable. Type: change mod, plus x, tilde slash bin slash hello."),
  c('u7', "Now run it by name. Type: hello"), c('u8', "Command not found. The folder is not on the path yet."),
  c('u9', "Add it. Type: export PATH=\"$HOME/bin:$PATH\"", "Add it. Type: export path, equals, in quotes, dollar home slash bin, colon, dollar path."),
  c('u10', "Run it again. Type: hello"), c('u11', "It works! And which shows where it was found. Type: which hello", "It works! And which shows where it was found. Type: which hello."),
  c('u12', "This is how every installed command works. A change like this lasts only for this terminal session. Saving it permanently comes later in the course."),
 ]),
 ('errors', [
  c('er1', "Let us connect all this to the errors you will really meet."), c('er2', "Command not found: check the path, and check the spelling."),
  c('er3', "Strange characters like A tilde: an encoding mismatch. Use UTF-8."), c('er4', "Required file not found, or caret M: hidden C R bytes. Convert the line endings."),
  c('er5', "No such file or directory: usually a wrong path. Check relative versus absolute, with p w d."), c('er6', "A variable is empty in a script: you forgot to export it."),
 ]),
 ('myths', [
  c('w1', "Watch out for four common myths."), c('w2', "Myth one: all text files are the same. In fact, encoding and line endings differ."),
  c('w3', "Myth two: a character is one byte. In fact, in UTF-8 it can take up to four."),
  c('w4', "Myth three: a variable set in the terminal reaches every program. In fact, only exported ones reach child programs."),
  c('w5', "Myth four: command not found means the program is not installed. In fact, it may simply be outside the path."), c('w6', "Check before you assume."),
 ]),
 ('rubric', [
  c('ru1', "Here is how you check your own understanding."), c('ru2', "Imagine a colleague asks you to explain a broken script."),
  c('ru3', "Explain bits, bytes, and hex for one byte."), c('ru4', "Tell a text file from a program, using the file command."), c('ru5', "Show bytes versus characters in UTF-8."),
  c('ru6', "Find and remove hidden C R line endings."), c('ru7', "Use absolute and relative paths correctly."), c('ru8', "Export a variable, and fix a command that is not on the path."),
  c('ru9', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('y1', "Your turn, in the virtual machine you built last time."), c('y2', "One: use x x d to show the bytes of your own first name."),
  c('y3', "Two: pick a word with an accent. Show its bytes, then its characters."), c('y4', "Three: make a file with C R L F endings, find them, and remove them."),
  c('y5', "Four: export a variable, and prove that a child shell can see it."), c('y6', "Five: put a script in your bin folder, and run it by name."),
  c('y7', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('z1', "Quick check."), c('z2', "How many bits make a byte, and what is hex?"), c('z3', "Why can a word have more bytes than characters?"),
  c('z4', "What does command not found usually mean?"), c('z8', "What is the difference between a variable and an exported variable?"),
  c('z9', "Objective covered: MC02-O06.", "Objective covered: number six, in the I T fundamentals masterclass."),
  c('z5', "Pause the video, and answer out loud."), c('z6', "Next lesson: server components and failure symptoms."), c('z7', "Subscribe, so you do not miss it."),
 ]),
]
EXTRA = {'o14': 0.7, 'h4': 0.5, 'b5': 0.5, 'x11': 0.5, 'k9': 0.5, 'e6': 0.5, 'n12': 0.5, 'l5': 0.5, 'o15': 0.5, 'p5': 0.5, 'a9': 0.5, 'v5': 0.5, 'm9': 0.5, 'pv5': 0.5, 'u12': 0.5, 'er6': 0.5, 'w6': 0.5, 'ru9': 0.5,
         'y7': 14.0, 'z5': 10.0}
CHAP = {'bits': 'Bits and bytes', 'xxd': 'Live: real bytes', 'text': 'Bytes to text', 'kinds': 'Live: text or program', 'enc': 'Encodings', 'encdemo': 'Live: UTF-8', 'eol': 'Line endings', 'eoldemo': 'Live: hidden CR',
        'paths': 'Paths', 'pathdemo': 'Live: paths', 'envvars': 'Environment variables', 'envdemo': 'Live: export', 'pathvar': 'The PATH variable', 'pathrun': 'Live: fix PATH', 'errors': 'Symptoms and causes',
        'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
def head(title, sub, t): return [El(T('Fundamentals  ·  Lesson 14', 'b', 30, ACC), 100, 120, t), El(T(title, 'x', 64), 100, 160, t + 0.1), El(T(sub, 'm', 32, MUTED, maxw=1200), 100, 245, t + 0.4)]
def takeaway(s, y, t, col=None, w=1500, size=38): return El(T(s, 'b', size, col or WARN, maxw=w), 100, y, t)
def trio(E, C, items, ids, y=520, h=230, w=540):
    for i, (n, s, cl) in enumerate(items): E.append(Pop(card(w, h, cl, n, [(s, TXT)], 44, 32), 100 + i * 590, y, C[ids[i]]))
def photo(path, w, h, col):
    im = Image.open(path).convert('RGB'); im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, 0.5))
    out = Image.new('RGBA', (w + 12, h + 12), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    d.rounded_rectangle([0, 0, w + 11, h + 11], radius=26, fill=tuple(col)[:3] + (255,))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=20, fill=255)
    out.paste(im, (6, 6), m); return out
PHOTO = '/home/claude/academy/lesson14/assets/photo_l14_binary.jpg'
PHOTO_CREDIT = 'Punch cards in storage  ·  U.S. National Archives  ·  Public domain  ·  via Wikimedia Commons'
def mono(s, col, size=28):
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', size)
    im = Image.new('RGBA', (int(f.getlength(s)) + 10, size + 16), (0, 0, 0, 0)); ImageDraw.Draw(im).text((0, 0), s, font=f, fill=tuple(col)[:3] + (255,)); return im
def chip(s, col, size=40, padx=22, pady=10):
    return badge(s, ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', size), INK, col, padx=padx, pady=pady, r=18)

def s_hook(C, D, dur):
    E = [El(T('Everything is bytes', 'x', 64), 100, 130, C['h1'])]
    if os.path.exists(PHOTO):
        E.append(Pop(photo(PHOTO, 740, 500, ACC), 1080, 250, C['h1']))
        E.append(El(T(PHOTO_CREDIT, 'm', 24, MUTED, maxw=740), 1080, 770, C['h1'] + 0.5, anim='fade'))
    E.append(Pop(card(900, 150, ACC, 'Text, pictures, programs', [('All stored as bytes.', TXT)], 46, 36), 100, 250, C['h1']))
    E.append(Pop(card(900, 150, WARN, 'Mix the bytes up', [('And servers misbehave.', TXT)], 46, 36), 100, 430, C['h3']))
    bs = [badge(n, F('b', 34), INK, col, padx=26, pady=14, r=26) for n, col in [('Bytes', ACC), ('Encodings', VIO), ('Paths', GOOD), ('Variables', WARN)]]
    E.append(El(T('Today, live', 'b', 32, MUTED), 100, 640, C['h4'], anim='fade'))
    bx = 100
    for i, b in enumerate(bs): E.append(Pop(b, bx, 700, C['h4'] + 0.3 + i * 0.5)); bx += b.width + 24
    E.append(takeaway('Real commands, real output.', 840, C['h4'] + 1.8, GOOD, 1600)); return E
def s_bits(C, D, dur):
    E = head('Bits and bytes', 'The smallest pieces of data.', C['b1'])
    bits = '01000001'
    for i, ch in enumerate(bits): E.append(Pop(chip(ch, ACC if ch == '1' else VIO, 64, 30, 18), 100 + i * 120, 340, C['b3'] + i * 0.12))
    E.append(Pop(badge('1 bit  =  0 or 1', F('b', 40), INK, ACC, padx=28, pady=14, r=24), 100, 330 + 150, C['b2']))
    E.append(Pop(card(560, 200, VIO, '8 bits  =  1 byte', [('The unit everything counts in', TXT)], 44, 32), 100, 600, C['b3']))
    E.append(Pop(card(560, 200, GOOD, '256 values', [('From 0 to 255', TXT)], 44, 32), 690, 600, C['b4']))
    E.append(Pop(card(500, 200, WARN, 'Counted in bytes', [('Files, memory, network', TXT)], 44, 32), 1280, 600, C['b5']))
    E.append(takeaway('This byte happens to be the letter A.', 860, C['b5'] + 1.0, GOOD, 1600)); return E
def _lab(title, sub, first, badge_, steps, mono_steps=True):
    def f(C, D, dur):
        E = head(title, sub, C[first]); E.append(real(C[first] + 0.2, badge_, 1260, 286))
        E.append(Pop(card(1100, 640, ACC, '', [], 4), 100, 330, C[first]))
        n = len(steps); gap = min(120, (1035 - 345) // n); fs_t, fs_s = (30, 25) if n <= 6 else (27, 23)
        for i, (cid, t, sb, col) in enumerate(steps): E.append(Pop(card(560, gap - 12, col, t, [(sb, TXT)], fs_t, fs_s), 1260, 345 + i * gap, C[cid] + 0.2))
        return E
    return f
RB = 'REAL RECORDING  ·  Ubuntu 24.04 terminal'
s_xxd = _lab('Real bytes', 'Look at a letter, bit by bit.', 'x1', RB, [('x3', 'xxd -b', 'Show the bits', ACC), ('x4', '01000001', 'Eight bits = 65 = A', VIO), ('x6', 'xxd', 'Show hex instead', GOOD), ('x7', '41', '65 in hexadecimal', WARN), ('x9', 'Hi', 'Two letters, two bytes', PINK), ('x10', '48 69', 'One byte per letter', ACC)])
s_kinds = _lab('Text, or a program?', 'The file command tells you.', 'k1', RB, [('k2', 'echo > file', 'Make a text file', ACC), ('k3', 'file hello.txt', 'Ask what it is', VIO), ('k4', 'ASCII text', 'Bytes + the ASCII table', GOOD), ('k5', 'file -b /bin/ls', 'Ask about a program', WARN), ('k6', 'ELF executable', 'The Linux program format', PINK), ('k7', 'xxd the start', '7f 45 4c 46 = .ELF', ACC)])
s_encdemo = _lab('Bytes versus characters', 'Prove it with an accent.', 'n1', RB, [('n2', 'cafe', '4 letters, 4 bytes', ACC), ('n4', 'café', 'The é takes 2 bytes: c3 a9', VIO), ('n6', 'wc -c', 'Count bytes: 5', GOOD), ('n7', 'wc -m', 'Count characters: 4', WARN), ('n9', 'iconv wrong table', 'Reading UTF-8 as latin1', PINK), ('n10', 'cafÃ©', 'Garbled: wrong table', BAD)])
s_eoldemo = _lab('Hidden line endings', 'Find them, then fix them.', 'o1', RB, [('o2', 'printf ... > win.txt', 'Windows-style file', ACC), ('o3', 'file win.txt', 'CRLF line terminators', VIO), ('o5', 'cat -A', '^M is the hidden CR', GOOD), ('o10', './run.sh', 'required file not found', BAD), ('o13', 'sed -i', 'Remove the CR', WARN), ('o14', './run.sh', 'Now it prints hi', GOOD)])
s_pathdemo = _lab('Walk a path', 'Absolute, relative, dot dot, tilde.', 'a1', RB, [('a1', 'mkdir -p', 'Make nested folders', ACC), ('a2', 'cd project/docs', 'Relative path', VIO), ('a3', 'pwd', 'Absolute path of here', GOOD), ('a4', 'cd ..', 'One folder up', WARN), ('a6', 'cd ~', 'Home, from anywhere', PINK), ('a7', 'ls project, ls /home/...', 'Relative, then absolute', ACC)])
s_envdemo = _lab('Export a variable', 'A child sees only exported ones.', 'm1', RB, [('m2', 'echo $HOME', 'Read a variable', ACC), ('m3', 'GREETING=hello', 'Set a shell variable', VIO), ('m5', 'bash -c ...', 'Child: sees nothing', BAD), ('m7', 'export GREETING', 'Pass it down', WARN), ('m8', 'Up arrow x2, Enter', 'Repeat the child test', PINK), ('m9', 'child sees: hello', 'Now it arrives', GOOD)])
s_pathrun = _lab('Fix a command not found', 'Put the folder on PATH.', 'u1', RB, [('u1', 'echo $PATH', 'Folders, colon-separated', ACC), ('u4', 'mkdir, printf, chmod', 'Our own script in ~/bin', VIO), ('u7', 'hello', 'command not found', BAD), ('u9', 'export PATH=...', 'Add the folder', WARN), ('u10', 'hello', 'Works', GOOD), ('u11', 'which hello', 'Where it was found', PINK)])
def s_text(C, D, dur):
    E = head('Bytes to text', 'A number plus an agreed table.', C['t1'])
    rows = [('65', 'A', ACC), ('66', 'B', VIO), ('97', 'a', GOOD), ('48', '0', WARN), ('32', 'space', PINK)]
    E.append(El(T('The ASCII table (a small piece)', 'b', 32, MUTED), 100, 330, C['t3'], anim='fade'))
    for i, (n, ch, col) in enumerate(rows):
        x = 100 + i * 345
        E.append(Pop(chip(n, col, 60, 30, 16), x, 400, C['t4'] + i * 0.25)); E.append(El(T('means', 'm', 28, MUTED), x + 5, 505, C['t4'] + i * 0.25 + 0.2, anim='fade')); E.append(Pop(chip(ch, TXT, 60, 30, 16), x, 550, C['t4'] + i * 0.25 + 0.4))
    E.append(Pop(card(840, 170, ACC, 'ASCII', [('128 characters. English letters, digits, symbols.', TXT)], 46, 32), 100, 700, C['t3']))
    E.append(Pop(card(840, 170, WARN, 'No table, no text', [('Without the right table, bytes are only numbers.', TXT)], 46, 32), 980, 700, C['t6']))
    return E
def s_enc(C, D, dur):
    E = head('Encodings', 'One number per character, stored as bytes.', C['e1'])
    trio(E, C, [('Unicode', 'A number for every character', ACC), ('UTF-8', 'Stores those numbers as bytes', VIO), ('Default', 'On almost every Linux server', GOOD)], ['e2', 'e3', 'e5'], y=330, h=230)
    E.append(El(T('Bytes needed in UTF-8', 'b', 32, MUTED), 100, 600, C['e4'], anim='fade'))
    ex = [('e', '1 byte', ACC), ('é', '2 bytes', VIO), ('€', '3 bytes', WARN), ('emoji', '4 bytes', PINK)]
    for i, (ch, n, col) in enumerate(ex):
        x = 100 + i * 430
        E.append(Pop(card(400, 120, col, ch + '   ' + n, [], 44), x, 650, C['e4'] + i * 0.5))
    E.append(takeaway('A character is what you see. A byte is what is stored.', 840, C['e6'], GOOD, 1700)); return E
def s_eol(C, D, dur):
    E = head('Line endings', 'The invisible bytes at the end of a line.', C['l1'])
    E.append(Pop(card(840, 250, GOOD, 'Linux', [('One byte: LF', TXT), ('Hex 0a', TXT)], 52, 38), 100, 330, C['l2']))
    E.append(Pop(card(840, 250, WARN, 'Windows', [('Two bytes: CR then LF', TXT), ('Hex 0d 0a', TXT)], 52, 38), 980, 330, C['l3']))
    E.append(Pop(card(1720, 150, BAD, 'The trap', [('A Windows file on a Linux server carries hidden CR bytes.', TXT)], 46, 36), 100, 620, C['l4']))
    E.append(takeaway('Scripts refuse to run, with confusing errors.', 830, C['l5'], BAD, 1700)); return E
def s_paths(C, D, dur):
    E = head('Paths', 'Where a file lives.', C['p1'])
    E.append(Pop(card(840, 250, ACC, 'Absolute', [('Starts with a slash', TXT), ('/home/student/project', ACC)], 50, 36), 100, 330, C['p2']))
    E.append(Pop(card(840, 250, VIO, 'Relative', [('No leading slash; starts from here', TXT), ('project/docs', VIO)], 50, 36), 980, 330, C['p3']))
    sh = [('/', 'the top', ACC), ('.', 'here', VIO), ('..', 'up one', GOOD), ('~', 'your home', WARN)]
    for i, (s, t_, col) in enumerate(sh):
        E.append(Pop(card(410, 170, col, s + '   ' + t_, [], 48), 100 + i * 437, 640, C['p4'] + i * 0.8))
    E.append(takeaway('Scripts and servers: prefer absolute paths.', 860, C['p5'], GOOD, 1600)); return E
def s_envvars(C, D, dur):
    E = head('Environment variables', 'Named values programs can read.', C['v1'])
    E.append(Pop(card(840, 230, ACC, 'Shell variable', [('Lives in this shell only', TXT), ('GREETING=hello', ACC)], 48, 34), 100, 330, C['v2']))
    E.append(Pop(card(840, 230, GOOD, 'Environment variable', [('Exported, so child programs inherit it', TXT), ('export GREETING', GOOD)], 48, 34), 980, 330, C['v3']))
    for i, (n, col) in enumerate([('HOME', ACC), ('USER', VIO), ('SHELL', GOOD), ('PATH', WARN)]):
        E.append(Pop(chip(n, col, 44, 30, 14), 100 + i * 300, 620, C['v4'] + i * 0.3))
    E.append(Pop(card(1720, 160, VIO, 'On servers', [('Settings such as which database to talk to', TXT)], 44, 34), 100, 740, C['v5']))
    E.append(takeaway('Export it, or the child will not see it.', 940, C['v5'] + 1.0, WARN, 1600)); return E
def s_pathvar(C, D, dur):
    E = head('The PATH variable', 'Where the shell looks for commands.', C['pv1'])
    E.append(El(T('PATH =', 'b', 36, MUTED), 100, 340, C['pv2'], anim='fade'))
    x = 100
    parts = ['/usr/local/bin', '/usr/bin', '/bin']
    for i, p in enumerate(parts):
        ch = chip(p, [ACC, VIO, GOOD][i], 40, 24, 12); E.append(Pop(ch, x, 400, C['pv2'] + i * 0.4)); x += ch.width + 20
        if i < 2: E.append(El(T(':', 'x', 52, WARN), x - 12, 396, C['pv2'] + i * 0.4 + 0.2, anim='fade')); x += 24
    E.append(Pop(card(840, 210, ACC, 'You type: hello', [('Search folder one, then two, then three', TXT)], 46, 34), 100, 540, C['pv3']))
    E.append(Pop(card(840, 210, BAD, 'Not in any of them', [('bash: hello: command not found', BAD)], 46, 34), 980, 540, C['pv4']))
    E.append(takeaway('Fix: move the program onto the path, or add its folder.', 830, C['pv5'], GOOD, 1700)); return E
def s_errors(C, D, dur):
    E = head('Symptoms and causes', 'Match the error to the cause.', C['er1'])
    it = [('command not found', 'Path or spelling', 'er2', BAD), ('cafÃ©', 'Encoding mismatch: use UTF-8', 'er3', WARN), ('required file not found  /  ^M', 'Hidden CR line endings', 'er4', VIO), ('No such file or directory', 'Wrong path: check pwd', 'er5', ACC), ('Variable empty in a script', 'Forgot to export', 'er6', GOOD)]
    for i, (a, b, cid, col) in enumerate(it):
        y = 335 + i * 130
        E.append(Pop(card(900, 112, col, '', [(a, TXT)], 4, 34), 100, y, C[cid])); E.append(El(T('→', 'x', 50, MUTED), 1020, y + 25, C[cid] + 0.3, anim='fade')); E.append(Pop(card(700, 112, col, '', [(b, TXT)], 4, 32), 1100, y, C[cid] + 0.4))
    return E
def s_myths(C, D, dur):
    E = head('Four common myths', 'Clear them up early.', C['w1'])
    it = [('Myth: all text files are the same', 'Reality: encoding and line endings differ.', WARN, 'w2'), ('Myth: one character = one byte', 'Reality: UTF-8 uses up to four.', BAD, 'w3'),
          ('Myth: a terminal variable reaches all', 'Reality: only exported ones reach children.', VIO, 'w4'), ('Myth: not found = not installed', 'Reality: it may be outside PATH.', GOOD, 'w5')]
    for i, (a, b, col, cid) in enumerate(it): E.append(Pop(card(840, 210, col, a, [(b, TXT)], 34, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 240, C[cid]))
    E.append(takeaway('Check before you assume.', 860, C['w6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Check yourself on six points.', C['ru1'])
    items = [('Explains bits, bytes, hex', 'ru3'), ('Text vs program with file', 'ru4'), ('Bytes vs characters in UTF-8', 'ru5'), ('Removes hidden CR endings', 'ru6'), ('Absolute and relative paths', 'ru7'), ('Exports a variable, fixes PATH', 'ru8')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 150
        E.append(Pop(card(840, 120, [ACC, VIO, GOOD, WARN, BAD, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid]))
        E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 36, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 830, C['ru9'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In the virtual machine you built.', C['y1'])
    it = [('1  xxd', 'Bytes of your first name', ACC, 'y2'), ('2  Accent', 'Bytes, then characters', VIO, 'y3'), ('3  CRLF', 'Make, find, remove', WARN, 'y4'), ('4  export', 'Prove a child sees it', GOOD, 'y5'), ('5  ~/bin', 'Script, run by name', PINK, 'y6')]
    for i, (n, s, col, cid) in enumerate(it): E.append(Pop(card(540, 215, col, n, [(s, TXT)], 44, 32, True), 100 + (i % 3) * 590, 330 + (i // 3) * 245, C[cid]))
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['y7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['z1'])]
    qs = [('How many bits make a byte, and what is hex?', 'z2'), ('Why can a word have more bytes than characters?', 'z3'), ('What does command not found usually mean?', 'z4'), ('A variable versus an exported variable?', 'z8')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['z9'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['z9'] + 0.2))
    E.append(El(T('Objective covered: MC02-O06  ·  bytes, text, files, variables, paths', 'b', 28, TXT, maxw=960), 220, 748, C['z9'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['z5']))
    E.append(El(T('Next: server components and failure symptoms', 'x', 46, ACC, maxw=1600), 100, 960, C['z6'])); E.append(Pop(badge('SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['z7']))
    return E
FN = dict(hook=s_hook, bits=s_bits, xxd=s_xxd, text=s_text, kinds=s_kinds, enc=s_enc, encdemo=s_encdemo, eol=s_eol, eoldemo=s_eoldemo, paths=s_paths, pathdemo=s_pathdemo, envvars=s_envvars, envdemo=s_envdemo,
          pathvar=s_pathvar, pathrun=s_pathrun, errors=s_errors, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(bits=('gear', ACC), xxd=('eye', GOOD), text=('question', VIO), kinds=('eye', GOOD), enc=('swap', VIO), encdemo=('eye', GOOD), eol=('loop', WARN), eoldemo=('eye', GOOD), paths=('steps', ACC), pathdemo=('eye', GOOD),
           envvars=('link', ACC), envdemo=('eye', GOOD), pathvar=('steps', WARN), pathrun=('eye', GOOD), errors=('question', BAD), myths=('question', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
