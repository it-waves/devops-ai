cd /home/claude/academy
for s in hook why task rubric yourturn recap files json yaml csv env; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson49 scene {} > lesson49/build_{}.log 2>&1'
python3 common/pipe.py lesson49 av > lesson49/av.log 2>&1
python3 common/overlay_term.py lesson49 > lesson49/ov.log 2>&1
echo done > lesson49/ALLDONE
