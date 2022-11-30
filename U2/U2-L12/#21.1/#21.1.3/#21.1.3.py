file = open("#21.1.3file", "r")
a = file.readlines()
for items in a:
    if items[0] == "#":
        continue
    print(items, end="")
file.close()  # 这一步差点就忘记了hhhh

