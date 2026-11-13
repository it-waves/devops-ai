cd /home/claude/academy
for s in hook ideas models task rubric yourturn recap vermem portcp; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson83 scene {} > lesson83/build_{}.log 2>&1'
python3 common/pipe.py lesson83 av > lesson83/av.log 2>&1
python3 common/overlay_term.py lesson83 > lesson83/ov.log 2>&1
echo done > lesson83/ALLDONE
