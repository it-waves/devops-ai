cd /home/claude/academy
for s in hook plan maven live task labinfo rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson114 scene {} > lesson114/build_{}.log 2>&1'
python3 common/pipe.py lesson114 av > lesson114/av.log 2>&1
python3 common/overlay_term.py lesson114 > lesson114/ov.log 2>&1
echo done > lesson114/ALLDONE
