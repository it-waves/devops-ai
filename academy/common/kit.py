import sys, math
sys.path.insert(0, '/home/claude/osi'); sys.path.insert(0, '/home/claude/academy/common')
import theme
from engine import *
import engine as EN
from PIL import Image, ImageDraw
import logos as LG
VIO = (140, 164, 240); PINK = (198, 172, 240); INK = (8, 24, 26)
def T(s, w='m', size=34, color=None, maxw=None, align='left', lh=1.32): return text_img(s, F(w, size), color or EN.TXT, maxw, lh, align)
def card(w, h, col, title, lines, tsize=36, lsize=30):
    im = rrect(w, h, 18, fill=EN.PANEL, outline=col, width=3); d = ImageDraw.Draw(im)
    d.text((28, 20), title, font=F('b', tsize), fill=col); y = 20 + tsize + 20
    for s, c in lines:
        t = T(s, 'm', lsize, c, maxw=w - 40); im.alpha_composite(t, (28, y)); y += t.height + 8
    return im
def ease_back(p):
    c1 = 1.9; c3 = c1 + 1; p = min(1, max(0, p)); return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2
class Pop(El):
    """spring pop-in: scales from 55% with overshoot while fading in."""
    def __init__(self, img, x, y, t0, t1=None, d=0.5):
        super().__init__(img, x, y, t0, t1, anim='fade', d=d)
    def draw(self, base, t, k):
        p, o = k; s = 0.55 + 0.45 * ease_back(p); a = min(1, p * 2.2) * o
        w, h = max(2, int(self.img.width * s)), max(2, int(self.img.height * s)); im = self.img.resize((w, h), Image.LANCZOS)
        if a < 0.999: al = im.getchannel('A').point(lambda v: int(v * a)); im = im.copy(); im.putalpha(al)
        base.alpha_composite(im, (int(self.x + (self.img.width - w) / 2), int(self.y + (self.img.height - h) / 2)))
def logo(name, x, y, t, size=110, label=None, ring=None, d=0.5):
    return Pop(LG.chip(name, size, label, F('b', 24) if label else None, ring), x, y, t, d=d)
def pill(s, x, y, t, col, fg=INK, size=30, padx=22, pady=11, anim='pop'):
    im = badge(s, F('b', size), fg, col, padx=padx, pady=pady, r=int(size * 0.8)); return Pop(im, x, y, t) if anim == 'pop' else El(im, x, y, t, anim='fade')
def ill(t, x=1400, y=170): return El(badge('ILLUSTRATION  ·  not a capture', F('b', 24), INK, EN.WARN, padx=16, pady=8), x, y, t, anim='fade')
def real(t, label, x, y): return El(badge(label, F('b', 24), INK, EN.GOOD, padx=16, pady=8), x, y, t, anim='fade')
def arrow2(pts, col, lw=7, head=30):
    pad = head + lw; xs = [q[0] for q in pts]; ys = [q[1] for q in pts]
    x0, y0 = min(xs) - pad, min(ys) - pad; w = int(max(xs) - min(xs) + 2 * pad); h = int(max(ys) - min(ys) + 2 * pad)
    S = 3; im = canvas(w * S, h * S); d = ImageDraw.Draw(im); P = [((q[0] - x0) * S, (q[1] - y0) * S) for q in pts]
    (ax, ay), (bx, by) = P[-2], P[-1]; ang = math.atan2(by - ay, bx - ax); hl = head * S
    base = (bx - hl * 0.9 * math.cos(ang), by - hl * 0.9 * math.sin(ang)); d.line(P[:-1] + [base], fill=col, width=lw * S, joint='curve'); wing = hl * 0.52
    d.polygon([(bx, by), (base[0] + wing * math.sin(ang), base[1] - wing * math.cos(ang)), (base[0] - wing * math.sin(ang), base[1] + wing * math.cos(ang))], fill=col)
    return im.resize((w, h), Image.LANCZOS), x0, y0
def A(pts, t, col=None, lw=7, head=30, d=0.5):
    im, x0, y0 = arrow2(pts, col or EN.ACC, lw, head); return El(im, x0, y0, t, anim='fade', d=d)
