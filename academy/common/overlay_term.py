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
    hl = ''
    for (cid, row, n, x0, x1, label) in getattr(V, 'HL', {}).get(scene, []):
        a = C[cid] + 0.35 - C[first] * 0 ; b = C[cid] + dur[cid] + 0.45; y = 6 + 30 * row; h = 30 * n
        en = f"enable='between(t,{a:.2f},{b:.2f})'"
        hl += f",drawbox=x={x0}:y={y}:w={x1 - x0}:h={h}:color=0xffd24a@0.22:t=fill:{en},drawbox=x={x0}:y={y}:w={x1 - x0}:h={h}:color=0xffd24a@0.95:t=3:{en}"
        if label: hl += f",drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='{label.replace(chr(37), chr(92) * 2 + chr(37))}':fontsize=20:fontcolor=0x0b1a1e:box=1:boxcolor=0xffd24a:boxborderw=6:x={x1 + 12}:y={y + (h - 22) // 2}:{en}"
    f = f"[1:v]setpts=PTS-STARTPTS{hl},scale=1080:600[c];[0:v][c]overlay=110:342:enable='gte(t,{st})':eof_action=repeat,format=yuv420p[o]"
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', base, '-ss', '1.0', '-i', info['file'], '-filter_complex', f, '-map', '[o]', '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-t', str(dur_of(base)), B + scene + '.mp4'], check=True)
    print('overlay', scene, round(st, 1))
