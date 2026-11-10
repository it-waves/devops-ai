#!/bin/sh
cd /home/claude/academy
rm -f /tmp/l13.txt
( cat lesson13/build/order.txt | tr '\n' '\0' | xargs -0 -P2 -I{} sh -c "rm -f lesson13/build/{}.mp4; python3 common/pipe.py lesson13 scene {} > lesson13/build/{}.log 2>&1" )
python3 common/overlay_vbox.py > /tmp/ov.log 2>&1
python3 common/pipe.py lesson13 av && sh /home/claude/rhcsa/mux2.sh lesson13/build final.mp4 && echo "l13 done" >> /tmp/l13.txt
