import os
import requests

URL = "http://127.0.0.1:8081/servers"
H = {"Authorization": "Bearer " + os.environ["API_TOKEN"]}
page, names = 1, []
while page:
    r = requests.get(URL, headers=H, params={"page": page}, timeout=5)
    r.raise_for_status()
    data = r.json()
    names += [s["name"] for s in data["items"]]
    page = data["next_page"]
print(len(names), "servers, first:", names[0])
