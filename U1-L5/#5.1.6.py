# 5.1.6 定义一个函数，将列表每隔一个元素就增加一个 0，将新列表作为返回值
def expand(a):
    for i in range(0, len(a)):
        if i % 2 == 0:
            a[i] = str(a[i])
            a[i] += "0"
            a[i] = int(a[i])
    return a


b = [1, "a", 2, "b", 3, "c", 4, True, 5]
expand(b)
print(b)
