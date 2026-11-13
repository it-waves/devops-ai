cd /home/claude/academy
for s in hook ideas models task rubric yourturn recap jar war; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson80 scene {} > lesson80/build_{}.log 2>&1'
python3 common/pipe.py lesson80 av > lesson80/av.log 2>&1
python3 common/overlay_term.py lesson80 > lesson80/ov.log 2>&1
echo done > lesson80/ALLDONE
