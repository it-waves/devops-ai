#!/bin/sh
# post a message to the team chat webhook
curl -s -o /dev/null -X POST -H 'Content-Type: application/json' -d "{\"text\":\"$1\"}" http://localhost:9300/hook
