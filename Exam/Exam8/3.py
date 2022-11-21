def hamming_distance(x: int, y: int) -> int:
    x = str(bin(x)).removeprefix("0b")
    y = str(bin(y)).removeprefix("0b")
    z = abs(len(x) - len(y))
    if len(x) > len(y):
        y = "0" * z + y
        z = 1
    elif len(x) < len(y):
        x = "0" * z + x
        z = -1
    else:
        z = 0
    count = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
    return count


print(hamming_distance(3, 1))


