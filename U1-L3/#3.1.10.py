# 3.1.10 分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
a = int(input("Please enter a number: "))
b = a
i = 2
while 1:
    if i > (a / i):
        print(int(a))
        break
    if a % i == 0:
        print(i)
        a /= i
        i = 2
        continue
    i += 1

print("Number(s) above is(are) all the prime number factor(s) for %d" % b)

"""
这玩意写的我累死了， 琢磨半天才想出来。下面是一个网上的，我实在是打不出来公式的输出了，就这样吧
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

