# 1. 什么是异常？
"""
·程序在运行时，如果Python解释器遇到到一个错误，会停止程序的执行，并且提示一些错误信息，这就是异常
·程序停止执行并且提示错误信息这个动作，我们通常称之为：抛出（raise）异常
"""
# 2. 异常有哪些类型？（如何找到全部的异常类型？)
"""
for name in dir(__builtins__):
    print(name)
"""

# 3. 如何捕获异常？
try:
    num = int(input("Input an integer: "))
    result = 1 / num
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("数据类型输入错误")
except Exception as result:
    print("Unknown error %s" % result)
else:
    # 没有异常才会被执行
    pass
finally:
    # 无论是否异常都会执行
    pass


# 4. 如何抛出异常？
def demo1():
    return int(input("输入整数："))

def demo2():
    return demo1()

# 利用异常的传递性，在主程序捕获异常

try:
    print(demo2())
except Exception as result:
    print("Wrong position %s" % result)
"""

"""

# 5. 什么是异常的传递？
"""
·异常的传递--当函数/方法执行出现异常，会将异常传递给函数/方法的调用一方
·如果传递到主程序，仍然没有异常处理，程序才会被终止
提示
·在开发中，可以在主函数中增加异常捕获
·而在主函数中调用的其他函数，只要出现异常，都会传递到主函数的异常捕获中
·这样就不需要在代码中，增加大量的异常捕获，能够保证代码的整洁
"""
