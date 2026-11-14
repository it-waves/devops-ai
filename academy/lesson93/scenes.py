def s_hook(C, D, dur):
    E = [El(T('Old snapshots fill the disk.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(700, 140, WARN, '10 builds a day', [('thousands of files a year', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(700, 140, BAD, 'disk full', [('uploads stop mid-release', TXT)], 46, 30), 100, 480, C['h3']))
    E.append(Pop(card(760, 180, GOOD, 'a scheduled task', [('Nexus cleans up by itself', TXT)], 52, 38), 900, 440, C['h4']))
    E.append(Pop(card(1100, 140, ACC, 'Every screen, every click', [('highlighted on the real Nexus', TXT)], 46, 30), 100, 660, C['h5']))
    E.append(takeaway('Do not delete by hand. Schedule it.', 900, C['h6'] + 1.0, GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
s_why = _list('Two knobs decide what is deleted', 'Maven - Delete SNAPSHOT.', 'w1', [('snapshot', 'work in progress: safe to delete when old', WARN, 'w2'), ('minimum count', 'how many newest builds to always keep', ACC, 'w4'), ('retention (days)', 'older than this may be deleted', VIO, 'w5'), ('schedule', 'manual, hourly, daily, weekly, monthly, cron', PINK, 'w7')], 'Old enough AND not one of the newest.', 'w6')
def s_task(C, D, dur):
    E = head('Your lab task', 'lab93.sh: real Nexus, four builds waiting. lab check judges you.', C['a1']); E.append(ill(C['a1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['a2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab93.sh', 'mono', 32, TXT, align='left'), 140, 360, C['a2'] + 0.3, anim='fade'))
    steps = [('1  Look', [('Browse: four builds', TXT)], 'a3', ACC), ('2  Create task', [('Delete SNAPSHOT', TXT), ('keep 1, retention 0', TXT)], 'a4', VIO), ('3  Schedule', [('daily or weekly', TXT), ('a quiet hour', TXT)], 'a5', GOOD), ('4  Run it', [('last result OK', TXT), ('one build left', TXT)], 'a6', WARN), ('5  notes.txt', [('keep: ...', TXT), ('when: ...', TXT)], 'a7', PINK), ('6  Check + down', [('lab check', TXT), ('lab down', TXT)], 'a8', ACC)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 2 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Five points. All five to pass.', C['q1'])
    items = [('Task exists, on corp-snapshots', 'q2'), ('Ran: last result OK', 'q3'), ('One build left: the newest', 'q4'), ('Scheduled, not manual', 'q5'), ('notes.txt: keep + when', 'q6')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all five', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q7'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, open Nexus', PINK, 'z2'), ('2  Create', 'Delete SNAPSHOT, keep 1', ACC, 'z3'), ('3  Schedule + run', 'daily, then Run', VIO, 'z4'), ('4  Notes', 'browse, then notes.txt', WARN, 'z5'), ('5  Check', 'lab check', GOOD, 'z6'), ('6  Clean up', 'lab down', ACC, 'z6')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z7'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Why do snapshots pile up?', 'f12'), ('Which two settings decide?', 'f13'), ('Why did the blob count stay?', 'f14'), ('Never point it at releases: why?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Enrichment for MC10-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: the Maven wrapper', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live on real Nexus: pile, task, run, proof', 'A terminal and a browser, one continuous recording.', 'l0', RB, [('l2b', 'four builds', 'the pile in the terminal', ACC), ('v2', 'see them in Browse', 'tree of builds', VIO), ('k3', 'create the task', 'type, name, repo, knobs', WARN), ('k13', 'schedule it', 'daily at 02:00', GOOD), ('r2', 'run it', 'confirm, status, OK', PINK), ('p2', 'prove it', 'one build, API check', ACC)])
FN = dict(hook=s_hook, why=s_why, live=s_live, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(why=('test', ACC), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [('l2b', 2, 4, 0, 560, 'FOUR UPLOADS'), ('y1b', 3, 1, 0, 60, ''), ('y2b', 3, 3, 0, 700, 'OK + NEXT RUN')]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson93/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
