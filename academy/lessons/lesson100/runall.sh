cd /home/claude/academy
for s in hook parts live ui task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson100 scene {} > lesson100/build_{}.log 2>&1'
python3 common/pipe.py lesson100 av > lesson100/av.log 2>&1
python3 common/overlay_term.py lesson100 > lesson100/ov.log 2>&1
echo done > lesson100/ALLDONE
