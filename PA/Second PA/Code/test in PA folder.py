with open("../Course/all course") as f:
    a = f.readlines()
    for i, items in enumerate(a):
        a[i] = items.rstrip("\n").split(" | ")
    for items in a:
        for i in items:
            print(i.ljust(15), end="\t")
        print("\n")

