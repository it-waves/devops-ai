cd /home/claude/academy
for s in hook why live task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson93 scene {} > lesson93/build_{}.log 2>&1'
python3 common/pipe.py lesson93 av > lesson93/av.log 2>&1
python3 common/overlay_term.py lesson93 > lesson93/ov.log 2>&1
echo done > lesson93/ALLDONE
