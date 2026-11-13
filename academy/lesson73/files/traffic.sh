#!/bin/sh
# usage: ./traffic.sh   pretends to be five customers (one asks for a missing product, one arrives during a database outage)
for i in 1 2 3; do curl -s -o /dev/null localhost:5000/api/products; done
curl -s -o /dev/null localhost:5000/api/products/99
mv shop.db shop.db.off; curl -s -o /dev/null localhost:5000/api/products; mv shop.db.off shop.db
echo "sent 5 requests"
