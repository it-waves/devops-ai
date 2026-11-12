def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h



def s_hook(C, D, dur):
    E = [El(T('Ship with confidence', 'x', 72), 100, 130, C['y1'])]
    E.append(Pop(card(1100, 140, BAD, 'Friday, 5 pm', [('a small push, and the team build breaks', TXT)], 44, 32), 100, 290, C['y1'] + 2.0))
    for i, (a, b, col) in enumerate([('checks', 'a script that says safe or not', ACC), ('gate + CI', 'bad changes stop early', VIO), ('tags', 'every release has a version', GOOD)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 470 + i * 150, C['y2'] + i * 3.0))
    E.append(takeaway('Lab and checker at the end.', 960, C['y4'], GOOD, 1700)); return E
def s_model(C, D, dur):
    E = head('The release workflow', 'Every change walks the same path.', C['d1']); E.append(ill(C['d1'] + 0.2, 1400, 170))
    steps = [('Branch', ACC), ('Check', VIO), ('Review', WARN), ('Merge', PINK), ('Tag', GOOD)]
    for i, (n, col) in enumerate(steps): E.append(Pop(card(320, 120, col, n, [], 40), 100 + i * 345, 340, C['d1'] + 1.5 + i * 1.2))
    it = [('exit code', '0 means safe, anything else means stop', ACC, 'd2'), ('local gate', 'checks on your computer, in seconds', VIO, 'd3'), ('CI', 'the same checks on the server, every pull request', WARN, 'd4'), ('git tag', 'major.minor.patch on one commit', GOOD, 'd5')]
    for i, (n, s_, col, cid) in enumerate(it): E.append(Pop(card(1700, 105, col, n, [(s_, TXT)], 38, 30), 100, 520 + i * 125, C[cid]))
    return E
s_checks = _lab('Automated checks', 'A script that answers: is this change safe?', 'ck1', RB, [('ck3', './check.sh', 'Syntax, markers, tests', ACC), ('ck5', 'broken line added', 'The check fails', BAD), ('ck6', 'echo $?', 'Exit code 1 means fail', WARN), ('ck7', 'git restore', 'Undo the mistake', VIO), ('ck8', './check.sh', 'checks passed', GOOD)])
s_gate = _lab('A pre-push gate', 'Git runs the check before every push.', 'g1', RB, [('g2', 'pre-push hook', 'Runs check.sh first', ACC), ('g3', 'core.hooksPath', 'Turns the gate on', VIO), ('g6', 'git push', 'Blocked: bad commit stays home', BAD), ('g7', 'reset --hard', 'Private commit: safe to drop', WARN), ('g11', 'git push', 'Check passes, push goes through', GOOD)])
s_ci = _lab('Checks in CI', 'The same script, on the server.', 'cw0', RB, [('cw2', 'on: pull_request', 'Runs on every pull request', ACC), ('cw3', 'runs-on', 'A fresh Ubuntu machine', VIO), ('cw4', 'actions/checkout', 'Gets your code', WARN), ('cw5', 'run: ./check.sh', 'One check, two places', GOOD), ('cw6', 'branch protection', 'Red check: no merge', BAD)])
s_release = _lab('Tags and releases', 'A version is a label on one commit.', 'r1', RB, [('r2', 'git tag', 'List the releases', ACC), ('r3', 'v1.0.0..HEAD', 'What changed: release notes', VIO), ('r4', 'git describe', 'Distance from the last tag', WARN), ('r5', 'tag -a v1.1.0', 'Annotated: author, date, message', PINK), ('r6', 'git push origin v1.1.0', 'Tags do not travel alone', GOOD)])
def s_task(C, D, dur):
    E = head('Your lab task', 'lab65.sh builds the shop. lab check judges it.', C['t1']); E.append(ill(C['t1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['t2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab65.sh', 'mono', 32, TXT, align='left'), 140, 360, C['t2'] + 0.3, anim='fade'))
    steps = [('lab up', 'a shop repo and a shared copy', 't3', ACC), ('1  fix', 'run check.sh, fix the bug', 't4', VIO), ('2  gate', 'core.hooksPath .githooks', 't5', WARN), ('3  push', 'main to origin', 't6', PINK), ('4  tag', 'annotated v1.0.0, pushed', 't7', BAD), ('5  answers.txt', 'major, minor or patch?', 't8', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 230, C[cid]))
    E.append(takeaway('Check, gate, tag.', 940, C['t9'], GOOD, 1700)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['rb1'])
    items = [('Five PASS lines', 'rb2'), ('Fixed in a new commit', 'rb3'), ('Gate on, push through it', 'rb4'), ('Annotated tag on origin', 'rb5'), ('Major, minor, patch', 'rb6'), ('lab down, removed', 'rb7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['rb8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Fix', 'run the check, fix the bug', ACC, 'z3'), ('3  Gate', 'core.hooksPath', WARN, 'z4'), ('4  Push', 'main to origin', VIO, 'z5'), ('5  Tag + check', 'v1.0.0, answers, lab check', BAD, 'z6'), ('6  Clean up', 'lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What does an exit code tell you?', 'f12'), ('Why run checks locally and in CI?', 'f13'), ('What does a pre-push gate do?', 'f14'), ('Major, minor and patch: what are they?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC07-O09', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: the Git and GitHub mastery lesson', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, model=s_model, checks=s_checks, gate=s_gate, ci=s_ci, release=s_release, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(model=('board', ACC), checks=('test', GOOD), gate=('code', WARN), ci=('doc', VIO), release=('doc', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson65/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
