cd /home/claude/academy
for s in hook ideas models task rubric yourturn recap inspect settings; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson79 scene {} > lesson79/build_{}.log 2>&1'
python3 common/pipe.py lesson79 av > lesson79/av.log 2>&1
python3 common/overlay_term.py lesson79 > lesson79/ov.log 2>&1
echo done > lesson79/ALLDONE
