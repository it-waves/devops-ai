cd /home/claude/academy
for s in hook myths rubric yourturn recap ids perms sudo ssh; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson29 scene {} > lesson29/build_{}.log 2>&1'
python3 common/pipe.py lesson29 av > lesson29/av.log 2>&1
python3 common/overlay_term.py lesson29 > lesson29/ov.log 2>&1
echo done > lesson29/ALLDONE
