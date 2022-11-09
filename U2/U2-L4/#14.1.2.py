# 14.1.2  定义父类 User 和继承类 Vip
# User 类
# - 属性：id: str, nickname: str, credits: int
# - 方法：get_info()，打印用户的所有信息；upgrade_to_vip()，将用户修改为 Vip 类型
# Vip 类
# - 属性：父类全部属性、vip_level: int=1
# - 方法：get_info()，打印用户的所有信息

class User:
    def __init__(self, credits, id="123", nicname="hello"):
        self.id = id
        self.nicname = nicname
        self.credits = credits
        print("%s, %s, %d" % (self.id, self.nicname, self.credits))

    def get_info(self):
        return self


class Vip(User):
    def vip_level(self, level=1):
        self.vip_level()


user1 = User(6666)
print(user1.get_info())

# 写不出来了
