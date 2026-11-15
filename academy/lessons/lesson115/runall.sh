cd /home/claude/academy
for s in hook plan arch live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson115 scene {} > lesson115/build_{}.log 2>&1'
python3 common/pipe.py lesson115 av > lesson115/av.log 2>&1
python3 common/overlay_term.py lesson115 > lesson115/ov.log 2>&1
echo done > lesson115/ALLDONE
