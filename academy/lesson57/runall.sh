cd /home/claude/academy
for s in hook why anat task rubric yourturn recap init commit objs clone ui; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson57 scene {} > lesson57/build_{}.log 2>&1'
python3 common/pipe.py lesson57 av > lesson57/av.log 2>&1
python3 common/overlay_term.py lesson57 > lesson57/ov.log 2>&1
echo done > lesson57/ALLDONE
