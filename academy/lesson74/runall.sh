cd /home/claude/academy
for s in hook draw parts trace layers models task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson74 scene {} > lesson74/build_{}.log 2>&1'
python3 common/pipe.py lesson74 av > lesson74/av.log 2>&1
python3 common/overlay_term.py lesson74 > lesson74/ov.log 2>&1
echo done > lesson74/ALLDONE
