"""Record Lesson 85 live UI scenes (continuous full-screen browser recording, real mouse and keyboard on a private Gitea). usage: record_ui.py all | SCENE..."""
import sys, os, json, time, subprocess
sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson85')
from uidrv import *
import term, video as V
MEASURE = os.environ.get('MEASURE') == '1'
LD = '/home/claude/academy/lesson85'; H = 'http://127.0.0.1:8085'
dur = json.load(open(LD + "/vo/dur.json"))
class Sc:
    def __init__(s, u, name):
        s.u = u; s.name = name; s.C, s.D, s.first = term.cue_times(V, dur, name); s.out = LD + f'/build/clip_{name}.mp4'; s.warn = []
        os.makedirs(LD + '/build', exist_ok=True)
        s.prev = None; s.meas = {}
        if MEASURE: return
        s.ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-draw_mouse', '0', '-framerate', '30', '-video_size', '1920x1080', '-i', DISP, '-t', str(s.D + 8), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p', s.out], env=E, stdin=subprocess.PIPE)
        time.sleep(1.0); s.T0 = time.time()
    def at(s, cid, off=0.2):
        if MEASURE:
            now = time.time()
            if s.prev and s.prev != cid: s.meas[s.prev] = s.meas.get(s.prev, 0) + now - s.prevt
            if s.prev != cid: s.prev = cid; s.prevt = now
            return
        t = s.T0 + s.C[cid] + off - time.time()
        if t > 0: time.sleep(t)
        elif t < -0.5: s.warn.append(f'{cid} late by {-t:.1f}s')
    def end(s):
        if MEASURE:
            if s.prev: s.meas[s.prev] = s.meas.get(s.prev, 0) + time.time() - s.prevt + 1.2
            d = json.load(open(LD + '/measure.json')) if os.path.exists(LD + '/measure.json') else {}
            d.update(s.meas); json.dump(d, open(LD + '/measure.json', 'w')); print(s.name, 'measured', {k: round(v, 1) for k, v in s.meas.items()}, flush=True); return
        t = s.T0 + s.D + 0.6 - time.time()
        if t > 0: time.sleep(t)
        try: s.ff.stdin.write(b'q'); s.ff.stdin.flush()
        except Exception: pass
        s.ff.wait(); print(s.name, 'recorded', round(s.D, 1), 'warn:', s.warn, flush=True)
        clips = LD + '/build/clips.json'; d = json.load(open(clips)) if os.path.exists(clips) else {}
        d[s.name] = dict(mode='full', file=s.out); json.dump(d, open(clips, 'w'))
def scroll(u, dy, secs=1.0, n=10):
    for i in range(n): u.pg.mouse.wheel(0, dy / n); time.sleep(secs / n)
def s_repo(u):
    S = Sc(u, 'repo')
    S.at('l1', 0.0); u.goto(H + '/'); u.wait(1.0)
    S.at('l2', 0.2); u.click('a[href="/org/"]', dur=0.9); u.wait(0.9); u.click('a[href="/org/apache/"]', dur=0.8); u.wait(0.9); u.click('a[href="/org/apache/commons/"]', dur=0.8); u.wait(0.9)
    S.at('l3', 0.2); u.click('a[href="/org/apache/commons/commons-lang3/"]', dur=0.9); u.wait(0.9)
    S.at('l4', 0.2); u.click('a[href="/org/apache/commons/commons-lang3/3.14.0/"]', dur=0.9); u.wait(1.0)
    S.at('l5', 0.2); u.click('a[href$=".pom"]', dur=0.9); u.wait(2.5)
    S.at('l5', 5.0); u.pg.go_back(); u.wait(1.0); u.pg.evaluate(CURSOR_JS); u.click('a[href$=".jar.sha1"]', dur=0.8); u.wait(1.2)
    S.at('l6', 0.2); u.goto(H + '/org/apache/commons/'); u.wait(1.0); scroll(u, 500, 1.6); u.wait(0.6)
    S.end()
if __name__ == '__main__':
    if MEASURE and os.path.exists(LD + '/measure.json'): os.remove(LD + '/measure.json')
    u = UI(rec=False)
    for n, f in [('repo', s_repo)]:
        if sys.argv[1:] in (['all'], []) or n in sys.argv[1:]: f(u)
    u.close()
