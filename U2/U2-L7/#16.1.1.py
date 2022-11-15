class Duck:
    def quack(self):
        print("这鸭子正在嘎嘎叫")

    def feathers(self):
        print("这鸭子拥有白色和灰色的羽毛")


class Person:
    def quack(self):
        print("这人正在模仿鸭子")

    def feathers(self):
        print("这人在地上拿起1根羽毛然后给其他人看")


def in_the_forest(duck):
    duck.quack()
    duck.feathers()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


game()

"""
如果假设所有会quack和有feathers的都是duck，那么在上述代码的情况之下，person也是duck
    (这里到底指的是如果一个对象调用了和另一个对象相同的方法并且输出不同，那么这两个对象可以看作一个，
    还是指如果是一个类只包含和另一个类相同的方法但是输出不同，那这两个类可以是一个类啊？)

根据维基百科的解释，对于多态的定义的描述总结如下：
    如果假设含有某些方法的就是鸭子，那么所有只包含这些方法的其他类都可以是鸭子
"""