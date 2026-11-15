cd /home/claude/academy
for s in hook plan live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson108 scene {} > lesson108/build_{}.log 2>&1'
python3 common/pipe.py lesson108 av > lesson108/av.log 2>&1
python3 common/overlay_term.py lesson108 > lesson108/ov.log 2>&1
echo done > lesson108/ALLDONE
