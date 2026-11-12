cd /home/claude/academy
for s in hook flow msg task rubric yourturn recap stage hist ignore; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson58 scene {} > lesson58/build_{}.log 2>&1'
python3 common/pipe.py lesson58 av > lesson58/av.log 2>&1
python3 common/overlay_term.py lesson58 > lesson58/ov.log 2>&1
echo done > lesson58/ALLDONE
