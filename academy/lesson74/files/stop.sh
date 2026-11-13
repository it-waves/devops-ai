#!/bin/sh
pkill -f "python3 (app|api|web).py" 2>/dev/null; sleep 0.5; exit 0
