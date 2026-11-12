cd /home/claude/academy
python3 - <<'PY'
import sys, json, subprocess
sys.path.insert(0, 'lesson64'); sys.path.insert(0, 'common')
import video as V, term
dur = json.load(open('lesson64/vo/dur.json'))
for s in ['token', 'access']:
    C, D, f = term.cue_times(V, dur, s)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', 'color=c=black:s=1920x1080:r=30', '-t', str(D), '-c:v', 'libx264', '-pix_fmt', 'yuv420p', f'lesson64/build/{s}.mp4'], check=True)
PY
for s in hook model leak ssh task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson64 scene {} > lesson64/build_{}.log 2>&1'
python3 common/pipe.py lesson64 av > lesson64/av.log 2>&1
python3 common/overlay_term.py lesson64 leak ssh > lesson64/ov.log 2>&1
python3 lesson64/overlay_ui.py lesson64 >> lesson64/ov.log 2>&1
echo done > lesson64/ALLDONE
