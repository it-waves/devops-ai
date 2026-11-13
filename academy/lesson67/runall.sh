cd /home/claude/academy
for s in hook roles browser trade task rubric yourturn recap mono split; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson67 scene {} > lesson67/build_{}.log 2>&1'
python3 common/pipe.py lesson67 av > lesson67/av.log 2>&1
python3 common/overlay_term.py lesson67 > lesson67/ov.log 2>&1
echo done > lesson67/ALLDONE
