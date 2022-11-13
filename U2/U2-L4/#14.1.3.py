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
        self.segment_length = (((self.__left_point.x - self.__right_point.x) ** 2) +
                               ((self.__left_point.y - self.__right_point.y) ** 2)) ** (1/2)

    def get_len(self):
        return self.segment_length

# 我知道我这样写可能让point类segment类没关系了，但是我也不知道怎么把他们俩关联起来。
