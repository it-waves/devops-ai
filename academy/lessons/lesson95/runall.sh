cd /home/claude/academy
for s in hook parts live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson95 scene {} > lesson95/build_{}.log 2>&1'
python3 common/pipe.py lesson95 av > lesson95/av.log 2>&1
python3 common/overlay_term.py lesson95 > lesson95/ov.log 2>&1
echo done > lesson95/ALLDONE
