#!/usr/bin/env python3
"""Flag wildcard Action or Resource in an IAM policy file."""
import json, sys

def audit(policy):
    problems = []
    for i, st in enumerate(policy["Statement"], 1):
        if st["Effect"] != "Allow":
            continue
        for key in ("Action", "Resource"):
            vals = st[key] if isinstance(st[key], list) else [st[key]]
            for v in vals:
                if v == "*" or v.endswith(":*") and key == "Action":
                    problems.append(f"statement {i}: {key} is {v}")
    return problems

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        found = audit(json.load(f))
    for p in found:
        print("BAD", p)
    if not found:
        print("OK  no wildcards, least privilege")
    sys.exit(1 if found else 0)
