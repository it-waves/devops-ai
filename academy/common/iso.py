"""Software isometric (dimetric) renderer: boxes, slabs, houses, parcels, skewed labels. No external 3D engine."""
import math, numpy as np, cv2
from PIL import Image, ImageDraw
AN = math.radians(18); CA, SA = math.cos(AN), math.sin(AN)
def P(x, y, z): return ((x - y) * CA, (x + y) * SA - z)
def shade(c, f): return tuple(max(0, min(255, int(v * f))) for v in c[:3])
def _canvas(pts, ss, pad=6):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]; x0, y0 = min(xs) - pad, min(ys) - pad; w, h = int(max(xs) - x0 + pad), int(max(ys) - y0 + pad)
    return x0, y0, Image.new('RGBA', (w * ss, h * ss), (0, 0, 0, 0))
def box(w, d, h, col, top_label=None, ss=3, tape=None, edge=True, glow=None):
    """returns (RGBA image, ox, oy) where (ox,oy) = pixel of world origin corner A(0,0,0)."""
    pts = [P(0, 0, 0), P(w, 0, 0), P(w, d, 0), P(0, d, 0), P(0, 0, h), P(w, 0, h), P(w, d, h), P(0, d, h)]
    x0, y0, im = _canvas(pts, ss, 14 if glow else 6); dr = ImageDraw.Draw(im)
    sc = lambda p: ((p[0] - x0) * ss, (p[1] - y0) * ss)
    A, B, Cc, D = [sc(P(*q)) for q in [(0, 0, h), (w, 0, h), (w, d, h), (0, d, h)]]; B0, C0, D0 = sc(P(w, 0, 0)), sc(P(w, d, 0)), sc(P(0, d, 0))
    ln = (255, 255, 255, 70) if edge else None
    dr.polygon([D, Cc, C0, D0], fill=shade(col, 0.62) + (255,)); dr.polygon([B, Cc, C0, B0], fill=shade(col, 0.82) + (255,)); dr.polygon([A, B, Cc, D], fill=shade(col, 1.12) + (255,))
    if tape:
        tw = d * 0.18; a1, a2 = sc(P(w * 0.5 - tw, 0, h)), sc(P(w * 0.5 + tw, 0, h)); b1, b2 = sc(P(w * 0.5 + tw, d, h)), sc(P(w * 0.5 - tw, d, h)); dr.polygon([a1, a2, b1, b2], fill=tape + (255,))
    if ln:
        for pl in ([A, B, Cc, D], [D, Cc, C0, D0], [B, Cc, C0, B0]): dr.line(pl + [pl[0]], fill=ln, width=ss)
    out = im.resize((im.width // ss, im.height // ss), Image.LANCZOS); ox, oy = -x0, -y0
    if top_label is not None: out = _skew_top(out, top_label, w, d, h, ox, oy)
    return out, ox, oy
def _skew_top(out, lab, w, d, h, ox, oy):
    """warp a text image (RGBA) onto the top face"""
    tw, th = lab.size; src = np.float32([[0, 0], [tw, 0], [0, th]])
    a = P(0, 0, h); b = P(w, 0, h); dd = P(0, d, h); dst = np.float32([[a[0] + ox, a[1] + oy], [b[0] + ox, b[1] + oy], [dd[0] + ox, dd[1] + oy]])
    M = cv2.getAffineTransform(src, dst); arr = np.asarray(lab).copy(); warped = cv2.warpAffine(arr, M, (out.width, out.height), flags=cv2.INTER_AREA if False else cv2.INTER_LINEAR, borderValue=(0, 0, 0, 0))
    o = out.copy(); o.alpha_composite(Image.fromarray(warped, 'RGBA')); return o
def house(col=(110, 215, 190), ss=3):
    w = d = 170; h = 110; ap = 80
    pts = [P(0, 0, 0), P(w, 0, 0), P(w, d, 0), P(0, d, 0), P(w / 2, d / 2, h + ap), P(0, 0, h), P(w, d, h)]
    x0, y0, im = _canvas(pts, ss); dr = ImageDraw.Draw(im); sc = lambda q: ((q[0] - x0) * ss, (q[1] - y0) * ss)
    Aa, Bb, Cc, Dd = [sc(P(*q)) for q in [(0, 0, h), (w, 0, h), (w, d, h), (0, d, h)]]; B0, C0, D0 = sc(P(w, 0, 0)), sc(P(w, d, 0)), sc(P(0, d, 0)); ap_ = sc(P(w / 2, d / 2, h + ap))
    dr.polygon([Dd, Cc, C0, D0], fill=shade(col, 0.62) + (255,)); dr.polygon([Bb, Cc, C0, B0], fill=shade(col, 0.82) + (255,))
    roof = (232, 170, 110); dr.polygon([Dd, Cc, ap_], fill=shade(roof, 0.8) + (255,)); dr.polygon([Bb, Cc, ap_], fill=shade(roof, 0.62) + (255,))
    # door + window on faces
    dr.polygon([sc(P(w * .15, d, 0)), sc(P(w * .15 + 38, d, 0)), sc(P(w * .15 + 38, d, 70)), sc(P(w * .15, d, 70))], fill=(22, 36, 42, 255))
    dr.polygon([sc(P(w, d * .25, 40)), sc(P(w, d * .5, 40)), sc(P(w, d * .5, 82)), sc(P(w, d * .25, 82))], fill=(240, 250, 246, 255))
    return im.resize((im.width // ss, im.height // ss), Image.LANCZOS)
def slab_label(text_img, w, d): return text_img
def face_label(text, w, d, size=64, col=(8, 24, 26), font=None, k=3):
    """text centred on a w:d face image (aspect matches the top face)."""
    from kit import F, T
    im = Image.new('RGBA', (int(w * k), int(d * k)), (0, 0, 0, 0)); sz = size * k // 2
    while True:
        t = T(text, 'x', sz, col)
        if t.width <= im.width * 0.74 or sz < 12: break
        sz -= 4
    im.alpha_composite(t, ((im.width - t.width) // 2, (im.height - t.height) // 2)); return im