def arc_pts(cx, cy, r, a0, a1, n=24): return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
def outside(pt, boxes, m=14): return all(not (b[0] - m <= pt[0] <= b[2] + m and b[1] - m <= pt[1] <= b[3] + m) for b in boxes)
class Move(Dyn):
    """image travelling through waypoints [(t,x,y)] with easing; visible from first t until t_end (None=forever)."""
    def __init__(self, img, way, t_end=None, bob=0):
        self.img, self.way, self.te, self.bob = img, way, t_end, bob
        super().__init__(self._key, self._draw)
    def _pos(self, t):
        w = self.way
        if t <= w[0][0]: return w[0][1], w[0][2]
        for a, b in zip(w, w[1:]):
            if a[0] <= t <= b[0]:
                p = ease((t - a[0]) / max(1e-6, b[0] - a[0])); return a[1] + (b[1] - a[1]) * p, a[2] + (b[2] - a[2]) * p
        return w[-1][1], w[-1][2]
    def _key(self, t):
        if t < self.way[0][0] or (self.te is not None and t > self.te): return None
        x, y = self._pos(t); return (int(x), int(y + self.bob * math.sin(t * 6)))
    def _draw(self, base, t, k): base.alpha_composite(self.img, (k[0] - self.img.width // 2, k[1] - self.img.height // 2))
class Ripple(Dyn):
    def __init__(self, x, y, t0, col, r=70, dur=0.9):
        self.x, self.y, self.t0, self.col, self.r, self.dur = x, y, t0, col, r, dur
        super().__init__(lambda t: round((t - t0) / dur, 2) if t0 <= t <= t0 + dur else None, self._d)
    def _d(self, base, t, k):
        ov = canvas(self.r * 3, self.r * 3); d = ImageDraw.Draw(ov); rr = self.r * (0.3 + 1.1 * ease(k)); a = int(200 * (1 - k))
        d.ellipse([self.r * 1.5 - rr, self.r * 1.5 - rr, self.r * 1.5 + rr, self.r * 1.5 + rr], outline=self.col + (a,), width=6); base.alpha_composite(ov, (int(self.x - self.r * 1.5), int(self.y - self.r * 1.5)))
def bar(x, y, w, h, t0, t1, col, a=70):
    """highlight bar visible between t0 and t1 (for code lines)."""
    im = canvas(w, h); ImageDraw.Draw(im).rounded_rectangle([0, 0, w - 1, h - 1], radius=8, fill=col + (a,), outline=col + (200,), width=2)
    e = El(im, x, y, t0, t1, anim='fade', d=0.2); e.dout = 0.2; return e
def lines_el(lines, x, y, fs=27, lh=None):
    lh = lh or int(fs * 1.55); return [El(T(txt, 'mono', fs, col, align='left'), x, y + i * lh, t, anim='fade', d=0.25) for i, (txt, t, col) in enumerate(lines)]
def parcel(size=64, col=None):
    col = col or EN.ACC; S = 3; w = size * S; im = canvas(w, w); d = ImageDraw.Draw(im)
    d.rounded_rectangle([w * .1, w * .22, w * .9, w * .86], radius=w * .08, fill=col, outline=(255, 255, 255, 120), width=S * 2)
    d.rectangle([w * .44, w * .22, w * .56, w * .86], fill=(255, 255, 255, 150)); d.polygon([(w * .1, w * .22), (w * .5, w * .06), (w * .9, w * .22)], fill=tuple(max(0, c - 35) for c in col))
    return im.resize((size, size), Image.LANCZOS)
def bulb(size=80):
    S = 3; w = size * S; im = canvas(w, w); d = ImageDraw.Draw(im); c = EN.ACC
    d.ellipse([w * .22, w * .08, w * .78, w * .64], fill=c); d.polygon([(w * .34, w * .54), (w * .66, w * .54), (w * .58, w * .78), (w * .42, w * .78)], fill=c)
    d.rounded_rectangle([w * .4, w * .78, w * .6, w * .9], radius=w * .03, fill=EN.MUTED)
    for a in (-60, -30, 0, 30, 60):
        r0, r1 = w * .42, w * .5; x0 = w / 2 + r0 * math.sin(math.radians(a)); y0 = w * .36 - r0 * math.cos(math.radians(a)); x1 = w / 2 + r1 * math.sin(math.radians(a)); y1 = w * .36 - r1 * math.cos(math.radians(a))
        d.line([x0, y0, x1, y1], fill=c, width=S * 3)
    return im.resize((size, size), Image.LANCZOS)
def house(size=220, col=None):
    col = col or EN.GOOD; S = 3; w = size * S; im = canvas(w, w); d = ImageDraw.Draw(im)
    d.polygon([(w * .08, w * .46), (w * .5, w * .1), (w * .92, w * .46)], fill=tuple(max(0, c - 40) for c in col)); d.rectangle([w * .17, w * .46, w * .83, w * .9], fill=col)
    d.rectangle([w * .42, w * .62, w * .58, w * .9], fill=(22, 36, 42)); d.rectangle([w * .24, w * .55, w * .36, w * .68], fill=(235, 250, 245)); d.rectangle([w * .64, w * .55, w * .76, w * .68], fill=(235, 250, 245))
    return im.resize((size, size), Image.LANCZOS)
def phone(w=430, h=760):
    return rrect(w, h, 56, fill=(14, 34, 40), outline=EN.EDGE, width=6)

# ---------- design system v2 ----------
import numpy as np, cv2
from PIL import ImageFilter
PADC = 22
_oi = El.__init__
def _ni(self, img, x, y, *a, **k):
    p = getattr(img, 'info', {}).get('pad', 0); _oi(self, img, x - p, y - p, *a, **k)
El.__init__ = _ni
def glass(w, h, col, r=22):
    P = PADC; im = Image.new('RGBA', (w + 2 * P, h + 2 * P), (0, 0, 0, 0))
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle([P, P + 12, P + w, P + h + 12], radius=r, fill=(0, 0, 0, 130)); im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(15)))
    pn = EN.PANEL[:3]; top = [min(255, int(c * 1.55) + 6) for c in pn]; t = np.linspace(0, 1, h)[:, None]
    arr = np.zeros((h, w, 4), np.uint8)
    for i in range(3): arr[..., i] = (top[i] * (1 - t) + pn[i] * t).astype(np.uint8)
    arr[..., 3] = 255; mask = Image.new('L', (w, h), 0); ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=r, fill=255)
    im.paste(Image.fromarray(arr, 'RGBA'), (P, P), mask); d = ImageDraw.Draw(im)
    d.rounded_rectangle([P, P, P + w - 1, P + h - 1], radius=r, outline=tuple(col[:3]) + (200,), width=2)
    d.line([(P + r, P + 2), (P + w - r, P + 2)], fill=(255, 255, 255, 50), width=2); d.rounded_rectangle([P + 26, P - 1, P + 96, P + 5], radius=3, fill=tuple(col[:3]) + (255,))
    im.info['pad'] = P; return im
