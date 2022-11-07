# 3.1.4 猜数游戏 v2.0
# 在程序中设定一个 1-100 的数
# 让用户输入一个数，最多有 5 次机会
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，显示 “猜大了” 或 “猜小了”
"""我真的很想说，这5次根本猜不中啊，您要不信您可以试一试"""
import random
computer = random.randint(1, 100)
i = 5
a = int(input("Enter a number:"))
while a != computer:
    i -= 1
    print("You have only %d more chances, keep up!" % i)
    if a > computer:
        print("Too big")
        a = int(input("Enter another number:"))
    elif a < computer:
        print("Too small")
        a = int(input("Enter another number:"))
    if a == computer:
        break
    elif i == 1:
        print("There's no more chance for you, I'm sorry that you failed:(")
        break

print("The number is: %d" % computer)
if a == computer:
    print("Your right!")
