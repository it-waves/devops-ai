#!/bin/sh
cd /home/claude/academy
B=lesson17/build
L="hook address ipdemo private privdemo cidr cidrdemo gateway gwdemo four errors myths rubric yourturn recap"
for s in $L; do rm -f $B/$s.mp4 $B/${s}_base.mp4; done
( echo $L | tr ' ' '\0' | xargs -0 -P3 -I{} sh -c "python3 common/pipe.py lesson17 scene {} > $B/{}.log 2>&1" )
python3 common/pipe.py lesson17 info > /dev/null
python3 common/overlay_term.py lesson17 > /tmp/ov17.log 2>&1
python3 common/pipe.py lesson17 av && sh /home/claude/rhcsa/mux2.sh $B final.mp4 && echo "l17 done" > /tmp/l17.txt
