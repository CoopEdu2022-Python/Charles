# 3.2.9 for循环：质数判断：用户输入一个正整数，用程序判断是否为质数
a = int(input("Please enter a number: "))
for i in range(2, a + 1):
    b = a % i
    if a == 2:
        print("This number is both prime number and sum number")
        break
    if b == 0:
        print("This is a sum number")
        break
    else:
        print("This number is a prime number")
        break
