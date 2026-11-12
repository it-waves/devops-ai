"""Build the GitHub UI clip (real captured frames + animated cursor + highlights) synced to scene 'ui' cues. Registers it in build/clips.json."""
import sys, os, json, math, subprocess, numpy as np, cv2
sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson57')
from PIL import Image, ImageDraw, ImageFont
import importlib; V = importlib.import_module('video'); import term
LD = '/home/claude/academy/lesson57'; U = LD + '/ui/'; B = LD + '/build/'; os.makedirs(B, exist_ok=True)
dur = json.load(open(LD + '/vo/dur.json')); C, D, first = term.cue_times(V, dur, 'ui')
FPS = 30; W, H = 1080, 600
# real cursor tip in each captured frame (removed, then replaced by an animated one)
GHOST = {'01': (166, 547), '02': (600, 300), '03': (1182, 130), '04': (797, 493), '05': (870, 267), '06': (1153, 591), '07': (872, 209)}
def load(n):
    f = [x for x in os.listdir(U) if x.startswith(n)][0]; im = cv2.imread(U + f); gx, gy = GHOST[n]
    m = np.zeros(im.shape[:2], np.uint8); m[max(0, gy - 3):gy + 34, max(0, gx - 3):gx + 24] = 255
    im = cv2.inpaint(im, m, 3, cv2.INPAINT_TELEA); return Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
