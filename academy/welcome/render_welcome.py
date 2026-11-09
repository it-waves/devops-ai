import json, math, os, re, subprocess, sys
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw
sys.path.insert(0, '/home/claude/osi'); sys.path.insert(0, '/home/claude/academy/welcome')
import theme
from engine import *
from script_welcome import SCENES
import scenes_welcome as S
OUTD = '/home/claude/academy/welcome/build'; VO = '/home/claude/academy/welcome/vo'
dur = json.load(open(VO + '/dur.json'))
GAP = 0.45; TAIL = 0.9; LEAD = {'hook': 0.4}
EXTRA = {'a2': 4.0, 'b2': 2.5, 'b3': 2.5, 'b4': 2.5, 'b5': 2.5, 'b6': 3.0, 'c2': 3.0, 'c3': 2.0, 'c4': 3.0, 'c5': 3.0, 'd2': 2.5, 'd3': 3.0, 'd4': 3.0, 'e2': 2.0, 'e3': 2.0, 'e4': 2.0, 'e5': 2.5, 'e6': 3.0, 'f1': 3.0, 'f2': 4.0}
CHAP = {'promise': 'How we teach', 'path': 'The roadmap', 'lesson': 'Every lesson', 'expect': 'What to expect', 'start': 'Start here'}
TL = []; gt = 0.0
for name, cues in SCENES:
    t = LEAD.get(name, 0.6); C = {}
    for cid, text, say in cues:
        C[cid] = t; t += dur[cid] + GAP + EXTRA.get(cid, 0)
    D = round(t - GAP + TAIL, 3); TL.append(dict(name=name, C=C, D=D, start=gt, cues=cues)); gt += D
TOTAL = gt
def chrome(name):
    im = theme.backdrop(); d = ImageDraw.Draw(im); f = F('b', 20)
    lab = 'DEVOPS ENGINEERING BOOTCAMP'; w = int(f.getlength(lab)) + 44
    d.rounded_rectangle([60, 30, 60 + w, 70], radius=20, fill=ACC); d.text((82, 38), lab, font=f, fill=(8, 24, 26))
    x = 60 + w + 24
    if CHAP.get(name): d.text((x, 38), CHAP[name], font=F('m', 22), fill=ACC)
    s2 = 'DevOps Simplified'; d.text((W - 60 - F('s', 22).getlength(s2), 38), s2, font=F('s', 22), fill=MUTED)
    d.rectangle([0, H - 6, W, H], fill=(30, 62, 68)); return im
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
