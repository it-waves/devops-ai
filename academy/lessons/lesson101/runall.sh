cd /home/claude/academy
for s in hook parts live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson101 scene {} > lesson101/build_{}.log 2>&1'
python3 common/pipe.py lesson101 av > lesson101/av.log 2>&1
python3 common/overlay_term.py lesson101 > lesson101/ov.log 2>&1
echo done > lesson101/ALLDONE
