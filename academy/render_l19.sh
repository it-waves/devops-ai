#!/bin/sh
cd /home/claude/academy
B=lesson19/build
L="hook request methods methoddemo status statusdemo headers https certs tlsdemo errors myths rubric yourturn recap"
for s in $L; do rm -f $B/$s.mp4 $B/${s}_base.mp4; done
( echo $L | tr ' ' '\0' | xargs -0 -P3 -I{} sh -c "python3 common/pipe.py lesson19 scene {} > $B/{}.log 2>&1" )
python3 common/pipe.py lesson19 info > /dev/null
python3 common/overlay_term.py lesson19 > /tmp/ov19.log 2>&1
python3 common/pipe.py lesson19 av && sh /home/claude/rhcsa/mux2.sh $B final.mp4 && echo "l19 done" > /tmp/l19.txt
