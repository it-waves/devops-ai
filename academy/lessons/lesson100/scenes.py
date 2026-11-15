def s_hook(C, D, dur):
    E = [El(T('Your build, on a clean machine.', 'x', 62), 100, 130, C['h1'])]
    E.append(Pop(card(760, 140, ACC, 'every push', [('built by a workflow', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(760, 160, WARN, 'read it, fix it', [('5 problems in a real workflow', TXT)], 52, 30), 100, 480, C['h3']))
    E.append(Pop(card(760, 160, VIO, 'a real run on GitHub', [('step by step in the UI', TXT)], 46, 30), 900, 440, C['h4']))
    E.append(Pop(card(1100, 140, GOOD, 'repair one alone', [('with a checker', TXT)], 46, 30), 100, 700, C['h5']))
    E.append(takeaway('CI = your build on a clean computer.', 900, C['h6'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
s_parts = _list('One file runs your build', 'A GitHub Actions workflow lives in .github/workflows.', 'a1', [('1  trigger', 'on: push, pull request, or a Run button', ACC, 'a2'), ('2  runner + steps', 'checkout, set up Java, run ./gradlew build', VIO, 'a3'), ('3  cache, secret, artifact', 'fast, safe, and the jar is kept', GOOD, 'a4')], 'The runner starts empty: the file must say everything.', 'a5', h=125, gap=145)
def s_task(C, D, dur):
    E = head('Your lab task', 'lab100.sh: a broken ci.yml. lab check judges you.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    steps = [('1  Trigger', [('push + pull_request', TXT)], 'k2', ACC), ('2  Java', [('checkout + Java 21', TXT)], 'k3', WARN), ('3  Cache', [('setup-gradle action', TXT)], 'k4', VIO), ('4  Secret', [('secrets.REPO_PASSWORD', TXT), ('no plain text', TXT)], 'k5', BAD), ('5  Artifact', [('upload-artifact', TXT), ('build/libs jar', TXT)], 'k6', GOOD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 330 + (i // 3) * 290, C[cid]))
    return E
def s_labinfo(C, D, dur):
    E = head('Where to find the lab', 'Pause here and write it down.', C['i1x']); E.append(ill(C['i1x'] + 0.2, 1400, 170))
    rows = [('1  Repository', 'github.com/it-waves/devops-ai  >  academy/lab', ACC, 'i2'), ('2  Files', 'lab100.sh   and   shortcuts100.sh', VIO, 'i3'), ('3  Install', 'sudo install -m 755 lab100.sh /usr/local/sbin/', GOOD, 'i4'), ('4  Short name', 'source shortcuts100.sh  then: lab up, lab check, lab down', WARN, 'i5'), ('5  You need', 'JDK, curl, python3, 1 GB memory, internet', PINK, 'i6'), ('6  Check + cleanup', 'lab check reads your yaml, builds locally. lab down removes all.', ACC, 'i7')]
    for i, (n, t, col, cid) in enumerate(rows):
        y = 320 + i * 118; E.append(Pop(card(1700, 94, col, n, [], 34), 100, y, C[cid])); E.append(El(T(t, 'm', 32, TXT, maxw=1180), 560, y + 26, C[cid] + 0.25, anim='fade'))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1x'])
    items = [('Five PASS lines', 'q2x'), ('Runs on push + pull request', 'q3x'), ('Java 21 + setup-gradle', 'q4x'), ('No plain text password', 'q5x'), ('Jar saved, local build passes', 'q6x'), ('lab down, nothing left', 'q7x')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8x'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, find 5 problems', PINK, 'z2'), ('2  Trigger + Java', 'push, PR, Java 21', ACC, 'z3'), ('3  Cache', 'add setup-gradle', VIO, 'z4'), ('4  Secret', 'no plain text password', WARN, 'z5'), ('5  Artifact + check', 'upload-artifact, lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Name three workflow triggers.', 'f12'), ('Why set up Java in the file?', 'f13'), ('Why no password in the file?', 'f14'), ('What does upload-artifact keep?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective: MC11-O06 Gradle in CI', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: diagnose Gradle failures', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_live = _lab('Live: read the workflow, find the mistakes, run the build', 'A real Gradle 8.14.3 build on the CloudCart cartcore project.', 'p0', RB, [('t1', '1  read the file', '16 lines, 5 problems', ACC), ('t2', '2  find them', 'main only, password, Java 8', BAD), ('t3', '3  run the build', 'what the runner runs', GOOD), ('t4', '4  the artifact', 'the jar in build/libs', VIO), ('t5', '5  the fix, part 1', 'triggers and a secret', WARN), ('t6', '6  the fix, part 2', 'Java 21, cache, upload', PINK)])

# ---- UI scene: real GitHub Actions captures (stills) with highlighted click targets ----
UIDIR = '/home/claude/academy/lesson100/ui'
_SC = 1.2; _OX, _OY = 192, 300
_shots = {}
def _shot(name):
    if name not in _shots:
        im = Image.open(f'{UIDIR}/{name}.jpg').convert('RGBA'); im = im.resize((int(im.width * _SC), int(im.height * _SC)), Image.LANCZOS)
        m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], radius=16, fill=255); im.putalpha(m); _shots[name] = im
    return _shots[name]
def _frame(w, h, col, lw=7):
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im); d.rounded_rectangle([lw // 2, lw // 2, w - 1 - lw // 2, h - 1 - lw // 2], radius=12, outline=col, width=lw); return im
def s_ui(C, D, dur):
    E = head('Real run on GitHub Actions', 'Step-by-step screenshots of my own repository.', C['u1']); E.append(El(badge('REAL CAPTURE  ·  step-by-step screenshots', F('b', 24), INK, GOOD, padx=16, pady=8), 1150, 170, C['u1'] + 0.2, anim='fade'))
    seq = [('u1', 's01', []), ('u2', 's01', [(344, 450, 1246, 536, 'ONE PUSH = ONE RUN')]), ('u3', 's03', [(1090, 280, 1208, 318, 'RUN IT BY HAND')]), ('u4', 's05', [(620, 225, 945, 278, 'STATUS · TIME · ARTIFACTS'), (380, 430, 640, 476, 'THE JOB')]),
           ('u5', 's07', [(376, 295, 1230, 535, 'EVERY STEP, TIMED')]), ('u6', 's08', [(440, 243, 720, 482, 'THE GRADLE TASKS'), (440, 522, 600, 544, 'BUILD SUCCESSFUL', 'r')]), ('u7', 's09', [(380, 30, 1080, 106, 'GRADLE REPORT', 'r')]), ('u8', 's07', [(384, 228, 505, 268, '30 s, NOT 55 s')])]
    for i, (cid, shot, boxes) in enumerate(seq):
        t0 = C[cid]; t1 = C[seq[i + 1][0]] if i + 1 < len(seq) else D - 0.15
        E.append(El(_shot(shot), _OX, _OY, t0, t1, anim='fade', d=0.35))
        for j, bx in enumerate(boxes):
            x0, y0, x1, y1, lab = bx[:5]
            X0, Y0, X1, Y1 = _OX + x0 * _SC, _OY + y0 * _SC, _OX + x1 * _SC, _OY + y1 * _SC
            E.append(El(_frame(int(X1 - X0) + 12, int(Y1 - Y0) + 12, WARN), int(X0) - 6, int(Y0) - 6, t0 + 0.7 + 0.2 * j, t1, anim='fade', d=0.3))
            bd = badge(lab, F('b', 28), INK, WARN, padx=14, pady=7); by = int(Y0) - 6 - bd.height - 8
            if by < 292: by = int(Y1) + 14
            bx_ = min(int(X0), 1920 - 60 - bd.width)
            if len(bx) > 5: bx_, by = int(X1) + 24, int(Y0) - 2
            E.append(El(bd, bx_, by, t0 + 0.9 + 0.2 * j, t1, anim='fade', d=0.3))
    return E
FN = dict(hook=s_hook, parts=s_parts, live=s_live, ui=s_ui, task=s_task, labinfo=s_labinfo, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(parts=('board', ACC), task=('test', GOOD), labinfo=('board', ACC), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'live': [
 ('t2b', 2, 1, 94, 330, 'ONLY MAIN', 360, 2), ('t2c', 3, 1, 126, 518, 'PLAIN TEXT', 548, 3), ('t2d', 4, 1, 198, 458, 'JAVA 8', 488, 4),
 ('t3b', 6, 1, 0, 205, 'RUNS THE JAR', 235, 6), ('t3c', 13, 1, 0, 270, 'BUILD SUCCESSFUL', 375, 13),
 ('t4b', 1, 1, 0, 251, 'THE JAR', 281, 1),
 ('t5b', 3, 1, 157, 236, 'PUSH', 266, 3), ('t5b', 6, 1, 157, 361, 'PULL REQUEST', 391, 6), ('t5b', 8, 1, 157, 440, 'RUN BUTTON', 470, 8),
 ('t5c', 13, 1, 220, 895, 'A SECRET', 300, 14),
 ('t6b', 8, 1, 270, 560, 'JAVA 21', 595, 8), ('t6c', 9, 1, 220, 816, 'CACHE', 846, 9), ('t6d', 11, 1, 220, 785, 'SAVES THE JAR', 815, 11)]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson100/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
