#!/bin/sh
cd /home/claude/academy
rm -f /tmp/l10.txt
( cat lesson10/build/order.txt | tr '\n' '\0' | xargs -0 -P2 -I{} sh -c "rm -f lesson10/build/{}.mp4; python3 common/pipe.py lesson10 scene {} > lesson10/build/{}.log 2>&1" )
python3 common/pipe.py lesson10 av && sh /home/claude/rhcsa/mux2.sh lesson10/build final.mp4 && echo "l10 done" >> /tmp/l10.txt
