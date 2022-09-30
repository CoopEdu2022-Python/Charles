# 5.1.5 定义一个函数，作用是将列表中的数字元素全部扩大两倍，其他类型保持不变，修改完成后，将新列表作为返回值
def expand(a):
    for i in range(0, len(a)):
        if type(a[i]) == float or type(a[i]) == int:
            a[i] = 2 * a[i]
    return a


b = [1, "a", 2, "b", 3, "c", 4, True, 5]
expand(b)
print(b)
