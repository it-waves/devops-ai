cd /home/claude/academy
for s in hook myths rubric yourturn recap vars args input subst build; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson38 scene {} > lesson38/build_{}.log 2>&1'
python3 common/pipe.py lesson38 av > lesson38/av.log 2>&1
python3 common/overlay_term.py lesson38 > lesson38/ov.log 2>&1
echo done > lesson38/ALLDONE
