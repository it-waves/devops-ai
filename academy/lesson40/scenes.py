def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Search, reshape, find', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('grep', 'search lines', ACC), ('cut / sort', 'columns and order', VIO), ('sed / awk', 'replace and calculate', WARN), ('find', 'locate files', GOOD)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 255 + i * 150, C['h2'] + i * 3.4))
    E.append(takeaway('Small tools. Big jobs.', 880, C['h3'], GOOD, 1700)); return E
s_grep = _lab('Search with grep', 'Print the lines that match.', 'r1', RB, [('r1', 'cat app.log', 'The log', ACC), ('r2', 'grep ERROR app.log', 'Matching lines', GOOD), ('r3', 'grep -c INFO', 'Count: -c', VIO), ('r4', 'grep -v INFO', 'Invert: -v', WARN), ('r5', 'grep -n timeout', 'Line number: -n', PINK), ('r6', 'grep -E "WARN|ERROR"', 'Either word: -E', BAD)])
s_cutsort = _lab('Cut and sort', 'Pick columns, put lines in order.', 'p1', RB, [('p1', 'cat users.csv', 'name, team, age', ACC), ('p2', 'cut -d, -f1', 'Pick a column', GOOD), ('p3', 'sort -t, -k3 -n', 'Sort by number', VIO), ('p4', '... | sort | uniq -c', 'Count repeats', WARN)])
s_sed = _lab('Replace with sed', 'Search and replace in a stream.', 's1', RB, [('s1', 'cat config.txt', 'Three settings', ACC), ('s2', "sed 's/dev/prod/'", 'Prints the change', GOOD), ('s3', 'cat config.txt', 'File unchanged', VIO), ('s4', "sed -i 's/8080/9090/'", '-i edits the file', WARN), ('s5', 'cat config.txt', 'Now changed', PINK), ('s6', "sed '/mode/d'", 'Delete matching lines', BAD)])
s_awk = _lab('Calculate with awk', 'Fields, conditions, totals.', 'a1', RB, [('a1', 'cat users.csv', 'The table', ACC), ('a2', "awk -F, '{print $1}'", 'Print field one', GOOD), ('a3', 'NR > 1 && $3 > 30', 'Test a condition', VIO), ('a4', 'sum += $3 ... END', 'Average age', WARN)])
s_find = _lab('Find files', 'Search folders by name and age.', 'n1', RB, [('n1', 'ls -R', 'Two subfolders', ACC), ('n2', 'find . -name "*.log"', 'By name', GOOD), ('n3', '-mtime +7', 'Older than 7 days', VIO), ('n4', '-exec wc -l {} +', 'Run on each match', WARN)])
s_build = _lab('Put it together', 'A small log report.', 'w1', RB, [('w1', 'cat app.log', 'The log', ACC), ('w2', 'awk | sort | uniq -c', 'Count the levels', GOOD), ('w3', 'grep ERROR | awk', 'Time and cause', VIO)])
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: sed edits the file', 'Only -i edits it.', 'my2'), ('Myth: grep reads files only', 'It filters pipes too.', 'my3'), ('Myth: uniq removes all', 'Only neighbours: sort first.', 'my4'), ('Myth: find needs a name', 'Type, size and age work too.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 38, 30), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Search. Cut. Replace. Calculate. Find.', 800, C['my6'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('grep: -c -v -n', 'b2'), ('cut and sort', 'b3'), ('sed and -i', 'b4'), ('awk totals', 'b5'), ('find and -exec', 'b6'), ('Join with pipes', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Type every command.', C['z1'])
    it = [('1  grep', 'count, invert, number', PINK, 'z2'), ('2  cut, sort', 'column, by number', ACC, 'z3'), ('3  sed', 'replace, then -i on a copy', WARN, 'z4'), ('4  awk', 'sum and average', VIO, 'z5'), ('5  find', 'name, age, wc -l', BAD, 'z6'), ('6  Pipeline', 'count the levels', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which grep flag inverts?', 'f12'), ('Why sort before uniq?', 'f13'), ('How does sed edit a file?', 'f14'), ('What does NR hold in awk?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC05-O04', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: pipes and redirection', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = {'hook': s_hook, 'grep': s_grep, 'cutsort': s_cutsort, 'sed': s_sed, 'awk': s_awk, 'find': s_find, 'build': s_build, 'myths': s_myths, 'rubric': s_rubric, 'yourturn': s_yourturn, 'recap': s_recap}
_GL = {'grep': ('question', ACC), 'cutsort': ('board', VIO), 'sed': ('gear', WARN), 'awk': ('gear', GOOD), 'find': ('question', ACC), 'build': ('test', GOOD), 'myths': ('question', BAD), 'rubric': ('test', GOOD), 'yourturn': ('board', VIO)}
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'grep': [('r2', 2, 1, 308, 386, ''), ('r2', 5, 1, 308, 386, ''), ('r3', 1, 2, 4, 690, ''), ('r4', 1, 1, 4, 22, ''), ('r5', 1, 3, 4, 690, ''), ('r6', 1, 1, 4, 40, ''), ('r7', 1, 3, 4, 690, '')],
 'cutsort': [('p2', 1, 6, 4, 65, ''), ('p3', 1, 6, 4, 70, ''), ('p4', 2, 2, 4, 190, ''), ('p5', 1, 3, 4, 150, '')],
 'sed': [('s2', 3, 1, 4, 126, ''), ('s3', 3, 1, 4, 142, ''), ('s4', 3, 1, 4, 126, ''), ('s6', 2, 1, 4, 142, ''), ('s7', 1, 2, 4, 220, '')],
 'awk': [('a2', 1, 1, 4, 200, ''), ('a3', 1, 6, 4, 70, ''), ('a4', 1, 3, 4, 110, ''), ('a5', 2, 1, 4, 60, '')],
 'find': [('n2', 5, 1, 4, 175, ''), ('n2', 8, 1, 4, 80, ''), ('n3', 1, 3, 4, 170, ''), ('n4', 1, 1, 4, 172, ''), ('n5', 1, 4, 4, 210, '')],
 'build': [('w2', 1, 6, 308, 386, ''), ('w3', 1, 3, 4, 205, ''), ('w4', 1, 2, 4, 250, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson40/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
