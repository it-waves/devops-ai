cd /home/claude/academy
for s in hook scenario getlab notes report hints rubric yourturn recap start fix1 cleanup; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson36 scene {} > lesson36/build_{}.log 2>&1'
python3 common/pipe.py lesson36 av > lesson36/av.log 2>&1
python3 common/overlay_term.py lesson36 > lesson36/ov.log 2>&1
echo done > lesson36/ALLDONE
