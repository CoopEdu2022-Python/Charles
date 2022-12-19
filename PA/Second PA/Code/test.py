id_number = "s_007"
with open("../Students/%s" % id_number, "r") as f:
    a = f.readline()
    c = a.split(" | ")
    print(c)
    for items in c:
        if items[0] == id_number:
            user = items
with open("../Students/format", "r") as f:
    b = f.read()
    print(b, a, sep="\n")