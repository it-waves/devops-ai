import sys, math; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
import numpy as np, cv2
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
LABEL = 'THE DEVOPS LOOP  ·  BOOTCAMP'
DEV, OPS = (96, 214, 226), (244, 170, 100)
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "This is the DevOps loop."), c('h2', "Every app you use goes around it, again and again."),
  c('h3', "On the left, Dev."), c('h3b', "On the right, Ops."), c('h4', "DevOps joins them into one endless loop."),
 ]),
 ('stages', [
  c('p1', "Plan.", None, 0.2), c('p2', "Decide what to build, and why.", None, 0.2), c('p3', "Track the work in GitHub."),
  c('k1', "Code.", None, 0.2), c('k2', "Developers write it,", None, 0.1), c('k3', "and track every change in Git."),
  c('b1', "Build.", None, 0.2), c('b2', "Turn the code into a program,", None, 0.1), c('b3', "with a tool like Maven."),
  c('t1', "Test.", None, 0.2), c('t2', "Let automated checks catch bugs first,", None, 0.1), c('t3', "with JUnit and SonarQube."),
  c('x1', "That is the Dev side."), c('x2', "Now, the Ops side."),
  c('r1', "Release.", None, 0.2), c('r2', "Package the program so it can ship,", None, 0.1), c('r3', "as a Docker image."),
  c('d1', "Deploy.", None, 0.2), c('d2', "Run it for real users,", None, 0.1), c('d3', "on Kubernetes, installed with Helm.", "on Kubernetes, installed with Helm."),
  c('o1', "Operate.", None, 0.2), c('o2', "Create and manage servers from code,", None, 0.1), c('o3', "with Terraform and Ansible.", "with terra form, and Ansible."),
  c('m1', "Monitor.", None, 0.2), c('m2', "Watch the system, and learn from it,", None, 0.1), c('m3', "with Prometheus and Grafana."),
 ]),
 ('end', [
  c('z1', "And then, the loop closes."), c('z2', "What you learn from monitoring becomes the next plan."),
  c('z3', "Every lesson in this bootcamp lives somewhere on this loop."), c('z4', "Learn the loop, and you learn DevOps."),
  c('z5', "Start with lesson one."),
 ]),
]
EXTRA = {'h2': 1.2, 'h4': 1.6, 'p3': 0.6, 'k3': 0.6, 'b3': 0.6, 't3': 0.8, 'x2': 0.3, 'r3': 0.6, 'd3': 0.8, 'o3': 0.8, 'm3': 1.0, 'z1': 1.4, 'z3': 1.8, 'z4': 0.5, 'z5': 1.0}
CHAP = {'hook': 'The loop', 'stages': 'The eight stages', 'end': 'The big picture'}
CX, CY, A_, YS = 960, 565, 700, 1.15
PI = math.pi
def P(t):
    s, k = math.sin(t), math.cos(t); d = 1 + s * s; return CX + A_ * k / d, CY + YS * A_ * s * k / d
N = 720; T0, T1 = PI / 2, 5 * PI / 2
STG = [('Plan', 'Memo', DEV, 5, 'up'), ('Code', 'Laptop', DEV, 7, 'up'), ('Build', 'Hammer and wrench', DEV, 9, 'down'), ('Test', 'Test tube', DEV, 11, 'down'),
       ('Release', 'Package', OPS, 13, 'up'), ('Deploy', 'Rocket', OPS, 15, 'up'), ('Operate', 'Gear', OPS, 17, 'down'), ('Monitor', 'Bar chart', OPS, 19, 'down')]
NP = [PI * s[3] / 8 for s in STG]
TOOLS = [['github'], ['git'], ['maven'], ['junit', 'sonarqube'], ['docker'], ['kubernetes', 'helm'], ['terraform', 'ansible'], ['prometheus', 'grafana']]
TAG = ['Decide what to build', 'Write the code', 'Make it runnable', 'Catch bugs early', 'Package to ship', 'Run for real users', 'Manage the servers', 'Watch and learn']
def lerp(a, b, u): return tuple(int(a[i] + (b[i] - a[i]) * u) for i in range(3))
def col_at(u):
    if u < .04: return lerp(OPS, DEV, .5 + u / .08)
    if u < .46: return DEV
    if u < .54: return lerp(DEV, OPS, (u - .46) / .08)
    if u < .96: return OPS
    return lerp(OPS, DEV, (u - .96) / .08)
