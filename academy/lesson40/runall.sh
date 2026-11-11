cd /home/claude/academy
for s in hook myths rubric yourturn recap grep cutsort sed awk find build; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson40 scene {} > lesson40/build_{}.log 2>&1'
python3 common/pipe.py lesson40 av > lesson40/av.log 2>&1
python3 common/overlay_term.py lesson40 > lesson40/ov.log 2>&1
echo done > lesson40/ALLDONE
