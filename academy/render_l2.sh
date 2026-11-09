#!/bin/sh
cd /home/claude/academy
rm -f /tmp/l2.txt
( cat lesson02/build/order.txt | tr '\n' '\0' | xargs -0 -P2 -I{} sh -c "rm -f lesson02/build/{}.mp4; python3 common/pipe.py lesson02 scene {} > lesson02/build/{}.log 2>&1" )
python3 common/pipe.py lesson02 av && sh /home/claude/rhcsa/mux2.sh lesson02/build final.mp4 && echo "l2 done" >> /tmp/l2.txt
