import requests

def running(servers):
    return [s["name"] for s in servers if s["state"] == "running"]

def health(url):
    r = requests.get(url, timeout=2)
    r.raise_for_status()
    return r.json()["status"]
