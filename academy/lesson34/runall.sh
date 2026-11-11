cd /home/claude/academy
for s in hook habits myths rubric yourturn recap net ssh harden fw; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson34 scene {} > lesson34/build_{}.log 2>&1'
python3 common/pipe.py lesson34 av > lesson34/av.log 2>&1
python3 common/overlay_term.py lesson34 > lesson34/ov.log 2>&1
echo done > lesson34/ALLDONE
