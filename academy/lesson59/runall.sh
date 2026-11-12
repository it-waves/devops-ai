cd /home/claude/academy
for s in hook model kinds marks task rubric yourturn recap branch merge conflict; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson59 scene {} > lesson59/build_{}.log 2>&1'
python3 common/pipe.py lesson59 av > lesson59/av.log 2>&1
python3 common/overlay_term.py lesson59 > lesson59/ov.log 2>&1
echo done > lesson59/ALLDONE
