# 12.2.1  修改父类的稀有属性
# 为 B 类增加一个实例方法，功能是修改 A 类中的私有属性 a 的值，不要使用 _A__a 进行修改

class A:
    def __init__(self):
        self.__a = 1

    def change(self, iterated):
        self.__a = iterated
        return self.__a


class B(A):
    def __init__(self):
        print(self.change(int(input("你爱改啥改啥："))))

b = B()



