cd /home/claude/academy
for s in hook parts live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson97 scene {} > lesson97/build_{}.log 2>&1'
python3 common/pipe.py lesson97 av > lesson97/av.log 2>&1
python3 common/overlay_term.py lesson97 > lesson97/ov.log 2>&1
echo done > lesson97/ALLDONE
