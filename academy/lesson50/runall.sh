cd /home/claude/academy
for s in hook why task rubric yourturn recap basics auth timeout pages; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson50 scene {} > lesson50/build_{}.log 2>&1'
python3 common/pipe.py lesson50 av > lesson50/av.log 2>&1
python3 common/overlay_term.py lesson50 > lesson50/ov.log 2>&1
echo done > lesson50/ALLDONE
