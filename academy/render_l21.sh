#!/bin/sh
cd /home/claude/academy
B=lesson21/build
L="hook ladder ipdemo pingdemo tracedemo ssdemo diagdemo errors myths rubric yourturn recap"
for s in $L; do rm -f $B/$s.mp4 $B/${s}_base.mp4; done
( echo $L | tr ' ' '\0' | xargs -0 -P3 -I{} sh -c "python3 common/pipe.py lesson21 scene {} > $B/{}.log 2>&1" )
python3 common/pipe.py lesson21 info > /dev/null
python3 common/overlay_term.py lesson21 > /tmp/ov21.log 2>&1
python3 common/pipe.py lesson21 av && sh /home/claude/rhcsa/mux2.sh $B final.mp4 && echo "l21 done" > /tmp/l21.txt
