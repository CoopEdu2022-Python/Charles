# 4.3.5 改写 #4.2.5：函数内不打印菱形，将需要打印的菱形作为函数的返回值，用 2 种方式调用函数，传入不同的参数，打印 2 个不同的菱形
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


n = diamond(7)
print(n)
print(diamond(9))
