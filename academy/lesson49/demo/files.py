with open("notes.txt", "w") as f:
    f.write("web1 ok\n")

with open("notes.txt", "a") as f:
    f.write("web2 busy\n")

with open("notes.txt") as f:
    for line in f:
        print(line.strip())
