for num in range(1, 1001):
    a = num
    factor = 1
    while factor < a:
        if a % factor == 0:
            num = num - factor
        factor += 1
    if num == 0:
        print(a)




