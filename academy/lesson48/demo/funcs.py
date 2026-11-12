def busy(servers, limit):
    names = []
    for name, cpu in servers:
        if cpu > limit:
            names.append(name)
    return names


if __name__ == "__main__":
    data = [("web1", 72), ("web2", 91), ("db1", 55)]
    print(busy(data, 80))
