def recursion_inverse(n):
    n = str(n)
    if len(n) == 1:
        return n
    else:
        return recursion_inverse(n[1:]) + n[0]


print(recursion_inverse(123))
