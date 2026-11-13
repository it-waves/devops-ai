cd /home/claude/academy
for s in hook scenario getlab notes report hints rubric yourturn recap start fix1 cleanup; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson84 scene {} > lesson84/build_{}.log 2>&1'
python3 common/pipe.py lesson84 av > lesson84/av.log 2>&1
python3 common/overlay_term.py lesson84 > lesson84/ov.log 2>&1
echo done > lesson84/ALLDONE
