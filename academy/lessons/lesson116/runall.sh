cd /home/claude/academy
for s in hook plan arch live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson116 scene {} > lesson116/build_{}.log 2>&1'
python3 common/pipe.py lesson116 av > lesson116/av.log 2>&1
python3 common/overlay_term.py lesson116 > lesson116/ov.log 2>&1
echo done > lesson116/ALLDONE
