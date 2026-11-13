cd /home/claude/academy
python3 - <<'PY'
import sys, json, subprocess
sys.path.insert(0, 'lesson85'); sys.path.insert(0, 'common')
import video as V, term
dur = json.load(open('lesson85/vo/dur.json'))
for s in ['repo']:
    C, D, f = term.cue_times(V, dur, s)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'color=c=black:s=1920x1080:r=30', '-t', str(D), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', f'lesson85/build/{s}.mp4'], check=True)
PY
for s in hook ideas models task rubric yourturn recap tour deps; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson85 scene {} > lesson85/build_{}.log 2>&1'
python3 common/pipe.py lesson85 av > lesson85/av.log 2>&1
python3 common/overlay_term.py lesson85 > lesson85/ov.log 2>&1
python3 lesson85/overlay_ui.py lesson85 >> lesson85/ov.log 2>&1
echo done > lesson85/ALLDONE
