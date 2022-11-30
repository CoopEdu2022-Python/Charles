file = open("#21.1.4file", "r")
a = list(map(int, file.readline()))
output_list = []
for i, items in enumerate(a):
    if items == 1 and a[i + 1] == 0:
        output_list.append(int(str(items) + str(a[i + 1])))
    else:
        output_list.append(items)
# print(a)
# print(output_list)
output_list.sort()
for items in output_list:
    print(items, end="\n")
