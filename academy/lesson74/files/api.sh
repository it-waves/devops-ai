#!/bin/sh
# usage: ./api.sh stop | start   controls only the API, so you can see what each layer does alone
case "$1" in
  stop) pkill -f "python3 api.py" 2>/dev/null; sleep 0.5; echo "api stopped";;
  start) set -a; . ./secrets.env; set +a; python3 api.py > /dev/null 2>&1 & sleep 1; echo "api started";;
  *) echo "usage: ./api.sh stop|start";;
esac
