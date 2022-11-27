# 19.2.2  判断用户输入
# 定义函数 float_input()，如果用户输入的是小数，返回这个小数
# 自定义异常 GetFloatError，如果用户输入的不是小数，抛出异常
# 在主程序中运行函数float_input()，并捕获异常，发生异常时打印 'not float'
class GetFloatError(Exception):
    pass


def float_input(a):
    if (0 < a.count(".") <= 1) and (a.replace(".", "").isdigit() == True):
        return a
    raise GetFloatError


try:
    print(float_input(input("请输入小数：")))
except Exception as result:
    print("not float")
