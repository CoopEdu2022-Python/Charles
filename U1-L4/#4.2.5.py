# 4.2.5 参考上节课练习 #3.3.2 的打印菱形，定义一个函数，能够根据不同的参数打印不同大小的菱形
def diamond():
    a = int(input("How many rows you want to print: "))
    b = "*"
    c = "*"
    d = ((a // 2) + 1) - a
    for i in range(d, abs(d)):
        b *= i
        print(b)
# 我也就这样了，还是写不下去了，今天不生气了，已经没力气了
