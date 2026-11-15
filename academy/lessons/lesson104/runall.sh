cd /home/claude/academy
for s in hook parts live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson104 scene {} > lesson104/build_{}.log 2>&1'
python3 common/pipe.py lesson104 av > lesson104/av.log 2>&1
python3 common/overlay_term.py lesson104 > lesson104/ov.log 2>&1
echo done > lesson104/ALLDONE
