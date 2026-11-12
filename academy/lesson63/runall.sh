cd /home/claude/academy
for s in hook model restore revert reset reflog task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson63 scene {} > lesson63/build_{}.log 2>&1'
python3 common/pipe.py lesson63 av > lesson63/av.log 2>&1
python3 common/overlay_term.py lesson63 > lesson63/ov.log 2>&1
echo done > lesson63/ALLDONE
