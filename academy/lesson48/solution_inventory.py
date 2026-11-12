from data48 import SERVERS


def busy(servers, limit):
    names = []
    for server in servers:
        if server["cpu"] > limit:
            names.append(server["name"])
    return names


def count_by_env(servers):
    counts = {}
    for server in servers:
        env = server["env"]
        counts[env] = counts.get(env, 0) + 1
    return counts


if __name__ == "__main__":
    print("servers:", len(SERVERS))
    counts = count_by_env(SERVERS)
    print("by env:", " ".join(f"{env}={counts[env]}" for env in sorted(counts)))
    print("busy (cpu > 80):", ", ".join(busy(SERVERS, 80)))
    print("average cpu:", sum(s["cpu"] for s in SERVERS) / len(SERVERS))
