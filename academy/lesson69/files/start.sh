#!/bin/sh
# usage: ./start.sh   (starts the backend on 5000 and the frontend on 8080)
./stop.sh
python3 api.py & python3 web.py &
echo "api and web started"
sleep 1
