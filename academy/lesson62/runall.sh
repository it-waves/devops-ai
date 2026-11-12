cd /home/claude/academy
python3 - <<'PY'
import sys, json, subprocess
sys.path.insert(0, 'lesson62'); sys.path.insert(0, 'common')
import video as V, term
dur = json.load(open('lesson62/vo/dur.json'))
for s in ['protect', 'pr', 'review', 'merge']:
    C, D, f = term.cue_times(V, dur, s)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'color=c=black:s=1920x1080:r=30', '-t', str(D), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', f'lesson62/build/{s}.mp4'], check=True)
PY
for s in hook model task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson62 scene {} > lesson62/build_{}.log 2>&1'
python3 common/pipe.py lesson62 av > lesson62/av.log 2>&1
python3 lesson62/overlay_ui.py lesson62 > lesson62/ov.log 2>&1
echo done > lesson62/ALLDONE
