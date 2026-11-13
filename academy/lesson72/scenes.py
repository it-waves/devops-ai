def s_hook(C, D, dur):
    E = [El(T('Where is the cart?', 'x', 72), 100, 130, C['h1'])]
    E.append(Pop(card(840, 140, ACC, 'Two copies of the API', [('a busy shop runs more than one', TXT)], 44, 32), 100, 330, C['h1'] + 1.2))
    E.append(Pop(card(840, 110, WARN, 'Cart added on copy one', [], 44, 32), 100, 500, C['h1'] + 5.0))
    E.append(Pop(card(840, 110, BAD, 'Next click lands on copy two', [], 44, 32), 100, 630, C['h2']))
    mv = [('State', 'what a program remembers', ACC), ('Stateful or not', 'keeps it, or keeps nothing', VIO), ('Persistent data', 'survives a restart', GOOD), ('Scale out', 'needs stateless servers', PINK)]
    for i, (n, s_, col) in enumerate(mv): E.append(Pop(card(420, 170, col, n, [(s_, TXT)], 36, 26, True), 1000 + (i % 2) * 440, 330 + (i // 2) * 200, C['h3'] + 2.0 + i * 2.2))
    E.append(Pop(badge('server 1', F('x', 52), INK, ACC, padx=34, pady=18), 100, 800, C['h4'])); E.append(Pop(badge('server 2', F('x', 52), INK, WARN, padx=34, pady=18), 440, 800, C['h4'] + 0.6))
    E.append(takeaway('Watch a cart vanish, then fix it.', 980, C['h4'] + 1.4, GOOD, 1700)); return E
s_memory = _lab('State lives in memory', 'A cart kept in memory dies with the process.', 'a1', RB, [('a2', './start.sh', 'start the shop', ACC), ('a3', 'POST /api/cart/1', 'add an item', VIO), ('a6', 'storage: memory', 'one process remembers', WARN), ('a7', './start.sh', 'a restart, as in a deploy', BAD), ('a9', 'cart: empty', 'memory died with the process', BAD)])
s_scale = _lab('Two servers, one cart', 'The next click may land on another copy.', 'b1', RB, [('b3', './second.sh', 'a second copy, port 5001', ACC), ('b5', 'POST to 5000', 'the cart is on server 1', VIO), ('b7', 'GET from 5001', 'ask server 2', WARN), ('b8', 'cart: empty', 'server 2 knows nothing', BAD)])
s_db = _lab('Stateless and persistent', 'State moves out of the server, into the database.', 'c1', RB, [('c2', 'STORAGE=db', 'cart goes to the database', ACC), ('c4', 'POST to 5000', 'add item 2', VIO), ('c7', 'both servers agree', 'servers are stateless now', GOOD), ('c8', 'restart', 'start everything again', WARN), ('c10', 'cart: still there', 'persistent data', GOOD), ('c12', 'back it up', 'servers are replaceable, data is not', PINK)])
def s_models(C, D, dur):
    E = head('Stateful or stateless', 'Keep state out of the server, and keep it safe.', C['m1']); E.append(ill(C['m1'] + 0.2, 1400, 170))
    E.append(Pop(card(840, 150, ACC, 'State', [('what is remembered between requests', TXT)], 40, 30), 100, 340, C['m2']))
    E.append(Pop(card(840, 150, BAD, 'Stateful', [('memory or disk on the server', TXT)], 40, 30), 980, 340, C['m3']))
    E.append(Pop(card(840, 190, GOOD, 'Stateless', [('any copy answers any request', TXT), ('add, remove, replace freely', TXT)], 40, 28), 100, 530, C['m4']))
    E.append(Pop(card(840, 190, WARN, 'Backing service', [('database, cache, object storage', TXT), ('the state moves there', TXT)], 40, 28), 980, 530, C['m5']))
    E.append(Pop(card(840, 140, PINK, 'Persistent data', [('volume or managed DB, and a backup', TXT)], 40, 28), 100, 750, C['m6']))
    E.append(Pop(card(840, 140, VIO, 'Tokens, settings', [('keep them outside the server too', TXT)], 40, 28), 980, 750, C['m7']))
    E.append(takeaway('Docker volumes and cloud databases do exactly this.', 950, C['m8'], WARN, 1700)); return E
def s_task(C, D, dur):
    E = head('Your lab task', 'lab72.sh starts CloudCart. lab check judges your work.', C['k1']); E.append(ill(C['k1'] + 0.2, 1400, 170))
    E.append(Pop(card(1700, 100, ACC, '', [], 4), 100, 330, C['k2'])); E.append(El(T('github.com/it-waves/devops-ai   ›   academy/lab/lab72.sh', 'mono', 32, TXT, align='left'), 140, 360, C['k2'] + 0.3, anim='fade'))
    steps = [('1  Split', 'memory: save split.txt', 'k3', BAD), ('2  Share', 'db: save shared.txt', 'k4', VIO), ('3  Survive', 'restart, cart still there', 'k5', WARN), ('4  Answer', 'state: shop.db', 'k6', PINK), ('5  Both up', 'two servers, same cart', 'k7', ACC), ('lab check', 'five PASS lines', 'k8', GOOD)]
    for i, (n, s_, cid, col) in enumerate(steps): E.append(Pop(card(540, 190, col, n, [(s_, TXT)], 40, 28), 100 + (i % 3) * 590, 470 + (i // 3) * 230, C[cid]))
    return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['q1'])
    items = [('Five PASS lines', 'q2'), ('What is state?', 'q3'), ('Stateful or stateless', 'q4'), ('Scale out needs stateless', 'q5'), ('Persistent data and backup', 'q6'), ('lab down, nothing listening', 'q7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 32), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['q8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'Your own VM only. Slow and exact.', C['z1'])
    it = [('1  Install', 'the lab, then lab up', PINK, 'z2'), ('2  Split', 'watch the cart vanish', BAD, 'z3'), ('3  Share', 'switch to the database', VIO, 'z4'), ('4  Restart', 'data must survive', WARN, 'z5'), ('5  Answer', 'two servers running', ACC, 'z6'), ('6  Check', 'lab check, lab down', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('What is state?', 'f12'), ('Why did the cart vanish?', 'f13'), ('What makes a service stateless?', 'f14'), ('Where does persistent data live?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC08-O06', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next: health, logs, metrics', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, memory=s_memory, scale=s_scale, db=s_db, models=s_models, task=s_task, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(memory=('doc', ACC), scale=('test', BAD), db=('doc', GOOD), models=('board', ACC), task=('test', GOOD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'memory': [('a6', 1, 1, 0, 800, 'IN MEMORY'), ('a9', 1, 1, 0, 770, 'LOST')],
 'scale': [('b8', 1, 1, 0, 770, 'EMPTY')],
 'db': [('c7', 1, 1, 0, 740, 'SHARED'), ('c10', 1, 1, 0, 740, 'STILL THERE')],
}
import re as _re
CMDLEN = {}
_rs = open('/home/claude/academy/lesson72/record.py').read()
for _m in _re.finditer(r"\('cmd', '(\w+)', ('(?:[^'\\]|\\.)*'|\"(?:[^\"\\]|\\.)*\")\)", _rs): CMDLEN[_m.group(1)] = len(eval(_m.group(2)))
