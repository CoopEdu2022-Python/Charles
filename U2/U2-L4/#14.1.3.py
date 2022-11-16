# 14.1.3  定义 Point 类和 Segment 类
# Point 类包含 2 个属性，分别为点的横坐标与纵坐标
# Segment 类包含 2 个私有属性，分别为两个端点的坐标
# Segment 类包含 get_len() 方法，可以获得直线的长度
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.__left_point = Point(x1, y1)
        self.__right_point = Point(x2, y2)

    def get_len(self, x1, x2, y1, y2):
        x1, x2 = self.__left_point.x, self.__right_point.x
        y1, y2 = self.__left_point.y, self.__right_point.y
        return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)

