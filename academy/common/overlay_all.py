"""Overlay recorded clips onto rendered scene mp4s. Needs build/clips.json (scene -> {mode, file})."""
import json, os, subprocess, sys, shutil
sys.path.insert(0, '/home/claude/academy/common'); import lab_times
B = '/home/claude/academy/lesson13/build/'
def dur_of(f): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).decode())
clips = json.load(open(B + 'clips.json'))
only = sys.argv[1:] 
for scene, info in clips.items():
    if only and scene not in only: continue
    if not os.path.exists(B + scene + '.mp4') and not os.path.exists(B + scene + '_base.mp4'): print('skip', scene); continue
    C, D, first = lab_times.times(scene); st = C[first] + 0.3
    base = B + scene + '_base.mp4'
    if not os.path.exists(base): os.replace(B + scene + '.mp4', base)
    W, H, X, Y = (1080, 589, 110, 335) if info.get('gui') else (1080, 600, 110, 342)
    if info['mode'] == 'sync':
        f = f"[1:v]setpts=PTS-STARTPTS,scale={W}:{H}[c]"; ss = ['-ss', '1.0']
    else:
        L = dur_of(info['file']) - 1.0; k = max(1.0, L / max(1.0, (D - st - 0.5))); f = f"[1:v]setpts=(PTS-STARTPTS)/{k}+{st}/TB,scale={W}:{H}[c]"; ss = ['-ss', '1.0']
    f += f";[0:v][c]overlay={X}:{Y}:enable='gte(t,{st})':eof_action=repeat,format=yuv420p[o]"
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', base, *ss, '-i', info['file'], '-filter_complex', f, '-map', '[o]', '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-t', str(dur_of(base)), B + scene + '.mp4'], check=True)
    print('overlay', scene, round(st, 1), info['mode'])
