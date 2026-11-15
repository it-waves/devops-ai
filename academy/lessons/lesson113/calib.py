"""Dry run of the tour in display :98, one screenshot per step. usage: calib.py FIRST_INDEX LAST_INDEX"""
import subprocess, time, sys, os
sys.path.insert(0, '/home/claude/academy/lesson113')
from tour import TOUR
E = dict(os.environ, DISPLAY=':98')
def xt(*a): subprocess.run(['xdotool', *map(str, a)], env=E)
def shot(n): subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'x11grab', '-video_size', '1920x1080', '-i', ':98', '-frames:v', '1', '-vf', 'scale=640:360', f'/tmp/shots/c_{n:02d}.png'], env=E)
a, b = int(sys.argv[1]), int(sys.argv[2])
for i, (cid, acts) in enumerate(TOUR):
    if i < a or i > b: continue
    for f, act in acts:
        k = act[0]
        if k == 'chrome':
            subprocess.Popen(['google-chrome','--no-sandbox','--incognito','--user-data-dir=/tmp/chp98','--no-first-run','--no-default-browser-check','--disable-gpu','--disable-infobars','--test-type','--window-position=0,0','--force-device-scale-factor=1.25','--window-size=1536,864','about:blank'], env=E, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(5)
        if k == 'type': xt('type', '--delay', 80, act[1])
        elif k == 'key': xt('key', act[1])
        elif k == 'move': xt('mousemove', act[1], act[2]); time.sleep(0.15)
        elif k == 'click': xt('mousemove', act[1], act[2]); time.sleep(0.3); xt('click', 1)
        elif k == 'scroll':
            for _ in range(act[1]): xt('click', '5'); time.sleep(0.12)
        elif k == 'up':
            for _ in range(act[1]): xt('click', '4'); time.sleep(0.12)
        time.sleep(0.5)
    time.sleep(0.8); shot(i); print(i, cid, flush=True)
