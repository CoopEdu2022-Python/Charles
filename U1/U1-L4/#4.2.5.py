# 4.2.5 参考上节课练习 #3.3.2 的打印菱形，定义一个函数，能够根据不同的参数打印不同大小的菱形
def diamond(a):
    d = ((a // 2) + 1) - a
    rhombus = ""
    for i in range(d, abs(d) + 1):
        b, c = "*", " "
        if a % 2 == 0:
            print("Nonono")
            break
        c *= abs(i)
        b *= (a - 2 * abs(i))
        rhombus += (c + b) + "\n"
    return rhombus


n = diamond(int(input("How many rows you want to print: ")))
print(n)

