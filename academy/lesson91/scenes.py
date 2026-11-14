def s_hook(C, D, dur):
    E = [El(T('The jar is on your laptop. Publish it.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(700, 140, ACC, 'mvn deploy', [('upload to the shared repo', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(700, 140, WARN, 'snapshot or release', [('two kinds of version', TXT)], 46, 30), 100, 480, C['h3']))
    E.append(Pop(card(760, 180, BAD, 'HTTP 409', [('release already exists', TXT)], 52, 40), 900, 440, C['h4']))
    E.append(Pop(card(1100, 140, VIO, 'CloudCart v0  ·  cart-core', [('one module becomes a shared package', TXT)], 46, 30), 100, 660, C['h6']))
    E.append(takeaway('Publish once. Never overwrite a release.', 900, C['h6'] + 1.0, GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
s_what = _list('Install vs deploy', 'Snapshot or release.', 'a1', [('install', 'copies the jar into your own ~/.m2', ACC, 'a1'), ('deploy', 'uploads it to the shared repository', VIO, 'a1'), ('-SNAPSHOT', 'work in progress: upload again and again', WARN, 'a3'), ('release', 'final: can never be replaced', GOOD, 'a4')], 'The pom says where: distributionManagement.', 'a5')
s_rule = _list('Why a release is immutable', 'Same version, same code. Always.', 'b1', [('people built on it', 'old builds must stay repeatable', ACC, 'b1'), ('409 Conflict', 'the repository refuses the overwrite', BAD, 'b3'), ('fix: 1.0.1', 'publish a new version, never overwrite', GOOD, 'b3'), ('snapshot', 'a timestamp makes each upload a new file', VIO, 'b4')], 'Same login as last lesson: server id + env password.', 'b5')
def s_task(C, D, dur):
    E = head('Your lab task', 'lab91.sh: real Nexus plus a project to publish. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab91.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Wizard + repos', [('corp-snapshots', TXT), ('corp-releases', TXT)], 'k4', ACC), ('2  Snapshot', [('export NEXUS_PASS', TXT), ('mvn -s ... deploy', TXT)], 'k4', VIO), ('3  Release', [('version 1.0.0', TXT), ('deploy', TXT)], 'k5', GOOD), ('4  Again', [('409: conflict.txt', TXT), ('SHA-1: sha1.txt', TXT)], 'k6', BAD), ('5  Next + why', [('1.0.1, deploy', TXT), ('why.txt', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', WARN)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('Snapshot vs release', 'q3'), ('Why 409 happens', 'q4'), ('Fix = new version', 'q5'), ('Repos made in the UI', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Repos (UI)', 'create both in the web page', ACC, 'z3'), ('3  Deploy', 'snapshot, then release', VIO, 'z4'), ('4  Again', '409, SHA-1 from Browse', WARN, 'z5'), ('5  Next + check', '1.0.1, why.txt, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Install vs deploy?', 'f12'), ('Which can be uploaded twice?', 'f13'), ('What does 409 mean?', 'f14'), ('Bug in a release?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC10-O07', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: diagnose build failures', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_deploy = _lab('Live on real Nexus: wizard, repos, deploy, 409, proxy', 'A browser and a terminal, one continuous recording.', 'u0', RB, [('u1', 'login + wizard', 'real first-run setup', ACC), ('t1', 'tour of the UI', 'sidebar, repositories, types', VIO), ('r2', 'create repos', 'snapshot + release policies', WARN), ('d3b', 'mvn deploy', 'snapshot twice, release once', GOOD), ('d7b', 'deploy again', '409 Conflict', BAD), ('v3', 'browse + SHA-1', 'what arrived', ACC), ('x2', 'advanced: group', 'maven-public members', VIO), ('x5', 'advanced: proxy cache', 'Central, stored by Nexus', PINK)])
FN = dict(hook=s_hook, what=s_what, rule=s_rule, deploy=s_deploy, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(what=('link', ACC), rule=('test', BAD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'deploy': [('d1b', 3, 1, 60, 330, 'SAME ID'), ('d1b', 7, 1, 60, 330, ''), ('d3b', 2, 2, 0, 1070, 'TIMESTAMP'), ('d4b', 2, 2, 0, 1070, 'BUILD 2'), ('d6b', 2, 1, 0, 1070, 'NO TIMESTAMP'), ('d7b', 2, 1, 0, 1070, '409')]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson91/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
