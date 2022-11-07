# 2.2.2 思考学校生活中有没有逻辑嵌套的场景，仿照 #2.2.1（变量赋值、打印等），实现代码逻辑
import random

parabola = random.randint(0, 1)
delta = random.randint(-5, 5)

if parabola:
    print("这是二次函数")

    if delta > 0:
        print("这个二次函数有两个实数根")
    elif delta == 0:
        print("这个二次函数有两个相同的实数根")
    elif delta < 0:
        print("这个二次函数没有实数根")
else:
    print("这不是二次函数")


