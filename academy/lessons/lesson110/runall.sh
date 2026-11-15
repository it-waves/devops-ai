cd /home/claude/academy
for s in hook plan live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson110 scene {} > lesson110/build_{}.log 2>&1'
python3 common/pipe.py lesson110 av > lesson110/av.log 2>&1
python3 common/overlay_term.py lesson110 > lesson110/ov.log 2>&1
echo done > lesson110/ALLDONE
