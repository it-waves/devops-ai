import os
import sys

import requests

BASE = os.getenv("API_URL", "http://127.0.0.1:8081")
TOKEN = os.getenv("API_TOKEN")
if not TOKEN:
    sys.exit("API_TOKEN is not set")
headers = {"Authorization": "Bearer " + TOKEN}

servers = []
page = 1
while page:
    r = requests.get(BASE + "/servers", headers=headers, params={"page": page}, timeout=5)
    r.raise_for_status()
    data = r.json()
    servers += data["items"]
    page = data["next_page"]

stopped = [s["name"] for s in servers if s["state"] == "stopped"]
print("servers:", len(servers))
print("stopped:", ", ".join(stopped))
