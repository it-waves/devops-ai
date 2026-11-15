cd /home/claude/academy
for s in hook plan live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson112 scene {} > lesson112/build_{}.log 2>&1'
python3 common/pipe.py lesson112 av > lesson112/av.log 2>&1
python3 common/overlay_term.py lesson112 > lesson112/ov.log 2>&1
echo done > lesson112/ALLDONE
