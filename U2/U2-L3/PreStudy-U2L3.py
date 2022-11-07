class Woman:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d 岁" % (self.name, self.__age))


xiaofang = Woman("小芳")

# 私有属性在外界不能够被直接访问
# print(xiaofang.__age)
# 这样就可以访问了
print(xiaofang._Woman__age)
# 私有方法同样不能够在外界被直接访问
# xiaofang.__secret()
# 这样就可以访问了
xiaofang._Woman__secret()

# python只有伪私有属性和方法
