def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))



def s_hook(C, D, dur):
    E = [El(T('Python for DevOps', 'x', 72), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Isolate', 'one environment per project', ACC), ('Pin', 'exact versions in a file', GOOD), ('Rebuild', 'anyone, anywhere, same result', WARN)]):
        E.append(Pop(card(1100, 140, col, a, [(b, TXT)], 44, 32), 100, 290 + i * 160, C['h2'] + i * 3.5))
    E.append(takeaway('Works on my machine becomes works on every machine.', 850, C['h3'], GOOD, 1700)); return E
def s_why(C, D, dur):
    E = head('Why virtual environments', 'Packages belong to the project, not the machine.', C['w1']); E.append(ill(C['w1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 120, BAD, 'System Python  ·  /usr', [('owned by Ubuntu, used by system tools', TXT)], 36, 28), 100, 330, C['w2']))
    for i, (n, pk, col) in enumerate([('Project A', 'requests 2.31', ACC), ('Project B', 'requests 2.34', VIO), ('Project C', 'pyyaml 6.0', GOOD)]):
        E.append(Pop(card(540, 215, col, n + '  ·  .venv', [(pk, TXT), ('own Python, own packages', MUTED)], 36, 30, True), 100 + i * 580, 490 + 0, C['w3'] + i * 0.4 if i < 2 else C['w4']))
    E.append(takeaway('Create. Activate. Install. Freeze.', 800, C['w5'], GOOD, 1700)); return E
def s_task(C, D, dur):
    E = head('Get the lab and task', 'Everything is in the repository.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    rows = [('Repository', 'github.com/it-waves/devops-ai', 't2', ACC), ('Task file', 'academy/lesson47/TASK.md', 't3', VIO), ('Checker', 'academy/lesson47/check47.sh', 't3', GOOD)]
    for i, (a, b, cid, col) in enumerate(rows): E.append(Pop(card(1700, 100, col, '', [], 4), 100, 330 + i * 115, C[cid] + i * 0.2)); E.append(El(T(a, 'b', 28, MUTED, align='left'), 140, 352 + i * 115, C[cid] + 0.3 + i * 0.2, anim='fade')); E.append(El(T(b, 'mono', 30, TXT, align='left'), 420, 350 + i * 115, C[cid] + 0.4 + i * 0.2, anim='fade'))
    steps = [('sudo apt install python3-venv', 't4'), ('git clone https://github.com/it-waves/devops-ai', 't4'), ('cd devops-ai/academy/lesson47', 't5'), ('bash check47.sh PATH/TO/servers', 't6')]
    E.append(Pop(glass(1700, 4 * 46 + 48, WARN), 100, 700, C['t4']))
    for i, (t, cid) in enumerate(steps): E.append(El(T('$ ' + t, 'mono', 28, TXT, align='left'), 130, 724 + i * 46, C[cid] + 0.3 + 0.35 * i, anim='fade'))
    E.append(El(T('Needs: Ubuntu VM, python3. Your own machine only. Report: commands + output.', 'm', 26, MUTED, maxw=1700), 100, 960, C['t7'], anim='fade')); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Checker: five PASS', 'b2'), ('Pinned requirements', 'b3'), ('Fresh env matches file', 'b4'), ('.venv ignored by Git', 'b5'), ('Cleanup proof', 'b6'), ('Own VM, no system pip', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only.', C['z1'])
    it = [('1  Create', 'servers folder and .venv', PINK, 'z2'), ('2  Install', 'activate, one package', ACC, 'z3'), ('3  Freeze', 'requirements.txt', WARN, 'z4'), ('4  Layout', 'src, tests, .gitignore', VIO, 'z5'), ('5  Rebuild', 'fresh env, diff is empty', BAD, 'z6'), ('6  Check', 'five PASS, then clean up', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why use a virtual environment?', 'f12'), ('Which command turns it on?', 'f13'), ('What does pip freeze give you?', 'f14'), ('Why is .venv not in Git?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC06-O01', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: types, collections and functions', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_setup = _lab('Check Python, create a venv', 'Real Python 3.12, a real environment.', 's1', RB, [('s1', 'python3 --version', 'Ubuntu 24.04 ships 3.12', ACC), ('s2', 'sys.prefix', 'System Python is /usr', BAD), ('s4', 'mkdir, cd', 'The project folder', VIO), ('s5', 'python3 -m venv', 'Create .venv', WARN), ('s6', 'ls -a', 'A hidden .venv folder', GOOD)])
s_activate = _lab('Activate and install', 'The prompt tells you it is on.', 'a1', RB, [('a1', 'source activate', 'Turn it on', ACC), ('a2', 'which python', 'Inside the project', VIO), ('a3', 'pip install', 'From PyPI', WARN), ('a4', 'pip list', 'Package + dependencies', GOOD), ('a5', 'pip show', 'Name and version', PINK)])
s_deps = _lab('Freeze the versions', 'The recipe for the environment.', 'd1', RB, [('d1', 'pip freeze', 'Exact versions', ACC), ('d2', '> requirements.txt', 'Save the recipe', WARN), ('d3', 'cat', 'Five pinned lines', VIO), ('d4', 'deactivate', 'Leave the env', PINK), ('d5', 'import requests', 'System Python: no', BAD)])
s_repro = _lab('Rebuild from the file', 'A teammate gets only the recipe.', 'r1', RB, [('r1', 'ls', 'No .venv, just files', ACC), ('r2', 'venv .venv', 'A fresh environment', VIO), ('r4', 'pip install -r', 'Read the list', WARN), ('r5', 'pip freeze | diff', 'Compare with the file', GOOD), ('r6', 'echo $?', 'Exit status 0', VIO)])
s_layout = _lab('Project layout and checker', 'Source, tests, and an ignore file.', 'l1', RB, [('l1', 'mkdir -p', 'src and tests', ACC), ('l2', '__init__.py', 'A package', VIO), ('l3', '.gitignore', 'Ignore .venv', WARN), ('l4', 'find', 'The layout', PINK), ('l5', 'check47.sh', 'Five PASS lines', GOOD)])
s_cleanup = _lab('Cleanup with proof', 'An environment is just a folder.', 'c1', RB, [('c1', 'ls -a', 'Before', ACC), ('c3', 'rm -rf', 'Delete the project', BAD), ('c4', 'ls', 'Proof: gone', GOOD)])
FN = dict(hook=s_hook, why=s_why, setup=s_setup, activate=s_activate, deps=s_deps, repro=s_repro, layout=s_layout, cleanup=s_cleanup, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('board', ACC), setup=('gear', ACC), activate=('gear', VIO), deps=('board', WARN), repro=('test', GOOD), layout=('board', VIO), cleanup=('eye', GOOD), task=('gear', VIO), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'setup': [('s2', 1, 1, 4, 215, ''), ('s3', 1, 1, 4, 70, ''), ('s7', 1, 1, 110, 188, '')],
 'activate': [('a2', 1, 1, 4, 115, ''), ('a3', 1, 1, 4, 675, ''), ('a5', 7, 1, 4, 470, ''), ('a6', 1, 1, 4, 330, '')],
 'deps': [('d2', 1, 5, 4, 402, ''), ('d4', 1, 5, 4, 402, ''), ('d6', 3, 1, 4, 720, '')],
 'repro': [('r7', 1, 1, 4, 30, '')],
 'layout': [('l6', 1, 5, 4, 590, '')],
 'cleanup': [('c5', 1, 1, 4, 190, '')],
}

import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson47/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
CMDLEN['s2'] = len('python3 -c "import sys; print(sys.prefix)"')
