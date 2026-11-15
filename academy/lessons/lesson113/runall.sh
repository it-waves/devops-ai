cd /home/claude/academy
for s in hook plan arch live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson113 scene {} > lesson113/build_{}.log 2>&1'
python3 common/pipe.py lesson113 av > lesson113/av.log 2>&1
python3 common/overlay_term.py lesson113 > lesson113/ov.log 2>&1
echo done > lesson113/ALLDONE
