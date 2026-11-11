cd /home/claude/academy
for s in hook manage myths rubric yourturn recap repo installed plan; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson32 scene {} > lesson32/build_{}.log 2>&1'
python3 common/pipe.py lesson32 av > lesson32/av.log 2>&1
python3 common/overlay_term.py lesson32 > lesson32/ov.log 2>&1
echo done > lesson32/ALLDONE
