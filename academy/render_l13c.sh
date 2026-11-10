#!/bin/sh
cd /home/claude/academy
rm -f /tmp/l13.txt
B=lesson13/build
L="installer bootvm login walk notes snap snapvb snaphost boot2 breakit resthost boot3 verify yourturn"
for s in $L; do rm -f $B/$s.mp4 $B/${s}_base.mp4; done
( echo $L | tr ' ' '\0' | xargs -0 -P2 -I{} sh -c "python3 common/pipe.py lesson13 scene {} > $B/{}.log 2>&1" )
python3 common/overlay_all.py > /tmp/ov.log 2>&1
python3 common/pipe.py lesson13 av && sh /home/claude/rhcsa/mux2.sh $B final.mp4 && echo "l13 done" >> /tmp/l13.txt
