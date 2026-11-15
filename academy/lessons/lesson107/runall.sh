cd /home/claude/academy
for s in hook plan live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson107 scene {} > lesson107/build_{}.log 2>&1'
python3 common/pipe.py lesson107 av > lesson107/av.log 2>&1
python3 common/overlay_term.py lesson107 > lesson107/ov.log 2>&1
echo done > lesson107/ALLDONE
