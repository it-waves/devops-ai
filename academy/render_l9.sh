#!/bin/sh
cd /home/claude/academy
rm -f /tmp/l9.txt
( cat lesson09/build/order.txt | tr '\n' '\0' | xargs -0 -P2 -I{} sh -c "rm -f lesson09/build/{}.mp4; python3 common/pipe.py lesson09 scene {} > lesson09/build/{}.log 2>&1" )
python3 common/pipe.py lesson09 av && sh /home/claude/rhcsa/mux2.sh lesson09/build final.mp4 && echo "l9 done" >> /tmp/l9.txt
