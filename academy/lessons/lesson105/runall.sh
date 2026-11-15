cd /home/claude/academy
for s in hook plan live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson105 scene {} > lesson105/build_{}.log 2>&1'
python3 common/pipe.py lesson105 av > lesson105/av.log 2>&1
python3 common/overlay_term.py lesson105 > lesson105/ov.log 2>&1
echo done > lesson105/ALLDONE
