cd /home/claude/academy
for s in hook plan live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson111 scene {} > lesson111/build_{}.log 2>&1'
python3 common/pipe.py lesson111 av > lesson111/av.log 2>&1
python3 common/overlay_term.py lesson111 > lesson111/ov.log 2>&1
echo done > lesson111/ALLDONE
