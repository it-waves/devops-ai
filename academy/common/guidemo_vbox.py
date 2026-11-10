"""Drive VirtualBox's New VM wizard on Xvfb :99 (880x480), timed to Lesson 13 cues. usage: guidemo_vbox.py [dry|rec OUT.mp4 SECONDS]"""
import os, sys, time, json, re, subprocess
sys.path.insert(0, '/home/claude/academy/lesson13'); sys.path.insert(0, '/home/claude/academy/common')
import importlib; V = importlib.import_module('video')
E = dict(os.environ, DISPLAY=':99', HOME='/tmp/guihome')
def x(*a): subprocess.run(['xdotool', *map(str, a)], env=E, check=False)
dur = json.load(open('/home/claude/academy/lesson13/vo/dur.json')); SENT = re.compile(r'[.?!:]$')
C = {}
for name, cues in V.SCENES:
    if name != 'vbox': continue
    t = 0.5
    for c in cues:
        cid, cap = c[0], c[1]; gap = c[3] if len(c) > 3 and c[3] is not None else (0.55 if SENT.search(cap) else 0.13)
        C[cid] = t; t += dur[cid] + gap + V.EXTRA.get(cid, 0)
    D = round(t - 0.4 + 0.9, 3)
mode = sys.argv[1]; shots = '/tmp/gui/dry'; os.makedirs(shots, exist_ok=True)
cur = [440, 240]
def move(tx, ty, d=0.9):
    sx, sy = cur; n = max(8, int(d * 25))
    for i in range(1, n + 1):
        p = i / n; e = p * p * (3 - 2 * p); x('mousemove', int(sx + (tx - sx) * e), int(sy + (ty - sy) * e)); time.sleep(d / n)
    cur[:] = [tx, ty]
def click(tx, ty, d=0.8): move(tx, ty, d); time.sleep(0.15); x('click', 1); time.sleep(0.15)
def triple(tx, ty, d=0.7): move(tx, ty, d); x('click', '--repeat', 3, '--delay', 80, 1)
def typ(s, delay=140): x('type', '--delay', delay, s)
def shot(n):
    if mode == 'dry': subprocess.run(['import', '-window', 'root', f'{shots}/{n}.png'], env=E)
T0 = [0]
def at(cid, off=0.0):
    t = T0[0] + C[cid] + off - time.time()
    if t > 0: time.sleep(t)
def run():
    T0[0] = time.time()
    shot('0_start')
    at('b3', 0.3); click(536, 60, 1.0); time.sleep(1.6); shot('1_open')
    at('b3', 3.2); click(535, 133, 0.9); typ('lab'); time.sleep(0.4)
    at('b3', 4.8); click(520, 257, 0.8); time.sleep(0.5); typ('Linux', 120); time.sleep(0.3); x('key', 'Return'); time.sleep(0.5)
    at('b3', 6.8); click(520, 288, 0.7); time.sleep(0.5); typ('Ubuntu (64', 120); time.sleep(0.3); x('key', 'Return'); time.sleep(0.4); shot('2_named')
    at('b3', 8.8); move(535, 196, 1.0)
    at('b4', 0.3); click(710, 404, 1.0); time.sleep(1.2); shot('3_hw')
    move(790, 117, 1.0); time.sleep(0.8)
    at('b4', 3.4); triple(813, 165); typ('2'); x('key', 'Tab'); time.sleep(0.6); shot('4_cpu')
    at('b5', 0.3); click(710, 404, 1.0); time.sleep(1.2); shot('5_disk0')
    at('b5', 2.2); triple(785, 161); typ('20'); x('key', 'Tab'); time.sleep(0.6); shot('6_disk')
    at('b6', 0.3); click(710, 404, 1.0); time.sleep(1.5); shot('7_summary'); move(712, 380, 0.8)
    at('b6', 4.3); click(710, 404, 0.8); time.sleep(3.0); shot('8_done')
    at('b7', 1.0); move(600, 120, 1.2); shot('9_end')
if mode == 'dry': run()
else:
    out, secs = sys.argv[2], float(sys.argv[3])
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-draw_mouse', '1', '-framerate', '30', '-video_size', '880x480', '-i', ':99', '-t', str(secs + 1.0), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p', out], env=E)
    time.sleep(1.0); run(); ff.wait()
print('D', D)
