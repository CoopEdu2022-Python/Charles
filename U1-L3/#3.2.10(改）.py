# 3.2.10 for 循环：分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
a = int(input("Please enter a number: "))
print(a, end=" = ")
for i in range(2, a + 1):
    while a % i == 0:
        print(i, end="")
        a /= i
        if a != 1:
            print(" *", end=" ")

"""
n = int(input("请输入需要分解的数字："))
print("{} =".format(n), end=' ')
while n > 1:
    for i in range(2, n + 1):
        if n % i == 0:
            n = int(n / i)
            if n == 1:
                print(i)
            else:
                print("{} *".format(i), end=' ')
            break
"""






