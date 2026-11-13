cd /home/claude/academy
for s in hook map models task rubric yourturn recap tools compile bytecode process; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson76 scene {} > lesson76/build_{}.log 2>&1'
python3 common/pipe.py lesson76 av > lesson76/av.log 2>&1
python3 common/overlay_term.py lesson76 > lesson76/ov.log 2>&1
echo done > lesson76/ALLDONE
