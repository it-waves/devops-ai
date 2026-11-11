cd /home/claude/academy
for s in hook order myths rubric yourturn recap run quote expand env exit; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson37 scene {} > lesson37/build_{}.log 2>&1'
python3 common/pipe.py lesson37 av > lesson37/av.log 2>&1
python3 common/overlay_term.py lesson37 > lesson37/ov.log 2>&1
echo done > lesson37/ALLDONE
