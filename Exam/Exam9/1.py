# 2.1  探究 finally 的执行机制
# 在 try……finally 结构中，无论 try 语句是否出现异常，finally 语句都会执行
# 在函数中，finally 的执行顺序在 return 之前还是之后？
# 设计一段代码，探究以上问题，在设计并运行代码后，用多行注释简单说明 finally 的执行机制
def explore():
    try:
        return "我是return"
    except:
        pass
    finally:
        print("我是finally")


print(explore())
# output:
# 我是finally
# 我是return
"""
看来 finally 会优先被执行
"""
