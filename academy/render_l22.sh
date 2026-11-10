#!/bin/sh
cd /home/claude/academy
B=lesson22/build
L="hook routing routedemo nat natdemo firewall fwdemo proxy lbdemo errors myths rubric yourturn recap"
for s in $L; do rm -f $B/$s.mp4 $B/${s}_base.mp4; done
( echo $L | tr ' ' '\0' | xargs -0 -P3 -I{} sh -c "python3 common/pipe.py lesson22 scene {} > $B/{}.log 2>&1" )
python3 common/pipe.py lesson22 info > /dev/null
python3 common/overlay_term.py lesson22 > /tmp/ov22.log 2>&1
python3 common/pipe.py lesson22 av && sh /home/claude/rhcsa/mux2.sh $B final.mp4 && echo "l22 done" > /tmp/l22.txt
