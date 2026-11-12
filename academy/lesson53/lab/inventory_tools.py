import requests


def count_by_env(servers):
    counts = {}
    for s in servers:
        env = s["env"]
        counts[env] = counts.get(env, 0) + 1
    return counts


def api_status(url):
    r = requests.get(url, timeout=2)
    r.raise_for_status()
    return r.json()["status"]
