cd /home/claude/academy
for s in hook model task rubric yourturn recap clone fetch push tags; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson61 scene {} > lesson61/build_{}.log 2>&1'
python3 common/pipe.py lesson61 av > lesson61/av.log 2>&1
python3 common/overlay_term.py lesson61 > lesson61/ov.log 2>&1
echo done > lesson61/ALLDONE
