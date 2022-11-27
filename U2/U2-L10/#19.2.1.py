# 19.2.1  随机数
# 让用户输入 2 个整数 start 和 end，打印这两个整数之间（包含两端）的一个随机整数
# 考虑用户输入不是整数的情况，以及 start > end 的情况，抛出异常并处理
import random


def random_number(a, b):
    return random.randint(a, b)


while 1:
    try:
        a = int(input("请输入起始值: "))
        b = int(input("请输入终止值: "))
        print(random_number(a, b))
    except ValueError:
        print("不是整数，请从起始值重新输入")

