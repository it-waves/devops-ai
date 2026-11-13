cd /home/claude/academy
for s in hook anatomy json rest browser task rubric yourturn recap get status write; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson68 scene {} > lesson68/build_{}.log 2>&1'
python3 common/pipe.py lesson68 av > lesson68/av.log 2>&1
python3 common/overlay_term.py lesson68 > lesson68/ov.log 2>&1
echo done > lesson68/ALLDONE
