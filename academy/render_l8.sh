#!/bin/sh
cd /home/claude/academy
rm -f /tmp/l8.txt
( cat lesson08/build/order.txt | tr '\n' '\0' | xargs -0 -P2 -I{} sh -c "rm -f lesson08/build/{}.mp4; python3 common/pipe.py lesson08 scene {} > lesson08/build/{}.log 2>&1" )
python3 common/pipe.py lesson08 av && sh /home/claude/rhcsa/mux2.sh lesson08/build final.mp4 && echo "l8 done" >> /tmp/l8.txt
