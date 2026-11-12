def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))




def s_hook(C, D, dur):
    E = [El(T('Files, formats and config', 'x', 72), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Files', 'open, read, write, append', ACC), ('JSON  ·  YAML  ·  CSV', 'the formats of APIs, tools and exports', GOOD), ('Environment variables', 'settings and secrets, outside the code', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 2.2))
    E.append(takeaway('Your code meets real data today.', 850, C['h3'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('Why these formats matter', 'Almost every tool keeps its settings in one of them.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(540, 215, ACC, 'YAML', [('Ansible, Kubernetes,', TXT), ('Compose, Actions', MUTED)], 44, 32, True), 100, 340, C['w2']))
    E.append(Pop(card(540, 215, VIO, 'JSON', [('APIs speak JSON', TXT), ('config and logs too', MUTED)], 44, 32, True), 690, 340, C['w3']))
    E.append(Pop(card(540, 215, WARN, 'CSV', [('spreadsheets and', TXT), ('monitoring exports', MUTED)], 44, 32, True), 1280, 340, C['w3'] + 2.5))
    E.append(Pop(card(1700, 150, GOOD, 'Environment variables', [('secrets and switches, outside the code', TXT)], 38, 30), 100, 620, C['w4']))
    E.append(takeaway('Read safely. Convert types. Works on any machine.', 850, C['w5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Get the lab and task', 'Everything is in the repository.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 't2', ACC), ('Folder', 'academy/lesson49', 't3', VIO), ('Files', 'TASK.md  servers49.csv  config49.yaml  check49.sh', 't3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('git clone https://github.com/it-waves/devops-ai', 't3'), ('cd devops-ai/academy/lesson49 && pip install pyyaml', 't3'), ('# write report.py: YAML + CSV + env -> JSON', 't4'), ('bash check49.sh .      # four PASS lines', 't5')]
    E.append(Pop(glass(1700, 4 * 46 + 48, WARN), 100, 700, C['t3']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, python3, your venv. Your own machine only. No peeking at the solution first.', 'm', 26, MUTED, maxw=1700), 100, 960, C['t6'], anim='fade')); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Checker: four PASS', 'b2'), ('Limit from YAML: safe_load', 'b3'), ('CPU converted with int', 'b4'), ('APP_ENV with a default', 'b5'), ('JSON via with + json.dump', 'b6'), ('Complete report, own VM', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only.', C['z1'])
    it = [('1  Get files', 'lesson49 folder, pip install pyyaml', PINK, 'z2'), ('2  YAML', 'limit via safe_load', ACC, 'z3'), ('3  CSV', 'DictReader, int(cpu)', WARN, 'z4'), ('4  Env', 'os.getenv with default', VIO, 'z5'), ('5  JSON', 'with open + json.dump', BAD, 'z6'), ('6  Check', 'four PASS, then report', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why open files with a with block?', 'f12'), ('Why convert values read from a CSV?', 'f13'), ('Which YAML loader is the safe one?', 'f14'), ('Environment variable with a default?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC06-O03', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: REST APIs, auth, timeouts, pagination', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_files = _lab('Reading and writing files', 'open, a mode, and a with block.', 'fl1', RB, [('fl1', 'cat files.py', 'with open(...)', ACC), ('fl2', 'modes: w  a  r', 'write, append, read', WARN), ('fl2', 'with = auto close', 'safe even on errors', VIO), ('fl3', 'cat notes.txt', 'same two lines', GOOD)])
s_json = _lab('JSON', 'Objects and lists become dicts and lists.', 'j1', RB, [('j1', 'cat servers.json', 'object + list', ACC), ('j4', 'json.load(file)', 'file to Python', VIO), ('j5', 'd["servers"][1]["name"]', 'key, index, key', WARN), ('j6', 'json.dumps(obj)', 'Python to text', GOOD)])
s_yaml = _lab('YAML', 'Indentation is the structure.', 'y1', RB, [('y1', 'cat config.yaml', 'no braces, no quotes', ACC), ('y3', 'import yaml', 'pip install pyyaml', VIO), ('y4', 'yaml.safe_load(file)', 'always the safe one', GOOD), ('y6', 'limit: 80 is an int', 'YAML keeps types', WARN)])
s_csv = _lab('CSV', 'Rows as dictionaries. Values are text.', 's1', RB, [('s1', 'cat servers.csv', 'header + rows', ACC), ('s4', 'csv.DictReader', 'one dict per row', VIO), ('s6', "'cpu': '91'", 'text, in quotes', BAD), ('s7', 'int(row["cpu"])', 'convert first', GOOD)])
s_env = _lab('Environment variables', 'Settings and secrets, outside the code.', 'e1', RB, [('e1', 'export LIMIT=80', 'set in the shell', ACC), ('e4', "os.getenv('LIMIT')", "'80' is text", WARN), ('e5', 'getenv + default + int', 'safe and typed', GOOD), ('e7', 'os.environ["TOKEN"]', 'KeyError: fail loudly', BAD)])
FN = dict(hook=s_hook, why=s_why, files=s_files, json=s_json, yaml=s_yaml, csv=s_csv, env=s_env, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('board', ACC), files=('gear', ACC), json=('board', VIO), yaml=('test', WARN), csv=('board', GOOD), env=('gear', VIO), task=('gear', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'files': [('fl3', 1, 2, 4, 150, '')],
 'json': [('j6', 1, 1, 4, 98, ''), ('j7', 1, 1, 4, 460, '')],
 'yaml': [('y6', 1, 1, 4, 50, ''), ('y7', 1, 1, 4, 248, '')],
 'csv': [('s6', 1, 1, 4, 30, ''), ('s7', 1, 1, 489, 657, ''), ('s8', 1, 1, 4, 50, '')],
 'env': [('e5', 1, 1, 4, 68, ''), ('e6', 1, 1, 4, 50, ''), ('e7', 1, 1, 4, 170, ''), ('e8', 4, 1, 4, 262, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson49/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
