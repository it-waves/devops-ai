cd /home/claude/academy
for s in hook skills live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson94 scene {} > lesson94/build_{}.log 2>&1'
python3 common/pipe.py lesson94 av > lesson94/av.log 2>&1
python3 common/overlay_term.py lesson94 > lesson94/ov.log 2>&1
echo done > lesson94/ALLDONE
