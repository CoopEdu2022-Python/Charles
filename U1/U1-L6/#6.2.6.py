correspond_dict = {}
for i in range(0, 26):
    correspond_dict[i] = chr(65 + i)
# print(correspond_dict)


def return_excel(columnNumber):
    a = ""
    b = -1
    while 1:
        if columnNumber == 0:
            break
        if b != (columnNumber - 1) % 26 or columnNumber >= 26:
            b = (columnNumber - 1) % 26
            a += correspond_dict[(columnNumber - 1) % 26]
        elif (columnNumber - 1) == (columnNumber - 1) % 26 or (columnNumber - 1) % 26 == 0:
            a += correspond_dict[(columnNumber - 1) % 26]
            break
        columnNumber = (columnNumber - 1) // 26
    return a[::-1]


print(return_excel(92834))
