cd /home/claude/academy
for s in hook why task rubric yourturn recap exceptions logging retry; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson51 scene {} > lesson51/build_{}.log 2>&1'
python3 common/pipe.py lesson51 av > lesson51/av.log 2>&1
python3 common/overlay_term.py lesson51 > lesson51/ov.log 2>&1
echo done > lesson51/ALLDONE
