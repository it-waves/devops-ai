cd /home/claude/academy
for s in hook control journal boot cron myths rubric yourturn recap unit mine timers; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson31 scene {} > lesson31/build_{}.log 2>&1'
python3 common/pipe.py lesson31 av > lesson31/av.log 2>&1
python3 common/overlay_term.py lesson31 > lesson31/ov.log 2>&1
echo done > lesson31/ALLDONE
