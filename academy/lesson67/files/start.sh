#!/bin/sh
# usage: ./start.sh mono | split
./stop.sh
case "$1" in
  mono)  python3 app.py & echo "monolith started" ;;
  split) python3 api.py & python3 web.py & echo "api and web started" ;;
  *) echo "usage: ./start.sh mono|split" ;;
esac
sleep 1
