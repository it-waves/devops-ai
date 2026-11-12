cd /home/claude/academy
for s in hook model golden task rubric yourturn recap amend rebase rconf; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson60 scene {} > lesson60/build_{}.log 2>&1'
python3 common/pipe.py lesson60 av > lesson60/av.log 2>&1
python3 common/overlay_term.py lesson60 > lesson60/ov.log 2>&1
echo done > lesson60/ALLDONE
