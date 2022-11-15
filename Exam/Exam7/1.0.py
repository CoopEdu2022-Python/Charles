def gcd_pro_max_1(*n: int) -> int:
    n = list(n)
    while 1:
        new_list = list()
        n.sort(reverse=True)
        for i in range(len(n)):
            if i + 1 >= len(n):
                new_list.append(n[i])
                break
            if n[i] % n[i + 1] == 0:
                new_list.append(n[i + 1])
            else:
                new_list.append(n[i] % n[i + 1])
        n = new_list
        if n.count(n[0]) == len(n):
            return n[0]


print(gcd_pro_max_1(1, 2, 3, 4, 5))
print(gcd_pro_max_1(2, 4, 6, 8, 10))
print(gcd_pro_max_1(999, 1999, 2999, 3999, 4999))


