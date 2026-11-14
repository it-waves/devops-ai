def s_hook(C, D, dur):
    E = [El(T('We cannot deploy a jar.', 'x', 66), 100, 130, C['h1'])]
    E.append(Pop(card(700, 140, ACC, 'what you built', [('cart-web.jar', TXT)], 46, 30), 100, 300, C['h2']))
    E.append(Pop(card(700, 140, BAD, 'what the server wants', [('cloudcart.war', TXT)], 46, 30), 100, 480, C['h2'] + 2.5))
    E.append(Pop(card(760, 180, VIO, 'One line in the pom', [('packaging', TXT)], 52, 40), 900, 440, C['h3']))
    E.append(takeaway('Package it. Then look inside.', 900, C['h4'], GOOD, 1700)); return E
def _list(title, sub, first, items, take=None, tcid=None, h=130, w=1700, y0=330, gap=150):
    def f(C, D, dur):
        E = head(title, sub, C[first])
        for i, (n, s_, col, cid) in enumerate(items): E.append(Pop(card(w, h, col, n, [(s_, TXT)], 44, 32), 100, y0 + i * gap, C[cid]))
        if take: E.append(takeaway(take, y0 + len(items) * gap + 20, C[tcid], GOOD, 1700))
        return E
    return f
s_what = _list('What is a WAR?', 'A zip file for a servlet container.', 'a1', [('1  Web archive', 'a zip with the extension .war', ACC, 'a1'), ('2  Container', 'tomcat unpacks it and serves the site', VIO, 'a2'), ('3  jar vs war', 'a jar holds classes; a war holds a whole web app', WARN, 'a3'), ('4  One pom line', 'packaging jar  becomes  packaging war', GOOD, 'a4')], 'No new tool. One line.', 'a5')
s_inside = _list('Inside a WAR', 'A strict layout.', 'b1', [('index.html', 'top folder: public pages', ACC, 'b2'), ('WEB-INF/', 'private: browsers never reach it', VIO, 'b3'), ('WEB-INF/web.xml  classes/  lib/', 'settings, your code, library jars', WARN, 'b4')], 'Maven builds the layout for you.', 'b5')
s_scope = _list('Compile vs provided', 'Does the server already have it?', 'x1', [('compile (default)', 'copied into WEB-INF/lib', GOOD, 'x2'), ('provided', 'used to build, NOT packaged', VIO, 'x3'), ('e.g. servlet API', 'the container supplies it; your copy can break it', WARN, 'x4')], 'Server supplies it: provided.', 'x5')
def s_task(C, D, dur):
    E = head('Your lab task', 'lab89.sh gives a project that builds a jar. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab89.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Packaging', [('packaging war', TXT), ('finalName cloudcart', TXT)], 'k3', ACC), ('2  Build', [('mvn clean package', TXT), ('cloudcart.war', TXT)], 'k4', GOOD), ('3  Contents', [('unzip -l', TXT), ('contents.txt', TXT)], 'k5', VIO), ('4  Libraries', [('util inside', TXT), ('liba provided', TXT)], 'k6', WARN), ('5  why.txt', [('one sentence', TXT), ('provided + server', TXT)], 'k7', PINK), ('6  Check', [('lab check', TXT), ('then lab down', TXT)], 'k8', BAD)]
    for i, (n, ls, cid, col) in enumerate(steps): E.append(Pop(card(540, 190 if len(ls) < 3 else 240, col, n, ls, 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 270, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('What a WAR is', 'q3'), ('Pages on top, WEB-INF private', 'q4'), ('compile vs provided', 'q5'), ('List it with unzip', 'q6'), ('lab down, nothing left', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Start', 'lab up, read the task file', PINK, 'z2'), ('2  Packaging', 'war, and the final name', ACC, 'z3'), ('3  Build', 'package, contents.txt', VIO, 'z4'), ('4  Provided', 'liba out of the WAR', WARN, 'z5'), ('5  Explain, check', 'why.txt, then lab check', BAD, 'z6'), ('6  Clean up', 'lab down, prove it', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What is a WAR?', 'f12'), ('Which folder is private?', 'f13'), ('Scope that stays out?', 'f14'), ('Command to list contents?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC10-O05', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: repository mirrors', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
s_war = _lab('Live: build and inspect a WAR', 'Switch the packaging, read the contents, keep a library out.', 'w0', RB, [('w1', 'mvn package', 'a jar: not deployable', BAD), ('w2', 'packaging war', 'one line changed', VIO), ('w3', '<finalName>', 'cloudcart.war', ACC), ('w4', 'mvn package', 'cloudcart.war built', GOOD), ('w5', 'unzip -Z1', 'pages, web.xml, classes, libs', ACC), ('w6', 'scope provided', 'liba from the server', WARN), ('w7', 'rebuild, list', 'liba is gone', GOOD)])
FN = dict(hook=s_hook, what=s_what, inside=s_inside, scope=s_scope, war=s_war, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(what=('gear', ACC), inside=('link', VIO), scope=('gear', GOOD), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {'war': [('w1b', 1, 1, 0, 400, 'A JAR'), ('w4b', 1, 1, 0, 370, ''), ('w5b', 5, 2, 0, 800, 'LIBS INSIDE'), ('w7b', 6, 1, 0, 600, 'ONLY UTIL')]}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson89/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