def card(w, h, col, title, lines, tsize=36, lsize=30):
    im = glass(w, h, col); d = ImageDraw.Draw(im); P = PADC
    d.text((P + 28, P + 20), title, font=F('b', tsize), fill=col); y = P + 20 + tsize + 20
    for s, c in lines:
        t = T(s, 'm', lsize, c, maxw=w - 40); im.alpha_composite(t, (P + 28, y)); y += t.height + 8
    im.info['pad'] = P; return im
def row(w, h, col): return glass(w, h, col, 18)

# ---------- 3D scene helpers ----------
import iso
class Drop(El):
    """drops in from above with a soft landing."""
    def __init__(self, img, x, y, t0, t1=None, d=0.6, h=90): self.h = h; super().__init__(img, x, y, t0, t1, anim='fade', d=d)
    def draw(self, base, t, k):
        p, o = k; e = ease_back(p) if p < 1 else 1; a = min(1, p * 2.5) * o; y = self.y - (1 - e) * self.h; im = self.img
        if a < 0.999: im = im.copy(); im.putalpha(im.getchannel('A').point(lambda v: int(v * a)))
        base.alpha_composite(im, (int(self.x), int(y)))
class GrowBox(Dyn):
    """isometric box that rises from the ground; (sx,sy) = screen pos of world corner A(0,0,0)."""
    def __init__(self, sx, sy, w, d, h, col, label, t0, dur=0.7, glow=None):
        self.a = (sx, sy, w, d, h, col, label); self.t0, self.dur = t0, dur; self.cache = {}
        super().__init__(lambda t: None if t < t0 else round(min(1, (t - t0) / dur) * 20) / 20, self._d)
    def _d(self, base, t, k):
        sx, sy, w, d, h, col, label = self.a; f = ease_back(k) if k < 1 else 1; f = max(0.02, min(1.12, f)); q = round(f * 25) / 25
        if q not in self.cache: self.cache[q] = iso.box(w, d, max(2, h * q), col, label if q >= 0.99 else None)
        im, ox, oy = self.cache[q]; base.alpha_composite(im, (int(sx - ox), int(sy - oy)))
