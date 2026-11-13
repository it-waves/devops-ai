cd /home/claude/academy
for s in hook ideas bind flags task rubric yourturn recap life fail; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson86 scene {} > lesson86/build_{}.log 2>&1'
python3 common/pipe.py lesson86 av > lesson86/av.log 2>&1
python3 common/overlay_term.py lesson86 > lesson86/ov.log 2>&1
echo done > lesson86/ALLDONE
