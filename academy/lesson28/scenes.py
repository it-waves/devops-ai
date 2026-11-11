def s_hook(C, D, dur):
    E = [El(T('A server is made of files.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Configs', 'settings as text', ACC), ('Logs', 'what happened', VIO), ('Scripts and data', 'what it runs on', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('Make. Read. Move. Edit. Safely.', 850, C['h3'], GOOD, 1600)); return E
def s_hook(C, D, dur):
    E = [El(T('A server talks in text.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Logs', 'thousands of lines', VIO), ('Lists', 'names, files, users', ACC), ('Configs', 'settings as text', WARN)]):
        E.append(Pop(card(900, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 1.8))
    E.append(takeaway('Redirect. Pipe. Search. Count. Pack.', 850, C['h3'], GOOD, 1600)); return E
s_redirect = _lab('Redirect output', 'Send output to a file instead of the screen.', 'r1', RB, [('r1', '>', 'Replace the file', ACC), ('r3', '>>', 'Add to the end', VIO), ('r5', '2>', 'Errors only', WARN)])
s_pipe = _lab('Pipes', 'Output of one command feeds the next.', 'p1', RB, [('p1', 'a | b', 'Pipe into next', ACC), ('p3', '| wc -l', 'Count the lines', VIO), ('p5', 'find | wc -l', 'Chain commands', WARN)])
s_grep = _lab('Search with grep', 'Print only the lines that match.', 'g1', RB, [('g1', 'grep word file', 'Matching lines', ACC), ('g2', '-c', 'Count matches', VIO), ('g3', '-n', 'Line numbers', WARN), ('g4', '-i', 'Ignore case', PINK), ('g5', '-v', 'Everything else', GOOD), ('g6', '-r', 'Whole folder', BAD)])
s_sortcut = _lab('Sort, count and cut', 'Small tools for lists and tables.', 't1', RB, [('t1', 'sort', 'Put in order', ACC), ('t2', 'uniq -c', 'Count repeats', VIO), ('t4', 'sort -rn', 'Biggest first', WARN), ('t5', 'cut -d, -f1', 'One column', PINK)])
s_archive = _lab('Pack with tar', 'Back up a folder in one file.', 'a1', RB, [('a1', 'tar -czf', 'Create, compress', ACC), ('a3', 'tar -tzf', 'List contents', VIO), ('a5', 'tar -xzf -C', 'Extract to a folder', WARN)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: > adds to a file', 'One arrow replaces. Two add.', 'my2'), ('Myth: a pipe saves a file', 'A pipe feeds a command.', 'my3'), ('Myth: grep edits the file', 'It only reads and prints.', 'my4'), ('Myth: tar compresses alone', 'The z flag compresses.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Arrow to file. Pipe to command.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Redirect: > and >>', 'b2'), ('Chain commands with a pipe', 'b3'), ('grep with two flags', 'b4'), ('sort and count repeats', 'b5'), ('Pack and unpack with tar', 'b6'), ('Explain each tar flag', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'In your own virtual machine. Practice folder only.', C['z1'])
    it = [('1  Redirect', 'ls /etc > and >>', PINK, 'z2'), ('2  Pipe', 'count the lines', ACC, 'z3'), ('3  grep', 'count, number', WARN, 'z4'), ('4  Count', 'sort, uniq -c', VIO, 'z5'), ('5  tar', 'pack, list, restore', GOOD, 'z6'), ('6  Compare', 'one sentence', BAD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which arrow adds to the end of a file?', 'f12'), ('What does a pipe connect?', 'f13'), ('Which grep flag counts matching lines?', 'f14'), ('Which tar flag extracts?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O03', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: users, permissions and SSH keys', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, redirect=s_redirect, pipe=s_pipe, grep=s_grep, sortcut=s_sortcut, archive=s_archive, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(redirect=('eye', GOOD), pipe=('steps', ACC), grep=('eye', GOOD), sortcut=('eye', GOOD), archive=('eye', GOOD), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'grep': [('g2', 1, 2, 4, 400, ''), ('g3', 1, 1, 4, 300, '')],
 'sortcut': [('t3', 1, 1, 4, 330, '')],
}
