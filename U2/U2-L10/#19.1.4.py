# 定义一个函数，参数为半径 r，计算圆的面积
# 自定义一个异常类 RadiusError，如果半径为负值，抛出 RadiusError
import math


class RadiusError(Exception):
    pass


def area(r):
    if r < 0:
        raise RadiusError("radius less than 0")

    return math.pi * (r ** 2)


try:
    print(area(float(input("Enter the radius: "))))
except Exception as result:
    print("Radius error：%s" % result)