_B = {}
def build_loop():
    if _B: return _B
    x0, y0, x1, y1 = 150, 150, 1770, 990; w, h = x1 - x0, y1 - y0
    body = np.zeros((h, w, 4), np.uint8); Tm = np.full((h, w), 65535, np.uint16)
    pts = [P(T0 + (T1 - T0) * i / N) for i in range(N + 1)]; pts = [(int(round(x - x0)), int(round(y - y0))) for x, y in pts]
    LAY = [(44, 0.0), (34, .42), (27, .68), (19, .95), (10, 1.25), (4, 1.55)]
    def seg(i, wd, f):
        col = col_at(i / N); p0, p1 = pts[i], pts[i + 1]; cc = (8, 18, 22) if f == 0.0 else tuple(min(255, int(v * f)) for v in col)
        cv2.line(body, p0, p1, cc + (255,), wd, cv2.LINE_AA); cv2.circle(body, p1, wd // 2, cc + (255,), -1, cv2.LINE_AA)
    allr = list(range(N)); B_ = [i for i in allr if N // 4 <= i < 3 * N // 4]; A_s = [i for i in allr if not (N // 4 <= i < 3 * N // 4)]
    for i in allr: seg(i, 44, 0.0)
    for wd, f in LAY[1:]:
        for i in B_: seg(i, wd, f)
    for i in A_s:
        if i < N * 0.07 or i >= N * 0.93: seg(i, 46, 0.0)
    for wd, f in LAY[1:]:
        for i in A_s: seg(i, wd, f)
    for i in range(N - 1, -1, -1):
        cv2.line(Tm, pts[i], pts[i + 1], int(i), 46); cv2.circle(Tm, pts[i + 1], 23, int(i), -1)
    al = body[..., 3].astype(np.float32) / 255
    sh = np.zeros((h, w, 4), np.uint8); sh[..., 3] = (cv2.GaussianBlur(al, (0, 0), 10) * 130).astype(np.uint8)
    M = np.roll(np.roll(sh, 16, axis=0), 8, axis=1); M[..., 3] = np.roll(np.roll(sh[..., 3], 16, axis=0), 8, axis=1)
    gl = np.zeros((h, w, 4), np.uint8); g = cv2.GaussianBlur(body[..., :3].astype(np.float32), (0, 0), 22) * 1.5; ga = cv2.GaussianBlur(al, (0, 0), 22)
    gl[..., :3] = np.clip(g, 0, 255).astype(np.uint8); gl[..., 3] = np.clip(ga * 150, 0, 255).astype(np.uint8)
    _B.update(dict(body=body, T=Tm, sh=M, gl=gl, o=(x0, y0)))
    return _B
class Loop(Dyn):
    def __init__(self, rev=None, dim=None):
        self.rev, self.dim = rev, dim; super().__init__(self._k, self._d)
    def _idx(self, t):
        if self.rev is None: return N + 5
        t0, du = self.rev
        if t < t0: return -1
        return int(min(1, (t - t0) / du) ** 1.0 * (N + 5))
    def _k(self, t):
        i = self._idx(t)
        if i < 0: return None
        return (i, round(self.dim(t), 2) if self.dim else 1.0)
    def _d(self, base, t, k):
        i, dm = k; B = build_loop(); m = (B['T'] <= i)
        for key in ('sh', 'gl', 'body'):
            a = B[key].copy(); a[..., 3] = (a[..., 3] * m * (dm * (0.5 if key == 'gl' else 1.0))).astype(np.uint8)
            base.alpha_composite(Image.fromarray(a, 'RGBA'), B['o'])
_SP = {}
def glow(r, col):
    k = (r, col)
    if k not in _SP:
        y, x = np.mgrid[-r:r, -r:r]; g = np.exp(-((x * x + y * y) / (r * r)) * 3.0); a = np.zeros((2 * r, 2 * r, 4), np.uint8); a[..., 0], a[..., 1], a[..., 2] = col; a[..., 3] = (g * 255).astype(np.uint8); _SP[k] = Image.fromarray(a, 'RGBA')
    return _SP[k]
class Orb(Dyn):
    """glowing comet running along the loop; way = [(time, param)] eased."""
    def __init__(self, way, t_end=None):
        self.way, self.te = way, t_end; super().__init__(lambda t: None if t < way[0][0] or (t_end is not None and t > t_end) else round(t, 3), self._d)
    def par(self, t):
        w = self.way
        if t <= w[0][0]: return w[0][1]
        for a, b in zip(w, w[1:]):
            if a[0] <= t <= b[0]: u = (t - a[0]) / max(1e-6, b[0] - a[0]); u = u * u * (3 - 2 * u) if b[0] - a[0] < 3.5 else u; return a[1] + (b[1] - a[1]) * u
        return w[-1][1]
    def _d(self, base, t, k):
        for j in range(18, -1, -1):
            tt = t - 0.03 * j
            if tt < self.way[0][0]: continue
            x, y = P(self.par(tt)); r = int(34 - j * 1.4); a = 1 - j / 20
            sp = glow(max(6, r), (255, 235, 190)); sp = sp.copy(); sp.putalpha(sp.getchannel('A').point(lambda v: int(v * a * 0.9))); base.alpha_composite(sp, (int(x - sp.width / 2), int(y - sp.height / 2)))
        x, y = P(self.par(t)); d = ImageDraw.Draw(base); d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=(255, 255, 255, 255))
_NI = {}
def node_img(i, state):
    k = (i, state)
    if k in _NI: return _NI[k]
    nm, em, col, _, _ = STG[i]
    if state == 'dim':
        R = 40; im = Image.new('RGBA', (R * 2, R * 2), (0, 0, 0, 0)); d = ImageDraw.Draw(im); d.ellipse([R - 17, R - 17, R + 17, R + 17], fill=PANEL + (255,), outline=(90, 120, 124, 255), width=4)
    else:
        r = 48 if state == 'done' else 58; R = r + 50; im = Image.new('RGBA', (R * 2, R * 2), (0, 0, 0, 0))
        if state == 'on': g = glow(R, col); im.alpha_composite(g)
        d = ImageDraw.Draw(im); d.ellipse([R - r, R - r, R + r, R + r], fill=PANEL + (255,), outline=col + (255,), width=6 if state == 'on' else 5)
        e = emoji_img(em, int(r * 1.25)); im.alpha_composite(e, (R - e.width // 2, R - e.height // 2))
    _NI[k] = im; return im
class Node(Dyn):
    def __init__(self, i, t_show, ta, te):
        self.i, self.ts, self.ta, self.te = i, t_show, ta, te; self.x, self.y = P(NP[i]); super().__init__(lambda t: None if t < t_show else round(t, 3), self._d)
    def _d(self, base, t, k):
        i = self.i; nm, em, col, _, side = STG[i]
        if self.ta is None or t < self.ta: st = 'dim' if self.ta is not None else 'done'
        elif t < self.te: st = 'on'
        else: st = 'done'
        im = node_img(i, st); s = 1.0
        if st == 'dim' and self.ta is not None: u = min(1, (t - self.ts) / 0.4); s = 0.4 + 0.6 * ease_back(u)
        if st == 'done' and self.ta is None: u = min(1, (t - self.ts) / 0.45); s = 0.4 + 0.6 * ease_back(u)
        if st == 'on':
            u = min(1, (t - self.ta) / 0.45); s = 0.6 + 0.4 * ease_back(u); s *= 1 + 0.035 * math.sin((t - self.ta) * 5)
        if abs(s - 1) > 0.01: im = im.resize((max(2, int(im.width * s)), max(2, int(im.height * s))), Image.LANCZOS)
        base.alpha_composite(im, (int(self.x - im.width / 2), int(self.y - im.height / 2)))
        if st != 'dim' or True:
            tc = col if st != 'dim' else MUTED; lab = T(nm, 'b', 30, tc if st != 'dim' else MUTED); a = 1.0
            yy = self.y - 62 - lab.height - 6 if side == 'up' else self.y + 62 + 6
            if st == 'dim': lab = lab.copy(); lab.putalpha(lab.getchannel('A').point(lambda v: int(v * 0.6)))
            base.alpha_composite(lab, (int(self.x - lab.width / 2), int(yy)))
def stage_cards(C, ids, t_end, chip_dt=0.9):
    """lobe info card per stage: card at name cue, tools at tool cue"""
    E = []
    for i, (nm, em, col, _, _) in enumerate(STG):
        n1, n2, n3 = ids[i]; ta = C[n1]; te = C[ids[i + 1][0]] - 0.15 if i + 1 < 8 else t_end
        cx = 560 if i < 4 else 1360; w, h = 380, 280; x = cx - w // 2; y = CY - h // 2
        E.append(Pop(card(w, h, col, nm, [(TAG[i], MUTED)], 50, 30), x, y, ta, te))
        for j, tn in enumerate(TOOLS[i]):
            E.append(Pop(LG.chip(tn, 84, LG.PRETTY[tn], F('b', 19)), x + 28 + j * 128, y + 148, C[n3] + j * chip_dt - 0.15, te))
    return E
def s_hook(C, D, dur):
    t0 = C['h1'] + 0.35; du = 4.6
    E = [Loop(rev=(t0, du)), Orb([(t0, T0), (t0 + du, T1), (D - 0.2, T1 + 2 * PI * 0.7)])]
    for nm, cx, col, cid, sub in [('DEV', 560, DEV, 'h3', 'Developers build it'), ('OPS', 1360, OPS, 'h3b', 'Operations run it')]:
        im = T(nm, 'x', 128, col); E.append(Pop(im, cx - im.width // 2, CY - 100, C[cid]))
        s2 = T(sub, 'm', 34, MUTED); E.append(El(s2, cx - s2.width // 2, CY + 60, C[cid] + 0.35, anim='fade'))
    E.append(El(T('Every piece of software goes around this loop', 'm', 40, MUTED), 330, 118, C['h2'], anim='fade'))
    E.append(pill('DevOps  =  Dev  +  Ops', 640, 930, C['h4'], ACC, INK, 54, 40, 18))
    for i in range(8): E.append(Node(i, C['h4'] + 0.4 + i * 0.16, 1e9, 1e9))
    return E
def s_stages(C, D, dur):
    ids = [('p1', 'p2', 'p3'), ('k1', 'k2', 'k3'), ('b1', 'b2', 'b3'), ('t1', 't2', 't3'), ('r1', 'r2', 'r3'), ('d1', 'd2', 'd3'), ('o1', 'o2', 'o3'), ('m1', 'm2', 'm3')]
    way = [(0.0, T0), (C['p1'], NP[0])]
    for i in range(1, 8): way += [(C[ids[i][0]] - 1.1, NP[i - 1]), (C[ids[i][0]], NP[i])]
    way += [(D - 0.2, NP[7] + 0.0)]
    E = [Loop(), Orb(way)]
    for i in range(8):
        ta = C[ids[i][0]]; te = C[ids[i + 1][0]] if i < 7 else D + 5
        E.append(Node(i, 0.0, ta, te))
        if i < 7: pass
        E.append(Ripple(*P(NP[i]), ta, STG[i][2], 90, 1.0))
    E += stage_cards(C, ids, D, 0.9)
    E.append(pill('DEV SIDE', 360, 118, C['p1'], DEV, INK, 30, 22, 10)); E.append(pill('OPS SIDE', 1450, 118, C['x2'], OPS, INK, 30, 22, 10))
    E.append(El(T('That is the Dev side. Now, the Ops side.', 'b', 38, MUTED), 560, 940, C['x1'], C['r1'] - 0.1, anim='fade')) if False else None
    return E
def s_end(C, D, dur):
    t_t = C['z4']
    dim = lambda t: 1.0 if t < t_t else max(0.18, 1 - (t - t_t) / 0.6 * 0.82)
    way = [(0.0, NP[7]), (C['z1'] + 0.0, NP[7]), (C['z1'] + 3.2, 5 * PI / 2 + NP[0] - T0 + 0.0 - 0.0)]
    E = [Loop(dim=dim), Orb(way, t_t)]
    for i in range(8): E.append(Node(i, 0.0, None, None))
    E[-8:] = [Dyn(n.keyfn, n.fn) if False else n for n in E[-8:]]
    E.append(pill('feedback', 760, 258, C['z1'] + 1.0, WARN, INK, 34, 24, 12)) if False else None
    for i in range(8):
        x, y = P(NP[i]); side = STG[i][4]
        for j, tn in enumerate(TOOLS[i]):
            n = len(TOOLS[i]); cx = x + (j - (n - 1) / 2) * 96 - 41; yy = y - 230 if side == 'up' else y + 112
            e = Pop(LG.chip(tn, 72, LG.PRETTY[tn], F('b', 17)), cx, yy, C['z3'] + 0.25 * i + 0.08 * j, t_t); E.append(e)
    E.append(El(T('Plan  →  Code  →  Build  →  Test  →  Release  →  Deploy  →  Operate  →  Monitor', 'b', 30, MUTED), 215, 985, C['z2'], t_t, anim='fade')) if False else None
    E.append((lambda p: (setattr(p, 't1', t_t), p)[1])(pill('What you learn becomes the next plan', 700, 112, C['z2'], WARN, INK, 38, 28, 14)))
    veil = Image.new('RGBA', (W, H), (6, 18, 20, 215)); E.append(El(veil, 0, 0, C['z4'] - 0.1, anim='fade', d=0.5))
    for nm, y, sz, col, cid in [('DevOps Engineering', 360, 110, TXT, 'z4'), ('Bootcamp', 500, 110, ACC, 'z4')]:
        im = T(nm, 'x', sz, col); E.append(Pop(im, 960 - im.width // 2, y, C[cid] + (0.2 if nm == 'Bootcamp' else 0)))
    im = T('Lesson 1  ·  From Idea to Customer', 'b', 44, MUTED); E.append(El(im, 960 - im.width // 2, 680, C['z5'], anim='fade'))
    return E
FN = dict(hook=s_hook, stages=s_stages, end=s_end)
