cd /home/claude/academy
for s in hook plan live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson109 scene {} > lesson109/build_{}.log 2>&1'
python3 common/pipe.py lesson109 av > lesson109/av.log 2>&1
python3 common/overlay_term.py lesson109 > lesson109/ov.log 2>&1
echo done > lesson109/ALLDONE
