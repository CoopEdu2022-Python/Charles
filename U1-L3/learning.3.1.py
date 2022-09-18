#  打印 5 遍 Hello Python
i = 1
while i <= 5:
    print("Hello python")
    i = i + 1
print("循环结束后的 i = %d" % i)

# 计算 0 ~ 100 之间所有数字的累计求和结果
result = 0
i = 0
while i < 100:
    i += 1
    result += i
print(result)

# 计算 0 ~ 100 之间 所有 偶数 的累计求和结果
result = 0
i = 0
while i < 100:
    i += 2
    result += i
print(result)
# 上面这些是我自己写的，我感觉比判断奇数还是偶数要好
"""下面这些是课件里面的"""
# 0. 最终结果
result = 0

# 1. 计数器
i = 0

# 2. 开始循环
while i <= 100:

    # 判断偶数
    if i % 2 == 0:
        print(i)
        result += i

    # 处理计数器
    i += 1

print("0~100之间偶数求和结果 = %d" % result)
# break 和 continue
# break
i = 0

while i < 10:

    # break 某一条件满足时，退出循环，不再执行后续重复的代码
    # i == 3
    if i == 3:
        break

    print(i)

    i += 1

print("over")

# continue

i = 0

while i < 10:

    # 当 i == 7 时，不希望执行需要重复执行的代码
    if i == 7:
        # 在使用 continue 之前，同样应该修改计数器
        # 否则会出现死循环
        i += 1

        continue

    # 重复执行的代码
    print(i)

    i += 1
"""在控制台连续输出五行 *，每一行星号的数量依次递增"""
i = 1
while i < 6:
    print("*" * i)
    i += 1

"""嵌套打小星星"""
row = 1

while row <= 5:

    # 假设 python 没有提供字符串 * 操作
    # 在循环内部，再增加一个循环，实现每一行的 星星 打印
    col = 1

    while col <= row:
        print("*", end="")

        col += 1

    # 每一行星号输出完成后，再增加一个换行
    print("")

    row += 1
"""九九乘法表"""
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (row, col, row * col), end="\t")
        col += 1
    print("")
    row += 1
