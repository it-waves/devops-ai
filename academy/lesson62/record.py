"""Record Lesson 62 live UI scenes (continuous full-screen browser recording, real mouse and keyboard on a private Gitea). usage: record.py all | SCENE..."""
import sys, os, json, time, subprocess
sys.path.insert(0, '/home/claude/academy/common'); sys.path.insert(0, '/home/claude/academy/lesson62')
from uidrv import *
import term, video as V
MEASURE = os.environ.get('MEASURE') == '1'
LD = '/home/claude/academy/lesson62'; H = 'http://127.0.0.1:3000'; PW = open('/tmp/gt/adminpw').read().strip()
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
def s_protect(u):
    S = Sc(u, 'protect')
    S.at('p1', 0.0); login(u, 'sam'); u.click('a:has-text("sam/team-app")', dur=0.9); u.wait(1.0)
    S.at('p2', 0.1); u.click('a[href="/sam/team-app/settings"]')
    S.at('p3', 0.1); u.click('a[href="/sam/team-app/settings/branches"]'); u.wait(0.8); u.click('a:has-text("Add New Rule")')
    S.at('p4', 0.1); u.click('input[name=rule_name]'); u.type('main', 110)
    S.at('p5', 0.1); scroll(u, 420, 1.6)
    S.at('p6', 0.1); u.click('input[name=required_approvals]'); u.key('ctrl+a'); u.type('1', 120); u.wait(0.8)
    S.at('p7', 0.1); u.click('button:has-text("Save Rule")', dur=0.9); u.wait(2.0)
    S.end()
def s_pr(u):
    S = Sc(u, 'pr')
    S.at('q1', 0.1); u.click('a[href="/sam/team-app/pulls"]'); u.wait(0.8)
    S.at('q2', 0.1); u.click('a:has-text("New Pull Request")'); u.wait(1.2)
    u.clickxy(390, 246); u.wait(0.8); u.clickxy(403, 377); u.wait(1.5)
    S.at('q3', 0.3); scroll(u, 360, 1.8)
    S.at('q4', 0.1); scroll(u, -360, 0.8); u.click('button:has-text("New Pull Request")'); u.wait(0.8)
    u.click('input[name=title]'); u.key('ctrl+a'); u.type('Add a health check script', 50)
    u.click('textarea[name=content]'); u.type('Adds health.sh, and documents it in the readme so the team can run it.', 35)
    S.at('q5', 0.1); u.click('button:has-text("Create Pull Request")', dur=0.9); u.wait(2.0)
    S.at('q6', 0.3); 
    for sel in ['a.item:has-text("Commits") >> nth=0', 'a.item:has-text("Files Changed") >> nth=0']:
        b = u.box(sel); u.move(b['x'] + b['width'] / 2, b['y'] + b['height'] / 2, 0.8); u.wait(0.8)
    u.click('a.item:has-text("Conversation") >> nth=0'); u.wait(0.5)
    S.at('q7', 0.2); scroll(u, 520, 1.6); u.wait(0.5)
    S.end()
def s_review(u):
    S = Sc(u, 'review')
    S.at('r1', 0.0); login(u, 'alex'); u.goto(H + '/sam/team-app/pulls/1'); u.wait(1.0)
    S.at('r2', 0.1); u.click('a.item:has-text("Files Changed") >> nth=0'); u.wait(1.5)
    S.at('r3', 0.1); n = u.pg.locator('tr.add-code').count() - 1; b = u.box('tr.add-code', n); u.move(b['x'] + 700, b['y'] + 10, 0.7); u.wait(0.3)
    u.click(f'tr.add-code >> nth={n} >> button.add-code-comment'); u.wait(0.6); u.click('textarea[name=content]'); u.type('Please check that curl exists, and use the port from app.conf.', 40)
    S.at('r4', 0.1); u.click('button:has-text("Start review")'); u.wait(3.2); u.clickxy(1830, 326); u.wait(1.0)
    S.at('r5', 0.1); u.click('.review-box-panel textarea, textarea[name=content] >> nth=-1'); u.type('Almost there. Two small fixes, then I will approve.', 40); u.clickxy(1424, 725); u.wait(2.5)
    S.at('r6', 0.1); u.click('a.item:has-text("Conversation") >> nth=0'); u.wait(0.6)
    S.at('r6', 4.0)
    subprocess.run(f"cd {FIX} && printf '#!/bin/sh\\ncommand -v curl >/dev/null || exit 1\\ncurl -s localhost:80 > /dev/null && echo healthy\\n' > health.sh && git add -A && git -c user.name='Sam Lee' -c user.email=sam@example.com commit -qm 'Check that curl exists' && git push -q origin feature/health-check", shell=True, capture_output=True)
    S.at('r7', 0.2); u.pg.reload(); u.wait(1.0); u.pg.evaluate(CURSOR_JS); scroll(u, 500, 1.4)
    S.at('r8', 0.1); u.goto(H + '/sam/team-app/pulls/1/files'); u.wait(1.2); u.clickxy(1830, 326); u.wait(0.8)
    u.click('.review-box-panel textarea, textarea[name=content] >> nth=-1'); u.type('Looks good now. Approved.', 40); u.clickxy(1211, 725); u.wait(2.5)
    S.at('r9', 0.2); u.goto(H + '/sam/team-app/pulls/1'); u.wait(1.0); scroll(u, 900, 1.4)
    S.end()
def s_merge(u):
    S = Sc(u, 'merge')
    S.at('m1', 0.1); u.click('.merge-section .ui.dropdown.icon.button'); u.wait(0.6)
    S.at('m2', 0.1)
    S.at('m3', 0.1); u.click(".merge-section .menu .item:has-text('Create squash commit')"); u.wait(0.8)
    S.at('m4', 0.1); u.click('.merge-section .ui.button >> nth=0'); u.wait(1.0)
    u.click('.merge-section input[type=checkbox]:visible, .merge-section label:has-text("Delete Branch")'); u.wait(0.8)
    u.wait(2.5); u.click('.merge-section button:has-text("Create squash commit")'); u.wait(2.5)
    S.at('m5', 0.2); scroll(u, -300, 0.8); u.wait(1.0)
    S.at('m6', 0.1); u.goto(H + '/sam/team-app/commits/branch/main'); u.wait(1.5)
    S.end()
if __name__ == '__main__':
    subprocess.run(['sh', LD + '/reseed.sh'], capture_output=True)
    if MEASURE and os.path.exists(LD + '/measure.json'): os.remove(LD + '/measure.json')
    u = UI(rec=False)
    for n, f in [('protect', s_protect), ('pr', s_pr), ('review', s_review), ('merge', s_merge)]:
        if sys.argv[1:] in (['all'], []) or n in sys.argv[1:]: f(u)
    u.close()
