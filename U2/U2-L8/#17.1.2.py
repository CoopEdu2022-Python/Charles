# 17.1.2  统计水果数量 2.0
# 在 17.1.1 的基础上添加一个逻辑：如果在主程序中删除了水果实例，就要修改对应的类属性 nums
# 下方为预期的运行效果
class Fruit:
    variety = 0


class Apple(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Apple.nums += 1

    def __del__(self):
        Apple.nums -= 1


class Orange(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Orange.nums += 1

    def __del__(self):
        Orange.nums -= 1


class Banana(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Banana.nums += 1

    def __del__(self):
        Banana.nums -= 1


class Pear(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Pear.nums += 1

    def __del__(self):
        Pear.nums -= 1


class Peach(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Peach.nums += 1

    def __del__(self):
        Peach.nums -= 1


