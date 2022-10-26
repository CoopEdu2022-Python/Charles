# 1. [多行注释] Python 的 self 是什么？
class Cat:
    def eat(self):
        print("%s爱吃鱼"%self.name)


"""
假设对象是 x ，由 x 调用的方法，方法内的 self 就是 x 的引用
在类封装的方法内部，self 就表示当前调用方法的对象自己
"""

tom = Cat()
tom.name = "Tom"
tom.eat()

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()


"""内部定义属性"""


class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat("Tom")
print(tom.name)
tom.eat()
Lazy_cat = Cat("大懒猫")
Lazy_cat.eat()


# 2. [多行注释] Python 类的内置方法有哪些？

def demo():
    pass


print(dir(demo()))
"""
'__bool__',         '__class__',  '__delattr__',   '__dir__',   '__doc__',           '__eq__',   '__format__', '__ge__', 
'__getattribute__', '__gt__',     '__hash__',      '__init__',  '__init_subclass__', '__le__',   '__lt__',     '__ne__', 
'__new__',          '__reduce__', '__reduce_ex__', '__repr__',  '__setattr__',      '__sizeof__',  '__str__', 
'__subclasshook__'
"""
