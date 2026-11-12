cd /home/claude/academy
for s in hook model checks gate ci release task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson65 scene {} > lesson65/build_{}.log 2>&1'
python3 common/pipe.py lesson65 av > lesson65/av.log 2>&1
python3 common/overlay_term.py lesson65 > lesson65/ov.log 2>&1
echo done > lesson65/ALLDONE
