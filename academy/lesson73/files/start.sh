#!/bin/sh
# usage: ./start.sh   (loads secrets.env, then starts the API; settings come from app.conf and your environment)
./stop.sh
set -a; . ./secrets.env; set +a
python3 api.py & python3 web.py &
echo "api and web started"
sleep 1
