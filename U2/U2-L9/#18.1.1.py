class A:
    nums_cls = 0

    def __init__(self):
        self.nums_A = 0

    @staticmethod
    def test1():
        dir_A = []
        for name in dir(A):
            if name[:2] != '__' and name[::-1][:2] != '__':
                dir_A.append(name)
        print("A: ", dir_A)

    @classmethod
    def test2(cls):
        dir_cls = []
        for name in dir(cls):
            if name[:2] != '__' and name[::-1][:2] != '__':
                dir_cls.append(name)
        print("cls: ", dir_cls)

    def test3(self):
        dir_self = []
        for name in dir(self):
            if name[:2] != '__' and name[::-1][:2] != '__':
                dir_self.append(name)
        print("self: ", dir_self)


a = A()
a.test1()
a.test2()
a.test3()

