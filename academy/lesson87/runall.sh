cd /home/claude/academy
for s in hook plug props prof task rubric yourturn recap cfg repro; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson87 scene {} > lesson87/build_{}.log 2>&1'
python3 common/pipe.py lesson87 av > lesson87/av.log 2>&1
python3 common/overlay_term.py lesson87 > lesson87/ov.log 2>&1
echo done > lesson87/ALLDONE
