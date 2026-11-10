import sys, time, subprocess; sys.path.insert(0, '/home/claude/academy/common')
import lab_record as L
E = L.E99
def x(*a): subprocess.run(['xdotool', *map(str, a)], env=E)
cur = [440, 240]
def move(tx, ty, d=0.9):
    sx, sy = cur; n = max(8, int(d * 25))
    for i in range(1, n + 1):
        p = i / n; e = p * p * (3 - 2 * p); x('mousemove', int(sx + (tx - sx) * e), int(sy + (ty - sy) * e)); time.sleep(d / n)
    cur[:] = [tx, ty]
def click(tx, ty, d=0.8): move(tx, ty, d); time.sleep(0.15); x('click', 1); time.sleep(0.15)
# reset: Details view
x('mousemove', 291, 112, 'click', 1); time.sleep(1); x('mousemove', 400, 106, 'click', 1); time.sleep(1.5); cur[:] = [400, 106]
r = L.Run('snapvb', env=E, size='880x480')
r.at('sv1', 0.8); click(291, 112, 1.0)
r.at('sv1', 3.0); click(400, 152, 0.8)
r.at('sv1', 6.0); click(348, 50, 1.0)
time.sleep(1.5); click(460, 103, 0.7); x('key', 'ctrl+a'); L.typ('clean-install', 110, env=E)
r.at('sv1', 12.0); click(377, 356, 0.8)
r.at('sv2', 1.0); move(450, 150, 1.0)
r.end(); L.save_clip('snapvb', mode='sync', file=r.out, gui=True)
