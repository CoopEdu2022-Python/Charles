# 定义一个函数，计算列表中任意三个数的最大乘积
# 函数的参数是一个整数列表 num_list ，且 num_list 中至少含有 3 个整数，
# 在列表中找出任意三个数的最大乘积，并返回最大乘积和包含这 3 个数的列表
def damn(a):
    result_list = []
    overall_dict = {}
    for x in range(0, len(a) - 2):
        for y in range(x + 1, len(a) - 1):
            for z in range(x + 2, len(a)):
                result_list.append(a[x] * a[y] * a[z])
                overall_dict[a[x] * a[y] * a[z]] = [a[x], a[y], a[z]]
    result_list.sort(reverse=True)
    max_value = result_list[0]
    factor = overall_dict[result_list[0]]
    return max_value, factor


print(damn([1, 5, -3, -3, 0]))