def isoimg(*a, **k): return iso.box(*a, **k)
class Tilt(Dyn):
    """perspective-tilted plane of logo chips that slowly sways; each chip pops at its own time."""
    def __init__(self, names, cx, cy, t0, t_out, t_start, t_end, cols=6, chip=104, gap=26):
        self.names, self.cx, self.cy, self.t0, self.t_out = names, cx, cy, t0, t_out; rows = -(-len(names) // cols)
        self.cols, self.rows, self.chip, self.gap = cols, rows, chip, gap; self.w = cols * (chip + gap); self.h = rows * (chip + gap)
        self.ts = [t_start + (t_end - t_start) * i / len(names) for i in range(len(names))]; self.chips = [LG.chip(n, chip) for n in names]
        super().__init__(lambda t: None if t < t0 or t > t_out + 0.6 else round(t, 2), self._d)
    def _d(self, base, t, k):
        wall = Image.new('RGBA', (self.w, self.h), (0, 0, 0, 0))
        for i, (c, ts) in enumerate(zip(self.chips, self.ts)):
            p = min(1, max(0, (t - ts) / 0.45)) if t >= ts else 0
            if p <= 0: continue
            s = 0.5 + 0.5 * ease_back(p); cw = max(2, int(self.chip * s)); im = c.resize((cw, cw), Image.LANCZOS)
            wall.alpha_composite(im, ((i % self.cols) * (self.chip + self.gap) + (self.chip - cw) // 2 + self.gap // 2, (i // self.cols) * (self.chip + self.gap) + (self.chip - cw) // 2 + self.gap // 2))
        yaw = math.radians(-26 + 7 * math.sin(t * .6)); pit = math.radians(10 + 3 * math.sin(t * .45 + 1)); f, dist = 1500, 320
        pts = []
        for X, Y in [(-self.w / 2, -self.h / 2), (self.w / 2, -self.h / 2), (self.w / 2, self.h / 2), (-self.w / 2, self.h / 2)]:
            x1 = X * math.cos(yaw); z1 = X * math.sin(yaw); y1 = Y * math.cos(pit) - z1 * math.sin(pit); z2 = Y * math.sin(pit) + z1 * math.cos(pit)
            s = f / (f + dist + z2); pts.append((x1 * s * 1.0 + self.cx, y1 * s + self.cy))
        sc = 1.0; a = max(0, 1 - (t - self.t_out) / 0.5) if t > self.t_out else 1.0
        if t > self.t_out: u = (t - self.t_out) / 0.5; sc = 1 + 0.35 * u; pts = [(self.cx + (x - self.cx) * sc, self.cy + (y - self.cy) * sc) for x, y in pts]
        M = cv2.getPerspectiveTransform(np.float32([[0, 0], [self.w, 0], [self.w, self.h], [0, self.h]]), np.float32(pts))
        warped = cv2.warpPerspective(np.asarray(wall), M, (W, H), flags=cv2.INTER_LINEAR, borderValue=(0, 0, 0, 0))
        if a < 1: warped[..., 3] = (warped[..., 3] * a).astype(np.uint8)
        base.alpha_composite(Image.fromarray(warped, 'RGBA'))
