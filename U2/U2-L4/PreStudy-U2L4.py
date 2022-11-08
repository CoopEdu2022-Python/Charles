"""
面向对象三大特性：
1.封装 根据职责将属性和方法封装到一个抽象的类中
2.继承 实现代码的重用，相同的代码不需要重复的编写
3.多态 不同的对象调用相同的方法，产生不同的执行结果，增加代码的灵活度
"""


class Animal:

    def eat(self):
        print("Eat")

    def drink(self):
        print("Drink")

    def run(self):
        print("Run")

    def sleep(self):
        print("Sleep")


class Dog(Animal):
    # 子类拥有父类所有的属性和方法
    def bark(self):
        print("Bark")


"""
Dog 类是 Animal 类的 子类，Animal 类是 Dog 类的 父类，Dog 类从 Animal 类 继承
Dog 类是 Animal 类的 派生类，Animal 类是 Dog 类的 基类，Dog 类从 Animal 类 派生
"""


class XiaotTianQuan(Dog):
    # 子类 拥有 父类 以及 父类的父类 中封装的所有 属性 和 方法
    def fly(self):
        print("I believe I can fly!")

# 没有继承关系的不可以调用
