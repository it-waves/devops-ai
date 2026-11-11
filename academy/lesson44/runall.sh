cd /home/claude/academy
for s in hook myths rubric yourturn recap idem fix state finds fixes build; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson44 scene {} > lesson44/build_{}.log 2>&1'
python3 common/pipe.py lesson44 av > lesson44/av.log 2>&1
python3 common/overlay_term.py lesson44 > lesson44/ov.log 2>&1
echo done > lesson44/ALLDONE
