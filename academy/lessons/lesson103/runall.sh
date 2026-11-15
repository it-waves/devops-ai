cd /home/claude/academy
for s in hook scenario live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson103 scene {} > lesson103/build_{}.log 2>&1'
python3 common/pipe.py lesson103 av > lesson103/av.log 2>&1
python3 common/overlay_term.py lesson103 > lesson103/ov.log 2>&1
echo done > lesson103/ALLDONE
