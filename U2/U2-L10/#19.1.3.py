# 定义一个函数，参数为两个数字 a，b，计算 a / b 的值
# 如果 b 等于零，抛出异常
def function(a, b):
    return a / b


try:
    print(function(int(input("enter a number: ")), int(input("enter a number: "))))
except ZeroDivisionError:
    print("b cannot be 0")
