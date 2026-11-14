cd /home/claude/academy
for s in hook what inside scope task rubric yourturn recap war; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson89 scene {} > lesson89/build_{}.log 2>&1'
python3 common/pipe.py lesson89 av > lesson89/av.log 2>&1
python3 common/overlay_term.py lesson89 > lesson89/ov.log 2>&1
echo done > lesson89/ALLDONE
