def reverse_bin(n):
    n = str(bin(int(n))).removeprefix("0b")
    n = "0" * (32 - len(n)) + n
    n = "0b" + n[::-1]
    result = int(n, 2)
    return result


print(reverse_bin(4294967293))
