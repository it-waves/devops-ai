cd /home/claude/academy
for s in hook what settings secrets task rubric yourturn recap mirror; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson90 scene {} > lesson90/build_{}.log 2>&1'
python3 common/pipe.py lesson90 av > lesson90/av.log 2>&1
python3 common/overlay_term.py lesson90 > lesson90/ov.log 2>&1
echo done > lesson90/ALLDONE
