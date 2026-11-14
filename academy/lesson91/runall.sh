cd /home/claude/academy
for s in hook what rule deploy task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson91 scene {} > lesson91/build_{}.log 2>&1'
python3 common/pipe.py lesson91 av > lesson91/av.log 2>&1
python3 common/overlay_term.py lesson91 > lesson91/ov.log 2>&1
echo done > lesson91/ALLDONE
