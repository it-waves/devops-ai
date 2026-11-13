cd /home/claude/academy
for s in hook probes errors logs metrics models task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson73 scene {} > lesson73/build_{}.log 2>&1'
python3 common/pipe.py lesson73 av > lesson73/av.log 2>&1
python3 common/overlay_term.py lesson73 > lesson73/ov.log 2>&1
echo done > lesson73/ALLDONE
