servers = [("web1", 72), ("web2", 91), ("db1", 55)]
for name, cpu in servers:
    if cpu > 80:
        print(name, "is busy")
    else:
        print(name, "ok")
