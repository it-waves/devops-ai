cd /home/claude/academy
for s in hook why task rubric yourturn recap policy sdk; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson54 scene {} > lesson54/build_{}.log 2>&1'
python3 common/pipe.py lesson54 av > lesson54/av.log 2>&1
python3 common/overlay_term.py lesson54 > lesson54/ov.log 2>&1
echo done > lesson54/ALLDONE
