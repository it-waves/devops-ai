cd /home/claude/academy
for s in hook scenario getlab notes report hints rubric yourturn recap start fix1 cleanup; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson46 scene {} > lesson46/build_{}.log 2>&1'
python3 common/pipe.py lesson46 av > lesson46/av.log 2>&1
python3 common/overlay_term.py lesson46 > lesson46/ov.log 2>&1
echo done > lesson46/ALLDONE
