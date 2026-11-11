cd /home/claude/academy
for s in hook fstab myths rubric yourturn recap see make mount full grow; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson33 scene {} > lesson33/build_{}.log 2>&1'
python3 common/pipe.py lesson33 av > lesson33/av.log 2>&1
python3 common/overlay_term.py lesson33 > lesson33/ov.log 2>&1
echo done > lesson33/ALLDONE
