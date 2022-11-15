# 13.1.2  定义 Exam 类和 Test 类
# Exam 类包含 4 个实例属性：id，start_time，end_time，points
# Test 类继承自 Exam 类，不同的是，Test 类不包含起始和终止时间，points 属性永远为 10


class Exam:
    def __init__(self, id, start_time, end_time):
        self.id = id
        self.points = 10
        self.start_time = start_time
        self.end_time = end_time


class Test(Exam):
    def __init__(self, id, points):
        super().__init__()
        self.id = id
        self.points = 10