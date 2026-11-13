#!/bin/sh
cd "$(dirname "$0")"
java -Xmx16m -cp mem/classes cloudcart.Hog
