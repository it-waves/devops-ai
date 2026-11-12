def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Python building blocks', 'x', 72), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Types and collections', 'int, str, list, dict', ACC), ('Control flow', 'if, else, for loops', GOOD), ('Functions and modules', 'reuse, import, structure', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 2.2))
    E.append(takeaway('The base for every tool in this masterclass.', 850, C['h3'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('Why Python for DevOps', 'When data has structure, use a language that understands it.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(820, 230, VIO, 'Shell', [('great for gluing commands', TXT), ('text in, text out', MUTED)], 44, 32, True), 100, 340, C['w1'] + 0.5))
    E.append(Pop(card(820, 230, ACC, 'Python', [('lists, dictionaries, types', TXT), ('readable errors, testable code', MUTED)], 44, 32, True), 980, 340, C['w3']))
    E.append(Pop(card(1700, 150, WARN, 'DevOps data is already shaped like Python', [('servers = list   ·   settings = dictionary   ·   API answer = both', TXT)], 38, 30), 100, 620, C['w4']))
    E.append(takeaway('Five building blocks. Everything else builds on them.', 850, C['w5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Get the lab and task', 'Everything is in the repository.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 't2', ACC), ('Folder', 'academy/lesson48', 't3', VIO), ('Files', 'TASK.md  data48.py  expected48.txt  check48.sh', 't3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 't3'), ('cd devops-ai/academy/lesson48', 't3'), ('# write inventory.py: busy(), counts, average', 't4'), ('bash check48.sh .      # four PASS lines', 't5')]
    E.append(Pop(glass(1700, 4 * 46 + 48, WARN), 100, 700, C['t3']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, python3. Your own machine only. No peeking at the solution first.', 'm', 26, MUTED, maxw=1700), 100, 960, C['t6'], anim='fade')); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Checker: four PASS', 'b2'), ('busy(servers, limit)', 'b3'), ('Counts: dict + loop', 'b4'), ('Data imported', 'b5'), ('Complete report', 'b6'), ('Own VM only', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only.', C['z1'])
    it = [('1  Get files', 'lesson48 folder, venv on', PINK, 'z2'), ('2  Import', 'from data48 import SERVERS', ACC, 'z3'), ('3  busy()', 'function with a limit', WARN, 'z4'), ('4  Count', 'dict and a for loop', VIO, 'z5'), ('5  Print', 'under the main guard', BAD, 'z6'), ('6  Check', 'four PASS, then report', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why is port == "8080" False?', 'f12'), ('Dictionary value with a default?', 'f13'), ('What marks lines inside a loop?', 'f14'), ('Why the __main__ guard?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC06-O02', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: files, JSON, YAML, CSV and config', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_repl = _lab('Types in the REPL', 'int and str, and a classic trap.', 'r1', RB, [('r2', 'port = 8080', 'A whole number', ACC), ('r3', 'type(port)', 'class int', VIO), ('r5', 'type(name)', 'class str', WARN), ('r6', 'port == "8080"', 'False: number vs text', BAD), ('r7', 'int("8080") + 1', 'Convert: 8081', GOOD)])
s_coll = _lab('Lists and dictionaries', 'Order, and lookup by name.', 'c1', RB, [('c2', 'ports = [...]', 'A list, in order', ACC), ('c3', '.append(22)', 'Add an item', VIO), ('c5', 'ports[0]', 'Index starts at 0', WARN), ('c6', 'server = {...}', 'A dictionary', PINK), ('c8', '.get(key, default)', 'Safe lookup', GOOD), ('c9', 'KeyError', 'Missing key', BAD)])
s_script = _lab('Conditions and loops', 'for, if, else, and indentation.', 'p1', RB, [('p1', 'cat check.py', 'A list of pairs', ACC), ('p2', 'for / if / else', 'Indent = inside', WARN), ('p3', 'python3 check.py', 'web2 is busy', GOOD)])
s_func = _lab('Functions', 'def, parameters and return.', 'f1', RB, [('f1', 'cat funcs.py', 'def busy(...)', ACC), ('f2', 'return names', 'Gives back a list', VIO), ('f3', 'python3 funcs.py', "['web2']", GOOD)])
s_mod = _lab('Modules and imports', 'The standard library, and your own files.', 'm1', RB, [('m1', 'import json', 'Standard library', ACC), ('m2', 'import funcs', 'Your file is a module', VIO), ('m3', '__main__ guard', 'No output on import', WARN), ('m4', 'ModuleNotFound', 'Missing install?', BAD)])
FN = dict(hook=s_hook, why=s_why, repl=s_repl, coll=s_coll, script=s_script, func=s_func, mod=s_mod, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('board', ACC), repl=('gear', ACC), coll=('board', VIO), script=('test', WARN), func=('gear', VIO), mod=('board', GOOD), task=('gear', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'repl': [('r4', 1, 1, 4, 205, ''), ('r6', 1, 1, 4, 205, ''), ('r7', 1, 1, 4, 80, ''), ('r8', 1, 1, 4, 70, '')],
 'coll': [('c5', 1, 1, 4, 312, ''), ('c6', 1, 1, 4, 50, ''), ('c8', 1, 1, 4, 50, ''), ('c9', 1, 1, 4, 80, ''), ('c10', 3, 1, 4, 240, '')],
 'script': [('p3', 2, 1, 4, 190, '')],
 'func': [('f3', 1, 1, 4, 132, '')],
 'mod': [('m2', 1, 1, 4, 132, ''), ('m4', 3, 1, 4, 720, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson48/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
CMDLEN['m1'] = len('python3 -c "import json; print(json.dumps({' + "'a'" + ': 1}))"')
