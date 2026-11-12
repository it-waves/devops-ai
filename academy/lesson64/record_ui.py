"""Record Lesson 64 live UI scenes (continuous full-screen browser recording, real mouse and keyboard on a private Gitea). usage: record.py all | SCENE..."""
import sys, os, json, time, subprocess
sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson64')
from uidrv import *
import term, video as V
MEASURE = os.environ.get('MEASURE') == '1'
LD = '/home/claude/academy/lesson64'; H = 'http://127.0.0.1:3000'; PW = open('/tmp/gt/adminpw').read().strip()
dur = json.load(open(LD + '/vo/dur.json'))
FIX = '/tmp/seedwork'
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
def login(u, who):
    u.ctx.clear_cookies(); u.goto(H + '/user/login'); u.wait(0.6)
    u.click('input[name=user_name]'); u.type(who, 80); u.click('input[name=password]'); u.type(PW, 40); u.key('Return'); u.wait(1.8)
def s_token(u):
    S = Sc(u, 'token')
    S.at('tk1', 0.0); login(u, 'sam'); u.wait(0.6); u.clickxy(1878, 24, 0.9); u.wait(0.6); u.click('a.item[href="/user/settings"]'); u.wait(1.2); u.click('a.item[href="/user/settings/applications"]'); u.wait(1.0)
    S.at('tk2', 0.1); u.clickxy(1087, 249); u.type('ci-readonly', 90); u.wait(0.6)
    S.at('tk3', 0.1); u.clickxy(1100, 659, 1.0); u.wait(1.0); u.move(1100, 560, 0.7); u.wait(0.8)
    S.at('tk4', 0.1); u.clickxy(663, 740, 0.9); u.wait(2.2)
    S.at('tk5', 0.3); u.wait(2.0)
    S.end()
def s_access(u):
    S = Sc(u, 'access')
    S.at('ac1', 0.0); u.goto(H + '/sam/team-app'); u.wait(1.0); u.clickxy(1550, 117, 0.9); u.wait(1.0); u.clickxy(381, 269, 0.8); u.wait(1.0)
    S.at('ac2', 0.2); u.move(650, 229, 0.8); u.wait(1.0)
    S.at('ac3', 0.1); u.clickxy(1457, 229, 0.9); u.wait(0.9); u.click('.ui.dropdown .menu .item:has-text("Read") >> nth=0'); u.wait(2.0)
    S.at('ac4', 0.3); u.move(900, 300, 0.7); u.wait(1.5)
    S.end()
if __name__ == '__main__':
    subprocess.run(['sh', LD + '/reseed.sh'], capture_output=True)
    if MEASURE and os.path.exists(LD + '/measure.json'): os.remove(LD + '/measure.json')
    u = UI(rec=False)
    for n, f in [('token', s_token), ('access', s_access)]:
        if sys.argv[1:] in (['all'], []) or n in sys.argv[1:]: f(u)
    u.close()
