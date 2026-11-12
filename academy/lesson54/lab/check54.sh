#!/bin/bash
# Lesson 54 checker: bash check54.sh [FOLDER]   (folder holds your policy.json and s3tools.py; needs boto3 and moto in your venv)
d=${1:-.}; cd "$d" || exit 2
fails=0
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fails=$((fails+1)); fi; }
pol() { python3 - "$1" <<'PY'
import json, sys
try:
    p = json.load(open("policy.json")); st = p["Statement"]
    if isinstance(st, dict): st = [st]
    acts = []; res = []
    for s in st:
        assert s["Effect"] == "Allow"
        a = s["Action"]; r = s["Resource"]
        acts += a if isinstance(a, list) else [a]; res += r if isinstance(r, list) else [r]
    mode = sys.argv[1]
    if mode == "valid": ok = len(st) >= 1
    elif mode == "nowild": ok = all(a != "*" and not a.endswith(":*") for a in acts) and len(acts) >= 1
    elif mode == "res": ok = set(res) == {"arn:aws:s3:::devops-lab", "arn:aws:s3:::devops-lab/*"}
    elif mode == "readonly": ok = set(acts) == {"s3:ListBucket", "s3:GetObject"}
    sys.exit(0 if ok else 1)
except Exception:
    sys.exit(1)
PY
}
code() { python3 - "$1" <<'PY'
import sys, boto3
from moto import mock_aws
mode = sys.argv[1]
try:
    import s3tools
    with mock_aws():
        s3 = boto3.client("s3", region_name="us-east-1"); s3.create_bucket(Bucket="devops-lab")
        if mode == "empty":
            ok = s3tools.big_files(s3, "devops-lab", 1) == []
        else:
            for i in range(1005):
                s3.put_object(Bucket="devops-lab", Key=f"k{i:04d}", Body=b"x" * (10 if i % 5 else 200))
            got = s3tools.big_files(s3, "devops-lab", 200)
            want = sorted(f"k{i:04d}" for i in range(1005) if i % 5 == 0)
            ok = got == want and len(got) == 201
    sys.exit(0 if ok else 1)
except Exception:
    sys.exit(1)
PY
}
chk "policy.json is valid JSON with Allow statements" "pol valid"
chk "no wildcard in any Action" "pol nowild"
chk "Resource names only the devops-lab bucket and its objects" "pol res"
chk "read-only: only s3:ListBucket and s3:GetObject" "pol readonly"
chk "big_files returns the right keys across more than 1000 objects" "code many"
chk "big_files returns an empty list for an empty bucket" "code empty"
exit $((fails>0))
