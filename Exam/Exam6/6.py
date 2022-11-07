class EasyMath:
    def __init__(self):  # 内置方法
        print(self)

    def easy_add(self, num1, num2):  # 实例方法
        print(num1 + num2)

    def easy_minus(self, num1, num2):  # 实例方法
        print(num1 - num2)

# main program starts below

math = EasyMath()
math.easy_add(1, 2)
math.easy_minus(2, 1)
