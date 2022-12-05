def find_lus_length(a: str, b: str) -> int:
    if a == b:
        return -1
    elif len(a) < len(b):
        return len(b)
    else:
        return len(a)


fin = open("2.1_test.txt", "r")
a = fin.readlines()
# print(a)
b = []
for i, items in enumerate(a):
    a[i] = items.rstrip("\n")
    b.append(a[i].split(' '))
c = []
for items in b:
    c.append(items[0])
    c.append(items[1])
d = []
for i, items in enumerate(b):
    temp = []
    temp.append(items[0])
    temp.append(items[1])
    temp.append(str(find_lus_length(items[0], items[1])))
    d.append(temp)
print(b)
print(d)
if d == b:
    print("nice")
fin.close()
