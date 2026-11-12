cd /home/claude/academy
for s in hook myths rubric yourturn recap layout script deploy rollback; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson45 scene {} > lesson45/build_{}.log 2>&1'
python3 common/pipe.py lesson45 av > lesson45/av.log 2>&1
python3 common/overlay_term.py lesson45 > lesson45/ov.log 2>&1
echo done > lesson45/ALLDONE
