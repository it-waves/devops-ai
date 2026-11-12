#!/usr/bin/env python3
import argparse, socket, sys
def main():
    p = argparse.ArgumentParser(description="Check a TCP port.")
    p.add_argument("host", help="name or address")
    p.add_argument("port", type=int, help="TCP port number")
    p.add_argument("-q", "--quiet", action="store_true", help="mute")
    a = p.parse_args()
    try:
        socket.create_connection((a.host, a.port), 2).close()
    except OSError as e:
        if not a.quiet: print("CLOSED", e.strerror, file=sys.stderr)
        return 1
    if not a.quiet: print("OPEN", a.host, a.port)
    return 0
sys.exit(main())
