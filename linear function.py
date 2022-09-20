# 输入A的坐标和B的坐标能够给出两点连线的解析式
x1, y1 = float(input("点A的x坐标是：")), float(input("点A的y坐标是："))
x2, y2 = float(input("点B的x坐标是：")), float(input("点B的y坐标是："))
k = (y2 - y1)/(x2 - x1)
b = y1 - x1 * k
if b == 0:
    print("两点连成的线的解析式是：y = %.2f * x" % k)
else:
    print("两点连成的线的解析式是：y = %.2f * x + %.2f" % (k, b))

