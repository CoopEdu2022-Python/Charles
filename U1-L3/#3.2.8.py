#  for循环：分别计算 1 到 100 中所有奇数、偶数的和
a = 0
b = 0
for i in range(1, 101):
    if i % 2 == 0:
        a += i
    else:
        b += i
print("sum of all the odd numbers from 1 to 100 is:", b)
print("sum of all the even numbers from 1 to 100 is:", a)
