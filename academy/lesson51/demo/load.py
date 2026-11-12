import json
try:
    with open("settings.json") as f:
        cfg = json.load(f)
except FileNotFoundError:
    print("settings.json not found, using defaults")
    cfg = {"retries": 3}
except json.JSONDecodeError as e:
    print("bad JSON:", e.msg)
    cfg = {"retries": 3}
else:
    print("loaded settings")
finally:
    print("done")
print("retries =", cfg["retries"])
