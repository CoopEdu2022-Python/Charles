# 2.2.3 人生的不同阶段：设置变量 age 的值，编写 if-elif-else 结构，根据 age 的值判断处于人生的哪个阶段
import random
age = random.randint(1,100)
if age < 1:
    print("This random person is an infant")
elif 1 <= age <= 2:
    print("This random person is a baby")
elif 3 <= age <= 12:
    print("This random person is a child")
if 13 <= age <= 20:
    print("This random person is a teenager")
if 15 <= age <= 24:
    print("This random person is a young man")
if 18 <= age <= 64:
    print("This random person is an adult")
elif age >= 65:
    print("This random person is an old man")
print(age)
