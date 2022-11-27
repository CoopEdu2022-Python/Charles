# 定义一个函数，函数的参数为一个字符串，获取用户的输入
# 主程序中，用户一次性输入 5 个数，以逗号分隔
# 函数需要将用户输入的数字提取出来，存入列表并返回这个列表
# 如果输入数据不为整数，要捕获产生的异常，打印 '请输入整数'
# 捕获输入参数不足 5 个或超过 5 个的异常，打印 '请输入 5 个整数'
class LengthError(Exception):
    pass


def get(*a):
    a = a[0].split(",")
    if len(a) != 5:
        # print("请输入5个整数")
        raise LengthError("请输入5个整数")
    return a


try:
    print(get(input("请输入数字： ")))
except ValueError:
    print('请输入整数')
except Exception as result:
    print("长度错误：%s" % result)
