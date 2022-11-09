# 14.1.1  屏蔽父类方法
# People 类中包含实例方法 talk()，Infant 类继承自 People 类，但是 Infant 类的对象不应该包含 talk() 方法
# 定义 Infant 类，同时屏蔽父类的 talk() 方法

class People:
    def talk(self):
        print('Ahhhh')


class Infant(People):
    def del_method(self):
        del Infant.talk()

# 想不通了


