def bin_calculate(a, b):
    c = int(str(a), 2) + int(str(b), 2)
    return str(bin(c)).removeprefix("0b")


print(bin_calculate(11, 1))
