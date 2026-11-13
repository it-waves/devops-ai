cd /home/claude/academy
for s in hook authn access secrets models task rubric yourturn recap; do echo $s; done | xargs -P 3 -I{} sh -c 'python3 common/pipe.py lesson70 scene {} > lesson70/build_{}.log 2>&1'
python3 common/pipe.py lesson70 av > lesson70/av.log 2>&1
python3 common/overlay_term.py lesson70 > lesson70/ov.log 2>&1
echo done > lesson70/ALLDONE
