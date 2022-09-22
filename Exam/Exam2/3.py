m = int(input("请输入一个数字："))
n = int(input("请输入另一个数字："))
i = 0
c = 0
while i < n + 1:
    a = m * (((10 ** i) - 1)/(10 - 1))
    i += 1
    c += a
print(c)
