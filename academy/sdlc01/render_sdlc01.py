import json, math, os, re, subprocess, sys
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw
sys.path.insert(0, '/home/claude/osi'); sys.path.insert(0, '/home/claude/academy/sdlc01')
from engine import *
from script_sdlc01 import SCENES
import scenes_sdlc01 as S
OUTD = '/home/claude/academy/sdlc01/build'; VO = '/home/claude/academy/sdlc01/vo'
dur = json.load(open(VO + '/dur.json'))
GAP = 0.45; TAIL = 0.9; LEAD = {'hook': 0.4}
EXTRA = {'h2': 5.0, 'r2': 3.0, 'p1': 3.0, 'p2': 3.0, 'p3': 2.0, 'q2': 3.0, 'q3': 5.0, 'd2': 6.0, 'b2': 8.0, 'b3': 3.0, 't2': 3.0, 't3': 2.0, 'y2': 5.0, 'y3': 3.0, 'o2': 6.0, 'z1': 8.0, 'z2': 3.0, 'z3': 3.0}
CHAP = {'roadmap': 'Overview', 'plan': 'Plan', 'req': 'Requirements', 'design': 'Design', 'build': 'Build', 'test': 'Test', 'deploy': 'Deploy', 'operate': 'Operate', 'recap': 'Quick check'}
TL = []; gt = 0.0
for name, cues in SCENES:
    t = LEAD.get(name, 0.6); C = {}
    for cid, text, say in cues:
        C[cid] = t; t += dur[cid] + GAP + EXTRA.get(cid, 0)
    D = round(t - GAP + TAIL, 3); TL.append(dict(name=name, C=C, D=D, start=gt, cues=cues)); gt += D
TOTAL = gt
def chrome(name):
    g = np.linspace(0, 1, H)[:, None]
    arr = (np.array(BG0)[None, None, :] * (1 - g[..., None]) + np.array(BG1)[None, None, :] * g[..., None])
    im = Image.fromarray(np.repeat(arr, W, axis=1).astype(np.uint8), 'RGB').convert('RGBA'); d = ImageDraw.Draw(im); f = F('s', 22)
    d.ellipse([60, 46, 72, 58], fill=ACC); lab = 'DevOps Engineering Bootcamp  ·  SDLC'; d.text((86, 38), lab, font=f, fill=TXT)
    x = 86 + f.getlength(lab); s = '   ·   Lesson 1'; d.text((x, 38), s, font=F('m', 22), fill=MUTED)
    if CHAP.get(name): d.text((x + F('m', 22).getlength(s), 38), '   ·   ' + CHAP[name], font=F('m', 22), fill=ACC)
    s2 = 'DevOps Simplified'; d.text((W - 60 - f.getlength(s2), 38), s2, font=f, fill=MUTED)
    d.rectangle([0, H - 5, W, H], fill=(28, 40, 62)); return im
def build_scene(sc):
    E = S.FN[sc['name']](sc['C'], sc['D'], dur); E = [e for e in E if e is not None]
    for e in E:
        if isinstance(e, El) and e.t1 is None: e.t1 = sc['D'] - 0.35
    return E
def frame_at(sc, E, base, t, cache):
    keys = tuple(e.key(t) for e in E); pw = int(W * (sc['start'] + t) / TOTAL); k = (keys, pw)
    if cache.get('k') == k: return cache['b']
    if cache.get('kk') == keys: im = cache['im'].copy()
    else:
        im = base.copy()
        for e, kk in zip(E, keys):
            if kk is not None: e.draw(im, t, kk)
        cache['kk'] = keys; cache['im'] = im.copy()
    ImageDraw.Draw(im).rectangle([0, H - 5, pw, H], fill=ACC)
    b = im.convert('RGB').tobytes(); cache['k'] = k; cache['b'] = b; return b
def render_scene(sc, only=None):
    base = chrome(sc['name']); E = build_scene(sc)
    if only is not None: return [Image.frombytes('RGB', (W, H), frame_at(sc, E, base, t, {})) for t in only]
    n = int(round(sc['D'] * FPS)); tmp = f"{OUTD}/{sc['name']}.tmp.mp4"; fin = f"{OUTD}/{sc['name']}.mp4"
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), tmp], stdin=subprocess.PIPE)
    cache = {}
    for i in range(n): p.stdin.write(frame_at(sc, E, base, i / FPS, cache))
    p.stdin.close(); rc = p.wait()
    if rc == 0: os.replace(tmp, fin)
    return rc
def fmt(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h:02d}:{m:02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}'.replace(',1000', ',999')
def build_av():
    sr = 24000; buf = np.zeros(int((TOTAL + 1) * sr), dtype=np.float32); out = []; k = 1
    for sc in TL:
        for cid, text, say in sc['cues']:
            a, r = sf.read(f'{VO}/{cid}.wav', dtype='float32'); i = int((sc['start'] + sc['C'][cid]) * sr); buf[i:i + len(a)] += a
            t0 = sc['start'] + sc['C'][cid]; d = dur[cid]; parts = re.split(r'(?<=[.?!:])\s+', text); pp = []; carry = ''
            for p in parts:
                if len(p) <= 9 and p.endswith('.'): carry = (carry + ' ' + p).strip(); continue
                pp.append((carry + ' ' + p).strip()); carry = ''
            if carry: pp.append(carry)
            parts = pp; chunks = []; cur = ''
            for p in parts:
                if len(cur) + len(p) + 1 <= 84: cur = (cur + ' ' + p).strip()
                else:
                    if cur: chunks.append(cur)
                    while len(p) > 84:
                        cut = p.rfind(',', 0, 84); cut = cut if cut > 30 else p.rfind(' ', 0, 84); chunks.append(p[:cut + 1].strip()); p = p[cut + 1:].strip()
                    cur = p
            if cur: chunks.append(cur)
            m = []
            for c in chunks:
                if m and len(c) < 14 and len(m[-1]) + len(c) < 100: m[-1] += ' ' + c
                else: m.append(c)
            if len(m) > 1 and len(m[0]) < 14: m = [m[0] + ' ' + m[1]] + m[2:]
            tot = sum(len(c) for c in m); t = t0
            for c in m:
                dd = d * len(c) / tot; out.append(f'{k}\n{fmt(t)} --> {fmt(t + dd - 0.02)}\n{c}\n'); k += 1; t += dd
    buf = buf / np.max(np.abs(buf)) * 0.89; sf.write(f'{OUTD}/voice.wav', buf[:int(TOTAL * sr)], sr); open(f'{OUTD}/captions.srt', 'w').write('\n'.join(out))
if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'info':
        for sc in TL: print(sc['name'], round(sc['start'], 1), sc['D'])
        print('TOTAL', round(TOTAL, 1))
    elif cmd == 'preview':
        for sc in TL:
            if sc['name'] in sys.argv[2].split(','):
                ts = [float(x) if x != 'end' else sc['D'] - 0.6 for x in sys.argv[3].split(',')]
                for t, im in zip(ts, render_scene(sc, ts)): im.save(f"{OUTD}/prev_{sc['name']}_{t:.1f}.jpg", quality=85)
    elif cmd == 'scene':
        for sc in TL:
            if sc['name'] in sys.argv[2].split(','): print(sc['name'], render_scene(sc), flush=True)
    elif cmd == 'av': build_av()
