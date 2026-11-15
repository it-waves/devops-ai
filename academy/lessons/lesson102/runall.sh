cd /home/claude/academy
for s in hook parts live decide task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson102 scene {} > lesson102/build_{}.log 2>&1'
python3 common/pipe.py lesson102 av > lesson102/av.log 2>&1
python3 common/overlay_term.py lesson102 > lesson102/ov.log 2>&1
echo done > lesson102/ALLDONE