FR = {n: load(n) for n in GHOST}
# plan: cue -> (frame, cursor target or None, click?, [highlights (x0,y0,x1,y1,label)], focus x)
PLAN = {
 'u1': ('01', (228, 132), False, [], 228), 'u2': ('02', (1182, 132), True, [], 640), 'u3': ('03', (797, 493), True, [], 640),
 'u4': ('04', (870, 267), True, [(738, 258, 790, 278, 'short hash'), (833, 254, 912, 280, '')], 800),
 'u5': ('05', (244, 292), True, [(1100, 290, 1160, 314, 'same hash')], 640),
 'u6': ('06', (1090, 282), False, [(1028, 264, 1204, 286, 'zero parents = root commit'), (322, 496, 760, 566, 'what the commit added')], 900),
 'u7': ('07', (700, 382), False, [(542, 364, 876, 400, 'the clone address')], 700), 'u8': ('04', (800, 330), False, [(738, 258, 790, 278, ''), (66, 300, 690, 330, '')], 640),
}
ORDER = [cid for cid in PLAN]
def arrow_sprite():
    S = 4; im = Image.new('RGBA', (30 * S, 40 * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    pts = [(2, 2), (2, 30), (9, 24), (14, 35), (19, 33), (14, 22), (23, 22)]; P = [(x * S, y * S) for x, y in pts]
    d.polygon(P, fill=(255, 255, 255, 255), outline=(10, 10, 10, 255)); d.line(P + [P[0]], fill=(10, 10, 10, 255), width=3 * S // 2, joint='curve')
    return im.resize((30 * 3 // 2, 40 * 3 // 2), Image.LANCZOS)
CUR = arrow_sprite()
def ease(p): p = min(1, max(0, p)); return p * p * (3 - 2 * p)
# segment timeline in CLIP time: cue c shown during [S, E)
LEAD = 1.0; OFF = LEAD - 0.3 - C[first]
seg = {}
for i, cid in enumerate(ORDER):
    s = C[cid] + OFF; e = (C[ORDER[i + 1]] + OFF) if i + 1 < len(ORDER) else (D + OFF + 2.0)
    seg[cid] = (s if i else 0.0, e)
TOTAL = seg[ORDER[-1]][1] + 1.0
def fnt(sz): return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', sz)
def render(t):
    cid = next((c for c in ORDER if seg[c][0] <= t < seg[c][1]), ORDER[-1]); s, e = seg[cid]; fr, tgt, click, hls, fx = PLAN[cid]
    i = ORDER.index(cid)
    # cursor position
    prev_tgt = PLAN[ORDER[i - 1]][1] if i else (166, 547)
    if i and PLAN[ORDER[i - 1]][1] is None: prev_tgt = (640, 300)
    p0 = prev_tgt; p1 = tgt or prev_tgt
    ms, me = s + 0.5, s + 0.5 + min(1.8, 0.55 * (e - s)); k_ = ease((t - ms) / (me - ms))
    cx = p0[0] + (p1[0] - p0[0]) * k_; cy = p0[1] + (p1[1] - p0[1]) * k_ - 22 * math.sin(math.pi * k_)
    img = FR[fr].copy()
    # crossfade from previous frame at the start of a segment
    if i and t - s < 0.3:
        pf = FR[PLAN[ORDER[i - 1]][0]]; img = Image.blend(pf, img, ease((t - s) / 0.3))
    d = ImageDraw.Draw(img, 'RGBA')
    for (x0, y0, x1, y1, lab) in hls:
        a = ease((t - (s + 0.9)) / 0.4) * ease((e - 0.2 - t) / 0.3)
        if a > 0.02:
            pulse = 0.75 + 0.25 * math.sin((t - s) * 6)
            d.rounded_rectangle([x0 - 6, y0 - 5, x1 + 6, y1 + 5], radius=8, fill=(255, 210, 74, int(40 * a)), outline=(255, 210, 74, int(255 * a * pulse)), width=4)
            if lab:
                tw = d.textlength(lab, font=fnt(20)); lx = min(x0, 1270 - tw - 16); ly = y1 + 12 if y1 + 40 < 598 else y0 - 38
                d.rounded_rectangle([lx, ly, lx + tw + 16, ly + 30], radius=8, fill=(255, 210, 74, int(255 * a))); d.text((lx + 8, ly + 3), lab, font=fnt(20), fill=(11, 26, 30, int(255 * a)))
    # click ripple
    if click and tgt:
        ct = e - 0.45
        if 0 <= t - ct < 0.55:
            r = 10 + 60 * ((t - ct) / 0.55); a = int(220 * (1 - (t - ct) / 0.55)); d.ellipse([tgt[0] - r, tgt[1] - r, tgt[0] + r, tgt[1] + r], outline=(127, 224, 208, a), width=5)
    if i == 0 and t < LEAD - 0.3 or (i == 0 and False): pass
    img.paste(CUR, (int(cx - 3), int(cy - 3)), CUR)
    # zoomed crop of the full frame, placed under an address bar with a step caption (nothing is cropped away unless zoomed)
    zt = ZOOM.get(cid)
    if zt:
        z = 1.0 + (zt[2] - 1.0) * ease((t - s) / max(0.8, 0.5 * (e - s))); vw, vh = 1280 / z, 598 / z
        x0 = min(max(zt[0] - vw / 2, 0), 1280 - vw); y0 = min(max(zt[1] - vh / 2, 0), 598 - vh)
    else: vw, vh, x0, y0 = 1280, 598, 0, 0
    view = img.resize((W, 505), Image.LANCZOS, box=(x0, y0, x0 + vw, y0 + vh))
    cv = Image.new('RGB', (W, H), (11, 26, 30)); cv.paste(view, (0, 47))
    dd = ImageDraw.Draw(cv)
    dd.rounded_rectangle([14, 8, W - 14, 40], radius=16, fill=(22, 44, 50)); dd.text((34, 12), 'private', font=fnt(15), fill=(127, 224, 208)); dd.text((110, 12), URL[fr], font=fnt(20), fill=(228, 240, 241))
    dd.text((18, 560), CAP[cid], font=fnt(24), fill=(255, 210, 74))
    return cv
URL = {'01': 'github.com/it-waves/git-lab-demo/new/main', '02': 'github.com/it-waves/git-lab-demo/new/main', '03': 'github.com/it-waves/git-lab-demo/new/main', '04': 'github.com/it-waves/git-lab-demo', '05': 'github.com/it-waves/git-lab-demo/commits/main', '06': 'github.com/it-waves/git-lab-demo/commit/e485ca5', '07': 'github.com/it-waves/git-lab-demo'}
CAP = {'u1': '1  Create a new file: name it README.md', 'u2': '2  Write the content, then Commit changes', 'u3': '3  The commit message says what changed', 'u4': '4  A commit on main: short hash, 1 commit', 'u5': '5  The history: open the commit', 'u6': '6  0 parents: the root commit', 'u7': '7  Code: the address for git clone', 'u8': 'Same objects, same hashes, same history'}
ZOOM = {'u4': (800, 290, 1.18), 'u6': (900, 400, 1.15), 'u7': (700, 330, 1.15)}
out = B + 'clip_ui.mp4'
p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '15', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
n = int(TOTAL * FPS)
for f in range(n): p.stdin.write(render(f / FPS).tobytes())
p.stdin.close(); p.wait()
cl = B + 'clips.json'; d = json.load(open(cl)) if os.path.exists(cl) else {}; d['ui'] = dict(mode='sync', file=out); json.dump(d, open(cl, 'w'))
print('ui clip', round(TOTAL, 1), 's', n, 'frames')
