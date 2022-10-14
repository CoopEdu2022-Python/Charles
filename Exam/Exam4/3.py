def reverse(n, str="123456789"):
    a = len(str) // n
    b = ""
    temp = []
    i = 0
    while i < (a + 1):
        for x in range(i * n, (i + 1) * n):
            if x > len(str)-1:
                break
            temp.insert(i * n, str[x])
        i += 1
    for items in temp:
        b += items
    return b


print(reverse(int(input("Enter the length: ")), input("Enter only lower words: ")))









