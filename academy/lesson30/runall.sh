cd /home/claude/academy
for s in hook myths rubric yourturn recap ps signals resources running; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson30 scene {} > lesson30/build_{}.log 2>&1'
python3 common/pipe.py lesson30 av > lesson30/av.log 2>&1
python3 common/overlay_term.py lesson30 > lesson30/ov.log 2>&1
echo done > lesson30/ALLDONE
