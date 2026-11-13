"""overlay_ui.py LESSON_DIR : turn recorded full-screen UI clips (mode full) into the scene videos, with a step label strip"""
import json, os, subprocess, sys
LD = os.path.abspath(sys.argv[1]); sys.path.insert(0, LD); sys.path.insert(0, '/home/claude/academy/common')
import importlib; V = importlib.import_module('video'); import term
B = LD + '/build/'; dur = json.load(open(LD + '/vo/dur.json'))
def dur_of(f): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).decode())
clips = json.load(open(B + 'clips.json')); FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for scene, info in clips.items():
    if info.get('mode') != 'full': continue
    if not os.path.exists(B + scene + '.mp4') and not os.path.exists(B + scene + '_base.mp4'): print('skip', scene); continue
    C, D, first = term.cue_times(V, dur, scene); base = B + scene + '_base.mp4'
    if not os.path.exists(base): os.replace(B + scene + '.mp4', base)
    ids = [c[0] for c in dict(V.SCENES)[scene]]
    f = '[0:v]setpts=PTS-STARTPTS,scale=1920:1080,drawbox=x=0:y=1000:w=1920:h=80:color=0x0b1a1e@0.90:t=fill,drawbox=x=0:y=1000:w=1920:h=4:color=0xffd24a@1:t=fill'
    for i, cid in enumerate(ids):
        a = C[cid]; b = C[ids[i + 1]] if i + 1 < len(ids) else D
        lab = V.UI_LABEL.get(cid, '').replace("'", '').replace(':', '\\:').replace('%', '\\%')
        if lab: f += f",drawtext=fontfile={FONT}:text='{lab}':fontsize=34:fontcolor=0xffffff:x=40:y=1025:enable='between(t,{a:.2f},{b:.2f})'"
    f += f",drawtext=fontfile={FONT}:text='REAL RECORDING  ·  Chrome on this computer, local Maven repo copy':fontsize=22:fontcolor=0x7fe0d0:x=w-tw-40:y=1018,drawtext=fontfile={FONT}:text='Maven Central uses the same folder layout':fontsize=20:fontcolor=0xbcd0d2:x=w-tw-40:y=1046,format=yuv420p[o]"
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '1.0', '-i', info['file'], '-filter_complex', f, '-map', '[o]', '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-t', str(dur_of(base)), B + scene + '.mp4'], check=True)
    print('ui overlay', scene)
