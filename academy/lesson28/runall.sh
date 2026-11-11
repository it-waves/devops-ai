cd /home/claude/academy
for s in hook myths rubric yourturn recap redirect pipe grep sortcut archive; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson28 scene {} > lesson28/build_{}.log 2>&1'
python3 common/pipe.py lesson28 av > lesson28/av.log 2>&1
python3 common/overlay_term.py lesson28 > lesson28/ov.log 2>&1
echo done > lesson28/ALLDONE
