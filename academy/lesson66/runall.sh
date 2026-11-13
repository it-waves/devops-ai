cd /home/claude/academy
for s in hook scenario getlab notes report hints rubric yourturn recap start fix1 cleanup; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson66 scene {} > lesson66/build_{}.log 2>&1'
python3 common/pipe.py lesson66 av > lesson66/av.log 2>&1
python3 common/overlay_term.py lesson66 > lesson66/ov.log 2>&1
echo done > lesson66/ALLDONE
