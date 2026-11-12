import csv
import json
import os

import yaml

with open("config49.yaml") as f:
    cfg = yaml.safe_load(f)
with open("servers49.csv") as f:
    rows = list(csv.DictReader(f))

busy = [r["name"] for r in rows if int(r["cpu"]) > cfg["limit"]]
out = {"env": os.getenv("APP_ENV", "dev"), "limit": cfg["limit"], "count": len(rows), "busy": busy}
with open("report.json", "w") as f:
    json.dump(out, f, indent=2)
print("wrote report.json")
