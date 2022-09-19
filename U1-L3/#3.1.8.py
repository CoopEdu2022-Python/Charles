# 3.1.8 分别计算 1 到 100 中所有奇数、偶数的和
i = 0
odd_sum = 0
even_sum = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("sum of all the odd numbers from 1 to 100 is:", odd_sum)
print("sum of all the even numbers from 1 to 100 is:", even_sum)

