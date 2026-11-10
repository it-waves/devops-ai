"""usage: overlay_term.py LESSON_DIR [scene...]  -- overlay recorded sync clips (build/clips.json) onto rendered scene mp4s"""
import json, os, subprocess, sys
LD = os.path.abspath(sys.argv[1]); sys.path.insert(0, LD); sys.path.insert(0, '/home/claude/academy/common')
import importlib; V = importlib.import_module('video'); import term
B = LD + '/build/'; dur = json.load(open(LD + '/vo/dur.json'))
def dur_of(f): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).decode())
clips = json.load(open(B + 'clips.json')); only = sys.argv[2:]
for scene, info in clips.items():
    if only and scene not in only: continue
    if not os.path.exists(B + scene + '.mp4') and not os.path.exists(B + scene + '_base.mp4'): print('skip', scene); continue
    C, D, first = term.cue_times(V, dur, scene); st = C[first] + 0.3
    base = B + scene + '_base.mp4'
    if not os.path.exists(base): os.replace(B + scene + '.mp4', base)
    f = f"[1:v]setpts=PTS-STARTPTS,scale=1080:600[c];[0:v][c]overlay=110:342:enable='gte(t,{st})':eof_action=repeat,format=yuv420p[o]"
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', base, '-ss', '1.0', '-i', info['file'], '-filter_complex', f, '-map', '[o]', '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-t', str(dur_of(base)), B + scene + '.mp4'], check=True)
    print('overlay', scene, round(st, 1))
