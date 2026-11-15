cd /home/claude/academy
for s in hook parts live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson99 scene {} > lesson99/build_{}.log 2>&1'
python3 common/pipe.py lesson99 av > lesson99/av.log 2>&1
python3 common/overlay_term.py lesson99 > lesson99/ov.log 2>&1
echo done > lesson99/ALLDONE
