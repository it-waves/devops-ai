cd /home/claude/academy
for s in hook trans rules fixes task rubric yourturn recap tree; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson88 scene {} > lesson88/build_{}.log 2>&1'
python3 common/pipe.py lesson88 av > lesson88/av.log 2>&1
python3 common/overlay_term.py lesson88 > lesson88/ov.log 2>&1
echo done > lesson88/ALLDONE
