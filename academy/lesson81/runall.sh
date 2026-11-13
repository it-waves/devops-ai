cd /home/claude/academy
for s in hook ideas models task rubric yourturn recap trace logs; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson81 scene {} > lesson81/build_{}.log 2>&1'
python3 common/pipe.py lesson81 av > lesson81/av.log 2>&1
python3 common/overlay_term.py lesson81 > lesson81/ov.log 2>&1
echo done > lesson81/ALLDONE
