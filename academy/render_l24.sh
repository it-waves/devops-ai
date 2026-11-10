#!/bin/sh
cd /home/claude/academy
B=lesson24/build
L="hook method dns port fw tls route table myths rubric yourturn recap"
for s in $L; do rm -f $B/$s.mp4 $B/${s}_base.mp4; done
( echo $L | tr ' ' '\0' | xargs -0 -P3 -I{} sh -c "python3 common/pipe.py lesson24 scene {} > $B/{}.log 2>&1" )
python3 common/pipe.py lesson24 info > /dev/null
python3 common/overlay_term.py lesson24 > /tmp/ov24.log 2>&1
python3 common/pipe.py lesson24 av && sh /home/claude/rhcsa/mux2.sh $B final.mp4 && echo "l24 done" > /tmp/l24.txt
