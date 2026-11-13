cd /home/claude/academy
for s in clients verbose headers timing exit trace; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson69 scene {} > lesson69/build_{}.log 2>&1'
python3 common/pipe.py lesson69 av > lesson69/av.log 2>&1
python3 common/overlay_term.py lesson69 > lesson69/ov.log 2>&1
echo done > lesson69/ALLDONE
