cd /home/claude/academy
for s in hook why task rubric yourturn recap tool tests; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson55 scene {} > lesson55/build_{}.log 2>&1'
python3 common/pipe.py lesson55 av > lesson55/av.log 2>&1
python3 common/overlay_term.py lesson55 > lesson55/ov.log 2>&1
echo done > lesson55/ALLDONE
