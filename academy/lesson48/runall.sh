cd /home/claude/academy
for s in hook why task rubric yourturn recap repl coll script func mod; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson48 scene {} > lesson48/build_{}.log 2>&1'
python3 common/pipe.py lesson48 av > lesson48/av.log 2>&1
python3 common/overlay_term.py lesson48 > lesson48/ov.log 2>&1
echo done > lesson48/ALLDONE
