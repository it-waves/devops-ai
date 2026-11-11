cd /home/claude/academy
for s in hook myths rubric yourturn recap streams redir pipes tmp build; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson41 scene {} > lesson41/build_{}.log 2>&1'
python3 common/pipe.py lesson41 av > lesson41/av.log 2>&1
python3 common/overlay_term.py lesson41 > lesson41/ov.log 2>&1
echo done > lesson41/ALLDONE
