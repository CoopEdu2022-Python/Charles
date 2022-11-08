class Test1:
    def __init__(self):
        self._n1 = 10
        self.__n2 = 10
        self.___n3 = 10

    def ____test(self):
        pass


test = Test1()
print(len(dir(test)))

# dir 函数是列出类所有的实例属性和方法，包括了私有的，所以输出还是30
