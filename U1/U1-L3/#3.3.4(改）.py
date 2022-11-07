# 3.3.4 用户输入 1 个整数，打印出这个整数的所有因数。打印后程序持续运行，而非结束
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
