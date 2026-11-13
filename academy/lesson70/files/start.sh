#!/bin/sh
# usage: ./start.sh   (loads secrets.env into the environment, then starts the API on 5000)
./stop.sh
set -a; . ./secrets.env; set +a
python3 api.py & python3 web.py &
echo "api and web started"
sleep 1
