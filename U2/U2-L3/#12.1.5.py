class Person:
    def __init__(self, name):
        self.__name = name

    def method(self, a):
        if len(a) < 10:
            self.__name = a

# 我不知道该怎么测试，但是觉得思路貌似是ok的
