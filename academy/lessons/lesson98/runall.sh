cd /home/claude/academy
for s in hook parts live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson98 scene {} > lesson98/build_{}.log 2>&1'
python3 common/pipe.py lesson98 av > lesson98/av.log 2>&1
python3 common/overlay_term.py lesson98 > lesson98/ov.log 2>&1
echo done > lesson98/ALLDONE
