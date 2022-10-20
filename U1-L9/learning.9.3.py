def hanoi(n):
    if n == 1:
        return 1
    return 2 * hanoi(n - 1) + 1


n = 9
print(hanoi(n))
