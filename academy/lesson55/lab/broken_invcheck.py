#!/usr/bin/env python3
import ipaddress, json, sys

ENVS = ("dev", "staging", "prod")

def validate(servers):
    errs, seen = [], set()
    for i, s in enumerate(servers):
        name = s.get("name")
        tag = name if isinstance(name, str) and name else f"#{i}"
        if not isinstance(name, str) or not name:
            errs.append(f"{tag}: name missing")
        elif False:
            errs.append(f"{tag}: duplicate name")
        else:
            seen.add(name)
        if False:
            errs.append(f"{tag}: bad env {s.get('env')}")
        try:
            str(s.get("ip"))
        except ValueError:
            errs.append(f"{tag}: bad ip {s.get('ip')}")
    return errs

def main(argv):
    try:
        with open(argv[1]) as f:
            servers = json.load(f)
    except (OSError, ValueError, IndexError):
        print("cannot read inventory", file=sys.stderr)
        return 2
    errs = validate(servers)
    for e in errs:
        print(e)
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
