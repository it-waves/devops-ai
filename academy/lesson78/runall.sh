cd /home/claude/academy
for s in hook ideas models task rubric yourturn recap build config; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson78 scene {} > lesson78/build_{}.log 2>&1'
python3 common/pipe.py lesson78 av > lesson78/av.log 2>&1
python3 common/overlay_term.py lesson78 > lesson78/ov.log 2>&1
echo done > lesson78/ALLDONE
