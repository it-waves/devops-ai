#!/bin/sh
cd /home/claude/academy
B=lesson23/build
L="hook bound bdemo ctrs ctrdemo pub pubdemo cloud awsA awsB errors myths rubric yourturn recap"
for s in $L; do rm -f $B/$s.mp4 $B/${s}_base.mp4; done
( echo $L | tr ' ' '\0' | xargs -0 -P3 -I{} sh -c "python3 common/pipe.py lesson23 scene {} > $B/{}.log 2>&1" )
python3 common/pipe.py lesson23 info > /dev/null
python3 common/overlay_term.py lesson23 > /tmp/ov22.log 2>&1
python3 common/pipe.py lesson23 av && sh /home/claude/rhcsa/mux2.sh $B final.mp4 && echo "l23 done" > /tmp/l23.txt
