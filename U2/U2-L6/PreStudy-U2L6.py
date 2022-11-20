# 1. 什么是多继承？
"""
一个子类可以有多个父类，它继承了多个父类的特性。
"""

# 2. 如果子类继承自多个父类，且父类中具有相同名称的方法，子类会选择哪个父类的方法执行？


class D(object): pass
class E(object): pass
class F(object): pass
class B(D, E): pass
class C(D, F): pass
class A(B, C): pass


print(A.__mro__)  # 使用mro函数可以查看A所继承的父类的属性到底是从谁哪里来的

