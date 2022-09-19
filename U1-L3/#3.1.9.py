# 3.1.9 质数判断：用户输入一个正整数，用程序判断是否为质数
a = int(input("Please enter a number: "))
i = 2
while a % i != 0:
    if i >= (a / i):
        print("this number is a prime number")
        break
    i += 1
if a % i == 0:
    print("this number is a sum number")
