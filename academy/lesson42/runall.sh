cd /home/claude/academy
for s in hook myths rubric yourturn recap exitcodes strict trap logging build; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson42 scene {} > lesson42/build_{}.log 2>&1'
python3 common/pipe.py lesson42 av > lesson42/av.log 2>&1
python3 common/overlay_term.py lesson42 > lesson42/ov.log 2>&1
echo done > lesson42/ALLDONE
