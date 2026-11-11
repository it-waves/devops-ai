cd /home/claude/academy
for s in hook myths rubric yourturn recap secrets perms validate inject build; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson43 scene {} > lesson43/build_{}.log 2>&1'
python3 common/pipe.py lesson43 av > lesson43/av.log 2>&1
python3 common/overlay_term.py lesson43 > lesson43/ov.log 2>&1
echo done > lesson43/ALLDONE
