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
            cid, cap, say, gap = norm(c)
            if not os.path.exists(f'{VO}/{cid}.wav'):
                ph = k.tokenizer.phonemize(say, 'en-us')
                if re.search(r'\blives\b', say, re.I): ph = ph.replace('lˈaɪvz', 'lˈɪvz')   # verb 'lives' = /livz/, not /laivz/
                s, sr = k.create(ph, voice='af_heart', speed=1.0, lang='en-us', is_phonemes=True); sf.write(f'{VO}/{cid}.wav', s, sr)
            dur[cid] = sf.info(f'{VO}/{cid}.wav').duration
    json.dump(dur, open(VO + '/dur.json', 'w'), indent=1); print(round(sum(dur.values()), 1), 's speech')
dur = json.load(open(VO + '/dur.json')) if os.path.exists(VO + '/dur.json') else {}
TAIL = 0.9; TL = []; gt = 0.0
if dur and all(norm(c)[0] in dur for _, cs in SCENES for c in cs):
    for name, cues in SCENES:
        t = LEAD.get(name, 0.5); C = {}
        for c in cues:
            cid, cap, say, gap = norm(c); C[cid] = t; C[cid + '.e'] = t + dur[cid]; t += dur[cid] + gap + EXTRA.get(cid, 0)
        D = round(t - 0.4 + TAIL, 3); TL.append(dict(name=name, C=C, D=D, start=gt, cues=cues)); gt += D
TOTAL = gt
import cv2
BG = theme.backdrop().convert('RGBA')
def _sprite(r, col):
    y, x = np.mgrid[-r:r, -r:r]; g = np.exp(-((x * x + y * y) / (r * r)) * 3.2); arr = np.zeros((2 * r, 2 * r, 4), np.uint8); arr[..., 0], arr[..., 1], arr[..., 2] = col; arr[..., 3] = (g * 255).astype(np.uint8); return Image.fromarray(arr, 'RGBA')
SPR = [(_sprite(r, col), r, sx, sy, sp) for r, col, sx, sy, sp in [(120, (70, 150, 150), .12, .2, 5), (90, (230, 190, 120), .8, .3, -4), (150, (110, 130, 220), .55, .75, 3), (80, (80, 180, 160), .25, .8, -6), (110, (230, 190, 120), .93, .85, 4)]]
def _dim(im, a):
    al = im.getchannel('A').point(lambda v: int(v * a)); im = im.copy(); im.putalpha(al); return im
def bg_at(t):
    im = BG.copy()
    for sp, r, sx, sy, v in SPR: im.alpha_composite(_dim(sp, .22), (int(W * sx - r + v * t * 3), int(H * sy - r + math.sin(t * .35 + sx * 9) * 22)))
    return im
CH = {}
def chrome(sc):
    if sc['name'] in CH: return CH[sc['name']]
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); f = F('b', 20); lab = V.LABEL; w = int(f.getlength(lab)) + 44
    d.rounded_rectangle([60, 30, 60 + w, 70], radius=20, fill=EN.ACC); d.text((82, 38), lab, font=f, fill=INK)
    if CHAP.get(sc['name']): d.text((60 + w + 24, 38), CHAP[sc['name']], font=F('m', 22), fill=EN.ACC)
    s2 = 'DevOps Simplified'; d.text((W - 60 - F('s', 22).getlength(s2), 38), s2, font=F('s', 22), fill=EN.MUTED)
    d.rectangle([0, H - 8, W, H], fill=(24, 54, 60))
    for q in TL[1:]: x = int(W * q['start'] / TOTAL); d.rectangle([x - 1, H - 14, x + 1, H], fill=(120, 170, 170))
    CH[sc['name']] = np.asarray(im); return CH[sc['name']]
def build_scene(sc):
    E = [e for e in FN[sc['name']](sc['C'], sc['D'], dur) if e is not None]
    for e in E:
        if isinstance(e, El) and e.t1 is None: e.t1 = sc['D'] - 0.35
    return E
def zoom_at(t, D):
    e = min(1.0, t / 0.6); return 1.0 + 0.032 * (t / D) + 0.05 * (1 - (1 - (1 - e) ** 3))
def frame_at(sc, E, t):
    im = bg_at(t)
    for e in E:
        k = e.key(t)
        if k is not None: e.draw(im, t, k)
    arr = np.asarray(im)[..., :3]; z = zoom_at(t, sc['D']); x0 = (W - W / z) / 2; y0 = (H - H / z) / 2
    out = cv2.warpAffine(arr, np.float32([[z, 0, -x0 * z], [0, z, -y0 * z]]), (W, H), flags=cv2.INTER_LINEAR).astype(np.float32)
    a = max(0.0, 1 - t / 0.45) ** 2 * 0.9 + max(0.0, (t - (sc['D'] - 0.25)) / 0.25) * 0.45
    if a > 0: out = out * (1 - a) + np.float32([6, 18, 20]) * a
    ch = chrome(sc).astype(np.float32); al = ch[..., 3:4] / 255.0; out = out * (1 - al) + ch[..., :3] * al
    pw = int(W * (sc['start'] + t) / TOTAL); out[H - 8:H, :pw] = np.float32(EN.ACC[:3]); return np.clip(out, 0, 255).astype(np.uint8)
def render_scene(sc, only=None):
    E = build_scene(sc)
    if only is not None: return [Image.fromarray(frame_at(sc, E, t)) for t in only]
    n = int(round(sc['D'] * FPS)); tmp = f"{OUTD}/{sc['name']}.tmp.mp4"; fin = f"{OUTD}/{sc['name']}.mp4"
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(FPS), tmp], stdin=subprocess.PIPE)
    for i in range(n): p.stdin.write(frame_at(sc, E, i / FPS).tobytes())
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
