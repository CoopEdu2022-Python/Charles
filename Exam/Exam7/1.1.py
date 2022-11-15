def gcd_pro_max_2(* n: int) -> int:
    if len(set(n)) == 1:
        return set(n).pop()
    n = sorted(n, reverse=True)
    for i in range(len(n)-1):
        if n[i] % n[i + 1] == 0:
            n[i] = n[i + 1]
        else:
            n[i] = n[i] % n[i + 1]

    return gcd_pro_max_2(* n)


print(gcd_pro_max_2(1, 2, 3, 4, 5))
print(gcd_pro_max_2(2, 4, 6, 8, 10))
print(gcd_pro_max_2(999, 1999, 2999, 3999, 4999))
