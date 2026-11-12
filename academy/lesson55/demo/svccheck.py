#!/usr/bin/env python3
import json, sys

def validate(items):
    errs, seen = [], set()
    for i, s in enumerate(items):
        n = s.get("name")
        if not n:
            errs.append(f"#{i}: name missing")
        elif n in seen:
            errs.append(f"{n}: duplicate")
        seen.add(n)
        p = s.get("port")
        if not isinstance(p, int) or not 1 <= p <= 65535:
            errs.append(f"{n}: bad port {p}")
        if s.get("proto") not in ("tcp", "udp"):
            errs.append(f"{n}: bad proto {s.get('proto')}")
    return errs

def main(argv):
    try:
        with open(argv[1]) as f:
            items = json.load(f)
    except (OSError, ValueError):
        print(f"cannot read {argv[1]}", file=sys.stderr)
        return 2
    errs = validate(items)
    for e in errs:
        print(e)
    if errs:
        print(f"FAIL: {len(errs)} problems in {argv[1]}")
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
