correspond_dict = {}
for i in range(0, 26):
    correspond_dict[chr(65 + i)] = i + 1
print(correspond_dict)


def return_excel(columnNumber):
    a = ""
    a += correspond_dict([(return_excel(columnNumber) - 1) % 26])
    return a

print(return_excel(26))