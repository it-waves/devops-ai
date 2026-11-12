cd /home/claude/academy
for s in hook why task rubric yourturn recap setup activate deps repro layout cleanup; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson47 scene {} > lesson47/build_{}.log 2>&1'
python3 common/pipe.py lesson47 av > lesson47/av.log 2>&1
python3 common/overlay_term.py lesson47 > lesson47/ov.log 2>&1
echo done > lesson47/ALLDONE
