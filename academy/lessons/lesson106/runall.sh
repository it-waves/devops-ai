cd /home/claude/academy
for s in hook plan live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson106 scene {} > lesson106/build_{}.log 2>&1'
python3 common/pipe.py lesson106 av > lesson106/av.log 2>&1
python3 common/overlay_term.py lesson106 > lesson106/ov.log 2>&1
echo done > lesson106/ALLDONE
