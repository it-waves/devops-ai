"""usage: python3 pipe.py VIDEO_DIR tts|info|scene NAMES|preview NAMES t,t|av|all"""
import json, os, re, subprocess, sys, importlib
VD = os.path.abspath(sys.argv[1]); sys.path.insert(0, VD); sys.path.insert(0, '/home/claude/academy/common')
from kit import *
import numpy as np, soundfile as sf
V = importlib.import_module('video')
SCENES, FN, CHAP = V.SCENES, V.FN, V.CHAP; EXTRA = getattr(V, 'EXTRA', {}); LEAD = getattr(V, 'LEAD', {})
OUTD = VD + '/build'; VO = VD + '/vo'; os.makedirs(OUTD, exist_ok=True); os.makedirs(VO, exist_ok=True)
SENT = re.compile(r'[.?!:]$')
def norm(c):
    cid, cap = c[0], c[1]; say = c[2] if len(c) > 2 and c[2] else cap; gap = c[3] if len(c) > 3 else (0.55 if SENT.search(cap) else 0.13)
    sp = say if re.search(r'[.?!,;:]$', say) else say + ','
    return cid, cap, sp, gap
def do_tts():
    from kokoro_onnx import Kokoro
    k = Kokoro('/home/claude/tts/kokoro-v1.0.onnx', '/home/claude/tts/voices-v1.0.bin'); dur = {}
    for scene, cues in SCENES:
        for c in cues:
            cid, cap, say, gap = norm(c); s, sr = k.create(say, voice='af_heart', speed=1.0, lang='en-us'); sf.write(f'{VO}/{cid}.wav', s, sr); dur[cid] = sf.info(f'{VO}/{cid}.wav').duration
    json.dump(dur, open(VO + '/dur.json', 'w'), indent=1); print(round(sum(dur.values()), 1), 's speech')
dur = json.load(open(VO + '/dur.json')) if os.path.exists(VO + '/dur.json') else {}
TAIL = 0.9; TL = []; gt = 0.0
if dur:
    for name, cues in SCENES:
        t = LEAD.get(name, 0.5); C = {}
        for c in cues:
            cid, cap, say, gap = norm(c); C[cid] = t; C[cid + '.e'] = t + dur[cid]; t += dur[cid] + gap + EXTRA.get(cid, 0)
        D = round(t - 0.4 + TAIL, 3); TL.append(dict(name=name, C=C, D=D, start=gt, cues=cues)); gt += D
TOTAL = gt
def chrome(name):
    im = theme.backdrop(); d = ImageDraw.Draw(im); f = F('b', 20); lab = V.LABEL; w = int(f.getlength(lab)) + 44
    d.rounded_rectangle([60, 30, 60 + w, 70], radius=20, fill=EN.ACC); d.text((82, 38), lab, font=f, fill=INK)
    if CHAP.get(name): d.text((60 + w + 24, 38), CHAP[name], font=F('m', 22), fill=EN.ACC)
    s2 = 'DevOps Simplified'; d.text((W - 60 - F('s', 22).getlength(s2), 38), s2, font=F('s', 22), fill=EN.MUTED)
    d.rectangle([0, H - 6, W, H], fill=(30, 62, 68)); return im
def build_scene(sc):
    E = [e for e in FN[sc['name']](sc['C'], sc['D'], dur) if e is not None]
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
    ImageDraw.Draw(im).rectangle([0, H - 5, pw, H], fill=EN.ACC); b = im.convert('RGB').tobytes(); cache['k'] = k; cache['b'] = b; return b
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
    return f'{h:02d}:{m:02d}:{int(s):02d},{min(999, int(round((s - int(s)) * 1000))):03d}'
def build_av():
    sr = 24000; buf = np.zeros(int((TOTAL + 1) * sr), dtype=np.float32); out = []; k = 1
    for sc in TL:
        for c in sc['cues']:
            cid, cap = c[0], c[1]; a, r = sf.read(f'{VO}/{cid}.wav', dtype='float32'); t0 = sc['start'] + sc['C'][cid]; i = int(t0 * sr); buf[i:i + len(a)] += a
            parts = [cap] if len(cap) <= 90 else [p for p in re.split(r'(?<=[.?!,])\s+', cap)]; tot = sum(len(p) for p in parts); t = t0
            for p in parts: dd = dur[cid] * len(p) / tot; out.append(f'{k}\n{fmt(t)} --> {fmt(t + dd)}\n{p}\n'); k += 1; t += dd
    buf = buf / np.max(np.abs(buf)) * 0.89; sf.write(f'{OUTD}/voice.wav', buf[:int(TOTAL * sr)], sr); open(f'{OUTD}/captions.srt', 'w').write('\n'.join(out))
if __name__ == '__main__':
    cmd = sys.argv[2]
    if cmd == 'tts': do_tts()
    elif cmd == 'info':
        for sc in TL: print(sc['name'], round(sc['start'], 1), sc['D'])
        print('TOTAL', round(TOTAL, 1)); open(OUTD + '/order.txt', 'w').write('\n'.join(sc['name'] for sc in TL))
    elif cmd == 'preview':
        for sc in TL:
            if sc['name'] in sys.argv[3].split(','):
                ts = [float(x) if x != 'end' else sc['D'] - 0.6 for x in sys.argv[4].split(',')]
                for t, im in zip(ts, render_scene(sc, ts)): im.save(f"{OUTD}/prev_{sc['name']}_{t:.1f}.jpg", quality=85)
    elif cmd == 'scene':
        for sc in TL:
            if sc['name'] in sys.argv[3].split(','): print(sc['name'], render_scene(sc), flush=True)
    elif cmd == 'av': build_av()
