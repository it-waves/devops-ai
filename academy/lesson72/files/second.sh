#!/bin/sh
# usage: ./second.sh   (starts a second copy of the API on port 5001; settings come from your environment)
set -a; . ./secrets.env; set +a
PORT=5001 python3 api.py &
echo "second api started on 5001"
sleep 1
