#!/bin/sh
cd /home/claude/academy
rm -f /tmp/l7.txt
( cat lesson07/build/order.txt | tr '\n' '\0' | xargs -0 -P2 -I{} sh -c "rm -f lesson07/build/{}.mp4; python3 common/pipe.py lesson07 scene {} > lesson07/build/{}.log 2>&1" )
python3 common/pipe.py lesson07 av && sh /home/claude/rhcsa/mux2.sh lesson07/build final.mp4 && echo "l7 done" >> /tmp/l7.txt
