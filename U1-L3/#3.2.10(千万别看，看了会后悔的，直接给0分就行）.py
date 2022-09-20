# 3.2.10 for 循环：分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
a = int(input("Please enter a number: "))
for i in range(2, a + 1):
    b = a % i
    n = int(a / i)
    e = i
    if b == 0:
        d = i
        if e == d:
            for j in range(2, n + 1):
                c = j % n
                if c != 0:
                    print(i)
写不出来，放弃了。 操他妈这破玩意搞我一个小时没弄出来，弄个屁啊，那么多作业
马勒戈壁别人的我又看不懂，自己写也写不出来

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





