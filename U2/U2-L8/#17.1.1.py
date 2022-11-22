# 17.1.1  统计水果数量
# 定义水果类 Fruit，包含类属性品种 variety
# 定义 5 个品种的水果类，继承自 Fruit，包含类属性数量 nums
# 在主程序中分别为 5 种水果创建若干实例，打印水果的品种数以及各自品种的数量
class Fruit:
    variety = 0


class Apple(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Apple.nums += 1


class Orange(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Orange.nums += 1


class Banana(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Banana.nums += 1


class Pear(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Pear.nums += 1


class Peach(Fruit):
    Fruit.variety += 1
    nums = 0

    def __init__(self):
        Peach.nums += 1


apple1 = Apple()
apple2 = Apple()
banana = Banana()
peach1 = Peach()
peach2 = Peach()
peach3 = Peach()
pear = Pear()
orange1 = Orange()
orange2 = Orange()

print("Fruit: {}, Apple: {}, Banana: {}, Orange: {}, Pear: {}, Peach: {}". format
      (Fruit.variety, Apple.nums, Banana.nums, Orange.nums, Pear.nums, Peach.nums))
