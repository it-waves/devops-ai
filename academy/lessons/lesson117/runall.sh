cd /home/claude/academy
for s in hook plan arch live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson117 scene {} > lesson117/build_{}.log 2>&1'
python3 common/pipe.py lesson117 av > lesson117/av.log 2>&1
python3 common/overlay_term.py lesson117 > lesson117/ov.log 2>&1
echo done > lesson117/ALLDONE
