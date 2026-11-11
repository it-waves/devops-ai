cd /home/claude/academy
for s in hook myths rubric yourturn recap if tests case loops func build; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson39 scene {} > lesson39/build_{}.log 2>&1'
python3 common/pipe.py lesson39 av > lesson39/av.log 2>&1
python3 common/overlay_term.py lesson39 > lesson39/ov.log 2>&1
echo done > lesson39/ALLDONE
