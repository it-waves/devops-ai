cd /home/claude/academy
for s in hook layers env flags failfast models task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson71 scene {} > lesson71/build_{}.log 2>&1'
python3 common/pipe.py lesson71 av > lesson71/av.log 2>&1
python3 common/overlay_term.py lesson71 > lesson71/ov.log 2>&1
echo done > lesson71/ALLDONE
