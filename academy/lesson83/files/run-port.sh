#!/bin/sh
cd "$(dirname "$0")"
java -cp port/classes cloudcart.Server 18083 &
FIRST=$!
sleep 1
java -cp port/classes cloudcart.Server 18083 || exit 1
wait $FIRST
