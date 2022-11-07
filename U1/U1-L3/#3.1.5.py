# 3.1.5 猜数游戏 v2.1
# 在程序中设定一个 1-100 的数
# 让用户输入一个数，用户可以一直猜，直到猜对为止
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，告知误差范围：如果误差超过 50，打印 '离谱'；误差超过 30，打印 'nonono'；误差不超过 10，打印 'close!'
"""
这个题目有个缺陷啊，就是用户不知道到底是大了还是小了，所以我把提示大小的那个保留了
还有就是这个10到30这个区间没提示啊，就很离谱
我觉得现在这个样子猜5次有很大可能性是可以猜对的
"""
import random
computer = random.randint(1, 100)
a = int(input("Enter a number:"))
while a != computer:
    if abs(a - computer) > 50:
        print("离谱")
    elif 30 < abs(a - computer) < 50:
        print("nonono")
    elif abs(a - computer) <= 10:
        print("close")
    if a > computer:
        print("Too big")
        a = int(input("Enter another number:"))
    elif a < computer:
        print("Too small")
        a = int(input("Enter another number:"))
print("The number is: ", computer)
print("Your right!")
