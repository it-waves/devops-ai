cd /home/claude/academy
for s in hook why task rubric yourturn recap pytest mock; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson53 scene {} > lesson53/build_{}.log 2>&1'
python3 common/pipe.py lesson53 av > lesson53/av.log 2>&1
python3 common/overlay_term.py lesson53 > lesson53/ov.log 2>&1
echo done > lesson53/ALLDONE
