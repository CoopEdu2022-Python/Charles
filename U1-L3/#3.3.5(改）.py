# 3.3.5 有 1 2 3 4 四个数字，组成互不相同且无重复数字的 3 位数，打印出所有结果
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i * 100 + j * 10 + k, end=" ")
