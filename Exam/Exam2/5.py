for i in range(1, 1001):
    j = 0
    while j < i:
        if j != 0:
            if i % j == 0:
                i = i - j
                if i == 0:
                    print(i)
        j += 1
