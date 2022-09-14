# 1. 输入用户年龄
age = int(input("今年多大了？"))

# 2. 判断是否满 18 岁
# if 语句以及缩进部分的代码是一个完整的语法块
if age >= 18:
    print("可以进网吧嗨皮……")
else:
    print("你还没长大，应该回家写作业！")

# 3. 思考！- 无论条件是否满足都会执行
print("这句代码什么时候执行?")    # 用户输入的年龄小于18的时候运行

# 练习1: 定义一个整数变量 age，编写代码判断年龄是否正确
age = 100

# 要求人的年龄在 0-120 之间
if age >= 0 and age <= 120:
    print("年龄正确")
else:
    print("年龄不正确")

# 练习2: 定义两个整数变量 python_score、c_score，编写代码判断成绩
py_score = int(input("enter your python score: "))
c_score = int(input("enter your c score: "))
if py_score > 60 or c_score > 60:
    print("合格")
else:
    print("不合格")

# 练习3: 定义一个布尔型变量 `is_employee`，编写代码判断是否是本公司员工
is_employee = False
if not is_employee:
    print("you are not allow to enter")
"""    
if 条件1:
    条件1满足执行的代码
    ……
elif 条件2:
    条件2满足时，执行的代码
    ……
elif 条件3:
    条件3满足时，执行的代码
    ……
else:
    以上条件都不满足时，执行的代码
    ……
"""
holiday_name = input("今天什么节日：")

if holiday_name == "情人节":
    print("buy some roses")
    print("watch a movie")
elif holiday_name == "平安夜":
    print("Buy some apples")
    print("and have a nice meal")
elif holiday_name == "生日":
    print("buy a birthday cake")
else:
    print("everyday is a holiday......")

"""
if 条件 1:
    条件 1 满足执行的代码
    ……
    
    if 条件 1 基础上的条件 2:
        条件 2 满足时，执行的代码
        ……    
        
    # 条件 2 不满足的处理
    else:
        条件 2 不满足时，执行的代码
        
# 条件 1 不满足的处理
else:
    条件1 不满足时，执行的代码
    ……
"""
# 一天就要预习这么多真的是折磨人
player = int(input("Enter stone(1), paper(2), scissor(3): "))
import random

computer = random.randint(1, 3)
print("The choice from the computer: ", computer)
if ((player == 1 and computer == 3) or
        (player == 2 and computer == 1) or
        (player == 3 and computer == 2)):
    print("噢耶！！！电脑弱爆了！！！")
elif player == computer:
    print("心有灵犀，再来一盘！")
else:
    print("不行，我要和你决战到天亮！")
# 这个还挺好玩的，就这了我觉得差不多了
