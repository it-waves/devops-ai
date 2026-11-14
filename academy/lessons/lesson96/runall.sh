cd /home/claude/academy
for s in hook parts live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson96 scene {} > lesson96/build_{}.log 2>&1'
python3 common/pipe.py lesson96 av > lesson96/av.log 2>&1
python3 common/overlay_term.py lesson96 > lesson96/ov.log 2>&1
echo done > lesson96/ALLDONE
