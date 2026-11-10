"""Live terminal recording helpers (any lesson). Xvfb :97 1080x600, xterm running a clean student shell.
Usage: from term import *; xterm_start(); r = Run(LD, scene) ; r.type_at(cid, text) ... r.end()"""
import os, sys, time, json, subprocess, importlib, re
WIN = [1080, 600]; DISP = ':97'; E97 = dict(os.environ, DISPLAY=DISP)
PS1 = r'\[\e[1;32m\]student@lab\[\e[0m\]:\[\e[1;36m\]\w\[\e[0m\]$ '
def sh(*a, **k): return subprocess.run(list(map(str, a)), env=E97, **k)
def xt(*a): sh('xdotool', *a)
def ensure_x():
    if subprocess.run(['pgrep', '-f', 'Xvfb ' + DISP], capture_output=True).returncode:
        subprocess.Popen(['Xvfb', DISP, '-screen', '0', '1080x600x24'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(2)
def reset_home():
    subprocess.run('find /home/student -mindepth 1 -delete', shell=True)
def xterm_start():
    ensure_x(); reset_home(); subprocess.run(['xsetroot', '-solid', '#0b1a1e'], env=E97)
    cmd = ['xterm', '-geometry', '71x19+0+0', '-b', '6', '-fa', 'DejaVu Sans Mono', '-fs', '18', '-bg', '#0b1a1e', '-fg', '#e4f0f1', '-cr', '#7fe0d0', '-xrm', 'XTerm*cursorBlink:false',
           '-xrm', 'XTerm*scrollBar:false', '-xrm', 'XTerm*borderWidth:0', '-e', 'runuser', '-u', 'student', '--', 'env', '-i', 'HOME=/home/student', 'LANG=C.UTF-8', 'TERM=xterm-256color',
           'PATH=/usr/local/bin:/usr/bin:/bin', 'PS1=' + PS1, 'USER=student', 'SHELL=/bin/bash', 'bash', '-c', 'cd ~; exec bash --rcfile /etc/ps1rc -i']
    p = subprocess.Popen(cmd, env=E97); time.sleep(2.0)
    w = subprocess.run(['xdotool', 'search', '--class', 'xterm'], env=E97, capture_output=True, text=True).stdout.split()
    if w:
        xt('windowmove', w[0], 0, 0)
        g = subprocess.run(['xdotool', 'getwindowgeometry', w[0]], env=E97, capture_output=True, text=True).stdout
        m = re.search(r'Geometry: (\d+)x(\d+)', g)
        if m: WIN[0], WIN[1] = int(m.group(1)) // 2 * 2, int(m.group(2)) // 2 * 2
    return p
def typ(s, delay=75): xt('type', '--delay', delay, '--clearmodifiers', s)
def key(k): xt('key', k)
def focus(): xt('mousemove', 540, 300); xt('click', 1)
def rec_start(out, secs):
    return subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-draw_mouse', '0', '-framerate', '30', '-video_size', f'{WIN[0]}x{WIN[1]}', '-i', DISP, '-t', str(secs), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '15', '-pix_fmt', 'yuv420p', out], env=E97, stdin=subprocess.PIPE)
def rec_stop(p):
    try: p.stdin.write(b'q'); p.stdin.flush()
    except Exception: pass
    p.wait()
SENT = re.compile(r'[.?!:]$')
def cue_times(V, dur, scene):
    for name, cues in V.SCENES:
        if name != scene: continue
        C = {}; t = 0.5
        for c in cues:
            gap = c[3] if len(c) > 3 and c[3] is not None else (0.55 if SENT.search(c[1]) else 0.13)
            C[c[0]] = t; t += dur[c[0]] + gap + V.EXTRA.get(c[0], 0)
        return C, round(t - 0.4 + 0.9, 3), cues[0][0]
class Run:
    def __init__(s, LD, V, scene, delay=75):
        s.clear = getattr(V, 'CLEAR', False); s.LD = LD; s.V = V; s.scene = scene; s.delay = delay; s.dur = json.load(open(LD + '/vo/dur.json'))
        s.C, s.D, s.first = cue_times(V, s.dur, scene); s.out = LD + f'/build/clip_{scene}.mp4'; os.makedirs(LD + '/build', exist_ok=True)
        s.ff = rec_start(s.out, s.D + 6); time.sleep(1.0); s.T0 = time.time(); s.warn = []
    def at(s, cid, off=0.0):
        t = s.T0 + s.C[cid] + off - time.time()
        if t > 0: time.sleep(t)
        elif t < -0.4: s.warn.append(f'{cid} late by {-t:.1f}s')
    def cmd(s, cid, text, enter=True):
        """type so that typing ends about when the cue's narration ends"""
        need = len(text) * s.delay / 1000.0 + 0.25; d = s.dur[cid]
        off = max(0.3, d - need)
        if d - need < 0.3: s.warn.append(f'{cid}: typing {need:.1f}s > cue {d:.1f}s -> add EXTRA {need + 0.3 - d:.1f}')
        s.at(cid, off)
        if s.clear: key('ctrl+l'); time.sleep(0.2)
        typ(text, s.delay)
        if enter: key('Return')
    def keys(s, cid, ks, off=None):
        s.at(cid, s.dur[cid] - 1.8 if off is None else off)
        for k in ks: key(k); time.sleep(0.6)
    def end(s):
        t = s.T0 + s.D + 0.6 - time.time()
        if t > 0: time.sleep(t)
        rec_stop(s.ff); print(s.scene, 'recorded', round(s.D, 1), 'warn:', s.warn)
        clips = s.LD + '/build/clips.json'; d = json.load(open(clips)) if os.path.exists(clips) else {}
        d[s.scene] = dict(mode='sync', file=s.out); json.dump(d, open(clips, 'w'))
