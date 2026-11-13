cd /home/claude/academy
for s in hook memory scale db models task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson72 scene {} > lesson72/build_{}.log 2>&1'
python3 common/pipe.py lesson72 av > lesson72/av.log 2>&1
python3 common/overlay_term.py lesson72 > lesson72/ov.log 2>&1
echo done > lesson72/ALLDONE
