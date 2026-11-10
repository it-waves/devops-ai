#!/bin/sh
cd /home/claude/academy
B=lesson18/build
L="hook ports servicedemo tcpudp handshake states statedemo udpdemo socket conflictdemo errors myths rubric yourturn recap"
for s in $L; do rm -f $B/$s.mp4 $B/${s}_base.mp4; done
( echo $L | tr ' ' '\0' | xargs -0 -P3 -I{} sh -c "python3 common/pipe.py lesson18 scene {} > $B/{}.log 2>&1" )
python3 common/pipe.py lesson18 info > /dev/null
python3 common/overlay_term.py lesson18 > /tmp/ov18.log 2>&1
python3 common/pipe.py lesson18 av && sh /home/claude/rhcsa/mux2.sh $B final.mp4 && echo "l18 done" > /tmp/l18.txt
