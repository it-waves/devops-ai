cd /home/claude/academy
for s in hook ideas models task rubric yourturn recap tests outputs; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson82 scene {} > lesson82/build_{}.log 2>&1'
python3 common/pipe.py lesson82 av > lesson82/av.log 2>&1
python3 common/overlay_term.py lesson82 > lesson82/ov.log 2>&1
echo done > lesson82/ALLDONE
