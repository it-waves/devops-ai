#!/bin/sh
cd /home/claude/academy
B=lesson20/build
L="hook names hierarchy records resolver digdemo journey e2edemo tools errors myths rubric yourturn recap"
for s in $L; do rm -f $B/$s.mp4 $B/${s}_base.mp4; done
( echo $L | tr ' ' '\0' | xargs -0 -P3 -I{} sh -c "python3 common/pipe.py lesson20 scene {} > $B/{}.log 2>&1" )
python3 common/pipe.py lesson20 info > /dev/null
python3 common/overlay_term.py lesson20 > /tmp/ov20.log 2>&1
python3 common/pipe.py lesson20 av && sh /home/claude/rhcsa/mux2.sh $B final.mp4 && echo "l20 done" > /tmp/l20.txt
