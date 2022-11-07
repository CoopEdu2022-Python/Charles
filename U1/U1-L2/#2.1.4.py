# 2.1.4 猜数游戏
# 在程序中设定一个 1-100 的数
# 让用户输入一个数
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，告知用户正确答案，并显示 “猜大了” 或 “猜小了”

# 这个循环我想了好久但是写对了芜湖！
import random
computer = random.randint(1, 100)
a = int(input("Enter a number:"))
while a != computer:
    if a > computer:
        print("Too big")
        a = int(input("Enter another number:"))
    elif a < computer:
        print("Too small")
        a = int(input("Enter another number:"))
print("The number is: ", computer)
print("Your right!")
