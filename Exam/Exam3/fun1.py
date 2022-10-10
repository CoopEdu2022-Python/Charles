# 定义一个函数，找到列表中任意 3 个数的和为 0 的组合
# 函数的参数是一个整数列表 num_list，且 num_list 中至少含有 3 个整数，
# 判断列表中是否存在三个元素 x, y, z ，使得 x + y + z = 0，将所有符合要求的三元组放进列表并返回，结果不可以包含重复的三元组

def whatever(a):
    return_list = []
    for x in range(0, len(a) - 2):
        for y in range(x + 1, len(a) - 1):
            for z in range(x + 2, len(a)):
                x, y, z = a[x], a[y], a[z]
                if x + y + z == 0:
                    return_list.append(tuple(sorted((x, y, z))))

    return set(return_list)


print(whatever([-1, 0, 1, 2, -1, -4, 0, 2, 0, 4, -4, -2, -1, 2]))
