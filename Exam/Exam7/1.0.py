def gcd_pro_max_1(*n: int) -> int:
    n = list(n)
    n.sort(reverse=True)
    while 1:
        new_list = list()
        for i in range(len(n)):
            if i + 1 >= len(n):
                break
            if n[i] % n[i + 1] == 0:
                new_list.append(n[i])
            else:
                new_list.append(n[i] % n[i + 1])
        n = new_list
        if n.count(n[0]) == len(n):
            return n[0]


print(gcd_pro_max_1(999, 1999, 2999, 3999, 4999))


