cd /home/claude/academy
for s in hook why task rubric yourturn recap cli shell; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson52 scene {} > lesson52/build_{}.log 2>&1'
python3 common/pipe.py lesson52 av > lesson52/av.log 2>&1
python3 common/overlay_term.py lesson52 > lesson52/ov.log 2>&1
echo done > lesson52/ALLDONE
