#!/usr/bin/env python3
import argparse
import sys

import requests


def main():
    p = argparse.ArgumentParser(description="Check that a URL answers 200.")
    p.add_argument("url")
    p.add_argument("-t", "--timeout", type=float, default=2.0, help="seconds to wait")
    p.add_argument("-q", "--quiet", action="store_true", help="print nothing")
    a = p.parse_args()
    try:
        r = requests.get(a.url, timeout=a.timeout)
        r.raise_for_status()
    except requests.RequestException as e:
        if not a.quiet:
            print(f"DOWN {a.url} ({type(e).__name__})", file=sys.stderr)
        return 1
    if not a.quiet:
        print(f"UP {a.url} {r.status_code}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
