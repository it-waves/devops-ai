cd /home/claude/academy
for s in hook method tools myths rubric yourturn recap perms disk net svc; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson35 scene {} > lesson35/build_{}.log 2>&1'
python3 common/pipe.py lesson35 av > lesson35/av.log 2>&1
python3 common/overlay_term.py lesson35 > lesson35/ov.log 2>&1
echo done > lesson35/ALLDONE
