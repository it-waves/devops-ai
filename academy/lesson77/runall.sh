cd /home/claude/academy
for s in hook rules models task rubric yourturn recap run errors; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson77 scene {} > lesson77/build_{}.log 2>&1'
python3 common/pipe.py lesson77 av > lesson77/av.log 2>&1
python3 common/overlay_term.py lesson77 > lesson77/ov.log 2>&1
echo done > lesson77/ALLDONE
