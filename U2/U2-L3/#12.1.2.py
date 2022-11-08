class Base:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __str__(self):
        return 'foo'

    def __foo__(self):
        print('Base')

    def __foo(self):
        print(self)

    def test(self):
        self.__foo()  # 因为这里的私有方法没有在外面调用


s = Base()
s.test()  # 因为这个不是私有属性
# 因为 print(self 执行的是 str 的代码
# 所以结果就是 foo
